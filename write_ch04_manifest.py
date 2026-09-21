#!/usr/bin/env python3
"""Record the Ch 4 strict source-review manifest (run AFTER the bank rebuild).

The ordered element->question checklist below was built by reading Part 1
PDF pp34-37 (Book p726-729) top-to-bottom. This script only serialises the
recorded review with fresh PDF/content hashes; it never invents coverage.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from check_source_coverage import content_digest

ROOT = Path(__file__).resolve().parent
PDF = "uploads/Medicine_Vol3_Part1_pages_705-759.pdf"

Q = [f"MED-C4-{i:03d}" for i in range(1, 56)]


def el(page, index, source, ids):
    return {"element": f"p{page}-e{index:03d}", "page": page,
            "source": source, "questionIds": ids}


pages = [
    {"page": 726, "pdfPage": 34,
     "traversal": ("Read top-to-bottom: chapter title; Components list (3 bullets); "
                   "'Macula Densa & JG cells' section; MACULA DENSA text (Composition, Site, Function); "
                   "JG-apparatus figure labels top-to-bottom with caption; 'Applied aspect of TG feedback' header; "
                   "phases/MOA table row by row, left cell then right cell (row-2 right cell continues onto p727). "
                   "Lecture timestamp, 'Active space' and footer excluded."),
     "elements": [
         el(726, 1, "Components list: Juxtaglomerular (JG) cells; macula densa; mesangial/lacis/supporting cells/Polkissen cells.", [Q[0]]),
         el(726, 2, "Macula densa composition: modified tall columnar cells.", [Q[1]]),
         el(726, 3, "Macula densa site: cortical portion of thick ascending limb of loop of Henle (TAL)/distal straight tubule.", [Q[2]]),
         el(726, 4, "Macula densa function: tubulo-glomerular (TG) feedback mediated by adenosine.", [Q[3]]),
         el(726, 5, "Composition/site/function of macula densa consolidated as a match, positioned after the three lines.", [Q[4]]),
         el(726, 6, "Macula densa site reconfirmed (true/false), positioned after the figure-independent text.", [Q[5]]),
         el(726, 7, "JG-apparatus figure: efferent arteriole leaving the glomerulus with its smooth muscle layer.", [Q[6]]),
         el(726, 8, "JG-apparatus figure labels: internal elastic lamina (top arteriole wall), glomerular epithelium (tuft covering), basement membrane (tubule wall).", [Q[7]]),
         el(726, 9, "JG-apparatus figure labels: distal tubule (straight) in cross-section, macula densa plaque, JG cells; caption 'JG apparatus'.", [Q[8]]),
         el(726, 10, "Table row 1: phase of tubular injury; duration < 24 hrs.", [Q[9]]),
         el(726, 11, "Row-1 MOA: renal tubular injury from tubulotoxic drugs (eg. gentamicin) leading to PCT injury.", [Q[10]]),
         el(726, 12, "Row-1 MOA: PCT injury lowers reabsorption of solute + H2O, raising their loss in urine.", [Q[11]]),
         el(726, 13, "Row-2 Findings cell as a set: decreased GFR; raised S.creatinine; raised K+ with cardiac arrhythmias (print 'arrythmias'); raised H+ with metabolic acidosis.", [Q[12]]),
         el(726, 14, "Row-2 finding line tested directly: raised H+ leads to metabolic acidosis.", [Q[13]]),
         el(726, 15, "Row-2 MOA: impaired reabsorption of solute + H2O; macula densa senses Cl- > K+ > Na+ load delivered to TAL.", [Q[14]]),
         el(726, 16, "Row-2 MOA: release of adenosine, which constricts the afferent arteriole (print 'afferent'; arrow continues onto p727).", [Q[15]]),
     ]},
    {"page": 727, "pdfPage": 35,
     "traversal": ("Table continued: row-2 left cell (Mx) then right cell (MOA chain with its two end branches); "
                   "row 3 (Recovery phase with dash); B. Dehydration flowchart top-to-bottom including the '+' "
                   "proximal-absorption input; AKI-causes note (Outside branch complete, then Inside branch); "
                   "JG Cells (Composition, Site, Function). Header/footer excluded."),
     "elements": [
         el(727, 1, "Row-2 Mx: supportive care; monitor fluid intake because of the raised chance of edema due to renal failure.", [Q[16]]),
         el(727, 2, "Row-2 MOA: afferent constriction lowers GFR (glomerular filtration rate), raising S.creatinine and preventing further salt + H2O loss due to impaired reabsorption.", [Q[17]]),
         el(727, 3, "Row 3: recovery phase with only a dash in the MOA column.", [Q[18]]),
         el(727, 4, "B. Dehydration example (increased vomiting leading to pre-renal failure); first event is loss of intravascular volume.", [Q[19]]),
         el(727, 5, "Dehydration chain: loss of volume lowers glomerular hydrostatic pressure and therefore GFR.", [Q[20]]),
         el(727, 6, "Dehydration chain: increased proximal tubular absorption (+) feeds the macula densa sensing of a decreased Na+/Cl-/K+ load.", [Q[21]]),
         el(727, 7, "Dehydration chain: dilatation of the afferent arteriole, mediated by prostaglandins.", [Q[22]]),
         el(727, 8, "Dehydration chain outcome: GFR rises.", [Q[23]]),
         el(727, 9, "AKI-causes note as a set: outside kidney (pre-renal, post-renal) versus inside kidney (ATI/ATN, acute interstitial nephritis).", [Q[24]]),
         el(727, 10, "AKI cause groups re-tested as a match, positioned after the note.", [Q[25]]),
         el(727, 11, "JG cells composition: granular cells.", [Q[26]]),
         el(727, 12, "JG cells site: tunica media of afferent arteriole more than efferent arteriole (print 'afferent').", [Q[27]]),
         el(727, 13, "JG cells function: produce renin.", [Q[28]]),
     ]},
    {"page": 728, "pdfPage": 36,
     "traversal": ("Renin-stimulator diagram (three stimuli left-to-right with (+) arrows into JG cells, then Renin); "
                   "'Vascular Anatomy of Kidney' section; renal-circulation chain in forward arrow order; "
                   "cortex-vs-medulla table (Cortex column top-to-bottom, then Medulla column); "
                   "vascularity-of-nephron figure (left labels top-to-bottom, right 'sandwiched' annotation, bottom urine caption). "
                   "Timestamp/footer excluded."),
     "elements": [
         el(728, 1, "Renin stimuli: decreased renal perfusion pressure, prostaglandins and beta-1 receptors all act positively (+) on JG cells, which release renin.", [Q[29]]),
         el(728, 2, "Beta-1 receptor positive drive on JG cells releasing renin.", [Q[30]]),
         el(728, 3, "Beta-1 drive re-tested through a beta-blocker scenario, positioned with the diagram.", [Q[31]]),
         el(728, 4, "Renal circulation starts at the renal artery, labelled an end artery.", [Q[32]]),
         el(728, 5, "Renal artery gives 5 segmental arteries (4 anterior + 1 posterior).", [Q[33]]),
         el(728, 6, "Chain continues: interlobar artery, arcuate artery, interlobular/cortical radial artery.", [Q[34]]),
         el(728, 7, "Afferent arteriole supplies the glomerular capillary plexus in the cortex.", [Q[35]]),
         el(728, 8, "Blood leaves via the efferent arteriole into the peritubular capillary plexus.", [Q[36]]),
         el(728, 9, "Medullary blood supply is mediated by the vasa recta.", [Q[37]]),
         el(728, 10, "Venous return: descending limb to ascending limb of vasa recta, renal vein, IVC (inferior vena cava).", [Q[38]]),
         el(728, 11, "Forward circulation order consolidated (odd-one-out), positioned after the full chain.", [Q[39]]),
         el(728, 12, "Cortex-vs-medulla table: cortex supplied by the renal artery with good supply; medulla supplied by vasa recta with poor supply.", [Q[40]]),
         el(728, 13, "Medulla: pars recta/proximal straight tubule is m/c vulnerable to hypoxia.", [Q[41]]),
         el(728, 14, "Zone-perfusion contrast reconfirmed (true/false), positioned before the figure questions.", [Q[42]]),
         el(728, 15, "Vascularity-figure upper labels: afferent arteriole entering the tuft, proximal convoluted tubule beside the glomerulus, glomerular capsule cupping the tuft.", [Q[43]]),
         el(728, 16, "Vascularity-figure vessel labels: interlobular artery (red) with interlobular vein and its venule (blue).", [Q[44]]),
         el(728, 17, "Vascularity-figure labels as a set: glomerular capsule, peritubular capillary network, loop of the nephron (no macula densa).", [Q[45]]),
         el(728, 18, "Right annotation: efferent arteriole sandwiched between glomerular and peritubular capillary plexuses.", [Q[46]]),
         el(728, 19, "Bottom annotation: urine flows into the renal papilla; caption 'Vascularity of nephron'.", [Q[47]]),
     ]},
    {"page": 729, "pdfPage": 37,
     "traversal": ("Note read as a tree: root 'Renal diseases', left branch completed first (85% arm: AKI with the ATN/AIN pair, "
                   "then CKD with RTA type 4), then right branch (5% arm: large-vessel disease to RAS, small-vessel disease to TMA "
                   "with hypertensive crisis progressing to CKD). Header/footer excluded."),
     "elements": [
         el(729, 1, "Tree root and left arm: tubules & interstitium form 85% of the kidney.", [Q[48]]),
         el(729, 2, "Left arm 1. AKI (hours to days): ATN due to ischemia (m/c); AIN due to drug hypersensitivity (m/c).", [Q[49]]),
         el(729, 3, "Left arm 2. CKD: chronic tubulointerstitial fibrosis/disease leading to RTA type 4.", [Q[50]]),
         el(729, 4, "Right arm: vascular disease forms 5% of the kidney; large vessel disorders lead to RAS (renal artery stenosis); small vessel disorders lead to TMA (thrombotic microangiopathy).", [Q[51]]),
         el(729, 5, "Small-vessel chain: TMA to hypertensive crisis, progressing to CKD (ischemic nephropathy).", [Q[52]]),
         el(729, 6, "Vascular arm consolidated (true/false), positioned after both branches.", [Q[53]]),
         el(729, 7, "Vascular arm consolidated (odd-one-out), positioned after both branches.", [Q[54]]),
     ]},
]

chapter = json.loads((ROOT / "data" / "ch04.json").read_text())
manifest = {
    "chapter": 4,
    "reviewedAt": "2026-09-21",
    "status": "reviewed-with-source-caveats",
    "pdf": PDF,
    "pdfSha256": hashlib.sha256((ROOT / PDF).read_bytes()).hexdigest(),
    "pdfOffset": 692,
    "pageRange": "726-729",
    "contentSha256": content_digest(chapter),
    "method": ("All four printed pages read from the supplied Part 1 PDF at 2x-5x zoom, with explicit local traversals "
               "recorded per page. Ordered source blocks include every instructional bullet, table row/cell, flowchart step, "
               "diagram label, arrow annotation and caption. Contiguous labels share an item; consolidation items sit after the "
               "lines they test and never pull later material forward. Headers, timestamps, footers and blank Active space excluded."),
    "caveats": [
        "p726: the scan prints 'Cardiac arrythmias' and 'afferent arteriole'; questions use standard 'arrhythmias'/'afferent'. 'Tubulo glomerular' is printed as two words; the bank uses TG feedback.",
        "p727: the dehydration chain is taught as printed — increased proximal tubular absorption (+) feeds a macula densa signal of decreased Na+/Cl-/K+ load (higher proximal reabsorption lowers distal delivery). The 'ATI/ATN' slash and the edema rationale for fluid monitoring are source wordings.",
        "p727: JG-cell site 'afferent arteriole > efferent arteriole' is taught as the printed predominance, not an exclusive site.",
        "p728: 'renal artery (end artery)' and '5 segmental arteries (4 anterior + 1 posterior)' are source simplifications taught as printed. The efferent-arteriole 'sandwiched' note is schematic (a vessel between two capillary beds).",
        "p728: 'Urine flows into renal papilla' is taught as printed; standard drainage continues via the minor calyx, which the figure does not label.",
        "p729: the tree arms sum to 90% (85% tubulointerstitial + 5% vascular); glomeruli (10% per the p717 compartment tree) have no arm here. Taught as printed, not completed. The '1. AKI'/'2. CKD' numbering, the m/c cause claims and RTA type 4 as the CKD tubulointerstitial endpoint are source-specific.",
    ],
    "pages": pages,
}

out = ROOT / "data" / "source_review" / "ch04.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"wrote {out} ({sum(len(p['elements']) for p in pages)} elements)")
