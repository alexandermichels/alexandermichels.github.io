from datetime import datetime
import json
import yaml


def pprint(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))


categories = {
    "conference": "Conference Presentations",
    "invited": "Invited Talks",
    "poster": "Poster Sessions"
}

pres_data = None
with open("../_data/presentations.yml", 'r') as stream:
    try:
        pres_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

assert pres_data is not None
markdown_text = ""
latex_text = ""
for category in categories.keys():
    for pres in pres_data[category]:
        pres["datetime"] = datetime.strptime(pres["time"], "%B %Y")
    category_data = sorted(pres_data[category], key=lambda x: x["datetime"], reverse=True)
    markdown_text += "\n\n    {}\n".format(categories[category])
    latex_text += "\n\n\\vspace{{0.5cm}}\hspace*{{2cm}}\\textbf{{{}}}\n\\vspace{{0.25cm}}\n\n".format(categories[category])
    for pres in category_data:
        markdown_text += "\n**{}**  \n{} | {}  \n{}  \n".format(pres["title"], pres["event"], pres["place"], pres["time"])
        latex_text += "\n    \Talk{{{}}}{{{}}}{{{}}}{{{}}}\n".format(pres["title"], pres["time"], pres["event"], pres["place"])
latex_text = latex_text.replace("&", "\&")
print("{}\nMarkdown text:\n{}\n".format("=" * 20, "=" * 20))
print(markdown_text)
print("{}\nLatex text:\n{}\n".format("=" * 20, "=" * 20))
print(latex_text)
with open("Presentations.md", "w") as mdout:
    mdout.write(markdown_text)
with open("Presentations.tex", "w") as texout:
    texout.write(latex_text)
