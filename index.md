---
layout: page
---
{% include JB/setup %}

<div class="index">
  {% for post in site.posts %}
    <div class="post">
      <h2 class="title"><a href="{{BASE_PATH}}{{post.url}}">{{post.title}}</a></h2>
      <h3 class="date">{{post.date | date: "%Y-%m-%d"}}</h3>
      <div class="content">{{post.content}}</div>
    </div>
  {% endfor %}
</div>

