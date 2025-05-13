---
layout: default
title: All Categories
lang: en
permalink: /en/categories/
---

<div class="category-index">
  {% for cat in site.data.categories %}
    <a class="category-tag" href="/en/category/{{ cat.slug }}/">{{ cat.name_en }}</a>
  {% endfor %}
</div> 