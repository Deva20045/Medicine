# Re-audit of Chapters 13–18 — what was wrong and what was fixed

Scope: **Book p775–p804** (Marrow Ed 8, Medicine Vol 3): Ch 13 Post Streptococcal
Glomerulonephritis, Ch 14 RPGN & Pulmonary Renal Syndrome, Ch 15 Familial
Glomerular Syndromes, Ch 16 Ciliopathies, Ch 17 Chronic Tubulointerstitial
Disease, Ch 18 Acute Kidney Injury.

## Why the earlier build failed the quality bar

The first pass over these six chapters was **page-summary level**: one shallow
question per printed heading, with these defects.

| Defect (found in the old Ch 13–18) | Example from the old data |
|---|---|
| Placeholder match stems, not real content | `MED-C13-012` — "Match the following — 1) first item 2) second item 3) third item …" |
| Unit titles were page labels, not concepts | "Book p775: Post Streptococcal Glomerulonephritis" |
| Whole tables never questioned | The PSGN-vs-PIGN/IRGN TYPES table had **no** question on organisms, strains, incubation, C3 % or prognosis |
| Diagrams/figures ignored | The PSGN triad triangle, DPGN/IF figures, dialysis-disequilibrium flowchart, ADPKD cyst figures, ATN histology, IVC/PLR figures, contrast vacuolar degeneration, cholesterol crystals |
| Flowcharts reduced to one line | RPGN type I–V tree, Ravinson's criteria, ARPKD fibrocystin flowchart, CKDu theories flowchart, sepsis/NSAID/aminoglycoside flowcharts, FeNa formula |
| Values and exceptions dropped | 90% vs 60% C3, 7–10 days vs 2–4 weeks vs "alongside infection", 80/15/5% Alport inheritance, 70%/30% ARPKD deaths, 5% post-transplant Goodpasture, FeNa <1 exceptions, 5–6 L/day, 2–2.5 cm IVC, lactate 1/4 mmol/L |
| Answer spot-able by length | Old Ch 13: the longest option was the answer in **58.3%** of items; old Ch 17: **50%** |
| No real clinical application | Only 1 scenario in Ch 13 and **0** in Ch 14–17 |

## What this re-audit did

Every page of p775–p804 was re-rendered at 2.6–25× zoom and read line by line
(tables, flowcharts, figures and their arrow labels included). The chapters were
then **re-authored from scratch** through an ordered, page-anchored pipeline
(`data/parts/c13…c18/<page><section>.json` → `author.py` → `data/chNN.json`),
so book order is enforced structurally, not by hand.

### Before → after

| Ch | Book pages | Units before → after | Questions before → after | Pages cited |
|---|---|---|---|---|
| 13 Post Streptococcal GN | 775–777 | 3 → **3** | 12 → **73** | 3/3 |
| 14 RPGN & Pulmonary Renal | 778–782 | 5 → **5** | 18 → **82** | 5/5 |
| 15 Familial Glomerular | 783–785 | 3 → **4** | 11 → **54** | 3/3 |
| 16 Ciliopathies | 786–792 | 7 → **6** | 27 → **139** | 7/7 |
| 17 Chronic Tubulointerstitial | 793–795 | 3 → **3** | 10 → **53** | 3/3 |
| 18 Acute Kidney Injury | 796–804 | 9 → **9** | 34 → **181** | 9/9 |
| **Total** | p775–804 | 30 → **30** | **112 → 582** | **30/30 pages** |

Bank total: 901 → **1371 questions**, 136 units, 18 live chapters.

### Per-chapter coverage (new units are concept-named, not page-named)

**Ch 13 (73 q)** — the PSGN vs PIGN/IRGN TYPES table row by row (demographics,
GABHS strains 1/3/4/12 vs 47/49/55/57, MRSA, incubation 7–10 d vs 2–4 wk vs
"alongside infection", ↓C3 90% vs 60%, prognosis); HLA DR4/DR1; NAPlr, SPEB,
anti-DNAase B; the acute triad triangle and PRES/seizures; the ENaC flowchart;
urine and RFT findings; both biopsy indications; DPGN histopathology; the
clinical-phase vs recovery-phase IF and camel-hump EM; the sign→Rx table
(amlodipine 2.5–5 mg, torsemide 5–10 mg, ECG tall T waves); antibiotic regimens;
99% recovery and the microhaematuria note; C3 follow-up to 8 weeks; PIGN/IRGN
C3 60%, garland/rope biopsy, vancomycin/dialysis, "steroids worsen cellulitis";
and all 8 rows of the nephrotic-vs-nephritic table read both ways.

**Ch 14 (82 q)** — renal-failure and RPRF flowcharts; RPGN definition and
features; auscultation/urine/blood panel; crescents and IF panels A–D with the
Goodpasture/diabetes/light-chain associations; the "dialyse first, then biopsy"
rule for a high creatinine; the ECG/ABG/volume-status check with calcium
gluconate 10 mL over 2–3 min, NaHCO₃ or dialysis, IVC diameter and diuretics;
absolute vs relative dialysis indications; type I–III plus the type IV/V
double-positive/double-negative table with prognosis; pulmonary renal syndrome
definition and conditions; anti-GBM α3 noncollagenous domain, triggers, HLA
high/low risk; the dialysis-disequilibrium flowchart (<1 h first session);
Goodpasture lung 75% and DLCO ↑; the four active-management indications;
PLEX + steroid/cyclophosphamide 3–6 months; transplant after 6 months of
antibody negativity; no post-transplant recurrence vs the 5% Alport risk.

**Ch 15 (54 q)** — COL4A5 deletion; the three type-IV collagen trimers and their
sites; the 80/15/5 inheritance table with affected chains, ESRD ≤30 y in males
and the AR/AD 40 y and mild patterns; the 5→30-year clinical timeline; SNHL low
then high frequency; anterior lenticonus/oil droplet; LM/IF normal with EM
splitting, lamellation and basket weave; transplant and 5% post-transplant
Goodpasture; thin GBM disease (AD COL4A4/A3, <5 y microhaematuria, good
prognosis, <200–300 nm); Fabry α-galactosidase, angiokeratoma, cornea
verticillata, ESRD 4th–5th decade, maltese crosses, podocyte vacuolation; and the
moth-eaten nail-patella syndrome (AD, LMX1B, iliac horn, benign renal course).

**Ch 16 (139 q)** — cilia function/polycystin and the four ciliopathy types;
ADPKD features (10% spontaneous, 5% nephrons, PKD1/PKD2/PKD3), the smooth-muscle
polycystin→HTN box, all three Ravinson's age bands; the six clinical features
with nocturia physiology and the "least anaemia" note; 60% ESRD by 60 y and all
five poor-prognosis indicators; MRI volume as the strongest predictor; the four
abdominal-pain complications with E. coli and the stone-type table; all
investigations (IVC rule for donation, FDG PET), tolvaptan 15 mg/LFT, SBP
95–110/DBP 60–75, prevention measures, CCC antibiotics, the six irreversible
extrarenal associations, the >10 mm aneurysm rule, the four pre-transplant
nephrectomy indications and "brain has no cysts"; ARPKD's PKHD1→fibrocystin
flowchart into collecting and biliary ducts, 70%/30% deaths, USG signs; the
10-row JN vs MCDK table (Senior Loken, Cogan, Joubert, situs inversus, gout,
insulin resistance); the 10-row ADPKD/ARPKD/JN table; and medullary sponge
kidney (not a ciliopathy, distal RTA 50%, paintbrush/bouquet, potassium citrate)
with the medullary vs cortical nephrocalcinosis lists and the oxalosis exception.

**Ch 17 (53 q)** — the >5% CKD definition and the causes table with its
secondary-fibrosis brace; etiology from ciliopathies and VUR through lithium
microcysts, calcineurin-inhibitor striped pattern, PPIs, lead and cadmium,
metabolic and hypokalemic vacuolization to sarcoid/Sjögren/IgG4 and CKDu; the
asymptomatic insidious onset; every row of the clinical-features table (anaemia
from peritubular fibroblasts, nephrogenic DI, RTA IV and RTA I cell types,
phosphate loss rickets) with the maximum/minimum anaemia note; urine <2 g/day
β₂-microglobulin with inactive sediment, deranged RFT and small kidneys; and
CKDu's theory flowchart, eastern-coast epidemiology, "asymptomatic until ESRF"
and anemia + proteinuria.

**Ch 18 (181 q)** — AKI definition and all three KDIGO stages by both urine
output and creatinine, newer markers; the pre-renal → renal → post-renal
flowchart and the six pre-renal groups; non-oliguric vs oliguric pathophysiology
and the ischemic-ATN flowchart; ATN toxins and AIN causes; the four-column drug
chart (pre-renal/ATN/obstruction/AIN mnemonics); the full 11-row pre-renal vs
ATN table plus the FeNa formula, normal 1–2% and the FeNa <1 exceptions; AIN
features, investigations and "stop insult then steroids after 1 week"; the NSAID
and aminoglycoside flowcharts with single-dose prevention; ATN's three phases
and the hypercalcemia/hypernatremia note; sepsis pathophysiology, causes,
perfusion signs, IVC 2–2.5 cm, lactate >1/>4 mmol/L and the obsolete PLR; the
crystalloid→vasopressor (noradrenaline > dopamine)→dobutamine→cortisol ladder,
the SAFE note and "no diuretics in AKI"; tumour lysis syndrome features,
rasburicase, dialysis and 5–6 L/day prevention; rhabdomyolysis causes,
pathophysiology, CPK kinetics, HAGMA with FeNa <1, benzidine 3+ with no RBCs and
its treatment; contrast-induced AKI timings and hydration; athero-embolism
(triggers, small-vessel occlusion, 75%, blue toe, livedo, Hollenhorst, labs,
skin-not-kidney biopsy, cholesterol crystals, ACE avoidance); and all five CRS
types plus the acute cortical necrosis note.

## Verification (all green after the rebuild)

```
python build_content.py    → 1371 questions, 136 units, 18 live chapters embedded
python check_integrity.py  → PASS (IDs, 4-option structure, citations, book order,
                              per-page coverage, no length-giveaway, JS syntax)
node check_app_smoke.js    → PASS (74-row roadmap, ch 13–18 paths, quiz starts)
python audit_variety.py    → AUDIT.md
```

Predictability, Chapters 13–18 (longest option is the answer; chance = 25%):

| Ch | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|
| before | 58.3% | 33.3% | 45.5% | 40.7% | 50.0% | 23.5% |
| **after** | **23.3%** | **20.7%** | **13.0%** | **23.0%** | **24.5%** | **28.2%** |

Other bank-wide signals after the re-audit: filler distractors ("none of the
above" etc.) 0.0%, answer restated in the stem 0.2%, back-to-back repeated stem
templates 0. Formats per chapter now include fill-ups, match-the-following,
true/false sets, clinical scenarios, odd-one-out, numeric/management items in
every unit — no unit is pure recall.

## Authoring rules enforced for these chapters

1. Read the rendered page (not the summary) before writing any item; zoom into
   every unclear line rather than guessing.
2. Strict book order, page by page, line by line — enforced by the part-file
   order and re-checked by `check_integrity.py`.
3. Every table becomes several questions (row-wise, pair-wise and
   compare-the-two-columns); every flowchart becomes a completion/matching item;
   every figure and arrow label becomes a question.
4. Four plausible medical options; no "none/all of the above", no page-quizzing,
   no "which statement is recorded on page X".
5. Distractors carry the same amount of clinical detail as the answer, so length
   gives nothing away (verified by the audit above).
6. Every explanation teaches the point and ends with the exact `(Book pX)`.

---

# Second-pass audit (answer-position and option-quality sweep)

The first re-audit fixed *content* (thin page-summaries → 582 exam-grade items).
A second pass then re-read **all 30 pages again** and checked every item against
its page image, and audited the *item-writing* itself. Result: **zero content
errors** (all 582 items were faithful to p775–p804), but four structural
defects were found and fixed.

| Defect found in the second pass | How many | Fix |
|---|---|---|
| Shallow "Both A / Both B" or 2-row match option sets whose distractors gave the answer away | **55 items** | Rewritten as 3-row matches with four real permutation keys, or as scenario / recall / fill-up items whose four options are all substantive medical statements |
| Match stem with no keyed list and a mislabelled format | 1 item (MED-C18-008) | Format corrected to `recall` |
| Item quizzing the printed page ("disease name printed beneath each figure") | 1 item (MED-C17-020) | Rewritten to test the pathology of the two histology panels |
| Redundant item whose content duplicates a neighbouring item | 1 item (MED-C17-043) | Deleted; its content folded into the rewritten MED-C17-042 |

Two further improvements were made at the **build** level:

1. **Answer-position bias removed.** Every item had been authored with the
   correct option at index 0 (the app shuffles at runtime, but the stored data
   was biased and any export/PDF would have inherited it). `author.py` now
   rotates each item's options deterministically (seeded by the stable question
   id), giving Ch 13–18 a spread of **A 156 / B 132 / C 157 / D 136**.
2. **Match-key diversification.** 119 match items had the correct option text
   identical ("1-A, 2-B, 3-C"). A build step (later folded into the same sweep)
   permutes each item's key list — still printed A) B) C) in order — so the
   correct permutation differs from item to item; shallow 2-row matches = **0**.

The book's own internal contradiction on C3 in PIGN/IRGN (p775 table prints
"↑C3 in 60%", p777 text prints "Serum C3: low (60% patients)") is now explicitly
taught in two items (MED-C13-013, MED-C13-059) so a learner is not misled by
either page.

### Verification after the second pass

```
python author.py 13..18     → 581 questions rebuilt from the page-anchored parts
python build_content.py     → 1370 questions, 136 units, 18 live chapters embedded
python check_integrity.py   → PASS (IDs, 4 options, citations, book order,
                              per-page coverage, no length-giveaway, JS syntax)
node check_app_smoke.js     → PASS (74-row roadmap, ch 13–18 paths, quiz starts)
python audit_variety.py     → AUDIT.md
```

Ch 13–18 now hold **581 questions** (Ch 17: 53 → 52), every one of the 30 book
pages p775–804 is cited, filler distractors remain 0.0%, and the longest-option
signal is 13–27% per chapter (chance 25%).

### Tools added

| File | Purpose |
|---|---|
| `fix_audit2.py` | Applies the 55 item rewrites, 1 relabel and 1 deletion to `data/parts/c13…c18` |
| `diversify_keys.py` | Permutes match key lists so correct-option key strings differ between items |
