# Legacy format defects — 2026-09-20

The expanded `node check_app_smoke.js` exercises every live question with both
correct and incorrect selections. It identified the following **44** format
issues in chapters not yet source-reviewed. Plain-text fallbacks function, but
these are NOT valid matching boards/fill-up blanks merely because runtime passes.
They must be repaired when their chapter is reached in the strict source-order
queue. Reviewed chapters fail the runtime gate for either defect.

PR #18 replaced Ch 52–56; this reconciled inventory no longer attributes the
old ten malformed matching stems to that new content.

Regenerate the inventory from the warnings printed by the smoke test after repairs.
The report covers renderer-compatible match and fill-up syntax only; it does not
validate clinical scenarios, true/false substance, or source completeness.

- MED-C26-021: match label without a parseable matching list
- MED-C29-019: match label without a parseable matching list
- MED-C60-003: fill-up label without a renderable blank
- MED-C60-008: fill-up label without a renderable blank
- MED-C60-012: fill-up label without a renderable blank
- MED-C60-016: fill-up label without a renderable blank
- MED-C60-019: fill-up label without a renderable blank
- MED-C60-022: fill-up label without a renderable blank
- MED-C60-023: fill-up label without a renderable blank
- MED-C60-027: fill-up label without a renderable blank
- MED-C60-029: fill-up label without a renderable blank
- MED-C60-034: fill-up label without a renderable blank
- MED-C60-035: fill-up label without a renderable blank
- MED-C60-039: fill-up label without a renderable blank
- MED-C60-041: fill-up label without a renderable blank
- MED-C60-045: fill-up label without a renderable blank
- MED-C60-049: fill-up label without a renderable blank
- MED-C60-050: fill-up label without a renderable blank
- MED-C60-056: fill-up label without a renderable blank
- MED-C60-057: fill-up label without a renderable blank
- MED-C60-061: fill-up label without a renderable blank
- MED-C60-062: fill-up label without a renderable blank
- MED-C60-066: fill-up label without a renderable blank
- MED-C60-077: fill-up label without a renderable blank
- MED-C60-083: fill-up label without a renderable blank
- MED-C60-084: fill-up label without a renderable blank
- MED-C61-001: fill-up label without a renderable blank
- MED-C61-007: fill-up label without a renderable blank
- MED-C61-011: fill-up label without a renderable blank
- MED-C61-014: fill-up label without a renderable blank
- MED-C61-019: fill-up label without a renderable blank
- MED-C61-025: fill-up label without a renderable blank
- MED-C61-028: fill-up label without a renderable blank
- MED-C61-029: fill-up label without a renderable blank
- MED-C61-032: fill-up label without a renderable blank
- MED-C61-033: fill-up label without a renderable blank
- MED-C61-034: fill-up label without a renderable blank
- MED-C61-039: match label without a parseable matching list
- MED-C61-045: match label without a parseable matching list
- MED-C61-052: match label without a parseable matching list
- MED-C61-057: match label without a parseable matching list
- MED-C61-062: match label without a parseable matching list
- MED-C61-067: match label without a parseable matching list
- MED-C61-073: match label without a parseable matching list
