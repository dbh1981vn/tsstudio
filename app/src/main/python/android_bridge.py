"""Android-safe TS Studio core adapter. No Qt or external ADB process.

This adapter makes *selected* engine functions available to Android UI. Core's
Windows-oriented CLI/ADB functions are retained for audit but NEVER invoked.
Only Python engine functions which operate on in-memory XML bytes are called.
"""
from __future__ import annotations

import json
import os
import re
import secrets
import struct
import hashlib
import time
from pathlib import Path

import township_studio_core as B

_CURRENT: bytes | None = None
_ORIGINAL: bytes | None = None
_CONTAINER: bytes | None = None
_FILE_NAME = ""
_HISTORY: list[bytes] = []
_DATA_DIR: Path | None = None
_ORIGIN: str = ""


def _require() -> bytes:
    if _CURRENT is None:
        raise B.SaveToolError("Chưa nhập save. Chọn Mở file trước.")
    return _CURRENT


def _safe_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", (name or 'save'))[:96] or 'save'


def _summary() -> dict:
    if _CURRENT is None:
        return {"loaded": False, "dirty": False, "name": "", "size": 0}
    result = {
        "loaded": True, "dirty": _CURRENT != _ORIGINAL,
        "name": _FILE_NAME, "size": len(_CURRENT),
        "sha256": hashlib.sha256(_CURRENT).hexdigest()[:12],
        "encrypted_source": bool(_CONTAINER is not None and _CONTAINER[:1] == b'\x79'),
        "origin": _ORIGIN,
        "undo_available": bool(_HISTORY),
        "can_export_template": bool(_CONTAINER and _CONTAINER[:1] == b'\x79'),
    }
    for key in ("money", "moneyCash", "gameStartDate"):
        try:
            attrs = B.read_var(_CURRENT, key)
            result[key] = attrs.get("v", attrs.get("value", ""))
        except Exception:
            result[key] = None
    try:
        result["level"] = B.read_township_level(_CURRENT)
    except Exception:
        result["level"] = None
    return result


def _commit(value: bytes, details: object) -> dict:
    global _CURRENT
    old = _require()
    value = B.canonical_xml(value)
    B.validate_xml_document(value, "Sau chỉnh sửa")
    if value != old:
        _HISTORY.append(old)
        if len(_HISTORY) > 3:
            del _HISTORY[0]
        _CURRENT = value
    return {"changed": value != old, "report": details, "state": _summary()}


def _checksum(payload: bytes) -> int:
    # TSVIP v1.39: running sums in unsigned 32-bit, not Adler-32 modulo 65521.
    first = 1
    second = 0
    for x in payload:
        first = (first + x) & 0xFFFFFFFF
        second = (second + first) & 0xFFFFFFFF
    return (((first | ((second << 16) & 0xFFFFFFFF)) >> 16) ^ (first & 0xFFFF)) & 0xFFFF


def encode_standalone(xml_input: bytes, compress: bool = True) -> bytes:
    """Direct port of TS_Studio_v1.39.gui_encode_xml_standalone."""
    B.validate_xml_document(xml_input, "Encode")
    xml = B.canonical_xml(xml_input)
    raw = xml + b"\x00"
    if len(raw) > B.MAX_XML_SIZE:
        raise B.SaveToolError("XML vượt giới hạn 32 MB")
    payload = (B.LZ4_MAGIC + struct.pack('<I', len(raw)) +
               B.lz4.block.compress(raw, mode='default', store_size=False)) if compress else raw
    total = len(payload) + B.HEADER_SIZE
    header = (len(payload) ^ B.PAYLOAD_XOR) + (total ^ B.HEADER_XOR)
    if header > 0xFFFFFF:
        raise B.SaveToolError("Header vượt giới hạn 24-bit")
    seed = ((secrets.randbelow(65535) + 1) << 16) | _checksum(payload)
    table = B.build_hash_table(header, (seed + 4) & 0xFFFFFFFF)
    output = bytearray(total)
    output[0] = B.FORMAT_79
    output[1:4] = header.to_bytes(3, 'little')
    output[4:8] = struct.pack('<I', seed)
    previous = 0
    for index, value in enumerate(payload):
        output[B.HEADER_SIZE + index] = ((value ^ table[index % B.HASH_TABLE_SIZE]) + previous) & 0xFF
        previous = value
    result = bytes(output)
    if B.decode_save(result) != xml:
        raise B.SaveToolError("Kiểm tra Encode/Decode không khớp")
    return result


def _set_change(action: str, p: dict) -> dict:
    xml = _require()
    if action == 'setvar':
        key = str(p['key'])
        if key not in ('money', 'moneyCash'):
            raise B.SaveToolError('Chỉ cho sửa money / moneyCash tại form này')
        value = int(p['value'])
        updated, report = B.set_integer_var(xml, key, value)
    elif action == 'level':
        value = int(p['value'])
        updated, report = B.set_township_level(xml, value, allow_decrease=True)
        report = {"changes": report, "warning": "Mới sửa mGameInfo trong phiên; LocalInfo chưa đồng bộ."}
    elif action == 'startmonth':
        updated, report = B.set_game_start_month(xml, int(p['year']), int(p['month']))
    elif action == 'decoration':
        updated, report = B.set_decorations(xml, [str(i) for i in p['ids']], int(p['count']))
    elif action == 'avatars':
        updated = xml
        reports = []
        for value, ids in ((True, p.get('enable', [])), (False, p.get('disable', []))):
            if ids:
                updated, changes = B.set_avatar_unlocks(updated, ids, value)
                reports.append(changes)
        report = reports
    elif action == 'barnlevel':
        level = int(p['level'])
        updated = B.set_barn_level(xml, level)
        report = {"barn_level": level, "capacity": B.barn_capacity(level)}
    elif action == 'barnproducts':
        updated = B.set_barn_products(xml, p['ids'], int(p['count']))
        report = {"selected": len(p['ids']), "count": int(p['count'])}
    elif action == 'pass':
        updated, report = B.unlock_golden_pass(xml)
    elif action == 'land':
        updated, report = B.unlock_land(xml)
    elif action == 'museum':
        updated, report = B.unlock_museum(xml)
    elif action == 'academy':
        updated = B.set_academy(xml, p['group'], p['ids'], p.get('bonuses', {}))
        report = {"group": p['group'], "count": len(p['ids'])}
    elif action == 'genericvar':
        key = str(p['key'])
        if not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9.:-]{0,127}', key):
            raise B.SaveToolError('Tên Var không hợp lệ')
        if re.search(r'(city.?id|game.?id|token|auth|device|ssaid|secret|password|account.?id|player.?id)', key, re.I):
            raise B.SaveToolError('Không cho sửa định danh / token bằng công cụ Var tổng quát')
        attrs = B.read_var(xml, key)
        if not attrs:
            raise B.SaveToolError('Var không tồn tại, không tự tạo Var mới')
        updated, report = B.patch_var(xml, key, {'v': str(p['value'])})
    else:
        raise B.SaveToolError('Chức năng chưa được tích hợp: ' + action)
    return _commit(updated, report)


def _catalog(kind: str, extra: dict) -> dict:
    xml = _require()
    if kind == 'decoration':
        inventory = B.decoration_inventory(xml)
        group = extra.get('group', 'normal')
        if group not in B.DECORATION_GROUPS:
            raise B.SaveToolError('Nhóm Decoration không hợp lệ')
        return {"items": [{"id": str(i), "count": inventory.get(str(i), 0)} for i in B.DECORATION_GROUPS[group]]}
    if kind == 'avatars':
        states = B.avatar_states(xml)
        return {"items": [{"id": i, "checked": data['state'] is True,
                           "unknown": data['state'] not in (True, False, None)}
                          for i, data in states.items() if data['catalog']]}
    if kind == 'barn':
        return {"items": [{"id": v} for v in B.TSVIP_BARN_PRODUCTS]}
    if kind == 'academy':
        group = extra.get('group', 'Industry')
        if group not in B.TSVIP_ACADEMY:
            raise B.SaveToolError('Nhóm Academy không hợp lệ')
        return {"items": [{"id": v} for v in B.TSVIP_ACADEMY[group]]}
    if kind == 'vars':
        import xml.etree.ElementTree as ET
        root = B.validate_xml_document(xml, 'Browse Vars')
        items = []
        visited = set()
        for node in root.iter('Var'):
            key = node.get('name', '')
            if key and key not in visited and len(items) < 4000:
                visited.add(key)
                items.append({'id': key, 'value': node.get('v', node.get('value', ''))})
        return {"items": items}
    raise B.SaveToolError('Danh mục chưa hỗ trợ: ' + kind)


def _backup_original() -> str:
    if _DATA_DIR is None or _CONTAINER is None:
        return ''
    folder = _DATA_DIR / 'backups'
    folder.mkdir(parents=True, exist_ok=True)
    name = f"{time.strftime('%Y%m%d_%H%M%S')}_{secrets.token_hex(3)}_{_safe_name(_FILE_NAME)}"
    B.atomic_write(folder / name, _CONTAINER)
    return name


def command(serialized: str) -> str:
    """One UTF-8 JSON request -> one UTF-8 JSON response."""
    global _CURRENT, _ORIGINAL, _CONTAINER, _FILE_NAME, _DATA_DIR, _ORIGIN
    try:
        request = json.loads(serialized)
        action = request.get('action')
        p = request.get('args') or {}
        if action == 'init':
            _DATA_DIR = Path(str(p['data_dir'])).resolve()
            _DATA_DIR.mkdir(parents=True, exist_ok=True)
            result = {'state': _summary(), 'version': '2.0.0-alpha1'}
        elif action == 'state':
            result = {'state': _summary()}
        elif action == 'import':
            path = Path(str(p['path'])).resolve()
            if _DATA_DIR is None or not path.is_relative_to(_DATA_DIR):
                raise B.SaveToolError('Input phải nằm trong không gian riêng của ứng dụng')
            if path.stat().st_size > B.MAX_CONTAINER_SIZE:
                raise B.SaveToolError('File vượt giới hạn 64 MB')
            raw = path.read_bytes()
            decoded = B.decode_save(raw)
            B.validate_xml_document(decoded, 'Import Township XML')
            _CONTAINER = raw
            _ORIGINAL = B.canonical_xml(decoded)
            _CURRENT = _ORIGINAL
            _FILE_NAME = str(p.get('name') or path.name)
            _ORIGIN = str(p.get('origin') or 'file')
            _HISTORY.clear()
            _backup_original()
            result = {'state': _summary(), 'message': 'Đã nhập, giải mã và kiểm tra XML'}
        elif action == 'change':
            result = _set_change(str(p.get('kind', '')), p)
        elif action == 'catalog':
            result = _catalog(str(p.get('kind', '')), p)
        elif action == 'undo':
            if not _HISTORY:
                raise B.SaveToolError('Không có bước để hoàn tác')
            _CURRENT = _HISTORY.pop()
            result = {'state': _summary()}
        elif action == 'reset':
            _require()
            _CURRENT = _ORIGINAL
            _HISTORY.clear()
            result = {'state': _summary()}
        elif action == 'export':
            xml = _require()
            mode = str(p.get('mode', 'xml'))
            if mode == 'xml':
                content, name = xml, 'mGameInfo_edited.xml'
            elif mode == 'standalone':
                content, name = encode_standalone(xml), 'mGameInfo_encoded.xml'
            elif mode == 'template':
                if not _CONTAINER or _CONTAINER[:1] != b'\x79':
                    raise B.SaveToolError('Cần container gốc 0x79 mới dùng được chế độ Template')
                content, name = B.encode_save(xml, _CONTAINER), 'mGameInfo_template_encoded.xml'
                if B.decode_save(content) != xml:
                    raise B.SaveToolError('Template Encode không đạt kiểm tra decode')
            elif mode == 'original':
                content, name = _CONTAINER, _safe_name(_FILE_NAME)
            else:
                raise B.SaveToolError('Chế độ Export không hợp lệ')
            if content is None:
                raise B.SaveToolError('Không có file gốc')
            assert _DATA_DIR is not None
            target = _DATA_DIR / 'pending_export.bin'
            B.atomic_write(target, content)
            result = {'path': str(target), 'filename': name,
                      'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest()}
        elif action == 'history':
            folder = _DATA_DIR / 'backups' if _DATA_DIR else Path('/nonexistent')
            entries = sorted(folder.iterdir(), reverse=True)[:40] if folder.exists() else []
            result = {'items': [{'name': entry.name, 'size': entry.stat().st_size}
                                for entry in entries if entry.is_file()]}
        elif action == 'restore':
            assert _DATA_DIR is not None
            name = str(p.get('name', ''))
            if not name or name in ('.', '..') or name != _safe_name(name):
                raise B.SaveToolError('Tên backup không hợp lệ')
            path = _DATA_DIR / 'backups' / name
            raw = path.read_bytes()
            xml = B.decode_save(raw)
            B.validate_xml_document(xml, 'Backup')
            _CONTAINER, _ORIGINAL = raw, B.canonical_xml(xml)
            _CURRENT, _FILE_NAME, _ORIGIN = _ORIGINAL, name, 'backup'
            _HISTORY.clear()
            result = {'state': _summary(), 'message': 'Đã mở backup trong phiên; chưa ghi vào game'}
        else:
            raise B.SaveToolError('Lệnh chưa hỗ trợ: ' + str(action))
        return json.dumps({'ok': True, 'result': result}, ensure_ascii=False)
    except Exception as exc:
        return json.dumps({'ok': False, 'error': f'{type(exc).__name__}: {exc}'}, ensure_ascii=False)
