---
layout: default
title: 아카이브
permalink: /archive/
---

<section class="archive">
  <h1 class="page-title">아카이브</h1>
  <p class="page-sub">지금까지 게시한 논문 요약 {{ site.posts.size }}편</p>

  <div class="filters">
    <label class="search">
      <span class="visually-hidden">제목·키워드 검색</span>
      <input type="search" id="archive-search" placeholder="제목이나 키워드로 검색" autocomplete="off">
    </label>
    <div class="chip-filters" id="topic-filters">
      <button type="button" class="chip chip-btn is-active" data-filter="all">전체</button>
      {%- assign topics = site.posts | map: 'topic' | compact | uniq | sort %}
      {%- for t in topics %}
      <button type="button" class="chip chip-btn" data-filter="{{ t }}">{{ t }}</button>
      {%- endfor %}
    </div>
  </div>

  <p class="archive-count" id="archive-count" role="status"></p>

  <ol class="archive-list" id="archive-list">
    {%- for post in site.posts %}
    <li class="archive-item"
        data-topic="{{ post.topic }}"
        data-search="{{ post.title | downcase | escape }} {{ post.one_liner | downcase | escape }} {{ post.keywords | join: ' ' | downcase | escape }} {{ post.topic | escape }}">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y.%m.%d' }}</time>
      <span class="chip chip-sm" data-topic="{{ post.topic_key }}">{{ post.topic }}</span>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
    {%- endfor %}
  </ol>

  <p class="archive-empty" id="archive-empty" hidden>조건에 맞는 논문이 없습니다.</p>
</section>

<script src="{{ '/assets/js/archive.js' | relative_url }}" defer></script>
