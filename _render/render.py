import sys, pymupdf
# usage: render.py <pdf> <first_pdfpage> <last_pdfpage> <K> <zoom>
pdf, a, b, K, zoom = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
d = pymupdf.open(pdf)
mat = pymupdf.Matrix(zoom, zoom)
for n in range(a, b+1):
    p = d[n-1]
    pix = p.get_pixmap(matrix=mat, clip=pymupdf.Rect(p.rect.x0, p.rect.y0+28, p.rect.x1, p.rect.y1-28))
    out = f"_render/_{K+n}.png"   # name = book page
    pix.save(out)
    print(out, pix.width, pix.height)
