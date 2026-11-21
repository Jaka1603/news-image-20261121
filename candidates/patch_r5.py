#!/usr/bin/env python3
"""Round-5: r3 -> r5. Restore map interior from r1 and remove its city
labels by per-column vertical interpolation of the local background;
remove the '12.' full stop by measured component bbox."""
import numpy as np
from PIL import Image
from collections import deque

rng = np.random.default_rng(25)
r1 = Image.open("r1-c1.png").convert("RGB")
img = Image.open("r3-final.png").convert("RGB")

# ---- map: restore interior, then interpolate-out the labels
img.paste(r1.crop((16, 76, 202, 216)), (16, 76))
arr = np.array(img).astype(float)


def interp_fill(box):
    x0, y0, x1, y1 = box
    top = arr[y0 - 3:y0, x0:x1].mean(axis=0)
    bot = arr[y1:y1 + 3, x0:x1].mean(axis=0)
    h = y1 - y0
    for i in range(h):
        t = (i + 0.5) / h
        row = top * (1 - t) + bot * t
        noise = rng.normal(0, 2.5, (x1 - x0, 1))
        arr[y0 + i, x0:x1] = np.clip(row + noise, 0, 255)


for box in [(98, 70, 132, 88), (38, 110, 68, 130), (48, 118, 114, 142),
            (116, 108, 158, 130), (26, 152, 72, 174)]:
    interp_fill(box)
img = Image.fromarray(arr.astype(np.uint8))

# ---- '12.' dot: find small baseline component right of the '2'
a = np.array(img.convert("L"))
sub = a[795:825, 640:675] < 140
lab = np.zeros(sub.shape, dtype=int)
cur = 0
best = None
for yy in range(sub.shape[0]):
    for xx in range(sub.shape[1]):
        if sub[yy, xx] and lab[yy, xx] == 0:
            cur += 1
            q = deque([(yy, xx)])
            lab[yy, xx] = cur
            pts = []
            while q:
                cy, cx = q.popleft()
                pts.append((cy, cx))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < sub.shape[0] and 0 <= nx < sub.shape[1] \
                            and sub[ny, nx] and lab[ny, nx] == 0:
                        lab[ny, nx] = cur
                        q.append((ny, nx))
            ys = [p[0] for p in pts]
            xs = [p[1] for p in pts]
            h = max(ys) - min(ys) + 1
            w = max(xs) - min(xs) + 1
            print("component:", 640 + min(xs), 795 + min(ys), "w", w, "h", h,
                  "n", len(pts))
            if h <= 6 and w <= 6:
                best = (640 + min(xs) - 1, 795 + min(ys) - 1,
                        640 + max(xs) + 2, 795 + max(ys) + 2)
if best:
    arr2 = np.array(img).astype(int)
    med = np.median(arr2[818:830, 700:760].reshape(-1, 3), axis=0)
    x0, y0, x1, y1 = best
    noise = rng.normal(0, 3.0, (y1 - y0, x1 - x0, 1))
    fill = np.clip(med + noise, 0, 255).astype(np.uint8)
    img.paste(Image.fromarray(fill), (x0, y0))
    print("dot painted:", best)
else:
    print("NO dot component found")

img.save("r5-final.png")
print("saved r5-final.png")
