---
layout: page
title: Code Packages
permalink: /codes/
---

Here are a selection of recent projects that have been used in our work. 

{% for project in site.codes %}
  <div class="clearfix" style="margin-bottom: 40px;">
    {% if project.image %}
      <img src="{{ project.image }}" width="200" style="float: left; margin-right: 15px; margin-bottom: 10px;">
    {% endif %}
    
    <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
    <p>{{ project.description | markdownify }}</p>
    {% if project.link %}
      <a href="{{ project.link }}" target="_blank" rel="noopener noreferrer">Link.</a>
    {% endif %}
  </div>
{% endfor %}
