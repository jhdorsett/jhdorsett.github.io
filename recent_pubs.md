---
layout: page
title: "Recent Publications"

---

This is accessed by editing recent_pubs.md

You can just write stuff here. 

the text below is looping through all of the .md files in _pubs and plotting their metadata in a nice way. I have it set that the max posts are 5 and it will truncate the list and link to an archive if we end up with more than that

{% assign max_projects = 5 %}
{% assign project_count = 0 %}
{% for project in site.pubs %}
  {% if project_count < max_projects %}
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
    {% assign project_count = project_count | plus: 1 %}

  {% endif %}
{% endfor %}


{% if site.pubs.size > max_projects %}
  <div style="margin-top: 20px;">
    <a href="/archive" target="_self">See all publications</a>
  </div>
{% endif %}

# with markdown syntax
* one
* two

[you can link things](https://google.com)

or write code 

```language
a = b**2
c=d/4
```
and latex $$E = mc^2$$
