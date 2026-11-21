# AUDIT — r10-final.png (THIRD audit, adversarial)

- File: `r10-final.png`, 1024×1024 RGB
- Method: PIL crops of every region upscaled 3–8× into `/tmp/audit21c/` (LANCZOS + one NEAREST cross-check on Panel 3), every crop read, text transcribed letter-by-letter from the pixels. 300px downscale also made and read (`24_downscale300.png`).
- **Overall verdict: NOT zero-defect. The builder's "all fixed" claim is FALSE.** Two material defects survive — one is the exact Panel 3 defect the builder claimed to have fixed, the other is a sheared letter in the CARACAS brief label. Claims (1), (5), (6), (7) genuinely pass; claim (4) passes on its main points with one minor residue; claims (2) and (3) fail.

---

## DEFECTS — MATERIAL

### M1. Panel 3 subline is STILL misspelled and STILL overflows — claim (3) FAILS
Evidence: `/tmp/audit21c/10_panel3_zoom.png`, `30_panel3_subline_L.png`, `31_panel3_subline_NN.png` (NEAREST, un-interpolated pixels), `32_panel3_fullrules.png`.

Pixel transcription, line 1: **"Trump. Xi & Putin sian"**
- T-r-u-m-p, then a baseline dot with no comma tail visible — reads as a full stop, not the intended comma in "Trump, Xi & Putin sign".
- "Xi" clean; "&" clean; "Putin" present (its "u" glyph is slightly malformed but readable).
- Final word: s-i-**a**-n = **"sian"**, not "sign". The third letter is a two-storey "a" with no descender; there is no "g". Spelling defect confirmed in both LANCZOS and NEAREST renders, so it is in the source pixels, not an upscaling artefact.

Pixel transcription, line 2: "reconciliation declaration" — spelling correct, but **containment fails on the left**: the initial "r" of "reconciliation" starts **left of Panel 3's left vertical rule**, in Panel 2's column space, and the vertical rule is interrupted/absent at exactly that line's height (rule is visible above it beside "SUMMIT" and below it beside the flags). The line therefore overflows its panel. (On the right, "declaration" ends at/just inside the right rule — no clear overflow into Panel 4; the proven overflow is leftward into Panel 2, which is the same class of defect the claim denied.)

### M2. CARACAS brief label: initial "C" is sheared — claim (2) FAILS in part
Evidence: `/tmp/audit21c/42_caracas_label2.png` (8×), `17_briefs_mid.png`, `43_briefs_full_right.png`.

The label reads **"ᶜARACAS —"**: the first letter is only a small top-hook fragment of a C, at roughly half letter height; the left and lower strokes of the C are missing. The fragment sits well inside the column (the column's left rule is visible further left in the same crop), so this is a defective glyph in the image, not a crop or column-edge clip. Every other brief label (SUMY, JAKARTA, ROME, MEXICO CITY, KHARTOUM, NEW DELHI, BAYELSA, KABUL) has complete initial letters.

What in claim (2) DOES hold: the body text "Venezuela rejects world / court over Essequibo dispute" is in clean, correctly spelled glyphs (V-e-n-e-z-u-e-l-a / r-e-j-e-c-t-s / w-o-r-l-d / c-o-u-r-t / o-v-e-r / E-s-s-e-q-u-i-b-o / d-i-s-p-u-t-e), and line 2 does **not** overflow the column's right rule — "dispute" ends with a clear margin before the rule (`33_caracas_wide.png`).

---

## DEFECTS — MINOR

### m1. CARACAS (and JAKARTA/ROME) briefs are in a mismatched patched typeface
Evidence: `43_briefs_full_right.png`, `33_caracas_wide.png`, `16_briefs_top.png`.
The CARACAS body text is set in a narrower, taller, condensed face and indented further right than the standard brief face used by SUMY, MEXICO CITY, KHARTOUM, NEW DELHI, BAYELSA and KABUL. The JAKARTA + ROME block shows the same condensed face and extra indentation. Wording is correct and legible, but the patch seam is visible to the eye. Related layout inconsistency: there is **no horizontal separator rule between the JAKARTA brief and the ROME brief** — they run together in one ruled block, while every other pair of briefs is rule-separated.

### m2. Taiwan pictogram carries a detached edge sliver
Evidence: `/tmp/audit21c/36_taiwan_island.png` (8×), `06_markets_right2.png`.
The Taiwan island's main body is whole — continuous black outline, grey fill, centre star, pointed southern tip; it is not cut through. However, a thin black curved sliver, detached from the main outline by a gap of background, runs down its east/south-east edge — a leftover slice fragment beside the island. Claim (4)'s "whole, not sliced" is therefore only substantially, not cleanly, met.

### m3. Panel 4 subline drops the intended dash
Evidence: `11_panel4_zoom.png`. Image: "Food checks end / 100,000 youth visas a year" on two lines with no "—" between the clauses. Intended: "Food checks end — 100,000 youth visas a year". Wording otherwise exact.

---

## DEFECTS — COSMETIC

- c1. Markets band patch residue: faint extra horizontal strokes under the pictograms of columns 1–2, and a row of tiny dots under the NVIDIA chip pictogram (`05_markets_left2.png`, `06_markets_right2.png`).
- c2. Panel 12: the Capitol dome's spire touches the "t" of "unconstitutionally" (`15_panel12_zoom.png`). Text remains fully legible and "budget" is intact.
- c3. Panel 9 illustration: a small stray virus/sun-like icon at top-right of the arch scene, unrelated to the Iraq story (`14_panels_row3.png`).
- c4. Masthead world-map box: its left/bottom border is broken and gappy (`01_masthead.png`). The map itself is unaffected.

---

## CLAIM-BY-CLAIM VERDICTS (the 7 builder claims)

1. **ROME brief label present — PASS.** "ROME — Workers & students / walk out over pay and / living costs", clean glyphs (`20_briefs_rome_zoom.png`, `16_briefs_top.png`).
2. **CARACAS brief clean, no overflow — FAIL (see M2, m1).** Body text clean and inside the right rule, but the label's initial C is sheared and the block is in a mismatched patched face.
3. **Panel 3 subline correct and contained — FAIL (see M1).** Reads "Trump. Xi & Putin sian"; line 2 overflows the left rule into Panel 2.
4. **MARKETS TODAY pictograms/sub-lines — PASS with minor residue (m2).** All four pictograms fall: descending bar chart (Asia), descending line ending in × (Anthropic), descending line inside chip + descending line ending in × (NVIDIA), down arrow + island + descending line ending in × (Taiwan) (`07_markets_pictograms.png`). All second sub-lines fully legible, none cut or sheared: "— worst since 2020", "as selloff deepens", "in six weeks", "— worst since 1990" (`04_markets_band.png`, `05`, `06`). "1990": the final 0 is a complete closed oval (`35_taiwan_1990.png`). Taiwan island whole except the detached sliver in m2.
5. **World map has zero text labels — PASS.** Continent outlines only; no letters anywhere on the map (`03_worldmap.png`, `01_masthead.png`).
6. **Panel 12 number and subline — PASS.** Number is "12" with no full stop after it and no ghost smudge around it — background clean at 8× (`34_panel12_number.png`, corroborated by `39_row3_numbers.png`). Subline: "Court: 2022 budget / passed unconstitutionally"; "budget" = b-u-d-g-e-t, intact (`15_panel12_zoom.png`).
7. **Panel 5 chip arrow falls — PASS.** The arrow on the chip zigzags from upper-left down to an arrowhead at lower-right, ending well below its start (`13_panel5_zoom.png`).

---

## FULL TRANSCRIPTION (from the pixels)

**Edition line:** LATE EDITION — ALL THE DAY'S NEWS IN ONE PAGE
**Masthead:** THE WORLD TODAY
**Date:** SATURDAY, 21 NOVEMBER 2026
**Dateline:** KYIV • WARSAW • BRUSSELS • RIYADH
**Corner box:** MARKETS / ASIA ▼ −8.5% WEEK / WALL ST ▼ / TAIWAN ▼ −17% — all three arrows ▼ (fall). Consistent with band and tape.

**MARKETS TODAY band:**
1. ASIA'S WORST WEEK / Asia-Pacific shares sink 8.5% / — worst since 2020
2. ANTHROPIC SLIDES / Record $81B IPO fades / as selloff deepens
3. NVIDIA AT A LOW / Chip giant sheds $2 trillion / in six weeks
4. TAIWAN TANKS / Shares down 17% this week / — worst since 1990

**Tape:** NASDAQ ▼ · S&P 500 ▼ · NIKKEI ▼ −5% · TAIPEI ▼ −17% WEEK · MSCI ASIA ▼ −8.5% · WORLD ▼ 7TH DAY — exact, all ▼.

**Panels** (all 12 present, numbered 1–12 in order, none duplicated or missing; illustrations match labels):
1. RUSSIA POUNDS UKRAINE / 400+ drones & 110+ missiles / — three Kyiv bridges hit — drones, missiles, Kyiv skyline, bridges ✔
2. MISSILES REACH POLAND / Russian missile & drone / violate NATO airspace — Polish flag, missile, jet ✔
3. TRILATERAL SUMMIT / **[as printed: "Trump. Xi & Putin sian" — see M1]** / reconciliation declaration — US, China, Russia flags + handshake ✔
4. UK–EU RESET / Food checks end / 100,000 youth visas a year — Union Jack, EU flag, market stalls, two youths ✔
5. NVIDIA PROBED / California subpoenas chip / giant — SEC inquiry — chip, "SUBPOENA" document, gavel ✔
6. SAUDIS DOWN MISSILES / Three Houthi ballistic missiles / intercepted at Riyadh — missiles over Riyadh skyline ✔
7. MYANMAR DEFIES COURT / Generals reject genocide / verdict as biased — scales, gavel, boats ✔
8. MEASLES SURGE / US cases near 6,000 — / worst outbreak in decades — US map with virus icons, clinic ✔
9. IRAQ MOVES IN / Army enters militia stronghold / held 12 years — Iraq flag, victory arch, soldiers ✔
10. DENMARK FOILS PLOT / Russian plot to kill / Ukrainian rapper stopped — Danish flag, shield with ✓, crossed-out microphone ✔
11. BERLIN SUMMIT / Coalition of the willing / backs Ukraine talks — Brandenburg Gate ringed by flags ✔
12. SPENDING LAW VOIDED / Court: 2022 budget / passed unconstitutionally — scroll, Capitol dome, gavel ✔ (US Capitol imagery for a story whose court is not specified in the brief; noted, not scored as a text defect)

**AROUND THE WORLD IN BRIEF** (all 9 intended briefs present, in order, none duplicated/missing):
- SUMY — HIMARS strike kills 20 Russian commanders
- JAKARTA — Indonesia asks Google why 19,000 YouTube accounts were removed
- ROME — Workers & students walk out over pay and living costs
- MEXICO CITY — Caravan of 300 migrants crosses into southern Mexico
- KHARTOUM — Army says RSF strongholds dismantled in West Kordofan
- NEW DELHI — IndusInd Bank sacks ex-CEO, seeks pay clawback
- CARACAS — Venezuela rejects world court over Essequibo dispute **[label's C sheared — see M2]**
- BAYELSA — Rescuers search after funeral barge capsizes in Nigeria
- KABUL — UN warns ISIS-K is gaining drones in Afghanistan

**Black bar:** EU APPROVES €1 BILLION IN MILITARY AID FOR UKRAINE • FRANCE CALLS UN SECURITY COUNCIL MEETING AFTER KYIV STRIKES — exact, € glyph present, clean (`37_blackbar2.png`).

**Internal consistency:** Asia −8.5% agrees across corner box, band and tape; Taiwan −17% agrees across corner box, band and tape (as TAIPEI); no figure contradicts another anywhere on the page.

---

## 300px DOWNSCALE LEGIBILITY (`24_downscale300.png`)

Legible at 300px: masthead, date, dateline, MARKETS TODAY headlines, all 12 panel headlines, black-bar headline, corner-box figures. Marginal: Markets band sub-lines and panel sub-lines are blurred but their word shapes are partly discernible. Illegible: the briefs column body text (only the "AROUND THE WORLD IN BRIEF" heading and some labels register). This is a density limit of the one-page design rather than a print defect, but at thumbnail size the briefs — a third of the page's stories — cannot be read.

---

## BOTTOM LINE

Do not ship as "all fixed". Two material defects remain: **Panel 3 still prints "sian" for "sign" and its second line still breaks out of the panel (leftward)**, and **the CARACAS label's initial C is a sheared fragment**. Fix those two, the Taiwan sliver (m2) and the JAKARTA/ROME separator + typeface patch (m1) if a clean pass is required. Everything else on the page — masthead, corner box, tape, map, Panels 1, 2, 4–12 text, Markets headlines/sub-lines/pictogram directions, Panel 12, Panel 5 arrow, black bar — verified clean from the pixels.
