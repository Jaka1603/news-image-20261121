#!/usr/bin/env python3
"""Round-4: remove '12.' full stop; feathered texture transplants over
the map label fills so no rectangular seams remain. r3 -> r4."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

rng = np.random.default_rng(24)
img = Image.open("r3-final.png").convert("RGB")


def paper(box, sample_box):
    arr = np.array(img).astype(int)
    sx0, sy0, sx1, sy1 = sample_box
    med = np.median(arr[sy0:sy1, sx0:sx1].reshape(-1, 3), axis=0)
    x0, y0, x1, y1 = box
    noise = rng.normal(0, 3.0, (y1 - y0, x1 - x0, 1))
    fill = np.clip(med + noise, 0, 255).astype(np.uint8)
    img.paste(Image.fromarray(fill), (x0, y0))


# '12.' full stop
paper((653, 805, 661, 813), (700, 818, 760, 830))

# map: feathered ocean-texture transplants over the five label boxes
DONOR = (115, 160)  # clean ocean inside the map box
boxes = [(100, 72, 130, 86), (40, 112, 66, 128), (50, 120, 112, 140),
         (118, 110, 156, 128), (28, 154, 70, 172)]
base = img.copy()
for (x0, y0, x1, y1) in boxes:
    w, h = x1 - x0, y1 - y0
    tex = base.crop((DONOR[0], DONOR[1], DONOR[0] + w, DONOR[1] + h))
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, w - 1, h - 1], radius=4, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(2.5))
    img.paste(tex, (x0, y0), mask)

img.save("r4-final.png")
print("saved r4-final.png")
