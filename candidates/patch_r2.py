#!/usr/bin/env python3
"""Local PIL patches for r1-c1 -> r2-final (news-image-20261121).
Fixes: M1 ROME label, M2 map labels, M3 Venezuela, m1 falling band
pictograms, m2 reconciliation, cosmetic '12.' dot + panel-5 chip glyph."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC = "r1-c1.png"
DST = "r2-final.png"
ECB = "/usr/share/fonts/truetype/noto/NotoSans-ExtraCondensedBold.ttf"
LIBB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

rng = np.random.default_rng(21)
img = Image.open(SRC).convert("RGB")
W, H = img.size
arr = np.array(img).astype(int)


def paper(box, sample_box):
    """Fill box with local paper colour + grain."""
    sx0, sy0, sx1, sy1 = sample_box
    med = np.median(arr[sy0:sy1, sx0:sx1].reshape(-1, 3), axis=0)
    x0, y0, x1, y1 = box
    noise = rng.normal(0, 3.0, (y1 - y0, x1 - x0, 1))
    fill = np.clip(med + noise, 0, 255).astype(np.uint8)
    img.paste(Image.fromarray(fill), (x0, y0))


def typeset(text, font_path, size, ink_xy, target_w=None):
    """Render text; paste so its ink top-left lands at ink_xy.
    Optionally squeeze horizontally to target_w."""
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
    return crop.width, crop.height


INK = (15, 15, 15)

# ---- M3: CARACAS line 2 'Venezuule' -> 'Venezuela rejects world'
paper((860, 788), (995, 820)) if False else None
paper((860, 788, 990, 810), (995, 760, 1005, 790))
typeset("Venezuela rejects world", ECB, 13, (865, 792))

# ---- M1: JAKARTA + ROME block re-typeset (6 lines, ECB 12)
paper((860, 543, 990, 617), (995, 640, 1005, 670))
block = [
    ("JAKARTA — Indonesia asks", 113),
    ("Google why 19,000 YouTube", 113),
    ("accounts were removed", None),
    ("ROME — Workers & students", 112),
    ("walk out over pay and", None),
    ("living costs", None),
]
top = 547.0
for text, tw_ in block:
    typeset(text, ECB, 12, (865, int(round(top))), target_w=tw_)
    top += 11.4

# ---- m2: panel 3 'reconciliia' -> 'reconciliation'
paper((442, 522, 562, 542), (450, 480, 540, 500))
typeset("reconciliation", LIBB, 17, (445, 526))

# ---- M2: paint out the map locator's misplaced city labels
gray = np.array(img.convert("L"))
sub = (gray[78:216, 16:202] < 140)
lab = np.zeros(sub.shape, dtype=int)
cur = 0
from collections import deque
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
            fill = len(pts) / (h * w)
            # text blobs: short, wide-ish, dense; coastlines are sparse/thin
            if 4 <= h <= 13 and w >= 9 and fill >= 0.30:
                paper((16 + min(xs) - 1, 78 + min(ys) - 1,
                       16 + max(xs) + 2, 78 + max(ys) + 2),
                      (150, 190, 195, 210))

# ---- m1: falling pictograms in the MARKETS band
d = ImageDraw.Draw(img)
# ASIA: descending bars
paper((95, 360, 178, 402), (60, 415, 120, 435))
d.line([(100, 397), (172, 397)], fill=INK, width=2)
for i, bx in enumerate((104, 120, 136, 152)):
    d.rectangle([bx, 372 + i * 6, bx + 10, 397], outline=INK, width=2)
# ANTHROPIC: falling line chart (keep IPO doc at x>=338)
paper((258, 360, 336, 402), (240, 415, 300, 435))
d.line([(266, 366), (266, 397), (330, 397)], fill=INK, width=2)
d.line([(270, 372), (286, 381), (298, 376), (314, 389)], fill=INK, width=2)
d.line([(314, 389), (306, 388), (313, 381)], fill=INK, width=2)
# NVIDIA band cell: chip with falling arrow + small falling chart
paper((432, 360, 568, 402), (420, 415, 480, 435))
d.rectangle([446, 368, 484, 398], outline=INK, width=2)
for px in (452, 462, 472):
    d.line([(px, 362), (px, 368)], fill=INK, width=2)
    d.line([(px, 398), (px, 402)], fill=INK, width=2)
for py in (376, 386):
    d.line([(440, py), (446, py)], fill=INK, width=2)
    d.line([(484, py), (490, py)], fill=INK, width=2)
d.line([(453, 376), (461, 383), (467, 379), (477, 390)], fill=INK, width=2)
d.line([(496, 397), (560, 397)], fill=INK, width=2)
d.line([(500, 371), (516, 381), (528, 376), (546, 390)], fill=INK, width=2)
d.line([(546, 390), (538, 389), (545, 382)], fill=INK, width=2)
# TAIWAN: replace rising side chart with falling one (keep arrow + island)
paper((692, 360, 754, 402), (600, 415, 660, 435))
d.line([(698, 397), (748, 397)], fill=INK, width=2)
d.line([(702, 371), (716, 380), (727, 376), (742, 389)], fill=INK, width=2)
d.line([(742, 389), (734, 388), (741, 381)], fill=INK, width=2)

# ---- cosmetic: panel-5 chip glyph rising -> falling
paper((64, 724, 98, 758), (150, 730, 190, 760))
d.line([(68, 732), (76, 740), (82, 736), (92, 749)], fill=INK, width=2)
d.line([(92, 749), (84, 748), (91, 741)], fill=INK, width=2)

# ---- cosmetic: remove the stray full stop after panel number '12'
sub = (gray[820:875, 775:830] < 140)
lab2 = np.zeros(sub.shape, dtype=int)
cur = 0
for yy in range(sub.shape[0]):
    for xx in range(sub.shape[1]):
        if sub[yy, xx] and lab2[yy, xx] == 0:
            cur += 1
            q = deque([(yy, xx)])
            lab2[yy, xx] = cur
            pts = []
            while q:
                cy, cx = q.popleft()
                pts.append((cy, cx))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < sub.shape[0] and 0 <= nx < sub.shape[1] \
                            and sub[ny, nx] and lab2[ny, nx] == 0:
                        lab2[ny, nx] = cur
                        q.append((ny, nx))
            ys = [p[0] for p in pts]
            xs = [p[1] for p in pts]
            h = max(ys) - min(ys) + 1
            w = max(xs) - min(xs) + 1
            if h <= 5 and w <= 5 and len(pts) >= 6:
                paper((775 + min(xs) - 1, 820 + min(ys) - 1,
                       775 + max(xs) + 2, 820 + max(ys) + 2),
                      (850, 830, 900, 850))

img.save(DST)
print("saved", DST)
