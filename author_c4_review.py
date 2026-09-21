#!/usr/bin/env python3
"""Rebuild Ch 4 (Juxtaglomerular Apparatus, p726-729) in strict source order.

Source review 2026-09-21: all four pages read from the Part 1 scan (PDF pp34-37).
Repairs vs the 50-question bank:
  * MED-C4-005 pulled p727 JG-cell facts (granular/tunica media) into a p726
    match -> re-authored to p726-only content (composition/site/function match).
  * Findings questions sat on p727 while the findings print on p726 -> moved to
    p726 (new MED-C4-013) and given their own H+/acidosis item (new MED-C4-014).
  * MED-C4-022 (old) had TWO correct answers (pre-renal AND post-renal are both
    outside-kidney) -> re-authored as a true/false item (new MED-C4-025).
  * MED-C4-043 (cortex/medulla perfusion) sat after the vascularity-figure
    questions -> moved before them (new MED-C4-043).
  * Every JG-apparatus figure label (p726) and every vascularity-of-nephron
    figure label (p728) is now directly questioned; the old bank tested only
    the efferent arteriole and a 3-label subset.
  * Q009 converted to a clinical scenario (gentamicin case); Q045 stem now
    carries the printed "hours to days" AKI timeframe.
Result: 55 questions in 7 retained units. Unit guides carry the revision note
(previous badges/XP retained; replay recommended), as in the Ch 1-3 repairs.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = json.loads((ROOT / "data" / "ch04.json").read_text())
# One-shot repair script: the input must be the pre-review 50-question bank
# (commit 019913f). Refuse to run against the rebuilt bank or any other base.
if len(OLD["questions"]) != 50 or "Source-order revision" in OLD["units"][0].get("guide", ""):
    raise SystemExit("author_c4_review.py expects the pre-review 50-question data/ch04.json as input; refusing to re-run.")
BY_ID = {q["id"]: dict(q) for q in OLD["questions"]}

REVISION = ("Source-order revision, 21 Sep 2026: questions have been repaired, "
            "expanded and reordered. Previous completion badges and XP are retained; "
            "replay this unit to cover the revised questions. ")


def keep(old_id, **over):
    q = dict(BY_ID[old_id])
    q.update(over)
    return q


def new(qid_seq, sec, page, fmt, q, opts, ans, exp):
    return {"id": qid_seq, "sec": sec, "page": page, "q": q, "opts": opts,
            "ans": ans, "exp": exp, "fmt": fmt}


SEC_MD = "JGA components & macula densa"
SEC_TI = "TG feedback: tubular injury"
SEC_DH = "TG feedback: dehydration & AKI"
SEC_JG = "JG cells & renin"
SEC_RC = "Renal circulation"
SEC_CM = "Cortex vs medulla supply"
SEC_RD = "Renal diseases tree"

# Ordered (old_id | new-dict, ) sequence -------------------------------------
seq = [
    # ---- p726: components / macula densa text ----
    keep("MED-C4-001"),
    keep("MED-C4-002"),
    keep("MED-C4-003"),
    keep("MED-C4-004"),
    new(None, SEC_MD, 726, "match",
        "Match each macula densa fact with its detail — 1) Composition 2) Site 3) Function … "
        "A) TG feedback mediated by adenosine B) Modified tall columnar cells C) Cortical TAL / distal straight tubule",
        ["1-B, 2-C, 3-A", "1-A, 2-C, 3-B", "1-C, 2-A, 3-B", "1-B, 2-A, 3-C"], 0,
        "Macula densa: modified tall columnar cells (composition) in the cortical TAL/distal straight tubule (site), "
        "doing TG feedback via adenosine (function). (Book p726)"),
    keep("MED-C4-006"),
    keep("MED-C4-007"),
    # ---- p726: JG apparatus figure labels ----
    new(None, SEC_MD, 726, "match",
        "Match each label in the JG apparatus figure with where its leader points — 1) Internal elastic lamina "
        "2) Glomerular epithelium 3) Basement membrane … A) Wall of the distal tubule in cross-section "
        "B) Top wall of the arteriole C) Covering of the glomerular tuft",
        ["1-B, 2-C, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B", "1-B, 2-A, 3-C"], 0,
        "Internal elastic lamina → top arteriole wall; glomerular epithelium → tuft covering; "
        "basement membrane → distal tubule wall. (Book p726)"),
    new(None, SEC_MD, 726, "oddoneout",
        "All of the following are labelled in the JG apparatus figure EXCEPT:",
        ["Thin ascending limb of Henle", "Distal tubule (Straight)", "Macula densa", "Juxtaglomerular cells"], 0,
        "The figure labels distal tubule (straight), macula densa and JG cells (with efferent arteriole, smooth muscle "
        "layer, internal elastic lamina, glomerular epithelium and basement membrane); no thin ascending limb. (Book p726)"),
    # ---- p726: row 1 + row 2 of the sequence table ----
    keep("MED-C4-008"),
    new(None, SEC_TI, 726, "scenario",
        "A patient started on gentamicin develops renal tubular injury with PCT damage in under 24 hours. "
        "In the book's phase-1 MOA, gentamicin is the example of:",
        ["A tubulotoxic drug", "A prostaglandin inhibitor", "A β1-receptor blocker", "An adenosine antagonist"], 0,
        "Renal tubular injury from tubulotoxic drugs (eg. gentamicin) → PCT injury within < 24 hrs. (Book p726)"),
    keep("MED-C4-010"),
    keep("MED-C4-013", page=726,
         exp="TG-feedback phase findings: ↓GFR, ↑S.creatinine, ↑K+ → cardiac arrhythmias, ↑H+ → metabolic acidosis; "
             "GFR falls, not rises. (Book p726)"),
    new(None, SEC_TI, 726, "recall",
        "In the TG-feedback phase, the raised H+ load leads to:",
        ["Metabolic acidosis", "Metabolic alkalosis", "Respiratory acidosis", "Respiratory alkalosis"], 0,
        "Phase-2 findings: ↑H+ → metabolic acidosis (with ↓GFR, ↑S.creatinine and ↑K+ → cardiac arrhythmias). (Book p726)"),
    keep("MED-C4-011"),
    keep("MED-C4-012"),
    # ---- p727: table continued (Mx / MOA / recovery) ----
    keep("MED-C4-015"),
    keep("MED-C4-014",
         q="Which of the following statements about the TG-feedback MOA is TRUE?",
         opts=["Afferent arteriolar constriction lowers GFR (glomerular filtration rate) and prevents further salt + H2O loss",
               "Afferent constriction raises GFR to flush the tubule",
               "Efferent dilatation is the protective step",
               "The feedback increases urinary salt loss"],
         exp="Constricts afferent arteriole → ↓GFR (glomerular filtration rate) → ↑S.creatinine and prevents further salt + H2O "
             "loss due to impaired reabsorption. (Book p727)"),
    keep("MED-C4-016"),
    # ---- p727: dehydration chain ----
    keep("MED-C4-017"),
    keep("MED-C4-018"),
    keep("MED-C4-019"),
    keep("MED-C4-020"),
    keep("MED-C4-021"),
    # ---- p727: AKI causes note (old 022 had two correct answers: re-authored) ----
    new(None, SEC_DH, 727, "truefalse",
        "Which of the following statements about the book's AKI cause groups is TRUE?",
        ["Inside-kidney causes are ATI/ATN and acute interstitial nephritis",
         "Pre-renal causes arise inside the kidney",
         "Post-renal causes arise inside the kidney",
         "ATI/ATN arises outside the kidney"], 0,
        "Outside kidney = pre-renal + post-renal; inside kidney = ATI/ATN + AIN. (Book p727)"),
    keep("MED-C4-023"),
    # ---- p727: JG cells ----
    keep("MED-C4-024"),
    keep("MED-C4-025"),
    keep("MED-C4-026"),
    # ---- p728: renin stimulator diagram ----
    keep("MED-C4-027"),
    keep("MED-C4-028"),
    keep("MED-C4-029"),
    # ---- p728: renal circulation chain ----
    keep("MED-C4-030"),
    keep("MED-C4-031"),
    keep("MED-C4-032"),
    keep("MED-C4-033"),
    keep("MED-C4-034"),
    keep("MED-C4-035"),
    keep("MED-C4-036"),
    keep("MED-C4-037"),
    # ---- p728: cortex vs medulla table ----
    keep("MED-C4-038"),
    keep("MED-C4-039"),
    keep("MED-C4-043"),
    # ---- p728: vascularity-of-nephron figure, top to bottom ----
    new(None, SEC_CM, 728, "match",
        "Match each label in the vascularity-of-nephron figure with the structure it names — 1) Afferent arteriole "
        "2) Proximal convoluted tubule 3) Glomerular capsule … A) Vessel entering the glomerular tuft "
        "B) Cup around the glomerular tuft C) Tubule segment coiling beside the glomerulus",
        ["1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B"], 0,
        "Afferent arteriole enters the tuft; proximal convoluted tubule coils beside the glomerulus; "
        "glomerular capsule cups the tuft. (Book p728)"),
    new(None, SEC_CM, 728, "recall",
        "In the vascularity figure, the red vessel ascending beside the tubule and the blue vessel with its small tributary are labelled:",
        ["Interlobular artery, and interlobular vein with venule",
         "Interlobar artery, and interlobar vein with venule",
         "Arcuate artery, and arcuate vein with venule",
         "Segmental artery, and segmental vein with venule"], 0,
        "Figure labels: interlobular artery (red) with interlobular vein and its venule (blue). (Book p728)"),
    keep("MED-C4-041"),
    keep("MED-C4-040"),
    keep("MED-C4-042"),
    # ---- p729: renal diseases tree ----
    keep("MED-C4-044"),
    keep("MED-C4-045",
         q="In AKI (hours to days), match each lesion with its m/c cause — 1) ATN 2) AIN … A) Drug hypersensitivity B) Ischemia"),
    keep("MED-C4-046"),
    keep("MED-C4-047"),
    keep("MED-C4-048"),
    keep("MED-C4-049"),
    keep("MED-C4-050"),
]

assert len(seq) == 55, len(seq)

questions = []
for i, q in enumerate(seq, 1):
    q["id"] = f"MED-C4-{i:03d}"
    questions.append(q)

unit_specs = [
    ("MED-U4-1", "JGA components & the macula densa", "Macula Densa & JG cells · p726",
     "The three JGA components, macula densa composition/site/function (adenosine-mediated TG feedback) and every label of the JG-apparatus figure.", 1, 9),
    ("MED-U4-2", "TG feedback: sequence of tubular injury", "Macula Densa & JG cells · p726-727",
     "The phases/MOA table: <24 h tubular injury (gentamicin → PCT), TG-feedback findings, Cl->K+>Na+ sensing, adenosine release, afferent-constriction consequences, management and the recovery row.", 10, 19),
    ("MED-U4-3", "TG feedback in dehydration & AKI cause groups", "Macula Densa & JG cells · p727",
     "The dehydration (vomiting → pre-renal) chain with prostaglandin-mediated afferent dilatation, plus the inside/outside-kidney AKI cause note.", 20, 26),
    ("MED-U4-4", "JG cells & renin release", "Macula Densa & JG cells · p727-728",
     "JG cell composition (granular), site (tunica media, afferent > efferent), function (renin) and the three positive stimulators of renin release.", 27, 32),
    ("MED-U4-5", "Renal circulation: artery to IVC", "Vascular Anatomy of Kidney · p728",
     "The full circulation chain: end artery, 5 segmental arteries, interlobar/arcuate/interlobular stations, glomerular and peritubular plexuses, vasa recta limbs and venous return to the IVC.", 33, 40),
    ("MED-U4-6", "Cortex vs medulla supply & nephron vascularity", "Vascular Anatomy of Kidney · p728",
     "The cortex/medulla supply table, the hypoxia-vulnerable pars recta, the efferent-arteriole 'sandwich' note and every label of the vascularity-of-nephron figure.", 41, 48),
    ("MED-U4-7", "Renal diseases tree (85% vs 5%)", "Renal diseases note · p729",
     "The closing note: tubulointerstitial (85%) AKI/CKD arms with their m/c causes and RTA-4 endpoint, and the vascular (5%) arm with RAS, TMA and hypertensive crisis to ischemic nephropathy.", 49, 55),
]

units = []
for uid, title, sec, guide, a, b in unit_specs:
    units.append({"id": uid, "ch": 4, "n": int(uid.rsplit("-", 1)[1]), "title": title,
                  "sec": sec, "guide": REVISION + guide,
                  "qs": [f"MED-C4-{i:03d}" for i in range(a, b + 1)]})

out = {"chapter": 4, "title": "Juxtaglomerular Apparatus", "pageRange": "726-729",
       "questions": questions, "units": units}
(ROOT / "data" / "ch04.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")

# Sanity: pages non-decreasing, citations match, 4 distinct options.
pages = [q["page"] for q in questions]
assert all(b >= a for a, b in zip(pages, pages[1:])), "page order"
import re
for q in questions:
    m = re.search(r"\(Book p(\d+)\)$", q["exp"])
    assert m and int(m.group(1)) == q["page"], q["id"]
    assert len(q["opts"]) == 4 and len({o.strip().casefold() for o in q["opts"]}) == 4, q["id"]
print(f"ch04: {len(questions)} questions, {len(units)} units")
