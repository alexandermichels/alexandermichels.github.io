---
layout: page
permalink: /publications/
title: Publications
years: [2021, 2020, 2019]
nav: true
---

For an up-to-date list and metrics see <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}" target="_blank" title="Google Scholar">Google Scholar  <i class="ai ai-google-scholar"></i></a>. 

<h2>Table of Contents</h2>
<ul>
{% for type in site.scholar.type_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @{{type}} -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <li><a href="#{{type}}">{{ site.scholar.type_names[type] }}</a></li>
  {% endif %}
{% endfor %}
</ul>

<div class="publications">
{% for type in site.scholar.type_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @{{type}} -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <h2 id="{{type}}">{{ site.scholar.type_names[type] }}</h2>
    {% bibliography --query @{{type}} --group_by year --group_order descending %}
  {% endif %}
{% endfor %}
</div>