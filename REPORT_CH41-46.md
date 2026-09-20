# Report — Chapters 41–46 (Part 4, Book p902–935)

**418 new questions · 34 units · all 34 pages p902–935.**

| Chapter | Title                              | Pages | Units | Questions | Format mix (fill/match/tf/scen/odd/recall/num/mgmt) |
| ------- | ---------------------------------- | ----- | ----- | --------- | ---------------------------------------------------- |
| 41      | Thyroid Function Tests             | 902–904 | 3 | 38  | 5 / 9 / 8 / 9 / 4 / 3 / 0 / 0 |
| 42      | Hypothyroidism                     | 905–909 | 5 | 63  | 10 / 15 / 15 / 15 / 7 / 1 / 0 / 0 |
| 43      | Thyrotoxicosis and Thyroiditis     | 910–916 | 7 | 86  | 14 / 21 / 21 / 21 / 8 / 1 / 0 / 0 |
| 44      | Diabetes Mellitus & Classification | 917–926 | 10 | 123 | 20 / 30 / 30 / 30 / 11 / 2 / 0 / 0 |
| 45      | Insulin Physiology & Acute Comp.   | 927–932 | 6 | 72  | 12 / 18 / 18 / 18 / 6 / 0 / 0 / 0 |
| 46      | DM Management — 2024 Guidelines    | 933–935 | 3 | 36  | 6 / 9 / 9 / 9 / 3 / 0 / 0 / 0 |

## Pipeline

1. **Source render.** All 34 pages rendered at zoom 3.0 (`_render/_902.png`–`_935.png`) from `uploads/Medicine_Vol3_Part4_pages_894-964.pdf` (K = 893).
2. **Visual read-through.** Every page read end-to-end; ambiguous table cells, arrows and footer entries re-cropped at zoom 4.0 (`_render/zoom_*.png`). Twelve zoom crops generated to verify p902 TBG excess, p904 totals vs frees arrows, p905 lithium / IFN-α / amiodarone lines, p907 complications row, p909 taper & 3 a.m. note, p915 graph axes, p918 ominous-octet schematic, p920 metformin / screening age line, p923 marker table, p925 antibody-vs-subtype arrow scheme, p932 header strip.
3. **Authoring.** Each page → `data/parts/cNN/<page>a.json` (one part per page, in book order). Units in `data/units/cNN.json` follow concept-based titles (one unit per page) so the path reflects the source's narrative arc.
4. **Assembly.** `python author.py 41…46` rebuilds `data/chNN.json` with deterministic SHA-256 answer rotation; gates four distinct options, no length giveaway (>3× longest distractor), no banned filler, mandatory `(Book pNN)` citation, valid format token.
5. **Embed.** `python build_content.py` writes the inline `QUESTIONS`/`UNITS`/`CHAPTERS` arrays in `pulse-medicine.html`.
6. **Gates.** `python check_integrity.py` and `node check_app_smoke.js` both pass (verified extraction: **3,533 questions / 296 units / 74 chapters / 48 live**).
7. **Variety audit.** `python audit_variety.py` — every new chapter mixes fill-ups, match, true/false, scenario and odd-one-out; answer-position spread is balanced by the SHA-256 rotation; no chapter shows predictable option patterns.

## Coverage check — every page asked

| Book page | Topic anchor                                                              | Sample ID    |
| --------- | ------------------------------------------------------------------------- | ------------ |
| p902      | Hormone levels, TBG/albumin/transthyretin, RTH, MCT8 & CNS transport      | MED-C41-001  |
| p903      | Tc-99m ectopic scan, BMR, cardiac alpha, thermogenesis, metabolic actions | MED-C41-014  |
| p904      | Drugs & TFT (inducers, inhibitors), CLIA TSH (0.5-5), 7-row table         | MED-C41-027  |
| p905      | Primary/secondary/consumptive/congenital classification; lithium, IFN-a   | MED-C42-001  |
| p906      | Hashimoto features, HLA, Hurthle cells, germinal centers, MALT lymphoma   | MED-C42-014  |
| p907      | Slowing, TSH-driven GAG deposition, Hoffman syndrome, complications       | MED-C42-026  |
| p908      | Autoantibody workup, TSH cut-offs, L-thyroxine dosing (<60 vs elderly)    | MED-C42-039  |
| p909      | Empty stomach rules, follow-up, myxedema coma protocol, SREAT             | MED-C42-051  |
| p910      | Thyrotoxicosis classification, Graves demographics, Wolff-Chaikoff & Jod  | MED-C43-001  |
| p911      | TRAb triad (eye, dermopathy, acropachy), apathetic, periodic paralysis    | MED-C43-013  |
| p912      | Scintigraphy grid, IM SLOW, 40/40/20, eye signs (Von Graefe, Möbius)      | MED-C43-025  |
| p913      | Thionamide equivalents, PTU pregnancy, rash/agranulocytosis, RAI, surgery | MED-C43-037  |
| p914      | Thyrotoxic crisis 4-drug protocol, acute piriform, de Quervain, Riedel    | MED-C43-050  |
| p915      | Subacute release mechanism, triphasic graph, postpartum comparison        | MED-C43-062  |
| p916      | Amiodarone Type I vs Type II, Subacute vs Graves vs Toxic MNG grid        | MED-C43-074  |
| p917      | Three diagnostic pillars (FPG, 2-h PG, HbA1c); pre-diabetes ranges        | MED-C44-001  |
| p918      | Ominous octet; hepatic gluconeogenesis primary defect                    | MED-C44-014  |
| p919      | Classification; MODY 2 vs MODY 3                                         | MED-C44-027  |
| p920      | Pre-DM treatment; ADA targets by age / comorbidity                       | MED-C44-040  |
| p921      | LADA, type 3c, Wolfram (DIDMOAD), mitochondrial                          | MED-C44-053  |
| p922      | Metabolic syndrome criteria; Asian-Indian BMI cut-offs                   | MED-C44-066  |
| p923      | T1DM autoantibody panel (GAD, IA-2, ZnT8, IAA); HLA                      | MED-C44-079  |
| p924      | Insulin-resistance syndromes (A, B, HAIR-AN); neonatal diabetes genes     | MED-C44-092  |
| p925      | Pancreatic / drug-induced DM; antibody → subtype algorithm               | MED-C44-105  |
| p926      | Endocrine (Cushing, acromegaly, pheo) and pancreatic tumour diabetes      | MED-C44-118  |
| p927      | Insulin structure / secretion / signalling                               | MED-C45-001  |
| p928      | GLUTs, C-peptide interpretation, incretins                               | MED-C45-013  |
| p929      | GLP-1 RAs; dual GIP/GLP-1 (tirzepatide)                                  | MED-C45-025  |
| p930      | DKA pathophysiology, features, lab work-up                               | MED-C45-037  |
| p931      | DKA protocol (3/3+3/9+3/12, KCl, regular insulin); HHS; SGLT2 eDKA       | MED-C45-049  |
| p932      | Basal-bolus / premixed / CSII; dawn vs Somogyi; CGM                      | MED-C45-061  |
| p933      | ADA 2024 drug class map; SGLT2i and GLP-1 RA CV outcome trials           | MED-C46-001  |
| p934      | Dual therapy threshold; insulin indications; trial names                  | MED-C46-013  |
| p935      | BP / LDL / aspirin / renal triple (ACEi + SGLT2i + finerenone) targets   | MED-C46-025  |

## Variety and predictability

All five requested formats are represented in every chapter. The audit shows
filler-distractor use at 0.0%, hedge-only correct at 0.3%, longest-option-is-answer
at 28.9% bank-wide — slightly above the 25–27% range reported for Ch 36–40 but
within the historical band for our poly-format chapters. The audit was rerun
after the option-length equalisation pass so that no question's correct option
exceeds 3× the longest distractor. No stem template repeats back-to-back inside
a unit.

## Source-contradiction flags (taught explicitly)

1. **p907 complications column.** The page lists "Hypocholesterolaemia" among
   hypothyroid complications. Hypothyroidism classically causes
   *hyper*cholesterolaemia; the source label is therefore an inconsistency. Items
   note the page's literal label while the explanation flags the discrepancy so
   the learner is not surprised by clinical practice.
2. **p904 sick-euthyroid row.** The schematic shows totals *normal* with
   free-hormone arrows pointing upward (free T4/FT3 ↑) — at odds with the
   lab-trajectory convention of normal totals with FT3 ↓ and rT3 ↑. The
   explanation teaches the standard three-pattern interpretation and flags the
   page's atypical arrow direction.
3. **p918 ominous-octet schematic.** The diagram labels CPT-1 as "Absent in
   liver" while showing fatty-acyl-CoA accumulation leading to insulin
   resistance. CPT-1 is physiologically present in liver; the printed label is
   an inconsistency. Items teach the actual biology and flag the source.
4. **p920 screening-age note.** The source lists "Age 2–60 yrs"; the ADA's
   current guidance starts screening at ≥35 in overweight adults. The
   explanation notes the inconsistency and the standard cut-off.
5. **p925 antibody arrow scheme.** The page's algorithm draws
   *high antibodies → T1DM, low antibodies → LADA, no antibodies → T2DM/MODY*,
   which is the inverse of the C-peptide picture on p928 (T1DM undetectable,
   T2DM raised). Items teach the C-peptide table as the consistent reference
   and flag the inverted arrow.

## Source pages verified (zoom crops)

`zoom_902_causes.png`, `zoom_904_table.png`, `zoom_905_ifn.png`,
`zoom_907_comp.png`, `zoom_907_comp2.png` (footer re-crop), `zoom_909_taper.png`,
`zoom_915_graph.png`, `zoom_918_top.png`, `zoom_918_bot.png`, `zoom_920_met.png`,
`zoom_923_mark.png`, `zoom_925_algo.png`, `zoom_932_top.png`. All retained in
`_render/`.

## Final verification

```
$ python check_integrity.py
Verified extraction: 3533 questions, 296 units, 74 chapters.
PASS: 48 live chapter(s) of 74; 3533 questions; 296 units; all 240 in-scope
Book pages represented; IDs, four-option structure, citations, order, source
artifacts, UI hooks, and JavaScript syntax verified.

$ node check_app_smoke.js
PASS: 544 new-question answer paths across 19 units; matching boards, blanks,
feedback, locking and completion verified.
PASS: roadmap of 74 chapters (48 live, rest "Soon"), … Chapter 1… 46, 60, 61 …
```

**Live preview:** https://deva20045.github.io/Medicine/ (after merge to `main`).
