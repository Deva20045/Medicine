# Chapter 6 — source-order repair, 2026-09-22

## Scope and result

**Renal Physiology, Book p734–739 / Part 1 PDF pages 42–47.**
All six pages were read from the scan (whole-page renders at 2x plus 4x–6x
crops of every formula, table cell, flowchart branch, graph and figure label)
and reconciled question by question to the shipped 133-item bank.
**133 → 138 questions; the same 10 unit IDs retained.**
Status: **reviewed with explicit source caveats**, not independent medical
validation.

The ordered checklist is `data/source_review/ch06.json` (90 source elements).
Rebuild script: `author_c6_review.py` (one-shot, guarded). Manifest writer:
`write_ch06_manifest.py`. The old page-anchored part files
(`data/parts/c6/`, `data/units/c6.json`) were removed because they encoded
the wrong keys; `data/ch06.json` is now the reviewed source of truth, as for
Ch 1–5.

| Book page | PDF page | Questions | Source blocks |
|---|---:|---:|---|
| 734 | 42 | 20 | Definition; every calculation line in printed order; figure labels + arrows; the four boxes; normal GFR; use + G5 example |
| 735 | 43 | 29 | Creatinine 4 bullets; C&G formulas + both follow-up bullets; MDRD; CKD-EPI (+ Preferred-now bracket); table row by row, both cells; Schwartz heading |
| 736 | 44 | 23 | Schwartz formula then K constants; disadvantages 1–5 in order incl. obesity note, drug flow, graph and both Eg lines |
| 737 | 45 | 18 | snGFR note + chain; both clearance formulas; cystatin C properties, advantages, disadvantages, conclusion |
| 738 | 46 | 25 | Autoregulation range/constancy; myogenic then TGF with both branches; graph; GT balance both examples; FF formula, value, chain; pressure-natriuresis theory |
| 739 | 47 | 23 | Pressure-natriuresis mechanism chain; four arteriolar bullets; table (control + 4 rows + margin notes); medullary hypoxia; normal-flow note; ACEI and NSAID blocks |

## Critical finding: 35 of 133 shipped answer keys were wrong

The live bank taught, for example, net filtration pressure **32 mm Hg**
(print: 10), calculated GFR **140 ml/min** (125), normal GFR **125–150** (90–125),
G5 requires **ACE inhibitor therapy** (dialysis), creatinine made from **urea**
(creatine), pregnancy normal creatinine **1.0–1.5** (0.3–0.6), female C&G
factor **1.2** (0.8), denominator **76** (72), C&G **preferred in children**
(obsolete), cystatin C cannot replace **PAH** (Cr), FF = **0.5** (0.1–0.2),
GT balance **180/20 (10%)** (198/2, 1%), NSAID + ACEI → **nephrocalcinosis**
(frank renal failure), b/l RAS explanation **"prostaglandins were blocking the
afferent arteriole"** (afferent not working, efferent maintains GFR), and so on.
Every explanation quoted the correct printed value while the stored `ans`
pointed at a distractor — a runtime/structural check cannot see this.

Cause: the page-anchored pipeline's `migrate_parts.py` "un-rotates" options
assuming every item was authored answer-first; for hand-authored items the
heuristic moved the correct option out of slot 0, and `author.py` then shipped
slot 0 (a distractor) as the key. **Every chapter that passed through
`migrate_parts.py` (Ch 7–12 and any other migrated bank) must have each stored
key checked against the print when reached in book order.** A text heuristic
(answer text absent from the explanation while a distractor's text is present)
flags only ~half of the Ch 6 cases, so it is a screen, not a verification.

Full list of re-keyed old IDs: 004, 005, 007, 013, 015, 022, 023, 024, 025,
031, 032, 033, 034, 038, 053, 055, 056, 057, 058, 059, 060, 070, 072, 073,
074, 075, 091, 101, 102, 118, 120, 122, 123, 124, 125.

## Order repairs (within-page)

- **p734:** the net-pressure and 125 ml/min lines were tested before the
  bracket/UF-coefficient lines that precede them; the "= net HP − net OP" line
  (old 007) sat after the figure. Now: definition → each equation line in
  print order → figure labels/arrows → boxes → normal GFR → use → G5.
- **p735:** the Jaffe's-method table cell (old 027) was tested inside the
  creatinine block, before the C&G heading; "obsolete" came after the
  bed-side/×0.8 lines. Now: 4 creatinine bullets → C&G heading → male → female
  → bed side → not preferred → MDRD → CKD-EPI → best >60 → Preferred-now bracket
  → table row 1 (L, R) → row 2 (L, R) → row 3 (L, R) → Schwartz heading.
- **p736:** K constants were tested before the eGFR formula; the diet/obesity,
  sex and after-40 lines were interleaved; the drug flow was split around the
  inverse-relationship items. Now strictly disadvantages 1 → 2 (muscle, race,
  age, sex) → 3 (diet, obesity) → 4 (drugs) → 5 (curve, graph, Eg 5→20, Eg 1.7→2.8).
- **p737:** "Beyond point of compensation" (old 078) sat after the chain
  consolidations; both clearance items now follow the formula lines in order.
- **p738:** the myogenic reflex (old 093) sat after tubulo-glomerular feedback;
  the GFR-200 example was tested before GFR-100; PAH/RPF before the FF formula.
- **p739:** the four arteriolar bullets were split around the table; the
  medullary-hypoxia and normal-flow lines sat after the ACEI/NSAID blocks.

## Uncovered lines given questions (5 new, 1 duplicate removed)

Figure vessel labels "Afferent arteriole / Efferent arteriole" (p734, replaces
old 012 which duplicated old 001 verbatim); "Not preferred now d/t
disadvantages"; "CrCl = GFR (only true for inert molecules like inulin)";
"Directly measures GFR"; "Over emphasis on BW"; "4. Schwartz equation:
Estimate GFR in children" (all p735).

## Explanation / wording repairs

- Old 099 claimed the doubling example is "300 meq filtered" — print is 200.
- Old 131 now flags the NSAID chain's back-arrow "maintain GFR ←" as an
  unexplained print feature rather than paraphrasing around it.
- Old 026/037/061 explanations now state the print caveats below explicitly.

## Source caveats retained in the manifest

- p735 prints "Cockroft", "113 Kda molecule" (true creatinine MW is 113 Da),
  "IDM (Isotope dilution mass spectrosopy)" and "CKD- Epidemiology problem
  initiative group" — taught as printed, not corrected.
- p736 prints "Sex (↓ in males)" — quoted verbatim and flagged (male creatinine
  is physiologically higher).
- p739: the NSAID back-arrow and the position of the margin words
  unfavourable / Favourable for Kidney / unfavourable (rows 2, 3, 5; row 4
  unlabelled) are recorded as read.

## Checks after the rebuild

`python3 check_integrity.py` PASS (5,366 questions, 412 units);
`node check_app_smoke.js` PASS (10,732 answer paths; 44 legacy warnings in
unreviewed chapters unchanged); `python3 audit_variety.py` Ch 6 longest-answer
23.2%, option-set reuse 5; `python3 test_source_coverage.py` 17/17;
`python3 check_source_coverage.py` 6/74 chapters reviewed — whole-book
compliance remains **NOT COMPLETE**. Next in order: **Ch 7 — Urine Analysis,
p740**, with a mandatory per-item key check because it is a migrated chapter.
