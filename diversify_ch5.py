#!/usr/bin/env python3
"""Permute Ch 5 match key lists so correct-option key strings differ between items.

Same relabel algorithm as diversify_keys.py (hash-seeded permutation of the
A/B/C labels inside match stems), applied once to the rebuilt data/ch05.json.
Option shuffling only: stems keep their numbered lists and descriptions; each
option's key string is remapped consistently and the answer keeps its index.
Re-run write_ch05_manifest.py afterwards to refresh contentSha256.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FULL = re.compile(r"^(\d+-[A-E](?:, )?)+$")


def permutations(letters):
    return [p for p in itertools.permutations(letters) if p != tuple(letters)]


def relabel(stem: str, opts: list[str], qid: str):
    head, sep, tail = stem.rpartition("… ")
    if not sep:
        return None  # refuse to touch stems without the standard separator
    order = [m.group(1) for m in re.finditer(r"\b([A-E])\)", tail)]
    if not order or any(not FULL.match(o.strip()) for o in opts):
        return None
    if len(set(order)) != len(order):
        return None
    seed = int(hashlib.sha256(qid.encode()).hexdigest(), 16)
    perms = permutations(order)
    new_order = list(perms[seed % len(perms)])
    mapping = dict(zip(order, new_order))
    marks = list(re.finditer(r"\b([A-E])\)", tail))
    entries = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(tail)
        new_label = mapping[m.group(1)]
        entries.append((new_label, new_label + ")" + tail[m.end():end].rstrip()))
    entries.sort(key=lambda e: e[0])
    new_tail = "  ".join(text for _label, text in entries)
    new_opts = [re.sub(r"(?<=-)([A-E])", lambda m: mapping[m.group(1)], o) for o in opts]
    return head + sep + new_tail, new_opts


def main() -> None:
    path = ROOT / "data" / "ch05.json"
    chapter = json.loads(path.read_text())
    changed = 0
    for q in chapter["questions"]:
        stem = q["q"].replace(" ... ", " … ")
        result = relabel(stem, list(q["opts"]), q["id"])
        if result:
            q["q"], q["opts"] = result
        elif stem != q["q"]:
            q["q"] = stem
        if result or stem != q["q"]:
            changed += 1
    # sanity: answer content unchanged, four distinct options, citations intact
    for q in chapter["questions"]:
        assert len(q["opts"]) == 4 and len({o.strip().casefold() for o in q["opts"]}) == 4, q["id"]
        assert q["exp"].endswith(f"(Book p{q['page']})"), q["id"]
    path.write_text(json.dumps(chapter, ensure_ascii=False, indent=2) + "\n")
    print(f"diversify_ch5: relabelled/normalised {changed} items")


if __name__ == "__main__":
    main()
