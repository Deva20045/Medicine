# PULSE Medicine

A single-file MCQ study app for **Marrow Ed 8, Medicine Vol 3** (Book p705–1068).
Questions follow the book **line-by-line, in strict page order**, in varied formats
(recall, fill-ups, match-the-following, true/false, clinical scenarios, odd-one-out,
numeric). Every explanation ends with the exact book-page citation, and options are
shuffled on every run — so after solving a chapter you should not need the PDF.

> **Live:** https://deva20045.github.io/Medicine/ (served from `main`; the working
> branch previews here). Open `pulse-medicine.html` directly — no build step.

## Status
All 74 chapters are listed from day one; live chapters unlock automatically, the
rest show a **Soon** badge.

| Scope | Status |
|---|---|
| Ch 1 · Development of Kidneys (p705–710) — 9 units, 68 questions | ✅ live on this branch |
| Ch 2 · Gross Anatomy of Kidney (p711–716) — 11 units, 66 questions | ✅ live |
| Ch 3 · Tubular Anatomy (p717–725) — 13 units, 100 questions | ✅ live |
| Ch 4 · Juxtaglomerular Apparatus (p726–729) — 7 units, 50 questions | ✅ live |
| Ch 5 · Glomerulus - Anatomy (p730–733) — 8 units, 56 questions | ✅ live |
| Ch 6 · Renal Physiology (p734–739) — 9 units, 69 questions | ✅ live |
| Ch 7 · Urine Analysis (p740–747) — 13 units, 94 questions | ✅ live on this branch |
| Ch 8 · Basic Approach to Kidney Disease and Renal Artery Stenosis (p748–752) — 8 units, 56 questions | ✅ live on this branch |
| Ch 9 · Thrombotic Microangiopathy (p753–755) — 5 units, 35 questions | ✅ live on this branch |
| Ch 10 · Glomerular Disease - Patterns (p756–761) — 9 units, 60 questions | ✅ live on this branch |
| Ch 11 · Podocytopathies (p762–769) — 8 units, 83 questions | ✅ live on this branch |
| Ch 12 · MPGN and IgA Nephropathy (p770–774) — 6 units, 52 questions | ✅ live on this branch |
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
| Ch 26–59 (Endocrinology, Hepatology part 1) | 🚧 in progress |
| Ch 60 · Portal Hypertension (p1001–1004) — 8 units, 86 questions | ✅ live on this branch |
| Ch 61 · Ascites and Hepatorenal Syndrome (p1005–1009) — 8 units, 81 questions | ✅ live on this branch |
| Ch 62–74 (Hepatology, Viral Hepatitis, Infectious Diseases) | 🚧 in progress |

See **`PROGRESS.md`** — the single source of truth: page-offset map, 74-chapter
roadmap, data schema, per-chapter pipeline, and NEXT step.

## Repository layout
| Path | What it is |
|---|---|
| `pulse-medicine.html` | The app (all data embedded; standalone) |
| `index.html` | Redirect → `pulse-medicine.html` |
| `data/chNN.json` | Authoring source of truth per live chapter |
| `build_content.py` | Roadmap + validator; embeds `data/chNN.json` into the app |
| `check_integrity.py` | Structural gate (counts, order, citations, option quality, JS syntax) |
| `check_app_smoke.js` | Runtime test (DOM shim): roadmap rows, paths, quiz start |
| `audit_variety.py` | Format-mix + predictability audit (output saved to `AUDIT.md`) |
| `itemlab.py` | Add/edit questions with renumbering + auto-rebuild |
| `uploads/` | The 6 source book PDFs (Book p705–1070) |
| `data/parts/cNN/…` | Ordered, page-anchored authoring parts (source of truth for Ch 13–18, 23–25) |
| `author.py` | Assembles `data/chNN.json` from the ordered parts, with quality gates |
| `REAUDIT.md` | Re-audit report for Ch 13–18 (before → after, coverage, verification) |
| `REPORT_CH23-25.md` | Build report for the Acid–Base chapters (coverage, metrics, verification) |

## Run the checks (after any content change)
```bash
python build_content.py        # embeds data/ into pulse-medicine.html
python check_integrity.py      # must PASS
node check_app_smoke.js        # must PASS
python audit_variety.py > AUDIT.md
```

## Quality bar (enforced, not aspirational)
- Every book line, table, diagram, flowchart, classification, value and exception
  covered in book order; every page cited.
- 4 distinct, plausible, medical options per question — never "None of the above",
  never length-givable (answer ≤ 3× longest distractor), options shuffled at runtime.
- Mixed formats in every unit; clinical scenarios, comparisons and exam
  distinctions, not page-quizzing.
