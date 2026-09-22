# Re-audit — Chapter 7 · Urine Analysis (Book p740–747) — strict line-by-line, book order

**Date:** 2026-09-22 · **Source:** `uploads/Medicine_Vol3_Part1_pages_705-759.pdf`, PDF pp48–55 (offset 692) · **Evidence:** `data/source_review/ch07.json` (85 elements → 140 question IDs, each listed once in printed order).

## Method
Every page rendered at 2× (`_render/_740–_747.png`) plus a 6× crop of the abnormal-values table (`_render/_z_741abn.png`). Each printed line, table row, flowchart box and figure caption was read in order and matched to the bank; every stored `ans` index was compared with the print.

## Findings
| Class | Count | Detail |
|---|---|---|
| Wrong answer keys | **0 / 135** | Unlike Ch 6 (35 wrong keys from `migrate_parts.py`), every Ch 7 key matched the scan. |
| Wrong printed value | 1 | Old MED-C7-033 / 039 taught diabetes-insipidus osmolality **< 300** mOsm/kg; the print reads **< 200 mOsm/kg**. Fixed (now MED-C7-040 / 041). |
| Order faults | every page | Bank tested table rows / panels out of printed order (e.g. appearance rows 1–2 after rows 3–7; p747 panels D–E before A–C). Re-sequenced to the recorded traversal. |
| Uncovered elements | 5 | Added items: "Brown – Nitrofurantoin" row; captions "Collection of urine", "Normal urine colour", "High coloured urine"; the "Positive → Blood in urine" box. |

Result: 135 → **140 questions**, same 10 unit IDs (MED-U7-1…10; 8/10/10/14/22/14/18/15/16/13). `data/parts/c7/` and `data/units/c7.json` removed — `data/ch07.json` is the single source of truth. Unit guides carry the revision note; user progress is preserved.

## Print caveats (taught as printed, flagged in explanations)
- p740 "Imepenem + cilastatin"; p741 "Beta ketothiolase deficiency"; p743 "leucocyte"/"leukocytes"; p746 "Acute Interstitial **Necrosis** (AIN)".
- Photograph content is tested only through its printed captions.

## Checks
`build_content.py`, `check_integrity.py` (Ch 7 = 140), `check_app_smoke.js`, `check_source_coverage.py` (7/74), `test_source_coverage.py` — all PASS. Whole-book compliance is **not** claimed.
