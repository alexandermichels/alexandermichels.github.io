---
layout: page
title: ABMs for Public Health
description: Agent-based models for public health. Work covers calibration, reproducibility, and more.
img: /assets/gif/pso-rastrigin.gif
importance: 1
category: Agent-Based Modeling
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
    <p style="text-align:center;">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/gif/pso-rastrigin.gif' | relative_url }}" alt="" title="Particle Swarm Optimization"/>
    </p>
    </div>
</div>
<div class="caption">
    The Particle Swarm Optimization algorithm running on the Rastrigin function
</div>

I have done a lot of work, especially with Dr. Jeon-Young Kang, using spatially-explicit agent-based models for investigating disease spread. This work has examined using CyberGISX for reproducible and transparent modeling and calibration of ABMs.


## Associated Publications

<div class="publications">
{% for type in site.scholar.type_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @{{type}}[abmph=true] -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <h4>{{ site.scholar.type_names[type] }}</h4>
    {% bibliography --query @{{type}}[abmph=true] --group_by year --group_order descending %}
  {% endif %}
{% endfor %}
</div>