---
layout: page
permalink: /presentations/
title: Presentations
description: Presentations and posters from past conferences. Asterisk (*) indicates the presenter.
nav: false
---


## Table of Contents:

<ul>
{% for type in site.data.presentations %}
  <li><a href="#{{type.link}}">{{type.type}}</a></li>
{% endfor %}
</ul>

{% for type in site.data.presentations %}
  <a id="{{type.link}}"></a>
  <hr>
  <h2><a href="#{{type.link}}">{{type.type}}</a></h2>
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