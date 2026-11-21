#!/usr/bin/env python3
"""Round-7b: r6 -> r7. Ink-only transfer of the generated world map
onto the page paper inside the map box (single clean blend)."""
import numpy as np
from PIL import Image

img = Image.open("r6-final.png").convert("RGB")
arr = np.array(img).astype(float)
r1 = np.array(Image.open("r1-c1.png").convert("RGB")).astype(float)

tile = Image.open(
    "media-generation-maptile-0-fc265b25-e002-4d51-aeed-"
    "1431c16da072.png").convert("L")
ta = np.array(tile)
ink_mask = ta < 200
rows = np.where(ink_mask.any(axis=1))[0]
cols = np.where(ink_mask.any(axis=0))[0]
crop = tile.crop((cols[0] - 8, rows[0] - 8, cols[-1] + 9, rows[-1] + 9))

IX0, IY0, IX1, IY1 = 20, 79, 200, 215
IW, IH = IX1 - IX0, IY1 - IY0
scale = min(IW / crop.width, IH / crop.height)
nw, nh = int(crop.width * scale), int(crop.height * scale)
small = np.array(crop.resize((nw, nh), Image.LANCZOS)).astype(float)

# page paper: bright pixels of the original map's empty ocean corner
sample = r1[175:210, 150:196].reshape(-1, 3)
paper = np.median(sample[sample.mean(axis=1) > 200], axis=0)
inkcol = np.array([22.0, 22.0, 22.0])

arr[IY0:IY1, IX0:IX1] = paper
ox = IX0 + (IW - nw) // 2
oy = IY0 + (IH - nh) // 2
t = np.clip((small - 40) / 110.0, 0, 1)[:, :, None]
arr[oy:oy + nh, ox:ox + nw] = paper * t + inkcol * (1 - t)

Image.fromarray(arr.astype(np.uint8)).save("r7-final.png")
print("saved r7-final.png; paper=", paper, "tile placed", nw, nh)
