---
layout: page
title: SVI and CBSA Mapping
description: Mapping Social Vulnerability
img: /assets/img/SVIbyCensusTract.png
importance: 1
category: Spatial Analysis
---

## TOC:

* [SVI Mapping with Geopandas](#svi-gpd)
* [SVI Mapping with Folium](#svi-folium)
* [Metro/Micro-politan Statistical Areas (MSA/&mu;SA)](#cbsa)
* [Combined Statistical Area (CSA)](#csa)

<a id="svi-gpd"></a>

***

### SVI Mapping with Geopandas

This is a test to see how putting maps/a project online would look. For information on the CDC Social Vulnerability Index, see the documentation: [https://www.atsdr.cdc.gov/placeandhealth/svi/documentation/SVI_documentation_2018.html](https://www.atsdr.cdc.gov/placeandhealth/svi/documentation/SVI_documentation_2018.html) As the documentation states about the SVI index: "Percentile ranking values range from 0 to 1, with higher values indicating greater vulnerability."

Below you can see a simple map of the CDC's 2018 Social Vulnerability Index (SVI) by Census Tract created using GeoPandas ([data available here](https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html)):

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/SVIbyCensusTract.png' | relative_url }}" alt="" title="SVI by Census Tract"/>
    </div>
</div>
<div class="caption">
    Map of SVI by Census Tract
</div>

<a id="svi-folium"></a>

***

### SVI Mapping with Folium

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

Maps can be large making them slow to load and memory intensive so simplifying the geometries can be helpful, but it's a tradeoff between accuracy of the shapes and size of the map. The maps above are ~34MB on the disk while the map below only takes up approximatley 10MB. 

<div class="row">
    <iframe src="{{ '/assets/html/maps/SVI2018_US_COUNTY_YlGnBu_Tol01.html' | relative_url }}" title="Map2" style="width:100%; height:400px;"></iframe>
</div>
<div class="caption">
    Map of SVI by County using a simplified geometry with tolerance 0.01 for WGS84.
</div>

The map looks fine, but you can see issues around odd-shaped counties when you zoom in close (zoom into around the Missippi River for examples).

<a id="cbsa"></a>

***

### Metro/Micro-politan Statistical Areas (MSA/&mu;SA)

<a id="csa"></a>

A useful geography is the [Metropolitan Statistical Area](https://en.wikipedia.org/wiki/Metropolitan_statistical_area) and [Micropolitan Statistical Area](https://en.wikipedia.org/wiki/Micropolitan_statistical_area) which are collectively referred to as "Core Based Statistical Areas (CBSAs)". According to Wikipedia: "CBSAs are delineated on the basis of a central urban area or urban cluster – in other words: a contiguous area of relatively high population density."


<div class="row">
    <iframe src="{{ '/assets/html/maps/CBSA.html' | relative_url }}" title="Map2" style="width:100%; height:400px;"></iframe>
</div>
<div class="caption">
    Map of Metro/Micro-politan Statistical Areas (MSA/&mu;SA)
</div>

***

### Combined Statistical Area (CSA)

A useful geography is the [Combined Statistical Area](https://en.wikipedia.org/wiki/Combined_statistical_area) which capture a city's area including suburbs and ignoring state/adminstrative lines. According to Wikipedia "CSAs represent multiple metropolitan or micropolitan areas that have an employment interchange of at least 15%. CSAs often represent regions with overlapping labor and media markets.":

<div class="row">
    <iframe src="{{ '/assets/html/maps/CSA.html' | relative_url }}" title="Map2" style="width:100%; height:400px;"></iframe>
</div>
<div class="caption">
    Map of Combined Statistical Areas
</div>
