---
layout: page
title: All Posts
permalink: /archive/
hide_post: true
---

{% for project in site.pubs %}
  <div class="clearfix" style="margin-bottom: 40px;">
    {% if project.image %}
      <img src="{{ project.image }}" width="200" style="float: left; margin-right: 15px; margin-bottom: 10px;">
    {% endif %}
    
    <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
    <p>{{ project.description | markdownify }}</p>
  </div>
{% endfor %}

{% for person in site.people %}
  <div class="clearfix" style="margin-bottom: 40px;">
    {% if person.image %}
      <img src="{{ person.image }}" width="200" style="float: left; margin-right: 15px; margin-bottom: 10px;">
    {% endif %}
    
    <h3><a href="{{ person.url }}">{{ person.name }}</a></h3>
    <p>{{ person.description | markdownify }}</p>
  </div>
{% endfor %}

{% for post in site.posts %}
  <div class="clearfix" style="margin-bottom: 40px;">
    {% if person.image %}
      <img src="{{ post.image }}" width="200" style="float: left; margin-right: 15px; margin-bottom: 10px;">
    {% endif %}
    
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    <p>{{ post.description }}</p>
  </div>
{% endfor %}

{% for code in site.codes %}
  <div class="clearfix" style="margin-bottom: 40px;">
    {% if code.image %}
      <img src="{{ post.image }}" width="200" style="float: left; margin-right: 15px; margin-bottom: 10px;">
    {% endif %}
    
    <h3><a href="{{ code.url }}">{{ code.title }}</a></h3>
    <p>{{ code.description }}</p>
  </div>
{% endfor %}
