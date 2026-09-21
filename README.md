# PULSE Medicine

A single-file MCQ study app for **Marrow Ed 8, Medicine Vol 3** (Book p705–1068).
The mandatory authoring standard is **every line/element, in exact book order,
without compromise**, with varied question formats and exact book-page citations.
Only answer options may shuffle; questions must remain in source order.

> **2026-09-20 self-audit: NOT YET COMPLIANT.** Structural/runtime checks pass,
> Ch 1–3 (p705–725) have since been rebuilt with ordered source checklists and
> explicit caveats; 71 chapters remain pending review. The source failures in
> Ch 54 concern an older bank: PR #18 has replaced Ch 52–56, which remain pending
> strict review. See [`SOURCE_REVIEW.md`](SOURCE_REVIEW.md) for all 74 chapters.
> Live content is not automatically line-by-line verified. See
> [`SELF_AUDIT_BOOK_ORDER.md`](SELF_AUDIT_BOOK_ORDER.md) for evidence and scope,
> and [`AGENTS.md`](AGENTS.md) for the persistent project rule.

> **Live:** https://deva20045.github.io/Medicine/ (served from `main`; the working
> branch previews here). Open `pulse-medicine.html` directly — no build step.

## Status
All 74 chapters are listed from day one and **all 74 are now live** (Ch 70–74 completed the
roadmap on 2026-09-21; see [`REPORT_CH70-74.md`](REPORT_CH70-74.md)).

| Scope | Status |
|---|---|
| Ch 1 · Development of Kidneys (p705–710) — 9 units, 140 questions | ✅ live; source-reviewed with caveats |
| Ch 2 · Gross Anatomy of Kidney (p711–716) — 11 units, 148 questions | ✅ live; source-reviewed with caveats |
| Ch 3 · Tubular Anatomy (p717–725) — 13 units, 202 questions | ✅ live; source-reviewed with caveats |
| Ch 4 · Juxtaglomerular Apparatus (p726–729) — 7 units, 50 questions | ✅ live |
| Ch 5 · Glomerulus - Anatomy (p730–733) — 8 units, 56 questions | ✅ live |
| Ch 6 · Renal Physiology (p734–739) — 10 units, 133 questions | ✅ live (page-anchored re-audit) |
| Ch 7 · Urine Analysis (p740–747) — 10 units, 135 questions | ✅ live (page-anchored re-audit) |
| Ch 8 · Basic Approach to Kidney Disease and Renal Artery Stenosis (p748–752) — 8 units, 83 questions | ✅ live (page-anchored re-audit) |
| Ch 9 · Thrombotic Microangiopathy (p753–755) — 5 units, 52 questions | ✅ live (page-anchored re-audit) |
| Ch 10 · Glomerular Disease - Patterns (p756–761) — 9 units, 78 questions | ✅ live (page-anchored re-audit) |
| Ch 11 · Podocytopathies (p762–769) — 8 units, 88 questions | ✅ live (page-anchored re-audit) |
| Ch 12 · MPGN and IgA Nephropathy (p770–774) — 6 units, 52 questions | ✅ live (page-anchored re-audit) |
| Ch 13 · Post Streptococcal Glomerulonephritis (p775–777) — 3 units, 73 questions | ✅ live (re-audited) |
| Ch 14 · RPGN and Pulmonary Renal Syndrome (p778–782) — 5 units, 82 questions | ✅ live (re-audited) |
| Ch 15 · Familial Glomerular Syndromes (p783–785) — 4 units, 54 questions | ✅ live (re-audited) |
| Ch 16 · Ciliopathies (p786–792) — 6 units, 139 questions | ✅ live (re-audited) |
| Ch 17 · Chronic Tubulointerstitial Disease (p793–795) — 3 units, 52 questions | ✅ live (re-audited) |
| Ch 18 · Acute Kidney Injury (p796–804) — 9 units, 181 questions | ✅ live (re-audited) |
| Ch 19 · Chronic Kidney Disease (p805–807) — 8 units, 91 questions | ✅ live (re-audited) |
| Ch 20 · Anemia in Chronic Kidney Disease (p808–810) — 7 units, 76 questions | ✅ live (re-audited) |
| Ch 21 · CKD - Calciphylaxis and Cardiovascular changes (p811–814) — 6 units, 93 questions | ✅ live (re-audited) |
| Ch 22 · Diabetic Kidney Disease (p815–818) — 7 units, 90 questions | ✅ live (re-audited) |
| Ch 23 · Introduction to Acid Base Analysis (p819–823) — 9 units, 137 questions | ✅ live |
| Ch 24 · Metabolic Alkalosis (p824–825) — 3 units, 40 questions | ✅ live |
| Ch 25 · Methodology and Interpretation of ABG Analysis (p826–829) — 6 units, 105 questions | ✅ live |
| Ch 26 · Overview of Hormones (p830–836) — 7 units, 71 questions | ✅ live |
| Ch 27 · Physiology of Adrenal Cortex (p837–840) — 4 units, 39 questions | ✅ live |
| Ch 28 · Conn's Syndrome (p841–843) — 3 units, 29 questions | ✅ live |
| Ch 29 · Cushing's Syndrome (p844–848) — 5 units, 50 questions | ✅ live |
| Ch 30 · Addison's Disease (p849–851) — 3 units, 33 questions | ✅ live |
| Ch 31 · Adrenal Medulla : Part 1 (p852–857) — 5 units, 53 questions | ✅ live |
| Ch 32 · Adrenal Medulla : Part 2 (p858–862) — 5 units, 45 questions | ✅ live |
| Ch 33 · Basics of Bone and Mineral Metabolism (p863–873) — 6 units, 89 questions | ✅ live |
| Ch 34 · Calcium Metabolism (p874–876) — 3 units, 29 questions | ✅ live |
| Ch 35 · Hypercalcemia (p877–882) — 6 units, 64 questions | ✅ live |
| Ch 36 · Hypocalcemia (p883–886) — 4 units, 53 questions | ✅ live |
| Ch 37 · Phosphorus Metabolism (p887–891) — 5 units, 62 questions | ✅ live |
| Ch 38 · Magnesium Metabolism (p892–894) — 3 units, 48 questions | ✅ live |
| Ch 39 · Osteoporosis (p895–897) — 3 units, 50 questions | ✅ live |
| Ch 40 · Basics of Thyroid Gland (p898–901) — 4 units, 59 questions | ✅ live |
| Ch 41–51 (Thyroid function tests → Antidiuretic Hormone, p902–961) — 11 chapters, 735 questions | ✅ live |
| Ch 52 · Hyponatremia (p962–964) — 3 units, 47 questions | ✅ live |
| Ch 53 · Polyuria (p965–967) — 3 units, 53 questions | ✅ live |
| Ch 54 · Potassium Metabolism (p968–975) — 8 units, 106 questions | ✅ live |
| Ch 55 · Management of Hypertension - 2023 Guidelines (p976–981) — 6 units, 77 questions | ✅ live |
| Ch 56 · Basics of Development and Anatomy of Liver (p982–985) — 4 units, 55 questions | ✅ live |
| Ch 57 · Basics of Physiology of Liver (p986–992) — 7 units, 78 questions | ✅ live |
| Ch 58 · Acute Hepatitis and Acute Liver Failure (p993–996) — 4 units, 47 questions | ✅ live |
| Ch 59 · Chronic Hepatitis - Cirrhosis (p997–1000) — 4 units, 38 questions | ✅ live |
| Ch 60 · Portal Hypertension (p1001–1004) — 8 units, 86 questions | ✅ live |
| Ch 61 · Ascites and Hepatorenal Syndrome (p1005–1009) — 8 units, 81 questions | ✅ live |
| Ch 62 · Hepatic Encephalopathy (p1010–1012) — 3 units, 32 questions | ✅ live |
| Ch 63 · Metabolic Diseases of Liver (p1013–1019) — 7 units, 75 questions | ✅ live |
| Ch 64 · Biliary Cirrhosis (p1020–1022) — 3 units, 44 questions | ✅ live |
| Ch 65 · Autoimmune Hepatitis (p1023–1025) — 3 units, 34 questions | ✅ live |
| Ch 66 · Alcoholic Liver Disease (p1026–1029) — 4 units, 43 questions | ✅ live |
| Ch 67 · Nonalcoholic Steatohepatitis (p1030–1032) — 3 units, 28 questions | ✅ live |
| Ch 68 · Vascular Diseases of Liver (p1033–1035) — 3 units, 30 questions | ✅ live |
| Ch 69 · Hepatitis B Virus : Part 1 (p1036–1038) — 3 units, 40 questions | ✅ live |
| Ch 70 · Hepatitis B Virus : Part 2 (p1039–1044) — 6 units, 91 questions | ✅ live |
| Ch 71 · Hepatitis C Virus (p1045–1046) — 2 units, 33 questions | ✅ live |
| Ch 72 · Infective Endocarditis (p1047–1052) — 6 units, 76 questions | ✅ live |
| Ch 73 · Tropical Infections: Synopsis (p1053–1060) — 4 units, 95 questions | ✅ live |
| Ch 74 · HIV (p1061–1068) — 4 units, 96 questions | ✅ live |

See **`PROGRESS.md`** — the single source of truth: page-offset map, 74-chapter
roadmap, data schema, per-chapter pipeline, and NEXT step.

## Repository layout
| Path | What it is |
|---|---|
| `pulse-medicine.html` | The app (all data embedded; standalone) |
| `index.html` | Redirect → `pulse-medicine.html` |
| `data/chNN.json` | Extracted question bank (one JSON per live chapter) |
| `build_content.py` | Inlines `data/ch*.json` into `pulse-medicine.html` |
| `check_integrity.py` | Gate: schema, full-chapter page sequence, exact count, source↔app sync, existing review freshness |
| `check_source_coverage.py` | Ordered source-checklist/PDF/content-hash validation; `--require-all` refuses incomplete whole-book certification |
| `data/source_review/chNN.json` | Manually authored source-review checklist, traversal, caveats and hashes |
| `SOURCE_REVIEW.md` | Current all-74-chapter review queue; regenerate with `--write-report` |
| `test_source_coverage.py` | Evidence/order/freshness regression tests |
| `check_app_smoke.js` | DOM-shim runtime test: both answer outcomes for every live question; legacy format defects reported |
| `audit_variety.py` | Quality audit (formats, length-bias, leaks, repeats) |
| `author.py` | Assembles `data/chNN.json` from the ordered parts, with quality gates |
| `REAUDIT.md` | Re-audit report for Ch 13–18 (before → after, coverage, verification) |
| `REPORT_CH23-25.md` | Build report for the Acid–Base chapters (coverage, metrics, verification) |
| `REPORT_CH26-35.md` | Build report for Ch 26–35 (Endocrinology + Bone/Mineral; coverage, metrics, verification) |
| `REPORT_CH36-40.md` | Build report for Ch 36–40 (coverage, quality metrics, source caveats, verification) |
| `REPORT_CH41-46.md` | Build report for Ch 41–46 (Thyroid Function Tests → DM Management — 2024 Guidelines; coverage, quality metrics, source caveats, verification) |
| `REPORT_CH60-61.md` | Build report for Ch 60–61 (Portal Hypertension, Ascites and HRS) |
| `REPORT_CH52-56.md` | Build report for Ch 52–56 (Hyponatremia → Liver Development and Anatomy) |
| `REPORT_CH57-59_62-63.md` | Build report for Ch 57–59 & 62–63 (Hepatology Physiology, ALF, Cirrhosis, HE, Wilson's & Hemochromatosis) |
| `REPORT_CH70-74.md` | Build report for Ch 70–74 (HBV Part 2, HCV, Infective Endocarditis, Tropical Infections, HIV) |

## Run the checks (after any content change)
```bash
python3 build_content.py
python3 check_integrity.py
python3 -m unittest -v test_source_coverage.py
node check_app_smoke.js
python3 audit_variety.py
python3 check_source_coverage.py --write-report
```

Reading the scan while authoring (`_render/` helpers, not needed to run the app):
`_render/batch_dump.py <first> <last>` renders pages and OCRs them into ordered lines
(`_render/ocr/<page>.txt`); `_render/asciiart.py` prints a zoomed region as ASCII for
verifying numbers, which OCR garbles in these notes.

For a whole-book completion claim, also run:
```bash
python3 check_source_coverage.py --require-all
```
This currently **fails intentionally**: only Ch 1–2 have recorded reviews under
this standard. Do not create review manifests from page citations alone. After
changing reviewed questions or unit guides, recheck the source mapping before
updating the manifest content hash; otherwise builds will correctly refuse stale
evidence. Existing completion badges and XP are preserved; revised Ch 1/2 guides
recommend replay to cover the expanded questions.
