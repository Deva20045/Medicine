# Chapter 3 — source-order repair, 2026-09-20

## Scope and result

**Tubular Anatomy, Book p717–725 / Part 1 PDF pages 25–33.**
All nine pages were visually read at 2× from the supplied PDF.
**100 → 202 questions; all 13 existing unit IDs retained.**
Status: **reviewed with explicit source caveats**.

The ordered source-block checklist, reading traversals, PDF hash and content hash
are in `data/source_review/ch03.json`. This is a recorded source review, not an
independent medical validation. It does not certify any later chapter.

| Book page | PDF page | Questions | Reviewed source blocks |
|---|---:|---:|---|
| 717 | 25 | 22 | Compartment proportions; full embryology list; nephron regions, stripes/ray/loops; origin and numbered excretory branches |
| 718 | 26 | 18 | Collecting legend and origin; every nephron-type table row; complete renal-failure teaching tree |
| 719 | 27 | 18 | PCT transporter branches; phosphate cascade; membrane labels, solutes and bicarbonate-recovery arrows; final Mg note |
| 720 | 28 | 27 | Every inherited/acquired cause; drug exception; cardinal features with sub-bullets/cascades; both other-feature columns |
| 721 | 29 | 27 | CCD cell types; P-cell signalling/transport labels; Conn triad; every true/pseudo-hypoaldosteronism branch |
| 722 | 30 | 25 | Renin note; alpha/beta-cell diagrams; inherited/acquired distal RTA; clinical subbranches; type-III note |
| 723 | 31 | 23 | Each distal/proximal comparison row; unnamed-cell lines; both urine-gap equations, sign branches and ammonium diagram |
| 724 | 32 | 22 | TALH diagram; Bartter cascade and each consequence; type I–V branches; treatment arrows |
| 725 | 33 | 20 | DCT diagram; Gitelman bullets/cascades; calcium note; every Bartter/Gitelman comparison row |

Contiguous source labels/causal chains sometimes share a question. They are kept
within their original local block, not pulled across intervening material.
Nephron numeric labels are read with their printed legend spanning p717–718.
Decorative page headers, footer, timestamps and empty Active space are excluded.

## Ordering and coverage repairs

- Kept the embryology sub-bullets together, followed by the adjacent figure and
  numbered excretory/collecting legends. Added cortical/medullary regions,
  outer/inner stripes, medullary ray and long/short-loop labels.
- Read the p718 renal-failure tree depth-first, explicitly recording traversal
  instead of switching between branches by topic.
- Finished PCT symports and antiport before the passive branch; completed the
  carbonic-anhydrase cycle before the final magnesium note. The old bank moved
  the final magnesium note ahead of the bicarbonate-exit detail.
- Finished inherited Fanconi causes before acquired causes rather than pulling
  separated age-specific facts into an early composite match. Added galactosemia,
  all listed drugs, acidification sub-bullets and both other-feature columns.
- Expanded hypoaldosteronism to include diabetic submechanisms, reflux/obstruction,
  calcineurin inhibitors, pentamidine, and the full ordered drug lists.
- Finished inherited and acquired distal-RTA causes before manifestations and the
  type-III note. Added the full bone-calcium/stone/nephrocalcinosis/rickets and
  salt-loss cascades.
- Replaced sparse cross-row matching with every comparison-table row in its
  printed position, including both bicarbonate-dose cells.
- Finished all Bartter type branches before treatment. Gitelman comparison rows
  remain after the prose, not interleaved with earlier physiology.

## Source contradictions and clinical caveats

The source is not treated as medically infallible. Important issues are explicit
in the question explanations and manifest, including:

- **p717:** bladder versus primitive-rectum parenthesis; cephalic versus phallic
  wording; vesico-ureteric versus vesicourethral terminology.
- **p719:** kidney-only phosphate handling and all-ions wording; the upper
  basolateral Na/H sketch conflicts with canonical physiology and the lower sketch.
- **p720:** generalised Fanconi versus isolated proximal RTA; the unsafe universal
  **“no CKD risk”** claim; source-specific urine-pH/bicarbonate descriptions.
- **p721:** ENaC does not exchange H/K or conduct water; ROMK is not a proton pump;
  SOMK is a nonstandard printed label and receives no invented expansion.
- **p722:** simplified beta-cell basolateral diagram; toluene is an exposure;
  **osteoporosis** in the CA-II-deficiency note conflicts with classic
  **osteopetrosis**. Outdated disability terminology is not repeated as preferred usage.
- **p723:** AR/M>F common-features generalisation conflicts with prior AD/acquired
  branches; severity and solute patterns are simplified; countercurrent exchange
  is primarily vasa recta function; urine gap is an imperfect ammonium surrogate.
  Alkali doses are source teaching ranges, not an individual prescription.
- **p724:** the pump's **3 K** label conflicts with normal **3 Na/2 K** stoichiometry;
  the TALH **water** arrow conflicts with water impermeability; magnesium wording,
  percentages and older type-V classification are source-qualified.
- **p725:** an obligatory separate **TRMP6/ileal** defect and **100%** low Mg are not
  imposed as diagnostic requirements; **“no hypocalciuria”** conflicts with typical
  Gitelman physiology and the later table; **“salt water retention”** contradicts
  salt wasting; the final Gitelman **“low”** magnesium cell is ambiguous.

No guessed replacement values or fabricated source citations were used to hide
these contradictions. The explanations distinguish source recall from corrections.

## Progress compatibility

All 13 `MED-U3-*` IDs and broad unit scopes are preserved. The app stores XP,
streak, completed unit IDs and unlock preference, not per-question answer history.
No localStorage keys are cleared. Guides disclose the revision and recommend
replay: a preserved completion badge records an earlier attempt, not completion
of every newly added question.

## Verification

- `python3 build_content.py` and `python3 check_integrity.py`: PASS with
  **4,444 questions / 346 units / 58 live chapters** in the whole bank.
- `python3 -m unittest -v test_source_coverage.py`: **17 tests PASS**, including
  manifest validation for Chapters 1–3 and mutation tests for stale/missing/
  reordered evidence.
- `node check_app_smoke.js`: **8,888 correct/incorrect answer paths** across all
  live units, exact authored question order and saved-history checks PASS.
  **44 legacy format warnings remain** in unreviewed chapters; no revised Ch 3
  item uses a malformed match/fill-up fallback.
- Chapter 3 variety report: six formats; longest-option answer **25.2%**;
  zero filler distractors; no repeated-template run. Eleven option-set reuses
  remain, largely local comparisons/numeric choices. One heuristic answer-term
  flag is the explicit inherited/acquired comparison-sign question, not a reason
  to reorder the source. These heuristics do not establish source completeness.
- `python3 check_source_coverage.py --require-all`: **expected FAIL** because
  **71 chapters remain**. No gate was bypassed or pending manifest fabricated.

## Merge scope and next step

This is an incremental all-chapter continuation, **not completion of all 74
chapters**. Together with the existing Ch 1–2 repairs, the current recorded
source-review scope is **Ch 1–3, p705–725: 3/74 chapters, 21/364 pages**.

**Next in strict order: Ch 4 — Juxtaglomerular Apparatus, Book p726–729.**
Continue the same source-reading/checklist/repair/check workflow. Ch 57–59 and
62–74 are unbuilt.

### Merge reconciliation

While merging, `main` had advanced through PR #18, replacing the earlier 81-item
Ch 52–56 bank with **338 questions / 24 units**. Preserved that entire newer bank,
its authoring parts and its report; retained our all-bank tests and rebuilt the
embedded app from the combined JSON sources. The totals/checks above are for the
combined result. No new source-review manifest was fabricated for Ch 52–56.
Historical Ch 54 failures refer to the replaced version, so the new version needs
fresh review when reached; old question IDs do not identify the same questions.
