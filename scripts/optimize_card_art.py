#!/usr/bin/env python3
"""Generate web-optimized copies of the full-res card art.

Reads the original PNGs in `card-art/*.png` (1024x1536 from ChatGPT) and
writes resized WebP copies to `card-art/web/<slug>.webp` for the website to
load. The originals are kept for print / archival. Re-run after adding art:

    python3 scripts/optimize_card_art.py

Target: 750px wide (retina-crisp for the on-screen cards and adequate for the
63mm print cards) at WebP quality 80.
"""
import os
from PIL import Image

SRC = "card-art"
DST = "card-art/web"
WIDTH = 750
QUALITY = 80

os.makedirs(DST, exist_ok=True)
pngs = sorted(f for f in os.listdir(SRC) if f.lower().endswith(".png"))
total_in = total_out = 0
for f in pngs:
    src = os.path.join(SRC, f)
    dst = os.path.join(DST, os.path.splitext(f)[0] + ".webp")
    im = Image.open(src).convert("RGB")
    w, h = im.size
    if w > WIDTH:
        im = im.resize((WIDTH, round(h * WIDTH / w)), Image.LANCZOS)
    im.save(dst, "WEBP", quality=QUALITY, method=6)
    total_in += os.path.getsize(src)
    total_out += os.path.getsize(dst)
print(f"{len(pngs)} images -> {DST}")
print(f"  in : {total_in/1048576:6.1f} MB (originals)")
print(f"  out: {total_out/1048576:6.1f} MB (webp)  avg {total_out/max(len(pngs),1)/1024:.0f} KB")
