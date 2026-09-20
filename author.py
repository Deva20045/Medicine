#!/usr/bin/env python3
"""Assemble data/chNN.json from ordered, page-anchored part files.

Authoring workflow (quality re-audit for Ch 13-18):
  data/parts/c<NN>/_order.json   -> ordered list of part keys
  data/parts/c<NN>/<key>.json    -> {"page":int, "sec":str, "items":[{fmt,q,opts,ans,exp}]}
  data/units/c<NN>.json          -> [{"title","sec","guide","parts":[keys]}]

Running `python author.py <NN>` rebuilds data/ch<NN>.json with sequential MED
ids, validates every item (4 distinct options, length-giveaway, citation) and
prints the resulting counts so check_integrity.py stays in sync.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / "data" / "parts"
UNITS = ROOT / "data" / "units"

TITLES = {
    6: ("Renal Physiology", "734-739", 734),
    7: ("Urine Analysis", "740-747", 740),
    8: ("Basic Approach to Kidney Disease and Renal Artery Stenosis", "748-752", 748),
    9: ("Thrombotic Microangiopathy", "753-755", 753),
    10: ("Glomerular Disease - Patterns", "756-761", 756),
    11: ("Podocytopathies", "762-769", 762),
    12: ("MPGN and IgA Nephropathy", "770-774", 770),
    13: ("Post Streptococcal Glomerulonephritis", "775-777", 775),
    14: ("RPGN and Pulmonary Renal Syndrome", "778-782", 778),
    15: ("Familial Glomerular Syndromes", "783-785", 783),
    16: ("Ciliopathies", "786-792", 786),
    17: ("Chronic Tubulointerstitial Disease", "793-795", 793),
    18: ("Acute Kidney Injury", "796-804", 796),
    19: ("Chronic Kidney Disease", "805-807", 805),
    20: ("Anemia in Chronic Kidney Disease", "808-810", 808),
    21: ("CKD - Calciphylaxis and Cardiovascular changes", "811-814", 811),
    22: ("Diabetic Kidney Disease", "815-818", 815),
    23: ("Introduction to Acid Base Analysis", "819-823", 819),
    24: ("Metabolic Alkalosis", "824-825", 824),
    25: ("Methodology and Interpretation of ABG Analysis", "826-829", 826),
    26: ("Overview of Hormones", "830-836", 830),
    27: ("Physiology of Adrenal Cortex", "837-840", 837),
    28: ("Conn's Syndrome", "841-843", 841),
    29: ("Cushing's Syndrome", "844-848", 844),
    30: ("Addison's Disease", "849-851", 849),
    31: ("Adrenal Medulla : Part 1", "852-857", 852),
    32: ("Adrenal Medulla : Part 2", "858-862", 858),
    33: ("Basics of Bone and Mineral Metabolism", "863-873", 863),
    34: ("Calcium Metabolism", "874-876", 874),
    35: ("Hypercalcemia", "877-882", 877),
    36: ("Hypocalcemia", "883-886", 883),
    37: ("Phosphorus Metabolism", "887-891", 887),
    38: ("Magnesium Metabolism", "892-894", 892),
    39: ("Osteoporosis", "895-897", 895),
    40: ("Basics of Thyroid Gland", "898-901", 898),
    41: ("Thyroid Function Tests", "902-904", 902),
    42: ("Hypothyroidism", "905-909", 905),
    43: ("Thyrotoxicosis and Thyroiditis", "910-916", 910),
    44: ("Introduction to Diabetes Mellitus and Classification", "917-926", 917),
    45: ("Insulin Physiology and Acute Complications of Diabetes Mellitus", "927-932", 927),
    46: ("Management of Diabetes Mellitus - 2024 Guidelines", "933-935", 933),
    47: ("Basics of Pituitary Gland", "936-940", 936),
    48: ("Prolactin", "941-944", 941),
    49: ("Growth Hormone", "945-951", 945),
    50: ("Acquired Hypopituitarism", "952-957", 952),
    51: ("Antidiuretic Hormone", "958-961", 958),
    52: ("Hyponatremia", "962-964", 962),
    53: ("Polyuria", "965-967", 965),
    54: ("Potassium Metabolism", "968-975", 968),
    55: ("Management of Hypertension - 2023 Guidelines", "976-981", 976),
    56: ("Basics of Development and Anatomy of Liver", "982-985", 982),
    60: ("Portal Hypertension", "1001-1004", 1001),
    61: ("Ascites and Hepatorenal Syndrome", "1005-1009", 1005),
    62: ("Hepatic Encephalopathy", "1010-1012", 1010),
    63: ("Metabolic Diseases of Liver", "1013-1019", 1013),
    64: ("Biliary Cirrhosis", "1020-1022", 1020),
    65: ("Autoimmune Hepatitis", "1023-1025", 1023),
    66: ("Alcoholic Liver Disease", "1026-1029", 1026),
    67: ("Nonalcoholic Steatohepatitis", "1030-1032", 1030),
    68: ("Vascular Diseases of Liver", "1033-1035", 1033),
    69: ("Hepatitis B Virus : Part 1", "1036-1038", 1036),
    70: ("Hepatitis B Virus : Part 2", "1039-1044", 1039),
    71: ("Hepatitis C Virus", "1045-1046", 1045),
    72: ("Infective Endocarditis", "1047-1052", 1047),
    73: ("Tropical Infections: Synopsis", "1053-1060", 1053),
    74: ("HIV", "1061-1068", 1061),
}

BANNED = [
    r"none of the above",
    r"all of the above",
    r"what is written on",
    r"which statement is recorded",
    r"as stated on page",
    r"not stated on this page",
    r"unrelated surgical",
]


def fail(msg: str) -> None:
    print("ASSEMBLY FAILED: " + msg)
    sys.exit(1)


def build(ch: int) -> None:
    title, page_range, _start = TITLES[ch]
    order_path = PARTS / f"c{ch}" / "_order.json"
    if not order_path.exists():
        fail(f"missing {order_path}")
    order = json.loads(order_path.read_text(encoding="utf-8"))

    questions: list[dict] = []
    by_key: dict[str, list[str]] = {}
    pages_seen: list[int] = []
    for key in order:
        path = PARTS / f"c{ch}" / f"{key}.json"
        if not path.exists():
            fail(f"missing part {path}")
        part = json.loads(path.read_text(encoding="utf-8"))
        ids: list[str] = []
        for item in part["items"]:
            page = int(item.get("page", part["page"]))
            sec = item.get("sec", part["sec"])
            qid = f"MED-C{ch}-{len(questions) + 1:03d}"
            opts = [str(o).strip() for o in item["opts"]]
            ans = int(item["ans"])
            exp = item["exp"].strip()
            if not exp.endswith(f"(Book p{page})"):
                fail(f"{qid}: explanation must end with '(Book p{page})', got ...{exp[-40:]!r}")
            if len(opts) != 4 or len({o.casefold() for o in opts}) != 4 or any(not o for o in opts):
                fail(f"{qid}: need 4 distinct non-empty options")
            if not 0 <= ans <= 3:
                fail(f"{qid}: bad answer index")
            # Anti-bias: items are authored with the correct option first for
            # readable source files; rotate deterministically (seeded by the
            # stable id) so the stored answer index is spread evenly across A-D.
            shift = (int(hashlib.sha256(qid.encode()).hexdigest(), 16) % 4 - ans) % 4
            if shift:
                opts = opts[-shift:] + opts[:-shift]
                ans = (ans + shift) % 4
            longest = max(len(o) for i, o in enumerate(opts) if i != ans)
            if len(opts[ans]) > max(longest, 1) * 3.0:
                fail(f"{qid}: answer is {len(opts[ans]) / max(longest, 1):.1f}x the longest distractor")
            low = (item["q"] + " " + " ".join(opts)).casefold()
            for pattern in BANNED:
                if re.search(pattern, low):
                    fail(f"{qid}: banned filler phrase /{pattern}/")
            if item["fmt"] not in {"fillup", "match", "truefalse", "scenario", "oddoneout", "recall", "numeric", "management"}:
                fail(f"{qid}: unknown format {item['fmt']!r}")
            questions.append(
                {"id": qid, "sec": sec, "page": page, "fmt": item["fmt"],
                 "q": item["q"].strip(), "opts": opts, "ans": ans, "exp": exp}
            )
            ids.append(qid)
            pages_seen.append(page)
        by_key[key] = ids

    if any(b < a for a, b in zip(pages_seen, pages_seen[1:])):
        # book order inside a chapter: allow re-entering a page only if the part
        # explicitly says so (sec override), otherwise report it loudly.
        print("WARNING: page order is not monotonic:", pages_seen)

    specs = json.loads((UNITS / f"c{ch}.json").read_text(encoding="utf-8"))
    units: list[dict] = []
    for i, spec in enumerate(specs, 1):
        qids: list[str] = []
        for key in spec["parts"]:
            if key not in by_key:
                fail(f"unit {i} references unknown part {key!r}")
            qids.extend(by_key[key])
        units.append({"id": f"MED-U{ch}-{i}", "ch": ch, "n": i, "title": spec["title"],
                      "sec": spec["sec"], "guide": spec["guide"], "qs": qids})

    covered = [qid for unit in units for qid in unit["qs"]]
    if covered != [q["id"] for q in questions]:
        fail("units must cover every question exactly once, in order")

    artifact = {"chapter": ch, "title": title, "pageRange": page_range,
                "questions": questions, "units": units}
    out = ROOT / "data" / f"ch{ch:02d}.json"
    out.write_text(json.dumps(artifact, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    fmts: dict[str, int] = {}
    for q in questions:
        fmts[q["fmt"]] = fmts.get(q["fmt"], 0) + 1
    print(f"Ch{ch}: {len(questions)} questions, {len(units)} units -> {out.name}")
    print("  formats: " + ", ".join(f"{k}={v}" for k, v in sorted(fmts.items())))
    print(f"  pages covered: {min(pages_seen)}-{max(pages_seen)} ({len(set(pages_seen))} distinct)")


if __name__ == "__main__":
    build(int(sys.argv[1]))
