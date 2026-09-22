#!/usr/bin/env python3
"""Record the Ch 10 strict source-review manifest (run AFTER author_c10_review.py).
Checklist built by reading Part 1 PDF pp64-67 and Part 2 PDF pp1-2 (Book p756-761)
top-to-bottom at 2x. Serialises the recorded review only; never invents coverage."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from check_source_coverage import content_digest

ROOT = Path(__file__).resolve().parent
PDF = "uploads/Medicine_Vol3_Part1_pages_705-759.pdf"
PDF2 = "uploads/Medicine_Vol3_Part2_pages_760-823.pdf"


def Q(*ns):
    return [f"MED-C10-{n:03d}" for n in ns]


def el(page, index, source, ids):
    return {"element": f"p{page}-e{index:03d}", "page": page, "source": source, "questionIds": ids}


pages = [
    {"page": 756, "pdfPage": 64,
     "traversal": ("Title; PRESENTATIONS 1-6; Note (CKD of vascular / glomerular disease); Indication for biopsy flowchart: asymptomatic urine "
                   "abnormalities arm (two routes) and macrohematuria arm (40/5/1 rule) -> Biopsy; NEPHROTIC SYNDROME criteria 1-3 with "
                   "adults/children bracket; Note hyperlipidemia/lipiduria; Nephrotic range proteinuria: total protein adults/children."),
     "elements": [
         el(756, 1, "Presentations 1-6: asymptomatic, macrohematuria, nephrotic syndrome, nephritic syndrome (acute GN), RPGN, CKD (chronic GN).", Q(1, 2)),
         el(756, 2, "Note: CKD of vascular disease ischemic nephropathy; CKD of glomerular disease CKD CGN.", Q(3)),
         el(756, 3, "Asymptomatic urine abnormalities (m/c presentation): proteinuria >500 mg/24 hrs + microhematuria >=3 RBC/HPF; proteinuria alone >1 g/24 hrs.", Q(4, 5, 6)),
         el(756, 4, "Macrohematuria: on urine analysis; 40/5/1 rule (>=40 dysmorphic, >=5 acanthocytes, 1 RBC cast) + significant proteinuria -> biopsy.", Q(7, 8)),
         el(756, 5, "Criteria: 1 nephrotic range proteinuria; 2 hypoalbuminemia <3 g/dl; 3 edema extravascular; adults 1+2+3; children 1+2 or 3.", Q(9, 10, 11, 12)),
         el(756, 6, "Note: hyperlipidemia, lipiduria were previously part of diagnostic criteria.", Q(13, 14)),
         el(756, 7, "Nephrotic range proteinuria - total protein: adults >3500 mg/24 hrs; children >50 mg/kg/day.", Q(15)),
     ]},
    {"page": 757, "pdfPage": 65,
     "traversal": ("PCR adult >=3000 / children >=2000 mg/g; not diagnostic; also seen in (diabetes m/c, 2 degree FSGS, amyloidosis) Rx ACEi/ARB; "
                   "'Childhood Nephrotic Syndrome': proteinuria + hypoalbuminemia + edema -> nephrotic range / extravascular > intravascular; "
                   "HYPOALBUMINEMIA two bullets; Sign: Muehrcke's line photo; EDEMA pathophysiology: underfill > overfill; underfill chain."),
     "elements": [
         el(757, 1, "Urine PCR: adult >=3000 mg/g; children >=2000 mg/g; not diagnostic of nephrotic syndrome.", Q(16, 17, 18)),
         el(757, 2, "Also seen in: diabetes (m/c), 2 degree FSGS, amyloidosis - Rx: ACE inhibitors, ARB.", Q(19, 20, 21)),
         el(757, 3, "Childhood NS: proteinuria + hypoalbuminemia + edema; nephrotic range; extravascular > intravascular.", Q(22)),
         el(757, 4, "HYPOALBUMINEMIA: urinary loss of albumin; down compensation by liver.", Q(23, 24)),
         el(757, 5, "Sign: white transverse line - Muehrcke's line.", Q(25)),
         el(757, 6, "EDEMA pathophysiology: underfill theory > overfill theory.", Q(26)),
         el(757, 7, "Underfill: hypoalbuminemia -> loss of capillary oncotic pressure -> fluid to interstitium -> periorbital puffiness, pedal edema (extravascular) / down effective circulatory volume -> 2 degree RAS -> aldosterone -> Na+, water retention (intravascular).", Q(27, 28, 29, 30, 31)),
     ]},
    {"page": 758, "pdfPage": 66,
     "traversal": ("Overfill theory (nephritic): 1 beta hemolytic streptococci -> plasmin -> ENaC -> 1 degree RAS -> Na+/water retention; 2 ANP "
                   "resistance; management boxes MCD / FSGS / MN, IgA rare; Risk of thrombosis: albumin <2 g/dl, causes, correction of albumin; "
                   "Edema manifestation: ascites / pleural effusion / pericardial effusion."),
     "elements": [
         el(758, 1, "Overfill theory: beta hemolytic streptococci -> releases plasmin -> activates ENaC -> 1 degree RAS activation -> retention of Na+, water (intravascular edema).", Q(32, 33, 34, 35)),
         el(758, 2, "2. ANP resistance.", Q(36)),
         el(758, 3, "Management boxes: MCD 85-90%, steroid responsive (95%), no role of biopsy; FSGS genetic form unresponsive to steroid -> renal transplantation; MN, IgA rare.", Q(37, 38, 39)),
         el(758, 4, "Risk of thrombosis: serum albumin <2 g/dl -> renal vessel thrombosis, CVT, DVT.", Q(40, 41)),
         el(758, 5, "Causes: loss of antithrombin III in urine; loss of protein C, S in urine; up platelet aggregation; up fibrinogen; down plasminogen.", Q(42, 43)),
         el(758, 6, "Correction of albumin (to >2 g/dL): 20% albumin 20 g/100 ml; dose 0.5 g/kg; FFP, egg white can also be used.", Q(44, 45)),
         el(758, 7, "Edema manifestation: ascites (moderate to severe) Rx tapping, m/c death pneumococcal peritonitis; pleural effusion (mild); pericardial effusion (rare) disproportional dyspnoea Ix echo.", Q(46, 47, 48)),
     ]},
    {"page": 759, "pdfPage": 67,
     "traversal": ("Treatment for edema four bullets; Daily monitoring three bullets; Note: features against MCD; Steroid regimen -> taper -> stop -> "
                   "remission 90-95% (two bullets) / SRNS 5-10%; Hyperlipidemia three bullets; pathogenesis four bullets; associated features; xanthelasma photo."),
     "elements": [
         el(759, 1, "Treatment for edema: salt <2 g/day; protein 1 g/kg/day; albumin, FFP; diuretics avoided - only if IVC non-collapsible; precipitates pre-renal AKI.", Q(49, 50)),
         el(759, 2, "Daily monitoring: weight; urine routine examination; urine PCR.", Q(51)),
         el(759, 3, "Note - features against MCD: RBC casts in urine; hypertension; renal failure.", Q(52)),
         el(759, 4, "Steroid: oral prednisolone 2 mg/kg/day (or) 60 mg/m2/day x 6 wks; max 80 mg/day; taper x 6 weeks; stop.", Q(53)),
         el(759, 5, "Remission 90-95%: urine albumin nil/trace x 3 consecutive days; urine PCR <200 mg/g; SRNS 5-10%.", Q(54, 55)),
         el(759, 6, "Hyperlipidemia: resolves with steroid therapy; no risk of atherosclerosis; no role for statin.", Q(56)),
         el(759, 7, "Pathogenesis: loss of HDL in urine; up lipoprotein lipase up TG; down LCAT down HDL; up VLDL, LDL synthesis by liver.", Q(57, 58)),
         el(759, 8, "Associated features: xanthoma, xanthelasma (photo).", Q(59)),
     ]},
    {"page": 760, "pdfPage": 1, "pdf": PDF2, "pdfSha256": hashlib.sha256((ROOT / PDF2).read_bytes()).hexdigest(),
     "traversal": ("SRNS: proteinuria despite full dose steroid 4 wk -> biopsy (1st indication in child) -> genetic FSGS (podocin) Rx transplant / "
                   "MCD treatment CNI (DOC) duration, max; tacrolimus dose and S/E; cyclosporine S/E; Relapse flowchart 25/25/50; steroid sparing "
                   "drugs; relapse after intermission; SDNS definition; treatment MMF, rituximab."),
     "elements": [
         el(760, 1, "SRNS: proteinuria despite full dose of steroid for 4 wk -> biopsy (1st indication in child).", Q(60)),
         el(760, 2, "Genetic form of FSGS (podocin mutation) -> Rx renal transplantation.", Q(61)),
         el(760, 3, "MCD treatment: calcineurin inhibitors (DOC) duration 6 months, max 2 yrs; tacrolimus 0.1 mg/kg/day S/E neuropathy, DM, alopecia; cyclosporine S/E hirsutism, gingival hyperplasia.", Q(62, 63)),
         el(760, 4, "Relapse: proteinuria after 1 month of steroid; 25% no further relapse (very quick remission); 25% infrequent relapse; 50% FRNS.", Q(64, 65, 66)),
         el(760, 5, "Infrequent relapse -> steroid -> taper over 4 wks during remission.", Q(67)),
         el(760, 6, "FRNS: >=2 relapse within 6 months; >=4 relapse within 1 year; steroid sparing drug: oral cyclophosphamide 2 mg/kg/day x 12 wks + steroid x 2 wks; oral levamisole.", Q(68, 69)),
         el(760, 7, "Relapse: proteinuria reappears after 1 month of intermission.", Q(70)),
         el(760, 8, "SDNS: >=2 consecutive relapses during tapering (or) within 14 days after stopping steroid; treatment MMF 1200 mg/m2/day; rituximab 375 mg/m2/day x 4 doses.", Q(71, 72)),
     ]},
    {"page": 761, "pdfPage": 2, "pdf": PDF2, "pdfSha256": hashlib.sha256((ROOT / PDF2).read_bytes()).hexdigest(),
     "traversal": ("'Adult Nephrotic Syndrome' three bullets; CAUSES list with Rare bracket; MANAGEMENT 1-2; Treatment chain steroid -> no response -> "
                   "SRNS (m/c FSGS); Note figures: maltese crosses in polarized light; oval fat bodies; seen in Fabry's disease."),
     "elements": [
         el(761, 1, "Proteinuria: urine PCR >=3000 mg/d; edema; hypoalbuminemia.", Q(73)),
         el(761, 2, "Causes: membranous nephropathy (m/c); FSGS; MCD (15%); IgA; MPGN, 2 degree amyloidosis - rare.", Q(74, 75, 76)),
         el(761, 3, "Management: 1 biopsy; 2 rule out 2 degree causes (eg paraneoplastic syndrome).", Q(77)),
         el(761, 4, "Treatment: steroid 1 mg/kg/d x 4 months -> no response -> SRNS (m/c FSGS).", Q(78, 79)),
         el(761, 5, "Note: maltese crosses in polarized light; oval fat bodies -> seen in Fabry's disease.", Q(80)),
     ]},
]

chapter = json.loads((ROOT / "data" / "ch10.json").read_text())
ids = [q["id"] for q in chapter["questions"]]
assert [i for p in pages for e in p["elements"] for i in e["questionIds"]] == ids

manifest = {
    "chapter": 10, "reviewedAt": "2026-09-22", "status": "reviewed-with-source-caveats",
    "pdf": PDF, "pdfSha256": hashlib.sha256((ROOT / PDF).read_bytes()).hexdigest(), "pdfOffset": 692,
    "secondaryPdf": PDF2, "secondaryPdfSha256": hashlib.sha256((ROOT / PDF2).read_bytes()).hexdigest(), "secondaryPdfOffset": 759,
    "pageRange": "756-761", "contentSha256": content_digest(chapter),
    "method": ("Six printed pages read at 2x (p756-759 from Part 1 PDF pp64-67; p760-761 from Part 2 PDF pp1-2), top-to-bottom, flowcharts "
               "branch by branch. Every stored answer index checked against the print: all 78 correct. Two uncovered printed notes given "
               "items (80 total); questions re-sequenced to the traversal."),
    "caveats": [
        "p757: caption printed 'muehrcke's line' (lower case); p761: 'Paraneoplastic snydrome' misprint - taught with standard spelling.",
        "p758: management boxes are read left-to-right (MCD, FSGS, MN/IgA); the p758 header page number is cropped in the scan but the running head and content confirm p758.",
        "p759: the SRNS 5-10% arm and 'Features against MCD' note are printed to the right; traversal takes the note after Daily monitoring and before Steroid.",
        "Photographs (Muehrcke's line, xanthelasma, Maltese crosses, oval fat bodies) tested only through printed captions.",
    ],
    "pages": pages,
}
out = ROOT / "data" / "source_review" / "ch10.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"wrote {out} ({sum(len(p['elements']) for p in pages)} elements)")
