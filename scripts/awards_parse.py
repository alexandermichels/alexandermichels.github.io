from datetime import datetime
import json
import yaml


def pprint(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))


award_data = None
with open("../_data/awards.yml", 'r') as stream:
    try:
        award_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

assert award_data is not None
award_data = award_data["awards"]
markdown_text = ""
latex_text = ""
for pres in award_data:
    pres["datetime"] = datetime.strptime(pres["time"], "%B %Y")
award_data = sorted(award_data, key=lambda x: x["datetime"], reverse=True)

for pres in award_data:
    markdown_text += "\n**{}**  \n{} | {}  \n{}  \n".format(pres["title"], pres["desc"], pres["time"], pres["awarder"])
    latex_text += "\n    \Award{{{}}}{{{}}}{{{}}}{{{}}}\n".format(pres["title"], pres["time"], pres["desc"], pres["awarder"])
latex_text = latex_text.replace("&", "\&")
print("{}\nMarkdown text:\n{}\n".format("=" * 20, "=" * 20))
print(markdown_text)
print("{}\nLatex text:\n{}\n".format("=" * 20, "=" * 20))
print(latex_text)
with open("Awards.md", "w") as mdout:
    mdout.write(markdown_text)
with open("Awards.tex", "w") as texout:
    texout.write(latex_text)
