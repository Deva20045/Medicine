# Chapter 2 — source-order repair, 2026-09-20

## Scope and result

**Gross Anatomy of Kidney, Book p711–716 / Part 1 PDF pages 19–24.**
All six pages were visually read at 2×; the p711 level line and p712 anatomical
labels were additionally checked at 4×.
**66 → 148 questions; the same 11 unit IDs retained.**
Status: **reviewed with explicit source caveats**.

The ordered source-element checklist, PDF/content hashes and per-page reading
traversals are in `data/source_review/ch02.json`.

| Book page | PDF page | Questions | Source blocks |
|---|---:|---:|---|
| 711 | 19 | 32 | Levels, artery sequence, venous bullets, gross-anatomy labels, transplant line/table/locations |
| 712 | 20 | 33 | Posterior-relation labels, applied anatomy, calyces/pyramid, sectional-anatomy labels, medulla/papilla cascade |
| 713 | 21 | 25 | Both UTI branches, each symptom and regimen, investigation exclusions and treatment/imaging pathway |
| 714 | 22 | 16 | CT descriptors/captions, normal-papilla and nephrocalcinosis comparisons, necrosis definition/causes/prognosis/images |
| 715 | 23 | 23 | Papillary-type diagram and notes, abscess, childhood investigation branches and nuclear-scan panels |
| 716 | 24 | 19 | VUR grade labels/markers/comparator, asymmetry causes, both papillary diagrams and complete bullet lists |

## Repairs and recovered material

- Corrected the fetal level from **S1–S3 to S1–S2**, confirmed directly at 4×.
- Put the right-renal-artery length sub-bullet **before** the gonadal-artery bullet,
  matching its source position.
- Expanded figure-label coverage beyond the old two cut structures. Consecutive
  labels share matching items only within the documented local traversal. Match
  keys vary; they are not all `1-A, 2-B, 3-C`.
- Distinguished the **left 11th/12th rib** relations from the **right 12th rib**.
- Tested major and minor calyx counts separately, and included previously omitted
  labelled vessels, capsule, columns, pelvis and ureter.
- Completed the **left complicated-UTI branch first**, then the right uncomplicated
  branch, each symptom and regimen, before the investigation protocol.
- Added the cefoperazone–sulbactam source line, each ultrasound exclusion, both CT
  contrast qualifiers, both parts of the infundibulum/ureter thickening line, and
  the normal-papilla/nephrocalcinosis comparison captions.
- Followed the papillary-necrosis diagram through its branch labels and convergence
  before the adjacent C/E appearance notes. Covered childhood CAKUT examples,
  full test names, both targets, and normal/abnormal DMSA panels.
- Completed the composite-papilla branch before the simple-conical branch instead
  of revisiting pole distribution after later figure details.

## Important source caveats

- Transplant anastomosis preference, right iliac graft position, retained native
  kidneys and surgical approaches are **book descriptions**, not universal rules.
- The p712 sectional figure prints “interlobular artery” at a deeper right-side
  callout as well as the cortical left-side callout. The apparent labelling issue
  is recorded, not converted into an invented authoritative arterial sequence.
- The cotrimoxazole line prints **“200 mg mg BD × 3–5 days”**, without component
  strengths. The question identifies why this is not a complete safe prescription;
  **no corrected dose is guessed**.
- Other antibiotic doses are explicitly source-recall items. Formulation, renal
  function, dialysis, patient context and local guidance still govern prescribing.
  The book’s generic renal-failure schedule must not be applied to every patient.
- A normal ultrasound alone does not establish or exclude pyelonephritis. The
  childhood pathway is source-specific and does not justify delaying urgent imaging.
- “Poor prognosis” is not an invariant outcome for every treated patient.
- The final page prints **reflex** where the VUR/papillary context requires
  **reflux**; both occurrences are flagged.

## Honest figure-review limits

Printed labels, captions, named structures and visible comparator relationships
are covered. This does not claim that every unlabelled CT arrow is a separately
validated radiological diagnosis or that the app contains image-recognition
questions for every source photograph. The VUR montage labels Grades 1–5 and
Normal but prints no detailed grading criteria; the questions do not fabricate
thresholds that are absent from the page. Non-instructional headers, timestamps,
footers and blank “Active space” are excluded.

## Verification and saved progress

- Build, integrity and existing-manifest validation pass.
- The full-bank smoke test exercises both answer outcomes for every item in this
  chapter, including matching rows, fill-up blanks, locking and completion.
- The original eleven unit IDs remain; existing XP and completion history are not
  cleared. Unit guides disclose the revision and ask learners to replay for new
  coverage. Question numbers changed, but the app does not persist question-level
  answer records.
- Variety heuristics: longest answer **15.5%**, detected answer-term overlap
  **0.7%**, no filler distractors, no repeated-template runs. Heuristic overlap is
  not silently called zero, and these metrics do not establish source accuracy.

**Next: Chapter 3, Tubular Anatomy, Book p717.** The remaining chapters are pending
in `SOURCE_REVIEW.md`; no whole-book completion is claimed.
