---
layout: page
title: Spatial Accessibility for Public Health
description: Measuring spatial accessibility to healthcare resources
img: /assets/img/PLOSONE2022-HIVAccessibility.PNG
importance: 3
category: Spatial Accessibility
# github: https://github.com/cybergis/COVID-19AccessibilityNotebook
---

Spatial Accessibility helps to quantify the disparities in access to critical goods and services across space. In the context of healthcare, those disparities have real-word consequences for the health and lives of people. 

<div class="row" style="text-align: center;">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/WhereCOVID-19Acc.png' | relative_url }}" alt="" title="WhereCOVID-19 Accessibility"/>
    </div>
</div>
<div class="caption">
    A screenshot of the WhereCOVID-19 Dashboard's Accessibility Explorer
</div>

## Associated Publications

<div class="publications">
{% for type in site.scholar.type_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @{{type}}[accph=true] -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <h4>{{ site.scholar.type_names[type] }}</h4>
    {% bibliography --query @{{type}}[accph] --group_by year --group_order descending %}
  {% endif %}
{% endfor %}
</div>