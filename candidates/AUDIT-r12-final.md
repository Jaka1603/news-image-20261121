# AUDIT — r12-final.png (FIFTH / adversarial audit)

**Image:** `r12-final.png`, 1024×1024 RGB
**Method:** PIL crops of every region upscaled 3–8× into `/tmp/audit21e/` (31 crops), each read and transcribed letter-by-letter from the pixels. Builder claims were NOT trusted; every claimed fix was re-verified independently.
**Auditor stance:** adversarial — image assumed flawed until each region was personally cleared.

---

## VERDICT SUMMARY

**Material defects: NONE. Minor defects: NONE affecting content. Cosmetic observations: 3 (listed at the end, none requiring a fix for correctness).**

All seven builder claims from the previous audits are **VERIFIED FIXED** from the pixels. Full transcription matches the intended content exactly, with internal consistency across corner box / band / tape.

---

## CLAIM-BY-CLAIM VERIFICATION

### (1) ROME brief label present — ✅ VERIFIED
Crop `30_jakarta_rome.png` (6×) and `20_briefs_top.png` (5×):
`ROME — Workers & students / walk out over pay and / living costs`
R-O-M-E, real em dash, real ampersand, body complete and clean. The ROME block directly follows the JAKARTA block.

### (2) CARACAS brief — ✅ VERIFIED on all four sub-points
Crops `21_briefs_mid.png`, `23_caracas_rule.png` (6×), `31_caracas_label.png` (8×), `29_right_rule_strip.png` (full-height edge strip):
- Label reads **CARACAS —** letter-by-letter: C-A-R-A-C-A-S. The first C is a complete, normal C (full curve, open right side); the second C is likewise normal. Em dash present.
- Body: `Venezuela rejects world / court over Essequibo dispute` — every word clean, no garbling, no doubled or missing letters.
- Line 2 (`court over Essequibo dispute`) sits fully inside the column.
- The briefs column's thin right rule runs **continuously** beside the CARACAS block (and the full column height, per the edge strip); the paper to the right of the rule is clean cream — **no displaced thick bar outside the column**.

### (3) Panel 3 subline — ✅ VERIFIED on all sub-points
Crops `09_panel3.png` (5×), `25_panel3_subline.png` (8×), `10_panel2_3_boundary.png` (4×, spans both panels):
- Line 1: `Trump, Xi & Putin sign` — a **real comma** follows "Trump"; the verb is **"sign"** (s-i-g-n), correctly spelled.
- Line 2: `reconciliation declaration` — complete.
- Both lines lie fully inside panel 3's rules; the vertical rules on both sides of panel 3 are continuous for the panel's full height.
- Panel 2's right margin at the same height contains only its own jet silhouette and clean paper — **no stray text fragment**.

### (4) MARKETS TODAY pictograms & sublines — ✅ VERIFIED
Crops `04_markets_band.png` (3×), `05_markets_pictograms.png` (5×), `28_taiwan_pict.png` (7×):
- Pictogram 1 (ASIA): bar chart with bars descending left→right — FALLS.
- Pictogram 2 (ANTHROPIC): line chart descending overall, ending low with an × marker — FALLS.
- Pictogram 3 (NVIDIA): chip icon whose interior line descends, plus a companion descending line with × — FALLS.
- Pictogram 4 (TAIWAN): explicit down arrow + descending line with × — FALLS.
- Second sublines fully legible: `— worst since 2020` (0 closed), `as selloff deepens`, `in six weeks`, `— worst since 1990` (0 closed).
- Taiwan island: complete, unbroken outline with star marker — whole.

### (5) World map zero text labels — ✅ VERIFIED
Crop `03_worldmap.png` (6×): outline world map only (Americas, Africa, Europe/Asia, Australia). No letters, words or labels anywhere on or around the map; only continent outlines, island specks and paper grain.

### (6) Panel 12 — ✅ VERIFIED
Crops `19_panel12.png` (5×), `26_panel12_detail.png` (7×):
- Panel number reads **12** with **no full stop** after it.
- Subline: `Court: 2022 budget / passed unconstitutionally` — "budget" intact (b-u-d-g-e-t); "unconstitutionally" spelled in full and correctly.

### (7) Panel 5 chip arrow falls — ✅ VERIFIED
Crops `12_panel5.png` (5×), `27_panel5_chip.png` (7×): the line drawn on the chip starts high at left, zigzags, then drops steeply to a small triangular arrowhead at the **low** right end. Net direction is unambiguously DOWN. The arrow falls.

---

## FULL TRANSCRIPTION (from the pixels)

**Edition line:** LATE EDITION — ALL THE DAY'S NEWS IN ONE PAGE
**Masthead:** THE WORLD TODAY
**Date:** SATURDAY, 21 NOVEMBER 2026
**Dateline:** KYIV • WARSAW • BRUSSELS • RIYADH
**Corner box:** MARKETS / ASIA ▼ −8.5% WEEK / WALL ST ▼ / TAIWAN ▼ −17% (all three triangles point DOWN)

**MARKETS TODAY band:**
1. ASIA'S WORST WEEK — Asia-Pacific shares sink 8.5% — worst since 2020
2. ANTHROPIC SLIDES — Record $81B IPO fades as selloff deepens
3. NVIDIA AT A LOW — Chip giant sheds $2 trillion in six weeks
4. TAIWAN TANKS — Shares down 17% this week — worst since 1990

**Tape:** NASDAQ ▼ · S&P 500 ▼ · NIKKEI ▼ −5% · TAIPEI ▼ −17% WEEK · MSCI ASIA ▼ −8.5% · WORLD ▼ 7TH DAY (all ▼ point down)

**Panels:**
1. RUSSIA POUNDS UKRAINE — 400+ drones & 110+ missiles — three Kyiv bridges hit. *Illus: drones over a city with bridges — matches.*
2. MISSILES REACH POLAND — Russian missile & drone violate NATO airspace. *Illus: Polish flag (white over red, correct), missile, jet — matches.*
3. TRILATERAL SUMMIT — Trump, Xi & Putin sign reconciliation declaration. *Illus: US, China, Russia flags + handshake — matches.*
4. UK–EU RESET — Food checks end / 100,000 youth visas a year. *Illus: Union Jack, EU flag, market stalls, two young travellers — matches.*
5. NVIDIA PROBED — California subpoenas chip giant — SEC inquiry. *Illus: chip with falling line, document headed SUBPOENA, gavel — matches.*
6. SAUDIS DOWN MISSILES — Three Houthi ballistic missiles intercepted at Riyadh. *Illus: missiles over a city skyline — matches.*
7. MYANMAR DEFIES COURT — Generals reject genocide verdict as biased. *Illus: scales of justice, gavel, boats — court theme matches.*
8. MEASLES SURGE — US cases near 6,000 — worst outbreak in decades. *Illus: US map with virus markers, clinic — matches.*
9. IRAQ MOVES IN — Army enters militia stronghold held 12 years. *Illus: Iraq flag (red/white/black, green script), monumental arch, soldiers — matches.*
10. DENMARK FOILS — Russian plot to kill Ukrainian rapper stopped. *Illus: Danish flag (white cross on red, correct), shield with check, microphone under prohibition sign — matches.*
11. BERLIN SUMMIT — Coalition of the willing backs Ukraine talks. *Illus: Brandenburg Gate ringed by national flags — matches.*
12. SPENDING LAW VOIDED — Court: 2022 budget passed unconstitutionally. *Illus: scroll, domed capitol building, gavel — matches.*

Panels 1–12 all present, in order, none duplicated, none missing.

**Briefs — AROUND THE WORLD IN BRIEF (9/9 present, in intended order):**
- SUMY — HIMARS strike kills 20 Russian commanders
- JAKARTA — Indonesia asks Google why 19,000 YouTube accounts were removed
- ROME — Workers & students walk out over pay and living costs
- MEXICO CITY — Caravan of 300 migrants crosses into southern Mexico
- KHARTOUM — Army says RSF strongholds dismantled in West Kordofan
- NEW DELHI — IndusInd Bank sacks ex-CEO, seeks pay clawback
- CARACAS — Venezuela rejects world court over Essequibo dispute
- BAYELSA — Rescuers search after funeral barge capsizes in Nigeria
- KABUL — UN warns ISIS-K is gaining drones in Afghanistan

**Black bar:** EU APPROVES €1 BILLION IN MILITARY AID FOR UKRAINE • FRANCE CALLS UN SECURITY COUNCIL MEETING AFTER KYIV STRIKES (€ symbol correct)

**Internal consistency:** ASIA −8.5% (corner) = 8.5% (band) = MSCI ASIA −8.5% (tape) ✓ · TAIWAN −17% (corner) = 17% (band) = TAIPEI −17% WEEK (tape) ✓ · WALL ST ▼ consistent with NASDAQ ▼ / S&P 500 ▼ on the tape ✓ · every ▼ on the page points down; no ▲ anywhere ✓.

---

## COSMETIC OBSERVATIONS (not content defects; no fix required)

1. **Faint ghost strokes under the markets pictograms** (`05_markets_pictograms.png`): a thin extra horizontal line sits below the axis in column 1, two short stroke segments below the axis in column 2, and faint dots below the chip in column 3; column 4 has none. They read as faint duplicate-axis remnants at 5× zoom, are barely visible at full-page size, and do not form letters, numbers or a rising chart. Cosmetic only.
2. **JAKARTA/ROME share one ruled section** (`30_jakarta_rome.png`): unlike the other briefs, there is no horizontal separator rule between the JAKARTA and ROME blocks, and the CARACAS body lines are indented slightly differently from the other briefs. Typesetting inconsistency only; all text is complete and correct.
3. **Soft grey smudge below the panel 5 chip** (`27_panel5_chip.png`) and a small ambiguous sun/gear motif at the top-right of panel 9's illustration: illustration-level artefacts, no text impact.

---

## 300px DOWNSCALE LEGIBILITY REPORT

At 300×300 (`/tmp/audit21e/down300.png`): masthead THE WORLD TODAY, the date line, MARKETS corner box figures, the MARKETS TODAY band headlines, all 12 panel headlines, the briefs heading, and the black-bar headline remain legible. Panel sublines and brief body text are not legible at 300px — expected at this information density and not a defect of the artwork at its native 1024px, where every line was verified letter-by-letter above.

---

## FINAL VERDICT PER REGION

- Masthead / edition / date / dateline: **zero defects**
- Corner markets box: **zero defects**
- World map: **zero defects** (zero labels)
- MARKETS TODAY band (text + pictograms + Taiwan): **zero content defects** (cosmetic ghost strokes noted)
- Tape: **zero defects**
- Panels 1–12: **zero defects** (incl. panel 3 comma/sign, panel 5 falling chip arrow, panel 12 number/budget)
- Briefs column (incl. ROME, CARACAS, right rule): **zero content defects** (cosmetic separator/indent inconsistency noted)
- Black bar: **zero defects**

**Overall: NO material or minor content defects found. The image passes the fifth audit. The three cosmetic observations above are the only imperfections detectable at 5–8× zoom, and none alters, obscures or contradicts any intended content.**
