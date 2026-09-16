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
| 2 | Gross Anatomy of Kidney | p711 | SOON
| 3 | Tubular Anatomy | p717 | SOON
| 4 | Juxtaglomerular Apparatus | p726 | SOON
| 5 | Glomerulus - Anatomy | p730 | SOON
| 6 | Renal Physiology | p734 | SOON
| 7 | Urine Analysis | p740 | SOON
| 8 | Basic Approach to Kidney Disease and Renal Artery Stenosis | p748 | SOON
| 9 | Thrombotic Microangiopathy | p753 | SOON
| 10 | Glomerular Disease - Patterns | p756 | SOON
| 11 | Podocytopathies | p762 | SOON
| 12 | MPGN and IgA Nephropathy | p770 | SOON
| 13 | Post Streptococcal Glomerulonephritis | p775 | SOON
| 14 | RPGN and Pulmonary Renal Syndrome | p778 | SOON
| 15 | Familial Glomerular Syndromes | p783 | SOON
| 16 | Ciliopathies | p786 | SOON
| 17 | Chronic Tubulointerstitial Disease | p793 | SOON
| 18 | Acute Kidney Injury | p796 | SOON
| 19 | Chronic Kidney Disease | p805 | SOON
| 20 | Anemia in Chronic Kidney Disease | p808 | SOON
| 21 | CKD - Calciphylaxis and Cardiovascular changes | p811 | SOON
| 22 | Diabetic Kidney Disease | p815 | SOON
| 23 | Introduction to Acid Base Analysis | p819 | SOON
| 24 | Metabolic Alkalosis | p824 | SOON
| 25 | Methodology and Interpretation of ABG Analysis | p826 | SOON
| 26 | Overview of Hormones | p830 | SOON
| 27 | Physiology of Adrenal Cortex | p837 | SOON
| 28 | Conn's Syndrome | p841 | SOON
| 29 | Cushing's Syndrome | p844 | SOON
| 30 | Addison's Disease | p849 | SOON
| 31 | Adrenal Medulla : Part 1 | p852 | SOON
| 32 | Adrenal Medulla : Part 2 | p858 | SOON
| 33 | Basics of Bone and Mineral Metabolism | p863 | SOON
| 34 | Calcium Metabolism | p874 | SOON
| 35 | Hypercalcemia | p877 | SOON
| 36 | Hypocalcemia | p883 | SOON
| 37 | Phosphorus Metabolism | p887 | SOON
| 38 | Magnesium Metabolism | p892 | SOON
| 39 | Osteoporosis | p895 | SOON
| 40 | Basics of Thyroid Gland | p898 | SOON
| 41 | Thyroid Function Tests | p902 | SOON
| 42 | Hypothyroidism | p905 | SOON
| 43 | Thyrotoxicosis and Thyroiditis | p910 | SOON
| 44 | Introduction to Diabetes Mellitus and Classification | p917 | SOON
| 45 | Insulin Physiology and Acute Complications of Diabetes Mellitus | p927 | SOON
| 46 | Management of Diabetes Mellitus - 2024 Guidelines | p933 | SOON
| 47 | Basics of Pituitary Gland | p936 | SOON
| 48 | Prolactin | p941 | SOON
| 49 | Growth Hormone | p945 | SOON
| 50 | Acquired Hypopituitarism | p952 | SOON
| 51 | Antidiuretic Hormone | p958 | SOON
| 52 | Hyponatremia | p962 | SOON
| 53 | Polyuria | p965 | SOON
| 54 | Potassium Metabolism | p968 | SOON
| 55 | Management of Hypertension - 2023 Guidelines | p976 | SOON
| 56 | Basics of Development and Anatomy of Liver | p982 | SOON
| 57 | Basics of Physiology of Liver | p986 | SOON
| 58 | Acute Hepatitis and Acute Liver Failure | p993 | SOON
| 59 | Chronic Hepatitis - Cirrhosis | p997 | SOON
| 60 | Portal Hypertension | p1001 | SOON
| 61 | Ascites and Hepatorenal Syndrome | p1005 | SOON
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
*(Status column: Ch 1 = **LIVE**; every other chapter = **SOON** — rendered in the app
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
5. **Commit + push** `arena/01a0a851-medicine`, update this file (status, NEXT).
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
| `itemlab.py` | Add/edit questions in `data/` with renumbering + auto-rebuild (`map`, `flag`, `apply`, `stats`) |
| `AUDIT.md` | Latest output of `audit_variety.py` |

## Status
- [x] PDFs moved to `uploads/` and committed
- [x] App skeleton + index redirect (all 74 chapters listed, rest "Soon")
- [x] Tooling adapted from the OBG template
- [x] **Ch 1 "Development of Kidneys" (p705–710): 9 units, 68 questions — BUILT & VERIFIED**
- [x] **Ch 2 "Gross Anatomy of Kidney" (p711–716): 11 units, 66 questions — BUILT & VERIFIED**
- [x] **Ch 3 "Tubular Anatomy" (p717–725): 13 units, 100 questions — BUILT & VERIFIED**
- [x] **Ch 4 "Juxtaglomerular Apparatus" (p726–729): 7 units, 50 questions — BUILT & VERIFIED**
- [x] **Ch 5 "Glomerulus - Anatomy" (p730–733): 8 units, 56 questions — BUILT & VERIFIED**
- [x] **Ch 6 "Renal Physiology" (p734–739): 9 units, 69 questions — BUILT & VERIFIED**
- [x] **Ch 7 "Urine Analysis" (p740–747): 13 units, 94 questions — BUILT & VERIFIED**
- [x] **Ch 8 "Basic Approach to Kidney Disease and Renal Artery Stenosis" (p748–752): 8 units, 56 questions — BUILT & VERIFIED**
- [x] **Ch 9 "Thrombotic Microangiopathy" (p753–755): 5 units, 35 questions — BUILT & VERIFIED**
- [x] **Ch 10 "Glomerular Disease - Patterns" (p756–761): 9 units, 60 questions — BUILT & VERIFIED**
- [x] **Ch 11 "Podocytopathies" (p762–769): 8 units, 83 questions — BUILT & VERIFIED**
- [x] **Ch 12 "MPGN and IgA Nephropathy" (p770–774): 6 units, 52 questions — BUILT & VERIFIED**
- [ ] Ch 13–74 (per pipeline above)

## NEXT
**Ch 7–12 COMPLETE.** All six nephrology chapters built, verified and ready to merge
to main in a single PR. Ch 13+ continues the same pipeline when requested.

> **Merge policy for this run:** Chapters 2–6 stayed on `arena/01a0a8cf-medicine`
> until Ch 6 went green; a single PR then carried Ch 2–6 to `main` (live at
> https://deva20045.github.io/Medicine/).

## Live
- Preview: https://deva20045.github.io/Medicine/ (updates after merge to `main`)
- App file: `pulse-medicine.html` (also at `/pulse-medicine.html`)
