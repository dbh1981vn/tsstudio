"""Run on PC with: python -m unittest discover -s tests -v.
Requires pip install lz4 requests cryptography. No Android SDK needed.
"""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'app/src/main/python'))
import township_studio_core as B
import android_bridge as A

SAMPLE = b'''<root>
<Global>
  <Var name="money" v="20" t="i" />
  <Var name="moneyCash" v="10" t="i" />
  <Var name="levelup" v="12" t="i" />
  <Var name="experience" v="500" t="i" />
  <Var name="sexpx" v="40" t="i" />
</Global>
<SeasonTicket premium="0" score="0" />
<BuildingsStash><Building id="5years" count="1"/></BuildingsStash>
<TownGround d="nynyyy"/>
<!-- Unicode test -->
</root>'''


def cmd(action, **kwargs):
    output = json.loads(A.command(json.dumps({'action': action, 'args': kwargs})))
    if not output['ok']:
        raise RuntimeError(output['error'])
    return output['result']


class AndroidBridgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        cmd('init', data_dir=str(self.folder))
        raw = self.folder / 'fixture.xml'
        raw.write_bytes(SAMPLE)
        cmd('import', path=str(raw), name='fixture.xml')

    def test_standalone_round_trip_and_checksum(self):
        for compressed in (True, False):
            encrypted = A.encode_standalone(SAMPLE, compress=compressed)
            self.assertEqual(encrypted[0], 0x79)
            self.assertEqual(B.decode_save(encrypted), B.canonical_xml(SAMPLE))
            self.assertLess(len(encrypted), B.MAX_CONTAINER_SIZE)
            table = B.build_hash_table(int.from_bytes(encrypted[1:4], 'little'),
                                       (int.from_bytes(encrypted[4:8], 'little') + 4) & 0xffffffff)
            payload = bytearray()
            for index in range(len(encrypted) - 8):
                val = encrypted[8 + index]
                if index: val = (val - payload[index - 1]) & 0xff
                payload.append(val ^ table[index % B.HASH_TABLE_SIZE])
            self.assertEqual(int.from_bytes(encrypted[4:6], 'little'), A._checksum(bytes(payload)))

    def test_import_encrypted_and_export(self):
        raw = A.encode_standalone(SAMPLE)
        path = self.folder / 'encoded.bin'
        path.write_bytes(raw)
        imported = cmd('import', path=str(path), name='mGameInfo.xml')
        self.assertTrue(imported['state']['encrypted_source'])
        self.assertTrue(imported['state']['can_export_template'])
        cmd('change', kind='setvar', key='money', value=777)
        self.assertEqual(cmd('state')['state']['money'], '777')
        for mode in ('xml', 'standalone', 'original'):
            output = cmd('export', mode=mode)
            data = Path(output['path']).read_bytes()
            if mode == 'original':
                self.assertEqual(data, raw)
            else:
                self.assertEqual(B.read_var(B.decode_save(data), 'money')['v'], '777')
            self.assertEqual(len(data), output['bytes'])
        # Template encoder has a fixed original size and correctly rejects expansion.
        with self.assertRaises(RuntimeError):
            cmd('export', mode='template')

    def test_changes_undo_and_reset(self):
        cmd('change', kind='setvar', key='moneyCash', value=200)
        self.assertEqual(cmd('state')['state']['moneyCash'], '200')
        cmd('undo')
        self.assertEqual(cmd('state')['state']['moneyCash'], '10')
        cmd('change', kind='setvar', key='moneyCash', value=300)
        cmd('reset')
        self.assertEqual(cmd('state')['state']['moneyCash'], '10')
        self.assertFalse(cmd('state')['state']['dirty'])

    def test_avatar_and_decorations(self):
        ids = [i['id'] for i in cmd('catalog', kind='avatars')['items']]
        self.assertIn('1', ids)
        cmd('change', kind='avatars', enable=['1','3'], disable=[])
        states = {i['id']: i for i in cmd('catalog', kind='avatars')['items']}
        self.assertTrue(states['1']['checked'])
        cmd('change', kind='avatars', enable=[], disable=['1'])
        states = {i['id']: i for i in cmd('catalog', kind='avatars')['items']}
        self.assertFalse(states['1']['checked'])
        dec = cmd('catalog', kind='decoration', group='normal')['items']
        self.assertTrue(dec)
        key = dec[0]['id']
        cmd('change', kind='decoration', ids=[key], count=3)
        self.assertEqual(B.decoration_inventory(A._CURRENT)[key], 3)

    def test_profile_and_standalone(self):
        cmd('change', kind='level', value=15)
        self.assertEqual(cmd('state')['state']['level'], 15)
        cmd('change', kind='pass')
        self.assertIn(b'premium="1"', A._CURRENT)
        self.assertEqual(B.decode_save(Path(cmd('export', mode='standalone')['path']).read_bytes()), A._CURRENT)

    def test_backup_restore_and_input_safety(self):
        hist = cmd('history')['items']
        self.assertTrue(hist)
        cmd('change', kind='setvar', key='money', value=999)
        restored = cmd('restore', name=hist[0]['name'])
        self.assertEqual(restored['state']['money'], '20')
        self.assertFalse(restored['state']['dirty'])
        outside = self.folder.parent / 'outside.xml'
        with self.assertRaises(RuntimeError):
            cmd('import', path=str(outside), name='outside.xml')
        with self.assertRaises(RuntimeError):
            cmd('restore', name='../traversal')
        with self.assertRaises(RuntimeError):
            cmd('change', kind='setvar', key='token', value=1)

    def test_no_write_on_invalid_save(self):
        for bad in [b'not xml', b'\x79\x00\x00', b'<root><unterminated></root>']:
            path = self.folder / 'bad.bin'
            path.write_bytes(bad)
            with self.assertRaises(RuntimeError):
                cmd('import', path=str(path), name='bad.bin')
        self.assertEqual(cmd('state')['state']['money'], '20')


    def test_academy_barn_land_museum(self):
        factory = next(iter(B.TSVIP_ACADEMY['Factory']))
        r = cmd('change', kind='academy', group='Factory', ids=[factory], bonuses={'timeBonus':100})
        self.assertTrue(r['changed'])
        cmd('change', kind='barnlevel', level=20)
        self.assertIn(b'WareHouseCashUpgrade', A._CURRENT)
        cmd('change', kind='barnproducts', ids=['wheat','corn'], count=100)
        self.assertIn(b'wheatCounter', A._CURRENT)
        land = cmd('change', kind='land')
        self.assertEqual(land['report']['cells'], 2)
        museum = cmd('change', kind='museum')
        self.assertTrue(museum['changed'])
        B.validate_xml_document(A._CURRENT, 'after multi-edit')

    def test_codec_corruption_and_no_template(self):
        with self.assertRaises(RuntimeError):
            cmd('export', mode='template')
        encoded = A.encode_standalone(SAMPLE)
        wrong = bytearray(encoded)
        wrong[0] = 0x19
        with self.assertRaises(B.SaveToolError):
            B.decode_save(bytes(wrong))

    def test_invalid_type_and_generic_var(self):
        cmd('change', kind='genericvar', key='money', value='35')
        self.assertEqual(cmd('state')['state']['money'], '35')
        with self.assertRaises(RuntimeError):
            cmd('change', kind='genericvar', key='nonexistent', value='7')
        with self.assertRaises(RuntimeError):
            cmd('change', kind='setvar', key='money', value=-123)
        with self.assertRaises(RuntimeError):
            cmd('change', kind='level', value=-123)


if __name__ == '__main__': unittest.main()
