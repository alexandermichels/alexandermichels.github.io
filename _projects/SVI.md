---
layout: page
title: SVI Mapping Test
description: Mapping Social Vulnerability
img: /assets/img/SVIbyCensusTract.png
importance: 1
---

This is a test to see how putting maps/a project online would look. For information on the CDC Social Vulnerability Index, see the documentation: https://www.atsdr.cdc.gov/placeandhealth/svi/documentation/SVI_documentation_2018.html As the documentation states about the SVI index: "Percentile ranking values range from 0 to 1, with higher values indicating greater vulnerability."

Below you can see a simple map of the CDC's 2018 Social Vulnerability Index (SVI) by Census Tract ([data available here](https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html)):

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/SVIbyCensusTract.png' | relative_url }}" alt="" title="SVI by Census Tract"/>
    </div>
</div>
<div class="caption">
    Map of SVI by Census Tract
</div>

I also created some fancier maps using [Folium](https://python-visualization.github.io/folium/modules.html):

Color scheme 1:

<div class="row">
    <iframe src="{{ '/assets/html/maps/SVI2018_US_COUNTY_YlGnBu.html' | relative_url }}"  title="Map1" style="width:100%; height:400px;"></iframe>
</div>
<div class="caption">
    Map of SVI by County using the `YlGnBu` color pallete.
</div>

***

Color scheme 2:

<div class="row">
    <iframe src="{{ '/assets/html/maps/SVI2018_US_COUNTY_PRGn.html' | relative_url }}" title="Map2" style="width:100%; height:400px;"></iframe>
</div>
<div class="caption">
    Map of SVI by County using the `PRGn` color pallete.
</div>

Learn more about [color schemes available for folium's choropleth](https://colorbrewer2.org/).

***