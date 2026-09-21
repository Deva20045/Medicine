#!/usr/bin/env python3
"""OCR-dump a range of book pages (single RapidOCR load) -> /tmp/ocr/<page>.txt

Each line:  <y> <x> | <text> | <confidence>   (y is clip-relative: pdf_y = y + 28)
Groups of tokens on the same visual row are separated by a `--` marker.
"""
from __future__ import annotations

import pathlib
import sys

import numpy as np
import pymupdf
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / "uploads" / "Medicine_Vol3_Part6_pages_1035-1070.pdf"
K = 1034
HEADER = 28.0
ZOOM = 3.0


def main():
    first, last = int(sys.argv[1]), int(sys.argv[2])
    ocr = RapidOCR()
    doc = pymupdf.open(str(PDF))
    out_dir = pathlib.Path(__file__).resolve().parent / "ocr"
    out_dir.mkdir(exist_ok=True)
    for bp in range(first, last + 1):
        page = doc[bp - K - 1]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(ZOOM, ZOOM),
                              clip=pymupdf.Rect(page.rect.x0, page.rect.y0 + HEADER,
                                                page.rect.x1, page.rect.y1 - 28))
        img = np.asarray(Image.frombytes("RGB", (pix.width, pix.height), pix.samples))
        res, _ = ocr(img)
        items = []
        for box, text, score in (res or []):
            xs = [q[0] for q in box]
            ys = [q[1] for q in box]
            items.append({"x": min(xs) / ZOOM, "y": min(ys) / ZOOM,
                          "x2": max(xs) / ZOOM, "t": text, "s": score})
        items.sort(key=lambda it: (it["y"], it["x"]))
        lines = []
        for it in items:
            placed = False
            for ln in lines:
                if abs(ln["y"] - it["y"]) <= 12:
                    ln["items"].append(it)
                    ln["y"] = sum(i["y"] for i in ln["items"]) / len(ln["items"])
                    placed = True
                    break
            if not placed:
                lines.append({"y": it["y"], "items": [it]})
        lines.sort(key=lambda ln: ln["y"])
        out = out_dir / f"{bp}.txt"
        with out.open("w", encoding="utf-8") as f:
            for ln in lines:
                ln["items"].sort(key=lambda i: i["x"])
                for it in ln["items"]:
                    f.write(f"{int(it['y']):4d} {int(it['x']):4d}-{int(it['x2']):3d} | "
                            f"{it['t']} | {it['s']:.2f}\n")
                f.write("--\n")
        print(f"p{bp}: {len(items)} tokens -> {out.name}", flush=True)


if __name__ == "__main__":
    main()
