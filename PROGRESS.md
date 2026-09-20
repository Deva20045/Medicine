# PULSE Medicine — Build Progress (single source of truth)

## Goal
A learner should **not need to read the PDF separately** after solving the questions.
Every line, table, diagram, flowchart, classification, value and exception of the book
scope (Book p705–1068) is converted into questions in strict book order.

## Book & page map
- Book: **Marrow Ed 8, Medicine Vol 3** — scan covers **Book pages 705–1070** (366 PDF pages).
- The scan has **no text layer**; content is read from rendered page images
  (e.g. `/home/user/ch1/*.png`), with background OCR kept for boundary checks only.
- Offsets (book page = PDF page + K):

| Part file (in `uploads/`) | PDF pages | K | Book pages |
|---|---|---|---|
| `Medicine_Vol3_Part1_pages_705-759.pdf` | 1–55 | 692 | 705–759 |
| `Medicine_Vol3_Part2_pages_760-823.pdf` | 1–64 | 759 | 760–823 |
| `Medicine_Vol3_Part3_pages_824-893.pdf` | 1–70 | 823 | 824–893 |
| `Medicine_Vol3_Part4_pages_894-964.pdf` | 1–71 | 893 | 894–964 |
| `Medicine_Vol3_Part5_pages_965-1034.pdf` | 1–70 | 964 | 965–1034 |
| `Medicine_Vol3_Part6_pages_1035-1070.pdf` | 1–36 | 1034 | 1035–1070 |

- Final content page = Book p1068 (p1069 blank, p1070 unnumbered Osler back cover).
- Formula: **Book page = PDF page + K** (K per part above).

## Roadmap — all 74 chapters listed from day one (status: LIVE / SOON)
| # | Chapter | Book start | Status |
|---|---|---|---|
| 1 | Development of Kidneys | p705 | **LIVE**
| 2 | Gross Anatomy of Kidney | p711 | **LIVE**
| 3 | Tubular Anatomy | p717 | **LIVE**
| 4 | Juxtaglomerular Apparatus | p726 | **LIVE**
| 5 | Glomerulus - Anatomy | p730 | **LIVE**
| 6 | Renal Physiology | p734 | **LIVE (page-anchored re-audit)**
| 7 | Urine Analysis | p740 | **LIVE (page-anchored re-audit)**
| 8 | Basic Approach to Kidney Disease and Renal Artery Stenosis | p748 | **LIVE (page-anchored re-audit)**
| 9 | Thrombotic Microangiopathy | p753 | **LIVE (page-anchored re-audit)**
| 10 | Glomerular Disease - Patterns | p756 | **LIVE (page-anchored re-audit)**
| 11 | Podocytopathies | p762 | **LIVE (page-anchored re-audit)**
| 12 | MPGN and IgA Nephropathy | p770 | **LIVE (page-anchored re-audit)**
| 13 | Post Streptococcal Glomerulonephritis | p775 | **LIVE (re-audited)**
| 14 | RPGN and Pulmonary Renal Syndrome | p778 | **LIVE (re-audited)**
| 15 | Familial Glomerular Syndromes | p783 | **LIVE (re-audited)**
| 16 | Ciliopathies | p786 | **LIVE (re-audited)**
| 17 | Chronic Tubulointerstitial Disease | p793 | **LIVE (re-audited)**
| 18 | Acute Kidney Injury | p796 | **LIVE (re-audited)**
| 19 | Chronic Kidney Disease | p805 | **LIVE (re-audited)**
| 20 | Anemia in Chronic Kidney Disease | p808 | **LIVE (re-audited)**
| 21 | CKD - Calciphylaxis and Cardiovascular changes | p811 | **LIVE (re-audited)**
| 22 | Diabetic Kidney Disease | p815 | **LIVE (re-audited)**
| 23 | Introduction to Acid Base Analysis | p819 | **LIVE**
| 24 | Metabolic Alkalosis | p824 | **LIVE**
| 25 | Methodology and Interpretation of ABG Analysis | p826 | **LIVE**
| 26 | Overview of Hormones | p830 | **LIVE**
| 27 | Physiology of Adrenal Cortex | p837 | **LIVE**
| 28 | Conn's Syndrome | p841 | **LIVE**
| 29 | Cushing's Syndrome | p844 | **LIVE**
| 30 | Addison's Disease | p849 | **LIVE**
| 31 | Adrenal Medulla : Part 1 | p852 | **LIVE**
| 32 | Adrenal Medulla : Part 2 | p858 | **LIVE**
| 33 | Basics of Bone and Mineral Metabolism | p863 | **LIVE**
| 34 | Calcium Metabolism | p874 | **LIVE**
| 35 | Hypercalcemia | p877 | **LIVE**
| 36 | Hypocalcemia | p883 | **LIVE**
| 37 | Phosphorus Metabolism | p887 | **LIVE**
| 38 | Magnesium Metabolism | p892 | **LIVE**
| 39 | Osteoporosis | p895 | **LIVE**
| 40 | Basics of Thyroid Gland | p898 | **LIVE**
| 41 | Thyroid Function Tests | p902 | **LIVE**
| 42 | Hypothyroidism | p905 | **LIVE**
| 43 | Thyrotoxicosis and Thyroiditis | p910 | **LIVE**
| 44 | Introduction to Diabetes Mellitus and Classification | p917 | **LIVE**
| 45 | Insulin Physiology and Acute Complications of Diabetes Mellitus | p927 | **LIVE**
| 46 | Management of Diabetes Mellitus - 2024 Guidelines | p933 | **LIVE**
| 47 | Basics of Pituitary Gland | p936 | **LIVE**
| 48 | Prolactin | p941 | **LIVE**
| 49 | Growth Hormone | p945 | **LIVE**
| 50 | Acquired Hypopituitarism | p952 | **LIVE**
| 51 | Antidiuretic Hormone | p958 | **LIVE**
| 52 | Hyponatremia | p962 | SOON
| 53 | Polyuria | p965 | SOON
| 54 | Potassium Metabolism | p968 | SOON
| 55 | Management of Hypertension - 2023 Guidelines | p976 | SOON
| 56 | Basics of Development and Anatomy of Liver | p982 | SOON
| 57 | Basics of Physiology of Liver | p986 | SOON
| 58 | Acute Hepatitis and Acute Liver Failure | p993 | SOON
| 59 | Chronic Hepatitis - Cirrhosis | p997 | SOON
| 60 | Portal Hypertension | p1001 | LIVE (86 q, 8 u)
| 61 | Ascites and Hepatorenal Syndrome | p1005 | LIVE (81 q, 8 u)
| 62 | Hepatic Encephalopathy | p1010 | SOON
| 63 | Metabolic Diseases of Liver | p1013 | SOON
| 64 | Biliary Cirrhosis | p1020 | SOON
| 65 | Autoimmune Hepatitis | p1023 | SOON
| 66 | Alcoholic Liver Disease | p1026 | SOON
| 67 | Nonalcoholic Steatohepatitis | p1030 | SOON
| 68 | Vascular Diseases of Liver | p1033 | SOON
| 69 | Hepatitis B Virus : Part 1 | p1036 | SOON
| 70 | Hepatitis B Virus : Part 2 | p1039 | SOON
| 71 | Hepatitis C Virus | p1045 | SOON
| 72 | Infective Endocarditis | p1047 | SOON
| 73 | Tropical Infections: Synopsis | p1053 | SOON
| 74 | HIV | p1061 | SOON
*(Status column: Ch 1–35, 60, 61 = **LIVE**; the rest = **SOON** — rendered in the app
as a locked "Soon" row. Update this table as chapters go live.)*

### Section spans
- **Nephrology** — Ch 1–22 (p705→p815)
- **Acid–Base & Electrolytes** — Ch 23–25 (p819 / p824 / p826)
- **Endocrinology** — Ch 26–55 (p830→p976)
- **Hepatology** — Ch 56–71 (p982→p1045)
- **Infectious Diseases** — Ch 72–74 (p1047 / p1053 / p1061)

## Data schema (prefix `MED-`)
- **Question**: `{"id":"MED-C<N>-<seq:03d>", "sec":"<Section> · pX", "page":<int>,
  "q":"...", "opts":[4 strings], "ans":0-3, "exp":"...(Book pX)",
  "fmt":"fillup|match|truefalse|scenario|oddoneout|recall|numeric|management"}`
- **Unit**: `{"id":"MED-U<N>-<n>", "ch":N, "n":n, "title":"...", "sec":"<Section> · pX-Y",
  "guide":"...", "qs":[ids in book order]}`
- **Chapter (roadmap)**: `{"n":1..74, "t":"Title", "p":<start page>, "live":bool}`
- Source of truth = `data/chNN.json`; `build_content.py` embeds it into
  `pulse-medicine.html` and refuses to build if metadata or page ranges disagree.

## Per-chapter pipeline (repeat for every chapter)
1. **Render** the chapter's book pages to PNG and read every line, table, diagram,
   flowchart and label (zoom into any unclear spot; never guess).
2. **Author** `data/chNN.json`: questions in strict book order; units grouped by
   section; ≥1 varied-format item per unit (fill-up / match / true-false / scenario /
   odd-one-out / numeric / management); every explanation ends `(Book pX)`; every
   book page cited by ≥1 question.
3. **Build**: `python build_content.py` (embeds JSON → `pulse-medicine.html`,
   marks the chapter live, validates title + page range vs the roadmap).
4. **Verify**: `python check_integrity.py` (structure, counts, order, citations,
   no-length-giveaway answers) + `node check_app_smoke.js` (runtime roadmap + quiz)
   + `python audit_variety.py` (format mix, predictability signals) → regenerate
   `AUDIT.md`.
5. **Commit + push** the session branch (`arena/…-medicine`), update this file (status, NEXT).
6. **User quality-checks**, then merges to `main` → chapter goes live at
   https://deva20045.github.io/Medicine/

## Tooling
| File | Purpose |
|---|---|
| `pulse-medicine.html` | The app (single HTML, no build step; open directly or via GitHub Pages) |
| `index.html` | Redirect → `pulse-medicine.html` |
| `build_content.py` | 74-ch roadmap + JSON validator/embedder |
| `check_integrity.py` | Structural checks: counts, IDs, options, citations, order, source↔app equality, JS syntax |
| `check_app_smoke.js` | Runtime DOM-shim test: full 74-row roadmap, live-ch paths, quiz start |
| `audit_variety.py` | Format mix + predictability signals (length bias, hedging, fillers, template runs, option reuse) |
| `fix_audit2.py` | Second-pass rewrites for Ch 13–18 (55 items replaced, 1 relabelled, 1 deleted) |
| `diversify_keys.py` | Permutes match key lists so correct-option key strings differ between items |
| `patch_items.py` | Rewrite chosen items inside part files (format changes keep the page-cited explanation) |
| `itemlab.py` | Add/edit questions in `data/` with renumbering + auto-rebuild (`map`, `flag`, `apply`, `stats`) |
| `AUDIT.md` | Latest output of `audit_variety.py` |
| `REPORT_CH23-25.md` | Build report for Ch 23–25 (Acid–Base), page-by-page coverage + metrics |

## Status
- [x] PDFs moved to `uploads/` and committed
- [x] App skeleton + index redirect (all 74 chapters listed, rest "Soon")
- [x] Tooling adapted from the OBG template
- [x] **Ch 1 "Development of Kidneys" (p705–710): 9 units, 68 questions — BUILT & VERIFIED**
- [x] **Ch 2 "Gross Anatomy of Kidney" (p711–716): 11 units, 66 questions — BUILT & VERIFIED**
- [x] **Ch 3 "Tubular Anatomy" (p717–725): 13 units, 100 questions — BUILT & VERIFIED**
- [x] **Ch 4 "Juxtaglomerular Apparatus" (p726–729): 7 units, 50 questions — BUILT & VERIFIED**
- [x] **Ch 5 "Glomerulus - Anatomy" (p730–733): 8 units, 56 questions — BUILT & VERIFIED**
- [x] **Ch 6 "Renal Physiology" (p734–739): 10 units, 133 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 7 "Urine Analysis" (p740–747): 10 units, 135 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 8 "Basic Approach to Kidney Disease and Renal Artery Stenosis" (p748–752): 8 units, 83 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 9 "Thrombotic Microangiopathy" (p753–755): 5 units, 52 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 10 "Glomerular Disease - Patterns" (p756–761): 9 units, 78 questions — RE-AUDITED, gap-filled page-by-page**
- [x] **Ch 11 "Podocytopathies" (p762–769): 8 units, 88 questions — RE-AUDITED; 16 items re-formatted, p769 figures/treatment gap-filled**
- [x] **Ch 12 "MPGN and IgA Nephropathy" (p770–774): 6 units, 52 questions — RE-AUDITED; 16 items re-formatted, length leak 51.9% → 26.9%**
- [x] **Ch 13 "Post Streptococcal Glomerulonephritis" (p775–777): 3 units, 73 questions — RE-AUDITED ×2, re-verified in the Ch 6–15 pass**
- [x] **Ch 14 "RPGN and Pulmonary Renal Syndrome" (p778–782): 5 units, 82 questions — RE-AUDITED, rebuilt page-by-page, re-verified**
- [x] **Ch 15 "Familial Glomerular Syndromes" (p783–785): 4 units, 54 questions — RE-AUDITED, rebuilt page-by-page, re-verified (p785 covers every printed line)**
- [x] **Ch 16 "Ciliopathies" (p786–792): 6 units, 139 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 17 "Chronic Tubulointerstitial Disease" (p793–795): 3 units, 52 questions — RE-AUDITED ×2 (content + option quality)**
- [x] **Ch 18 "Acute Kidney Injury" (p796–804): 9 units, 181 questions — RE-AUDITED ×2 (content + option quality)**
- [x] **Ch 19 "Chronic Kidney Disease" (p805–807): 8 units, 91 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 20 "Anemia in Chronic Kidney Disease" (p808–810): 7 units, 76 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 21 "CKD - Calciphylaxis and Cardiovascular changes" (p811–814): 6 units, 93 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 22 "Diabetic Kidney Disease" (p815–818): 7 units, 90 questions — RE-AUDITED, rebuilt page-by-page**
- [x] **Ch 23 "Introduction to Acid Base Analysis" (p819–823): 9 units, 137 questions — BUILT & VERIFIED**
- [x] **Ch 24 "Metabolic Alkalosis" (p824–825): 3 units, 40 questions — BUILT & VERIFIED**
- [x] **Ch 25 "Methodology and Interpretation of ABG Analysis" (p826–829): 6 units, 105 questions — BUILT & VERIFIED**
- [x] **Ch 26 "Overview of Hormones" (p830–836): 7 units, 71 questions — BUILT & VERIFIED**
- [x] **Ch 27 "Physiology of Adrenal Cortex" (p837–840): 4 units, 39 questions — BUILT & VERIFIED**
- [x] **Ch 28 "Conn's Syndrome" (p841–843): 3 units, 29 questions — BUILT & VERIFIED**
- [x] **Ch 29 "Cushing's Syndrome" (p844–848): 5 units, 50 questions — BUILT & VERIFIED**
- [x] **Ch 30 "Addison's Disease" (p849–851): 3 units, 33 questions — BUILT & VERIFIED**
- [x] **Ch 31 "Adrenal Medulla : Part 1" (p852–857): 5 units, 53 questions — BUILT & VERIFIED**
- [x] **Ch 32 "Adrenal Medulla : Part 2" (p858–862): 5 units, 45 questions — BUILT & VERIFIED**
- [x] **Ch 33 "Basics of Bone and Mineral Metabolism" (p863–873): 6 units, 89 questions — BUILT & VERIFIED**
- [x] **Ch 34 "Calcium Metabolism" (p874–876): 3 units, 29 questions — BUILT & VERIFIED**
- [x] **Ch 35 "Hypercalcemia" (p877–882): 6 units, 64 questions — BUILT & VERIFIED**
- [x] **Ch 36–40 (p883–901): 19 units, 272 questions — BUILT & VERIFIED**
- [ ] Ch 41–59 and 62–74 (Ch 60–61 already live)

## NEXT
**Ch 6–15 re-audited (Book p734–785) — see `REAUDIT_CH6-15.md`.** Ch 19–22 (p805–818,
Nephrology), Ch 23–25 (p819–829, Acid–Base) and Ch 26–35 (p830–882, Endocrinology +
Bone/Mineral) are live.

**Ch 6–15 re-audited (Book p734–785) — see `REAUDIT_CH6-15.md`.** Ch 6–12 were taken
through the page-anchored pipeline page by page (p734–774, 41 pages read from the scan,
tables/flowcharts/figure captions included); Ch 13–15 were re-verified against every gate
and left intact because they already met it. Ch 11 and Ch 12 additionally had 32 items
re-authored into non-recall formats with `patch_items.py`, which keeps the existing
`(Book pX)` explanation so a format change can never drift the fact, and Ch 12's
longest-option leak was rebalanced from 51.9% to 26.9%.

Counts now: Ch 6 133 · Ch 7 135 · Ch 8 83 · Ch 9 52 · Ch 10 78 · Ch 11 88 · Ch 12 52 ·
Ch 13 73 · Ch 14 82 · Ch 15 54 = **830 questions in 68 units** for this window, with 70%
of them in non-recall formats.

Verification run (all green): `python3 assemble.py <ch>` per chapter →
`build_content.py` → `check_integrity.py` (IDs, four-option structure, citations, book
order, source↔app equality, JS syntax) → `node check_app_smoke.js` (full roadmap,
live-ch paths, final questions render) → `python3 audit_variety.py > AUDIT.md`.

Honest limits recorded in `REAUDIT_CH6-15.md`: Ch 10 p759–761 were reviewed as stems,
not re-read from the scan this pass, and Ch 11–12 gained format variety rather than new
facts (their page coverage came from the earlier pass; only p769 was newly read).


*Ch 19–22 (built & re-audited page-by-page):* all 14 pages re-rendered and read line by
line (tables, flowcharts, figures, graph axes, arrow labels), authored through the
ordered pipeline — **350 exam-grade questions** (91 + 76 + 93 + 90) across 28 units.
The re-audit caught one value error and fixed it against the scan: the iron-store
replenishment multiplier is **2.2** as printed on Book p809
(`2.2 × BW × (Hb deficit) + 1000 mg`), NOT the common Ganzoni **2.4** — MED-C20-045 now
teaches the book's value and names the 2.4 trap explicitly. (The BP target on p807 was
confirmed as **<120/80 mmHg** at 8× zoom, not 130/80.)

*Ch 23–25 (Acid–Base section):* 282 questions over 11 pages authored the same way —
Ch 23 (9 units, 137 q), Ch 24 (3 units, 40 q), Ch 25 (6 units, 105 q). Every table,
flowchart, cytosolic diagram, nomogram zone and figure label is questioned; per-chapter
longest-option rates are 22.6%, 25.0% and 24.8% (chance 25%), with 0.0% answer-leak,
zero shallow 2-row matches and zero filler distractors. Two book contradictions are
taught explicitly: the p824 "respiratory alkalosis" label for the ↑PaCO₂ response
(versus the p828 compensation table), and the reversed bicarbonate arrows in the p827
primary-problem tree (versus the p828 step-2 flowchart). See **`REPORT_CH23-25.md`**.

*Ch 26–35 (Endocrinology opening + Bone/Mineral section):* 502 questions over 53 pages
authored the same way — Ch 26 (7 u, 71 q), Ch 27 (4 u, 39 q), Ch 28 (3 u, 29 q),
Ch 29 (5 u, 50 q), Ch 30 (3 u, 33 q), Ch 31 (5 u, 53 q), Ch 32 (5 u, 45 q),
Ch 33 (6 u, 89 q), Ch 34 (3 u, 29 q), Ch 35 (6 u, 64 q). Every hormone classification
table, steroidogenesis ladder, adrenal cause tree, 1°/2°/3° HPT table, sestamibi scan
caption, bone-change X-ray list and the Jansen-vs-FHH paediatric table is questioned in
both directions; all gates green (build / integrity / smoke / audit). Book quirks taught
explicitly include Bartter V hypocalcemia vs the other Bartter types (p876), the
“oxyntic cell” print for sestamibi uptake (p879) and the not-recommended IV Lasix inside
the 1st-line crisis branch (p881). See **`REPORT_CH26-35.md`**.

**Bank total: 2676 questions · 227 units · 35 live chapters**, all 178 in-scope pages
p705–882 represented.

**Bank total: 2174 questions · 180 units · 25 live chapters**, all 125 in-scope pages
p705–829 represented (this batch alone took the bank from 1720 to 1892 before the
Acid–Base merge).


*Ch 60–61 (Hepatology: Portal Hypertension & Ascites/HRS):* 167 questions over 9 pages
(p1001–1009) authored in line-by-line book order — Ch 60 (8 units, 86 q), Ch 61 (8 units, 81 q).
Every diagram, branching tree, HVPG table, hemodynamic formula, fluid analysis table,
SBP diagnostic triad/variant, and treatment regimen covered. All degraded print values
resolved and taught explicitly (p1001 "a years", p1004 terlipressin "a mg", p1006 Na "a g/day",
p1007 cefotaxime "ag", p1008 spironolactone "40 mg"). Predictability gates passed:
longest option 24.4% and 34.6%, answer leak 0.0% and 0.0%, 0 fillers, 0 reused option sets in Ch 61.
See **`REPORT_CH60-61.md`**.

**Bank total: 2843 questions · 243 units · 37 live chapters**, all 187 in-scope pages
p705–882, p1001–1009 represented.

**Next sequential chapter: Ch 47 (Diabetes Mellitus continues after Part 4).**

Ch 62 remains the next pending chapter in the separate hepatology sequence.

### Re-audit pipeline (used for Ch 13–25)
1. `_render` every book page to PNG and zoom into each unclear line/table/arrow.
2. Author `data/parts/cNN/<page><section>.json` in strict book order, plus
   `data/units/cNN.json` (concept-named units) and `data/parts/cNN/_order.json`.
3. `python author.py <NN>` → rebuilds `data/chNN.json` with sequential IDs and
   quality gates (4 distinct options, citation format, no length giveaway, no
   filler phrases).
4. `python build_content.py` → `python check_integrity.py` → `node check_app_smoke.js`
   → `python audit_variety.py > AUDIT.md`.

> **Merge policy for this run:** Chapters 2–6 stayed on `arena/01a0a8cf-medicine`
> until Ch 6 went green; a single PR then carried Ch 2–6 to `main` (live at
> https://deva20045.github.io/Medicine/).

## Live
- Preview: https://deva20045.github.io/Medicine/ (updates after merge to `main`)
- App file: `pulse-medicine.html` (also at `/pulse-medicine.html`)


## Latest batch — Chapters 41–46 (2026-09-19)

**418 new questions · 34 units · all 34 pages p902–935.**
Ch 41: 38 q / 3 u; Ch 42: 63 q / 5 u; Ch 43: 86 q / 7 u;
Ch 44: 123 q / 10 u; Ch 45: 72 q / 6 u; Ch 46: 36 q / 3 u.

Covers TFT, hypothyroidism, thyrotoxicosis & thyroiditis, diabetes classification
and pathophysiology, insulin physiology & DKA/HHS, and ADA 2024 management. All
five requested question styles are present in every chapter. Page-by-page
coverage, source-error handling and verification details: **REPORT_CH41-46.md**.
The runtime regression exercises both correct and incorrect answer paths for
every new question, including board/blank rendering and unit completion.

**Current bank total: 3,533 questions · 296 units · 48 live chapters**, covering
240 pages (p705–935 and p1001–1009). Earlier totals above are historical snapshots.

**Next: Ch 47 (Diabetes Mellitus continues in Part 4 after p935).**

## Latest batch — Chapters 52–56 (2026-09-20)

**81 new questions · 20 units · all 24 pages p962–985.** Ch 52 Hyponatremia (16),
Ch 53 Polyuria (16), Ch 54 Potassium Metabolism (16), Ch 55 Management of Hypertension
— 2023 Guidelines (16), and Ch 56 Basics of Development and Anatomy of Liver (17).
Coverage includes the full diagnostic/treatment trees, nephron diagrams, ECG/algorithm
figures, embryology derivatives, liver zones, membrane transporters and disease table.
All requested varied formats are present, with non-obvious distractors and rotated answer
positions. See **REPORT_CH52-56.md**. Build, integrity, runtime smoke and variety audits
are green.

**Current bank total: 3,931 questions · 342 units · 58 live chapters**, covering Book
p705–985 plus p1001–1009.

**Next: Ch 57 (Basics of Physiology of Liver).**
