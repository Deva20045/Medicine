#!/usr/bin/env python3
"""Rebuild Ch 8 (Basic Approach to Kidney Disease & RAS, p748-752) in strict source order.

Source review 2026-09-22: five pages read from the Part 1 scan (PDF pp56-60) at 2x.
Every stored answer index checked against the print: all 83 correct.
Repairs (see REAUDIT_CH8_SOURCE_ORDER.md):
  * Text: the print says 'hydroureteronephrosis' (p749, twice); MED-C8-017 stem /
    exp and 019 exp said 'hydronephroureteronephrosis'. Aligned to print.
  * Typo distractor 'Captopren renography' (082) -> 'Captopril renography'.
  * Within-page order re-sequenced to the printed traversal on all five pages
    (e.g. urine-analysis boxes were tested at item 11, the 'most common' tree
    consolidation match came before its branches, the CDU flowchart before the
    page-top captions).
Result: 83 questions, same 8 unit IDs, unit membership re-cut to page order.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = json.loads((ROOT / "data" / "ch08.json").read_text())
if len(OLD["questions"]) != 83 or "Source-order revision" in OLD["units"][0].get("guide", ""):
    raise SystemExit("author_c8_review.py expects the pre-review 83-question data/ch08.json; refusing to re-run.")
BY_ID = {q["id"]: dict(q) for q in OLD["questions"]}
REVISION = ("Source-order revision, 22 Sep 2026: questions were reordered to the printed sequence and two "
            "wordings aligned to the print (all answer keys verified correct). Previous completion badges and "
            "XP are retained; replay this unit. ")

S1 = "Initial investigation & USG approach · p748"
S2 = "Non-CKD categories & RAS introduction · p749"
S3 = "Renal artery stenosis: causes & unilateral pathogenesis · p749-750"
S4 = "Radiological investigation & unilateral treatment · p751"
S5 = "Bilateral RAS · p751"
S6 = "CDU screening, angiography & FMD · p752"


def keep(old_id, sec, **over):
    q = dict(BY_ID[old_id]); q["sec"] = sec; q.update(over); return q


q017 = keep("MED-C8-017", S2,
            q="Before diagnosing CKD on USG one must rule out hydroureteronephrosis, whose clue on imaging is:",
            exp="Rule out hydroureteronephrosis before diagnosing CKD (printed spelling); figure caption: calyces becoming prominent and ureter seen. (Book p749)")
q019 = keep("MED-C8-019", S2, exp="AKI: postrenal (B/L hydroureteronephrosis on USG), pre-renal investigation (normal urine analysis), ATN, AIN. (Book p749)")
q082 = keep("MED-C8-082", S6)
q082["opts"] = ["Captopril renography" if o == "Captopren renography" else o for o in q082["opts"]]

seq = [
    # p748
    keep("MED-C8-001", S1), keep("MED-C8-003", S1), keep("MED-C8-002", S1), keep("MED-C8-011", S1),
    keep("MED-C8-009", S1), keep("MED-C8-004", S1), keep("MED-C8-015", S1), keep("MED-C8-014", S1),
    keep("MED-C8-005", S1), keep("MED-C8-006", S1), keep("MED-C8-007", S1), keep("MED-C8-016", S1),
    keep("MED-C8-010", S1), keep("MED-C8-008", S1), keep("MED-C8-012", S1), keep("MED-C8-013", S1),
    # p749
    q017,
    keep("MED-C8-023", S2), keep("MED-C8-024", S2), keep("MED-C8-030", S2), keep("MED-C8-031", S2),
    keep("MED-C8-025", S2), keep("MED-C8-029", S2), keep("MED-C8-026", S2),
    keep("MED-C8-022", S2), q019, keep("MED-C8-020", S2), keep("MED-C8-021", S2), keep("MED-C8-018", S2),
    keep("MED-C8-027", S3), keep("MED-C8-028", S3),
    # p750
    keep("MED-C8-034", S3), keep("MED-C8-050", S3), keep("MED-C8-035", S3), keep("MED-C8-047", S3),
    keep("MED-C8-036", S3), keep("MED-C8-049", S3), keep("MED-C8-033", S3), keep("MED-C8-046", S3), keep("MED-C8-032", S3),
    keep("MED-C8-037", S3), keep("MED-C8-038", S3),
    keep("MED-C8-041", S3), keep("MED-C8-048", S3), keep("MED-C8-045", S3),
    keep("MED-C8-043", S3), keep("MED-C8-042", S3),
    keep("MED-C8-044", S3), keep("MED-C8-039", S3), keep("MED-C8-040", S3),
    # p751 unilateral
    keep("MED-C8-051", S4), keep("MED-C8-052", S4), keep("MED-C8-055", S4),
    keep("MED-C8-053", S4), keep("MED-C8-054", S4), keep("MED-C8-056", S4),
    # p751 bilateral
    keep("MED-C8-058", S5), keep("MED-C8-064", S5), keep("MED-C8-059", S5), keep("MED-C8-065", S5),
    keep("MED-C8-060", S5), keep("MED-C8-061", S5), keep("MED-C8-067", S5),
    keep("MED-C8-062", S5), keep("MED-C8-057", S5), keep("MED-C8-063", S5), keep("MED-C8-066", S5),
    # p752
    keep("MED-C8-079", S6), keep("MED-C8-080", S6), keep("MED-C8-068", S6),
    keep("MED-C8-069", S6), keep("MED-C8-070", S6), q082, keep("MED-C8-071", S6), keep("MED-C8-081", S6),
    keep("MED-C8-072", S6), keep("MED-C8-073", S6),
    keep("MED-C8-074", S6), keep("MED-C8-083", S6), keep("MED-C8-075", S6), keep("MED-C8-076", S6),
    keep("MED-C8-077", S6), keep("MED-C8-078", S6),
]
used = [q["id"] for q in seq]
assert len(seq) == 83 and len(set(used)) == 83, (len(seq), len(set(used)))

questions = []
for i, q in enumerate(seq, 1):
    q["id"] = f"MED-C8-{i:03d}"; questions.append(q)

unit_specs = [
    ("MED-U8-1", "Initial investigation & the USG approach", S1,
     "The three initial-investigation arms; the Approach tree (USG most important, the three size lines, CMD present/absent, hemodialysis/transplant); the normal-kidney vs CKF ultrasound labels.", 1, 8),
    ("MED-U8-2", "USG approach continued: size bands, CMD and figures", S1,
     ">10 cm with loss of CMD (DM, HIV, amyloidosis); CMD present → CKD, absent → non-CKD; hemodialysis/transplant; isoechoic/hypoechoic/hyperechoic labels; 'CMD lost' caption.", 9, 16),
    ("MED-U8-3", "Non-CKD categories", S2,
     "Rule out hydroureteronephrosis; days-to-weeks RPRF (RPGN m/c, biopsy; severe ATN/TMA rare); hypertensive crisis (RAS large vessel, TMA small vessel); normal RFT with renal disease; hours-to-days AKI list.", 17, 29),
    ("MED-U8-4", "RAS introduction & most common causes", S3,
     "AKA RVH/RAOD, progression to CKD/ischemic nephropathy; then the 'most common' tree: atherosclerosis, fibromuscular dysplasia, Takayasu (F:m 9:1), polyarteritis nodosa.", 30, 40),
    ("MED-U8-5", "Unilateral RAS: pathogenesis", S3,
     "Goldblatt two-kidney-one-clip; asymmetric kidney size; affected-kidney chain (RAS → aldosterone → AT-II ↑↑ → vasoconstriction → HTN); normal-kidney pressure natriuresis; the note and potency line; C/F and basic investigation.", 41, 50),
    ("MED-U8-6", "Diagnosing RAS and treating unilateral disease", S4,
     "Asymmetric kidney on USG; renal doppler screen → CT/MR angiography (IOC); ACEi/ARB (DOC); PTRA only if kidney > 8 cm.", 51, 56),
    ("MED-U8-7", "Bilateral RAS: volume overload, flash edema & treatment", S5,
     "Poor prognosis; x = occlusion; loss of pressure natriuresis → Na+/H2O retention → volume overload (−) on RAS → recurrent flash pulmonary edema → B/L PTRA with stenting; diuretics DOC, ACEi/ARB C/I, stop smoking, start statins.", 57, 67),
    ("MED-U8-8", "Colour doppler cut-offs, angiography & fibromuscular dysplasia", S6,
     "Page-top captions; the cardiac note; CDU: parvus tardus, RI ≥ 0.8 vs < 0.8 criteria, inconclusive → CT/MR (IOC) → conventional angiography (gold standard); FMD block and the string-of-beads caption.", 68, 83),
]
units = []
for uid, title, sec, guide, a, b in unit_specs:
    ids = [f"MED-C8-{i:03d}" for i in range(a, b + 1)]
    assert all(q["sec"] == sec for q in questions if q["id"] in ids), uid
    units.append({"id": uid, "ch": 8, "n": int(uid.rsplit("-", 1)[1]), "title": title, "sec": sec, "guide": REVISION + guide, "qs": ids})
assert [q for u in units for q in u["qs"]] == [q["id"] for q in questions]

out = {"chapter": 8, "title": OLD["title"], "pageRange": "748-752", "questions": questions, "units": units}
(ROOT / "data" / "ch08.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
pages = [q["page"] for q in questions]
assert all(b >= a for a, b in zip(pages, pages[1:]))
for q in questions:
    m = re.search(r"\(Book p(\d+)\)$", q["exp"]); assert m and int(m.group(1)) == q["page"], q["id"]
    assert len(q["opts"]) == 4 and len({o.strip().casefold() for o in q["opts"]}) == 4, q["id"]
print(f"ch08: {len(questions)} questions, {len(units)} units")
