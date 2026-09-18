#!/usr/bin/env python3
"""Migrate a hand-authored data/chNN.json into the ordered, page-anchored part
pipeline used by author.py (the layout already used for Ch 13-22).

For every unit, its questions are grouped by Book page; each (unit, page) group
becomes one part file `data/parts/cNN/p<page><letter>.json` (a page that carries
two units therefore yields two parts, so a part never straddles a unit).  Parts
longer than MAX_ITEMS are split with further letters.

Options are un-rotated back to the authoring convention (correct option first)
by inverting author.py's deterministic rotation, so that `python author.py NN`
reproduces the original artifact byte-for-byte apart from the answer index.

Usage: python3 migrate_parts.py <chapter>
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
MAX_ITEMS = 18


def authored_first(question: dict) -> tuple[list[str], int]:
    """Invert author.py's rotation: return (opts with the answer first, 0)."""
    opts = list(question["opts"])
    ans = int(question["ans"])
    # author.py always stores the answer at index H = sha256(id) % 4; the item
    # was authored with the answer first (index 0). Undo a left-rotation by H.
    h = int(hashlib.sha256(question["id"].encode()).hexdigest(), 16) % 4
    if h == ans:
        # produced by author.py -> rotate right by h to recover "answer first"
        restored = [opts[(i - h) % 4] for i in range(4)]
        return restored, 0
    # hand-authored artifact with an arbitrary answer index -> move answer to 0
    ordered = [opts[ans]] + [o for i, o in enumerate(opts) if i != ans]
    return ordered, 0


def migrate(ch: int) -> None:
    path = DATA / f"ch{ch:02d}.json"
    chapter = json.loads(path.read_text(encoding="utf-8"))
    q_by_id = {q["id"]: q for q in chapter["questions"]}
    out_dir = DATA / "parts" / f"c{ch}"
    out_dir.mkdir(parents=True, exist_ok=True)

    order: list[str] = []
    units_spec: list[dict] = []
    page_counter: dict[int, int] = {}

    def next_letter(page: int) -> str:
        idx = page_counter.get(page, 0)
        page_counter[page] = idx + 1
        return chr(ord("a") + idx)

    for unit in chapter["units"]:
        groups: list[tuple[int, list[dict]]] = []
        for qid in unit["qs"]:
            q = q_by_id[qid]
            page = int(q["page"])
            if groups and groups[-1][0] == page:
                groups[-1][1].append(q)
            else:
                groups.append((page, [q]))
        keys: list[str] = []
        for page, qs in groups:
            for start in range(0, len(qs), MAX_ITEMS):
                chunk = qs[start:start + MAX_ITEMS]
                key = f"p{page}{next_letter(page) if start == 0 else ''}"
                if start > 0:  # second slice of the same (unit, page) group
                    key = f"p{page}{next_letter(page)}"
                items = []
                for q in chunk:
                    opts, _ = authored_first(q)
                    items.append({
                        "fmt": q.get("fmt", "recall"),
                        "q": q["q"],
                        "opts": opts,
                        "ans": 0,
                        "exp": q["exp"],
                    })
                sec = chunk[0].get("sec") or f"{unit['title']} · p{page}"
                (out_dir / f"{key}.json").write_text(
                    json.dumps({"page": page, "sec": sec, "items": items},
                               ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
                order.append(key)
                keys.append(key)
        units_spec.append({"title": unit["title"], "sec": unit["sec"],
                           "guide": unit["guide"], "parts": keys})

    (out_dir / "_order.json").write_text(json.dumps(order, indent=1) + "\n", encoding="utf-8")
    (DATA / "units").mkdir(exist_ok=True)
    (DATA / "units" / f"c{ch}.json").write_text(json.dumps(units_spec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Ch{ch}: {len(order)} part files, {len(units_spec)} units -> data/parts/c{ch}/")
    print("  order:", " ".join(order))


if __name__ == "__main__":
    migrate(int(sys.argv[1]))
