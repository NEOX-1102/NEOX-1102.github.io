---
layout: default
title: 全部分类
lang: zh
permalink: /categories/
---

<div class="category-index">
  {% for cat in site.data.categories %}
    <a class="category-tag" href="/category/{{ cat.slug }}/">{{ cat.name }}</a>
  {% endfor %}
</div> 