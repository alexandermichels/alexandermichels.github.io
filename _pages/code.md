---
layout: page
permalink: /code/
title: Code
description: Code I have written or contributed to
nav: true
---


<!---
Github badges from : https://ghbtns.com/
Docker badges: https://shields.io/category/downloads
--->

{% for category in site.data.code %}
  <a id="{{category.link}}"></a>
  <div class="theme-card hoverable mt-3 p-3">
  <h2 style="text-align: center;"><a href="#{{category.link}}">{{category.category}}</a></h2>
  {% for repo in category.repos %}
    {% if repo.platform == "github" %}
        <div class="row">
            <div class="col-sm-6">
                <p><a href="https://github.com/{{repo.user}}/{{repo.repo}}" target="_blank"><i class="fab fa-github"></i>  {{repo.user}}/{{repo.repo}}</a></p>
            </div>
            <div class="col-sm-2">
                <iframe src="https://ghbtns.com/github-btn.html?user={{repo.user}}&repo={{repo.repo}}&type=fork&count=true&v=2" frameborder="0" scrolling="0" width="150" height="20" title="GitHub"></iframe>
            </div>
            <div class="col-sm-2">
                <iframe src="https://ghbtns.com/github-btn.html?user={{repo.user}}&repo={{repo.repo}}&type=star&count=true&v=2" frameborder="0" scrolling="0" width="150" height="20" title="GitHub"></iframe>
            </div>
            <div class="col-sm-2">
                <iframe src="https://ghbtns.com/github-btn.html?user={{repo.user}}&repo={{repo.repo}}&type=watch&count=true&v=2" frameborder="0" scrolling="0" width="150" height="20" title="GitHub"></iframe>
            </div>
        </div>
    {% endif %}
  {% endfor %}
  </div>
{% endfor %}
<br>
<br>
<div style="display: flex; align-items: center; justify-content: center;">
    <iframe src="https://ghbtns.com/github-btn.html?user={{site.github_username}}&type=follow&count=true" frameborder="0" scrolling="0" width="230" height="30" title="GitHub"></iframe>
    <iframe src="https://ghbtns.com/github-btn.html?user={{site.github_username}}&type=sponsor" frameborder="0" scrolling="0" width="280" height="30" title="GitHub"></iframe>
</div>