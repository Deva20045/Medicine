#!/usr/bin/env python3
"""Order + unit check + rebuild for one chapter of the page-anchored pipeline.

    python3 assemble.py <chapter> [more chapters...]

1. every `data/parts/cNN/<key>.json` (key = p<page><letter>) is sorted by
   (page, letter) and written to `_order.json`;
2. `data/units/cNN.json` is validated: each part key used exactly once, units in
   page order, every unit has a non-recall format and >= 6 questions;
3. `author.py` rebuilds `data/chNN.json`.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import author  # noqa: E402

DATA = ROOT / "data"


def natural_key(name: str) -> tuple[int, str]:
    match = re.fullmatch(r"p(\d+)([a-z]*)", name)
    if not match:
        raise SystemExit(f"BAD PART NAME {name!r}: expected p<page><letter>")
    return int(match.group(1)), match.group(2) or "a"


def assemble(ch: int) -> None:
    parts_dir = DATA / "parts" / f"c{ch}"
    files = sorted((p for p in parts_dir.glob("*.json") if p.name != "_order.json"),
                   key=lambda p: natural_key(p.stem))
    keys = [p.stem for p in files]
    meta = {}
    for path in files:
        blob = json.loads(path.read_text(encoding="utf-8"))
        page = int(blob["page"])
        if natural_key(path.stem)[0] != page:
            raise SystemExit(f"{path.name}: file name page != 'page' field {page}")
        meta[path.stem] = {"page": page, "n": len(blob["items"]),
                           "fmts": Counter(i["fmt"] for i in blob["items"])}
    (parts_dir / "_order.json").write_text(json.dumps(keys, indent=1) + "\n", encoding="utf-8")

    specs = json.loads((DATA / "units" / f"c{ch}.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    used: Counter[str] = Counter()
    last_page = 0
    for i, spec in enumerate(specs, 1):
        for key in spec["parts"]:
            if key not in meta:
                errors.append(f"unit {i} ({spec['title']}): unknown part {key!r}")
                continue
            used[key] += 1
        pages = [meta[k]["page"] for k in spec["parts"] if k in meta]
        if pages and pages[0] < last_page:
            errors.append(f"unit {i} ({spec['title']}): page {pages[0]} goes back from {last_page}")
        if pages:
            last_page = pages[-1]
        total = sum(meta[k]["n"] for k in spec["parts"] if k in meta)
        fmts = Counter()
        for k in spec["parts"]:
            if k in meta:
                fmts.update(meta[k]["fmts"])
        if total < 6:
            errors.append(f"unit {i} ({spec['title']}): only {total} questions")
        if not (set(fmts) - {"recall"}):
            errors.append(f"unit {i} ({spec['title']}): no varied-format item")
    for key in keys:
        if used[key] != 1:
            errors.append(f"part {key} used {used[key]} times (must be exactly once)")
    if errors:
        print(f"Ch{ch}: ASSEMBLY BLOCKED")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    author.build(ch)
    artifact = json.loads((DATA / f"ch{ch:02d}.json").read_text(encoding="utf-8"))
    qs = artifact["questions"]
    pages = Counter(q["page"] for q in qs)
    print(f"  per page: " + " ".join(f"p{p}:{pages[p]}" for p in sorted(pages)))
    print(f"  answer spread: {dict(sorted(Counter(q['ans'] for q in qs).items()))}")
    print(f"  parts: {len(keys)} -> " + " ".join(f"{k}({meta[k]['n']})" for k in keys))


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        assemble(int(arg))
