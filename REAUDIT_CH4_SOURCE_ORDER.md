# Chapter 4 — source-order repair, 2026-09-21

## Scope and result

**Juxtaglomerular Apparatus, Book p726–729 / Part 1 PDF pages 34–37.**
All four source pages were read from the scan (whole-page OCR plus 2x–5x
zoomed renders for handwriting and figure labels) and reconciled to the bank.
**50 → 55 questions; the same 7 unit IDs retained.**
Status: **reviewed with explicit source caveats**, not independent medical validation.

The ordered checklist is `data/source_review/ch04.json`. It records every
reviewed instructional element, its question ID, printed page, PDF page, and
diagram/table reading traversal. Contiguous labels share an item; consolidation
items sit after the lines they test and never pull later material forward.
Headers, lecture timestamps, publisher footers and blank “Active space” are excluded.

| Book page | PDF page | Questions | Source blocks |
|---|---:|---:|---|
| 726 | 34 | 16 | Components, macula densa text, JG-apparatus figure labels, table rows 1–2 (left cells + row-2 MOA head) |
| 727 | 35 | 13 | Table row 2 continued (Mx/MOA) + recovery row, dehydration chain, AKI-causes note, JG cells |
| 728 | 36 | 19 | Renin-stimulator diagram, renal-circulation chain, cortex/medulla table, vascularity-figure labels |
| 729 | 37 | 7 | Renal-diseases tree (tubulointerstitial 85% arm, then vascular 5% arm) |

Rebuild script: `author_c4_review.py` (one-shot, guarded against re-running on
the rebuilt bank). Manifest writer: `write_ch04_manifest.py`.

## Repairs

- **Findings cited on the wrong page.** The TG-feedback findings (↓GFR,
  ↑S.creatinine, ↑K+ → arrhythmias, ↑H+ → acidosis) print on **p726**, but the
  old bank tested them from p727. Coverage moved to p726 (new MED-C4-013), ahead
  of the row-2 MOA items, and the H+ → metabolic acidosis line gained its own
  item (new MED-C4-014).
- **Forward jump removed.** The old p726 match taught JG-cell composition/site
  (“granular cells of the tunica media”), which print on **p727**. It is now a
  p726-only composition/site/function match (new MED-C4-005).
- **Double-answer defect fixed.** Old MED-C4-022 (“inside kidney causes EXCEPT”)
  had two correct options — pre-renal AND post-renal causes both arise outside
  the kidney. Re-authored as a true/false item on the cause groups (new MED-C4-025).
- **Within-page order fixed.** The cortex/medulla perfusion item sat after the
  vascularity-figure questions; it now precedes them (new MED-C4-043), matching
  the printed table-then-figure order.
- **Figure labels completed.** The old bank tested only the efferent arteriole
  (p726) and a 3-label subset (p728). Every printed label is now directly
  questioned: internal elastic lamina, glomerular epithelium, basement
  membrane, distal tubule (straight), macula densa plaque and JG cells (p726);
  afferent arteriole, PCT, glomerular capsule, interlobular artery/vein,
  venule, loop of the nephron and peritubular network (p728).
- Smaller fidelity tweaks: the gentamicin item is now a clinical scenario; the
  ATN/AIN match stem carries the printed “hours to days” AKI timeframe; the
  TG-feedback MOA stem names the printed GFR expansion; one verbatim-reused
  match option set was diversified (Ch 4 reuse 1 → 0).

## Source caveats retained in the manifest and explanations

- p726: the scan prints **“Cardiac arrythmias”** and **“afferent arteriole”**;
  the bank uses standard “arrhythmias”/“afferent”. “Tubulo glomerular” is
  printed as two words.
- p727: the dehydration chain is taught as printed — increased proximal tubular
  absorption (+) feeds a macula densa signal of *decreased* Na+/Cl-/K+ load.
  The “ATI/ATN” slash and the edema rationale for fluid monitoring are source
  wordings. “Afferent > efferent” is the printed JG-cell predominance.
- p728: “renal artery (**end artery**)” and “5 segmental (**4 anterior +
  1 posterior**)” are source simplifications taught as printed. The
  efferent-arteriole “sandwiched” note is schematic. “Urine flows into renal
  papilla” is taught as printed (the minor calyx is not labelled).
- p729: the tree arms sum to **90%** (85% tubulointerstitial + 5% vascular);
  glomeruli (10% per the p717 compartment tree) have no arm here — taught as
  printed, not completed. The “1. AKI”/“2. CKD” numbering, the m/c cause claims
  and RTA type 4 as the CKD tubulointerstitial endpoint are source-specific.

## Progress compatibility

All seven `MED-U4-*` IDs and their source scopes remain. The app persists XP,
completion IDs, unlock preference and streak—not per-question IDs—so renumbering
the expanded question bank does not migrate an old answer onto a different
persistent question record. No localStorage key is cleared. Unit guides disclose
the revision and recommend replay; retained completion badges describe past
attempts, not completion of all newly added questions.

## Verification and limits

- `build_content.py` → `check_integrity.py` PASS (5,329 questions, 412 units,
  all 364 in-scope pages; source-review evidence 4/74).
- `node check_app_smoke.js` PASS with zero Ch 4 items among the legacy format
  warnings; `python3 -m unittest test_source_coverage.py` 17/17 PASS.
- Variety: Ch 4 longest-option rate **27.3%** (≈ chance), answer-leak **0.0%**,
  zero reused option sets, zero fillers. All eight formats are present at
  chapter level; per-unit mixes follow the Ch 1–3 precedent (local source
  coverage first, no forced cross-line formats).
- `check_source_coverage.py --require-all` still fails **by design** (70
  chapters pending, next Ch 5). This merge is an incremental review, not
  whole-book compliance.
- `check_source_coverage.py` validates the checklist, source PDF hash, content
  hash, page map and unit traversal. It does **not** read the scan or prove
  medical truth; visual review remains a separate authoring duty.

Next sequential work is Ch 5 (Glomerulus – Anatomy, p730–733); see the current
`SOURCE_REVIEW.md` tracker.
