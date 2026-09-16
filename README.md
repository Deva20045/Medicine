# PULSE Medicine

A single-file MCQ study app for **Marrow Ed 8, Medicine Vol 3** (Book p705–1068).
Questions follow the book **line-by-line, in strict page order**, in varied formats
(recall, fill-ups, match-the-following, true/false, clinical scenarios, odd-one-out,
numeric). Every explanation ends with the exact book-page citation, and options are
shuffled on every run — so after solving a chapter you should not need the PDF.

> **Live:** https://deva20045.github.io/Medicine/ (served from `main`; the working
> branch previews here). Open `pulse-medicine.html` directly — no build step.

## Status
All 74 chapters are listed from day one; live chapters unlock automatically, the
rest show a **Soon** badge.

| Scope | Status |
|---|---|
| Ch 1 · Development of Kidneys (p705–710) — 9 units, 66 questions | ✅ live on this branch |
| Ch 2–74 (Nephrology, Acid–Base, Endocrinology, Hepatology, Infectious Diseases) | 🚧 in progress |

See **`PROGRESS.md`** — the single source of truth: page-offset map, 74-chapter
roadmap, data schema, per-chapter pipeline, and NEXT step.

## Repository layout
| Path | What it is |
|---|---|
| `pulse-medicine.html` | The app (all data embedded; standalone) |
| `index.html` | Redirect → `pulse-medicine.html` |
| `data/chNN.json` | Authoring source of truth per live chapter |
| `build_content.py` | Roadmap + validator; embeds `data/chNN.json` into the app |
| `check_integrity.py` | Structural gate (counts, order, citations, option quality, JS syntax) |
| `check_app_smoke.js` | Runtime test (DOM shim): roadmap rows, paths, quiz start |
| `audit_variety.py` | Format-mix + predictability audit (output saved to `AUDIT.md`) |
| `itemlab.py` | Add/edit questions with renumbering + auto-rebuild |
| `uploads/` | The 6 source book PDFs (Book p705–1070) |

## Run the checks (after any content change)
```bash
python build_content.py        # embeds data/ into pulse-medicine.html
python check_integrity.py      # must PASS
node check_app_smoke.js        # must PASS
python audit_variety.py > AUDIT.md
```

## Quality bar (enforced, not aspirational)
- Every book line, table, diagram, flowchart, classification, value and exception
  covered in book order; every page cited.
- 4 distinct, plausible, medical options per question — never "None of the above",
  never length-givable (answer ≤ 3× longest distractor), options shuffled at runtime.
- Mixed formats in every unit; clinical scenarios, comparisons and exam
  distinctions, not page-quizzing.
