---
layout: page
permalink: /cv/
title: CV
nav: true
---

**Curriculum Vitae:** <a href="https://raw.githubusercontent.com/alexandermichels/CV/master/CurriculumVitae.pdf" style="padding:3px; border:1px solid fuchsia" target="_blank">Download PDF</a> <a href="https://github.com/alexandermichels/CV/blob/master/CurriculumVitae.pdf" style="padding:3px; border:1px solid fuchsia" target="_blank">View On Github</a>

<!-- <p>Resume: <a href="https://raw.githubusercontent.com/alexandermichels/CV/master/Resume.pdf" target="_blank">Download PDF</a>, <a href="https://github.com/alexandermichels/CV/blob/master/Resume.pdf" target="_blank">View On Github</a></p> -->

## Table of Contents

<ul>
    <li><a href="#edu">Education</a></li>
    <li><a href="#research-exp">Research Experience</a></li>
    <li><a href="#teaching-exp">Teaching Experience</a></li>
    <li><a href="#awards">Awards</a></li>
    <li><a href="#pub">Publications</a></li>
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
    <li><a href="#pres">Presentations</a></li>
    <ul>
        {% for type in site.data.presentations %}
        <li><a href="#{{type.link}}">{{type.type}}</a></li>
        {% endfor %}
    </ul>
    <li><a href="#prof-assoc">Professional Associations</a></li>
    <li><a href="#prof-service">Professional Service</a></li>
</ul>

<hr id="edu" />


## [Education](#edu)

**Ph.D. in Informatics (in progress)**  
University of Illinois at Urbana-Champaign  
June 2019 - Present  
Advised by Dr. Shaowen Wang

**M.S. in Geography**  
University of Illinois at Urbana-Champaign  
May 2024  
Advised by Dr. Shaowen Wang

**B.S. in Mathematics and Financial Economics**   
Westminster College  
May 2019  
Minor in Computer Science, Cum Laude with Honors in Mathematics and CS  
Honors Thesis: "Capturing the Predictive Power of Cortical Learning Algorithms"

<hr id="research-exp" />

## [Research Experience](#research-exp)

**CyberGIS Center for Advanced Digital and Spatial Studies**  
[CyberGIS Center](https://cybergis.illinois.edu/) and [CyberInfrastructure and Geospatial Information Laboratory](https://cigi.illinois.edu/)  
June 2019 - Present  
* Lead developer on [CyberGIS-Compute](https://github.com/cybergis/cybergis-compute-python-sdk) (75 users; Typescript, Python, SLURM, Globus) and [CyberGIS-Jupyter](https://cybergisx.cigi.illinois.edu/) (1368 users; Docker, Docker Swarm, Linux, Bash, Ansible, Kubernetes).
* Managed 6 student research programmers; interviewed and hired students and full-time staff.
* Led workshops with 50+ participants and organized conference symposiums/sessions.
* Analyzed spatial Big Data using Bash, HPC, Python, Machine Learning (ML), and SQL.
* Published 16 articles and presented at 20+ conferences, garnering 200+ citations.

**SESYNC Graduate Research Fellow**  
National Socio-Environmental Synthesis Center (SESYNC)  
February 2020 - January 2022
* Worked on Graduate Pursuit entitled "[Financial Opacity and Challenges to Forest Governance in Indonesia and Malaysia](https://www.sesync.org/project/graduate-pursuits-request-for-proposals/financial-opacity-and-challenges-to-forest)"

**Informatics Researcher**  
Institute for Pure and Applied Mathematics at UCLA / Praedicat, Inc.  
June 2018 - August 2018
* Worked for Praedicat, Inc. automating information extraction, classification, and aggregation from web data for business profiling of over 52,600 companies and corporate entities.
* Worked for IPAM to develop a novel algorithm for computational fact-checking on knowledge graphs and a self-supervised machine learning algorithm for sentence importance which outperformed TF-IDF.


<hr id="teaching-exp" />


## [Teaching Experience](#teaching-exp)

**Business Location Decisions (GGIS/BADM 205)**, Spring 2023  
Department of Geography and Geographic Information Science  
*Analyzes location decision-making emphasizing industrial and commercial location patterns; identifies important institutional factors and their changing roles over the recent past; and focuses on plant closings, economic disruptions, and problems of structural change.*  


<hr id="awards" />

## [Awards](#awards)

{% for award in site.data.awards %}
  <b>{{award.title}}</b><br>
  {{award.desc}} | {{award.time}}<br>
  {{award.awarder}}
{% endfor %}

<hr id="pub" />

## [Publications](#pub)

<!--See [publications page](/publications/)-->
{% comment %}
<div class="publications">
{% for type in site.scholar.type_order %}
  {%- capture citecount -%}
  {%- bibliography_count --query @{{type}} -%}
  {%- endcapture -%}
  {% if citecount != "0"  %}
    <h3 id="{{type}}">{{ site.scholar.type_names[type] }}</h3>
    {% bibliography --query @{{type}} --group_by year --group_order descending %}
  {% endif %}
{% endfor %}
</div>
{% endcomment %}

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

<hr id="pres" />

## [Presentations](#pres)

<!--See [presentations page](/presentations/)-->

Asterisk (*) indicates the presenter(s).

{% for type in site.data.presentations %}
  <a id="{{type.link}}"></a>
  <h3><a href="#{{type.link}}">{{type.type}}</a></h3>
  <ul>
  {% for pres in type.presentations %}
    <li><b>{{pres.title}}</b><br>
    <p style="text-align:left;">
        {{pres.presenters}}<br>
        {{pres.event}}
        <span style="float:right;">
            {{pres.time}}
            {% if pres.poster %}
            | <a href="{{pres.poster}}" target="_blank">Poster</a>
            {% endif %}
            {% if pres.video %}
            | <a href="{{pres.video}}" target="_blank">Video</a>
            {% endif %}
        </span>
    </p>
    </li>
  {% endfor %}
  </ul>
{% endfor %}

<hr id="prof-assoc" />

## [Professional Associations](#prof-assoc)

**American Association of Geographers (AAG)**  
Specialty Groups:   
* Applied Geography  
* Cyberinfrastructure (CISG)  
* Geographic Information Science & Systems  
* Health and Medical Geography  
* Spatial Analysis and Modeling  
* Transportation Geography  

**Association for Computing Machinery (ACM)**  
Special Interest Groups:  
* SIGSPATIAL (Spatial Information)

**Cartography and Geographic Information Society (CaGIS)**  

**Campus Research Computing Consortium (CaRCC)**  

**United States Research Software Engineer Association (US-RSE)**  

<hr id="prof-service" />


## [Professional Service](#prof-service)

### Conference and Workshops

**Symposium Organizer**  
[AAG 2025 Symposium on Spatial AI & Data Science for Sustainability](https://i-guide.io/aag-2025-symposium-on-spatial-ai-data-science-for-sustainability/)  

**Session Organizer**, Challenges and Opportunities of Spatial Accessibility
[AAG 2025 Symposium on Spatial AI & Data Science for Sustainability](https://i-guide.io/aag-2025-symposium-on-spatial-ai-data-science-for-sustainability/) 

**Symposium Organizer**  
[AAG 2024 Symposium on Geospatial Data Science for Sustainability](https://iguide.illinois.edu/aag-2024-symposium-on-geospatial-data-science-for-sustainability/)  

**Session Organizer**, Challenges and Opportunities of Spatial Accessibility 1 & 2  
[AAG 2024 Symposium on Geospatial Data Science for Sustainability](https://iguide.illinois.edu/aag-2024-symposium-on-geospatial-data-science-for-sustainability/) 

**Reviewer**  
[Institute for Geospatial Understanding through an Integrative Discovery Environment (I-GUIDE) Forum](https://iguide.illinois.edu/forum-2023/)

**Symposium Program Co-Chair**  
[AAG 2023 Symposium on Harnessing the Geospatial Data Revolution for Sustainability Solutions](https://iguide.illinois.edu/aag-2023-symposium-on-harnessing-the-geospatial-data-revolution-for-sustainability-solutions/)  

**Session Chair**, Data-intensive and Computational Geography  
[AAG 2023 Symposium on Harnessing the Geospatial Data Revolution for Sustainability Solutions](https://iguide.illinois.edu/aag-2023-symposium-on-harnessing-the-geospatial-data-revolution-for-sustainability-solutions/)  

**Session Organizer**, Computation and Uncertainty of Spatial Accessibility  
[AAG 2022 Symposium on Data-Intensive Geospatial Understanding in the Era of AI and CyberGIS](https://cybergis.illinois.edu/aag-symposium-2022/)

### Journal Reviewer

* Geocarto International, Taylor & Francis
* International Journal of Geographical Information Science (IJGIS), Taylor & Francis


### Professional Organizations

**Director**  
AAG CyberInfrastructure Specialty Group (CISG)  
February 2022 - April 2026  

**Student Director**  
AAG CyberInfrastructure Specialty Group (CISG)  
April 2021 - February 2022  

