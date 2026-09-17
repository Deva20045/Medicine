#!/usr/bin/env python3
"""Validate PULSE Medicine's standalone app and structured chapter source artifacts."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_PATH = ROOT / "pulse-medicine.html"
DATA_DIR = ROOT / "data"

# Total roadmap chapters in the book (Medicine Vol 3, Book p705-1068).
TOTAL_ROADMAP_CHAPTERS = 74

# Book-page scope, exact title, and intended content volume for every live chapter.
# Add a chapter here (title, first page, last page, expected question count,
# expected unit count) when its data/chNN.json lands.
LIVE_CHAPTERS = {
    1: ("Development of Kidneys", 705, 710, 68, 9),
    2: ("Gross Anatomy of Kidney", 711, 716, 66, 11),
    3: ("Tubular Anatomy", 717, 725, 100, 13),
    4: ("Juxtaglomerular Apparatus", 726, 729, 50, 7),
    5: ("Glomerulus - Anatomy", 730, 733, 56, 8),
    6: ("Renal Physiology", 734, 739, 69, 9),
    7: ("Urine Analysis", 740, 747, 94, 13),
    8: ("Basic Approach to Kidney Disease and Renal Artery Stenosis", 748, 752, 56, 8),
    9: ("Thrombotic Microangiopathy", 753, 755, 35, 5),
    10: ("Glomerular Disease - Patterns", 756, 761, 60, 9),
    11: ("Podocytopathies", 762, 769, 83, 8),
    12: ("MPGN and IgA Nephropathy", 770, 774, 52, 6),
    13: ("Post Streptococcal Glomerulonephritis", 775, 777, 73, 3),
    14: ("RPGN and Pulmonary Renal Syndrome", 778, 782, 82, 5),
    15: ("Familial Glomerular Syndromes", 783, 785, 54, 4),
    16: ("Ciliopathies", 786, 792, 139, 6),
    17: ("Chronic Tubulointerstitial Disease", 793, 795, 52, 3),
    18: ("Acute Kidney Injury", 796, 804, 181, 9),
    19: ("Chronic Kidney Disease", 805, 807, 91, 8),
    20: ("Anemia in Chronic Kidney Disease", 808, 810, 76, 7),
    21: ("CKD - Calciphylaxis and Cardiovascular changes", 811, 814, 93, 6),
    22: ("Diabetic Kidney Disease", 815, 818, 90, 7),
}

# Question formats used by the varied-format authoring. Every unit must contain
# at least one item that is not plain recall, so a learner meets fill-ups,
# matching, true/false statements, scenarios and odd-one-out items.
VALID_FMTS = {"fillup", "match", "truefalse", "scenario", "oddoneout", "recall", "numeric", "management"}

REQUIRED_UI = [
    '<div id="home">', '<div id="chapters" class="hidden">',
    '<div id="path" class="hidden">', '<div id="guide" class="hidden">',
    '<div id="quiz" class="hidden">', '<div id="unitdone" class="hidden">',
    'id="hStreak"', 'id="hXP"', 'id="sXP"', 'id="sStreak"', 'id="sUnits"',
    'id="chList"', 'id="nodes"', 'id="qbar"', 'id="qtag"', 'id="qtext"',
    'id="opts"', 'id="fb"', 'id="nextBtn"', 'id="dScore"', 'id="dXP"',
    'id="dAcc"', 'id="dRev"', 'continueLearning()', 'unlockAll()', 'beginUnit()',
    'renderQ()', 'answer(o,btn)', 'finishUnit()', 'shuffle(a)',
]


def extract_json(html: str, name: str, next_name: str | None = None) -> object:
    """Extract one JSON array assigned to a top-level JS const."""
    tail = f";\\nconst {next_name}" if next_name else ";"
    match = re.search(rf"const {name} = (\[[\s\S]*?\]){tail}", html)
    if not match:
        raise ValueError(f"Could not extract {name} from {APP_PATH.name}")
    return json.loads(match.group(1))


def check_javascript_syntax(html: str, errors: list[str]) -> None:
    scripts = re.findall(r"<script>([\s\S]*?)</script>", html)
    if len(scripts) != 1:
        errors.append(f"Expected exactly one inline script, found {len(scripts)}")
        return
    temp_name = ""
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as temp:
            temp.write(scripts[0])
            temp_name = temp.name
        result = subprocess.run(
            ["node", "--check", temp_name], text=True, capture_output=True, check=False
        )
        if result.returncode:
            errors.append("JavaScript syntax check failed: " + result.stderr.strip())
    except FileNotFoundError:
        errors.append("Node.js is unavailable, so JavaScript syntax was not checked")
    finally:
        if temp_name:
            Path(temp_name).unlink(missing_ok=True)


def verify() -> None:
    html = APP_PATH.read_text(encoding="utf-8")
    errors: list[str] = []

    for element in REQUIRED_UI:
        if element not in html:
            errors.append(f"Missing UI element/function: {element}")

    try:
        questions = extract_json(html, "QUESTIONS", "UNITS")
        units = extract_json(html, "UNITS", "CHAPTERS")
        chapters = extract_json(html, "CHAPTERS")
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"FAILED: {exc}")
        sys.exit(1)

    print(f"Verified extraction: {len(questions)} questions, {len(units)} units, {len(chapters)} chapters.")

    if len(chapters) != TOTAL_ROADMAP_CHAPTERS:
        errors.append(
            f"Expected {TOTAL_ROADMAP_CHAPTERS} roadmap chapters, found {len(chapters)}"
        )
    chapter_numbers = [chapter.get("n") for chapter in chapters]
    if chapter_numbers != list(range(1, TOTAL_ROADMAP_CHAPTERS + 1)):
        errors.append(
            "Roadmap chapter numbers must be a unique contiguous sequence from 1 "
            f"through {TOTAL_ROADMAP_CHAPTERS}"
        )

    metadata = {chapter.get("n"): chapter for chapter in chapters}
    for number, (title, first_page, _last_page, expected_qs, expected_units) in LIVE_CHAPTERS.items():
        entry = metadata.get(number, {})
        if not entry.get("live"):
            errors.append(f"Chapter {number} should be marked live")
        if entry.get("t") != title:
            errors.append(f"Chapter {number} title mismatch: {entry.get('t')!r}")
        if entry.get("p") != first_page:
            errors.append(f"Chapter {number} roadmap page should be {first_page}, got {entry.get('p')}")
        # This makes accidental partial generation or duplicate appends fail loudly.
        if expected_qs < 1 or expected_units < 1:
            errors.append(f"Invalid expected content count configured for Chapter {number}")
    for number in range(1, TOTAL_ROADMAP_CHAPTERS + 1):
        if number not in LIVE_CHAPTERS and metadata.get(number, {}).get("live"):
            errors.append(f"Chapter {number} is marked live but has no expected content entry")

    question_ids = [question.get("id") for question in questions]
    if len(question_ids) != len(set(question_ids)):
        errors.append("Question IDs are not globally unique")
    unit_ids = [unit.get("id") for unit in units]
    if len(unit_ids) != len(set(unit_ids)):
        errors.append("Unit IDs are not globally unique")
    normalized_stems: dict[str, str] = {}
    for question in questions:
        stem = question.get("q", "")
        normalized = re.sub(r"\s+", " ", stem).strip().casefold()
        if normalized and normalized in normalized_stems:
            errors.append(
                f"Duplicate question stem: {question.get('id')} and {normalized_stems[normalized]}"
            )
        elif normalized:
            normalized_stems[normalized] = question.get("id", "")

    qs_by_ch: dict[int, list[dict]] = {}
    q_by_id: dict[str, dict] = {}
    for question in questions:
        qid = question.get("id", "")
        match = re.fullmatch(r"MED-C(\d+)-(\d{3})", qid)
        if not match:
            errors.append(f"Invalid question ID format: {qid!r}")
            continue
        number = int(match.group(1))
        qs_by_ch.setdefault(number, []).append(question)
        q_by_id[qid] = question

        for key in ("sec", "q", "exp"):
            if not isinstance(question.get(key), str) or not question[key].strip():
                errors.append(f"{qid}: missing/non-text {key}")
        if not isinstance(question.get("page"), int):
            errors.append(f"{qid}: page must be an integer")
        options = question.get("opts")
        if not isinstance(options, list) or len(options) != 4:
            errors.append(f"{qid}: expected exactly 4 options")
        elif any(not isinstance(option, str) or not option.strip() for option in options):
            errors.append(f"{qid}: options must be non-empty text")
        elif len({option.strip().casefold() for option in options}) != 4:
            errors.append(f"{qid}: options must be distinct")
        answer = question.get("ans")
        if isinstance(answer, bool) or not isinstance(answer, int) or not 0 <= answer <= 3:
            errors.append(f"{qid}: invalid answer index {answer!r}")
        # A learner must not be able to spot the answer by picking the longest
        # option. 3.0x is the accepted ceiling; anything above it is a giveaway.
        if isinstance(options, list) and len(options) == 4 and isinstance(answer, int) and 0 <= answer <= 3:
            lengths = [len(option) for option in options]
            longest_distractor = max(length for index, length in enumerate(lengths) if index != answer)
            if lengths[answer] > max(longest_distractor, 1) * 3.0:
                errors.append(
                    f"{qid}: the answer is {lengths[answer] / max(longest_distractor, 1):.1f}x the longest "
                    f"distractor, so it can be guessed from length alone"
                )
        if question.get("fmt") is not None and question.get("fmt") not in VALID_FMTS:
            errors.append(f"{qid}: unknown question format {question.get('fmt')!r}")

    unexpected_question_chapters = sorted(set(qs_by_ch) - set(LIVE_CHAPTERS))
    if unexpected_question_chapters:
        errors.append(f"Questions found in non-live chapters: {unexpected_question_chapters}")

    page_coverage: dict[int, set[int]] = {}
    for number, (title, first_page, last_page, expected_qs, _expected_units) in LIVE_CHAPTERS.items():
        chapter_questions = qs_by_ch.get(number, [])
        if len(chapter_questions) != expected_qs:
            errors.append(
                f"Chapter {number}: expected {expected_qs} questions, found {len(chapter_questions)}"
            )
        for index, question in enumerate(chapter_questions, 1):
            expected_id = f"MED-C{number}-{index:03d}"
            qid = question.get("id")
            if qid != expected_id:
                errors.append(f"Chapter {number} question {index}: expected {expected_id}, got {qid}")
            page = question.get("page")
            if isinstance(page, int):
                page_coverage.setdefault(number, set()).add(page)
                if not first_page <= page <= last_page:
                    errors.append(f"{qid}: Book p{page} outside Chapter {number} range {first_page}\u2013{last_page}")
            explanation = question.get("exp", "")
            page_match = re.search(r"\(Book p(\d+)\)$", explanation)
            if not page_match:
                errors.append(f"{qid}: explanation must end with '(Book pX)'")
            elif isinstance(page, int) and int(page_match.group(1)) != page:
                errors.append(f"{qid}: explanation citation and page field differ")
        missing_pages = set(range(first_page, last_page + 1)) - page_coverage.get(number, set())
        if missing_pages:
            errors.append(f"Chapter {number}: no question cites Book page(s) {sorted(missing_pages)}")

    units_by_ch: dict[int, list[dict]] = {}
    for unit in units:
        number = unit.get("ch")
        if number not in LIVE_CHAPTERS:
            errors.append(f"{unit.get('id')}: unit belongs to non-live/invalid Chapter {number}")
            continue
        units_by_ch.setdefault(number, []).append(unit)

    unexpected_unit_chapters = sorted(set(units_by_ch) - set(LIVE_CHAPTERS))
    if unexpected_unit_chapters:
        errors.append(f"Units found in non-live chapters: {unexpected_unit_chapters}")

    for number, (_title, _first_page, _last_page, _expected_qs, expected_units) in LIVE_CHAPTERS.items():
        chapter_units = units_by_ch.get(number, [])
        if len(chapter_units) != expected_units:
            errors.append(f"Chapter {number}: expected {expected_units} units, found {len(chapter_units)}")
        covered: list[str] = []
        for index, unit in enumerate(chapter_units, 1):
            expected_id = f"MED-U{number}-{index}"
            uid = unit.get("id")
            if uid != expected_id:
                errors.append(f"Chapter {number} unit {index}: expected {expected_id}, got {uid}")
            if unit.get("n") != index:
                errors.append(f"{uid}: expected n={index}, got {unit.get('n')}")
            for key in ("title", "sec", "guide"):
                if not isinstance(unit.get(key), str) or not unit[key].strip():
                    errors.append(f"{uid}: missing/non-text {key}")
            qids = unit.get("qs")
            if not isinstance(qids, list) or not qids:
                errors.append(f"{uid}: must contain at least one question")
                continue
            covered.extend(qids)
            unit_pages: list[int] = []
            unit_formats: set[str] = set()
            for qid in qids:
                question = q_by_id.get(qid)
                if question is None:
                    errors.append(f"{uid}: references unknown question {qid}")
                    continue
                if question["id"].split("-")[1] != f"C{number}":
                    errors.append(f"{uid}: references question from another chapter ({qid})")
                unit_pages.append(question["page"])
                if question.get("fmt") is not None:
                    unit_formats.add(question.get("fmt"))
            if not unit_formats:
                errors.append(f"{uid}: has no varied-format question (add a fill-up, match, true/false, scenario or odd-one-out item)")
            if any(unit_pages[i] < unit_pages[i - 1] for i in range(1, len(unit_pages))):
                errors.append(f"{uid}: Book pages are not in source order")

        expected_coverage = [question["id"] for question in qs_by_ch.get(number, [])]
        if covered != expected_coverage:
            errors.append(f"Chapter {number}: units must cover every question exactly once and in source order")

    # The editable JSON artifacts must exactly match what the standalone app ships.
    for number, (title, first_page, last_page, _expected_qs, _expected_units) in LIVE_CHAPTERS.items():
        path = DATA_DIR / f"ch{number:02d}.json"
        if not path.exists():
            errors.append(f"Missing source artifact: {path.relative_to(ROOT)}")
            continue
        try:
            artifact = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON ({exc})")
            continue
        if artifact.get("chapter") != number or artifact.get("title") != title:
            errors.append(f"{path.name}: chapter metadata mismatch")
        if artifact.get("pageRange") != f"{first_page}-{last_page}":
            errors.append(f"{path.name}: pageRange mismatch")
        if artifact.get("questions") != qs_by_ch.get(number, []):
            errors.append(f"{path.name}: questions do not exactly match the embedded app content")
        if artifact.get("units") != units_by_ch.get(number, []):
            errors.append(f"{path.name}: units do not exactly match the embedded app content")

    check_javascript_syntax(html, errors)

    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for error in errors[:50]:
            print(" -", error)
        if len(errors) > 50:
            print(f" ... and {len(errors) - 50} more")
        sys.exit(1)

    total_pages = sum(last - first + 1 for _title, first, last, _q, _u in LIVE_CHAPTERS.values())
    live_count = len(LIVE_CHAPTERS)
    print(
        f"PASS: {live_count} live chapter(s) of {TOTAL_ROADMAP_CHAPTERS}; "
        f"{len(questions)} questions; {len(units)} units; "
        f"all {total_pages} in-scope Book pages represented; "
        "IDs, four-option structure, citations, order, source artifacts, UI hooks, and JavaScript syntax verified."
    )


if __name__ == "__main__":
    verify()
