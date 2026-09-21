# Chapter 5 — source-order repair, 2026-09-21

## Scope and result

**Glomerulus - Anatomy, Book p730–733 / Part 1 PDF pages 38–41.**
All four source pages were read from the scan (whole-page renders at 2x plus
8x–20x glyph-level checks of every printed number and ambiguous token) and
reconciled to the bank.
**56 → 88 questions; the same 8 unit IDs retained.**
Status: **reviewed with explicit source caveats**, not independent medical
validation.

The ordered checklist is `data/source_review/ch05.json`. It records every
reviewed instructional element, its question ID, printed page, PDF page, and
figure/table reading traversal. Contiguous labels share an item; consolidation
items sit after the lines they test and never pull later material forward.
Headers, lecture timestamps, publisher footers and blank "Active space" are
excluded.

| Book page | PDF page | Questions | Source blocks |
|---|---:|---:|---|
| 730 | 38 | 19 | Fenestration-slits bullets, PSGN disease line + 4 findings, CKD chain (both end branches), size/charge passage tree, all 9 glomerular-capillary figure labels + caption |
| 731 | 39 | 26 | GBM constituent, type-4 configuration table, Alport defect note + both table rows, heparin sulfate charge, visualisation tree (both branches), thickness tree, mesangial note (both contraction branches), LM-image legend/labels/caption, all JGA-figure labels + caption |
| 732 | 40 | 25 | Slit definition, 5 podocyte bullets + proteins tree, nephrin roles, all 12 figure-(a) labels, all figure-(b) labels, 13-name legend + consolidation + shared caption, 10-step angiotensin chain, ARBs/ACEI Rx line |
| 733 | 41 | 18 | DMS line, congenital-NS table row by row (all 18 data cells), 2 cross-row consolidations, premature/large-placenta line, Denys Drash note, site-disease table column by column + 2 consolidations |

Rebuild script: `author_c5_review.py` (one-shot, guarded against re-running on
the rebuilt bank). Manifest writer: `write_ch05_manifest.py`. Match-key
relabel: `diversify_ch5.py` (same algorithm as `diversify_keys.py`), plus a
final distractor-set de-duplication (9 distractor swaps inside the match key
space) recorded here because it is applied to the built bank.

## Repairs

- **Within-page order fault (p730).** The PSGN expansion ("Post Streptococcal
  Glomerulo Nephritis", printed on the disease line) sat after items testing the
  sub-bullets; it now precedes them (new MED-C5-004).
- **Within-page order fault (p733 table).** The old cross-row defect/age match
  (old MED-C5-046) sat before items re-testing row-1 outcome and rows 2–3, and
  the old table true/false (old MED-C5-051) carried row-1 histology/management
  as its answer while sitting after rows 2–3. The table is now tested in strict
  row order (Finnish row complete, podocin row complete, AD row complete), with
  both cross-row consolidations after every row. Histology/management cells and
  the inheritance cells now have their own items.
- **Consolidation placed before its lines (p732).** The old whole-chain match
  (old MED-C5-041) sat mid-chain while later items re-tested later steps; the
  chain steps 4–6 (podocyte detached → podocyturia → podocytopenia) had no item
  of their own. They now do (a clinical scenario at their printed position) and
  the whole-chain match is the last chain item.
- **Silent correction removed (p732).** The podocyte protein tree prints
  "Inside : α actin 4"; the old item taught "α actinin 4" without comment. It
  now teaches the print verbatim and flags the standard nomenclature.
- **Uncovered source lines given questions.** Size rule "< 4 mm : passes
  through"; the GBM visualisation branch "1. Electron m/s (microscope)"; the
  slit "Function : Filtration."; the light-microscope image legend
  (PT = proximal tubule / CL = capillary lumen); both figure captions on p731;
  all 9 labels of the p730 glomerular-capillary figure + its caption (the old
  bank probed them only through one odd-one-out); all 10 JGA-figure labels
  (the old bank probed only the two bracket synonyms) + its caption; all 12
  figure-(a) labels on p732 (completely untested); figure-(b) labels F-actin,
  slit diaphragm, podocyte foot process, β/α dystroglycan, the agrin pair, GEC
  and the GBM base label; the 13-name protein legend (column by column) + its
  odd-one-out consolidation + the shared caption; the Finnish-type row-1
  defect/age/histology/management cells and the row-2/row-3 inheritance cells.
- **Answer incompleteness fixed (p730).** The CKD-chain sequence item's answer
  option omitted the printed "↑ capillary pore diameter" step; the full printed
  chain is now the answer, with the pore step also held by its own fill-up.
- **Option-set predictability reduced.** Match key lists were relabelled with
  per-ID seeded permutations and 9 distractors swapped within the key space;
  Ch 5 option-set reuse is 3 (was 15 as first rebuilt).

## Source caveats retained in the manifest and explanations

- p730: the size/charge rules print **"mm"** for all four values ("< 4 mm",
  "> 8-10mm", "4-8 mm", "7.6 mm") where nanometres are meant — the fenestration
  sizes on the same page correctly print "nm". Values are taught as printed and
  the unit error is flagged in every affected explanation, not silently fixed.
- p730: the figure label prints **"Podocyte 7"** — the trailing 7 sits just
  before the leader line and is unexplained; taught as "Podocyte" with the glyph
  flagged. "Post Streptococcal Glomerulo Nephritis" prints as three words;
  "No risk for CKD." is an absolute source claim taught as printed.
- p731: the Alport table header prints **"Immunoflorescence"** (one u) and the
  10–15% defect cell prints the nonstandard **"α₃+/ α₄"**. "Heparin sulfate
  proteoglycans" is the print (standard: heparan sulfate). The visualisation
  tree mixes numbering (**"1."** then **"a."**) and "masson's Trichrome" prints
  lowercase.
- p732: "Space btw **2** podocytes" uses a script 2 (background OCR read "a";
  confirmed as 2 at 16x zoom — recorded, not guessed). The protein tree prints
  **"Inside : α actin 4"** (standard: α-actinin-4). Figure (b) prints
  **"Laminin-11"** (nonstandard laminin nomenclature) and misspells agrin as
  **"Argin"** on the right label while the left reads "Agrin". Legend names
  print "NEPH1" and "Fat-1". The Rx line prints "ARBs /ACEI(–)'s … to block
  Angiotensin II Receptor", compressing both drug classes into receptor
  blockade (ACE inhibitors reduce angiotensin II formation) — taught as printed
  with the flag.
- p733: histology cells print the equivalence sign (**"≡ DMS" / "≡ FSGS"**),
  NPHS1 carries a subscript 1 and TRPC6 a subscript 6. The site-disease table
  prints **"mCD"** with a lowercase m and lists "membranous" as a bare
  adjective. **"Denys Drash Syndrome"** prints without a hyphen. The
  Finnish-type management cell is a bare dash.

## Progress compatibility

All eight `MED-U5-*` IDs and their source scopes remain. The app persists XP,
completion IDs, unlock preference and streak—not per-question IDs—so renumbering
the expanded question bank does not migrate an old answer onto a different
persistent question record. No localStorage key is cleared. Unit guides disclose
the revision and recommend replay; retained completion badges describe past
attempts, not completion of all newly added questions.

## Verification and limits

- `build_content.py` → `check_integrity.py` PASS (5,361 questions, 412 units,
  all 364 in-scope pages; source-review evidence 5/74).
- `node check_app_smoke.js` PASS — 10,722 correct/incorrect answer paths across
  all 412 units — with zero Ch 5 items among the 44 legacy format warnings
  (they remain in unreviewed Ch 26/29/60/61).
- `python3 -m unittest test_source_coverage.py` 17/17 PASS (the
  reviewed-chapters test now also validates the Ch 4 and Ch 5 manifests).
- Variety (AUDIT.md, Ch 5 row): 88 questions — 2 scenario, 16 fill-up,
  24 match, 7 true/false, 7 odd-one-out (plus recall/numeric/management);
  longest-option rate **20.5%** (below chance), answer-leak **0.0%**,
  option-set reuse **3**. All eight formats are present at chapter level; every
  unit has a real mix with ≥1 non-recall item. Local source coverage first — no
  format was forced across separated lines.
- `check_source_coverage.py --require-all` still fails **by design** (69
  chapters pending, next Ch 6). This merge is an incremental review, not
  whole-book compliance.
- `check_source_coverage.py` validates the checklist, source PDF hash, content
  hash, page map and unit traversal. It does **not** read the scan or prove
  medical truth; visual review remains a separate authoring duty.

Next sequential work is Ch 6 (Renal Physiology, p734–739); see the current
`SOURCE_REVIEW.md` tracker.
