# AUDIT — r11-final.png (FOURTH audit, adversarial)

Image: 1024×1024 RGB. Method: PIL crops of every region upscaled 3–10× into `/tmp/audit21d/`, each read from the pixels and transcribed letter-by-letter. Builder claims (1)–(7) treated as unproven until seen.

**Headline verdict: NOT clean. 2 material defects remain — both are patch seams the builder's claim list does not cover. All *text content* is now correct; the failures are structural (a destroyed column rule and a leftover glyph fragment).**

---

## DEFECTS

### MATERIAL

**M1 — CARACAS patch destroys the briefs column's right rule.**
The thin right border of the AROUND THE WORLD IN BRIEF column is **absent for the entire height of the CARACAS block** (label + both body lines). In its place, a **thick black vertical bar (≈4–5× the rule weight) floats displaced ~15px OUTSIDE the column**, spanning the two body lines. Below the CARACAS separator the thin rule resumes at its correct x; above the block it also exists (beside "seeks pay clawback") — so the border is interrupted exactly and only where the patch sits. The horizontal separator under the CARACAS body also stops short into empty space where the rule should be.
Evidence: `/tmp/audit21d/caracas_label.png` (rule ends above the block; thick bar begins at right edge), `/tmp/audit21d/caracas_body_rule.png` (no thin rule beside either body line; thick displaced bar; thin rule resuming below, offset left of the bar), `/tmp/audit21d/briefs_mid.png`, `/tmp/audit21d/briefs_bottom_caracas.png`.
Consequence for claim (2): the claim says line 2 does "not overflow the column's right rule" — there **is** no right rule beside this brief to measure against. The text itself does not cross the column's nominal boundary, but the rule the claim relies on has been destroyed by the patch.

**M2 — Stray truncated text fragment in panel 2, at the panel 2/3 seam.**
Immediately left of the shared vertical rule between panels 2 and 3, at the exact baseline of panel 3's "reconciliation declaration" line, panel 2 contains a clipped fragment: **"r" + a partial round glyph ("ro…")**, cut off by the rule. It belongs to no intended line — panel 2's own subline ends one line higher at "violate NATO airspace". It is the visible tail of a pre-patch text line that the panel-3 patch did not fully cover. Panel 3's own two lines are clean and inside its rules (see claim 3), but the seam leaks.
Evidence: `/tmp/audit21d/seam_panel23.png` (8×: "…rone / …ace" of panel 2 at left, fragment "r◐" centre, rule, panel 3 "Tru…/rec…" at right), `/tmp/audit21d/07_panel3_detail.png`, `/tmp/audit21d/panel03.png`.

### MINOR

**m1 — JAKARTA + ROME are one visibly patched block in the wrong typography, with a missing separator.**
Both briefs are indented ~12px relative to every other brief and set in a noticeably narrower condensed typeface, unlike the bold sans used by SUMY, MEXICO CITY, KHARTOUM, NEW DELHI, BAYELSA and KABUL. There is **no horizontal separator rule between JAKARTA and ROME** — every other adjacent pair of briefs has one (SUMY↓rule, ROME-block↓rule, MEXICO CITY↓rule, KHARTOUM↓rule, NEW DELHI↓rule, CARACAS↓rule, BAYELSA↓rule). "Google why" is set so tight the "e…w" nearly touch ("Googlewhy" at a glance); "were" has an abnormal internal gap ("w ere"). All words remain legible and spelled correctly.
Evidence: `/tmp/audit21d/jakarta_rome.png` (6×), `/tmp/audit21d/briefs_top.png`.

**m2 — CARACAS typography is foreign to the column (independent of M1's rule damage).**
Label "CARACAS —" and body are set in a different, lighter condensed face than all eight other briefs; the body is indented relative to its own label and to the column's left edge used by the other briefs. Even if the rule were repaired, the block would still read as pasted-in.
Evidence: `/tmp/audit21d/caracas_label.png`, `/tmp/audit21d/briefs_mid.png`.

**m3 — Stray line fragments along the bottom of the MARKETS TODAY band.**
Below the pictograms, floating above the band's bottom rule: column 1 has a full extra horizontal line segment under its bar chart; column 2 has two segments (one thick, one thin) under its chart; column 3 has a faint dotted row under its chip. The vertical dividers between band columns also terminate in tiny dangling ticks below their proper ends. These are remnants of a previous axis/rule layer, not part of any pictogram.
Evidence: `/tmp/audit21d/markets_bottom_seam.png` (6×), `/tmp/audit21d/05_markets_pictograms.png`, `/tmp/audit21d/06_tape.png` (top edge).

### COSMETIC

**c1 — World-map box (top-left) border is incomplete.** The left vertical rule is broken mid-height with small protruding ticks at the break, and the top rule's right end is not closed. Pre-existing art flaw, not a patch seam. No text is involved.
Evidence: `/tmp/audit21d/03_worldmap_left.png`, `/tmp/audit21d/worldmap_box_bottom.png` (bottom rule and corner are intact).

**c2 — Glyph quirks that do not change any reading.** "IndusInd" (NEW DELHI brief): the capital I after "Indus" renders like a lowercase l. Panel 5 chip arrowhead is an open triangle outline rather than a filled head. A few isolated paper-speck dots on the map and near panel 12's number (verified: not punctuation — nothing sits between "12" and "SPENDING").
Evidence: `/tmp/audit21d/briefs_mid.png`, `/tmp/audit21d/panel05.png`, `/tmp/audit21d/panel12_number_full.png`.

---

## BUILDER CLAIMS — VERIFIED ONE BY ONE

1. **ROME brief label present — TRUE.** "ROME — Workers & students / walk out over pay and / living costs", label and body complete and correctly spelled (`briefs_top.png`, `jakarta_rome.png`). Caveat: the block carries defect m1 (wrong typeface, indented, no separator above ROME within the block).
2. **CARACAS brief — TEXT TRUE, CLAIM FAILS OVERALL.** Label reads "CARACAS —"; at 8× both C's are complete, normal open curves (C-A-R-A-C-A-S) (`caracas_label.png`). Body: "Venezuela rejects world / court over Essequibo dispute" — every glyph clean, "Essequibo" E-s-s-e-q-u-i-b-o intact. Line 2 ("court over Essequibo dispute") ends inside the column's nominal right boundary. **But** the column's right rule beside this brief does not exist — it is interrupted for the whole block and replaced by a thick bar displaced outside the column (M1), and the block's typography is foreign (m2). The patched area is the most visible seam on the page.
3. **Panel 3 subline — TRUE for panel 3 itself.** "Trump, Xi & Putin sign" — the comma after "Trump" is a real comma, present at 6×; "sign" is s-i-g-n, clean. "reconciliation declaration" spelled in full. Both lines sit fully inside panel 3's rules (panel spans ≈x455–640; line 2's final "n" clears the right rule), and panel 3's left and right vertical rules are continuous top-to-bottom (`07_panel3_detail.png`). **However** the patch leaks into panel 2 as a truncated "ro…" fragment at the same baseline (M2) — the seam is not clean even though panel 3's interior is.
4. **MARKETS TODAY pictograms and sublines — TRUE.** All four pictograms FALL: (1) four bars strictly descending left→right; (2) line chart descending overall to a low ×; (3) chip-internal line descending + companion chart descending to ×; (4) down arrow beside Taiwan + chart descending to ×. Second sublines all fully legible: "— worst since 2020", "as selloff deepens", "in six weeks", "— worst since 1990" (final 0 is a closed oval). Taiwan island pictogram is whole — complete outline, pointed southern tip, star marker inside (`04_markets_band.png`, `05_markets_pictograms.png`). Caveat: stray fragments under the pictograms (m3).
5. **World map zero text labels — TRUE.** The masthead map contains only continent outlines and a few island/speck dots; no letters, numbers or labels anywhere on it (`03_worldmap_left.png`). (The Iraq flag in panel 9 carries its own Arabic script as part of the flag — that is flag artwork, not a map label.)
6. **Panel 12 — TRUE.** Number is "12" with **no full stop** after it (verified at 10×, `panel12_number_full.png`). Subline: "Court: 2022 budget / passed unconstitutionally" — "budget" b-u-d-g-e-t fully intact (`panel12_detail.png`).
7. **Panel 5 chip arrow falls — TRUE.** The line on the chip zigzags down-right and terminates in an arrowhead at the lowest-right point, pointing down-right (`panel05.png`, `panel5_detail.png`).

---

## FULL TRANSCRIPTION (from the pixels)

- Edition line: `LATE EDITION — ALL THE DAY'S NEWS IN ONE PAGE`
- Masthead: `THE WORLD TODAY`
- Date: `SATURDAY, 21 NOVEMBER 2026`
- Dateline: `KYIV • WARSAW • BRUSSELS • RIYADH`
- Corner box: `MARKETS / ASIA ▼ −8.5% / WEEK / WALL ST ▼ / TAIWAN ▼ −17%`
- MARKETS TODAY band:
  1. `ASIA'S WORST WEEK / Asia-Pacific shares sink 8.5% / — worst since 2020` + descending bars
  2. `ANTHROPIC SLIDES / Record $81B IPO fades / as selloff deepens` + descending chart
  3. `NVIDIA AT A LOW / Chip giant sheds $2 trillion / in six weeks` + chip & descending chart
  4. `TAIWAN TANKS / Shares down 17% this week / — worst since 1990` + ↓, Taiwan island, descending chart
- Tape: `NASDAQ ▼ · S&P 500 ▼ · NIKKEI ▼ −5% · TAIPEI ▼ −17% WEEK · MSCI ASIA ▼ −8.5% · WORLD ▼ 7TH DAY`
- Panels:
  1. `RUSSIA POUNDS UKRAINE / 400+ drones & 110+ missiles / — three Kyiv bridges hit` — drones/missiles over Kyiv skyline and bridges ✓ matches
  2. `MISSILES REACH POLAND / Russian missile & drone / violate NATO airspace` — Polish flag, missile, jet ✓ (plus stray fragment M2 at its right edge)
  3. `TRILATERAL SUMMIT / Trump, Xi & Putin sign / reconciliation declaration` — US, China, Russia flags + handshake ✓
  4. `UK–EU RESET / Food checks end / 100,000 youth visas a year` — UK & EU flags, market stalls, two youths with backpacks ✓
  5. `NVIDIA PROBED / California subpoenas chip / giant — SEC inquiry` — chip with falling arrow, "SUBPOENA" document, gavel ✓
  6. `SAUDIS DOWN MISSILES / Three Houthi ballistic missiles / intercepted at Riyadh` — missiles over Riyadh skyline ✓
  7. `MYANMAR DEFIES COURT / Generals reject genocide / verdict as biased` — scales, gavel, boats ✓
  8. `MEASLES SURGE / US cases near 6,000 — / worst outbreak in decades` — US map with virus markers, clinic ✓
  9. `IRAQ MOVES IN / Army enters militia stronghold / held 12 years` — Iraq flag, victory arch, soldiers ✓
  10. `DENMARK FOILS / Russian plot to kill / Ukrainian rapper stopped` — Danish flag, shield-check, crossed-out microphone ✓ (headline wraps as "DENMARK FOILS" on one line; subline carries the rest — matches intended content)
  11. `BERLIN SUMMIT / Coalition of the willing / backs Ukraine talks` — Brandenburg Gate ringed by flags ✓
  12. `SPENDING LAW VOIDED / Court: 2022 budget / passed unconstitutionally` — scroll, Capitol dome, gavel ✓
- Briefs (`AROUND THE WORLD IN BRIEF`), all 9 present, none duplicated, in order:
  1. `SUMY — HIMARS strike kills 20 Russian commanders`
  2. `JAKARTA — Indonesia asks Google why 19,000 YouTube accounts were removed` (patched block, m1)
  3. `ROME — Workers & students walk out over pay and living costs` (patched block, m1)
  4. `MEXICO CITY — Caravan of 300 migrants crosses into southern Mexico`
  5. `KHARTOUM — Army says RSF strongholds dismantled in West Kordofan`
  6. `NEW DELHI — IndusInd Bank sacks ex-CEO, seeks pay clawback`
  7. `CARACAS — Venezuela rejects world court over Essequibo dispute` (patched block, M1 + m2)
  8. `BAYELSA — Rescuers search after funeral barge capsizes in Nigeria`
  9. `KABUL — UN warns ISIS-K is gaining drones in Afghanistan`
- Black bar: `EU APPROVES €1 BILLION IN MILITARY AID FOR UKRAINE • FRANCE CALLS UN SECURITY COUNCIL MEETING AFTER KYIV STRIKES`

## INTERNAL CONSISTENCY
- Asia: corner −8.5% WEEK = band col 1 "sink 8.5% — worst since 2020" = tape "MSCI ASIA ▼ −8.5%" ✓
- Taiwan: corner −17% = band col 4 "down 17% this week" = tape "TAIPEI ▼ −17% WEEK" ✓
- Wall St: corner ▼ (no figure) = tape NASDAQ ▼ / S&P 500 ▼ (no figures) ✓
- Nikkei −5% appears only on the tape; nothing contradicts it. No panel or brief is missing or duplicated (12/12 panels, 9/9 briefs). All illustrations match their labels.

## 300px DOWNSCALE LEGIBILITY
At 300×300 (`/tmp/audit21d/downscale300.png`): masthead, date line, MARKETS TODAY headlines, all 12 panel headlines and the black bar remain legible; band sublines and panel sublines are partially readable; the briefs column and tape are grey texture (expected at this density — not a defect). Neither M1 nor M2 is discernible at 300px; both are plainly visible at full size and unmissable at 4–8× zoom.

## BOTTOM LINE
Every word of intended content is present, correctly spelled and consistent — claims (1), (4), (5), (6), (7) verified true in full; claim (3) true inside panel 3. **Claim (2) fails as stated**: the CARACAS text is fixed but its patch destroyed the column's right rule and left a thick displaced bar outside the column (M1). One further material seam the claims never mention: the truncated "ro…" fragment leaking into panel 2 (M2). Fix those two seams (plus the JAKARTA/ROME separator + typeface, m1) before calling this final.
