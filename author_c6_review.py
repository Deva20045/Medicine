#!/usr/bin/env python3
"""Rebuild Ch 6 (Renal Physiology, p734-739) in strict source order.

Source review 2026-09-22: all six pages read from the Part 1 scan (PDF pp42-47)
at 2x whole-page plus 4x-6x crops of every formula, table cell, flowchart and
figure label, and reconciled question by question to the 133-item bank.

Findings repaired here (see REAUDIT_CH6_SOURCE_ORDER.md):
  * 35 of 133 items carried the WRONG stored answer. Cause: migrate_parts.py
    treated any item whose sha256(id)%4 happened to equal its answer index as
    author.py output and "un-rotated" its options, moving the correct option out
    of slot 0; author.py then shipped a distractor as the key. Every affected
    item is re-keyed to the printed value. Source verified per item below.
  * Within-page order faults on every page (e.g. the p734 net-pressure line
    tested before the equation lines that precede it; the Jaffe's-method table
    cell tested before the Cockcroft & Gault heading; the Schwartz K constants
    before the formula; the diet/obesity, sex and 40-year lines out of sequence
    on p736; the 'Beyond point of compensation' label after the chain
    consolidations; the myogenic reflex after tubulo-glomerular feedback; the
    p739 arteriolar bullets split around the table). Every page is re-sequenced
    to the recorded traversal; consolidations sit after the lines they test.
  * Uncovered source lines given questions: p734 figure labels 'Afferent
    arteriole'/'Efferent arteriole' (replaces a duplicate of item 1); p735 'Not
    preferred now d/t disadvantages'; the 'CrCl = GFR (only true for inert
    molecules like inulin)' assumption; the 'Directly measures GFR' cell; the
    'Over emphasis on BW' cell; '4. Schwartz equation: estimate GFR in children'.
  * Explanation error fixed: MED-C6-099 claimed '300 meq filtered' (book: 200).
  * Print caveats flagged, not corrected: 'spectrosopy' (p735), 'Sex (↓ in
    males)' (p736), the p739 NSAID chain's back-arrow 'maintain GFR ←'.
Result: 138 questions in the same 10 unit IDs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = json.loads((ROOT / "data" / "ch06.json").read_text())
if len(OLD["questions"]) != 133 or "Source-order revision" in OLD["units"][0].get("guide", ""):
    raise SystemExit("author_c6_review.py expects the pre-review 133-question data/ch06.json; refusing to re-run.")
BY_ID = {q["id"]: dict(q) for q in OLD["questions"]}

REVISION = ("Source-order revision, 22 Sep 2026: 35 wrong answer keys were corrected, "
            "questions were reordered to the printed sequence and missing lines added. "
            "Previous completion badges and XP are retained; replay this unit. ")


def keep(old_id, **over):
    q = dict(BY_ID[old_id])
    q.update(over)
    return q


def fix(old_id, correct_option, **over):
    """Re-key an item whose stored answer index pointed at a distractor."""
    q = keep(old_id, **over)
    q["ans"] = q["opts"].index(correct_option)
    return q


def new(sec, page, fmt, q, opts, ans, exp):
    return {"id": None, "sec": sec, "page": page, "q": q, "opts": opts,
            "ans": ans, "exp": exp, "fmt": fmt}


S734A = "GFR: definition & Starling forces · p734"
S734B = "Normal GFR & its clinical use · p734"
S735A = "Creatinine · p735"
S735B = "Equations to calculate GFR · p735"
S736A = "Schwartz equation · p736"
S736B = "Disadvantages of creatinine · p736"
S737 = "Note, endogenous clearance & Cystatin C · p737"
S738A = "Regulation of Renal Functions · p738"
S738B = "Filtration Fraction & pressure natriuresis · p738"
S739A = "Pressure natriuresis mechanism · p739"
S739B = "Glomerular Hemodynamics · p739"

seq = [
    # ---------------- p734 ----------------
    keep("MED-C6-001", sec=S734A),                       # Definition
    keep("MED-C6-002", sec=S734A),                       # GFR = net UF pressure x UF coefficient
    fix("MED-C6-007", "Net ultrafiltration pressure = net hydrostatic pressure minus net oncotic pressure", sec=S734A),
    keep("MED-C6-009", sec=S734A),                       # (Glom cap HP - Bowman HP) = 42
    keep("MED-C6-006", sec=S734A),                       # Bowman's space OP = 0
    keep("MED-C6-008", sec=S734A),                       # x 12.5 ml/min/mmHg
    fix("MED-C6-004", "10 mm Hg", sec=S734A,
        q="The net filtration pressure worked out on this page (the '= 10 × 12.5 ml/min' line, repeated in the boxes below the figure) is:"),
    fix("MED-C6-005", "125 ml/min", sec=S734A),          # = 125 ml/min
    keep("MED-C6-003", sec=S734A),                       # figure values 60 / 32 / 18
    keep("MED-C6-011", sec=S734A),                       # figure arrows
    new(S734A, 734, "fillup",
        "Fill up: In the glomerular figure, the vessel labelled on the left of the capillary tuft is the ______ arteriole and the one on the right is the efferent arteriole.",
        ["Afferent", "Interlobular", "Arcuate", "Peritubular"], 0,
        "The figure labels 'Afferent arteriole' at the left and 'Efferent arteriole' at the right of the pink glomerular capillary, with the 60 mm Hg hydrostatic and 32 mm Hg colloid osmotic pressures inside it. (Book p734)"),
    keep("MED-C6-010", sec=S734A),                       # boxes
    keep("MED-C6-013", sec=S734B, ans=BY_ID["MED-C6-013"]["opts"].index("90–125 ml/min")),
    keep("MED-C6-017", sec=S734B),
    keep("MED-C6-014", sec=S734B),
    keep("MED-C6-019", sec=S734B),
    fix("MED-C6-015", "Dialysis", sec=S734B),
    keep("MED-C6-016", sec=S734B),
    keep("MED-C6-018", sec=S734B),
    keep("MED-C6-020", sec=S734B),
    # ---------------- p735 ----------------
    keep("MED-C6-021", sec=S735A),
    fix("MED-C6-022", "Creatine", sec=S735A),
    fix("MED-C6-023", "Amputation", sec=S735A),
    keep("MED-C6-030", sec=S735A),
    fix("MED-C6-024", "Pregnancy is the only condition where high creatinine values are significant independently", sec=S735A),
    keep("MED-C6-029", sec=S735A),
    fix("MED-C6-025", "0.3–0.6 mg/dL", sec=S735A),
    keep("MED-C6-026", sec=S735A,
         exp="Bullet 4 prints '113 Kda molecule' — taught as printed (cystatin C on p737 is the 13 kDa protein). (Book p735)"),
    keep("MED-C6-028", sec=S735A),
    fix("MED-C6-031", "Obsolete", sec=S735B),
    keep("MED-C6-039", sec=S735B),
    fix("MED-C6-033", "72 × S.Cr", sec=S735B),
    fix("MED-C6-032", "0.8", sec=S735B),
    keep("MED-C6-040", sec=S735B),
    new(S735B, 735, "truefalse",
        "The line printed directly under 'Bed side formula' says the Cockcroft & Gault equation is not preferred now because of its disadvantages.",
        ["True — 'Not preferred now d/t disadvantages' is the next bullet",
         "False — the next bullet says it is preferred in the ICU",
         "True — but the stated reason is cost, not disadvantages",
         "False — the page gives no reason for its obsolescence"], 0,
        "Two bullets follow the formula: 'Bed side formula.' then 'Not preferred now d/t disadvantages.' — the disadvantages are then tabulated lower on the page. (Book p735)"),
    keep("MED-C6-041", sec=S735B),
    fix("MED-C6-034", "1-B, 2-A, 3-C", sec=S735B),
    keep("MED-C6-042", sec=S735B),
    keep("MED-C6-035", sec=S735B),
    keep("MED-C6-043", sec=S735B),
    new(S735B, 735, "recall",
        "The table's first disadvantage says Cockcroft & Gault overestimates GFR because it assumes CrCl = GFR, which is only true for inert molecules such as:",
        ["Inulin", "Urea", "Glucose", "Para-aminohippuric acid"], 0,
        "Row 1, left column: 'Overestimate GFR: D/t assumption that CrCl = GFR (Only true for inert molecules like inulin).' (Book p735)"),
    fix("MED-C6-038", "GFR + tubular secretion (or GFR − tubular absorption)", sec=S735B),
    keep("MED-C6-044", sec=S735B),
    new(S735B, 735, "fillup",
        "Fill up: Opposite the 'Overestimate GFR' row, the advantage of the MDRD & CKD-EPI equations is that they ______ GFR.",
        ["Directly measure", "Underestimate", "Correct body weight for", "Stage"], 0,
        "Row 1, right column of the table reads simply 'Directly measures GFR.' (Book p735)"),
    keep("MED-C6-027", sec=S735B),
    keep("MED-C6-037", sec=S735B,
         exp="Advantage row 2: 'Equation uses estimation of Cr using standard assays: IDM. (Isotope dilution mass spectrosopy)' — the scan misspells spectroscopy; taught as printed. (Book p735)"),
    new(S735B, 735, "fillup",
        "Fill up: The last disadvantage listed for the Cockcroft & Gault equation is over emphasis on ______.",
        ["Body weight (BW)", "Age", "Serum creatinine", "Sex"], 0,
        "Row 3, left column: 'Over emphasis on BW.' — the matching advantage cell says race is used instead of weight. (Book p735)"),
    keep("MED-C6-036", sec=S735B),
    new(S735B, 735, "recall",
        "Equation 4 on this page, the Schwartz equation, is used to estimate GFR in:",
        ["Children", "Pregnancy", "Amputees", "Patients on dialysis"], 0,
        "4. Schwartz equation: Estimate GFR in children — its formula and constants continue on the next page. (Book p735)"),
    # ---------------- p736 ----------------
    keep("MED-C6-047", sec=S736A),
    keep("MED-C6-050", sec=S736A),
    keep("MED-C6-045", sec=S736A),
    keep("MED-C6-046", sec=S736A),
    keep("MED-C6-048", sec=S736A),
    keep("MED-C6-049", sec=S736A),
    keep("MED-C6-051", sec=S736A),
    keep("MED-C6-052", sec=S736B),
    keep("MED-C6-062", sec=S736B),
    keep("MED-C6-054", sec=S736B),
    fix("MED-C6-055", "Muscle mass", sec=S736B),
    keep("MED-C6-067", sec=S736B),
    keep("MED-C6-061", sec=S736B,
         exp="The four bullets are muscle mass (↓ muscle mass → ↓ Cr), race (↓ in African Americans), age (↓ after 40 years d/t ↓ in muscle mass) and sex (↓ in males). The print is quoted verbatim; physiologically greater male muscle mass gives HIGHER creatinine, so this line is a flagged source caveat. (Book p736)"),
    keep("MED-C6-066", sec=S736B),
    fix("MED-C6-056", "Fat", sec=S736B),
    fix("MED-C6-053", "Obesity", sec=S736B),                        # consolidation after the obesity line
    fix("MED-C6-057", "Secretion", sec=S736B),
    keep("MED-C6-063", sec=S736B),
    fix("MED-C6-060", "By the time creatinine rises, GFR has already fallen significantly", sec=S736B),
    fix("MED-C6-058", "60 ml/min", sec=S736B),
    keep("MED-C6-064", sec=S736B),
    fix("MED-C6-059", "Fallen significantly (about 50 → 30 ml/min)", sec=S736B),
    keep("MED-C6-065", sec=S736B),
    # ---------------- p737 ----------------
    keep("MED-C6-068", sec=S737),
    keep("MED-C6-078", sec=S737),
    keep("MED-C6-069", sec=S737),
    keep("MED-C6-077", sec=S737),
    fix("MED-C6-070", "Plasma", sec=S737),
    keep("MED-C6-083", sec=S737),
    keep("MED-C6-071", sec=S737),
    keep("MED-C6-082", sec=S737),
    fix("MED-C6-072", "1-B, 2-C, 3-A", sec=S737),
    fix("MED-C6-073", "It is secreted by the PCT", sec=S737),
    keep("MED-C6-079", sec=S737),
    keep("MED-C6-080", sec=S737),
    fix("MED-C6-074", "Inflammation", sec=S737),
    keep("MED-C6-085", sec=S737),
    keep("MED-C6-076", sec=S737),
    fix("MED-C6-075", "Creatinine", sec=S737),
    keep("MED-C6-081", sec=S737),
    keep("MED-C6-084", sec=S737),
    # ---------------- p738 ----------------
    keep("MED-C6-086", sec=S738A),
    keep("MED-C6-087", sec=S738A),
    keep("MED-C6-093", sec=S738A),
    keep("MED-C6-088", sec=S738A),
    keep("MED-C6-089", sec=S738A),
    keep("MED-C6-096", sec=S738A),
    keep("MED-C6-090", sec=S738A),
    keep("MED-C6-095", sec=S738A),
    keep("MED-C6-097", sec=S738A),
    keep("MED-C6-094", sec=S738A),
    keep("MED-C6-092", sec=S738A),
    keep("MED-C6-098", sec=S738A),
    fix("MED-C6-091", "198 meq reabsorbed, 2 meq excreted (1%)", sec=S738A),
    keep("MED-C6-099", sec=S738A,
         exp="The whole point of the balance is that the percentage of Na+ excreted remains constant at 1%; the doubling example on the page is GFR 200 ml/min with 200 meq filtered, 198 reabsorbed and 2 meq excreted. (Book p738)"),
    keep("MED-C6-106", sec=S738B),
    keep("MED-C6-105", sec=S738B),
    keep("MED-C6-100", sec=S738B),
    fix("MED-C6-101", "0.1 to 0.2", sec=S738B),
    keep("MED-C6-110", sec=S738B),
    fix("MED-C6-102", "Hydrostatic pressure (RIHP)", sec=S738B),
    keep("MED-C6-107", sec=S738B),
    keep("MED-C6-108", sec=S738B),
    keep("MED-C6-103", sec=S738B),
    keep("MED-C6-104", sec=S738B),
    keep("MED-C6-109", sec=S738B),
    # ---------------- p739 ----------------
    keep("MED-C6-111", sec=S739A),
    keep("MED-C6-112", sec=S739A),
    keep("MED-C6-113", sec=S739A),
    keep("MED-C6-114", sec=S739A),
    keep("MED-C6-115", sec=S739A),
    keep("MED-C6-116", sec=S739B),
    keep("MED-C6-117", sec=S739B),
    fix("MED-C6-125", "Afferent arteriolar constriction mediated by angiotensin II", sec=S739B),
    keep("MED-C6-133", sec=S739B),
    keep("MED-C6-129", sec=S739B),
    fix("MED-C6-118", "1-B, 2-A, 3-C, 4-D", sec=S739B),
    keep("MED-C6-126", sec=S739B),
    keep("MED-C6-127", sec=S739B),
    keep("MED-C6-128", sec=S739B),
    keep("MED-C6-119", sec=S739B),
    fix("MED-C6-120", "Peritubular capillary → vasa recta → renal medulla", sec=S739B),
    keep("MED-C6-130", sec=S739B),
    keep("MED-C6-121", sec=S739B),
    keep("MED-C6-132", sec=S739B),
    fix("MED-C6-122", "The afferent arteriole is not working and the efferent arteriole was maintaining GFR", sec=S739B),
    fix("MED-C6-123", "Afferent", sec=S739B),
    keep("MED-C6-131", sec=S739B,
         exp="Printed chain: Block prostaglandins → block afferent arteriolar dilatation → efferent arteriolar constriction → ↓ GFR & ↓ RBF. A back-arrow from '↓ GFR & ↓ RBF' to 'maintain GFR' is also drawn on the page; its intent is not explained and is flagged as a source caveat. (Book p739)"),
    fix("MED-C6-124", "Frank renal failure", sec=S739B),
]

assert len(seq) == 138, len(seq)
used = [q.get("id") for q in seq if q.get("id")]
assert len(set(used)) == len(used) == 132, (len(set(used)), len(used))   # 012 deliberately dropped (duplicate of 001)

questions = []
for i, q in enumerate(seq, 1):
    q["id"] = f"MED-C6-{i:03d}"
    questions.append(q)

unit_specs = [
    ("MED-U6-1", "GFR: definition, Starling forces & the calculation", S734A,
     "The definition, every line of the worked equation in printed order (down to 125 ml/min), then the figure's labels and arrows and the four boxes.", 1, 12),
    ("MED-U6-2", "Normal GFR & the single clinical use printed", S734B,
     "Normal 90–125 ml/min; CKD is classified on GFR; <15 ml/min is G5/ESRD, the uremic phase needing dialysis.", 13, 20),
    ("MED-U6-3", "Creatinine as the marker of GFR", S735A,
     "Best marker; produced in muscle from creatine, so it falls with lost muscle (amputation); pregnancy's independent significance with normal 0.3–0.6 mg/dL; printed as a 113 kDa molecule.", 21, 29),
    ("MED-U6-4", "GFR equations & the C&G versus MDRD/CKD-EPI table", S735B,
     "Cockcroft & Gault (obsolete, 140−age, 72, ×0.8, bed-side, not preferred), MDRD and CKD-EPI (preferred now; CKD-EPI best above 60), then the table row by row and the Schwartz heading.", 30, 51),
    ("MED-U6-5", "Schwartz equation & its K constants", S736A,
     "eGFR = K × length ÷ S.Cr, then the constants: pre-term 0.33, term 0.45 (if age not mentioned), 1–2 yr and adolescent girls 0.55, adolescent boys 0.7.", 52, 58),
    ("MED-U6-6", "Why creatinine misleads: determinants, drugs & the inverse curve", S736B,
     "The five disadvantages in printed order: 24–48 h lag; muscle mass, race, age after 40 and sex as printed; diet and obesity; cimetidine/trimethoprim; the inverse curve with its two worked examples.", 59, 74),
    ("MED-U6-7", "snGFR compensation, clearance formula & cystatin C", S737,
     "GFR = snGFR × nephron number and the hyperfiltration chain; the clearance formula; cystatin C's five properties, four advantages, three non-specific elevations and why it cannot replace creatinine.", 75, 92),
    ("MED-U6-8", "Renal autoregulation & glomerulo-tubular balance", S738A,
     "MAP 80–180; myogenic (stretch) reflex then adenosine-mediated tubulo-glomerular feedback with both flowchart branches and the graph; glomerulo-tubular balance with both worked examples at 1%.", 93, 106),
    ("MED-U6-9", "Filtration fraction & the pressure-natriuresis theory", S738B,
     "FF = GFR/RPF = 125/700 = 0.1–0.2 (PAH); the raised-FF chain to increased PCT reabsorption; the theory of pressure natriuresis and BP = CO × PVR, with its mechanism chain continuing on p739.", 107, 122),
    ("MED-U6-10", "Glomerular hemodynamics: arteriolar table & drug notes", S739B,
     "The four arteriolar bullets with their mediators, the five-row table with its favourable/unfavourable notes, medullary hypoxia, the normal-flow note, and the ACE-inhibitor and NSAID chains with their contraindications.", 123, 138),
]

units = []
for uid, title, sec, guide, a, b in unit_specs:
    units.append({"id": uid, "ch": 6, "n": int(uid.rsplit("-", 1)[1]), "title": title,
                  "sec": sec, "guide": REVISION + guide,
                  "qs": [f"MED-C6-{i:03d}" for i in range(a, b + 1)]})
assert [q for u in units for q in u["qs"]] == [q["id"] for q in questions]

out = {"chapter": 6, "title": "Renal Physiology", "pageRange": "734-739",
       "questions": questions, "units": units}
(ROOT / "data" / "ch06.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")

pages = [q["page"] for q in questions]
assert all(b >= a for a, b in zip(pages, pages[1:])), "page order"
for q in questions:
    m = re.search(r"\(Book p(\d+)\)$", q["exp"])
    assert m and int(m.group(1)) == q["page"], q["id"]
    assert len(q["opts"]) == 4 and len({o.strip().casefold() for o in q["opts"]}) == 4, q["id"]
    assert 0 <= q["ans"] <= 3
print(f"ch06: {len(questions)} questions, {len(units)} units")
