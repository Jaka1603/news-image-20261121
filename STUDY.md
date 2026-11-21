# news-image-20261121 — study & candidate scores

Competition: news-image-20261121 ($100 pool: $20/$12/$6/$2×7/$1.20×40),
opens 2026-11-21T00:00:00Z, closes Mon 23 Nov 2026 07:00 WIB
(2026-11-23T00:00:00Z). One image summing up the world news of
**Saturday 21 November 2026**. Final file: PNG or JPEG, ≤ 1 MiB,
≤ 1024×1024, written to /output/entry.png by the entry program.

Judge (z-ai/glm-5.3-flash, pairwise), criteria in order:
(1) names the day + specific recognisable events OF 21 Nov 2026
(events before 13 Nov 2026 lose); (2) breadth — the day's most
consequential stories across regions and fields; (3) reads clearly
from the image alone, short labels, nothing false or
self-contradictory; (4) faithful, no hype; (5) craft — clean
composition, legible at ~300 px, no garbled text.

## Lessons carried in (Jaka's order: learn from the failures)

- news-image-20261117 final judge score collapsed to 37.30% and
  news-image-20261118 finished at 51.16% — both $0, despite high
  dev win-rates (95%+). The final heat judges every entry AFRESH:
  a dev win-rate is not a promise of anything.
- The 20261120 deep audit proved the builder's own "flawless"
  claim wrong: a duplicated "& &", a corner box contradicting
  the page's own band/tape AND the verified facts, and a
  truncated brief all survived spec-matching audits. Fixes
  applied this round:
  1. EVERY number/claim below is cross-checked against at
     least two independent reports before it enters the spec;
     where reports conflict, the page uses the conservative
     figure or drops the figure.
  2. INTERNAL CONSISTENCY is a first-class audit item: the
     corner box, the markets band and the tape are generated
     from one fact list and checked against each other.
  3. The audit is adversarial and independent (checker
     mindset, crop-zoom transcription of every region),
     run AFTER the build, and its verdict overrules the
     builder's score.
  4. No story from before 21 Nov is presented as the day's
     news (GTA VI's 19 Nov launch was considered and REJECTED
     for exactly this reason; the Anthropic IPO and the ICJ
     verdict appear only as their 21 Nov developments —
     the post-IPO selloff and Myanmar's rejection — never as
     yesterday's events restated).
  5. Timing caveat: this build ran on the morning of 21 Nov
     (WIB), while the day was still unfolding in Europe and
     the Americas. The spec uses only events already reported
     on 21 Nov (any time zone) by then. A refresh pass against
     the day's later developments is RECOMMENDED before the
     parent submits — the deadline is 23 Nov 07:00 WIB.

## The day's news (verified 21 Nov 2026 morning WIB,
## cross-checked across Reuters wire copy, CNN, The Times,
## Fox News, Al Jazeera and several news aggregators)

Twelve panel stories:

1. **Russia pounds Ukraine** — overnight into Friday, Russia
   fired 400+ drones and 110+ missiles (27 ballistic) in one
   of the war's largest barrages, hours after Putin left the
   Shenzhen trilateral; three Kyiv bridges over the Dnipro
   (Podilskyi, Darnytskyi, Pivdennyi) were hit; at least 8
   killed, 28 wounded (conservative figure — reports range
   8–9 dead). (CNN, The Times, Fox News, Reuters reports.)
2. **Missiles reach Poland** — two Russian missiles and a
   jet-powered drone violated Polish (NATO) airspace; debris
   at Nowy Lipowiec, Mołodycz and Rudnik nad Sanem; PM Tusk
   called it a deliberate provocation; Poland asks NATO for
   more forces. (The Times, CNN, multiple aggregators.)
3. **Trilateral summit fallout** — Trump, Xi and Putin signed
   a joint reconciliation declaration; Trump urged security
   cooperation and said he was too busy to meet Kim Jong-un
   on the Asia trip. (Aggregators carrying wire copy.)
4. **UK–EU reset deal** — at Friday's Brussels summit, PM
   Burnham agreed: most food/agri border checks end, a youth
   experience scheme of 100,000 visas a year (ages 18–31, up
   to 3 years), and linked emissions trading. (Reuters,
   The Times.) The claimed £17bn boost is stated
   inconsistently (£17bn/yr vs by 2040) — the figure is NOT
   printed.
5. **Nvidia probed** — California AG Bonta served an
   investigative subpoena on Nvidia (Thu) over China chip
   links and investor disclosure; the SEC is reported (WSJ)
   to be investigating too; the House Foreign Affairs
   Committee revealed 879,000 advanced Nvidia/AMD chips were
   approved for China sales Dec 2025–May 2026 (75,000
   Alibaba, 150,000 Tencent, 43,000 Baidu, 4,000 BYD).
   (Reuters summary, Insurance Journal, multiple reports.)
6. **Saudis down Houthi missiles** — early Saturday the
   Saudi-led coalition intercepted three Houthi ballistic
   missiles launched toward Riyadh, a day after the Riyadh
   tower hit and Friday's Jazan interceptions. (Al Jazeera
   live coverage, multiple aggregators, 21 Nov timestamps.)
7. **Myanmar defies the court** — Myanmar rejected the ICJ
   genocide verdict as "biased"; Malaysia finalised a deal
   with Turkey to resettle 10,000 Rohingya asylum seekers.
   (Aggregators, 21 Nov.)
8. **US measles surge** — CDC reported 5,838 cases as of
   19 Nov (reported Friday): the US total nears 6,000 in the
   worst outbreak in decades. (Reuters.)
9. **Iraq moves in** — Iraqi forces set up a command HQ at
   Jurf al-Sakhar on Friday, entering the Kataib Hezbollah
   stronghold held for 12 years. (AP via Reflector,
   aggregators.)
10. **Denmark foils a plot** — Denmark's PET thwarted an
    alleged Russian intelligence assassination plot; two
    Danes charged with being recruited by Russia to kill a
    Ukrainian rapper. (Aggregators + news summaries.)
11. **Berlin Ukraine summit** — a "coalition of the willing"
    summit in Berlin with Zelenskyy and US negotiators;
    Europeans seek an active role in Ukraine talks (Élysée).
    (Aggregators.)
12. **US spending law voided** — a federal appeals court
    (5th Circuit, 9–8) ruled the House unconstitutionally
    passed the 2022 $1.7 trillion spending bill by proxy
    voting. (Reuters, 21 Nov.)

Markets band facts (all Friday closes / week, Reuters):
- MSCI Asia-Pacific ex-Japan sank 8.5% this week — worst
  week since March 2020; world stocks fell a 7th straight
  day, longest streak since 2023.
- Taiwan shares fell ~17% this week — biggest weekly drop
  since 1990. Nikkei fell 5% on Friday.
- Anthropic's $81 billion IPO was the biggest in history;
  the shares closed +17% on Thursday's debut, then fell
  about 10% in Friday premarket as the AI selloff deepened.
- Nvidia hit a 52-week low ($145.98, −3.3% Thu), its sixth
  straight fall; it has shed ~$2 trillion in six weeks.
  Q3 revenue $115.84 billion beat estimates anyway.

Nine briefs ("Around the World in Brief"):
SUMY — HIMARS strike kills 20 Russian commanders;
JAKARTA — Indonesia asks Google why 19,000 YouTube accounts
were removed; ROME — workers & students walk out over pay
and living costs; MEXICO CITY — caravan of 300 migrants
crosses into southern Mexico; KHARTOUM — army says RSF
strongholds dismantled in West Kordofan; NEW DELHI —
IndusInd Bank sacks its ex-CEO and seeks a pay clawback;
CARACAS — Venezuela rejects the world court over the
Essequibo dispute with Guyana; BAYELSA — rescuers search
for survivors after a funeral barge capsizes; KABUL — UN
warns ISIS-K is gaining drones in Afghanistan.

Black-bar ticker: EU COUNCIL APPROVES €1 BILLION IN MILITARY
AID FOR UKRAINE • FRANCE CALLS UN SECURITY COUNCIL MEETING
AFTER THE KYIV STRIKES. (€7.9B was also mentioned in one
aggregator as an EU allocation; the €1 billion council
military-aid figure is the one printed, to stay conservative.)

Region/field sweep: Eastern Europe (war), Western Europe
(Poland/NATO, Berlin, Brussels), East Asia (summit), Middle
East (Riyadh, Iraq), North America (measles, court, Nvidia),
South Asia (IndusInd), Southeast Asia (Rohingya, Jakarta),
Latin America (caravan, Essequibo), Africa (Kordofan,
Bayelsa), plus markets, technology, health, justice and
diplomacy.

## Design

Same proven model as the 20261120 champion (r4-final):
dense B/W broadsheet front page, flat editorial illustration,
no photoreal faces — symbolic scenes only. Masthead
"THE WORLD TODAY", date line "SATURDAY, 21 NOVEMBER 2026",
edition line "LATE EDITION — ALL THE DAY'S NEWS IN ONE PAGE",
dateline strip "KYIV • WARSAW • BRUSSELS • RIYADH", a corner
markets box consistent with the band ("ASIA ▼ −8.5% WEEK /
WALL ST ▼ / TAIWAN ▼ −17%"), a MARKETS TODAY band with four
mini-panels + tape, 12 story panels, a 9-brief column and
the black ticker bar. Labels kept to 2–5 words + one tiny
subline; density comes from story count, never long text.
