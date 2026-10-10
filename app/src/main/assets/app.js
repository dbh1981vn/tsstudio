'use strict';

const $ = selector => document.querySelector(selector);
const $$ = selector => [...document.querySelectorAll(selector)];
let requestNo = 0;
const requests = new Map();
let state = {loaded:false};
let active = 'home';
let allCatalogs = {};
let editedAvatars = new Map();
const selections = new Map();
let toastTimer;
let currentItems = [];

window.TSCallback = (id, data) => {
  const item = requests.get(id);
  if (!item) return;
  requests.delete(id);
  if (data && data.ok) item.resolve(data.result);
  else item.reject(new Error((data && data.error) || 'Lỗi không xác định'));
};

function bridge(action, args = {}) {
  return new Promise((resolve, reject) => {
    if (!window.TSNative || !TSNative.invoke) {
      reject(new Error('Cần chạy bằng APK Android để xử lý file và Python backend.'));
      return;
    }
    const id = ++requestNo;
    requests.set(id, {resolve, reject});
    try { TSNative.invoke(id, action, JSON.stringify(args)); }
    catch (e) { requests.delete(id); reject(e); }
  });
}

function toast(message, isError = false) {
  const el = $('#toast');
  el.textContent = message;
  el.classList.toggle('error', isError);
  el.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.remove('show'), 4300);
}
function log(message, level = 'info') {
  const time = new Date().toLocaleTimeString('vi-VN');
  const text = `[${time}] [${level.toUpperCase()}] ${message}`;
  const lines = ($('#activityLog').textContent + '\n' + text).split('\n');
  $('#activityLog').textContent = lines.slice(-180).join('\n');
  $('#activityLog').scrollTop = $('#activityLog').scrollHeight;
}
async function work(operation, msg) {
  $('#busy').classList.remove('hidden');
  try {
    const value = await operation();
    if (msg) { toast(msg); log(msg); }
    return value;
  } catch (e) {
    toast(e.message || String(e), true);
    log(e.message || String(e), 'error');
    return null;
  } finally {
    $('#busy').classList.add('hidden');
  }
}
function fmt(v) { return v === null || v === undefined || v === '' ? '—' : String(v).replace(/\B(?=(\d{3})+(?!\d))/g, ','); }
function applyState(updated) {
  if (!updated) return;
  state = updated;
  $('#workspaceStrip').classList.toggle('loaded', !!state.loaded);
  $('#workspaceStrip').classList.toggle('modified', !!state.dirty);
  $('#fileName').textContent = state.loaded ? state.name : 'Chưa mở file save';
  $('#fileMeta').textContent = state.loaded
    ? `${fmt(state.size)} byte XML · SHA ${state.sha256} · ${state.origin}`
    : 'Mở mGameInfo.xml hoặc container 0x79 để bắt đầu';
  $('#dirtyState').textContent = state.dirty ? 'CHƯA XUẤT' : state.loaded ? 'ĐÃ ĐỌC' : 'SẴN SÀNG';
  $('#statCoins').textContent = fmt(state.money);
  $('#statCash').textContent = fmt(state.moneyCash);
  $('#statLevel').textContent = fmt(state.level);
  const advanced = {vM3:'m3level',vFirst:'firstwin',vLives:'lives',vMine:'minedepth'};
  for (const [id,key] of Object.entries(advanced)) {
    const el = $('#' + id);
    if (el && state[key] !== null && state[key] !== undefined) el.value = state[key];
  }
  for (const [id,key] of Object.entries({vHelp:'help',vCard:'card',vRegata:'regata',vEnergy:'energy'})) {
    const vals = state[key];
    const value = vals && Object.values(vals).find(v=>v !== null && v !== undefined);
    if (value !== undefined) $('#' + id).value = value;
  }
  for (const field of ['money','moneyCash','level']) {
    const input = $('#' + field);
    if (input && state[field] !== null && state[field] !== undefined) input.value = state[field];
  }
}
function requireFile() {
  if (!state.loaded) { toast('Bạn cần mở file save trước.', true); return false; }
  return true;
}
async function setPage(page) {
  active = page;
  $$('.page').forEach(v => v.classList.toggle('active', v.id === 'page-' + page));
  $$('.nav').forEach(v => v.classList.toggle('active', v.dataset.page === page));
  if (page === 'log' || page === 'home') return;
  if (page === 'history') { await loadHistory(); return; }
  if (!requireFile()) return;
  if (page === 'decor') await getCatalog('decoration', {group:$('#decorGroup').value});
  if (page === 'avatar') await getCatalog('avatars', {});
  if (page === 'barn') await getCatalog('barn', {});
  if (page === 'academy') await getCatalog('academy', {group:$('#academyGroup').value});
  if (page === 'tools') await getCatalog('vars', {});
}
async function getCatalog(kind, opts = {}) {
  if (!state.loaded) return;
  const key = kind + ':' + (opts.group || '');
  const answer = await work(() => bridge('catalog', {kind, ...opts}));
  if (!answer) return;
  allCatalogs[key] = answer.items;
  if (kind === 'decoration') renderList('decorList', answer.items, 'decorSearch', 'decoration');
  if (kind === 'avatars') {
    renderList('avatarList', answer.items, 'avatarSearch', 'avatars');
  }
  if (kind === 'barn') renderList('barnList', answer.items, 'barnSearch', 'barn');
  if (kind === 'academy') renderList('academyList', answer.items, 'academySearch', 'academy');
  if (kind === 'vars') renderList('varsList', answer.items, 'varSearch', 'vars');
}
function renderList(containerId, items, filterId, kind) {
  const wrapper = $('#' + containerId);
  const search = ($('#' + filterId)?.value || '').trim().toLowerCase();
  const group = kind === 'decoration' ? $('#decorGroup').value : kind === 'academy' ? $('#academyGroup').value : '';
  const selectionKey = kind + ':' + group;
  const storedSelection = selections.get(selectionKey) || new Set();
  if (!selections.has(selectionKey)) selections.set(selectionKey, storedSelection);
  const filtered = items.filter(item => item.id.toLowerCase().includes(search));
  const visible = filtered.slice(0, 220);
  wrapper.replaceChildren();
  const frag = document.createDocumentFragment();
  for (const item of visible) {
    const label = document.createElement('label');
    label.className = 'item';
    const input = document.createElement('input');
    input.type = (kind === 'vars') ? 'radio' : 'checkbox';
    input.dataset.id = item.id;
    if (kind === 'avatars') {
      input.checked = editedAvatars.has(item.id) ? editedAvatars.get(item.id) : item.checked;
      input.disabled = item.unknown;
      input.addEventListener('change', () => {
        editedAvatars.set(item.id, input.checked);
        label.classList.add('edited');
        updateCounter();
      });
      if (editedAvatars.has(item.id)) label.classList.add('edited');
    } else if (kind === 'vars') {
      input.addEventListener('change', () => {
        $('#varKey').value = item.id;
        $('#varValue').value = item.value;
      });
    } else {
      input.checked = storedSelection.has(item.id);
      input.addEventListener('change', () => {
        if (input.checked) storedSelection.add(item.id); else storedSelection.delete(item.id);
      });
    }
    const span = document.createElement('span');
    span.textContent = item.id;
    span.title = item.id;
    label.append(input, span);
    if (kind === 'decoration' && item.count > 0) {
      const count = document.createElement('small');
      count.textContent = '×' + item.count;
      label.append(count);
    }
    frag.append(label);
  }
  wrapper.appendChild(frag);
  if (!visible.length) wrapper.textContent = 'Không có mục phù hợp.';
  if (filtered.length > visible.length) {
    const hint = document.createElement('p'); hint.className = 'muted';
    hint.textContent = `Đang hiển thị ${visible.length}/${filtered.length} mục. Hãy tìm theo tên để xem các mục khác.`;
    wrapper.appendChild(hint);
  }
  if (kind === 'decoration') $('#decorCounter').textContent = filtered.length + ' mục';
  if (kind === 'avatars') updateCounter();
}
function updateCounter() {
  $('#avatarCounter').textContent = `${editedAvatars.size} thay đổi`;
}
function selected(kind) {
  const group = kind === 'decoration' ? $('#decorGroup').value : kind === 'academy' ? $('#academyGroup').value : '';
  return [...(selections.get(kind + ':' + group) || new Set())];
}
async function applyChange(kind, args, confirmation) {
  if (!requireFile()) return;
  if (confirmation && !confirm(confirmation)) return;
  const answer = await work(() => bridge('change', {kind, ...args}));
  if (!answer) return;
  applyState(answer.state);
  const report = typeof answer.report === 'string' ? answer.report : JSON.stringify(answer.report);
  const message = answer.changed ? `Đã áp dụng ${kind}.` : `${kind}: không có dữ liệu thay đổi.`;
  log(message + ' ' + String(report || '').slice(0, 600));
  toast(message);
  if (kind === 'decoration') {selections.delete('decoration:' + $('#decorGroup').value);await getCatalog('decoration', {group:$('#decorGroup').value});}
  if (kind === 'avatars') {editedAvatars.clear();await getCatalog('avatars', {});}
  if (kind === 'barnproducts') {selections.delete('barn:');await getCatalog('barn', {});}
  if (kind === 'academy') {selections.delete('academy:' + $('#academyGroup').value);await getCatalog('academy', {group:$('#academyGroup').value});}
  if (kind === 'genericvar') await getCatalog('vars', {});
}
async function exportFile(mode) {
  if (!requireFile()) return;
  const answer = await work(() => bridge('exportFile', {mode}));
  if (answer) { toast('Đã lưu file vào vị trí chọn.'); log(`Xuất ${mode} thành công (${fmt(answer.size)} byte)`); }
}
async function openFile() {
  const answer = await work(() => bridge('selectInput'));
  if (answer) {
    applyState(answer.state);
    allCatalogs = {};
    editedAvatars.clear();
    selections.clear();
    log('Đã nhập và decode: ' + answer.state.name);
    toast('Đã đọc file save.');
  }
}
async function openRoot() {
  const choice = prompt('LDPlayer ROOT: Nhập 1 để đọc Township VN, 2 để đọc Township quốc tế. Chỉ đọc, không ghi game.', '1');
  if (choice === null) return;
  if (choice !== '1' && choice !== '2') {toast('Lựa chọn không hợp lệ', true); return;}
  const packageName = choice === '1' ? 'com.playrix.township.vn' : 'com.playrix.township';
  const answer = await work(() => bridge('importRoot', {package: packageName}));
  if (answer) { applyState(answer.state); toast('Đã đọc ROOT, chưa ghi vào trò chơi.'); log('ROOT READ: ' + packageName); }
}
async function loadHistory() {
  const result = await work(() => bridge('history'));
  if (!result) return;
  const parent = $('#historyList');
  parent.replaceChildren();
  if (!result.items.length) { parent.textContent = 'Chưa có backup trong bộ nhớ ứng dụng.'; return; }
  for (const item of result.items) {
    const row = document.createElement('div'); row.className = 'history-item';
    const div = document.createElement('div'); div.textContent = `${item.name} · ${fmt(item.size)} bytes`; div.title = item.name;
    const btn = document.createElement('button'); btn.className = 'btn secondary'; btn.textContent = 'Mở lại';
    btn.addEventListener('click', async () => {
      if (!confirm('Mở backup này? Các thay đổi chưa xuất hiện tại sẽ bị bỏ.')) return;
      const result = await work(() => bridge('restore', {name:item.name}));
      if (result) {applyState(result.state);toast('Đã mở bản backup trong phiên.');log('Restore workspace: ' + item.name);}
    });
    row.append(div, btn); parent.append(row);
  }
}

const commands = {
 'open': openFile,
 'root': openRoot,
 'export-xml': () => exportFile('xml'),
 'export-standalone': () => exportFile('standalone'),
 'export-template': () => exportFile('template'),
 'export-original': () => exportFile('original'),
 'undo': async () => { if (!requireFile())return;const r=await work(()=>bridge('undo'));if(r){applyState(r.state);toast('Đã hoàn tác.');log('Undo');}},
 'reset': async () => {if(!requireFile()||!confirm('Quay về XML đã nhập? Mọi chỉnh sửa chưa xuất sẽ bị bỏ.'))return;const r=await work(()=>bridge('reset'));if(r){applyState(r.state);toast('Đã đặt lại về bản gốc.');log('Reset workspace');}},
 'set-m3':()=>applyChange('m3level',{value:$('#vM3').value}),
 'set-first':()=>applyChange('firstwin',{value:$('#vFirst').value}),
 'set-lives':()=>applyChange('lives',{value:$('#vLives').value}),
 'set-help':()=>applyChange('help',{value:$('#vHelp').value}),
 'set-card':()=>applyChange('card',{value:$('#vCard').value}),
 'set-regata':()=>applyChange('regata',{value:$('#vRegata').value}),
 'set-energy':()=>applyChange('energy',{value:$('#vEnergy').value}),
 'set-mine':()=>applyChange('minedepth',{value:$('#vMine').value}),
 'set-tasks':()=>applyChange('regattatasks',{value:$('#vTasks').value}),
 'set-market':()=>applyChange('market',{value:$('#vMarket').value}),
 'all-cards':()=>applyChange('allcards',{},'Cập nhật tất cả thẻ trong save?'),
 'my-cards':()=>applyChange('mycards',{},'Cập nhật thẻ đang sở hữu?'),
 'set-money':()=>applyChange('setvar',{key:'money',value:$('#money').value}),
 'set-cash':()=>applyChange('setvar',{key:'moneyCash',value:$('#moneyCash').value}),
 'set-level':()=>applyChange('level',{value:$('#level').value},'Chỉ thay Level/XP của mGameInfo, chưa đồng bộ LocalInfo. Tiếp tục?'),
 'set-start':()=>applyChange('startmonth',{year:$('#startYear').value,month:$('#startMonth').value}),
 'select-visible-decor':()=>{const group=$('#decorGroup').value;const key='decoration:'+group;const set=selections.get(key)||new Set();$$('#decorList input[type=checkbox]').forEach(v=>{v.checked=true;set.add(v.dataset.id);});selections.set(key,set);},
 'apply-decor':()=>applyChange('decoration',{ids:selected('decoration'),count:$('#decorCount').value}),
 'apply-avatar':()=>{
   const enable=[],disable=[];
   for(const [id,enabled] of editedAvatars.entries())(enabled?enable:disable).push(id);
   if(!enable.length&&!disable.length){toast('Chưa thay đổi trạng thái avatar nào.',true);return;}
   return applyChange('avatars',{enable,disable});
 },
 'apply-barn-level':()=>applyChange('barnlevel',{level:$('#barnLevel').value}),
 'apply-barn-products':()=>applyChange('barnproducts',{ids:selected('barn'),count:$('#barnCount').value}),
 'apply-academy':()=>applyChange('academy',{group:$('#academyGroup').value,ids:selected('academy'),bonuses:{timeBonus:Number($('#academyTime').value)}}),
 'apply-pass':()=>applyChange('pass',{},'Mở Golden Pass trong XML làm việc?'),
 'apply-land':()=>applyChange('land',{},'Mở Land trong XML làm việc?'),
 'apply-museum':()=>applyChange('museum',{},'Mở Museum trong XML làm việc?'),
 'set-generic':()=>applyChange('genericvar',{key:$('#varKey').value,value:$('#varValue').value}),
 'reload-history':loadHistory,
 'clear-log':()=>{$('#activityLog').textContent='TS Studio Android · Nhật ký phiên làm việc\n';},
};

document.addEventListener('click', event => {
  const nav = event.target.closest('[data-page]');
  if (nav) { setPage(nav.dataset.page); return; }
  const button = event.target.closest('[data-command]');
  if (button && commands[button.dataset.command]) commands[button.dataset.command]();
});
for (const [field, kind, key] of [
 ['decorSearch','decoration','normal'], ['avatarSearch','avatars',''],
 ['barnSearch','barn',''], ['academySearch','academy','Factory'],
 ['varSearch','vars','']
]) {
  $('#' + field).addEventListener('input', () => {
    const group = kind === 'decoration' ? $('#decorGroup').value : kind === 'academy' ? $('#academyGroup').value : '';
    const items = allCatalogs[kind + ':' + group];
    if (items) renderList(({decoration:'decorList',avatars:'avatarList',barn:'barnList',academy:'academyList',vars:'varsList'})[kind],items,field,kind);
  });
}
$('#decorGroup').addEventListener('change',()=>getCatalog('decoration',{group:$('#decorGroup').value}));
$('#academyGroup').addEventListener('change',()=>getCatalog('academy',{group:$('#academyGroup').value}));

(async()=>{
  const info=await work(()=>bridge('init'));
  if(info){applyState(info.state);log('Đã khởi tạo Android bridge / Python core.');}
})();
