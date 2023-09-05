---
layout: page
title: Algorithms and Methods for Spatial Accessibility
description: Developing novel algorithms and methods for accurate and scalable spatial accessibility analyses.
img: /assets/gif/ConvexHullVsAlphaShape.gif
importance: 1
category: Spatial Analysis
# github: https://github.com/cybergis/COVID-19AccessibilityNotebook
---

This project focused on the development of algorithms, methods, and software to increase the accuracy and scalability of spatial accessibility analysese. We have also explored how best to utilize new data sources (OSM, Uber Movement, etc.) to improve our analyses.

<div class="row" style="text-align: center;">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/gif/ConvexHullVsAlphaShape.gif' | relative_url }}" alt="" title="Convex Hull vs Alpha Shape for Catchments"/>
    </div>
</div>
<div class="caption">
    A GIF demonstrating the difference between using Convex Hull and Alpha Shapes for determining catchments in spatial accessibility analyses.
</div>

## Associated Publications

<div class="publications">
{% for type in site.scholar.type_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @{{type}}[spaccmeth=true] -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <h4>{{ site.scholar.type_names[type] }}</h4>
    {% bibliography --query @{{type}}[spaccmeth] --group_by year --group_order descending %}
  {% endif %}
{% endfor %}
</div>