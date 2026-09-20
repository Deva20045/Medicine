# Report — Chapters 47–51 (Part 4, Book p936–961)

**317 new questions · 26 units · all 26 pages p936–961.**

| Chapter | Title                              | Pages | Units | Questions | Format mix (fill / match / tf / scen / odd / recall / num / mgmt) |
| ------- | ---------------------------------- | ----- | ----- | --------- | ----------------------------------------------------------------- |
| 47      | Basics of Pituitary Gland          | 936–940 | 5   | 61        | 10 / 11 / 8 / 9 / 6 / 15 / 2 / 0                                  |
| 48      | Prolactin                          | 941–944 | 4   | 52        | 6 / 7 / 6 / 6 / 7 / 10 / 7 / 3                                    |
| 49      | Growth Hormone                     | 945–951 | 7   | 84        | 12 / 16 / 9 / 11 / 9 / 20 / 5 / 2                                 |
| 50      | Acquired Hypopituitarism           | 952–957 | 6   | 72        | 10 / 11 / 8 / 10 / 10 / 15 / 4 / 4                                |
| 51      | Antidiuretic Hormone               | 958–961 | 4   | 48        | 7 / 10 / 5 / 5 / 5 / 10 / 6 / 0                                   |

## Pipeline

1. **Source render.** All 26 pages rendered at zoom 2.5 (`_render/_936.png`–`_961.png`) from `uploads/Medicine_Vol3_Part4_pages_894-964.pdf` (K = 893).
2. **Visual read-through.** Every page read end-to-end; diagrams, tables, handwritten margins, anatomical relations, flowcharts, doses, and clinical vignettes inspected visually across all pages.
3. **Authoring.** Each page → `data/parts/cNN/p<page>a.json` (one part per page, in strict book order). Units in `data/units/cNN.json` follow concept-based titles (one unit per page) ensuring the learning path mirrors the book's narrative structure.
4. **Assembly.** `python author.py 47...51` rebuilds `data/chNN.json` with deterministic SHA-256 answer rotation; gates four distinct options, no length giveaway (>3× longest distractor), no banned filler, mandatory `(Book pNN)` citation, valid format token.
5. **Embed.** `python build_content.py` writes the inline `QUESTIONS`/`UNITS`/`CHAPTERS` arrays in `pulse-medicine.html`.
6. **Gates.** `python check_integrity.py` and `node check_app_smoke.js` both pass (verified extraction: **3,850 questions / 322 units / 74 chapters / 53 live**).
7. **Variety audit.** `python audit_variety.py` — every new chapter mixes fill-ups, match, true/false, scenario and odd-one-out; answer-position spread is balanced by the SHA-256 rotation; 0.0% filler distractors, 0.0% answer-term leaks, and longest-option answer rates well below the 25% random guess line.

## Coverage check — every page asked

| Book page | Topic anchor                                                                    | Sample ID    |
| --------- | ------------------------------------------------------------------------------- | ------------ |
| p936      | Master gland, oral ectoderm Rathke's pouch vs 3rd ventricle, Prop-1, Sheehan    | MED-C47-001  |
| p937      | Cell percentages, twin hormones (GH/PRL), POMC cleavage, DOSE happiness notes   | MED-C47-013  |
| p938      | Superior vs inferior hypophyseal artery, portal vs magnocellular, Ca breast mets| MED-C47-026  |
| p939      | Sphenoid sinus approach, CN VI in cavernous sinus, T1 isointensity, bright spot | MED-C47-038  |
| p940      | Macroadenoma vs microadenoma, non-functioning vs functioning, stalk/mass effect | MED-C47-050  |
| p941      | Adenoma frequencies, 199 AA prolactin, micro vs macroprolactin, dopamine PRIF   | MED-C48-001  |
| p942      | Fasting levels (<25, 25-40, 40-100, >200), Hook effect, D2 blockers, <72h rule | MED-C48-014  |
| p943      | F:M 20:1, MEON syndromes, amenorrhea-galactorrhea, spinal osteopenia, post-MRI | MED-C48-027  |
| p944      | Asymptomatic watch, cabergoline DOC, bromocriptine in pregnancy, surgical rules | MED-C48-040  |
| p945      | Somatotrophs 50%, 191 AA, NREM 3/4 surge, IGFBP-3 integration, obesity growth   | MED-C49-001  |
| p946      | GH vs IGF-1 carbohydrate/lipids, BEAMS mnemonic, wonder molecule, IGF-2 MSA     | MED-C49-013  |
| p947      | Laron dwarf GHR mutation, ITT gold standard, 98% pituitary, bronchial carcinoid | MED-C49-025  |
| p948      | GH adenoma vs prolactinoma table, histopathology granulation, acral/brain, face | MED-C49-037  |
| p949      | Carpal tunnel, type 1/2 myopathy, HFpEF, DOSA mnemonic, McCune-Albright triad  | MED-C49-049  |
| p950      | Craniopharyngioma adamantinomatous vs papillary, claw sign, OGST cutoffs        | MED-C49-061  |
| p951      | Brain lesion signs table, transsphenoidal cure rates, SRLs, pegvisomant paradox | MED-C49-073  |
| p952      | Ranked hypopituitarism causes (stalk, Sheehan, viper bite), TSH vs ACTH roles  | MED-C50-001  |
| p953      | Adult GH deficit, unmasking of DI by glucocorticoids, acute apoplexy headache   | MED-C50-013  |
| p954      | 100 mg IV hydrocortisone, decompressive surgery, Sheehan PPH pathophysiology   | MED-C50-025  |
| p955      | Early agalactia, 3-4 month presentation, facial wrinkling, IgG4 hypophysitis    | MED-C50-037  |
| p956      | Primary (BIH) vs secondary empty sella, basal direct hormones, metyrapone test  | MED-C50-049  |
| p957      | 10-5-5 hydrocortisone, infection stress dosing, steroid ratios, Nelson syndrome | MED-C50-061  |
| p958      | Serum osmolality formula (285-290), effective vs ineffective osmoles, 1.6 rule  | MED-C51-001  |
| p959      | Severity tiers (130-135, 120-129, 100-119 hiccups, <100 ICT), ADH/thirst curve | MED-C51-013  |
| p960      | V1/V3 IP3-DAG vs V2 cAMP, tissue actions, countercurrent 4x multiplier, vasa    | MED-C51-025  |
| p961      | V2 PKA AQP2 exocytosis, basolateral AQP3/4, obligatory vs facultative water    | MED-C51-037  |

## Variety and predictability metrics

The audit verifies outstanding question diversity and anti-predictability across all new chapters:

| Chapter | Questions | Filler distractors | Answer-term leak | Longest-option answer | Reused option sets |
| ------: | --------: | -----------------: | ---------------: | --------------------: | -----------------: |
| 47      | 61        | 0.0%               | 0.0%             | 13.1%                 | 14                 |
| 48      | 52        | 0.0%               | 0.0%             | 13.5%                 | 8                  |
| 49      | 84        | 0.0%               | 0.0%             | 19.0%                 | 21                 |
| 50      | 72        | 0.0%               | 0.0%             | 20.8%                 | 16                 |
| 51      | 48        | 0.0%               | 0.0%             | 14.6%                 | 11                 |

- **Filler distractors:** 0.0% across all 5 chapters (no "all of the above", "none of the above", etc.).
- **Answer-term leaks:** 0.0% across all 5 chapters (no stem-word giveaway).
- **Longest option as answer:** Averaging ~16.2% across the five chapters, well below the 25% random distribution rate.
- **Answer position balance:** Deterministic SHA-256 rotation distributes correct keys evenly across options A, B, C, and D.
- **Formatting mix:** Every unit incorporates multiple rich formats (clinical scenarios, matching boards, fill-in-the-blanks with `___`, true/false paired assertions, odd-one-out discrimination, numeric thresholds, and management decisions).

## Source-nuance and contradiction flags (taught explicitly)

1. **p944 Cabergoline maximum dose note.** The book annotation notes `> 2g/week: Tricuspid regurgitation, lung fibrosis` (standard clinical pharmacology doses cabergoline in milligrams, e.g. 2–3 mg/week; the scan notes "2g/week"). The question notes the cardiopulmonary valvulopathy risk while explaining standard mg dosing.
2. **p946 Somatomedin-C vs Somatostatin-C.** The table on p946 writes "Somatostatin - c" under the other name for IGF-1. Physiologically, IGF-1 is somatomedin C (somatostatin is growth hormone-inhibiting hormone). Questions teach the physiological reality while noting the source text naming.
3. **p955 Sheehan polarity box typographical inversion.** The scan's comparison box states:
   *Pituitary apoplexy: Hypopituitarism + Hyperprolactinemia*
   *Sheehan's syndrome: Hyperpituitarism + Hypoprolactinemia*
   Sheehan syndrome causes ischemic necrosis leading to panhypopituitarism (not hyperpituitarism). The items test the true physiological presentation (hypopituitarism with hypoprolactinemia) and highlight the book's typographical error.
4. **p957 Gonadotropin replacement gender transposition.** Under non-fertility replacement, the handwritten diagram lists `Female: Testosterone (Depot/Patch/Gel)` and `Male: Estrogen`. Questions teach the physiological hormonal replacement (testosterone for hypogonadal males and estrogen/progesterone for hypogonadal females) while alerting learners to the text transposition.

## Final verification

```
$ python3 check_integrity.py
Verified extraction: 3850 questions, 322 units, 74 chapters.
PASS: 53 live chapter(s) of 74; 3850 questions; 322 units; all 266 in-scope Book pages represented;
IDs, four-option structure, citations, order, source artifacts, UI hooks, and JavaScript syntax verified.

$ node check_app_smoke.js
PASS: 634 new-question answer paths across 26 units; matching boards, blanks, feedback, locking and completion verified.
PASS: roadmap of 74 chapters (53 live, rest "Soon"), Chapter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 60, 61 path data and quiz starts, and final question IDs resolve at runtime.
```

**Live preview:** Standalone single-page web app in `pulse-medicine.html` (and GitHub Pages upon merge to `main`).
