# Re-audit — Chapter 10 · Glomerular Disease – Patterns (Book p756–761) — strict line-by-line, book order

**Date:** 2026-09-22 · **Source:** Part 1 PDF pp64–67 (p756–759, offset 692) + Part 2 PDF pp1–2 (p760–761, offset 759) · **Evidence:** `data/source_review/ch10.json` (42 elements → 80 question IDs, each listed once in printed order; per-page PDF + hash recorded for the split).

## Method
Pages rendered at 2× (`_render/_756–_761.png`), read top-to-bottom, flowcharts branch by branch; every stored `ans` compared with the print.

## Findings
| Class | Count | Detail |
|---|---|---|
| Wrong answer keys | **0 / 78** | Every key matched the scan. |
| Uncovered elements | 2 | p759 "Note: Features against MCD — RBC casts in urine, hypertension, renal failure" and p760 "(Very quick remission)" had no item. Added (MED-C10-052, MED-C10-066). |
| Order faults | all pages | Criteria items interleaved with the biopsy flowchart; thrombosis items split around the edema block; "MCD 15%" tested last on p761. Re-sequenced. |

Result: 78 → **80 questions**, same 9 unit IDs (8/13/15/9/5/9/4/9/8). `data/parts/c10/`, `data/units/c10.json` removed; `data/ch10.json` is the single source of truth.

## Print caveats
p757 "muehrcke's line" lower-case caption; p761 "Paraneoplastic snydrome"; p758 page number cropped in scan (running head confirms). Photographs tested via captions only.

## Checks
build, integrity (Ch 10 = 80; 5,373 q), smoke, `check_source_coverage.py` (10/74), `test_source_coverage.py` — all PASS. Whole-book compliance **not** claimed.
