#!/usr/bin/env python3
"""Relabel the keyed lists inside match-the-following stems.

Authored match items all used the natural 'A, B, C' order against '1, 2, 3', so
the correct option was textually the same permutation in dozens of items. This
relabels each item's key list with a permutation seeded by its stable id, so the
correct option string differs from item to item while the content is unchanged.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / "data" / "parts"
LETTER = "ABCDE"
FULL = re.compile(r"^(\d+-[A-E](?:, )?)+$")


def permutations(letters):
    perms = [p for p in itertools.permutations(letters) if p != tuple(letters)]
    return perms


def relabel(stem: str, opts: list[str], qid: str):
    head, sep, tail = stem.rpartition("… ")
    if not sep:
        head, tail = "", stem
    order = [m.group(1) for m in re.finditer(r"\b([A-E])\)", tail)]
    if not order or any(not FULL.match(o.strip()) for o in opts):
        return None
    if len(set(order)) != len(order):
        return None
    seed = int(hashlib.sha256(qid.encode()).hexdigest(), 16)
    perms = permutations(order)
    new_order = list(perms[seed % len(perms)])
    mapping = dict(zip(order, new_order))
    # split the keyed list into its lettered entries and re-emit them so the
    # page still reads A) ... B) ... C) ..., only with the labels permuted
    marks = list(re.finditer(r"\b([A-E])\)", tail))
    entries = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(tail)
        new_label = mapping[m.group(1)]
        entries.append((new_label, new_label + ")" + tail[m.end():end].rstrip()))
    entries.sort(key=lambda e: e[0])
    new_tail = "  ".join(text for _label, text in entries)
    new_opts = []
    for o in opts:
        new_opts.append(re.sub(r"(?<=-)([A-E])", lambda m: mapping[m.group(1)], o))
    return head + sep + new_tail, new_opts


def main() -> None:
    changed = 0
    for path in sorted(PARTS.glob("c1[3-8]/*.json")):
        if path.name == "_order.json":
            continue
        part = json.loads(path.read_text(encoding="utf-8"))
        touched = False
        for idx, item in enumerate(part["items"]):
            if item["fmt"] != "match":
                continue
            qid = f"{path.name}:{idx}"
            out = relabel(item["q"], item["opts"], qid)
            if not out or out[1] == item["opts"]:
                continue
            item["q"], item["opts"] = out
            touched = True
            changed += 1
        if touched:
            path.write_text(json.dumps(part, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"relabelled key mappings in {changed} match items")


if __name__ == "__main__":
    main()
