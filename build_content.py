#!/usr/bin/env python3
"""Embed the chapter JSON artifacts into the standalone PULSE Medicine app.

The browser app is intentionally a single offline HTML file.  Structured chapter
artifacts in data/chNN.json are the editable source of truth; run this script
whenever a chapter artifact changes.  Chapters without an artifact remain on
the roadmap as "Soon" (live: false).
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_PATH = ROOT / "pulse-medicine.html"
DATA_PATH = ROOT / "data"

# Full Volume-3 roadmap (Book p705-1068) from the book's Contents pages,
# cross-verified against the scanned chapter title pages.  Number, title,
# starting Book page.  The "p" shown on the roadmap is the starting page.
CHAPTERS = [
    (1, "Development of Kidneys", 705),
    (2, "Gross Anatomy of Kidney", 711),
    (3, "Tubular Anatomy", 717),
    (4, "Juxtaglomerular Apparatus", 726),
    (5, "Glomerulus - Anatomy", 730),
    (6, "Renal Physiology", 734),
    (7, "Urine Analysis", 740),
    (8, "Basic Approach to Kidney Disease and Renal Artery Stenosis", 748),
    (9, "Thrombotic Microangiopathy", 753),
    (10, "Glomerular Disease - Patterns", 756),
    (11, "Podocytopathies", 762),
    (12, "MPGN and IgA Nephropathy", 770),
    (13, "Post Streptococcal Glomerulonephritis", 775),
    (14, "RPGN and Pulmonary Renal Syndrome", 778),
    (15, "Familial Glomerular Syndromes", 783),
    (16, "Ciliopathies", 786),
    (17, "Chronic Tubulointerstitial Disease", 793),
    (18, "Acute Kidney Injury", 796),
    (19, "Chronic Kidney Disease", 805),
    (20, "Anemia in Chronic Kidney Disease", 808),
    (21, "CKD - Calciphylaxis and Cardiovascular changes", 811),
    (22, "Diabetic Kidney Disease", 815),
    (23, "Introduction to Acid Base Analysis", 819),
    (24, "Metabolic Alkalosis", 824),
    (25, "Methodology and Interpretation of ABG Analysis", 826),
    (26, "Overview of Hormones", 830),
    (27, "Physiology of Adrenal Cortex", 837),
    (28, "Conn's Syndrome", 841),
    (29, "Cushing's Syndrome", 844),
    (30, "Addison's Disease", 849),
    (31, "Adrenal Medulla : Part 1", 852),
    (32, "Adrenal Medulla : Part 2", 858),
    (33, "Basics of Bone and Mineral Metabolism", 863),
    (34, "Calcium Metabolism", 874),
    (35, "Hypercalcemia", 877),
    (36, "Hypocalcemia", 883),
    (37, "Phosphorus Metabolism", 887),
    (38, "Magnesium Metabolism", 892),
    (39, "Osteoporosis", 895),
    (40, "Basics of Thyroid Gland", 898),
    (41, "Thyroid Function Tests", 902),
    (42, "Hypothyroidism", 905),
    (43, "Thyrotoxicosis and Thyroiditis", 910),
    (44, "Introduction to Diabetes Mellitus and Classification", 917),
    (45, "Insulin Physiology and Acute Complications of Diabetes Mellitus", 927),
    (46, "Management of Diabetes Mellitus - 2024 Guidelines", 933),
    (47, "Basics of Pituitary Gland", 936),
    (48, "Prolactin", 941),
    (49, "Growth Hormone", 945),
    (50, "Acquired Hypopituitarism", 952),
    (51, "Antidiuretic Hormone", 958),
    (52, "Hyponatremia", 962),
    (53, "Polyuria", 965),
    (54, "Potassium Metabolism", 968),
    (55, "Management of Hypertension - 2023 Guidelines", 976),
    (56, "Basics of Development and Anatomy of Liver", 982),
    (57, "Basics of Physiology of Liver", 986),
    (58, "Acute Hepatitis and Acute Liver Failure", 993),
    (59, "Chronic Hepatitis - Cirrhosis", 997),
    (60, "Portal Hypertension", 1001),
    (61, "Ascites and Hepatorenal Syndrome", 1005),
    (62, "Hepatic Encephalopathy", 1010),
    (63, "Metabolic Diseases of Liver", 1013),
    (64, "Biliary Cirrhosis", 1020),
    (65, "Autoimmune Hepatitis", 1023),
    (66, "Alcoholic Liver Disease", 1026),
    (67, "Nonalcoholic Steatohepatitis", 1030),
    (68, "Vascular Diseases of Liver", 1033),
    (69, "Hepatitis B Virus : Part 1", 1036),
    (70, "Hepatitis B Virus : Part 2", 1039),
    (71, "Hepatitis C Virus", 1045),
    (72, "Infective Endocarditis", 1047),
    (73, "Tropical Infections: Synopsis", 1053),
    (74, "HIV", 1061),
]


def compact(value: object) -> str:
    """Use compact, UTF-8 JSON so the standalone app remains easy to ship."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def between(text: str, start: str, end: str) -> tuple[int, int]:
    first = text.index(start)
    second = text.index(end, first)
    return first, second


def main() -> None:
    # Never ship changed content under stale source-review evidence.
    from check_source_coverage import audit as audit_source_coverage
    _rows, review_errors = audit_source_coverage(ROOT)
    if review_errors:
        raise ValueError("Source-review evidence is invalid:\n" + "\n".join(review_errors))
    expected = {number: (title, page) for number, title, page in CHAPTERS}
    questions: list[dict] = []
    units: list[dict] = []
    live: dict[int, dict] = {}

    for number, title, start_page in CHAPTERS:
        path = DATA_PATH / f"ch{number:02d}.json"
        if not path.exists():
            continue
        chapter = json.loads(path.read_text(encoding="utf-8"))
        if chapter["chapter"] != number:
            raise ValueError(f"{path.name}: chapter number does not match filename")
        if chapter["title"] != title:
            raise ValueError(
                f"{path.name}: expected title {title!r}, got {chapter['title']!r}"
            )
        first = int(chapter["pageRange"].split("-", 1)[0])
        if first != start_page:
            raise ValueError(
                f"{path.name}: pageRange starts at {first}, expected {start_page}"
            )
        questions.extend(chapter["questions"])
        units.extend(chapter["units"])
        live[number] = chapter

    html = APP_PATH.read_text(encoding="utf-8")
    q_start, _ = between(html, "const QUESTIONS = ", "\nconst UNITS = ")
    u_start, _ = between(html, "const UNITS = ", "\nconst CHAPTERS = ")
    c_start, c_end = between(html, "const CHAPTERS = ", "\nconst QBYID = ")

    roadmap = []
    for number, title, start_page in CHAPTERS:
        if number in live:
            first = int(live[number]["pageRange"].split("-", 1)[0])
            roadmap.append({"n": number, "t": title, "p": first, "live": True})
        else:
            roadmap.append({"n": number, "t": title, "p": start_page, "live": False})

    html = (
        html[:q_start]
        + "const QUESTIONS = "
        + compact(questions)
        + ";\nconst UNITS = "
        + compact(units)
        + ";\nconst CHAPTERS = "
        + json.dumps(roadmap, ensure_ascii=False, indent=2)
        + ";"
        + html[c_end:]
    )
    APP_PATH.write_text(html, encoding="utf-8")
    live_count = len(live)
    print(
        f"Embedded {len(questions)} questions and {len(units)} units across "
        f"{live_count} live chapter(s) of {len(CHAPTERS)} roadmap chapters "
        f"in {APP_PATH.name}."
    )


if __name__ == "__main__":
    main()
