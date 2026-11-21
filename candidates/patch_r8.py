#!/usr/bin/env python3
"""Round-8b: r6 -> r8. Ink-only transfer of the generated world map
into the true map-box interior (33,66)-(178,204). Tile thresholded so
only true ink lines (<130) survive; min-pooled to target size."""
import numpy as np
from PIL import Image

img = Image.open("r6-final.png").convert("RGB")
arr = np.array(img).astype(float)
r1 = np.array(Image.open("r1-c1.png").convert("RGB")).astype(float)

tile = np.array(Image.open(
    "media-generation-maptile-0-fc265b25-e002-4d51-aeed-"
    "1431c16da072.png").convert("L")).astype(float)
tile = np.where(tile < 130, tile, 245.0)  # kill paper flecks
F = 14
h2 = (tile.shape[0] // F) * F
w2 = (tile.shape[1] // F) * F
pooled = tile[:h2, :w2].reshape(h2 // F, F, w2 // F, F).min(axis=(1, 3))
nh, nw = pooled.shape
print("pooled", nw, nh)

IX0, IY0, IX1, IY1 = 33, 66, 178, 204
IW, IH = IX1 - IX0, IY1 - IY0
sample = r1[175:200, 150:175].reshape(-1, 3)
paper = np.median(sample[sample.mean(axis=1) > 200], axis=0)
inkcol = np.array([22.0, 22.0, 22.0])
arr[IY0:IY1, IX0:IX1] = paper
ox = IX0 + (IW - nw) // 2
oy = IY0 + (IH - nh) // 2
t = np.clip((pooled - 50) / 130.0, 0, 1)[:, :, None]
arr[oy:oy + nh, ox:ox + nw] = paper * t + inkcol * (1 - t)

Image.fromarray(arr.astype(np.uint8)).save("r8-final.png")
print("saved r8-final.png")
