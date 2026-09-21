#!/usr/bin/env python3
"""Check recorded source-review evidence, NOT medical truth or visual coverage.

Default: validate every existing manifest and report the remaining chapters.
--require-all: fail until all 74 chapters have valid, complete review manifests.
--write-report: regenerate SOURCE_REVIEW.md with an honest all-chapter inventory.

Only a human/source-reading review may populate data/source_review/chNN.json. This
checker must never generate evidence from question counts or page citations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from build_content import CHAPTERS

ROOT = Path(__file__).resolve().parent
SOURCE_PARTS = (
    (705, 759, 692, "Medicine_Vol3_Part1_pages_705-759.pdf"),
    (760, 823, 759, "Medicine_Vol3_Part2_pages_760-823.pdf"),
    (824, 893, 823, "Medicine_Vol3_Part3_pages_824-893.pdf"),
    (894, 964, 893, "Medicine_Vol3_Part4_pages_894-964.pdf"),
    (965, 1034, 964, "Medicine_Vol3_Part5_pages_965-1034.pdf"),
    (1035, 1070, 1034, "Medicine_Vol3_Part6_pages_1035-1070.pdf"),
)


def content_digest(chapter: dict) -> str:
    payload = {key: chapter[key] for key in ("questions", "units")}
    return hashlib.sha256(json.dumps(
        payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode()).hexdigest()


def validate_manifest(manifest: dict, chapter: dict, first: int, last: int) -> list[str]:
    """Validate order, references and freshness; visual correctness is manual."""
    errors = []
    number = chapter["chapter"]
    if manifest.get("chapter") != number:
        errors.append("manifest chapter mismatch")
    if manifest.get("pageRange") != f"{first}-{last}":
        errors.append("manifest page range mismatch")
    if manifest.get("status") not in {"reviewed", "reviewed-with-source-caveats"}:
        errors.append("manifest must explicitly declare a completed source review")
    for key in ("reviewedAt", "method"):
        if not isinstance(manifest.get(key), str) or not manifest[key].strip():
            errors.append(f"missing review {key}")
    caveats = manifest.get("caveats")
    if not isinstance(caveats, list) or any(not isinstance(c, str) or not c.strip() for c in caveats):
        errors.append("caveats must be a list of nonempty text")
    elif manifest.get("status") == "reviewed-with-source-caveats" and not caveats:
        errors.append("source-caveat status requires explicit caveats")
    elif manifest.get("status") == "reviewed" and caveats:
        errors.append("review with caveats must use reviewed-with-source-caveats status")
    if manifest.get("contentSha256") != content_digest(chapter):
        errors.append("stale review: question/unit content changed after source review")

    pages = manifest.get("pages")
    if not isinstance(pages, list) or any(not isinstance(p, dict) for p in pages):
        return errors + ["pages must be an ordered list of page reviews"]
    if [p.get("page") for p in pages] != list(range(first, last + 1)):
        errors.append("review must list every chapter page once in exact order")
    questions = chapter["questions"]
    by_id = {q["id"]: q for q in questions}
    expected = [q["id"] for q in questions]
    covered = []
    for p in pages:
        page = p.get("page")
        if type(page) is not int or not first <= page <= last:
            errors.append("invalid reviewed page number")
            continue
        part = next(part for part in SOURCE_PARTS if part[0] <= page <= part[1])
        if p.get("pdfPage") != page - part[2]:
            errors.append(f"p{page}: PDF-to-book page map mismatch")
        # Page-specific sources allow chapters spanning two PDF files.
        source = p.get("pdf", manifest.get("pdf"))
        if source != f"uploads/{part[3]}":
            errors.append(f"p{page}: wrong source PDF")
        if not isinstance(p.get("traversal"), str) or not p["traversal"].strip():
            errors.append(f"p{page}: missing scan reading traversal")
        elements = p.get("elements")
        if not isinstance(elements, list) or not elements:
            errors.append(f"p{page}: no source-element checklist")
            continue
        for index, element in enumerate(elements, 1):
            if not isinstance(element, dict):
                errors.append(f"p{page}: invalid source element")
                continue
            eid = f"p{page}-e{index:03d}"
            if element.get("element") != eid or element.get("page") != page:
                errors.append(f"{eid}: source elements must be numbered in reading order")
            if not isinstance(element.get("source"), str) or not element["source"].strip():
                errors.append(f"{eid}: missing source-line/element description")
            ids = element.get("questionIds")
            if not isinstance(ids, list) or not ids or any(not isinstance(qid, str) for qid in ids):
                errors.append(f"{eid}: missing question IDs")
                continue
            covered.extend(ids)
            for qid in ids:
                if qid not in by_id:
                    errors.append(f"{eid}: unknown question {qid}")
                elif by_id[qid]["page"] != page:
                    errors.append(f"{eid}: {qid} cites a different page")
    if covered != expected:
        errors.append("source-element question IDs must cover the chapter exactly once in book order")
    if [qid for unit in chapter["units"] for qid in unit["qs"]] != expected:
        errors.append("unit playback must follow the reviewed source-element sequence")
    return errors


def audit(root: Path = ROOT) -> tuple[list[dict], list[str]]:
    rows, errors, pdf_hashes = [], [], {}
    directory = root / "data" / "source_review"
    expected_paths = {f"ch{n:02d}.json" for n, _, _ in CHAPTERS}
    for path in sorted(directory.glob("*.json")):
        if path.name not in expected_paths:
            errors.append(f"Unknown source-review manifest: {path.name}")
    for index, (number, title, first) in enumerate(CHAPTERS):
        last = CHAPTERS[index + 1][2] - 1 if index + 1 < len(CHAPTERS) else 1068
        source_path = root / "data" / f"ch{number:02d}.json"
        review_path = directory / source_path.name
        row = dict(chapter=number, title=title, first=first, last=last,
                   questions=0, status="not-built", manifest=None)
        try:
            if source_path.exists():
                chapter = json.loads(source_path.read_text())
                row.update(questions=len(chapter["questions"]), status="pending-source-review")
            if review_path.exists():
                if not source_path.exists():
                    raise ValueError("review exists without a chapter bank")
                manifest = json.loads(review_path.read_text())
                problems = validate_manifest(manifest, chapter, first, last)
                if chapter.get("chapter") != number:
                    problems.append("chapter filename/number mismatch")
                for p in manifest.get("pages", []):
                    if not isinstance(p, dict):
                        continue
                    name = p.get("pdf", manifest.get("pdf", ""))
                    # Do not read arbitrary paths supplied by a malformed manifest.
                    if name not in {f"uploads/{part[3]}" for part in SOURCE_PARTS}:
                        continue
                    if name not in pdf_hashes:
                        pdf_hashes[name] = hashlib.sha256((root / name).read_bytes()).hexdigest()
                    if p.get("pdfSha256", manifest.get("pdfSha256")) != pdf_hashes[name]:
                        problems.append(f"source PDF changed: {name}")
                if problems:
                    row["status"] = "invalid-review"
                    errors.extend(f"Ch {number}: {problem}" for problem in dict.fromkeys(problems))
                else:
                    row.update(status=manifest["status"], manifest=review_path.relative_to(root).as_posix())
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
            errors.append(f"Ch {number}: {exc}")
            row["status"] = "invalid-review"
        rows.append(row)
    return rows, errors


def write_report(rows: list[dict], errors: list[str], root: Path = ROOT) -> None:
    reviewed = [r for r in rows if r["manifest"]]
    pending = [r for r in rows if not r["manifest"]]
    pages = sum(r["last"] - r["first"] + 1 for r in reviewed)
    lines = [
        "# All-chapter source-review tracker", "",
        "Generated by `python3 check_source_coverage.py --write-report`.", "",
        "**Scope: all 74 chapters, Book p705–1068, in exact book order.**",
        "",
        f"- Valid recorded source reviews: **{len(reviewed)}/74 chapters**, **{pages}/364 pages**.",
        f"- Current bank: **{sum(r['questions'] for r in rows):,} questions**.",
        f"- Remaining chapters: **{len(pending)}** (existing content and unbuilt chapters both require review).",
        "- A valid manifest proves consistency with a recorded manual review, not medical truth or independent visual verification.",
        "- Source caveats remain explicit; no pending chapter is certified by question counts, citations, or runtime tests.",
        "",
    ]
    if pending:
        r = pending[0]
        lines += [f"**Next in order: Ch {r['chapter']} — {r['title']}, Book p{r['first']}.**", ""]
    lines += [
        "## Known blockers and source evidence", "",
        "- Historical findings: `SELF_AUDIT_BOOK_ORDER.md`. PR #18 replaced Ch 52–56; preserve the newer bank and source-review it when reached rather than applying old Ch 54 IDs to it.",
        "- Ch 1–4 source repairs and caveats: `REAUDIT_CH1_SOURCE_ORDER.md`, `REAUDIT_CH2_SOURCE_ORDER.md`, `REAUDIT_CH3_SOURCE_ORDER.md`, `REAUDIT_CH4_SOURCE_ORDER.md`, and their `data/source_review/` manifests.",
        "- Full-bank runtime tests flag 44 legacy match/fill-up format defects; see `CONTENT_FORMAT_ISSUES.md`. These are still pending source review.",
        "- Reviewed content edits invalidate the content hash until the source checklist is rechecked.",
        "- Never generate manifests for pending chapters merely to make `--require-all` pass.", "",
        "| Ch | Chapter | Book pages | Questions | Source review |", "|---:|---|---|---:|---|",
    ]
    for r in rows:
        status = (f"[{r['status']}]({r['manifest']})" if r["manifest"] else r["status"])
        lines.append(f"| {r['chapter']} | {r['title']} | {r['first']}–{r['last']} | {r['questions']} | {status} |")
    if errors:
        lines += ["", "## Invalid evidence (must repair)", ""] + [f"- {e}" for e in errors]
    (root / "SOURCE_REVIEW.md").write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-all", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    rows, errors = audit()
    reviewed = sum(bool(r["manifest"]) for r in rows)
    if args.write_report:
        write_report(rows, errors)
    for error in errors:
        print("ERROR:", error)
    print(f"Recorded source reviews: {reviewed}/{len(rows)}; remaining: {len(rows) - reviewed}.")
    if reviewed != len(rows):
        print("NOT COMPLETE: all-chapter strict line-by-line compliance is not certified.")
    if errors or (args.require_all and reviewed != len(rows)):
        return 1
    print("PASS: existing review manifests are consistent; unreviewed chapters are not certified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
