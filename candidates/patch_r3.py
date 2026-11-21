#!/usr/bin/env python3
"""Round-3 patches: r2-final -> r3-final (news-image-20261121).
Band pictograms redone with correct cell geometry (restore strip from
r1 first), briefs slivers + Caracas L3, panel-3 'declaration', map
labels via ring-median fill, panel-5 chip glyph, '12.' dot."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ECB = "/usr/share/fonts/truetype/noto/NotoSans-ExtraCondensedBold.ttf"
LIBB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
rng = np.random.default_rng(23)

r1 = Image.open("r1-c1.png").convert("RGB")
img = Image.open("r2-final.png").convert("RGB")
INK = (15, 15, 15)


def paper(box, sample_box):
    arr = np.array(img).astype(int)
    sx0, sy0, sx1, sy1 = sample_box
    med = np.median(arr[sy0:sy1, sx0:sx1].reshape(-1, 3), axis=0)
    x0, y0, x1, y1 = box
    noise = rng.normal(0, 3.0, (y1 - y0, x1 - x0, 1))
    fill = np.clip(med + noise, 0, 255).astype(np.uint8)
    img.paste(Image.fromarray(fill), (x0, y0))


def ring_paper(box, pad=6):
    """Fill box with median of surrounding paper-ish ring pixels."""
    arr = np.array(img).astype(int)
    lum = arr.mean(axis=2)
    x0, y0, x1, y1 = box
    ring = []
    for yy in range(y0 - pad, y1 + pad):
        for xx in range(x0 - pad, x1 + pad):
            if x0 <= xx < x1 and y0 <= yy < y1:
                continue
            if 0 <= yy < 1024 and 0 <= xx < 1024 and lum[yy, xx] > 165:
                ring.append(arr[yy, xx])
    med = np.median(np.array(ring), axis=0)
    noise = rng.normal(0, 3.0, (y1 - y0, x1 - x0, 1))
    fill = np.clip(med + noise, 0, 255).astype(np.uint8)
    img.paste(Image.fromarray(fill), (x0, y0))


def typeset(text, font_path, size, ink_xy, target_w=None):
    f = ImageFont.truetype(font_path, size)
    tmp = Image.new("RGBA", (600, 80), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((10, 10), text, font=f, fill=(15, 15, 15, 255))
    a = np.array(tmp)[:, :, 3]
    rows = np.where(a.any(axis=1))[0]
    cols = np.where(a.any(axis=0))[0]
    crop = tmp.crop((cols[0], rows[0], cols[-1] + 1, rows[-1] + 1))
    if target_w and crop.width > target_w:
        crop = crop.resize((target_w, crop.height), Image.LANCZOS)
    img.paste(crop, (ink_xy[0], ink_xy[1]), crop)


# ---------- A. band pictograms: restore strip, redo with true cells
img.paste(r1.crop((15, 348, 1010, 408)), (15, 348))
d = ImageDraw.Draw(img)
# ASIA (cell 15-255): descending bars
paper((98, 352, 212, 407), (60, 415, 120, 435))
d.line([(100, 400), (172, 400)], fill=INK, width=2)
for i, bx in enumerate((104, 120, 136, 152)):
    d.rectangle([bx, 374 + i * 6, bx + 10, 400], outline=INK, width=2)
# ANTHROPIC (cell 255-511): falling chart
paper((338, 352, 452, 407), (300, 415, 360, 435))
d.line([(352, 366), (352, 400), (440, 400)], fill=INK, width=2)
d.line([(356, 372), (372, 382), (384, 376), (400, 389), (412, 384),
        (426, 395)], fill=INK, width=2)
d.line([(426, 395), (418, 394), (425, 387)], fill=INK, width=2)
# NVIDIA (cell 511-765): chip with falling arrow + falling chart
paper((585, 352, 690, 407), (600, 415, 660, 435))
d.rectangle([598, 368, 638, 400], outline=INK, width=2)
for px in (606, 616, 626):
    d.line([(px, 362), (px, 368)], fill=INK, width=2)
    d.line([(px, 400), (px, 404)], fill=INK, width=2)
for py in (378, 390):
    d.line([(592, py), (598, py)], fill=INK, width=2)
    d.line([(638, py), (644, py)], fill=INK, width=2)
d.line([(605, 376), (613, 383), (619, 379), (631, 390)], fill=INK, width=2)
d.line([(652, 400), (725, 400)], fill=INK, width=2)
d.line([(656, 371), (672, 381), (684, 376), (702, 390)], fill=INK, width=2)
d.line([(702, 390), (694, 389), (701, 382)], fill=INK, width=2)
# TAIWAN (cell 765-1010): falling side chart, island kept
paper((865, 352, 918, 407), (950, 415, 1000, 435))
d.line([(870, 400), (915, 400)], fill=INK, width=2)
d.line([(874, 371), (886, 381), (894, 376), (908, 390)], fill=INK, width=2)
d.line([(908, 390), (900, 389), (907, 382)], fill=INK, width=2)
for tx in (880, 892, 904):
    d.line([(tx, 392), (tx, 400)], fill=INK, width=2)

# ---------- B. briefs: glyph slivers + Caracas line 3
paper((854, 543, 865, 617), (995, 640, 1005, 670))
paper((854, 786, 865, 812), (995, 760, 1005, 790))
paper((860, 801, 990, 819), (995, 830, 1005, 860))
paper((854, 801, 865, 819), (995, 830, 1005, 860))
typeset("court over Essequibo dispute", ECB, 13, (865, 804))

# ---------- C. panel 3: restore 'declaration'
paper((558, 522, 650, 542), (450, 480, 540, 500))
typeset("declaration", LIBB, 17, (560, 526))

# ---------- D. map labels: ring-median paint
for box in [(100, 72, 130, 86), (40, 112, 66, 128), (50, 120, 112, 140),
            (118, 110, 156, 128), (28, 154, 70, 172)]:
    ring_paper(box)

# ---------- E. panel-5 chip glyph: restore, refill screen, falling zigzag
img.paste(r1.crop((45, 700, 200, 780)), (45, 700))
a = np.array(img.convert("L"))
ink = a < 140
sub = ink[705:775, 55:120]
rows = np.where(sub.any(axis=1))[0]
cols = np.where(sub.any(axis=0))[0]
print("chip outer bbox:", 55 + cols[0], 705 + rows[0], 55 + cols[-1],
      705 + rows[-1])
# inner screen: inset from outer bbox
ox0, oy0, ox1, oy1 = 55 + cols[0], 705 + rows[0], 55 + cols[-1], 705 + rows[-1]
sx0, sy0, sx1, sy1 = ox0 + 10, oy0 + 10, ox1 - 9, oy1 - 9
paper((sx0, sy0, sx1, sy1), (sx0 + 2, sy1 - 6, sx0 + 14, sy1 - 1))
d = ImageDraw.Draw(img)
zx0, zy0 = sx0 + 5, sy0 + 7
zx1, zy1 = sx1 - 5, sy1 - 6
d.line([(zx0, zy0), (zx0 + 9, zy0 + 8), (zx0 + 15, zy0 + 3),
        (zx1, zy1)], fill=INK, width=2)
d.line([(zx1, zy1), (zx1 - 8, zy1 - 1), (zx1 - 1, zy1 - 8)],
       fill=INK, width=2)

# ---------- F. panel 12 number dot
sub = ink[828:868, 630:685]
pts = [(630 + x, 828 + y) for y in range(sub.shape[0])
       for x in range(sub.shape[1]) if sub[y, x]]
print("panel12 zone ink x-range:", min(p[0] for p in pts),
      max(p[0] for p in pts), "y-range:", min(p[1] for p in pts),
      max(p[1] for p in pts))

img.save("r3-final.png")
print("saved r3-final.png")
