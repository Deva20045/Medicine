#!/usr/bin/env python3
"""Rebuild Ch 7 (Urine Analysis, p740-747) in strict source order.

Source review 2026-09-22: all eight pages read from the Part 1 scan (PDF pp48-55)
at 2x whole-page plus 6x crops of every table row and number; every stored
answer index checked against the print (all 135 were correct - this chapter was
authored answer-first natively, unlike Ch 6).

Repairs (see REAUDIT_CH7_SOURCE_ORDER.md):
  * FACT: old MED-C7-033 / 039 taught diabetes insipidus at urine osmolality
    '< 300 mOsm/kg'; the abnormal-values table prints '< 200 mOsm/kg'. Fixed.
  * Within-page order faults on every page re-sequenced to the recorded traversal
    (appearance-table rows 1-2 were tested after rows 3-7; odour rows, the
    other-properties rows, the p742 flowchart branches, the p743 figure/table,
    the p744 uromodulin bullets and both tables, p745 captions, p746 cast rows
    and p747 crystal panels were all out of printed order).
  * Uncovered elements given items: 'Brown - Nitrofurantoin' row; the
    'Collection of urine', 'Normal urine colour' and 'High coloured urine'
    captions; 'Positive -> Blood in urine'.
Result: 140 questions in the same 10 unit IDs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = json.loads((ROOT / "data" / "ch07.json").read_text())
if len(OLD["questions"]) != 135 or "Source-order revision" in OLD["units"][0].get("guide", ""):
    raise SystemExit("author_c7_review.py expects the pre-review 135-question data/ch07.json; refusing to re-run.")
BY_ID = {q["id"]: dict(q) for q in OLD["questions"]}

REVISION = ("Source-order revision, 22 Sep 2026: questions were reordered to the printed "
            "sequence, one wrong value (<200 mOsm/kg) corrected and missing captions/rows added. "
            "Previous completion badges and XP are retained; replay this unit. ")


def keep(old_id, **over):
    q = dict(BY_ID[old_id]); q.update(over); return q


def new(sec, page, fmt, q, opts, ans, exp):
    return {"id": None, "sec": sec, "page": page, "q": q, "opts": opts, "ans": ans, "exp": exp, "fmt": fmt}


def sub_opt(q, old, new_text):
    q["opts"] = [new_text if o == old else o for o in q["opts"]]
    return q


S1 = "Urine Collection · p740"
S2 = "Physical Properties: appearance · p740"
S3 = "Physical Properties: odour · p740-741"
S4 = "Other properties & clinical significance · p741"
S5 = "High Colored Urine · p742"
S6 = "Types of RBC & dipstick parameters · p743"
S7 = "Proteinuria · p744"
S8 = "Microscopic Examination · p745"
S9 = "Casts in urine · p746"
S10 = "Crystals in urine · p747"

# ---- osmolality fix (print: < 200 mOsm/kg) ----
q033 = keep("MED-C7-033", sec=S4,
            q="Diabetes insipidus (↑ dilute urine) is flagged in the abnormal-values table when urine specific gravity and urine osmolality fall below:",
            opts=["1.005 and 200 mOsm/kg", "1.010 and 500 mOsm/kg", "1.003 and 300 mOsm/kg", "1.015 and 400 mOsm/kg"], ans=0,
            exp="Rows 2-3 read: urine specific gravity < 1.005; urine osmolality < 200 mOsm/kg → Diabetes insipidus (↑ dilute urine). The earlier bank printed 300; the scan shows 200. (Book p741)")
q039 = keep("MED-C7-039", sec=S4)
q039 = sub_opt(q039, "Diabetes insipidus — specific gravity <1.005 and osmolality <300 mOsm/kg",
               "Diabetes insipidus — specific gravity <1.005 and osmolality <200 mOsm/kg")
q039["q"] = "A patient with 4 L/day of dilute urine has urine osmolality 150 mOsm/kg and specific gravity 1.003, with a normal serum creatinine. Which row of the abnormal-values table does this match?"
q039["exp"] = "The table flags diabetes insipidus (↑ dilute urine) when urine specific gravity falls below 1.005 and osmolality below 200 mOsm/kg; isosthenuria instead equals blood parameters and points to ATN/CTID. (Book p741)"

seq = [
    # ---------------- p740 ----------------
    keep("MED-C7-001", sec=S1), keep("MED-C7-002", sec=S1), keep("MED-C7-004", sec=S1), keep("MED-C7-003", sec=S1),
    keep("MED-C7-005", sec=S1), keep("MED-C7-006", sec=S1), keep("MED-C7-007", sec=S1),
    new(S1, 740, "recall", "The photograph beside the collection instructions, showing gloved hands with a specimen, is captioned:",
        ["Collection of urine", "Midstream technique", "Catheterised patient", "Urobag sampling"], 0,
        "The photo to the right of the 'Instructions: To Avoid' list carries the caption 'Collection of urine'. (Book p740)"),
    keep("MED-C7-012", sec=S2), keep("MED-C7-009", sec=S2), keep("MED-C7-010", sec=S2), keep("MED-C7-013", sec=S2),
    new(S2, 740, "fillup", "Fill up: In the APPEARANCE table, brown urine is attributed to ______.",
        ["Nitrofurantoin", "Rifampicin", "Triamterene", "Imipenem + cilastatin"], 0,
        "Row 6 of the table: Brown — Nitrofurantoin. (Book p740)"),
    keep("MED-C7-014", sec=S2), keep("MED-C7-015", sec=S2), keep("MED-C7-008", sec=S2), keep("MED-C7-011", sec=S2),
    new(S2, 740, "recall", "The jar photographed beside the appearance table is captioned:",
        ["Normal urine colour", "High coloured urine", "Pale/white urine", "Collection of urine"], 0,
        "The photo of a jar of light-yellow urine to the right of the colour table is captioned 'Normal urine colour'; 'High coloured urine' is the p742 photo. (Book p740)"),
    keep("MED-C7-016", sec=S3), keep("MED-C7-017", sec=S3), keep("MED-C7-018", sec=S3),
    # ---------------- p741 ----------------
    keep("MED-C7-023", sec=S3), keep("MED-C7-022", sec=S3), keep("MED-C7-021", sec=S3), keep("MED-C7-025", sec=S3),
    keep("MED-C7-020", sec=S3), keep("MED-C7-024", sec=S3), keep("MED-C7-019", sec=S3),
    keep("MED-C7-036", sec=S4), keep("MED-C7-035", sec=S4), keep("MED-C7-027", sec=S4), keep("MED-C7-026", sec=S4),
    keep("MED-C7-028", sec=S4), keep("MED-C7-037", sec=S4), keep("MED-C7-029", sec=S4), keep("MED-C7-030", sec=S4),
    keep("MED-C7-031", sec=S4), keep("MED-C7-038", sec=S4),
    keep("MED-C7-032", sec=S4), q033, q039, keep("MED-C7-034", sec=S4),
    # ---------------- p742 ----------------
    keep("MED-C7-040", sec=S5), keep("MED-C7-059", sec=S5),
    new(S5, 742, "recall", "The photograph of a dark-brown specimen jar at the top right of this page is captioned:",
        ["High coloured urine", "Cola coloured urine", "Normal urine colour", "Hematuria"], 0,
        "Caption under the jar photo: 'High coloured urine'. (Book p742)"),
    keep("MED-C7-041", sec=S5), keep("MED-C7-042", sec=S5), keep("MED-C7-043", sec=S5), keep("MED-C7-056", sec=S5),
    new(S5, 742, "fillup", "Fill up: In the approach, a positive dipstick test is followed by the box '______ in urine'.",
        ["Blood", "Myoglobin", "Porphyrin", "Protein"], 0,
        "1. Dipstick test → Positive → 'Blood in urine' → 2. Centrifugation; the Negative branch lists porphyria and ↑ beetroot intake. (Book p742)"),
    keep("MED-C7-044", sec=S5), keep("MED-C7-045", sec=S5), keep("MED-C7-046", sec=S5),
    keep("MED-C7-047", sec=S5), keep("MED-C7-048", sec=S5), keep("MED-C7-057", sec=S5),
    keep("MED-C7-049", sec=S5), keep("MED-C7-050", sec=S5), keep("MED-C7-051", sec=S5), keep("MED-C7-058", sec=S5),
    keep("MED-C7-052", sec=S5), keep("MED-C7-053", sec=S5), keep("MED-C7-054", sec=S5), keep("MED-C7-055", sec=S5),
    # ---------------- p743 ----------------
    keep("MED-C7-068", sec=S6), keep("MED-C7-069", sec=S6), keep("MED-C7-061", sec=S6), keep("MED-C7-060", sec=S6),
    keep("MED-C7-062", sec=S6), keep("MED-C7-071", sec=S6), keep("MED-C7-063", sec=S6),
    keep("MED-C7-065", sec=S6), keep("MED-C7-064", sec=S6), keep("MED-C7-070", sec=S6), keep("MED-C7-073", sec=S6),
    keep("MED-C7-066", sec=S6), keep("MED-C7-072", sec=S6), keep("MED-C7-067", sec=S6),
    # ---------------- p744 ----------------
    keep("MED-C7-075", sec=S7), keep("MED-C7-076", sec=S7), keep("MED-C7-074", sec=S7),
    keep("MED-C7-077", sec=S7), keep("MED-C7-078", sec=S7), keep("MED-C7-087", sec=S7), keep("MED-C7-085", sec=S7), keep("MED-C7-079", sec=S7),
    keep("MED-C7-080", sec=S7), keep("MED-C7-091", sec=S7), keep("MED-C7-081", sec=S7), keep("MED-C7-088", sec=S7), keep("MED-C7-082", sec=S7),
    keep("MED-C7-089", sec=S7), keep("MED-C7-083", sec=S7), keep("MED-C7-090", sec=S7), keep("MED-C7-084", sec=S7), keep("MED-C7-086", sec=S7),
    # ---------------- p745 ----------------
    keep("MED-C7-092", sec=S8), keep("MED-C7-097", sec=S8), keep("MED-C7-096", sec=S8), keep("MED-C7-105", sec=S8), keep("MED-C7-093", sec=S8),
    keep("MED-C7-094", sec=S8), keep("MED-C7-103", sec=S8), keep("MED-C7-095", sec=S8), keep("MED-C7-102", sec=S8), keep("MED-C7-104", sec=S8),
    keep("MED-C7-098", sec=S8), keep("MED-C7-100", sec=S8), keep("MED-C7-106", sec=S8), keep("MED-C7-101", sec=S8), keep("MED-C7-099", sec=S8),
    # ---------------- p746 ----------------
    keep("MED-C7-108", sec=S9), keep("MED-C7-113", sec=S9), keep("MED-C7-122", sec=S9),
    keep("MED-C7-115", sec=S9), keep("MED-C7-119", sec=S9),
    keep("MED-C7-109", sec=S9), keep("MED-C7-114", sec=S9), keep("MED-C7-121", sec=S9), keep("MED-C7-120", sec=S9),
    keep("MED-C7-110", sec=S9), keep("MED-C7-118", sec=S9), keep("MED-C7-117", sec=S9), keep("MED-C7-107", sec=S9),
    keep("MED-C7-112", sec=S9), keep("MED-C7-111", sec=S9), keep("MED-C7-116", sec=S9),
    # ---------------- p747 ----------------
    keep("MED-C7-135", sec=S10), keep("MED-C7-127", sec=S10), keep("MED-C7-131", sec=S10), keep("MED-C7-130", sec=S10),
    keep("MED-C7-126", sec=S10), keep("MED-C7-125", sec=S10), keep("MED-C7-123", sec=S10), keep("MED-C7-132", sec=S10), keep("MED-C7-133", sec=S10),
    keep("MED-C7-128", sec=S10), keep("MED-C7-129", sec=S10), keep("MED-C7-124", sec=S10), keep("MED-C7-134", sec=S10),
]

assert len(seq) == 140, len(seq)
used = [q["id"] for q in seq if q["id"]]
assert len(set(used)) == len(used) == 135, (len(set(used)), len(used))

questions = []
for i, q in enumerate(seq, 1):
    q["id"] = f"MED-C7-{i:03d}"; questions.append(q)

unit_specs = [
    ("MED-U7-1", "Urine collection, analysis window & preservatives", S1,
     "Sample, analysis window, preservatives, storage, the two things to avoid, the two catheter rules and the photo caption, in printed order.", 1, 8),
    ("MED-U7-2", "Appearance: colour table & its drug causes", S2,
     "The seven colour rows top-to-bottom (light yellow, pale/white, pink, darkening on standing, green, brown, orange) and the jar caption.", 9, 18),
    ("MED-U7-3", "Odour table: metabolic diseases and their smells", S3,
     "Pungent, musty/mousy, curry/maple syrup, sweaty feet (p740), then cabbage-like/rancid butter, cat urine, acid, fish, sulfurous, sweet, swimming pool (p741).", 19, 28),
    ("MED-U7-4", "Other properties, acidification & concentration", S4,
     "pH, specific gravity and osmolality rows; the α-intercalated-cell diagram; the three concentration bullets; the abnormal-values table (Type-1 RTA, DI at <1.005 and <200 mOsm/kg, isosthenuria).", 29, 42),
    ("MED-U7-5", "High-coloured urine: causes & the dipstick–spin–biopsy approach", S5,
     "Presentation line and photo; the 90/9/1 causes; dipstick positive/negative; centrifugation; clear → RBC → glomerular criteria → biopsy → IgA, urological → imaging; high-coloured → 3–6 h → fades/persists.", 43, 64),
    ("MED-U7-6", "RBC morphology & the dipstick parameter table", S6,
     "Urological (crenated, isomorphic) then nephrological (dysmorphic, acanthocytes/Mickey mouse); the dipstick rows with conditions; the leucocyte-test factors.", 65, 78),
    ("MED-U7-7", "Proteinuria: uromodulin, cut-offs, albumin & tests", S7,
     "Uromodulin's four bullets; the protein-levels table row by row; the albumin injury chain; the albumin table; moderately elevated albumin; the four tests with the dipstick's disadvantages.", 79, 96),
    ("MED-U7-8", "Microscopy: cells, Maltese cross & cast formation", S8,
     "Cell size; the four photographs and captions; the polarizing-microscope list (blood: babesiosis; kidney: four causes); cast formation in the DCT; hyaline, coarse and fine granular rows.", 97, 111),
    ("MED-U7-9", "Casts and their clinical associations", S9,
     "Pigment fine granular, RBC, WBC, tubular epithelial (muddy brown), broad/waxy, fatty, eosinophil and fractured casts in table order.", 112, 127),
    ("MED-U7-10", "Urinary crystals, shapes and panels", S10,
     "Panels A–G in printed order: uric acid, calcium oxalate dihydrate and monohydrate, calcium phosphate, struvite, cholesterol, amoxicillin, cystine.", 128, 140),
]
units = []
for uid, title, sec, guide, a, b in unit_specs:
    units.append({"id": uid, "ch": 7, "n": int(uid.rsplit("-", 1)[1]), "title": title, "sec": sec,
                  "guide": REVISION + guide, "qs": [f"MED-C7-{i:03d}" for i in range(a, b + 1)]})
assert [q for u in units for q in u["qs"]] == [q["id"] for q in questions]
for u in units:
    assert len({q["page"] for q in questions if q["id"] in u["qs"]}) <= 2 and all(q["sec"] == u["sec"] for q in questions if q["id"] in u["qs"]), u["id"]

out = {"chapter": 7, "title": "Urine Analysis", "pageRange": "740-747", "questions": questions, "units": units}
(ROOT / "data" / "ch07.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
pages = [q["page"] for q in questions]
assert all(b >= a for a, b in zip(pages, pages[1:])), "page order"
for q in questions:
    m = re.search(r"\(Book p(\d+)\)$", q["exp"]); assert m and int(m.group(1)) == q["page"], q["id"]
    assert len(q["opts"]) == 4 and len({o.strip().casefold() for o in q["opts"]}) == 4, q["id"]
print(f"ch07: {len(questions)} questions, {len(units)} units")
