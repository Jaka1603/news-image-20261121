# ADVERSARIAL AUDIT — r8-final.png (news-image-20261121)

**Auditor role:** adversarial checker. Method: PIL crops of the 1024×1024 original, upscaled 3–8× into `/tmp/audit21b/` (35 crops), every crop read and transcribed letter-by-letter from the pixels.
**Overall verdict: ❌ FLAWED — DO NOT SHIP.** 4 material defects, 3 minor, 6 cosmetic. Two of the seven previously reported defects are **not** actually fixed, and the r8 patch pass introduced fresh damage (cut sublines, a broken word in panel 12).

---

## 1. Prior-defect scorecard (each verified from pixels, not trusted)

| # | Prior defect | Status in r8 | Evidence |
|---|---|---|---|
| 1 | ROME brief had no city label | ✅ FIXED | `z_rome.png`, `09a_briefs_top.png`: prints "ROME — Workers & students…" |
| 2 | CARACAS printed "Venezuule" | ❌ **NOT FIXED** | `z_caracas2.png` (8×): "Venezuule" is gone but the replacement line is garbled in a mismatched font: **"Vene7uela reierts world"** (see M1) |
| 3 | Panel 3 "reconciliia" (doubled i) | ✅ FIXED (spelling) | `z_panel3_subline.png`: "reconciliation" = r-e-c-o-n-c-i-l-i-a-t-i-o-n, single i. BUT a new glyph defect sits in the same subline: "sign" prints as **"siqn"** (see m1) |
| 4 | All 4 MARKETS pictograms rising under falling headlines | ✅ FIXED | `04a–04d`: bars descend left→right; Anthropic line falls to an ✗; NVIDIA chip line + side line both fall to an ✗; Taiwan line falls to an ✗ beside a ↓ arrow. All net-falling |
| 5 | Map locator labels misplaced (KYIV ×2, WARSAW over Central Asia, RIYADH over S. America) | ✅ FIXED | `03_map.png` (6×): outline world map with **zero text labels** anywhere |
| 6 | Panel 12 number printed "12." | ✅ FIXED (with residue) | `z_panel12_head.png` (6×): prints "12" with no full stop; a faint grey ghost smudge remains where the stop was removed (see c3) |
| 7 | Panel 5 chip icon had rising-trend arrow | ✅ FIXED | `z_panel5_icon.png` (6×): chip line zigzags down and ends in a **downward** arrowhead; net direction clearly falling |

---

## 2. Defect list (ranked)

### MATERIAL

**M1 — CARACAS brief body is garbled; prior defect #2 replaced by a worse one.**
Crop `z_caracas2.png` (8×) / `09b_briefs_mid.png`. Heading prints "**ᑕARACAS —**" — the initial letter is a small curved "ᑕ"-like glyph, not a C matching the other capitals. Body line 1 is set in a visibly different, distorted typeface and transcribes glyph-by-glyph as:
`Vene7uela reierts world`
- "Venezuela": the **z renders as "7"**, surrounding vowels malformed (e→ə-like glyphs, an apparent extra i-stroke).
- "rejects": prints "reierts" — j→i, c→r.
- "world": o's are open ∩-shapes ("wnrld"-like).
Line 2 ("court over Essequibo dispute") is in the normal font and spelled correctly, but see m3. A reader cannot read line 1 as printed; it only decodes as "Venezuela rejects world" from context.

**M2 — MARKETS TODAY: three of the four second sublines are physically cut in half by patch rectangles.**
Crop `z_markets_sublines.png` (5×) / `04a–04c`. A light patch block overlaps the subline row:
- ASIA cell: "— worst since 2020" — tops of all glyphs sheared off; only the lower ~60% of the line survives.
- ANTHROPIC cell: "as selloff deepens" — only the upper arcs of the letters peek above the patch edge; **illegible** without prior knowledge.
- NVIDIA cell: "in six weeks" — only lower fragments visible; half-height text.
The fourth (TAIWAN) subline escaped the cut but has its own defect (M4). Intended full lines are not readable as printed in 3 of 4 cells.

**M3 — Panel 12: the word "budget" is broken — printed "budg␣t".**
Crop `z_panel12_head.png` (6×) / `p12.png`. Subline transcribes: "Court: 2022 **budg[ pale vertical patch bar ]t** / passed unconstitutionally". The "e" of "budget" is obliterated by a light-grey rectangular patch artifact, leaving "budg t" with a visible gap/ghost glyph. The headline word of the subline is misspelled as printed.

**M4 — MARKETS / TAIWAN cell: "1990" is malformed — prints "199∩".**
Crop `04d_markets_taiwan.png` (5×). Subline: "— worst since 1990" where "since" has distorted glyphs (c/e malformed) and the final digit of 1990 is an **open ∩ shape, not a closed 0** — the year reads "199n"/"199∩". Wrong year as printed.

### MINOR

**m1 — Panel 3: "sign" prints as "siqn".** Crop `z_panel3_subline.png` (8×): "Trump, Xi & Putin **siqn**" — the g is a malformed q-like glyph (closed bowl + right descender). Word is recoverable from context but wrong as printed. (In the same panel, subline line 2 "reconciliation declaration" is set wider than the panel and **crosses both vertical panel rules** into panels 2 and 4.)

**m2 — Panel 10 headline omits "PLOT".** Crops `08_row3.png` / `p10.png`: headline prints "10 DENMARK FOILS" only; intended headline is "DENMARK FOILS PLOT" ("plot" survives only inside the subline "Russian plot to kill…").

**m3 — CARACAS line 2 overflows the sidebar.** Crop `z_caracas2.png`: "court over Essequibo dispute" is set too wide — the final "te" of "dispute" crosses the sidebar's right border rule.

### COSMETIC

**c1 — Visible patch seams throughout the MARKETS band.** Light rectangular patch blocks with a different paper tone sit behind/around all four pictograms (`04_markets_band_full.png`), and ghost fragments of the old chart axes remain under the new art (stray bracket/baseline debris under cells 1–2, dotted residue under the cell-3 chip).

**c2 — Taiwan island graphic sliced in half.** Crop `04d`: the Taiwan island pictogram is cut by a straight vertical patch edge; its right half is missing.

**c3 — Ghost residue after panel number "12".** Crop `z_panel12_head.png`: faint grey smudge where the removed full stop (prior defect #6) was patched out.

**c4 — Missing divider rule between JAKARTA and ROME briefs.** Crops `09a` / `z_rome.png`: the two briefs sit inside one light patch block with **no horizontal rule between them**, unlike every other brief pair in the column.

**c5 — Stray virus icon inside panel 9.** Crop `08_row3.png`: a small spiky virus ball (panel 8's motif) sits at the top-right inside panel 9's Iraq illustration area.

**c6 — Panel 12 illustration shows the US Capitol dome** for a story about a European constitutional court voiding a 2022 budget law (scroll + gavel are on-topic; the Capitol is the wrong building). Generic-art mismatch only.

---

## 3. Full transcription — as printed (from the pixels)

**Edition line:** `LATE EDITION — ALL THE DAY'S NEWS IN ONE PAGE` ✅
**Masthead:** `THE WORLD TODAY` ✅
**Date:** `SATURDAY, 21 NOVEMBER 2026` ✅
**Dateline:** `KYIV • WARSAW • BRUSSELS • RIYADH` ✅
**Corner box:** `MARKETS / ASIA ▼ −8.5% WEEK / WALL ST ▼ / TAIWAN ▼ −17%` ✅
**World map (top-left):** outline map, **no text labels** ✅

**MARKETS TODAY band:**
1. `ASIA'S WORST WEEK` / `Asia-Pacific shares sink 8.5%` / `— worst since 2020` **[line cut by patch — M2]** / pictogram: 4 bars descending ✅ falling
2. `ANTHROPIC SLIDES` / `Record $81B IPO fades` / `as selloff deepens` **[~illegible, covered by patch — M2]** / pictogram: line chart falling to ✗ ✅
3. `NVIDIA AT A LOW` / `Chip giant sheds $2 trillion` / `in six weeks` **[half-covered by patch — M2]** / pictograms: chip with falling line + falling line to ✗ ✅
4. `TAIWAN TANKS` / `Shares down 17% this week` / `— worst since 199∩` **[final 0 malformed — M4]** / pictograms: ↓ arrow, Taiwan island (sliced — c2), falling line to ✗ ✅ falling

**Tape:** `NASDAQ ▼ · S&P 500 ▼ · NIKKEI ▼ −5% · TAIPEI ▼ −17% WEEK · MSCI ASIA ▼ −8.5% · WORLD ▼ 7TH DAY` ✅

**Panels:**
1. `RUSSIA POUNDS UKRAINE` / `400+ drones & 110+ missiles — three Kyiv bridges hit` ✅ — drones over city + bridges, matches ✅
2. `MISSILES REACH POLAND` / `Russian missile & drone violate NATO airspace` ✅ — Polish flag (white/red) + missile + jet ✅
3. `TRILATERAL SUMMIT` / `Trump, Xi & Putin siqn` **[sic — m1]** / `reconciliation declaration` ✅ spelling — US/China/Russia flags + handshake ✅
4. `UK–EU RESET` / `Food checks end — 100,000 youth visas a year` (prints as two lines "Food checks end / 100,000 youth visas a year") ✅ — Union Jack + EU flag + market stalls + youths ✅
5. `NVIDIA PROBED` / `California subpoenas chip giant — SEC inquiry` ✅ — chip with **falling** arrow + document headed `SUBPOENA` + gavel ✅
6. `SAUDIS DOWN MISSILES` / `Three Houthi ballistic missiles intercepted at Riyadh` ✅ — missiles over Riyadh skyline ✅
7. `MYANMAR DEFIES COURT` / `Generals reject genocide verdict as biased` ✅ — scales of justice + gavel ✅
8. `MEASLES SURGE` / `US cases near 6,000 — worst outbreak in decades` ✅ — US map with virus icons + clinic ✅
9. `IRAQ MOVES IN` / `Army enters militia stronghold held 12 years` ✅ — Iraq flag + arch + soldiers ✅ (stray virus icon — c5)
10. `DENMARK FOILS` **[PLOT missing from headline — m2]** / `Russian plot to kill Ukrainian rapper stopped` ✅ — Danish flag + shield + barred microphone ✅
11. `BERLIN SUMMIT` / `Coalition of the willing backs Ukraine talks` ✅ — Brandenburg Gate + flag arc ✅
12. `SPENDING LAW VOIDED` — number prints `12` with **no full stop** ✅ / `Court: 2022 budg␣t passed unconstitutionally` **[e destroyed — M3]** — scroll + Capitol dome + gavel (c6)

**Briefs — AROUND THE WORLD IN BRIEF (9/9 present, none duplicated, none missing):**
- `SUMY — HIMARS strike kills 20 Russian commanders` ✅
- `JAKARTA — Indonesia asks Google why 19,000 YouTube accounts were removed` ✅ (divider missing below — c4)
- `ROME — Workers & students walk out over pay and living costs` ✅ **city label present**
- `MEXICO CITY — Caravan of 300 migrants crosses into southern Mexico` ✅
- `KHARTOUM — Army says RSF strongholds dismantled in West Kordofan` ✅
- `NEW DELHI — IndusInd Bank sacks ex-CEO, seeks pay clawback` ✅
- `CARACAS — Vene7uela reierts world court over Essequibo dispute` **[as printed; garbled — M1, m3]**
- `BAYELSA — Rescuers search after funeral barge capsizes in Nigeria` ✅
- `KABUL — UN warns ISIS-K is gaining drones in Afghanistan` ✅

**Black bar:** `EU APPROVES €1 BILLION IN MILITARY AID FOR UKRAINE • FRANCE CALLS UN SECURITY COUNCIL MEETING AFTER KYIV STRIKES` ✅ (€ glyph correct)

---

## 4. Consistency checks

- **Numbers agree everywhere they repeat:** Asia −8.5% (corner box = band cell 1 = tape MSCI ASIA −8.5%) ✅; Taiwan −17% (corner box = band cell 4 = tape TAIPEI −17% WEEK) ✅; Wall St ▼ consistent with tape NASDAQ ▼ / S&P 500 ▼ ✅; Nikkei −5% appears on tape only, contradicts nothing ✅. The failures are legibility/glyph failures, not value inconsistencies.
- **Counts:** 12/12 panels, numbered 1–12 in order, none duplicated or missing ✅. 9/9 briefs ✅. 4/4 markets cells ✅.
- **Illustration↔label:** all match except c5 (stray icon, panel 9) and c6 (Capitol, panel 12).
- **Chart direction:** all four MARKETS pictograms + panel 5 chip now fall ✅ (prior defects #4, #7 genuinely fixed).
- **Map:** label-free ✅ (prior defect #5 genuinely fixed).

## 5. 300px downscale legibility (`11_downscale300.png`)

At 300×300 the page still reads as a newspaper: edition line, THE WORLD TODAY, date, dateline, MARKETS TODAY + its four headlines, the tape (partially), all 12 panel headlines with numbers, the briefs header, and the black bar (just legible) survive. **No subline, brief body, or markets detail survives** — which means M1–M4 are invisible at thumbnail size and only appear at full resolution. Thumbnail approval would not have caught any of them.

## 6. Bottom line per region

- Masthead / date / dateline / corner box / tape / black bar: **zero defects.**
- World map: **zero defects** (prior #5 fixed).
- MARKETS TODAY band: **DEFECTIVE** — M2, M4, c1, c2.
- Panels 1, 2, 4, 5, 6, 7, 8, 11: **zero defects.**
- Panel 3: **DEFECTIVE** — m1 ("siqn"; subline overflows panel rules).
- Panel 9: cosmetic only (c5). Panel 10: minor (m2). Panel 12: **DEFECTIVE** — M3, plus c3/c6.
- Briefs column: **DEFECTIVE** — M1 + m3 (CARACAS), c4 (missing JAKARTA/ROME divider); other 8 briefs clean, ROME label fixed.
