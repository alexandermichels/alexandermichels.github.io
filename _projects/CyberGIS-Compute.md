---
layout: page
title: CyberGIS-Compute
description: Democratizing HPC for geospatial developers
img: /assets/gif/CyberGIS-ComputeHello.gif
importance: 1
category: Cyberinfrastructure
github: https://github.com/cybergis/cybergis-compute-python-sdk
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1 center" src="{{ '/assets/img/Compute.png' | relative_url }}" alt="" title="CyberGIS-Compute"/>
    </div>
</div>
<div class="caption">
    The concept behind CyberGIS-Compute
</div>

CyberGIS-Compute is a tool for running code on HPC from Jupyter notebooks. Compute is made up of two parts: (1) the Core which interacts with HPC resources and provides a RESTful API and (2) the SDK which provides users and developers a Python interface. It is specifically geared towards geospatial development and integrated into the CyberGISX and CJW ecosystem, but general enough that anyone can deploy and use it!

For more info see the [CyberGIS-Compute Python SDK](https://cybergis.github.io/cybergis-compute-python-sdk/) webpage.

## Associated Publications

<div class="publications">
{% for type in site.scholar.type_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @{{type}}[cybergiscompute=true] -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <h4>{{ site.scholar.type_names[type] }}</h4>
    {% bibliography --query @{{type}}[cybergiscompute] --group_by year --group_order descending %}
  {% endif %}
{% endfor %}
</div>