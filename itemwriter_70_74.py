#!/usr/bin/env python3
"""Helper: write page-anchored part files for Ch 70-74 from compact tuples.

Each item tuple: (fmt, question, [correct, d1, d2, d3], explanation_without_citation)
The correct option is listed FIRST; author.py rotates options deterministically.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / "data" / "parts"


def write_part(ch: int, key: str, page: int, sec: str, items: list[tuple]) -> None:
    out = []
    for fmt, q, opts, exp in items:
        assert len(opts) == 4, (key, q)
        assert len({o.casefold() for o in opts}) == 4, (key, q)
        out.append({"fmt": fmt, "q": q, "opts": list(opts), "ans": 0,
                    "exp": f"{exp.rstrip()} (Book p{page})"})
    d = PARTS / f"c{ch}"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{key}.json").write_text(
        json.dumps({"page": page, "sec": sec, "items": out}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")
    print(f"c{ch}/{key}: {len(out)} items")


def write_units(ch: int, units: list[dict]) -> None:
    (ROOT / "data" / "units" / f"c{ch}.json").write_text(
        json.dumps(units, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
