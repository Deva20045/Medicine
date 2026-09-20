# Self-audit — strict line-by-line book order

Date: **2026-09-20**

> **Historical baseline, before repairs.** Ch 1–2 have since been rebuilt and
> source-reviewed with caveats (p705–716). The old Ch 1 IDs/findings below refer
> to the original bank; its backward jump is repaired. Ch 54 findings remain
> unresolved. See `REAUDIT_CH1_SOURCE_ORDER.md`, `REAUDIT_CH2_SOURCE_ORDER.md`
> and `SOURCE_REVIEW.md` for current scope and next work (Ch 3, p717).

## Verdict: NOT COMPLIANT

The user's standard is **every line/element, in exact book order, without
compromise**. Passing the existing scripts does not establish that standard.
This audit found concrete source failures, not just missing verification evidence.
The rule is now persisted in `AGENTS.md` and at the top of `PROGRESS.md`.

## Scope and method

- Ran the existing integrity, runtime smoke, and variety checks on the current
  bank: **3,931 questions, 342 units, 58 live chapters** (Ch 1–56, 60–61).
- Independently inspected all chapter question arrays for adjacent decreases in
  `page`, including unit boundaries: **zero page reversals**.
- Reviewed the schema, unit coverage checks, and browser question-order code.
- Visually compared **Book p705, p970, and p971** with the chapter questions,
  using the supplied PDFs rendered at 1.7×. Inspected all 16 Ch 54 questions
  for the missing topics noted below.
- Counted PDF pages to reconcile the project page map.
- **This is not a completed line-by-line re-audit of all 290 represented pages.**
  Only the three pages above were visually checked in this pass. No other page
  receives a new source-verification PASS from this audit.

## Findings

### 1. FAIL — same-page source-order backtracking (Ch 1, Book p705)

The cloaca diagram's vesicourethral-canal branch lists the male urethral
contribution followed by the female contribution, before the next branch's
pelvic/phallic details. Current question order is:

| ID | Subject |
|---|---|
| MED-C1-010 | Male vesicourethral-canal contribution |
| MED-C1-011–012 | Pelvic-part contributions |
| MED-C1-013 | Phallic-part contributions |
| MED-C1-014 | Primitive rectum |
| MED-C1-015 | Female vesicourethral-canal contribution |

`MED-C1-015` returns to an earlier branch after the other branches. All these
questions cite p705, so a nondecreasing-page test cannot detect this violation.
The opening matching question also combines branches; such composites need
review against an explicitly documented diagram traversal.

### 2. FAIL — citation mismatch and omitted source content (Ch 54)

**Book p970** is Part 5, PDF page 6. It contains aldosterone action, collecting-duct
and intercalated-cell diagrams, Conn's syndrome features, and the comparison of
thiazide versus furosemide potassium loss with explanatory diagrams.

The only question assigned to p970 is **MED-C54-009**, asking about a significant
hypokalemia threshold of “below about 2–2.5 mEq/L.” That threshold is not on the
visually reviewed p970. Its `(Book p970)` citation therefore does not support it.
The chapter has a general aldosterone item (`MED-C54-008`, assigned p969), but
that does not cover p970's individual labels, branches, and applied points.
Neither the thiazide/furosemide comparison nor Conn's triad is tested by the
16-question chapter.

**Book p971** is Part 5, PDF page 7. It contains hypokalemia causes, renal/nonrenal
branches, cellular potassium shifts, clinical features, and a potassium-deficit
graph. The only question assigned to p971 is **MED-C54-010**, about flattened T
waves and prominent U waves. Those ECG details are not on this reviewed page.
Causes such as Bartter's/Gitelman's and clinical features such as rhabdomyolysis
and colonic pseudo-obstruction are absent from the chapter questions.

**Conclusion:** citing each page at least once is neither accurate source
attribution nor complete line-by-line coverage. Do not fix this by guessing new
page citations or merely sorting the existing questions; reread the chapter.

### 3. UNVERIFIED — most of the bank has no line-level verification in this pass

Question fields are `id`, `sec`, `page`, `q`, `opts`, `ans`, `exp`, and `fmt`.
There is no question-level source-line/element locator. Existing narrative reports
are historical evidence, not a complete ordered line-to-question checklist for
this audit. A manually verified checklist is needed for certification.

### 4. PASS, limited — stored question order is preserved at runtime

`beginUnit()` maps `curUnit.qs` without shuffling the question array; `shuffle()`
is applied to the answer options. Units are sorted by `n`. The integrity checker
requires flattened unit IDs to match the chapter question sequence exactly.
This preserves the authored sequence, **including any authoring mistakes**; it
does not prove that sequence matches the printed book.

### 5. FAIL — historical assurance is stronger than the evidence

`REPORT_CH52-56.md` and the latest batch entry in `PROGRESS.md` claimed full
coverage/green audits. The source failures above contradict a strict-coverage
interpretation. Added explicit superseding warnings rather than deleting the
historical reports. The live status means content is available, not certified.

The variety audit is a heuristic report, not a source-content gate. Its current
longest-answer rates for Ch 52–56 are **75.0%, 62.5%, 75.0%, 56.2%, 64.7%**,
respectively. These are additional quality concerns, not proof of omissions.

### 6. FIXED — inconsistent Part 1 page-map documentation

The actual Part 1 PDF has **67 pages**, not 55. Book p705 was visually confirmed
on PDF page **13**, consistent with the existing offset **K = 692**. Its mapped
book-content range is PDF pages **13–67** → Book p705–759. Other part lengths
are 64, 70, 71, 70, and 36 pages. The six files total **378 PDF pages**, including
12 pages before Book p705; the mapped Book p705–1070 span is 366 pages.
Corrected `PROGRESS.md`; the old row incorrectly paired PDF pages 1–55 with
K = 692. Individual printed page labels beyond the sample were not rechecked.

## Executed checks

| Check | Result | What it does NOT establish |
|---|---|---|
| `python3 check_integrity.py` | PASS: 58 chapters, 3,931 questions, 342 units, 290 represented pages | Every source line covered, within-page order, factual citation support |
| `node check_app_smoke.js` | PASS: all live chapter starts; 634 answer paths across 26 units | All questions medically/source-correct or all question flows exercised |
| `python3 audit_variety.py` | Completed; metrics reviewed | A source-coverage PASS or absence of quality risks |
| All chapter arrays: adjacent page comparison | No backwards page transitions | Order within a page |
| Visual source comparison: p705, p970, p971 | FAIL | No extrapolated verdict of full review for other pages |

To reproduce the independent page-order check:

```bash
python3 - <<'PY'
import json
from pathlib import Path
reversals = []
for path in sorted(Path('data').glob('ch*.json')):
    qs = json.loads(path.read_text())['questions']
    for previous, current in zip(qs, qs[1:]):
        if current['page'] < previous['page']:
            reversals.append((previous['id'], current['id']))
print('Backward page transitions:', reversals)
PY
```

Source images were rendered using PyMuPDF in an ignored local `.venv`; scratch
images in `_render/_audit_*.png` are ignored. The PDFs remain the source evidence.
No question-bank, question-ID, or application changes were made in this pass.

## Required next work, in book order

1. Start at **Ch 1, Book p705**. Make an ordered source-element → question-ID
   checklist, explicitly recording diagram/column traversal.
2. Repair the p705 backward jump and any uncovered elements, preserving saved
   progress compatibility when changing IDs/order.
3. Continue page by page through the existing bank. Do not jump directly to
   Ch 54 merely because it has a demonstrated failure; retain it as a known
   blocker to resolve when reached.
4. Rebuild and run structural/runtime/quality checks after content changes,
   then separately verify the source checklist. Resolve unclear print before
   marking the page complete.
5. Ch 57–59 and 62–74 are still unbuilt. Do not present them, or the currently
   live chapters, as fully line-by-line certified. Existing future-chapter NEXT
   instructions are superseded by this repair-first audit sequence.
