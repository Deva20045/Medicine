#!/usr/bin/env python3
"""Rebuild Ch 9 (Thrombotic Microangiopathy, p753-755) in strict source order.

Source review 2026-09-22: three pages read from the Part 1 scan (PDF pp61-63) at 2x.
Every stored answer index checked against the print: 51/52 correct.
Repairs (see REAUDIT_CH9_SOURCE_ORDER.md):
  * MED-C9-051 (old id): the keyed pairing '3-A' mapped ATN BUN/creatinine to the
    option 'A) > 20:1', but the print gives ATN '< 10:1' (> 20:1 is the pre-renal
    column). Option A text corrected to '< 10:1' so the key matches the print.
  * Within-page order re-sequenced (e.g. the causes-list consolidation match sat
    before the anti-RNA-P/bracket lines; TTP-pentagon items were interleaved with
    HUS-triad items; the drug-list oddoneout sat before the immune-mediated list).
Result: 52 questions, same 5 unit IDs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = json.loads((ROOT / "data" / "ch09.json").read_text())
if len(OLD["questions"]) != 52 or "Source-order revision" in OLD["units"][0].get("guide", ""):
    raise SystemExit("author_c9_review.py expects the pre-review 52-question data/ch09.json; refusing to re-run.")
BY_ID = {q["id"]: dict(q) for q in OLD["questions"]}
REVISION = ("Source-order revision, 22 Sep 2026: questions were reordered to the printed sequence and one "
            "mis-built match option corrected against the print. Previous completion badges and XP are "
            "retained; replay this unit. ")

S1 = "TMA causes & malignant hypertension · p753"
S2 = "HUS features, TTP pentad & types · p753"
S3 = "Pathophysiology & causes · p754"
S4 = "Investigation · p754"
S5 = "Presentation, treatment & pre-renal vs ATN · p755"


def keep(old_id, sec, **over):
    q = dict(BY_ID[old_id]); q["sec"] = sec; q.update(over); return q


q051 = keep("MED-C9-051", S5)
q051["q"] = q051["q"].replace("A) > 20:1", "A) < 10:1")
assert "A) < 10:1" in q051["q"]
q051["exp"] = ("The necrosis column reads: urine output decreased, edema +, BUN/creatinine < 10:1, fluids withhold, tubular "
               "injury +; the pre-renal column carries normal / − / > 20:1 / given / −. (Book p755)")

seq = [
    keep("MED-C9-001", S1), keep("MED-C9-002", S1), keep("MED-C9-008", S1), keep("MED-C9-004", S1), keep("MED-C9-003", S1),
    keep("MED-C9-005", S1), keep("MED-C9-007", S1), keep("MED-C9-006", S1),
    keep("MED-C9-009", S2), keep("MED-C9-010", S2), keep("MED-C9-011", S2), keep("MED-C9-016", S2), keep("MED-C9-015", S2), keep("MED-C9-012", S2),
    keep("MED-C9-013", S2), keep("MED-C9-014", S2), keep("MED-C9-017", S2), keep("MED-C9-018", S2),
    keep("MED-C9-019", S3), keep("MED-C9-025", S3), keep("MED-C9-020", S3), keep("MED-C9-021", S3),
    keep("MED-C9-022", S3), keep("MED-C9-024", S3), keep("MED-C9-023", S3),
    keep("MED-C9-026", S3), keep("MED-C9-027", S3),
    keep("MED-C9-028", S3), keep("MED-C9-034", S3), keep("MED-C9-036", S3), keep("MED-C9-035", S3), keep("MED-C9-029", S3),
    keep("MED-C9-030", S4), keep("MED-C9-031", S4), keep("MED-C9-033", S4), keep("MED-C9-032", S4),
    keep("MED-C9-037", S5), keep("MED-C9-047", S5), keep("MED-C9-048", S5), keep("MED-C9-038", S5), keep("MED-C9-039", S5),
    keep("MED-C9-040", S5), keep("MED-C9-041", S5), keep("MED-C9-042", S5), keep("MED-C9-049", S5), keep("MED-C9-043", S5), keep("MED-C9-050", S5),
    keep("MED-C9-044", S5), keep("MED-C9-045", S5), keep("MED-C9-046", S5), q051, keep("MED-C9-052", S5),
]
used = [q["id"] for q in seq]
assert len(seq) == 52 and len(set(used)) == 52
questions = []
for i, q in enumerate(seq, 1):
    q["id"] = f"MED-C9-{i:03d}"; questions.append(q)

unit_specs = [
    ("MED-U9-1", "TMA causes & malignant hypertension", S1,
     "HUS, HELLP, the rheumatological bracket (catastrophic APS, diffuse scleroderma – anti RNA P) small vs large vessels, malignant hypertension = accelerated HTN + papilloedema with the fundal/emergency bracket.", 1, 8),
    ("MED-U9-2", "HUS features, TTP pentad & types", S2,
     "The triad triangle, the TTP pentagon (with [Brain]), then the TYPES table row by row: onset, cause, prognosis.", 9, 18),
    ("MED-U9-3", "Pathophysiology & causes", S3,
     "Endothelial damage → VWF → platelet plug → thrombocytopenia / schistocytes → MAHA; typical toxins (90%); genetic atypical (alternate pathway, low C3 normal C4, factor H/B/MCP/I); sporadic drugs; immune-mediated HUS.", 19, 32),
    ("MED-U9-4", "Investigation", S4,
     "Schistocytes > 2%; ↑LDH, −ve Coombs, ↑indirect bilirubin, ↓haptoglobin, normal PT/APTT; the atypical-HUS vs SLE complement note.", 33, 36),
    ("MED-U9-5", "Presentation, treatment & pre-renal vs ATN", S5,
     "Typical HUS timeline and conservative treatment; atypical HUS features and treatment list (PLEX, eculizumab, immunosuppressant, transplant, recurrence); the pre-renal vs ATN note table.", 37, 52),
]
units = []
for uid, title, sec, guide, a, b in unit_specs:
    ids = [f"MED-C9-{i:03d}" for i in range(a, b + 1)]
    assert all(q["sec"] == sec for q in questions if q["id"] in ids), uid
    units.append({"id": uid, "ch": 9, "n": int(uid.rsplit("-", 1)[1]), "title": title, "sec": sec, "guide": REVISION + guide, "qs": ids})
assert [q for u in units for q in u["qs"]] == [q["id"] for q in questions]

out = {"chapter": 9, "title": OLD["title"], "pageRange": "753-755", "questions": questions, "units": units}
(ROOT / "data" / "ch09.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
pages = [q["page"] for q in questions]
assert all(b >= a for a, b in zip(pages, pages[1:]))
for q in questions:
    m = re.search(r"\(Book p(\d+)\)$", q["exp"]); assert m and int(m.group(1)) == q["page"], q["id"]
    assert len(q["opts"]) == 4 and len({o.strip().casefold() for o in q["opts"]}) == 4, q["id"]
print(f"ch09: {len(questions)} questions, {len(units)} units")
