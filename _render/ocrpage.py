#!/usr/bin/env python3
"""Render a book page from the Part-6 scan and OCR it into ordered lines.

usage: python3 _render/ocrpage.py <bookpage> [zoom]
Writes  _render/_<bookpage>.png  and prints ordered lines as "y  x  | text".
The scan has no text layer, so this is the only way to read it here; treat low
confidence / garbled numbers as UNCERTAIN and re-render a zoomed crop.
"""
import sys
from pathlib import Path

import pymupdf
from rapidocr_onnxruntime import RapidOCR

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "uploads" / "Medicine_Vol3_Part6_pages_1035-1070.pdf"
K = 1034

_ocr = None


def get_ocr():
    global _ocr
    if _ocr is None:
        _ocr = RapidOCR()
    return _ocr


def render(bookpage, zoom=3.0, clip=None):
    d = pymupdf.open(str(PDF))
    p = d[bookpage - K - 1]
    mat = pymupdf.Matrix(zoom, zoom)
    if clip is None:
        clip = pymupdf.Rect(p.rect.x0, p.rect.y0 + 28, p.rect.x1, p.rect.y1 - 28)
    pix = p.get_pixmap(matrix=mat, clip=clip)
    out = ROOT / "_render" / f"_{bookpage}.png"
    pix.save(out)
    return out


def ocr_lines(img, ytol=14):
    res, _ = get_ocr()(str(img))
    if not res:
        return []
    items = []
    for box, text, score in res:
        xs = [pt[0] for pt in box]
        ys = [pt[1] for pt in box]
        items.append({"x0": min(xs), "y0": min(ys), "x1": max(xs), "y1": max(ys),
                      "t": text, "s": score})
    items.sort(key=lambda it: (it["y0"], it["x0"]))
    lines = []
    for it in items:
        placed = False
        for ln in lines:
            if abs(ln["y"] - it["y0"]) <= ytol:
                ln["items"].append(it)
                ln["y"] = sum(i["y0"] for i in ln["items"]) / len(ln["items"])
                placed = True
                break
        if not placed:
            lines.append({"y": it["y0"], "items": [it]})
    lines.sort(key=lambda ln: ln["y"])
    out = []
    for ln in lines:
        ln["items"].sort(key=lambda i: i["x0"])
        out.append(ln)
    return out


def render_crop(bookpage, x0, y0, x1, y1, zoom=6.0, tag="crop"):
    """Render a sub-rectangle (PDF-point coords) of a book page at high zoom."""
    d = pymupdf.open(str(PDF))
    p = d[bookpage - K - 1]
    mat = pymupdf.Matrix(zoom, zoom)
    clip = pymupdf.Rect(x0, y0, x1, y1)
    pix = p.get_pixmap(matrix=mat, clip=clip)
    out = ROOT / "_render" / f"_{bookpage}_{tag}.png"
    pix.save(out)
    return out


if __name__ == "__main__":
    bp = int(sys.argv[1])
    if len(sys.argv) > 5:
        # crop mode: bookpage zoom tag x0 y0 x1 y1
        zoom = float(sys.argv[2]); tag = sys.argv[3]
        x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8])
        img = render_crop(bp, x0, y0, x1, y1, zoom, tag)
    else:
        zoom = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
        img = render(bp, zoom)
    for ln in ocr_lines(img):
        for it in ln["items"]:
            print(f"{int(it['y0']):5d} {int(it['x0']):5d} | {it['t']} | {it['s']:.2f}")
        print("--")
