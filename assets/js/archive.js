/* 아카이브 검색 및 주제 필터 — 외부 의존성 없음 */
(function () {
  var search  = document.getElementById('archive-search');
  var list    = document.getElementById('archive-list');
  var filters = document.getElementById('topic-filters');
  var counter = document.getElementById('archive-count');
  var empty   = document.getElementById('archive-empty');
  if (!list) return;

  var items  = Array.prototype.slice.call(list.querySelectorAll('.archive-item'));
  var topic  = 'all';

  function apply() {
    var q = (search && search.value || '').trim().toLowerCase();
    var shown = 0;

    items.forEach(function (item) {
      var matchTopic = topic === 'all' || item.dataset.topic === topic;
      var matchText  = !q || (item.dataset.search || '').indexOf(q) !== -1;
      var visible    = matchTopic && matchText;
      item.hidden = !visible;
      if (visible) shown++;
    });

    if (counter) {
      counter.textContent = shown === items.length
        ? items.length + '편'
        : shown + '편 / 전체 ' + items.length + '편';
    }
    if (empty) empty.hidden = shown !== 0;
  }

  if (search) search.addEventListener('input', apply);

  if (filters) {
    filters.addEventListener('click', function (event) {
      var btn = event.target.closest('.chip-btn');
      if (!btn) return;
      topic = btn.dataset.filter;
      filters.querySelectorAll('.chip-btn').forEach(function (b) {
        b.classList.toggle('is-active', b === btn);
      });
      apply();
    });
  }

  apply();
})();
