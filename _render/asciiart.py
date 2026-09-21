#!/usr/bin/env python3
"""Print a high-zoom crop of a book page as ASCII art (no image vision needed).

usage: python3 _render/asciiart.py <bookpage> <x0> <y0> <x1> <y1> [width] [zoom]
Coordinates are PDF points (page 595 x 842).
"""
import sys
from pathlib import Path

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "uploads" / "Medicine_Vol3_Part6_pages_1035-1070.pdf"
K = 1034

RAMP = " .:-=+*#%@"


def art(bp, x0, y0, x1, y1, width=180, zoom=12.0, invert=True):
    d = pymupdf.open(str(PDF))
    p = d[bp - K - 1]
    pix = p.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom),
                       clip=pymupdf.Rect(x0, y0, x1, y1))
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
    w = int(width)
    h = max(1, int(img.height / img.width * w * 0.5))
    img = img.resize((w, h), Image.LANCZOS)
    px = img.load()
    lines = []
    for yy in range(h):
        row = []
        for xx in range(w):
            v = px[xx, yy]
            v = 255 - v if invert else v  # dark ink -> high value
            row.append(RAMP[min(len(RAMP) - 1, v * len(RAMP) // 256)])
        lines.append("".join(row))
    return lines


if __name__ == "__main__":
    bp = int(sys.argv[1])
    x0, y0, x1, y1 = (float(v) for v in sys.argv[2:6])
    width = int(sys.argv[6]) if len(sys.argv) > 6 else 180
    zoom = float(sys.argv[7]) if len(sys.argv) > 7 else 12.0
    print("\n".join(art(bp, x0, y0, x1, y1, width, zoom)))
