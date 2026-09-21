# Chapters 70–74 — build report (HBV Part 2 → HIV)

Scope: **Book p1039–1068** (Marrow Ed 8, Medicine Vol 3) — the last five chapters of the
book and the last 30 pages of the scan. Authoring followed the project rule
(`AGENTS.md`): every OCR-detected line, bullet, table row, algorithm branch, figure
caption and note, kept in printed order, with only answer options shuffled.

| Chapter | Pages | Questions | Units |
|---|---|---|---|
| 70 · Hepatitis B Virus : Part 2 | p1039–1044 | 91 | 6 |
| 71 · Hepatitis C Virus | p1045–1046 | 33 | 2 |
| 72 · Infective Endocarditis | p1047–1052 | 76 | 6 |
| 73 · Tropical Infections: Synopsis | p1053–1060 | 95 | 4 |
| 74 · HIV | p1061–1068 | 96 | 4 |
| **Total** | **30 pages** | **391** | **22** |

Bank after the build: **5,324 questions · 412 units · 74/74 chapters live**, covering all
364 in-scope book pages (p705–1068).

## How the pages were read

The scan has no text layer, so each page was rendered from
`uploads/Medicine_Vol3_Part6_pages_1035-1070.pdf` (offset K = 1034) and read in two passes:

1. **Whole-page OCR into ordered lines** (`_render/batch_dump.py` → `_render/ocr/<page>.txt`)
   to establish the reading order, the column layout (x positions) and the block structure.
2. **Zoomed ASCII renders of individual tokens** (`_render/asciiart.py`) for every printed
   number, because the PP-OCRv4 recogniser reads the words of these notes correctly but
   garbles digits systematically (0→o, 1→I, 2→a, 5→S, 6→b). Restricted-alphabet decoding of
   the recogniser was tried and did **not** fix digit accuracy, so numbers were verified
   glyph-by-glyph instead.

Values verified this way include: HBV DNA > 20,000 in pregnancy, HBIg 0.5 ml and 0.06 mL/kg
with the 14-day and 24-hour windows, vaccine 0-1-6 and CKD 0-1-2-6 schedules with 20 μg/0.5 ml
and 40 μg/1 ml, 1st dose within 12 hours, anti-HBs thresholds >100 / 10-100 / <10,
phase-IV quantitative HBsAg > 1000 IU/mL, genotype 3 in India, HCV 9.7 kb and 1 in 10,00,000
transfusion risk, SVR 99.5-99.7 / 75 / 60%, treat above 12 years, DAA combinations for 12 weeks,
IE right-sided 10% with 70% MRSA, rheumatic 25-30 / congenital 10-20 / MVP 10-30 / parenteral
drug abuse 15-35 / none 25-45, the TTE (50-70 / 86) versus TEE (86-98 / 98) accuracies,
Duke blood-culture set and timing details (3 sets of 20 ml from 3 sites, 10 ml aerobic
plus 10 ml anaerobic over 30-60 minutes, repeat every 18-24 hours), regimen doses
(penicillin G 2-3 and 4-5 million units, vancomycin 15 mg/kg, gentamicin 1 mg/kg,
rifampicin 300 mg TID for 6-8 weeks, amoxicillin 2 g 30-60 minutes before, clindamycin 600 mg),
platelet thresholds in dengue (<10,000 or <20,000 with bleeding), QBC every 12 hours and three
consecutive negatives, artesunate 2.4 mg/kg at 0, 12 and 24 hours, the CDC CD4 bands
(≥500 / 200-499 with 14-28% / <200 with <14%), MAC at an average CD4 below 10 with
prophylaxis below 50, and the TED / TLD doses (300 / 200 / 50 mg and 300 / 300 / 50 mg).

## Source-order notes (what the page actually says)

- **p1040** — the phase table and the five phase blocks are read left to right, top row
  (phases I, II, III) then bottom row (phases IV, V), then the acute-HBV versus chronic
  phase-IV confirmation block at the foot.
- **p1041** — the "Replicative load" section is split into a *low replicative* and a
  *high replicative* branch. The two HBeAg profiles and their consequences are printed
  unambiguously (HBeAg +ve with HBV DNA > 20,000 IU/mL → high infectivity, risk of liver
  injury; HBeAg -ve precore mutant with HBV DNA > 2,000 IU/mL → anti-HBc reactive,
  progressive liver injury, bad prognosis). **Which branch label sits above which profile
  could not be resolved** (the two labels are drawn close to the branch arrows and the
  scan is faint there), so no question asserts that mapping — the report in
  `REPORT_CH70-74.md` is the record of the ambiguity.
- **p1042** — the gap between the treatment indications and the histology captions is a
  photomicrograph (pink/purple H&E image), not text; no content was missed.
- **p1047** — the third item in the congenital risk-factor list (below ventricular septal
  defect and atrial septal defect) is illegible at the resolution available; it is not
  asserted anywhere in the bank.
- **p1061** — stage 1 has no printed CD4 percentage in the scan (only stages 2 and 3 carry
  the 14-28% and <14% figures), so only the printed figures are quizzed.
- **p1053** — the fever-on-day-1-2 and fever-on-day-5 blocks carry figure content that OCR
  did not resolve; the day-3, investigations and day-4 blocks are covered in full.

## Question style

Every unit contains a mix of fill-ups, matching, true/false, clinical scenarios and
odd-one-out items, with non-obvious distractors drawn from the same page (for example the
wrong antibiotic duration, the other echocardiography modality, the species that does
*not* relapse, the CDC stage one band away). Formats across the five chapters:
match 104, recall 131, odd-one-out 26, true/false 24, fill-up 22, numeric 43, scenario 20.

## Verification run

```
python3 build_content.py      # 5,324 questions, 412 units, 74 live chapters embedded
python3 check_integrity.py    # PASS — 74 live chapters, 364 pages, IDs/order/citations/JS
node check_app_smoke.js       # PASS — 10,648 answer paths across 412 units
                              # WARN — 44 legacy format defects, all in Ch 26/29/60/61;
                              #         none in Ch 70–74
python3 -m unittest test_source_coverage.py   # OK — 17 tests
python3 audit_variety.py      # Ch 70–74: 17.6–27.1% longest-option bias, 0–1.1% leakage
python3 check_source_coverage.py --write-report
                              # PASS — 3/74 chapters carry recorded source review manifests
```

## Honest status

- The 74-chapter roadmap is now **fully live**; the app ships 5,324 questions.
- As with chapters 4–69, these five chapters are **built in strict printed order and
  verified page by page, but they do not carry the recorded line-by-line source-review
  manifests** that only chapters 1–3 have (`data/source_review/`). `check_source_coverage.py
  --require-all` therefore still fails by design, and nothing here claims whole-book
  line-by-line certification.
- Two specific printed values remain unresolved and are recorded above rather than guessed:
  the replicative-load branch mapping on p1041 and the third congenital risk factor on p1047.
- The perinatal/breast-feeding HCV transmission figure on p1045 is taught qualitatively
  ("a low single-digit percentage, far below the 40-90% quoted for IV drug users") because
  the exact numeral could not be read with confidence; the surrounding risk figures are exact.
