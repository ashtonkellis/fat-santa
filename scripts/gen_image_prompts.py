#!/usr/bin/env python3
"""Generate docs/card-image-prompts.md — a brief you can hand to ChatGPT (or any
image model) to illustrate every fat-santa card, with the exact output filename
for each. Regenerate after card changes: python3 scripts/gen_image_prompts.py
"""
import csv, re


def slug(name):
    s = name.lower().replace("&", "and")
    s = re.sub(r"[’'`]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


FLAVOR = {
    "Money":    " (feature shiny gold coins)",
    "Reindeer": " (feature a cute cartoon reindeer)",
    "Sled":     " (feature a festive sleigh)",
    "Present":  " (feature beautifully wrapped presents)",
}

rows = list(csv.DictReader(open("data/fat_santa_cards.csv")))
order = {"Money": 0, "Reindeer": 1, "Sled": 2, "Present": 3, "Action": 4, "Rest": 5}
rows.sort(key=lambda r: (order.get(r["types"], 9), int(r["cost"].lstrip("$")), r["name"]))

out = []
out.append("# fat-santa — card art brief\n")
out.append("Please generate **one illustration per card** listed below "
           f"({len(rows)} cards total). Hand this whole file to the image model.\n")
out.append("## Style (apply to every image)\n")
out.append("- Playful, whimsical **Christmas storybook** illustration — a cohesive set, "
           "the same style across all cards.\n"
           "- Bright, warm festive palette (reds, greens, gold, snow white); soft shading.\n"
           "- A single clear subject, centered, on a simple / uncluttered background.\n"
           "- **No text, letters, numbers, or logos anywhere in the image.**\n"
           "- Portrait orientation, **1024 × 1536 px**, PNG.\n")
out.append("## Output file names (IMPORTANT)\n")
out.append("- Save each image as a **PNG** using the exact `filename` given for that card.\n"
           "- File names are all lowercase, words separated by hyphens, no spaces or "
           "punctuation (e.g. `Santa's Piggy Bank` -> `santas-piggy-bank.png`).\n"
           "- Put every file in one folder named `card-art/`.\n")
out.append("---\n")

cur = None
for r in rows:
    if r["types"] != cur:
        cur = r["types"]
        out.append(f"\n## {cur} cards\n")
    name = r["name"]
    fn = slug(name) + ".png"
    effect = r["text"].replace("\n", "; ")
    flavor = FLAVOR.get(r["types"], "")
    out.append(f"### {name}")
    out.append(f"- **filename:** `{fn}`")
    out.append(f"- **type / cost:** {r['types']} · {r['cost']}")
    out.append(f"- **card effect (context, do NOT draw as text):** {effect}")
    out.append(f"- **prompt:** A playful whimsical Christmas storybook illustration of "
               f"*{name}*{flavor} — festive North Pole style, bright warm colors, "
               f"single centered subject, simple background, no text.\n")

open("docs/card-image-prompts.md", "w").write("\n".join(out) + "\n")
print("wrote docs/card-image-prompts.md for", len(rows), "cards")
