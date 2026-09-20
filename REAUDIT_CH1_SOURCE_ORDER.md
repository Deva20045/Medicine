# Chapter 1 — source-order repair, 2026-09-20

## Scope and result

**Development of Kidneys, Book p705–710 / Part 1 PDF pages 13–18.**
All six source pages were visually read and reconciled to the new bank.
**68 → 140 questions; the same 9 unit IDs retained.**
Status: **reviewed with explicit source caveats**, not independent medical validation.

The ordered checklist is `data/source_review/ch01.json`. It records every reviewed
instructional element, its question ID, printed page, PDF page, and diagram/column
reading traversal. Some elements contain a contiguous set of related labels;
headers, lecture timestamps, publisher footers and blank “Active space” are excluded.
Numbered clinical photographs are covered by their printed labels/captions;
this is not a claim that the app now provides image-recognition testing of every
unlabelled photographic detail.

| Book page | PDF page | Questions | Source blocks |
|---|---:|---:|---|
| 705 | 13 | 24 | Mesoderm tree, serosal layers, urogenital-development line, anal-pit note, complete cloacal tree |
| 706 | 14 | 24 | Intermediate-mesoderm branches, ridge bullets, remnants, first three timeline rows |
| 707 | 15 | 28 | Remaining timeline rows, every labelled CKD-flow transition and equation |
| 708 | 16 | 21 | CKD features, maternal cascade and risk list, PAX-2, levels, four WAGR captions |
| 709 | 17 | 25 | Denys–Drash, Frasier, WT2/imprinting, BWS images/list, Russell Silver |
| 710 | 18 | 18 | Unilateral agenesis and associations, montage caption, bilateral/Potter text and numbered captions |

## Repairs

- Female vesicourethral-canal contribution is now **MED-C1-017**, immediately
  after the male contribution (**016**) and before the definitive-sinus branch.
  The old backward jump to MED-C1-015 is gone; old IDs in the initial audit refer
  to the pre-repair bank.
- Replaced composite questions that pulled later branches forward with local,
  source-positioned questions. The GFR equation is now tested at its printed
  position, before continuing down the hyperfiltration cascade.
- Separately test the ridge relationships, timeline events, intermediate flow
  steps, maternal-risk labels, syndrome features and renal-agenesis associations
  that were previously compressed into explanations or grouped out of order.
- Source changes are recorded, not silently replaced by general medical recall.

## Source caveats retained in question explanations

- p706: “no role in humans” for mesonephros and the amphibians/reptiles parenthesis
  are qualified as source overgeneralisations, not universal developmental rules.
- p707: the proteinuria parenthesis prints **Albuminemia**; distinguish blood
  terminology from **albuminuria** rather than silently changing the scan.
- p708–709: historical disability/sex-development wording is identified and
  preferred terminology supplied. Frasier’s “normal external genitalia” is not
  treated as a universal rule.
- p709: WT2 is a historical source label; BWS “microcephaly” is flagged as
  questionable; intellectual disability is not made a universal Russell Silver
  diagnostic requirement.
- p710: the book’s sex ratio/incidence are labelled source-specific. Its broad
  “most common cause of death immediately after birth” claim is not taught as
  an established universal mortality statistic.
- p710: **pulmonary hyperplasia** is actually printed. The explanation explicitly
  flags this apparent error and identifies **pulmonary hypoplasia** as the clinical
  problem in Potter sequence. The standard GDNF expansion is distinguished from
  the scan’s abbreviated expansion.

## Progress compatibility

All nine `MED-U1-*` IDs and their broad source scopes remain. The app persists XP,
completion IDs, unlock preference and streak—not per-question IDs—so renumbering
the expanded question bank does not migrate an old answer onto a different
persistent question record. No localStorage key is cleared. Unit guides disclose
the revision and recommend replay; retained completion badges describe past
attempts, not completion of all newly added questions.

## Verification and limits

- Existing build/integrity checks pass with the new counts.
- Every revised item is included in the expanded full-bank runtime smoke test,
  with both correct and incorrect answers and exact authored playback order.
- `check_source_coverage.py` validates this checklist, source PDF hash, content
  hash, page map and unit traversal. It does **not** read the scan or prove medical
  truth; visual review remains a separate authoring duty.
- Current variety heuristics: longest-option answer **17.9%**, detected answer-term
  leakage **0.0%**, no filler distractors. One repeated-stem-template run remains;
  adjacent similar structures are intentionally not moved out of source order to
  improve a cosmetic metric. Five formats are present; the revision prioritises
  local source coverage over forcing a matching question across separated lines.

Next sequential work after this chapter was Ch 2; see
`REAUDIT_CH2_SOURCE_ORDER.md` and the current `SOURCE_REVIEW.md` tracker.
