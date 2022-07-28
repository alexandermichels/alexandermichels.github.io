---
layout: page
title: Spatial Accessibility for COVID-19
description: Measuring spatial accessibility to healthcare resources for the COVID-19 pandemic
img: /assets/img/WhereCOVID-19Acc.png
importance: 100
category: Spatial Analysis
github: https://github.com/cybergis/COVID-19AccessibilityNotebook
---

The COVID-19 pandemic has illustrated the life-saving importance of healthcare resources like ventilators and ICU beds. We employed spatial accessibility methods to understand how access to these crucial resources varies across space and analyzed the relationship between access and socio-economic vulnerability measured by the CDC Social Vulnerability Index (SVI). Our [publication can be seen here](https://doi.org/10.1186/s12942-020-00229-x) and the abstract for the paper is as follows:

> "The severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), causing the coronavirus disease 2019 (COVID-19) pandemic, has infected millions of people and caused hundreds of thousands of deaths. While COVID-19 has overwhelmed healthcare resources (e.g., healthcare personnel, testing resources, hospital beds, and ventilators) in a number of countries, limited research has been conducted to understand spatial accessibility of such resources. This study fills this gap by rapidly measuring the spatial accessibility of COVID-19 healthcare resources with a particular focus on Illinois, USA. Specifically, the rapid measurement is achieved by resolving computational intensity of an enhanced two-step floating catchment area (E2SFCA) method through a parallel computing strategy based on cyberGIS (cyber geographic information science and systems). The study compared the spatial accessibility measures for COVID-19 patients to those of general population, identifying which geographic areas need additional healthcare resources to improve access. The results also help delineate the areas that may face a COVID-19-induced shortage of healthcare resources caused by COVID-19. The Chicagoland, particularly the southern Chicago, shows an additional need for resources. Our findings are relevant for policymakers and public health practitioners to allocate existing healthcare resources or distribute new resources for maximum access to health services."

<div class="row" style="text-align: center;">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/WhereCOVID-19Acc.png' | relative_url }}" alt="" title="WhereCOVID-19 Accessibility"/>
    </div>
</div>
<div class="caption">
    A screenshot of the WhereCOVID-19 Dashboard's Accessibility Explorer
</div>

To keep pace with the rapidly evolving pandemic, our measures are re-calculated daily and included into the [CIGI WhereCOVID-19 analytics dashboard](https://wherecovid19.cigi.illinois.edu/spatialAccess.html) so we can understand how accessibility changes as infrastructure and cases do.
