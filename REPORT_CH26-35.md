# Chapters 26–35 — build report (Endocrinology opening + Bone/Mineral section)

Scope: **Book p830–p882** (Marrow Ed 8, Medicine Vol 3) — the opening Endocrinology
chapters (hormones, adrenal cortex/medulla) and the start of the bone–mineral section:

| # | Chapter | Book pages | Units | Questions |
|---|---|---|---|---|
| 26 | Overview of Hormones | p830–836 | 7 | **71** |
| 27 | Physiology of Adrenal Cortex | p837–840 | 4 | **39** |
| 28 | Conn's Syndrome | p841–843 | 3 | **29** |
| 29 | Cushing's Syndrome | p844–848 | 5 | **50** |
| 30 | Addison's Disease | p849–851 | 3 | **33** |
| 31 | Adrenal Medulla : Part 1 | p852–857 | 5 | **53** |
| 32 | Adrenal Medulla : Part 2 | p858–862 | 5 | **45** |
| 33 | Basics of Bone and Mineral Metabolism | p863–873 | 6 | **89** |
| 34 | Calcium Metabolism | p874–876 | 3 | **29** |
| 35 | Hypercalcemia | p877–882 | 6 | **64** |
| **Total** | | **53 pages** | **47** | **502** |

Bank total after this build (on top of the parallel Ch 6–15 re-audit merge, PR #9):
**2676 questions · 227 units · 35 live chapters**, with all **178 in-scope Book pages**
(p705–p882) represented.

Every page was **rendered from the scan and read line by line** before authoring —
tables, flowcharts, hormone trees, enzyme ladders, scan images (sestamibi, hand and
skull X-rays) and arrow directions included — and the chapters were assembled through
the ordered, page-anchored pipeline (`data/parts/c26…c35/<page><section>.json` →
`author.py` → `data/chNN.json`), so book order is enforced structurally rather than by
hand.

## What each chapter covers (book order, line by line)

**Ch 26 (71 q, p830–836)**
- **p830** — structure-based classification of hormones (peptide, steroid, amine rows)
  with every listed member queried both ways.
- **p831** — tryptophan derivatives (serotonin/melatonin chain), the sleep–wake cycle
  and the 80/20 rules printed on the page.
- **p832** — mechanism-based classification; Group I (nuclear) hormones and their
  receptor logic.
- **p833** — Type II nuclear receptors, orphan receptors and the PPAR agonist set.
- **p834** — Group II hormones: second messengers and the full GPCR cycle steps.
- **p835** — the GPCR hormone map (cAMP vs IP3/DAG arms), cGMP vasodilators and TKR.
- **p836** — JAK–STAT cytokine receptors and serine–threonine kinase receptors
  (TGF-β/activin family), with receptor→hormone matching in both directions.

**Ch 27 (39 q, p837–840)**
- **p837** — adrenal anatomy, embryology (cortex mesoderm, medulla neural crest) and
  the three-artery blood supply.
- **p838** — relations, the fetal zone and the definitive zones (glomerulosa →
  fasciculata → reticularis) with zone-product pairing.
- **p839** — the steroidogenesis enzyme ladder (cholesterol → aldosterone/cortisol/
  androgens), zone-specific enzymes and every step's blocker.
- **p840** — 11β-HSD2 defects: apparent mineralocorticoid excess and licorice, with
  the cortisol→cortisone block taught as a mechanism item.

**Ch 28 (29 q, p841–843)**
- **p841** — Conn's syndrome classification (adenoma vs hyperplasia) and the P-cell
  pathophysiology chain.
- **p842** — presentation (HTN + hypokalemia), who-to-screen recommendations and the
  drug-aware first-line work-up (drug effects on renin/aldosterone read both ways).
- **p843** — confirmatory saline infusion testing and CT lateralisation, with
  pre-test drug washout rules.

**Ch 29 (50 q, p844–848)**
- **p844** — Cushing definitions (syndrome vs disease), the causes table and metabolic
  effects.
- **p845** — other systemic effects, the eosinopenia clue and the cause tree.
- **p846** — important symptoms, childhood Cushing's (m/c cause by age) and the first
  diagnostic cut-offs.
- **p847** — the diagnostic algorithm: diurnal cortisol, low-dose DST and ACTH
  evaluation branches, each read forward and backward.
- **p848** — IPSS, high-dose DST discrimination, pseudo-Cushing features and medical
  therapy.

**Ch 30 (33 q, p849–851)**
- **p849** — Addison's classification, autoimmune (m/c) vs tuberculous causes and the
  hormone-deficiency feature set.
- **p850** — Addisonian crisis, the full 1° vs 2° table (pigmentation, K+, ACTH…) read
  both ways, cortisol and Synacthen tests.
- **p851** — maintenance replacement, steroid equivalence table and the crisis
  regimen (IV hydrocortisone + fluids) with dose items.

**Ch 31 (53 q, p852–857)**
- **p852** — medullary development, catecholamine biosynthesis ladder and the PNMT
  (cortisol-dependent) rule.
- **p853** — adrenomedullin, pheochromocytoma definition and the types tree
  (sporadic vs familial, 10% rules).
- **p854** — pathophysiology and the clinical triad, BP patterns (sustained vs
  paroxysmal).
- **p855** — incidentaloma alarms, cardiac effects, histology (Zellballen) and drugs
  affecting pre-test biochemistry.
- **p856** — biochemical screening (metanephrines), imaging and the surgical TOC.
- **p857** — pre-operative α- then β-blockade order and intraoperative crisis
  management.

**Ch 32 (45 q, p858–862)**
- **p858** — MEN syndromes overview and MEN1 (gene, 3P majors).
- **p859** — MEN1 organ-by-organ (parathyroid m/c, pancreatic, pituitary) and the
  MEN2A gene.
- **p860** — MEN2A variants, MEN2B/MEN3 features (marfanoid, mucosal neuromas) and
  MEN4.
- **p861** — the phakomatosis/syndrome gene table and Carney's triad vs complex.
- **p862** — RCC comparisons, Cushing's m/c cause by age and the APS 1/2 table.

**Ch 33 (89 q, p863–873)**
- **p863** — bone types (cortical vs trabecular) and trabecular assessment sites.
- **p864** — bone constituents and the collagen-type table (type I bone, II cartilage…),
  with the warfarin–osteocalcin link.
- **p865** — bone formation hypotheses and ALP isoforms.
- **p866** — osteoblast/osteocyte/osteoclast biology and the FGF23 axis entry.
- **p867** — RANK/RANKL/OPG, calcitonin and the bone remodelling cycle.
- **p868** — turnover markers (bsALP, CTX…) and vitamin D mechanism.
- **p869** — vitamin D metabolism steps and the drugs affecting it (calcitriol trio).
- **p870** — jejunal vitamin D action, anti-proliferative effect and PTH basics
  (2nd-gen assay note).
- **p871** — parathyroid anatomy/transcription factors and the PTH–vitD–FGF23 loop.
- **p872** — FGF23 actions, the PTH vs vitamin D table and the vitamin D assay
  (25(OH)D, 50k IU item).
- **p873** — PTH adverse effects, receptors, the sigmoid rule and CaSR mutations
  (senile osteoporosis note).

**Ch 34 (29 q, p874–876)**
- **p874** — total body calcium (1000–1300 g; 99.3% bone / 0.6% soft tissue with 48%
  ionized–40% albumin–12% other / 0.1% ECF); corrected Ca 8.6–10.3 and the
  +0.8×(4−albumin) formula; <8.4 hypo / >10.5 hyper; ionized-Ca functions; H+ competing
  for albumin (↓pH 0.1 → ↑Ca 0.1 meq/L); jejunal absorption (jejunum > duodenum, 20%
  net ≈ 200 mg, acid enhances) with the 95% transcellular calcitriol-controlled vs 5%
  paracellular split; calcitriol → nuclear receptor → calbindin → TRPV5/6 → Ca-ATPase.
- **p875** — ~200 mg/day urinary loss (4 mg/kg/24 h); the stone thresholds "4/7/11"
  (hypercalciuria >4 m/c, hyperuricosuria >7 second, hypocitraturia <11); milk-alkali
  >4 g/day chain; hypercalcemia → CaSR → ↓absorption + ↓ADH → volume depletion → RAAS →
  metabolic alkalosis; renal handling PCT 65% (independent) / TAL 25% (dependent) /
  DCT 10% (most dependent) with CLDN16/19 + claudin-14; the seconds-vs-days CaSR
  response table (parathyroid immediate vs TAL delayed) read both ways.
- **p876** — half-lives (PTH 2–4 min, calcitriol 6–8 h, 25(OH)D3 2–3 weeks = assay
  form); CaSR gain-of-function → Bartter type V (AD, all others AR) with ↑↑↑ excretion
  → hypocalcemia; CaSR loss-of-function → FHH in children (no excretion → complete
  reabsorption → hypocalciuria + hypercalcemia).

**Ch 35 (64 q, p877–882)**
- **p877** — >10.5 mg/dl starts evaluation (0.25 mmol = 0.5 meq/l = 1 mg/dl); the three
  cause groups (parathyroid 80% / Vit-D 20% / miscellaneous); primary HPT (m/c overall,
  F>M, 6th decade, adenoma 85% inferior gland, hyperplasia MEN1>2A, MEON CDC73,
  sporadic); FHH (AD CaSR loss, low urine Ca); lithium inhibits CaSR; tertiary in CKD;
  PTHrP (SCC lung/head–neck); 1α-hydroxylase tumours (lymphoma, sarcoidosis,
  acromegaly); miscellaneous endocrine (Addison's, pheo, thyrotoxicosis), milk-alkali,
  thiazide, osteolytic (breast m/c, lung, myeloma).
- **p878** — m/c asymptomatic; acute abdominal triad mimicking pancreatitis;
  neuropsychiatric list; short QT (vs long QT in hypocalcemia); chronic set (fatigue
  2nd m/c, painful bones, stones/UTI, myopathy, band keratopathy, pseudoclubbing); the
  Bone/Stone/Groan/Moans/Overtone mnemonic; renal presentations (neurogenic DI →
  polyuria → dehydration → pre-renal AKI; CTD); "no diarrhea/seizures" note.
- **p879** — CTD additions (hypokalemia, hyperoxaluria, hyperuricosuria); iPTH 2nd-gen
  immunoradiometric, 50–100 pg/ml; normal PTH + high Ca → suspect parathyroid
  dependent; >50 + ↓PO4 + ↑↑urine Ca → adenoma (Tc99 sestamibi IOC, oxyphil binding);
  <50 branch: 25↑&1,25↑ = hypervitaminosis D vs 25N&1,25↑ = 1α-hydroxylase tumours;
  <20 = PTHrP paraneoplastic (SCC lung m/c) → CT/PET.
- **p880** — the 1°/2°/3° table (causes; PTH >50 / 500–1000 / >1000; Ca↑/↓/↑↑;
  PO4↓/↑/↑↑) read in every direction; bone changes 1–6 (diffuse resorption m/c with the
  subperiosteal radial-side phalanx sign most characteristic; rugger jersey =
  intercortical; brown tumor; salt-and-pepper skull; endosteal scalloping; acral
  osteolysis).
- **p881** — osteitis fibrosa cystica chain (resorption > formation → fracture →
  fibrous/cystic); adenoma surgery absolute (single-gland excision curative, no medical
  role); asymptomatic indications (<50 yr, renal failure, urine Ca >400 mg/day,
  osteoporosis, S.Ca >1 mg/dl above baseline); crisis 1st line (fluids 300–400 ml/hr,
  IV Lasix not recommended, calcitonin 4 U/kg S/C BD, zoledronate 4 mg in 50 ml saline
  + 50 ml dextrose 5% preferred / pamidronate); 2nd line oral prednisolone (only
  osteolysis/Vit-D dependent) + denosumab.
- **p882** — malignancy mechanisms (PTHrP m/c humoral a/w SCC lung; lymphoma
  1α-hydroxylase; osteolysis → crisis with breast m/c, myeloma, lung); paediatric
  table Jansen (X-linked, PTH type-1 receptor activation; short stature, dementia,
  disorientation, abnormal facies, severe bone) vs FHH (AD, CaSR loss; mild, fatigue,
  weakness).

## Quality gates (all green)

```
python build_content.py      → 2676 questions, 227 units, 35 live chapters embedded
python check_integrity.py    → PASS (IDs, 4-option structure, citations, book order,
                               per-page coverage, no length-giveaway, JS syntax;
                               all 178 in-scope Book pages represented)
node check_app_smoke.js      → PASS (74-row roadmap, 35 live paths, quiz starts,
                               first/last question page of every chapter)
python audit_variety.py      → AUDIT.md
```

Per-chapter predictability (longest option is the answer; chance = 25%):

| Chapter | Longest-option rate | Answer-term leak | Reuse |
|---|---|---|---|
| 26 | 29.6% | 5.6% | 6 |
| 27 | 23.1% | 0.0% | 6 |
| 28 | 37.9% | 3.4% | 4 |
| 29 | 52.0% | 0.0% | 2 |
| 30 | 42.4% | 0.0% | 1 |
| 31 | 50.9% | 1.9% | 0 |
| 32 | 55.6% | 0.0% | 4 |
| 33 | 46.1% | 1.1% | 9 |
| 34 | 55.2% | 0.0% | 3 |
| 35 | 31.2% | 0.0% | 7 |

The hard gates (no filler distractors, four distinct medical options, answer ≤ 3× the
longest distractor, no banned phrases, option rotation at runtime) are all enforced by
`check_integrity.py`; the longest-option column above is the audit's soft signal and is
reported as-is, as in prior reports. Answer positions are rotated deterministically by
`author.py`, so no option letter carries a hidden bias.

Formats in every unit include fill-ups, match-the-following (≥ 3 keyed rows),
true/false sets, clinical scenarios, odd-one-out, numeric and recall items — no unit
is pure recall (Ch 34–35 each gained scenario/fill-up/odd-one-out coverage this pass).

## Authoring rules applied

1. Read the rendered page (not a summary) before writing any item; zoom into every
   unclear line rather than guessing.
2. Strict book order, page by page — enforced by the part-file order and re-checked by
   `check_integrity.py`.
3. Every table becomes several questions read **both ways** (row-wise, pair-wise and
   compare-the-two-columns — e.g. the 1°/2°/3° HPT table, the Jansen-vs-FHH table, the
   PCT/TAL/DCT calcium split); every flowchart becomes a completion/matching item
   (cause trees, the iPTH algorithm, the crisis regimen); every figure and arrow label
   becomes a question, with at least one clinical application per unit.
4. Four plausible medical options; no “none/all of the above”, no page-quizzing.
   Distractors carry the same amount of clinical detail as the answer so length gives
   nothing away beyond the enforced 3× cap (verified by the audit above).
5. Every explanation teaches the point and ends with the exact `(Book pX)`.

## Book inconsistencies taught explicitly (not silently copied)

| Page | Printed | Resolved by |
|---|---|---|
| p876 | Bartter type V (CaSR gain-of-function) causes hypocalcemia while “all other Bartter types” show hypercalcaemia | Taught exactly as printed, with a contrast item pairing type V hypocalcemia against the other Bartter types. |
| p879 | “Tc99 sestamibi binds with oxyntic cell” | The intended cell is the parathyroid **oxyphil** cell; items use oxyphil and the scan-image caption is explained. |
| p881 | IV Lasix sits on the 1st-line crisis branch but is flagged “(not recommended)” | Both facts taught together in one true/false item so the branch is not misread as an endorsement. |
| p877 | PTHrP-dependent cause printed with a bare “↓↓” arrow | Items teach the SCC lung/head–neck association without over-interpreting the arrow. |

## Files added

| Path | What it is |
|---|---|
| `data/parts/c26/`…`data/parts/c35/` | Ordered, page-anchored authoring parts (53 part files) |
| `data/units/c26.json`…`c35.json` | Concept-named unit definitions (47 units) |
| `data/ch26.json`…`ch35.json` | Assembled chapter artifacts (source of truth) |
| `author.py`, `check_integrity.py` | Chapter registry extended with 26–35 |
| `REPORT_CH26-35.md` | This report |
