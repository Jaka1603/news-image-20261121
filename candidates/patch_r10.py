#!/usr/bin/env python3
"""Round-10: r9 -> r10. Taiwan island fully restored from r1 (to x888);
the rising side chart east of it replaced with a falling chart."""
import numpy as np
from PIL import Image, ImageDraw

rng = np.random.default_rng(30)
INK = (15, 15, 15)
r1 = Image.open("r1-c1.png").convert("RGB")
img = Image.open("r9-final.png").convert("RGB")

img.paste(r1.crop((838, 355, 888, 408)), (838, 355))

arr = np.array(img).astype(int)
med = np.median(arr[415:435, 950:1000].reshape(-1, 3), axis=0)
noise = rng.normal(0, 3.0, (408 - 358, 965 - 888, 1))
fill = np.clip(med + noise, 0, 255).astype(np.uint8)
img.paste(Image.fromarray(fill), (888, 358))

d = ImageDraw.Draw(img)
d.line([(894, 400), (958, 400)], fill=INK, width=2)
d.line([(898, 371), (912, 381), (922, 376), (940, 390)], fill=INK, width=2)
d.line([(940, 390), (932, 389), (939, 382)], fill=INK, width=2)
for tx in (906, 920, 934):
    d.line([(tx, 392), (tx, 400)], fill=INK, width=2)

img.save("r10-final.png")
print("saved r10-final.png")
