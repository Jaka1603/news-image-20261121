#!/usr/bin/env python3
"""Round-6: r5 -> r6. Map labels removed by perimeter-median fill with
feathered edges (map interior first restored from r1)."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

rng = np.random.default_rng(26)
r1 = Image.open("r1-c1.png").convert("RGB")
img = Image.open("r5-final.png").convert("RGB")
img.paste(r1.crop((16, 76, 202, 216)), (16, 76))
arr = np.array(img).astype(int)
lum = arr.mean(axis=2)

boxes = [(98, 79, 132, 90), (38, 110, 68, 130), (48, 118, 114, 142),
         (116, 108, 158, 130), (26, 152, 72, 174)]
for (x0, y0, x1, y1) in boxes:
    per = []
    for xx in range(x0, x1):
        per.append(arr[y0, xx])
        per.append(arr[y1 - 1, xx])
    for yy in range(y0, y1):
        per.append(arr[yy, x0])
        per.append(arr[yy, x1 - 1])
    per = np.array(per)
    keep = per[lum[y0:y1, x0:x1].mean() >= 0]  # placeholder, replaced below
    mask_per = []
    for (yy, xx) in ([(y0, x) for x in range(x0, x1)] +
                     [(y1 - 1, x) for x in range(x0, x1)] +
                     [(y, x0) for y in range(y0, y1)] +
                     [(y, x1 - 1) for y in range(y0, y1)]):
        if lum[yy, xx] > 190:
            mask_per.append(arr[yy, xx])
    med = np.median(np.array(mask_per), axis=0) if mask_per else \
        np.array([244, 241, 233])
    w, h = x1 - x0, y1 - y0
    noise = rng.normal(0, 3.5, (h, w, 1))
    fill = np.clip(med + noise, 0, 255).astype(np.uint8)
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, w - 1, h - 1], radius=3, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(2))
    img.paste(Image.fromarray(fill), (x0, y0), mask)

img.save("r6-final.png")
print("saved r6-final.png")
