# Re-audit & rebuild report — Chapters 6–15 (Book p734–785)

Scope of this batch: **Ch 6 → Ch 15** of Marrow Ed 8, Medicine Vol 3 — i.e. Renal
Physiology (p734–739), Urine Analysis (p740–747), Basic Approach to Kidney Disease &
Renal Artery Stenosis (p748–752), Thrombotic Microangiopathy (p753–755), Glomerular
Disease – Patterns (p756–761), Podocytopathies (p762–769), MPGN & IgA Nephropathy
(p770–774), PSGN (p775–777), RPGN & Pulmonary Renal Syndrome (p778–782), Familial
Glomerular Syndromes (p783–785).

Standard applied (same as every earlier chapter): pages are rendered from the scan and
read line by line, questions are authored **in strict book order** through the
page-anchored pipeline (`data/parts/cNN/<page><section>.json` → `assemble.py` →
`author.py` → `data/chNN.json`), every explanation ends with `(Book pX)`, every
in-scope page is cited by at least one question, and predictable-MCQ patterns are
designed out (no "all/none of the above", four plausible medical options, answer never
the giveaway-longest option, options shuffled at runtime).

## What each chapter now holds

| Ch | Pages | Questions | Units | Non-recall share | Notes |
|---|---|---|---|---|---|
| 6 | 734–739 | **133** (was 69) | 10 | 82% | page-anchored rebuild, 6 pages, 18–25 q/page |
| 7 | 740–747 | **135** (was 94) | 10 | 69% | page-anchored rebuild, 8 pages, 13–21 q/page |
| 8 | 748–752 | **83** (was 56) | 8 | 59% | page-anchored rebuild, incl. the AKI/CKD flowchart arrows |
| 9 | 753–755 | **52** (was 35) | 5 | 63% | page-anchored rebuild of the TMA tables |
| 10 | 756–761 | **78** (was 60) | 9 | 53% | gap-fill rebuild: 18 new items on p756–758, 9 concept units |
| 11 | 762–769 | **88** (was 83) | 8 | 52% | 5 new items on p769 + 16 items re-authored into varied formats |
| 12 | 770–774 | **52** | 6 | 65% | 16 items re-authored into varied formats; length-leak fixed |
| 13 | 775–777 | 73 | 3 | 82% | verified against the gates, no change needed |
| 14 | 778–782 | 82 | 5 | 89% | verified against the gates, no change needed |
| 15 | 783–785 | 54 | 4 | 85% | verified; p785 holds 9 items that cover every printed line |

Ch 6–15 now carry **830 questions in 68 units**; the whole bank is
**1892 questions / 162 units / 22 live chapters**, and all **114 in-scope Book pages**
are represented.

## Format mix (this window)

`fillup 97 · match 96 · truefalse 113 · numeric 100 · oddoneout 79 · scenario 78 ·
management 21 · recall 246` across the 830 questions of Ch 6–15 — i.e. **70% of them are
not plain recall** (bank-wide recall is 29.0%). Recall was deliberately pushed down where
it had crept back up: Ch 11 57 → 42
recall items, Ch 12 34 → 18, each converted item keeping the page-cited fact it already
taught and only changing the *format* (fill-up, match, true/false, odd-one-out, numeric,
clinical scenario).

## Predictability numbers after the work (`AUDIT.md`)

| Ch | longest-option-is-answer | option sets reused |
|---|---|---|
| 6 | 21.1% | 4 |
| 7 | 28.9% | 1 |
| 8 | 36.1% | 0 |
| 9 | 30.8% | 0 |
| 10 | 29.5% | 1 |
| 11 | 29.5% | 0 |
| 12 | 26.9% (was 51.9%) | 0 |
| 13 | 26.0% | 5 |
| 14 | 23.2% | 4 |
| 15 | 13.0% | 6 |

Ch 12's length leak came from true/false options that were long statements beside short
distractors; 16 items were rebalanced (correct option shortened, distractors given the
same level of clinical detail). Bank-wide mean is 28.1%.

## Corrections and gap-fills found while re-reading

- **Ch 7 (p740):** the old item said the *first morning* sample is used; the page prints
  the **second urine sample of the morning** — corrected in place (MED-C7-001).
- **Ch 7 (p746):** the book prints AIN as "Acute Interstitial **Necrosis**"; the item now
  quotes the printed wording rather than the textbook expansion.
- **Ch 8 (p749/p751):** the ATN/AIN "nephrosis" wording, the order of the bilateral
  renal-artery-stenosis list and the **RPRF** acronym were re-checked against the scan
  with 6–8× crops before the items were written.
- **Ch 10 (p756–758):** hyperlipidemia/lipiduria are now tested as *previously* part of
  the diagnostic criteria (not current criteria); urine protein–creatinine ratio is
  marked **"not diagnostic of nephrotic syndrome"**; the **overfill** chain is tested
  against **underfill** (β-hemolytic streptococci → plasmin → ENaC → **primary** RAS
  activation vs **secondary** RAS activation in underfill, plus ANP resistance);
  thrombosis threshold **albumin <2 g/dL** with 20% albumin 0.5 g/kg and FFP/egg white;
  d-penicillamine/Wilson's disease pairing with membranous nephropathy.
- **Ch 11 (p769):** five new items on the figures and both treatment arms — Ponticelli
  cyclophosphamide **2 mg/kg on months 2, 4, 6** beside steroids on months **1, 3, 5**,
  the **"Abrupt stop"** brace, the "**IF in MN**" caption, the four labels of the
  membranous schematic, and the 70%-with-NS vs 30%-asymptomatic split (ACE inhibitor/ARB,
  salt restriction, 1 gm/kg/day protein).

## Tooling added this pass

- `patch_items.py <ch> <patch.json>` — rewrites a chosen item inside its part file,
  keyed by `MED` id, keeping the existing page-cited explanation when no new one is
  supplied. This makes a *format* change (recall → true/false, match, odd-one-out …) a
  purely structural edit, so no fact can drift while the format changes. Order:
  `assemble` → `patch_items` → `assemble`.

## Honest limits of this pass

- **Ch 10 p759–p761 were not re-read from the scan this session.** Their items were
  reviewed as stems against the assembled bank and inherited from the previously
  audited build; the units covering them are deliberately phrased ("as printed in the
  items") instead of asserting numbers that were not re-checked.
- **Ch 11 and Ch 12 gained format variety, not new facts** — their page coverage was
  rebuilt in the earlier pass; the only new content here is the p769 figure/treatment
  block.
- **Ch 13–15 were verified, not rewritten**: they passed every gate (page coverage,
  unit ≥5 questions, ≥1 non-recall format per unit, citation and answer-rotation rules)
  and their 24/22/27-question units in Ch 13 were left as they are because splitting them
  would change the verified unit contract without teaching anything new.
- Nothing was padded: where a page had few printed lines (p785) the chapter has few
  questions, but every line of that page is covered.

## Verification (all green)

```
python3 build_content.py    → Embedded 1892 questions and 162 units across 22 live chapter(s) of 74 roadmap chapters
python3 check_integrity.py  → PASS: 22 live chapters; 1892 questions; 162 units; all 114 in-scope Book pages
                              represented; IDs, four-option structure, citations, order, source artifacts,
                              UI hooks and JavaScript syntax verified
node check_app_smoke.js     → PASS: roadmap of 74 chapters (22 live, rest "Soon"), Chapter 1–22 path data,
                              quiz starts and final questions render at runtime
python3 audit_variety.py    → AUDIT.md regenerated (format mix + predictability signals)
```

Live at https://deva20045.github.io/Medicine/ once this branch is merged into `main`.
