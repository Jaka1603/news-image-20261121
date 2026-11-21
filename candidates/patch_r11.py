#!/usr/bin/env python3
"""Round-11: r10 -> r11. Panel 3 fixed properly: restore its rules from
r1 (earlier erases ate them), re-typeset BOTH subline lines centred
inside x455-640 in Liberation Bold 15. CARACAS label re-typeset (its
original C glyph is a flattened smear)."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ECB = "/usr/share/fonts/truetype/noto/NotoSans-ExtraCondensedBold.ttf"
LIBB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
rng = np.random.default_rng(32)

r1 = Image.open("r1-c1.png").convert("RGB")
img = Image.open("r10-final.png").convert("RGB")


def paper(box, sample_box):
    arr = np.array(img).astype(int)
    sx0, sy0, sx1, sy1 = sample_box
    med = np.median(arr[sy0:sy1, sx0:sx1].reshape(-1, 3), axis=0)
    x0, y0, x1, y1 = box
    noise = rng.normal(0, 3.0, (y1 - y0, x1 - x0, 1))
    fill = np.clip(med + noise, 0, 255).astype(np.uint8)
    img.paste(Image.fromarray(fill), (x0, y0))


def render(text, font_path, size, target_w=None):
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
    return crop


# ---- panel 3: restore rules, erase sublines, re-typeset centred
img.paste(r1.crop((453, 498, 458, 552)), (453, 498))
img.paste(r1.crop((638, 498, 643, 552)), (638, 498))
paper((458, 503, 638, 545), (995, 640, 1005, 670))
CENTRE = (455 + 640) // 2
l1 = render("Trump, Xi & Putin sign", LIBB, 15)
img.paste(l1, (CENTRE - l1.width // 2, 510), l1)
l2 = render("reconciliation declaration", LIBB, 15, target_w=162)
img.paste(l2, (CENTRE - l2.width // 2, 526), l2)

# ---- CARACAS label
paper((856, 774, 991, 791), (995, 640, 1005, 670))
lab = render("CARACAS —", ECB, 13)
img.paste(lab, (859, 775), lab)

img.save("r11-final.png")
print("saved r11-final.png; L1 w", l1.width, "L2 w", l2.width,
      "label w", lab.width)
