#!/usr/bin/env python3
"""Rewrite selected items inside the page-anchored part files of a chapter.

    python3 patch_items.py <chapter> <patch.json>

The patch file is a list of objects keyed by the MED id of the item being
replaced:  {"id": "MED-C11-012", "fmt": "oddoneout", "q": "...", "opts": [correct,
d1, d2, d3], "exp": "..."}  — opts follow the authoring convention (correct first);
the explanation is copied from the existing item whenever it is omitted, so a
format change never alters the page-cited fact it teaches.  The tool recomputes
ids exactly as author.py does, so ids stay stable as long as ordering is unchanged.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / "data" / "parts"


def main(ch: int, patch_path: str) -> None:
    d = PARTS / f"c{ch}"
    order = json.loads((d / "_order.json").read_text(encoding="utf-8"))
    index: dict[str, tuple[str, int]] = {}
    n = 0
    for key in order:
        blob = json.loads((d / f"{key}.json").read_text(encoding="utf-8"))
        for i in range(len(blob["items"])):
            n += 1
            index[f"MED-C{ch}-{n:03d}"] = (key, i)

    patches = json.loads(Path(patch_path).read_text(encoding="utf-8"))
    touched: dict[str, dict] = {}
    done = 0
    for patch in patches:
        loc = index.get(patch["id"])
        if loc is None:
            sys.exit(f"unknown id {patch['id']}")
        key, i = loc
        blob = touched.get(key) or json.loads((d / f"{key}.json").read_text(encoding="utf-8"))
        item = blob["items"][i]
        new = {
            "fmt": patch.get("fmt", item["fmt"]),
            "q": patch.get("q", item["q"]),
            "opts": patch.get("opts", item["opts"]),
            "ans": 0,
            "exp": patch.get("exp", item["exp"]),
        }
        if "page" in item:
            new["page"] = item["page"]
        if "sec" in item:
            new["sec"] = item["sec"]
        blob["items"][i] = new
        touched[key] = blob
        done += 1
    for key, blob in touched.items():
        (d / f"{key}.json").write_text(json.dumps(blob, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Ch{ch}: patched {done} item(s) across {len(touched)} part file(s)")


if __name__ == "__main__":
    main(int(sys.argv[1]), sys.argv[2])
