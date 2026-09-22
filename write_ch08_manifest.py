#!/usr/bin/env python3
"""Record the Ch 8 strict source-review manifest (run AFTER author_c8_review.py).

Element checklist built by reading Part 1 PDF pp56-60 (Book p748-752) top-to-bottom
at 2x whole-page renders; flowcharts read branch by branch left-to-right. This script
only serialises the recorded review with fresh hashes; it never invents coverage.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from check_source_coverage import content_digest

ROOT = Path(__file__).resolve().parent
PDF = "uploads/Medicine_Vol3_Part1_pages_705-759.pdf"


def Q(*ns):
    return [f"MED-C8-{n:03d}" for n in ns]


def el(page, index, source, ids):
    return {"element": f"p{page}-e{index:03d}", "page": page, "source": source, "questionIds": ids}


pages = [
    {"page": 748, "pdfPage": 56,
     "traversal": ("Chapter title; INITIAL INVESTIGATION tree left-to-right: USG abdomen; RFT (urea, creatinine, Na+, K+); Urine analysis "
                   "(24hr protein (Preferred), albumin/creatinine, protein/creatinine); 'Approach': USG abdomen (most important); Look for "
                   "three bullets; CMD Present -> CKD -> Hemodialysis / Transplant; Absent -> Non-CKD; 'USG ABDOMEN In CKD': normal kidney "
                   "labels (isoechoic cortex, hypoechoic pyramid, hyperechoic fat/calyx/sinus/vessels) and 'Chronic Kidney Failure' images "
                   "captioned 'CMD lost'."),
     "elements": [
         el(748, 1, "Initial investigation: USG abdomen; RFT - S. urea, S. creatinine, S. Na+, S. K+.", Q(1, 2)),
         el(748, 2, "Urine analysis: 24hr protein (Preferred); albumin/creatinine; protein/creatinine.", Q(3, 4)),
         el(748, 3, "Approach: USG abdomen (most important).", Q(5)),
         el(748, 4, "Look for: kidney size <8 cm; 8-10 cm loss of CMD.", Q(6, 7, 8)),
         el(748, 5, ">10 cm with loss of CMD with: DM, HIV, amyloidosis.", Q(9, 10)),
         el(748, 6, "CMD Present -> CKD; Absent -> Non-CKD.", Q(11, 12)),
         el(748, 7, "CKD -> Hemodialysis / Transplant.", Q(13)),
         el(748, 8, "Normal kidney: isoechoic cortex; hypoechoic pyramid; hyperechoic fat, calyx, sinus, vessels.", Q(14, 15)),
         el(748, 9, "Chronic kidney failure images: 'Cortico medullary differentiation (CMD) lost'.", Q(16)),
     ]},
    {"page": 749, "pdfPage": 57,
     "traversal": ("'Rule out hydroureteronephrosis before diagnosing CKD' + images captioned 'Calyces becoming prominent and ureter seen'; "
                   "Non-CKD tree: Days to weeks -> RPRF -> RPGN (m/c, biopsy), severe ATN / TMA (rare cause); Hypertensive crisis: vascular "
                   "cause -> RAS (large vessel) / TMA (small vessel); Normal RFT with renal disease -> nephrotic syn, RTA type I/II, "
                   "asymptomatic urine abnormality; Hours to days -> AKI -> postrenal, pre-renal, ATN, AIN; 'Renal Artery Stenosis' heading "
                   "two bullets."),
     "elements": [
         el(749, 1, "Rule out hydroureteronephrosis before diagnosing CKD; calyces becoming prominent and ureter seen.", Q(17)),
         el(749, 2, "Days to weeks -> RPRF -> RPGN (m/c; diagnosed with biopsy); severe ATN; TMA - rare cause.", Q(18, 19, 20, 21)),
         el(749, 3, "Hypertensive crisis: vascular cause -> RAS (large vessel kidney disease); TMA (small vessel kidney disease).", Q(22, 23)),
         el(749, 4, "Normal RFT with renal disease -> nephrotic syn; renal tubular acidosis type I/II; asymptomatic urine abnormality.", Q(24)),
         el(749, 5, "Hours to days -> AKI: postrenal B/L hydroureteronephrosis (USG); pre-renal investigation: normal urine analysis; ATN; AIN (printed 'nephrosis').", Q(25, 26, 27, 28)),
         el(749, 6, "Non-CKD tempo consolidation (match across the three arms).", Q(29)),
         el(749, 7, "RAS: AKA renovascular HTN (RVH) / renal artery occlusion disease (RAOD); can progress to CKD / ischemic nephropathy.", Q(30, 31)),
     ]},
    {"page": 750, "pdfPage": 58,
     "traversal": ("'most common' tree left-to-right: Overall atherosclerosis (proximal 1-2 cm; symptomatic >80%); Young population FMD "
                   "(arteriopathy; mid to distal); Indian/Asian Takayasu (F:m 9:1; proximal); Young males PAN (entire length; microaneurysm); "
                   "TYPES Goldblatt; Unilateral RAS pathogenesis: asymmetric kidney size; clip drawing; affected-kidney chain; normal-kidney "
                   "chain (pressure natriuresis theory); Note: asymmetric kidney seen in; vasoconstriction potency; C/F; basic investigation."),
     "elements": [
         el(750, 1, "Overall: atherosclerosis - proximal renal artery (1-2 cm) - symptomatic >80% occlusion.", Q(32, 33)),
         el(750, 2, "Young population: fibromuscular dysplasia (arteriopathy) - mid to distal renal artery.", Q(34, 35)),
         el(750, 3, "Indian/Asian: Takayasu arteritis (F:m = 9:1) - proximal renal artery.", Q(36, 37)),
         el(750, 4, "Young males: polyarteritis nodosa - entire length renal artery - microaneurysm; tree consolidation.", Q(38, 39, 40)),
         el(750, 5, "TYPES: explain by Goldblatt: two kidney one clip model.", Q(41)),
         el(750, 6, "Unilateral RAS pathogenesis: asymmetric kidney size (clip drawing).", Q(42)),
         el(750, 7, "Affected kidney: down RBF/perfusion ->(+) renin angiotensin system ->(+) up aldosterone -> up AT-II (up up) -> profound vasoconstriction -> up BP -> HTN/HTN crisis.", Q(43, 44, 45)),
         el(750, 8, "Normal kidney: up RBF/medullary flow -> up RIHP -> down reabsorption from PCT -> up excretion Na+/H2O (pressure natriuresis theory).", Q(46, 47)),
         el(750, 9, "Note: asymmetric kidney seen in vesicoureteral reflux; renal artery stenosis.", Q(48)),
         el(750, 10, "Vasoconstriction potency: urotension > endothelin > AT-II (printed spelling).", Q(49)),
         el(750, 11, "C/F: persistent HTN; basic investigation: RFT, urine analysis - normal range.", Q(50)),
     ]},
    {"page": 751, "pdfPage": 59,
     "traversal": ("Radiological investigation: on USG asymmetric kidney; screening test renal doppler -> Confirm -> IOC CT renal angio or MR "
                   "angiography (caption 'unilateral renal artery stenosis'); Treatment: ACEi/ARBs (DOC); PTRA only if kidney > 8 cm; "
                   "Bilateral RAS: poor prognosis; pathogenesis drawing (x - occlusion); left chain RBF -> RAS -> x; right chain loss of "
                   "pressure natriuresis -> Na+/H2O retention -> volume overload (-) -> recurrent flash pulmonary edema -> Rx B/L PTRA with "
                   "stenting; image 'Bilateral renal artery stenosis'; Treatment: in BP diuretics (DOC), ACEi/ARBs C/I; stop smoking; start statins."),
     "elements": [
         el(751, 1, "On USG: asymmetric kidney; screening test: renal doppler.", Q(51)),
         el(751, 2, "Confirm -> IOC: CT renal angio or MR angiography; caption 'unilateral renal artery stenosis'.", Q(52, 53)),
         el(751, 3, "Treatment: ACE inhibitors / ARBs (DOC).", Q(54)),
         el(751, 4, "PTRA - only if kidney size > 8 cm.", Q(55, 56)),
         el(751, 5, "Bilateral RAS: poor prognosis; drawing legend x - occlusion.", Q(57, 58)),
         el(751, 6, "Loss of pressure natriuresis / down RIHP -> up Na+/H2O retention -> intravascular volume overload -> recurrent flash pulmonary edema (d/t intravascular edema).", Q(59, 60)),
         el(751, 7, "(-) arrow from intravascular volume overload back to renin angiotensin system (-> x).", Q(61)),
         el(751, 8, "Rx -> B/L percutaneous transluminal renal angioplasty with stenting; image 'Bilateral renal artery stenosis'.", Q(62, 63)),
         el(751, 9, "Treatment: in BP -> diuretics (DOC); ACE inhibitors / ARBs: C/I as they down GFR.", Q(64, 65)),
         el(751, 10, "Stop smoking; start statins.", Q(66, 67)),
     ]},
    {"page": 752, "pdfPage": 60,
     "traversal": ("Top images: 'Stents in renal artery bifurcation stenosis'; Pre-op 'Severe stenosis' / Post-op 'Good flow'; Note on pulmonary "
                   "edema; Screening test CDU: look for parvus tardus, RI; RI >= 0.8 parenchymal disease CKD; investigation inconclusive; "
                   "RI < 0.8 PSV > 180 cm/s OR RAR > 3.5 OR delta RI > 0.05 -> CT/MR renal angiography (IOC) -> conventional angiograph (gold "
                   "standard) diagnostic and therapeutic; 'Fibromuscular dysplasia' block; image 'string of beads'."),
     "elements": [
         el(752, 1, "Captions: 'Stents in renal artery bifurcation stenosis'; Pre-op 'Severe stenosis' / Post-op 'Good flow'.", Q(68, 69)),
         el(752, 2, "Note: every pulmonary edema is cardiac unless proven otherwise.", Q(70)),
         el(752, 3, "Screening test: RAS colour doppler ultrasound (CDU); look for parvus tardus pattern; RI (resistivity index).", Q(71)),
         el(752, 4, "RI >= 0.8 -> parenchymal disease: CKD; middle arrow -> investigation inconclusive.", Q(72, 73)),
         el(752, 5, "RI < 0.8: peak systolic velocity > 180 cm/s OR RAR > 3.5 OR delta RI > 0.05.", Q(74, 75, 76)),
         el(752, 6, "-> CT/MR renal angiography (IOC) -> conventional angiograph (gold standard): diagnostic and therapeutic.", Q(77)),
         el(752, 7, "FMD: non atherosclerotic/non inflammatory arteriopathy; incident: m/c in young girls.", Q(78, 79)),
         el(752, 8, "Pathology: middle to distal renal artery, medial fibroplasia in tunica media; 25% B/L renal artery, 25% cerebral vessels.", Q(80, 81)),
         el(752, 9, "Image: 'The string of beads feature in medial fibromuscular dysplasia'.", Q(82)),
         el(752, 10, "Treatment: PTRA (good prognosis).", Q(83)),
     ]},
]

chapter = json.loads((ROOT / "data" / "ch08.json").read_text())
ids = [q["id"] for q in chapter["questions"]]
covered = [i for p in pages for e in p["elements"] for i in e["questionIds"]]
assert covered == ids, "manifest must list every question exactly once in printed order"

manifest = {
    "chapter": 8, "reviewedAt": "2026-09-22", "status": "reviewed-with-source-caveats",
    "pdf": PDF, "pdfSha256": hashlib.sha256((ROOT / PDF).read_bytes()).hexdigest(), "pdfOffset": 692,
    "pageRange": "748-752", "contentSha256": content_digest(chapter),
    "method": ("All five printed pages read from the supplied Part 1 PDF at 2x; flowcharts traversed branch by branch left-to-right, "
               "figures via their printed captions. Every stored answer index checked against the print: all 83 correct. Two "
               "wordings aligned to the print (hydroureteronephrosis; Captopril distractor typo); questions re-sequenced to the traversal."),
    "caveats": [
        "p749: prints 'hydroureteronephrosis' and 'diagonising'; ATN/AIN expanded as 'acute tubular nephrosis' / 'acute interstitial nephrosis' - taught as printed and flagged (MED-C8-028).",
        "p750: prints 'urotension' (urotensin) and 'occulsion'; stems use the standard spelling, explanation quotes the print.",
        "p752: 'Conventional angiograph' printed without -y; the FMD block's 'Incident' means incidence.",
        "Ultrasound/angiogram image content tested only through printed captions and labels.",
    ],
    "pages": pages,
}
out = ROOT / "data" / "source_review" / "ch08.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"wrote {out} ({sum(len(p['elements']) for p in pages)} elements)")
