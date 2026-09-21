#!/usr/bin/env python3
"""Record the Ch 5 strict source-review manifest (run AFTER the bank rebuild).

The ordered element->question checklist below was built by reading Part 1
PDF pp38-41 (Book p730-733) top-to-bottom at 2x-16x zoom (whole-page renders
plus glyph-level checks of every printed number and ambiguous token). This
script only serialises the recorded review with fresh PDF/content hashes; it
never invents coverage.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from check_source_coverage import content_digest

ROOT = Path(__file__).resolve().parent
PDF = "uploads/Medicine_Vol3_Part1_pages_705-759.pdf"

Q = [f"MED-C5-{i:03d}" for i in range(1, 89)]


def el(page, index, source, ids):
    return {"element": f"p{page}-e{index:03d}", "page": page,
            "source": source, "questionIds": ids}


pages = [
    {"page": 730, "pdfPage": 38,
     "traversal": ("Read top-to-bottom: page header and chapter title; 'Parts of Filtration Barrier' "
                   "section; CAPILLARY ENDOTHELIUM WITH FENESTRATIONS / 'Fenestration Slits' bullets 1-3; "
                   "'Disease of capillary endothelium' line with its PSGN parenthesis, then its four "
                   "sub-bullets; 'Pathophysiology of CKD' chain top-to-bottom (pore-diameter step included), "
                   "finishing the left terminal branch (tubulotoxicity) before the right branch "
                   "(interstitial inflammation to TGF-beta to tubulo interstitial fibrosis); "
                   "'Factors determining passage through filtration barrier' tree (Size branch complete, "
                   "then Charge branch complete); then the right-panel glomerular-capillary figure labels "
                   "top-to-bottom (glomerular basement membrane, podocyte, foot processes, capillary, "
                   "capillary endothelium, mesangial angle, microfilaments, mesangium, mesangial matrix) "
                   "with its caption. Timestamp, 'Active space' and footer excluded."),
     "elements": [
         el(730, 1, "Fenestration slits: 50-100nm diameter.", [Q[0]]),
         el(730, 2, "Fenestration slits coated with podocalyxin giving -ve charge that repels negatively charged proteins (the word 'repels' sits above the arrow).", [Q[1]]),
         el(730, 3, "Function: prevent proteinuria (albuminuria) -> prevent nephrotoxicity.", [Q[2]]),
         el(730, 4, "Disease of capillary endothelium line with the parenthesis 'PSGN : Post Streptococcal Glomerulo Nephritis'.", [Q[3]]),
         el(730, 5, "PSGN findings sub-bullets as a set: microhematuria; minimal proteinuria; exudative neutrophilic infiltration of lumen.", [Q[4]]),
         el(730, 6, "PSGN sub-bullet: 'No risk for CKD.'", [Q[5]]),
         el(730, 7, "CKD chain steps 1-6 in printed order: down functional nephrons, hyperfiltration by remaining nephrons, intraglomerular hypertension (HTN), stretching of capillaries, raised capillary pore diameter, proteinuria (albuminuria).", [Q[6]]),
         el(730, 8, "Chain pair re-tested: stretching of capillaries raises capillary pore diameter.", [Q[7]]),
         el(730, 9, "Proteinuria branches: tubulotoxicity and interstitial inflammation, the latter leading to TGF-beta formation.", [Q[8]]),
         el(730, 10, "Terminal step after TGF-beta formation: tubulo interstitial fibrosis.", [Q[9]]),
         el(730, 11, "Factors tree head and Size branch line 1: effective diameter < 4 mm passes through (printed unit 'mm').", [Q[10]]),
         el(730, 12, "Size branch line 2: effective diameter > 8-10mm does not pass (printed unit 'mm').", [Q[11]]),
         el(730, 13, "Charge branch line 1: effective diameter 4-8 mm is repelled if -ve charge (printed unit 'mm'; 'repelled' above the arrow).", [Q[12]]),
         el(730, 14, "Charge branch example: albumin 7.6 mm, -vely charged (printed unit 'mm').", [Q[13]]),
         el(730, 15, "Figure labels top-right cluster: glomerular basement membrane; podocyte (printed 'Podocyte 7' with a stray glyph); foot processes.", [Q[14]]),
         el(730, 16, "Figure labels mid cluster: capillary (lumen in cross-section); capillary endothelium; mesangial angle.", [Q[15]]),
         el(730, 17, "Figure labels lower cluster: microfilaments; mesangium; mesangial matrix.", [Q[16]]),
         el(730, 18, "Figure caption: 'Glomerular capillary'.", [Q[17]]),
         el(730, 19, "Figure-label consolidation (odd one out), positioned after every figure label.", [Q[18]]),
     ]},
    {"page": 731, "pdfPage": 39,
     "traversal": ("Read top-to-bottom: 'GLOMERULAR BASEMENT MEMBRANE (GBM)' heading; Constituent bullet; "
                   "'Type 4 collagen configuration' table (header row left-to-right, then the data row "
                   "left-to-right); the right column in the same vertical band: 'Type 4 collagen defect' "
                   "note with its Alport line, then the Alport inheritance table (header row left-to-right, "
                   "85% row left-to-right, then 10-15% row left-to-right); Negative charge bullet; "
                   "'Visualisation of GBM' tree (left branch '1.' complete, then right branch 'a.' with its "
                   "stain ranking); 'Thickness' tree (Normal first, then Thin GBM disease); 'Note' mesangial "
                   "block (supporting-cells line, constituent sub-bullet, violent-contraction branches left "
                   "then right, mesangial proliferative definition line, IgA prototype line); bottom figures "
                   "left-to-right: 'Light microscope image' legend then labels top-to-bottom with caption, "
                   "then 'Juxtaglomerular apparatus' labels top-to-bottom (PCT, GC circles, AA, parietal "
                   "layer, DCT, visceral layer, EA, macula densa, bracket labels) with caption. Header, "
                   "'Active space' and footer excluded."),
     "elements": [
         el(731, 1, "GBM constituent: type 4 collagen (majorly).", [Q[19]]),
         el(731, 2, "Type 4 collagen configuration table: alpha1alpha1alpha2 (at birth), alpha3alpha4alpha5 (GBM, cochlear Bm, ocular Bm), alpha5alpha5alpha6 (epidermal Bm).", [Q[20]]),
         el(731, 3, "Type 4 collagen defect: Alport syndrome.", [Q[21]]),
         el(731, 4, "Alport table rows as printed: 85% X-linked alpha5 with absent skin/epidermal immunoflorescence stain; 10-15% AD/AR with the 'alpha3+/ alpha4' defect cell and normal stain.", [Q[22]]),
         el(731, 5, "Negative charge: heparin sulfate proteoglycans (eg: perlecan, agrin) - 'Heparin sulfate' as printed.", [Q[23]]),
         el(731, 6, "Visualisation branch '1.': electron m/s (microscope); the mixed '1.'/'a.' numbering is recorded as a print oddity.", [Q[24]]),
         el(731, 7, "Visualisation branch 'a.': stains under light m/s - Gomori methenamine Silver Stain > masson's Trichrome.", [Q[25]]),
         el(731, 8, "Thickness branch 1: normal 350-400nm.", [Q[26]]),
         el(731, 9, "Thickness branch 2: thin GBM disease < 200nm.", [Q[27]]),
         el(731, 10, "GBM consolidation (odd one out: podocalyxin versus heparin sulfate), positioned after the GBM lines.", [Q[28]]),
         el(731, 11, "Note: supporting cells of the filtration barrier = mesangial cells.", [Q[29]]),
         el(731, 12, "Mesangial cells constituent: microfilaments.", [Q[30]]),
         el(731, 13, "Violent contraction branch 1: rupture of capillary -> macrohematuria.", [Q[31]]),
         el(731, 14, "Violent contraction branch 2: down surface area -> down GFR.", [Q[32]]),
         el(731, 15, "Mesangial proliferative definition line: >3 mesangial cells in a space (with mesangial cell / matrix expansion glosses).", [Q[33]]),
         el(731, 16, "Prototype disease line: IgA nephropathy (m/c) prototype of mesangial cell/matrix expansion.", [Q[34]]),
         el(731, 17, "Light-microscope image legend: PT = proximal tubule; CL = capillary lumen.", [Q[35]]),
         el(731, 18, "Light-microscope image labels: mesangial cells (arrows); Bowman's space; PT (in-photo).", [Q[36]]),
         el(731, 19, "Light-microscope image labels: open capillary loops (arrows); the four CL labels.", [Q[37]]),
         el(731, 20, "Light-microscope image label consolidation (odd one out: macula densa belongs to the JGA figure).", [Q[38]]),
         el(731, 21, "Light-microscope image caption: 'Light microscope image'.", [Q[39]]),
         el(731, 22, "JGA figure labels: PCT; GC (four capillary circles); AA.", [Q[40]]),
         el(731, 23, "JGA figure labels: parietal layer; DCT; visceral layer.", [Q[41]]),
         el(731, 24, "JGA figure labels: EA; macula densa.", [Q[42]]),
         el(731, 25, "JGA figure bracket labels: JG cells (granular cells); lacis cells (extraglomerular mesangial cells).", [Q[43]]),
         el(731, 26, "JGA figure caption: 'Juxtaglomerular apparatus'.", [Q[44]]),
     ]},
    {"page": 732, "pdfPage": 40,
     "traversal": ("Read top-to-bottom: 'SLIT DIAPHRAGM / FILTRATION SLITS' heading and its definition "
                   "line ('Space btw 2 podocytes'); 'Podocytes' bullets in order (terminally differentiated; "
                   "anchored to GBM by foot processes; Proteins tree - Inside branch then Surface branch "
                   "with Podocin then TRPC6; Diameter; Function); 'Nephrins' sub-bullets; then the right-panel "
                   "figure: panel (a) labels top-to-bottom (macula densa, distal convoluted tubule, afferent "
                   "arteriole, efferent arteriole, Bowman's capsule, mesangium, podocyte, capillary, "
                   "fenestrated endothelium, glomerular basement membrane, proximal tubule x2), panel (b) "
                   "labels top-to-bottom (F-actin, slit diaphragm, podocyte foot process x2, beta/alpha "
                   "dystro-glycan pair, Laminin-11, alpha3beta1 integrin pair, glomerular basement membrane, "
                   "Agrin/Argin pair, GEC x3), then the protein legend column by column (column 1, column 2, "
                   "column 3) and the shared caption; then back to the left column for the angiotensin chain "
                   "step-by-step to CKD and the closing ARBs/ACEI line. Header and footer excluded."),
     "elements": [
         el(732, 1, "Slit diaphragm / filtration slits definition: space btw 2 podocytes.", [Q[45]]),
         el(732, 2, "Podocytes: terminally differentiated cells (cannot be regenerated).", [Q[46]]),
         el(732, 3, "Podocytes: anchored to GBM by foot processes - no filtration.", [Q[47]]),
         el(732, 4, "Podocyte proteins tree: inside 'alpha actin 4' (as printed); surface podocin and TRPC6.", [Q[48]]),
         el(732, 5, "Filtration-slit diameter: 30-50nm, coated with podocalyxin.", [Q[49]]),
         el(732, 6, "Filtration-slit function: filtration.", [Q[50]]),
         el(732, 7, "Nephrins sub-bullets as a set: proteins contained in the slit diaphragm; prevents protein leak; maintains podocyte integrity.", [Q[51]]),
         el(732, 8, "Figure (a) labels: macula densa; distal convoluted tubule; afferent arteriole.", [Q[52]]),
         el(732, 9, "Figure (a) labels: efferent arteriole; Bowman's capsule; mesangium.", [Q[53]]),
         el(732, 10, "Figure (a) labels: podocyte; capillary; fenestrated endothelium.", [Q[54]]),
         el(732, 11, "Figure (a) labels: glomerular basement membrane; proximal tubule (labelled twice).", [Q[55]]),
         el(732, 12, "Figure (b) labels: F-actin; slit diaphragm; podocyte foot process (both sides).", [Q[56]]),
         el(732, 13, "Figure (b) label: beta/alpha dystro-glycan (both sides).", [Q[57]]),
         el(732, 14, "Figure (b) labels: Laminin-11; alpha3beta1 integrin (both sides).", [Q[58]]),
         el(732, 15, "Figure (b) labels: glomerular basement membrane; agrin pair (left 'Agrin', right 'Argin'); GEC x3.", [Q[59]]),
         el(732, 16, "Figure (b) protein legend, column by column: nephrin/NEPH1/CD2AP/ZO-1/podocin; Fat-1/NCK/ACTN4/ILK; CD151/TRPC6/podocalyxin/synaptopodin.", [Q[60]]),
         el(732, 17, "Legend consolidation (odd one out: Laminin-11 is a diagram label, not a legend entry).", [Q[61]]),
         el(732, 18, "Shared caption: 'Slit diaphragm podocytes'.", [Q[62]]),
         el(732, 19, "Angiotensin chain steps 1-2: angiotensin binds the podocyte angiotensin II binding receptor -> downregulation of nephrin.", [Q[63]]),
         el(732, 20, "Chain step 3: loss of podocyte integrity (podocytopathies).", [Q[64]]),
         el(732, 21, "Chain steps 4-6: podocyte detached -> podocyturia -> podocytopenia (clinical scenario positioned at these steps).", [Q[65]]),
         el(732, 22, "Chain steps 7-8: GBM attaches to parietal epithelial cells -> synechiae formation.", [Q[66]]),
         el(732, 23, "Chain steps 9-10: glomerulosclerosis -> CKD.", [Q[67]]),
         el(732, 24, "Whole-chain consolidation, positioned after every chain step.", [Q[68]]),
         el(732, 25, "Rx line: 'ARBs /ACEI(-)'s used in Rx of diabetic nephropathy to block Angiotensin II Receptor.'", [Q[69]]),
     ]},
    {"page": 733, "pdfPage": 41,
     "traversal": ("Read top-to-bottom: 'Congenital Nephrotic Syndrome :' heading and the DMS line; "
                   "congenital-NS table row by row, left cell then right cell (header row, Finnish-type row "
                   "complete, podocin-type row complete, autosomal dominant-type row complete), then the two "
                   "cross-row consolidations; the premature-babies line; 'Note' with the Denys Drash line; "
                   "site-disease table (header row left-to-right then disease row left-to-right), then the "
                   "pairing consolidations. Header, 'Active space' and footer excluded."),
     "elements": [
         el(733, 1, "Congenital nephrotic syndrome heading and 'DMS : Diffuse mesangial Sclerosis'.", [Q[70]]),
         el(733, 2, "Table row 1 (Finnish Type Nephrotic Syndrome) cells 2-4: inheritance AR; defect nephrin : NPHS1; age birth.", [Q[71]]),
         el(733, 3, "Table row 1 outcome: 100% mortality.", [Q[72]]),
         el(733, 4, "Table row 1 histology and management cells: histology equivalent to DMS; management a bare dash.", [Q[73]]),
         el(733, 5, "Table row 2 (Podocin type) cells 2-4: inheritance AR; defect podocin; age 3-5 years.", [Q[74]]),
         el(733, 6, "Table row 2 outcome: 100% steroid resistance -> CKD.", [Q[75]]),
         el(733, 7, "Table row 2 histology and management cells: equivalent to FSGS; renal transplant (presented as a steroid-resistant child scenario).", [Q[76]]),
         el(733, 8, "Table row 3 (Autosomal Dominant Type) cells 2-4: inheritance AD; defect alpha actinin 4/TRPC6; age adolescence.", [Q[77]]),
         el(733, 9, "Table row 3 outcome/histology/management cells: identical to row 2 (100% steroid resistance -> CKD, equivalent to FSGS, renal transplant).", [Q[78]]),
         el(733, 10, "Cross-row consolidation: the three types matched with defect and age, positioned after every row.", [Q[79]]),
         el(733, 11, "Cross-row consolidation: table-statements true/false, positioned after every row.", [Q[80]]),
         el(733, 12, "Line under the table: Finnish type nephrotic syndrome m/c seen in premature babies with large placenta.", [Q[81]]),
         el(733, 13, "Note line: DMS also seen in Denys Drash Syndrome.", [Q[82]]),
         el(733, 14, "Site-disease table columns 2-4: endothelium -> PSGN; GBM -> Alport; mesangium -> IgA nephropathy.", [Q[83]]),
         el(733, 15, "Site-disease column 'Podocyte with podocytopenia': diabetes; FSGS; membranous.", [Q[84]]),
         el(733, 16, "Site-disease column 'without podocytopenia': mCD.", [Q[85]]),
         el(733, 17, "Site-disease pairings consolidation (true/false), positioned after the columns.", [Q[86]]),
         el(733, 18, "Endothelium->PSGN consolidation, positioned after the table.", [Q[87]]),
     ]},
]

chapter = json.loads((ROOT / "data" / "ch05.json").read_text())
manifest = {
    "chapter": 5,
    "reviewedAt": "2026-09-21",
    "status": "reviewed-with-source-caveats",
    "pdf": PDF,
    "pdfSha256": hashlib.sha256((ROOT / PDF).read_bytes()).hexdigest(),
    "pdfOffset": 692,
    "pageRange": "730-733",
    "contentSha256": content_digest(chapter),
    "method": ("All four printed pages read from the supplied Part 1 PDF at 2x-16x zoom (whole-page "
               "renders plus glyph-level checks of every number and ambiguous token), with explicit local "
               "traversals recorded per page. Ordered source blocks include every instructional bullet, "
               "table row/cell, flowchart step, diagram label, arrow annotation, legend entry and caption. "
               "Contiguous labels share an item; consolidation items sit after the lines they test and never "
               "pull later material forward. Headers, timestamps, footers and blank Active space excluded."),
    "caveats": [
        "p730: the size and charge rules print 'mm' for all four values ('< 4 mm', '> 8-10mm', '4-8 mm', '7.6 mm') where nanometres are meant (the fenestration sizes on the same page correctly print 'nm'). Values are taught as printed and the unit error is flagged in every affected explanation.",
        "p730: the figure label prints 'Podocyte 7' - a stray '7' glyph sits just before the leader line and is unexplained; taught as 'Podocyte' with the glyph flagged. 'Post Streptococcal Glomerulo Nephritis' prints as three words and 'No risk for CKD.' is an absolute source claim taught as printed.",
        "p731: the Alport table header prints 'Immunoflorescence' (one u) and the 10-15% defect cell prints 'alpha3+/ alpha4', a nonstandard notation taught as printed. 'Heparin sulfate proteoglycans' is the print (standard: heparan sulfate). The visualisation tree mixes numbering ('1.' then 'a.') and 'masson's Trichrome' prints lowercase.",
        "p732: 'Space btw 2 podocytes' uses a script '2' (background OCR read 'a'; confirmed as 2 at 16x zoom). The podocyte protein tree prints 'Inside : alpha actin 4' (standard: alpha-actinin-4) - taught as printed. Figure (b) prints 'Laminin-11' (nonstandard laminin nomenclature) and misspells agrin as 'Argin' on the right label while the left reads 'Agrin'. Legend names print 'NEPH1' and 'Fat-1'. The Rx line prints 'ARBs /ACEI(-)'s ... to block Angiotensin II Receptor', compressing both drug classes into receptor blockade (ACE inhibitors reduce angiotensin II formation) - taught as printed with the flag.",
        "p733: histology cells print the equivalence sign ('equiv DMS'/'equiv FSGS'), NPHS1 carries a subscript 1 and TRPC6 a subscript 6. The site-disease table prints 'mCD' with a lowercase m and lists 'membranous' as a bare adjective. 'Denys Drash Syndrome' prints without a hyphen. The Finnish-type management cell is a bare dash.",
    ],
    "pages": pages,
}

out = ROOT / "data" / "source_review" / "ch05.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"wrote {out} ({sum(len(p['elements']) for p in pages)} elements)")
