# Chapters 23–25 — build report (Acid–Base section)

Scope: **Book p819–p829** (Marrow Ed 8, Medicine Vol 3), the whole Acid–Base section:

| # | Chapter | Book pages | Units | Questions |
|---|---|---|---|---|
| 23 | Introduction to Acid Base Analysis | p819–823 | 9 | **137** |
| 24 | Metabolic Alkalosis | p824–825 | 3 | **40** |
| 25 | Methodology and Interpretation of ABG Analysis | p826–829 | 6 | **105** |
| **Total** | | **11 pages** | **18** | **282** |

Bank total after this build (Ch 19–22 having merged to `main` in parallel):
**2002 questions · 182 units · 25 live chapters**, with all **125 in-scope Book pages**
(p705–p829) represented.

Every page was **rendered from the scan and read line by line** before authoring —
tables, flowcharts, cytosolic diagrams, figure labels and arrow directions included —
and the chapters were assembled through the ordered, page-anchored pipeline
(`data/parts/c23…c25/<page><section>.json` → `author.py` → `data/chNN.json`), so book
order is enforced structurally rather than by hand.

## What each chapter covers (book order, line by line)

**Ch 23 (137 q, p819–823)**
- **p819** — the four functions that need a narrow pH range; daily H⁺ production of
  7 crore nmol against 40 nmol/L at pH 7.4; the cellulotoxic chain
  (excess H⁺ → altered cellular morphology → rendered safe by buffering); buffering
  types (chemical = immediate, respiratory = fast, renal = slow); the general chemical
  reaction; H⁺ + HCO₃⁻ → H₂CO₃ as the most potent extracellular buffer; pKa and the
  pH = pKa + log [A⁻]/[HA] rule; strong vs weak acid buffering.
- **p819 nomogram** — both axes, the right-hand [H⁺] scale (100 → 20 nmol/L), the
  pCO₂ isobars (120 → 10 mmHg) and all six labelled zones, including the normal
  7.4 / 24 / 40 intersection, queried as clinical patterns.
- **p820** — the bicarbonate system (1st compensation in metabolic acidosis; exhaled
  CO₂ → ↓PaCO₂ as the 2nd compensation), phosphate buffer (pKa 6.8, 2nd most effective,
  better intracellularly) and haemoglobin buffer (pKa 7.3, best intracellular);
  metabolic acidosis causes (acid generation: exogenous methanol, endogenous
  ketoacids; alkali loss: GI and renal); the full anion gap derivation;
  NAGMA/hyperchloremic acidosis with GI (VIPoma, ureterosigmoidostomy) and renal (RTA)
  causes; HAGMA and the KUSMAL list read letter by letter.
- **p821** — acidemia/alkalemia thresholds (7.36/7.44) versus acidosis/alkalosis as
  unopposed states; the H⁺ ladder (pH 7.2 = 63 → 7.6 = 25 nmol/L) with the ×1.25 and
  ×0.8 steps and a worked correction of a wrong estimate; respiratory buffering chain;
  renal non-volatile (sulphuric, phosphoric) vs volatile acid handling; 1 mEq/kg/day
  (80 mEq/day) excretion as titratable acid and ammonia; 4330 mEq/day filtered HCO₃⁻
  (24 × 180 L), zero urinary HCO₃⁻ and the PCT ≈ 4000 mEq > thick AL > DCT reabsorption
  order; the **PCT diagram** — luminal Na⁺–H⁺ exchanger, CA IV (step ①), H₂CO₃ split
  (step ②), CA II (step ③), dissociation (step ④), basolateral Na⁺–HCO₃⁻ exchanger,
  plus the H₂O/Na⁺/Ca²⁺ arrows — including an acetazolamide prediction item.
- **p822** — 1 mEq H⁺ per 1 mEq HCO₃⁻ reabsorbed and the 4330 + 80 = 4400 mEq H⁺
  requirement labelled “not practically possible” (hence buffering); **type 2 RTA**
  (generalised PCT dysfunction; Na⁺–HCO₃⁻ exchanger or carbonic anhydrase defect;
  childhood Fanconi's syndrome with cystinosis m/c, Lowe's disease, Wilson disease in
  adolescence; adult myeloma and the four drugs); the three PCT-defect arms (NAGMA →
  salt water wasting → RAS activation → hypokalemia; phosphaturia → rickets-like
  changes; glycosuria); the **α-intercalated cell** diagram (H⁺-ATPase and
  H⁺,K⁺-ATPase both ATP-dependent, CA II, titratable vs non-titratable acid) and the
  net acid secretion formula.
- **p823** — **distal RTA** (H⁺-ATPase / H⁺,K⁺-ATPase defect) with every outflow:
  severe NAGMA, severe hypokalemia, salt wasting with RANS activation, ↑Ca²⁺ resorption
  → rickets-like change and stones, alkaline urine, no glycosuria; all **seven rows of
  the distal vs proximal RTA table** read in both directions (severity, rickets
  mechanism, stones, urine pH, glycosuria, inherited and acquired causes); the urine
  anion gap formula, its slightly negative normal value and the positive/negative
  significance; ammonia formation from glutamine → glutamate → α-keto glutarate in the
  proximal tubules.

**Ch 24 (40 q, p824–825)**
- **p824** — Henderson–Hasselbalch in both printed forms and [H⁺] = 24 × PaCO₂/HCO₃⁻;
  the ↑HCO₃⁻ → ↑PaCO₂ response with the p827-style label conflict explained; the renal
  decision flowchart (excreted with Cl⁻ conserved → no alkalosis vs failure to excrete
  → alkalosis); **ECF volume expansion** = saline-unresponsive alkalosis with urine
  Cl⁻ > 40 mEq/L and the three renin/aldosterone columns (Conn's; RAS and
  renin-secreting tumours; Liddle syndrome with the ENaC gain-of-function mutation);
  the “other causes” group — Cushing syndrome, apparent mineralocorticoid excess with
  the blocked cortisol → cortisone step, and glucocorticosteroid remediable
  aldosteronism via ACTH.
- **p825** — the alkalosis–hypokalemia–HTN triangle; ECF volume contraction features
  (secondary hyperreninemic hyperaldosteronism, ↓GFR with ↓urine Cl⁻ and ↓urine K⁺,
  saline responsiveness) and its GI/renal causes; the full **urine chloride ladder**
  (low < 25, normal > 40, high) including the early- vs late-phase diuretic
  distinction and the Bartter/Gitelman column; the closing note splitting metabolic
  acidosis into acid generation (high anion gap) and alkali loss, with GI (−ve UAG,
  VIPoma) versus renal (+ve UAG, RTA) causes.

**Ch 25 (105 q, p826–829)**
- **p826** — equipment (ABG analyzer, 1 ml syringe with 0.5 ml heparin and no excess,
  70% alcohol wipe and gauze, gloves and cover roll) and every pre-requisite (> 50%
  blood, syringe ≤ 3 ml, no air bubbles because they cause ↑PO₂/↓PCO₂, cold chain);
  Allen's test with the figure labels; the procedure steps (non-dominant wrist
  extended 20–30°, radial palpation, sterilisation, needle at 45°, capping and
  transport); the heparin dilutional effect (↓HCO₃⁻, ↓PCO₂); and the **delay table**
  values per 10 minutes at 37°C versus 4°C (pH 0.01/0.001, pCO₂ 1/0.1 mmHg,
  pO₂ 0.1%/0.01%).
- **p827** — all four contraindications; all five puncture sites in order; the
  measured → derived parameter arrow (HCO₃⁻, anion gap, base excess); the four primary
  problems with the acute/chronic bracket on the respiratory arms; the three reading
  methods; **Boston normal values** (7.4 / 40 / 24) with both rearrangements of the
  24-rule; the ±2 mEq validity rule against a venous sample; step 1 (pH 7.4 cut-off).
- **p828** — the full step-2 decision tree in both pH directions; both step-3
  compensation tables row by row (metabolic acidosis ↓HCO₃⁻/↓PaCO₂ → respiratory
  alkalosis; metabolic alkalosis ↑HCO₃⁻/↑PaCO₂ → respiratory acidosis; respiratory
  acidosis ↑PaCO₂/↑HCO₃⁻; respiratory alkalosis ↓PaCO₂/↓HCO₃⁻) with the printed
  quantitative rules — 1.2 mmHg and 0.7 mmHg per 1 mEq/L HCO₃⁻, and 10 mmHg PaCO₂ →
  1/4 mEq/L (acute/chronic rise) or 2/4 mEq/L (acute/chronic fall) HCO₃⁻ — worked as
  numbers and as chronic-versus-acute scenarios; the mirrored **adequacy-of-
  compensation** flowchart (≤ and ≥ expected value = adequate, between expected and
  normal = partial).
- **p829** — the **compensatory limits table** (respiratory acidosis ↑ up to 30 acute
  and 45 mEq/L chronic; respiratory alkalosis ↓ up to 20 acute and 12–14 mEq/L
  chronic) including a “beyond the limit” scenario; the anion gap derivation, formula
  and 12 ± 2 mEq/L with a worked corrected AG (AG + 2.5 (4.5 − S.albumin));
  the **osmolal gap** definition, the four-term calculated osmolality, the < 10 vs
  ≥ 10 mOsm/kg cut-off and the methanol/ethylene glycol examples; and the **delta
  ratio** (ΔAG/ΔHCO₃⁻) with all three bands (< 1 = HAGMA + NAGMA, 1–2 = HAGMA,
  > 2 = HAGMA + metabolic alkalosis) tested forwards and backwards.

## Quality gates (all green)

```
python build_content.py      → 2002 questions, 182 units, 25 live chapters embedded
python check_integrity.py    → PASS (IDs, 4-option structure, citations, book order,
                               per-page coverage, no length-giveaway, JS syntax)
node check_app_smoke.js      → PASS (74-row roadmap, 25 live paths, quiz starts,
                               first/last question page of every chapter)
python audit_variety.py      → AUDIT.md
```

Per-chapter predictability (longest option is the answer; chance = 25%):

| Chapter | Longest-option rate | Answer-term leak | Shallow 2-row matches |
|---|---|---|---|
| 23 | **22.6%** | 0.0% | 0 |
| 24 | **25.0%** | 0.0% | 0 |
| 25 | **24.8%** | 0.0% | 0 |

Bank-wide after the build: filler distractors 0.0%, answer-as-only-hedged-option 0.3%,
answer restated in the stem 0.1%, zero back-to-back repeated stem templates.
Answer positions are rotated deterministically by `author.py`, so no option letter
carries a hidden bias: Ch 23 A31/B27/C36/D43, Ch 24 A8/B7/C10/D15,
Ch 25 A25/B22/C20/D38.

Formats in every unit include fill-ups, match-the-following (≥ 3 keyed rows),
true/false sets, clinical scenarios, odd-one-out, numeric and recall items — no unit
is pure recall.

## Authoring rules applied

1. Read the rendered page (not a summary) before writing any item; zoom into every
   unclear line rather than guessing.
2. Strict book order, page by page — enforced by the part-file order and re-checked by
   `check_integrity.py`.
3. Every table becomes several questions read **both ways** (row-wise, pair-wise and
   compare-the-two-columns); every flowchart becomes a completion/matching item; every
   figure and arrow label becomes a question, with at least one clinical application
   per unit.
4. Four plausible medical options; no “none/all of the above”, no page-quizzing.
   Distractors carry the same amount of clinical detail as the answer so length gives
   nothing away (verified by the audit above).
5. Every explanation teaches the point and ends with the exact `(Book pX)`.

## Book inconsistencies taught explicitly (not silently copied)

| Page | Printed | Resolved by |
|---|---|---|
| p824 | “↑HCO₃⁻/metabolic alkalosis → ↑PaCO₂/respiratory alkalosis” | The p828 compensation table calls the same ↑PaCO₂ change a respiratory **acidosis**; both labels are taught side by side in one item. |
| p827 | The metabolic arms of the primary-problem tree carry the bicarbonate arrows in the reverse sense | The p828 step-2 flowchart (↓HCO₃⁻ = metabolic acidosis, ↑HCO₃⁻ = metabolic alkalosis) is the convention followed; the discrepancy itself is taught in one true/false item. |
| p825 | Diuretics appear in both the low (late phase) and high (early phase) urine-chloride bands | Explicit early- vs late-phase item so the ladder is not misread. |

## Files added

| Path | What it is |
|---|---|
| `data/parts/c23/` (14 parts) · `data/parts/c24/` (6) · `data/parts/c25/` (13) | Ordered, page-anchored authoring parts |
| `data/units/c23.json` (9) · `c24.json` (3) · `c25.json` (6) | Concept-named unit definitions |
| `data/ch23.json` · `ch24.json` · `ch25.json` | Assembled chapter artifacts (source of truth) |
| `author.py`, `check_integrity.py` | Chapter registry extended with 23–25 |
