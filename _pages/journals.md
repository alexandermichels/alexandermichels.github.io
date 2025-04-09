---
layout: page
permalink: /gisci-journals
title: Journals
description: Collecting SJR rankings for select sub-fields related to GIScience/CyberGIS
---

I found it difficult to use the [Scimago Journal Ranking](https://www.scimagojr.com/) site for some of the specific sub-disciplines I take part in and therefore used their amazing widgets to build my own little dashboard. This work was inspired by the rankings <a href="https://doi.org/10.1111/j.1467-9671.2008.01106.x" target="_blank">found here</a> and <a href="https://doi.org/10.1080/13658816.2015.1130831" target="_blank">this more recent paper.</a> 

I am not an expert in bibliometrics or scientometrics so this is a fun tool, but not one to be taken seriously. Also note that a lot of amazing work in GIScience happens at conferences, so journals do not give the complete picture. I also excluded interdisciplinary journals like PLOS One and Scientific Reports where GIScience work is often published, but these are great venues as well.

{% for category in site.data.journals %}
<a id="{{category.link}}"></a>
<div class="theme-card hoverable mt-3 p-3" style="text-align: center">
  <details>
  <summary>
  <h2 style="text-align: center; display: inline;"><a href="#{{category.link}}">{{category.category}}</a></h2>
  <p>{{category.desc}}</p>
  </summary>
  {% for journal in category.journals %}
    <a href="https://www.scimagojr.com/journalsearch.php?q={{journal}}&amp;tip=sid&amp;exact=no" target="_blank" title="SCImago Journal &amp; Country Rank"><img border="0" src="https://www.scimagojr.com/journal_img.php?id={{journal}}" alt="SCImago Journal &amp; Country Rank"  /></a>
  {% endfor %}
  </details>
  </div>
{% endfor %}