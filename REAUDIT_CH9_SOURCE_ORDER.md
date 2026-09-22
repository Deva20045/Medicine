# Re-audit — Chapter 9 · Thrombotic Microangiopathy (Book p753–755) — strict line-by-line, book order

**Date:** 2026-09-22 · **Source:** `uploads/Medicine_Vol3_Part1_pages_705-759.pdf`, PDF pp61–63 (offset 692) · **Evidence:** `data/source_review/ch09.json` (24 elements → 52 question IDs, each listed once in printed order).

## Method
Pages rendered at 2× (`_render/_753–_755.png`), read top-to-bottom, tables row by row; every stored `ans` compared with the print.

## Findings
| Class | Count | Detail |
|---|---|---|
| Wrong answer keys | **1 / 52** | Old MED-C9-051 (match, ATN column): its keyed pairing "3-A" mapped BUN/creatinine to option "A) > 20:1", but the print gives ATN **< 10:1** (> 20:1 is the pre-renal column). Option A corrected to "< 10:1" (now MED-C9-051 still). |
| Order faults | all 3 pages | Causes-list consolidation before the anti-RNA-P line; TTP-pentagon items interleaved with HUS-triad items; drug-list odd-one-out before the immune-mediated list; typical-HUS timeline items split across the unit. Re-sequenced. |
| Uncovered elements | 0 | Every printed line/box/table cell already had an item. |

Result: 52 questions, same 5 unit IDs (8/10/14/4/16). `data/parts/c9/`, `data/units/c9.json` removed; `data/ch09.json` is the single source of truth.

## Print caveats
p753 "Papilloedema", "Anti RNA P"; p754 "Streptococcus pneumonia", "Worst progosis", "Ecoli"; p755 "Withhold".

## Checks
build, integrity (Ch 9 = 52), smoke, `check_source_coverage.py` (9/74), `test_source_coverage.py` — all PASS. Whole-book compliance **not** claimed.
