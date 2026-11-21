#!/usr/bin/env python3
"""Round-9: r8 -> r9. Repairs for audit #2 findings:
- band sublines restored from r1 (pictogram erase boxes had eaten them)
- Taiwan island restored from r1; falling chart redrawn right of it
- panel 12 'budget' e restored from r1
- panel 3 subline line 2 re-typeset inside the panel (was overflowing)
- CARACAS brief body re-typeset (line 1 mushy, line 2 overflowing)
- ghost smudge after '12' refilled with local ring median."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ECB = "/usr/share/fonts/truetype/noto/NotoSans-ExtraCondensedBold.ttf"
LIBB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
rng = np.random.default_rng(29)
INK = (15, 15, 15)

r1 = Image.open("r1-c1.png").convert("RGB")
img = Image.open("r8-final.png").convert("RGB")


def paper(box, sample_box):
    arr = np.array(img).astype(int)
    sx0, sy0, sx1, sy1 = sample_box
    med = np.median(arr[sy0:sy1, sx0:sx1].reshape(-1, 3), axis=0)
    x0, y0, x1, y1 = box
    noise = rng.normal(0, 3.0, (y1 - y0, x1 - x0, 1))
    fill = np.clip(med + noise, 0, 255).astype(np.uint8)
    img.paste(Image.fromarray(fill), (x0, y0))


def typeset(text, font_path, size, ink_xy, target_w=None):
    f = ImageFont.truetype(font_path, size)
    tmp = Image.new("RGBA", (700, 80), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((10, 10), text, font=f, fill=(15, 15, 15, 255))
    a = np.array(tmp)[:, :, 3]
    rows = np.where(a.any(axis=1))[0]
    cols = np.where(a.any(axis=0))[0]
    crop = tmp.crop((cols[0], rows[0], cols[-1] + 1, rows[-1] + 1))
    if target_w and crop.width > target_w:
        crop = crop.resize((target_w, crop.height), Image.LANCZOS)
    img.paste(crop, (ink_xy[0], ink_xy[1]), crop)


# ---- 1. band sublines back from r1; NVIDIA pins redrawn; debris swept
img.paste(r1.crop((15, 324, 1010, 361)), (15, 324))
d = ImageDraw.Draw(img)
for px in (606, 616, 626):
    d.line([(px, 362), (px, 368)], fill=INK, width=2)
paper((90, 402, 765, 409), (60, 415, 120, 435))

# ---- 2. Taiwan island restored; falling chart redrawn at x>=868
img.paste(r1.crop((838, 355, 866, 408)), (838, 355))
paper((866, 360, 918, 407), (950, 415, 1000, 435))
d = ImageDraw.Draw(img)
d.line([(870, 400), (915, 400)], fill=INK, width=2)
d.line([(874, 371), (886, 381), (894, 376), (908, 390)], fill=INK, width=2)
d.line([(908, 390), (900, 389), (907, 382)], fill=INK, width=2)
for tx in (880, 892, 904):
    d.line([(tx, 392), (tx, 400)], fill=INK, width=2)

# ---- 3. panel 12: restore the 'e' of 'budget' from r1
img.paste(r1.crop((748, 844, 792, 870)), (748, 844))

# ---- 4. panel 3 subline line 2: one string, squeezed inside the panel
paper((438, 520, 655, 545), (450, 480, 540, 500))
typeset("reconciliation declaration", LIBB, 17, (445, 526), target_w=180)

# ---- 5. CARACAS body: one erase, two clean lines, rule redrawn
paper((860, 788, 1010, 819), (995, 830, 1005, 860))
d = ImageDraw.Draw(img)
d.line([(1004, 788), (1004, 819)], fill=INK, width=2)
typeset("Venezuela rejects world", ECB, 13, (865, 792))
typeset("court over Essequibo dispute", ECB, 13, (865, 804), target_w=118)

# ---- 6. '12' ghost: refill with ring median of nearby bright pixels
arr = np.array(img).astype(int)
lum = arr.mean(axis=2)
ring = []
for yy in range(804, 826):
    for xx in range(658, 680):
        if 666 <= xx < 671 and 812 <= yy < 818:
            continue
        if lum[yy, xx] > 200:
            ring.append(arr[yy, xx])
med = np.median(np.array(ring), axis=0)
noise = rng.normal(0, 2.5, (6, 5, 1))
fill = np.clip(med + noise, 0, 255).astype(np.uint8)
img.paste(Image.fromarray(fill), (666, 812))

img.save("r9-final.png")
print("saved r9-final.png")
