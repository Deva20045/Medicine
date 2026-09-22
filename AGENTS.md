# Project memory — mandatory authoring rules

## Non-negotiable user requirement (2026-09-20)
> Strictly line to line, no compromise, in book order very strictly.

This applies to all new content, corrections, re-audits, and completion claims.
Read `PROGRESS.md`, `SOURCE_REVIEW.md`, and `SELF_AUDIT_BOOK_ORDER.md` before continuing work.

1. **Follow the actual book, line by line.** Cover every instructional line,
   bullet, sub-bullet, table row/cell, diagram label, arrow, flowchart branch,
   caption, note, numerical value, and exception. Do not substitute a summary,
   selected high-yield facts, or a fixed question quota for complete coverage.
2. **Preserve exact source order:** chapter → page → section → line/element.
   Finish each source block before moving on. Do not regroup by topic, jump
   ahead, or return to an earlier branch. For diagrams/multi-column layouts,
   inspect the scan and record the reading traversal; do not infer order from
   topic similarity. Units and question formats must follow that traversal.
3. **Only answer options may shuffle.** Never shuffle the question sequence.
   Format variety must not cause omissions or reorder source material; avoid
   composite questions that pull later material ahead of intervening lines.
4. **Verify against the scan.** Read rendered pages, zoom unclear text, confirm
   the printed page number, and cite the page that actually supports the fact.
   Do not invent facts, source positions, or unreadable values. Flag unresolved
   text instead of silently replacing it with general medical knowledge.
5. **Keep auditable coverage evidence.** For every reviewed page, maintain an
   ordered checklist of source lines/elements with their question IDs. Include
   table and figure elements. A page number alone is not line-level evidence.
   Never mark an unreviewed page or chapter as line-by-line verified.
6. **Separate structural checks from source verification.** Build, integrity,
   runtime, and variety checks are necessary but cannot prove completeness,
   same-page order, or factual citation accuracy. A successful script run is
   not a line-by-line PASS. Report failures and unverified scope explicitly.
7. **Repair before extending.** Resume from the earliest pending chapter in
   `SOURCE_REVIEW.md` and continue in book order; resolve gaps and backward jumps before claiming completion or
   expanding the bank. Previously shipped/live content is not automatically
   compliant. Do not silently delete existing content or reset user progress.

## Verification workflow
- Render the actual source and create the ordered coverage checklist first.
- Author/reconcile the questions and units against that checklist.
- Rebuild with `python3 build_content.py` after content changes.
- Run `python3 check_integrity.py`, `node check_app_smoke.js`, and
  `python3 audit_variety.py`.
- Re-check source coverage and order manually; record exact reviewed scope,
  remaining failures, and limitations in the audit and `PROGRESS.md`.

## Current continuation state (updated 2026-09-21)
- The user requested continuation through **all 74 chapters**, strictly in order.
- **Ch 70–74, p1039–1068:** built as 391 questions in 22 units on 2026-09-21
  (`author_c70.py`–`author_c74.py`, report in `REPORT_CH70-74.md`). The roadmap is now
  **complete: 74/74 chapters live, 5,329 questions, 412 units, all 364 book pages**
  (5,324 at roadmap completion plus 5 net new Ch 4 review questions).
- **Ch 1–5, p705–733:** rebuilt to 140, 148, 202, 55 and 88 questions with ordered source
  checklists in `data/source_review/`, source caveats, and unchanged unit IDs/history.
  The Ch 4 repair (2026-09-21) fixed a wrong-page findings citation, a p726→p727
  forward jump, a double-answer item and a within-page order fault, and completed
  every figure label; see `REAUDIT_CH4_SOURCE_ORDER.md`. The Ch 5 repair
  (2026-09-21) fixed two within-page order faults (PSGN expansion before its
  sub-bullets; p733 table tested in strict row order), moved the whole-chain
  consolidation behind its steps, un-silenced the printed "α actin 4", flagged the
  'mm' unit error and completed every figure/legend/caption label on p730–732;
  see `REAUDIT_CH5_SOURCE_ORDER.md`.
- **Ch 6, p734–739 (2026-09-22):** source-reviewed and rebuilt to 138 questions
  (`author_c6_review.py`, `write_ch06_manifest.py`, `REAUDIT_CH6_SOURCE_ORDER.md`).
  **35 of 133 shipped answer keys were wrong** — `migrate_parts.py` mis-rotated
  hand-authored options and `author.py` then shipped a distractor as the key while
  the explanation quoted the right value. Structural/runtime checks cannot detect
  this. **Every migrated chapter (Ch 7–12 at least) needs each stored `ans` checked
  against the print when reached.** The Ch 6 part files were removed; `data/ch06.json`
  is the reviewed source of truth.
- **Rejected evidence (2026-09-22):** a parallel commit on this branch (`f5f89ad`) added
  manifests for Ch 7–74 whose "source" fields were the question stems pasted back, with
  boilerplate traversals, and it kept all 35 wrong Ch 6 keys while declaring
  `--require-all` PASS. Those 68 manifests and its `REAUDIT_CH6-74_SOURCE_ORDER.md`
  were removed in the merge; only its 44 legacy fill-up/match format conversions in
  Ch 26/29/60/61 (format-only, facts/citations unchanged) were retained. Do not
  reintroduce generated manifests.
- **Ch 7, p740–747 (2026-09-22):** source-reviewed and rebuilt to 140 questions
  (`author_c7_review.py`, `write_ch07_manifest.py`, `REAUDIT_CH7_SOURCE_ORDER.md`).
  All 135 keys were correct (this chapter was authored answer-first); one wrong
  value fixed (DI urine osmolality printed **< 200** mOsm/kg, bank said 300); order
  re-sequenced on every page; 5 uncovered captions/rows added. Parts files removed;
  `data/ch07.json` is the source of truth.
- **Ch 8, p748–752 (2026-09-22):** source-reviewed (`author_c8_review.py`,
  `write_ch08_manifest.py`, `REAUDIT_CH8_SOURCE_ORDER.md`). All 83 keys correct; two
  wordings aligned to print; order re-sequenced on every page. Parts files removed.
- **Next (authoritative): the strict recorded line-by-line source review of Ch 9–74.**
  Recorded review manifests exist for Ch 1–8 only, so
  `python3 check_source_coverage.py --require-all` fails by design. Ch 9 (p753,
  Part 1 PDF p61) is the earliest pending chapter — still a migrated chapter, so
  check every key against the scan; continue in book order and never
  describe an incremental merge as whole-book compliance.
- The initial Ch 1 backward jump is repaired. PR #18 replaced Ch 52–56 with a
  338-question bank; preserve it. Old Ch 54 findings refer to the replaced bank,
  and the replacement must be source-reviewed when reached. Whole-book compliance
  is **NOT COMPLETE**. See `SOURCE_REVIEW.md` and the Ch 1–3 repair reports.
- `check_source_coverage.py` checks manifest order, question/unit references,
  PDF-page mapping, and PDF/content hashes. It cannot read the scan or certify
  medical truth. **Never generate evidence or update a review hash merely to
  make the checks pass.** Recheck the affected source first.
- Builds and integrity checks reject stale existing manifests. Use
  `python3 check_source_coverage.py --require-all` for whole-book completion;
  its current nonzero exit is expected and must not be bypassed.
- Runtime tests now cover every live question. Their 44 legacy format warnings
  remain content defects, not proof that unreviewed content is complete.

- The user authorised merging this continuation. Merge only the actual reviewed
  scope and passing implementation changes; never describe an incremental merge
  as completion of all 74 chapters. No unattended/background authoring is running.
