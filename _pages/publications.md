---
layout: page
permalink: /publications/
title: Publications
years: [2021, 2020, 2019]
nav: true
---

For an up-to-date list and metrics see <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}" target="_blank" title="Google Scholar">Google Scholar  <i class="ai ai-google-scholar"></i></a>. 

<details>
<summary>Click here for a quick summary of the journals/conferences where I have published.</summary>

<div class="row">
<div class="col-sm-6">
    <h3>Journals:</h3>
    {% for venue in site.data.venues %}
    {% if venue[1].type == "journal" %}
    <div class="theme-card hoverable mt-2 p-2">
        <details>
            <summary><i>{{venue[1].name}}</i></summary>
            <hr />
            <b><a href='{{venue[1].url}}' target="_blank">{{venue[0]}} -</a></b>
            {{venue[1].desc}}
        </details>
    </div>
    {% endif %}
    {% endfor %}
</div>
<div class="col-sm-6">
    <h3>Conferences:</h3>
    {% for venue in site.data.venues %}
    {% if venue[1].type == "conf" %}
    <div class="theme-card hoverable mt-2 p-2">
        <details>
            <summary><i>{{venue[1].name}}</i></summary>
            <hr />
            <b><a href='{{venue[1].url}}' target="_blank">{{venue[0]}} -</a></b>
            {{venue[1].desc}}
        </details>
    </div>
    {% endif %}
    {% endfor %}
</div>
</div>
</details>



{% comment %}
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
{% endcomment %}


<h2>Table of Contents</h2>
<ul>
{% for type in site.scholar.keyword_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @*[{{type}}=true] -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <li><a href="#{{type}}">{{ site.scholar.keyword_names[type] }}</a></li>
  {% endif %}
{% endfor %}
</ul>

<div class="publications">
{% for type in site.scholar.keyword_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @*[{{type}}=true] -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <h2 id="{{type}}">{{ site.scholar.keyword_names[type] }}</h2>
    {% bibliography --query @*[{{type}}=true] --group_by year --group_order descending %}
  {% endif %}
{% endfor %}
</div>