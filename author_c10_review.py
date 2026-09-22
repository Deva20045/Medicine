#!/usr/bin/env python3
"""Rebuild Ch 10 (Glomerular Disease - Patterns, p756-761) in strict source order.

Source review 2026-09-22: six pages read from the scans (Part 1 PDF pp64-67, Part 2
PDF pp1-2) at 2x. Every stored answer index checked against the print: all 78 correct.
Repairs (see REAUDIT_CH10_SOURCE_ORDER.md):
  * Uncovered printed elements given items: p759 'Note: Features against MCD' (RBC
    casts, hypertension, renal failure) and p760 '(Very quick remission)'.
  * Within-page order re-sequenced to the printed traversal (e.g. criteria items were
    interleaved with the biopsy flowchart; thrombosis items split around the edema
    manifestation block; adult MCD 15% item at the end).
Result: 80 questions, same 9 unit IDs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = json.loads((ROOT / "data" / "ch10.json").read_text())
if len(OLD["questions"]) != 78 or "Source-order revision" in OLD["units"][0].get("guide", ""):
    raise SystemExit("author_c10_review.py expects the pre-review 78-question data/ch10.json; refusing to re-run.")
BY_ID = {q["id"]: dict(q) for q in OLD["questions"]}
REVISION = ("Source-order revision, 22 Sep 2026: questions were reordered to the printed sequence and two "
            "uncovered printed notes added (all answer keys verified correct). Previous completion badges and "
            "XP are retained; replay this unit. ")

S1 = "Presentations & indication for biopsy · p756"
S2 = "Nephrotic syndrome criteria & nephrotic-range proteinuria · p756-757"
S3 = "Childhood NS: hypoalbuminemia & edema theories · p757-758"
S4 = "Management boxes & risk of thrombosis · p758"
S5 = "Edema manifestation & treatment · p758-759"
S6 = "Monitoring, steroid regimen & hyperlipidemia · p759"
S7 = "SRNS & calcineurin inhibitors · p760"
S8 = "Relapse categories & their treatment · p760"
S9 = "Adult nephrotic syndrome · p761"


def keep(old_id, sec, **over):
    q = dict(BY_ID[old_id]); q["sec"] = sec; q.update(over); return q


def new(sec, page, fmt, q, opts, ans, exp):
    return {"id": None, "sec": sec, "page": page, "q": q, "opts": opts, "ans": ans, "exp": exp, "fmt": fmt}


K = lambda n: f"MED-C10-{n:03d}"
seq = [
    # p756
    keep(K(1), S1), keep(K(7), S1), keep(K(2), S1), keep(K(3), S1), keep(K(4), S1), keep(K(11), S1), keep(K(5), S1), keep(K(6), S1),
    keep(K(12), S2), keep(K(13), S2), keep(K(9), S2), keep(K(10), S2), keep(K(14), S2), keep(K(8), S2), keep(K(15), S2),
    # p757
    keep(K(16), S2), keep(K(17), S2), keep(K(21), S2), keep(K(18), S2), keep(K(20), S2), keep(K(22), S2),
    keep(K(19), S3), keep(K(23), S3), keep(K(31), S3), keep(K(24), S3), keep(K(25), S3), keep(K(26), S3), keep(K(28), S3), keep(K(30), S3), keep(K(27), S3), keep(K(29), S3),
    # p758
    keep(K(32), S3), keep(K(34), S3), keep(K(36), S3), keep(K(35), S3), keep(K(33), S3),
    keep(K(38), S4), keep(K(39), S4), keep(K(37), S4),
    keep(K(40), S4), keep(K(45), S4), keep(K(41), S4), keep(K(44), S4), keep(K(42), S4), keep(K(43), S4),
    keep(K(46), S5), keep(K(47), S5), keep(K(48), S5),
    # p759
    keep(K(49), S5), keep(K(50), S5),
    keep(K(51), S6),
    new(S6, 759, "oddoneout", "The p759 note lists 'Features against MCD'. Which of the following is NOT one of them?",
        ["Heavy proteinuria", "RBC casts in urine", "Hypertension", "Renal failure"], 0,
        "Note — Features against MCD: RBC casts in urine; hypertension; renal failure. Heavy proteinuria is the hallmark of nephrotic syndrome itself, not a feature against MCD. (Book p759)"),
    keep(K(52), S6), keep(K(53), S6), keep(K(54), S6),
    keep(K(55), S6), keep(K(57), S6), keep(K(56), S6), keep(K(58), S6),
    # p760
    keep(K(59), S7), keep(K(60), S7), keep(K(61), S7), keep(K(62), S7),
    keep(K(63), S8), keep(K(64), S8),
    new(S8, 760, "fillup", "Fill up: In the relapse flowchart, the 25% 'No further relapse' arm carries the bracket '(Very quick ______)'.",
        ["remission", "taper", "relapse", "biopsy"], 0,
        "The left arm reads: 25% → No further relapse (Very quick remission). (Book p760)"),
    keep(K(65), S8), keep(K(66), S8), keep(K(67), S8), keep(K(68), S8), keep(K(69), S8), keep(K(70), S8),
    # p761
    keep(K(71), S9), keep(K(72), S9), keep(K(78), S9), keep(K(73), S9), keep(K(74), S9), keep(K(75), S9), keep(K(76), S9), keep(K(77), S9),
]
used = [q["id"] for q in seq if q["id"]]
assert len(seq) == 80 and len(set(used)) == 78, (len(seq), len(set(used)))
questions = []
for i, q in enumerate(seq, 1):
    q["id"] = K(i); questions.append(q)

unit_specs = [
    ("MED-U10-1", "Presentations & indication for biopsy", S1, "The six presentations, the CKD note, and the biopsy flowchart (asymptomatic arm thresholds; macrohematuria 40/5/1 rule).", 1, 8),
    ("MED-U10-2", "Nephrotic syndrome criteria & nephrotic-range proteinuria", S2, "Criteria 1–3 with the adult/child bracket; the hyperlipidemia note; total protein and PCR thresholds; 'not diagnostic'; the 'also seen in' bracket.", 9, 21),
    ("MED-U10-3", "Childhood NS: hypoalbuminemia & edema theories", S3, "Extravascular > intravascular; hypoalbuminemia mechanisms and Muehrcke's line; underfill chain; overfill chain and ANP resistance.", 22, 36),
    ("MED-U10-4", "Management boxes & risk of thrombosis", S4, "MCD / FSGS / MN-IgA boxes; albumin < 2 g/dl; causes of thrombosis; albumin correction.", 37, 45),
    ("MED-U10-5", "Edema manifestation & treatment", S5, "Ascites, pleural and pericardial effusion; salt, protein, albumin/FFP; diuretics avoided (IVC rule).", 46, 50),
    ("MED-U10-6", "Monitoring, steroid regimen & hyperlipidemia", S6, "Daily monitoring; features against MCD; prednisolone regimen; remission vs SRNS; hyperlipidemia facts, pathogenesis, xanthelasma.", 51, 59),
    ("MED-U10-7", "SRNS & calcineurin inhibitors", S7, "Biopsy as 1st indication; podocin FSGS → transplant; MCD → CNI (6 months, max 2 yrs), tacrolimus/cyclosporine side effects.", 60, 63),
    ("MED-U10-8", "Relapse categories & their treatment", S8, "Relapse after 1 month; 25/25/50 split; infrequent relapse; FRNS definition and steroid-sparing drugs; relapse after intermission; SDNS and its treatment.", 64, 72),
    ("MED-U10-9", "Adult nephrotic syndrome", S9, "Definition; causes with the Rare bracket; management; steroid 1 mg/kg/d × 4 months → SRNS (FSGS); the Fabry note.", 73, 80),
]
units = []
for uid, title, sec, guide, a, b in unit_specs:
    ids = [K(i) for i in range(a, b + 1)]
    assert all(q["sec"] == sec for q in questions if q["id"] in ids), uid
    units.append({"id": uid, "ch": 10, "n": int(uid.rsplit("-", 1)[1]), "title": title, "sec": sec, "guide": REVISION + guide, "qs": ids})
assert [q for u in units for q in u["qs"]] == [q["id"] for q in questions]

out = {"chapter": 10, "title": OLD["title"], "pageRange": "756-761", "questions": questions, "units": units}
(ROOT / "data" / "ch10.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
pages = [q["page"] for q in questions]
assert all(b >= a for a, b in zip(pages, pages[1:]))
for q in questions:
    m = re.search(r"\(Book p(\d+)\)$", q["exp"]); assert m and int(m.group(1)) == q["page"], q["id"]
    assert len(q["opts"]) == 4 and len({o.strip().casefold() for o in q["opts"]}) == 4, q["id"]
print(f"ch10: {len(questions)} questions, {len(units)} units")
