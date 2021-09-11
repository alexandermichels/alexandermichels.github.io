---
layout: page
permalink: /publications/
title: Publications
years: [2021, 2020, 2019, 2018]
nav: true
---

For an up-to-date list and metrics see <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}" target="_blank" title="Google Scholar">Google Scholar  <i class="ai ai-google-scholar"></i></a>


<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
