#!/usr/bin/env python3
"""Record the Ch 6 strict source-review manifest (run AFTER author_c6_review.py).

The ordered element->question checklist below was built by reading Part 1 PDF
pp42-47 (Book p734-739) top-to-bottom at 2x whole-page renders plus 4x-6x crops
of every formula, table cell, flowchart branch and figure label. This script only
serialises the recorded review with fresh PDF/content hashes; it never invents
coverage.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from check_source_coverage import content_digest

ROOT = Path(__file__).resolve().parent
PDF = "uploads/Medicine_Vol3_Part1_pages_705-759.pdf"
Q = [f"MED-C6-{i:03d}" for i in range(1, 139)]


def el(page, index, source, ids):
    return {"element": f"p{page}-e{index:03d}", "page": page, "source": source, "questionIds": ids}


pages = [
    {"page": 734, "pdfPage": 42,
     "traversal": ("Read top-to-bottom: chapter title 'RENAL PHYSIOLOGY'; 'Glomerular Filtration Rate (GFR)' "
                   "heading; Definition line; Calculation lines in printed order (GFR = net UF pressure x UF "
                   "coefficient; = [net HP - net OP] x UF coefficient; = [(glom cap HP - Bowman HP) - (glom cap OP "
                   "- Bowman OP)] x UF coefficient; = [(60-18)-(32-0)] x 12.5; = 10 x 12.5; = 125 ml/min); the "
                   "glomerulus figure (afferent/efferent labels, the three pressure labels with arrows), then the "
                   "four boxes left-to-right; 'Normal GFR' line; 'Use' heading, CKD line and the Eg line with its "
                   "parenthesis. Timestamp, 'Active space' and header excluded."),
     "elements": [
         el(734, 1, "Definition: amount of urine filtered by all the nephrons in both kidneys in one minute.", [Q[0]]),
         el(734, 2, "GFR = Net ultrafiltration pressure x ultrafiltration (UF) coefficient.", [Q[1]]),
         el(734, 3, "= [Net Hydrostatic Pressure (H.P) - Net Oncotic pressure (O.P)] x UF coefficient.", [Q[2]]),
         el(734, 4, "= [(Glomerular Capillary HP - Bowman's space HP) - ...]: hydrostatic bracket, worked as 60-18 = 42.", [Q[3]]),
         el(734, 5, "... - (Glomerular Capillary OP - Bowman's space OP)] x UF coefficient, Bowman's OP = 0 in the next line.", [Q[4]]),
         el(734, 6, "= [(60 mmHg - 18 mmHg) - (32 mmHg - 0)] x 12.5 ml/min/mmHg: the UF coefficient value.", [Q[5]]),
         el(734, 7, "= 10 x 12.5 ml/min: net filtration pressure 10 (also the left box below the figure).", [Q[6]]),
         el(734, 8, "= 125 ml/min.", [Q[7]]),
         el(734, 9, "Figure pressure labels: glomerular hydrostatic pressure (60 mm Hg), glomerular colloid osmotic pressure (32 mm Hg), Bowman's capsule pressure (18 mm Hg).", [Q[8]]),
         el(734, 10, "Figure arrows: two arrows out of the capillary, Bowman's capsule pressure arrow pointing back at it.", [Q[9]]),
         el(734, 11, "Figure vessel labels: Afferent arteriole (left), Efferent arteriole (right).", [Q[10]]),
         el(734, 12, "Boxes: Net filtration pressure (10) = glomerular hydrostatic (60) - Bowman's capsule (18) - glomerular oncotic (32).", [Q[11]]),
         el(734, 13, "Normal GFR: 90-125 ml/min.", [Q[12], Q[13]]),
         el(734, 14, "Use: Chronic Kidney Disease (CKD) is classified based on GFR.", [Q[14], Q[15]]),
         el(734, 15, "Eg: GFR <15 ml/min: G5/End Stage Renal Disease (ESRD)/uremic phase (Dialysis required).", [Q[16], Q[17], Q[18]]),
         el(734, 16, "Page consolidation (odd one out) positioned after every line.", [Q[19]]),
     ]},
    {"page": 735, "pdfPage": 43,
     "traversal": ("Read top-to-bottom: 'CREATININE' heading and its four bullets; 'Equations to calculate GFR' "
                   "heading; '1. Cockroft & Gault equation: Obsolete' with the male formula, the female formula, "
                   "'Bed side formula', 'Not preferred now d/t disadvantages'; '2. MDRD equation' line; '3. CKD-EPI "
                   "equation' with its two bullets, the bracket 'Preferred now' spanning 2 and 3; the two-column "
                   "table read row by row, left cell then right cell (row 1 Overestimate GFR / Directly measures "
                   "GFR; row 2 Jaffe's method / IDM; row 3 Over emphasis on BW / Race used instead of weight); "
                   "'4. Schwartz equation: Estimate GFR in children'. Header, 'Active space' and footer excluded."),
     "elements": [
         el(735, 1, "Best marker to estimate GFR.", [Q[20]]),
         el(735, 2, "Produced in muscle from creatine -> decreased when muscle mass reduced (eg: amputation).", [Q[21], Q[22], Q[23]]),
         el(735, 3, "Pregnancy: only condition where high creatinine values significant independently (Normal: 0.3-0.6 mg/dL).", [Q[24], Q[25], Q[26]]),
         el(735, 4, "113 Kda molecule (printed as such).", [Q[27]]),
         el(735, 5, "Creatinine block consolidation (odd one out), after the four bullets.", [Q[28]]),
         el(735, 6, "1. Cockroft & Gault equation: Obsolete.", [Q[29]]),
         el(735, 7, "CrCl = (140-age) x body weight (BW) / (72 x S.creatinine) in males.", [Q[30], Q[31]]),
         el(735, 8, "= (140-age) x BW x 0.8 / (72 x S.Cr) in females.", [Q[32]]),
         el(735, 9, "Bed side formula.", [Q[33]]),
         el(735, 10, "Not preferred now d/t disadvantages.", [Q[34]]),
         el(735, 11, "2. MDRD equation: by society for modification of diet & renal diseases.", [Q[35]]),
         el(735, 12, "3. CKD-EPI equation: by CKD-Epidemiology problem initiative group (match consolidating 2, 3 and 4).", [Q[36]]),
         el(735, 13, "Best (Advantage when GFR > 60).", [Q[37]]),
         el(735, 14, "Bracket 'Preferred now' spanning MDRD and CKD-EPI.", [Q[38], Q[39]]),
         el(735, 15, "Table row 1 left: Overestimate GFR: d/t assumption that CrCl = GFR (only true for inert molecules like inulin).", [Q[40]]),
         el(735, 16, "Row 1 left cont.: Cr is secreted -> CrCl = GFR + tubular secretion (Clearance = GFR + tubular secretion or GFR - tubular absorption).", [Q[41], Q[42]]),
         el(735, 17, "Row 1 right: Directly measures GFR.", [Q[43]]),
         el(735, 18, "Row 2 left: Equation developed when Cr estimated by Jaffe's method: colorimetric assay using alkaline picrate (not standard method).", [Q[44]]),
         el(735, 19, "Row 2 right: Equation uses estimation of Cr using standard assays: IDM (Isotope dilution mass spectrosopy [sic]).", [Q[45]]),
         el(735, 20, "Row 3 left: Over emphasis on BW.", [Q[46]]),
         el(735, 21, "Row 3 right: Race used instead of weight (table consolidation, odd one out).", [Q[47]]),
         el(735, 22, "4. Schwartz equation: Estimate GFR in children.", [Q[48]]),
     ]},
    {"page": 736, "pdfPage": 44,
     "traversal": ("Read top-to-bottom: eGFR = K x length of child / S.Cr with the K-constant parenthesis on the "
                   "right (<1 yr: pre-term 0.33, term 0.45 (if age not mentioned); 1-2 yr & adolescent girls 0.55; "
                   "adolescent boys 0.7); 'Disadvantages of creatinine' 1 (24-48 hrs), 2 'Dependent on' four "
                   "bullets (muscle mass, race, age, sex), 3 'Diet alters S.Cr' two arrows plus the obesity "
                   "parenthesis, 4 'Affected by drugs' cimetidine/trimethoprim bracket and the three-step flow, "
                   "5 'Inverse relationship' two bullets, the graph (2 mg/dL vs 60 ml/min highlighted), the "
                   "'By the time S.Cr = 2' line and the two Eg lines. Header/'Active space'/footer excluded."),
     "elements": [
         el(736, 1, "eGFR = K x length of child / S.Cr (K = constant).", [Q[49], Q[50]]),
         el(736, 2, "K: <1 yr pre-term 0.33; term 0.45 (if age not mentioned).", [Q[51]]),
         el(736, 3, "K: 1-2 yr & adolescent girls 0.55; adolescent boys 0.7 (full match after all four values).", [Q[52], Q[53]]),
         el(736, 4, "K-constant consolidation (odd one out) and 'changed according to' item, after the values.", [Q[54], Q[55]]),
         el(736, 5, "Disadvantage 1: 24-48 hrs to start rising in Acute Kidney Injury (AKI).", [Q[56], Q[57]]),
         el(736, 6, "2. Dependent on: amount of muscle mass (down muscle mass -> down Cr); race (down in African Americans).", [Q[58]]),
         el(736, 7, "Age (down after 40 years d/t down in muscle mass).", [Q[59], Q[60]]),
         el(736, 8, "Sex (down in males) - printed wording, flagged.", [Q[61]]),
         el(736, 9, "3. Diet alters S.Cr: down protein supplementation -> down muscle mass -> down S.Cr; malnutrition -> down muscle mass -> down S.Cr.", [Q[62]]),
         el(736, 10, "(Obesity: no change in S.Cr as fat doesn't affect S.Cr).", [Q[63], Q[64]]),
         el(736, 11, "4. Affected by drugs: cimetidine, trimethoprim -> compete with Cr for tubular secretion -> down tubular secretion of Cr -> up serum Cr.", [Q[65], Q[66]]),
         el(736, 12, "5. Inverse relationship: by the time Cr rises, GFR falls significantly; initial rise in Cr corresponds to significant fall in GFR.", [Q[67]]),
         el(736, 13, "Graph and caption line: by the time S.Cr = 2, GFR falls to ~60 ml/min.", [Q[68]]),
         el(736, 14, "Eg: up S.Cr from 5 to 20: fall in GFR is insignificant (patient was already in ESRD).", [Q[69]]),
         el(736, 15, "Up S.Cr from 1.7 to 2.8: GFR falls significantly (50 ml/min -> 30 ml/min).", [Q[70], Q[71]]),
     ]},
    {"page": 737, "pdfPage": 45,
     "traversal": ("Read top-to-bottom: 'Note' with GFR = snGFR x number of nephrons; the compensation line and "
                   "the vertical chain (Beyond point of compensation -> intraglomerular HTN -> proteinuria -> "
                   "interstitial fibrosis -> down GFR); 'Endogenous creatinine clearance' two formula bullets; "
                   "'CYSTATIN C' bullets read left column top-to-bottom (13 kDa, cysteine protease inhibitor, "
                   "constant production) then right column (filtered but not secreted, reabsorbed by PCT); "
                   "'Advantages: not affected by' left column (race, diet) then right (muscle mass, drugs); "
                   "'Disadvantages: non specifically elevated in' three bullets; 'Therefore, cannot replace Cr'."),
     "elements": [
         el(737, 1, "GFR = single nephron GFR x number of nephrons.", [Q[72]]),
         el(737, 2, "Even if number down -> snGFR up to maintain GFR (hyperfiltration injury), arrow labelled 'Beyond point of compensation'.", [Q[73]]),
         el(737, 3, "Chain: intraglomerular HTN -> proteinuria -> interstitial fibrosis -> down GFR (two sequence items).", [Q[74], Q[75]]),
         el(737, 4, "Clearance = urine concentration x volume of urine in ml/min (V) / plasma concentration.", [Q[76], Q[77]]),
         el(737, 5, "Endogenous Cr clearance = Ucr x V / Pcr.", [Q[78], Q[79]]),
         el(737, 6, "Cystatin C: 13 kDa molecule protein; cysteine protease inhibitor; produced at constant rate by all nucleated cells.", [Q[80]]),
         el(737, 7, "Filtered but not secreted; reabsorbed by PCT (plus block consolidations).", [Q[81], Q[82], Q[83]]),
         el(737, 8, "Advantages: not affected by race, diet, muscle mass, drugs.", [Q[84], Q[85]]),
         el(737, 9, "Disadvantages: non specifically elevated in inflammation, taking steroids, smokers.", [Q[86]]),
         el(737, 10, "Therefore, cannot replace Cr.", [Q[87]]),
         el(737, 11, "Cystatin C consolidations (scenario, match) positioned after every cystatin line.", [Q[88], Q[89]]),
     ]},
    {"page": 738, "pdfPage": 46,
     "traversal": ("Read top-to-bottom: 'Regulation of Renal Functions' heading; RENAL AUTOREGULATION two bullets; "
                   "'mechanism' 1 myogenic reflex, 2 tubulo glomerular feedback, then the two flowchart branches "
                   "(down-GFR branch complete, then up-GFR/tubular-injury branch complete), then the right-panel "
                   "autoregulation graph; GLOMERULO TUBULAR BALANCE arrow line, Eg GFR 100 column then GFR 200 "
                   "column; FILTRATION FRACTION formula with the RPF bracket, = 125/700 = 0.1 to 0.2, the up-FF "
                   "chain left-to-right; 'Theory of pressure natriuresis' bullet and its 'Therefore' sentence with "
                   "(BP = CO x PVR). Timestamp/'Active space'/footer excluded."),
     "elements": [
         el(738, 1, "Within auto regulation range (MAP: 80-180 mmHg).", [Q[90]]),
         el(738, 2, "Renal Blood Flow (RBF) and GFR are constant.", [Q[91]]),
         el(738, 3, "Mechanism 1. Myogenic reflex (stretch reflex).", [Q[92]]),
         el(738, 4, "2. Tubulo glomerular feedback (adenosine mediated).", [Q[93]]),
         el(738, 5, "In response to down GFR (eg: pre renal failure) -> afferent arteriolar vasodilatation -> up filtration.", [Q[94], Q[95]]),
         el(738, 6, "Up GFR/tubular injury (eg: acute tubular injury) -> up NaCl/KCl reach macula densa -(adenosine)-> afferent arteriolar vasoconstriction -> down filtration.", [Q[96], Q[97], Q[98]]),
         el(738, 7, "Autoregulation graph: flow rate vs mean arterial pressure, autoregulatory range marked, RBF and GFR curves.", [Q[99]]),
         el(738, 8, "Glomerulo tubular balance: up GFR -> up reabsorption by tubule (compensation) -> % of Na+ excreted remains constant.", [Q[100]]),
         el(738, 9, "Eg: GFR = 100 ml/min, Na+ filtered = 100 meq -> 99 meq reabsorbed, 1 meq excreted (1%).", [Q[101]]),
         el(738, 10, "GFR = 200 ml/min, Na+ filtered = 200 meq -> 198 meq reabsorbed, 2 meq excreted (1%).", [Q[102], Q[103]]),
         el(738, 11, "FF = GFR / Renal plasma flow (RPF) [RPF = 700 ml: estimated using Para Amino Hippuric acid (PAH)].", [Q[104], Q[105], Q[106]]),
         el(738, 12, "= 125/700 = 0.1 to 0.2.", [Q[107], Q[108]]),
         el(738, 13, "Up FF -> up peritubular capillary OP (d/t more filtration) -(taken in fluid from interstitial space)-> down renal interstitial HP (RIHP) -> up reabsorption from PCT.", [Q[109], Q[110], Q[111]]),
         el(738, 14, "Theory of pressure natriuresis: up CO leads to up excretion of Na+ & H2O.", [Q[112]]),
         el(738, 15, "Therefore, up CO cannot produce sustained up in BP unless there is renal impairment (BP = CO x PVR).", [Q[113], Q[114]]),
     ]},
    {"page": 739, "pdfPage": 47,
     "traversal": ("Read top-to-bottom: 'mechanism' chain (up CO -> up RBF -> down reabsorption from PCT -> up RIHP "
                   "-> up medullary blood flow -> up Na+ & H2O excretion); GLOMERULAR HEMODYNAMICS heading; the "
                   "four left-hand arteriolar bullets top-to-bottom with their mediators; the table (header row, "
                   "Control row with Afferent/Efferent/Glomerulus labels, then increased afferent, decreased "
                   "afferent, increased efferent, decreased efferent rows with their arrows and right-margin "
                   "favourable/unfavourable notes); efferent constriction -> medullary hypoxia line; 'Note: Normal "
                   "blood flow' chain; ACE Inhibitor block (beneficial chain, C/I in b/l RAS); NSAID block "
                   "(prostaglandin chain with the back-arrow, C/I in patients on ACEI). Header/'Active space'/footer excluded."),
     "elements": [
         el(739, 1, "Mechanism: up CO -> up RBF -> down reabsorption from PCT -> up RIHP -> up medullary blood flow -> up Na+ & H2O excretion.", [Q[115], Q[116], Q[117], Q[118], Q[119]]),
         el(739, 2, "Afferent arteriolar constriction; afferent arteriolar dilatation (mediated by prostaglandins).", [Q[120]]),
         el(739, 3, "Efferent arteriolar constriction (mediated by angiotensin II); efferent arteriolar dilatation.", [Q[121], Q[122], Q[123]]),
         el(739, 4, "Table header and Control row: Arteriolar resistance / Renal blood flow / Net ultrafiltration pressure; Glomerulus, Afferent, Efferent labels.", [Q[124]]),
         el(739, 5, "Rows: increased afferent (down, down) unfavourable; decreased afferent (up, up) favourable for kidney; increased efferent (down, up); decreased efferent (up, down) unfavourable.", [Q[125], Q[126], Q[127], Q[128]]),
         el(739, 6, "Efferent arteriolar constriction -> down blood flow to medulla -> medullary hypoxia.", [Q[129]]),
         el(739, 7, "Note: Normal blood flow: efferent arteriole -> peritubular capillary -> vasa recta -> renal medulla.", [Q[130], Q[131]]),
         el(739, 8, "ACE Inhibitor: beneficial for nephrology patients: block angiotensin II -> efferent arteriolar dilatation -> down GFR (up S.Cr) but up blood flow.", [Q[132], Q[133]]),
         el(739, 9, "C/I in patients with b/l renal artery stenosis: afferent arteriole not working, efferent arteriole maintains GFR.", [Q[134]]),
         el(739, 10, "NSAID: block prostaglandins -> block afferent arteriolar dilatation -> efferent arteriolar constriction -> down GFR & down RBF (back-arrow to 'maintain GFR').", [Q[135], Q[136]]),
         el(739, 11, "C/I in patients on ACEI: ACEI -> efferent arteriolar constriction blocked -> frank renal failure.", [Q[137]]),
     ]},
]

chapter = json.loads((ROOT / "data" / "ch06.json").read_text())
manifest = {
    "chapter": 6,
    "reviewedAt": "2026-09-22",
    "status": "reviewed-with-source-caveats",
    "pdf": PDF,
    "pdfSha256": hashlib.sha256((ROOT / PDF).read_bytes()).hexdigest(),
    "pdfOffset": 692,
    "pageRange": "734-739",
    "contentSha256": content_digest(chapter),
    "method": ("All six printed pages read from the supplied Part 1 PDF (whole-page renders at 2x plus 4x-6x crops "
               "of every formula, table cell, flowchart branch, graph and figure label), with explicit local "
               "traversals recorded per page. Every question's stored answer index was checked against the print; "
               "35 wrong keys (introduced by migrate_parts.py's rotation heuristic) were corrected. Contiguous "
               "lines share an item; consolidation items sit after the lines they test and never pull later "
               "material forward. Headers, timestamps, footers and blank Active space excluded."),
    "caveats": [
        "p734: the hand-written net-pressure line reads '= 10 x 12.5 ml/min' and the figure boxes restate the same 10/60/18/32 values; the 42 mmHg hydrostatic difference is a worked intermediate, not a printed number.",
        "p735: prints 'Cockroft' (standard: Cockcroft), '113 Kda molecule' for creatinine (the true molecular weight is 113 Da; taught as printed and not corrected), 'IDM' in red with the parenthesis 'Isotope dilution mass spectrosopy' (missing 'c'), and 'CKD- Epidemiology problem initiative group' as the CKD-EPI expansion. All taught as printed.",
        "p736: the 'Dependent on' list prints 'Sex (down in males)'. Physiologically male creatinine is higher; the print is quoted verbatim and flagged in the explanation, not corrected.",
        "p736: the graph is a printed hyperbola with 2 (mg/dL) and 60 (mL/min) highlighted; the two Eg lines are hand-written under it and are taught as printed.",
        "p739: the NSAID chain draws a back-arrow from 'down GFR & down RBF' to 'maintain GFR' whose intent is not explained; flagged in the explanation. The table's right-margin words 'unfavourable' / 'Favourable for Kidney' / 'unfavourable' sit level with rows 2, 3 and 5; row 4 (increased efferent) carries no annotation.",
    ],
    "pages": pages,
}

out = ROOT / "data" / "source_review" / "ch06.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"wrote {out} ({sum(len(p['elements']) for p in pages)} elements)")
