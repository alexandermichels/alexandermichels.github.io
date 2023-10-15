---
layout: page
permalink: /teaching/
title: Teaching
description: Courses I have taught and related materials.
nav: true
---

## Courses Taught

**Business Location Decisions (GGIS/BADM 205)**, Spring 2023  
Department of Geography and Geographic Information Science, UIUC  
*Analyzes location decision-making emphasizing industrial and commercial location patterns; identifies important institutional factors and their changing roles over the recent past; and focuses on plant closings, economic disruptions, and problems of structural change.*  



## Awards & Certificates

**Certificate in Foundations of Teaching**  
May 5th, 2023  
The Center for Innovation in Teaching & Learning, University of Illinois

**Teacher Ranked As Excellent By Their Students**  
June 2023
Center for Innovation in Teaching & Learning,  
University of Illinois


## Tutorials & Workshops

{% for type in site.data.presentations %}
  {% if type.link == "workshop" %}
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
  {% endif %}
{% endfor %}


I've also created materials for a variety of tutorials/workshops on topics like cyberGIS, software hacking, HPC, and more. [Materials here](/code/#edu)
