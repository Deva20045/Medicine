#!/usr/bin/env python3
"""Shared book-page -> source-PDF mapping for _render tools.

Book page = PDF page + K (K per part file). All six parts cover Book p705-1070.
"""
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

SOURCE_PARTS = (
    (705, 759, 692, "Medicine_Vol3_Part1_pages_705-759.pdf"),
    (760, 823, 759, "Medicine_Vol3_Part2_pages_760-823.pdf"),
    (824, 893, 823, "Medicine_Vol3_Part3_pages_824-893.pdf"),
    (894, 964, 893, "Medicine_Vol3_Part4_pages_894-964.pdf"),
    (965, 1034, 964, "Medicine_Vol3_Part5_pages_965-1034.pdf"),
    (1035, 1070, 1034, "Medicine_Vol3_Part6_pages_1035-1070.pdf"),
)


def part_for(bookpage: int) -> tuple[pathlib.Path, int]:
    """Return (pdf_path, K) for a book page; raises ValueError if out of range."""
    for first, last, k, name in SOURCE_PARTS:
        if first <= bookpage <= last:
            return ROOT / "uploads" / name, k
    raise ValueError(f"book page {bookpage} outside scanned range 705-1070")
