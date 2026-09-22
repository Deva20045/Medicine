#!/usr/bin/env python3
"""Record the Ch 7 strict source-review manifest (run AFTER author_c7_review.py).

The ordered element->question checklist below was built by reading Part 1 PDF
pp48-55 (Book p740-747) top-to-bottom at 2x whole-page renders plus 6x crops of
every table row, number, flowchart branch and figure caption. This script only
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


def Q(*ns):
    return [f"MED-C7-{n:03d}" for n in ns]


def el(page, index, source, ids):
    return {"element": f"p{page}-e{index:03d}", "page": page, "source": source, "questionIds": ids}


pages = [
    {"page": 740, "pdfPage": 48,
     "traversal": ("Chapter title 'URINE ANALYSIS'; 'Urine Collection' heading; Sample, Analysis, Preservation, Storage lines; "
                   "'Instructions: To Avoid' two bullets; 'Catheterised patients' two bullets; photo caption 'Collection of urine'; "
                   "'Physical Properties' / APPEARANCE table rows 1-7 top-to-bottom; jar caption 'Normal urine colour'; ODOUR table "
                   "rows Pungent, Musty/mousy, Curry/maple syrup, Sweaty feet (two bullets). Timestamps/Active space excluded."),
     "elements": [
         el(740, 1, "Sample: 2nd urine sample of morning -> midstream technique.", Q(1)),
         el(740, 2, "Analysis: within 2-4 hours at room temperature (pH to be checked immediately).", Q(2)),
         el(740, 3, "Preservation: Formaldehyde, Glutaraldehyde.", Q(3)),
         el(740, 4, "Storage: 2-8 C upto 12 hours.", Q(4)),
         el(740, 5, "To avoid: strenuous physical activity 72 hrs prior -> false results due to rhabdomyolysis.", Q(5)),
         el(740, 6, "To avoid: collection during menstruation.", Q(6)),
         el(740, 7, "Catheterised patients: always collect fresh urine; do not collect from urobag.", Q(7)),
         el(740, 8, "Photo caption: Collection of urine.", Q(8)),
         el(740, 9, "APPEARANCE rows 1-2: Light yellow - Normal; Pale/white - up water intake.", Q(9)),
         el(740, 10, "Pink - Desferrioxamine, beetroot.", Q(10)),
         el(740, 11, "Darkening on long standing - Imepenem + cilastatin (printed spelling).", Q(11)),
         el(740, 12, "Green - Triamterene (ENaC blocker).", Q(12)),
         el(740, 13, "Brown - Nitrofurantoin.", Q(13)),
         el(740, 14, "Orange - Rifampicin, Entacapone (COMT inhibitor).", Q(14, 15)),
         el(740, 15, "Appearance table consolidation (match / odd-one-out after all rows).", Q(16, 17)),
         el(740, 16, "Photo caption: Normal urine colour.", Q(18)),
         el(740, 17, "ODOUR: Pungent - infection (unless proven otherwise) d/t ammonia produced by bacteria.", Q(19)),
         el(740, 18, "Musty/mousy - Phenylketonuria; Curry/maple syrup - MSUD; Sweaty feet - isovaleric acidemia, glutaric aciduria type II.", Q(20, 21)),
     ]},
    {"page": 741, "pdfPage": 49,
     "traversal": ("Odour table continued: Cabbage-like / Rancid butter (one condition), Cat urine, Acid smell, Fish urine, Sulfurous, "
                   "Sweet, Swimming pool; OTHER PROPERTIES table rows pH, specific gravity, osmolality (urine then blood cell); "
                   "CLINICAL SIGNIFICANCE / Acidification diagram (alpha-intercalated cell, H+ ATPase, H+/K+ ATPase, NH3->NH4+, "
                   "HPO4->H2PO4-); Concentration three bullets; Abnormal values table rows 1-4."),
     "elements": [
         el(741, 1, "Cabbage-like; Rancid butter - Tyrosinemia type I (single merged condition).", Q(22)),
         el(741, 2, "Cat urine - multiple carboxylase deficiency (MCD).", Q(23)),
         el(741, 3, "Acid smell - methyl malonic acidemia (MMA).", Q(24)),
         el(741, 4, "Fish urine - Trimethylaminuria.", Q(25)),
         el(741, 5, "Sulfurous - Cystinuria; Sweet - Beta ketothiolase deficiency.", Q(26, 27)),
         el(741, 6, "Swimming pool - Hawkinsinuria (table consolidation).", Q(28)),
         el(741, 7, "pH: urine 4-4.5 (acidic); blood 7.35-7.40.", Q(29)),
         el(741, 8, "Specific gravity: urine 1.020-1.040; blood 1.010.", Q(30)),
         el(741, 9, "Osmolality (mOsm/kg): urine 800-900; blood 285-290.", Q(31, 32)),
         el(741, 10, "Acidification: alpha-intercalated cells of cortical collecting duct (CCD); luminal H+ ATPase; H+/K+ ATPase.", Q(33, 34)),
         el(741, 11, "NH3 + H+ -> NH4+: non titratable, major acid.", Q(35)),
         el(741, 12, "HPO4 2- + H+ -> H2PO4-: titratable acid.", Q(36)),
         el(741, 13, "Concentration: ADH from posterior pituitary -> free water reabsorption; medullary interstitium up osmolality d/t urea; vasa recta.", Q(37, 38)),
         el(741, 14, "Urine pH > 5.5 for 3 days + normal RFT - Type-1 RTA.", Q(39)),
         el(741, 15, "Urine specific gravity < 1.005; urine osmolality < 200 mOsm/kg - Diabetes insipidus (up dilute urine).", Q(40, 41)),
         el(741, 16, "Isosthenuria (urinary parameters = blood parameters) - ATN; CTID.", Q(42)),
     ]},
    {"page": 742, "pdfPage": 50,
     "traversal": ("'High Colored Urine' heading; Presentation line; photo 'High coloured urine'; Causes: urological 90% (carcinoma "
                   "bladder), nephrological 9%, hematological 1% (intravascular hemolysis); Approach: 1. Dipstick -> Positive -> Blood in "
                   "urine / Negative -> porphyria, beetroot; 2. Centrifugation 1600 rpm 5 min; Clear supernatant -> RBCs settle -> "
                   "glomerular criteria -> 3. Biopsy -> IgA mechanism; urological -> USG/CT; High coloured supernatant -> 4. undisturbed "
                   "3-6 h -> fades (myoglobin) / persists (hemoglobin)."),
     "elements": [
         el(742, 1, "Presentation: hematuria - red, pink, tea or cola coloured urine.", Q(43, 44)),
         el(742, 2, "Photo caption: High coloured urine.", Q(45)),
         el(742, 3, "Causes: Urological 90% (carcinoma bladder); Nephrological 9%; Hematological 1% (intravascular hemolysis).", Q(46, 47, 48, 49)),
         el(742, 4, "1. Dipstick test -> Positive -> Blood in urine.", Q(50)),
         el(742, 5, "Negative -> Porphyria; up beetroot intake.", Q(51)),
         el(742, 6, "2. Centrifugation: 1600 rpm x 5 min.", Q(52)),
         el(742, 7, "Clear supernatant -> RBCs settle down.", Q(53)),
         el(742, 8, "Glomerular hematuria: >=40% dysmorphic RBCs / >=5% acanthocytes / single RBC cast with proteinuria.", Q(54, 55, 56)),
         el(742, 9, "3. Biopsy -> mesangial disease (IgA nephropathy): mesangial proliferation + matrix expansion -> capillary rupture.", Q(57, 58)),
         el(742, 10, "Urological -> radiological investigation (USG abdomen, CT).", Q(59, 60)),
         el(742, 11, "High coloured supernatant -> 4. sample undisturbed 3-6 h.", Q(61)),
         el(742, 12, "Colour fades -> myoglobin (short half-life); persists -> hemoglobin (long half-life).", Q(62, 63)),
         el(742, 13, "Numbering 1-4 of the approach (page consolidation).", Q(64)),
     ]},
    {"page": 743, "pdfPage": 51,
     "traversal": ("'Types of RBC' figure: Urological A crenated, isomorphic; Nephrological B dysmorphic, C acanthocytes (Mickey mouse "
                   "RBCs); dipstick parameter table rows Leukocytes, Nitrites, Urobilinogen, Protein, pH, Blood, S.G, Ketones, Conj. "
                   "bilirubin, Glucose; 'Factors affecting leucocyte urine dipstick test' seven bullets."),
     "elements": [
         el(743, 1, "Urological: crenated, isomorphic RBCs (A).", Q(65)),
         el(743, 2, "Nephrological: dysmorphic (B); acanthocytes - Mickey mouse RBCs (C).", Q(66, 67, 68)),
         el(743, 3, "Leukocytes / Nitrites - UTI (high specificity, poor sensitivity).", Q(69, 70)),
         el(743, 4, "Urobilinogen - extravascular hemolysis.", Q(71)),
         el(743, 5, "Protein, pH, Blood, S.G, Ketones (SGLT2 inhibitors - euglycemic ketosis), Conj. bilirubin, Glucose (euglycemic glycosuria - proximal RTA).", Q(72, 73, 74, 75)),
         el(743, 6, "Factors affecting leucocyte dipstick: seven bullets (cephalothin, tetracycline, cephalexin, tobramycin, glycosuria, proteinuria, concentrated urine).", Q(76, 77, 78)),
     ]},
    {"page": 744, "pdfPage": 52,
     "traversal": ("'Proteinuria' heading; Urine protein / Uromodulin four bullets; Proteinuria levels table rows <150, 150-500, >500, "
                   ">300 pregnancy; Albumin levels: injury chain; albumin table <30, 30-300, >300; moderately elevated albumin three "
                   "bullets; Tests for proteinuria 1-4 with dipstick sub-bullets."),
     "elements": [
         el(744, 1, "Uromodulin/Tamm Horsfall: 70-80 mg/day; most abundant component of normal urine; forms matrix of casts.", Q(79, 80)),
         el(744, 2, "Produced by thick ascending limb of loop of Henle.", Q(81)),
         el(744, 3, "<150 normal; 150-500 functional proteinuria (stress, anxiety, menses, protein supplements).", Q(82, 83, 84)),
         el(744, 4, ">500 significant proteinuria; >300 significant proteinuria in pregnancy.", Q(85, 86)),
         el(744, 5, "Albumin -> tubular injury -> inflammation -> TGF-beta -> fibrosis.", Q(87, 88)),
         el(744, 6, "Urinary albumin <30 normal; 30-300 microalbuminuria; >300 albuminuria.", Q(89, 90)),
         el(744, 7, "Moderately elevated albumin: marker of vascular integrity; up thrombosis risk (CVA, CAD) d/t endothelial injury; requires further evaluation.", Q(91)),
         el(744, 8, "Tests: 1. 24 hour urine protein; 2. spot PCR; 3. spot ACR.", Q(92, 93)),
         el(744, 9, "4. Urine dipstick: qualitative; positive only ~800 mg; detects only albumin; supplement with PCR/ACR/24 h protein.", Q(94, 95, 96)),
     ]},
    {"page": 745, "pdfPage": 53,
     "traversal": ("'Microscopic Examination'; cell size line; photos: phase contrast monomorphic RBCs with 'Large white cell' arrow, "
                   "tubular epithelial cell with nucleus, oval fat bodies (Maltese cross inset), granular cytoplasm & lobulated nucleus; "
                   "Polarizing microscope list (blood: babesiosis; kidney: Fabry's, ADPKD, acute/chronic interstitial nephritis, prerenal "
                   "azotemia); CASTS IN URINE formation DCT; table hyaline / coarse granular / fine granular."),
     "elements": [
         el(745, 1, "Cell size: RBC < WBC < epithelial cell.", Q(97)),
         el(745, 2, "Photo: 'Large white cell' arrow; caption 'Phase contrast microscopy with monomorphic red cells'.", Q(98, 99, 100)),
         el(745, 3, "Captions: 'Tubular epithelial cell with nucleus'; 'Granular cytoplasm & lobulated nucleus'.", Q(101)),
         el(745, 4, "Oval fat bodies -> Polarizing microscope: maltese cross appearance; in blood: babesiosis.", Q(102, 103)),
         el(745, 5, "In kidney: Fabry's disease, ADPKD, acute/chronic interstitial nephritis, prerenal azotemia.", Q(104, 105, 106)),
         el(745, 6, "CASTS IN URINE - Formation: distal convoluted tubule (DCT).", Q(107)),
         el(745, 7, "Hyaline cast - normal; kidney disease.", Q(108)),
         el(745, 8, "Coarse granular cast (label only); fine granular cast - kidney disease.", Q(109, 110, 111)),
     ]},
    {"page": 746, "pdfPage": 54,
     "traversal": ("Cast table continued row by row: pigment fine granular, RBC, WBC, tubular epithelial (muddy brown), broad/waxy, "
                   "fatty, eosinophil, fractured (on biopsy)."),
     "elements": [
         el(746, 1, "Pigment fine granular cast - pigment nephropathy: hemolysis; rhabdomyolysis.", Q(112, 113)),
         el(746, 2, "RBC cast - glomerular hematuria.", Q(114)),
         el(746, 3, "WBC cast - acute pyelonephritis; post streptococcal GN; ATN/Acute Interstitial Necrosis (AIN) as printed.", Q(115, 116)),
         el(746, 4, "Tubular epithelial cast (muddy brown) - ATN/AIN (most specific).", Q(117, 118, 119, 120)),
         el(746, 5, "Broad cast, waxy cast - chronic kidney disease.", Q(121, 122)),
         el(746, 6, "Fatty cast - lipiduria (nephrotic syndrome); Fabry's.", Q(123, 124)),
         el(746, 7, "Eosinophil cast - ATN/AIN.", Q(125)),
         el(746, 8, "Fractured cast (on biopsy) - myeloma.", Q(126, 127)),
     ]},
    {"page": 747, "pdfPage": 55,
     "traversal": ("'CRYSTALS IN URINE' figure panels A-G with captions: A uric acid rhomboid; B calcium oxalate dihydrate "
                   "bipyramidal/envelope; C calcium oxalate monohydrate dumb bell; D calcium phosphate (alkaline urine) star; E struvite "
                   "(MgNH4PO4) coffin lid; F cholesterol crystal; amoxicillin broom brush; G hexagonal cystine."),
     "elements": [
         el(747, 1, "A: Uric acid crystals - rhomboid.", Q(128, 129)),
         el(747, 2, "B: Calcium oxalate dihydrate - bipyramidal/envelope shaped; C: monohydrate - dumb bell shaped.", Q(130, 131)),
         el(747, 3, "D: Calcium phosphate (in alkaline urine) - star shaped.", Q(132)),
         el(747, 4, "E: Struvite (MgNH4PO4) - coffin lid appearance.", Q(133, 134)),
         el(747, 5, "F: Cholesterol crystal (no shape descriptor).", Q(135, 136)),
         el(747, 6, "Amoxicillin crystal - broom brush appearance.", Q(137)),
         el(747, 7, "G: Hexagonal cystine crystal (page consolidation after it).", Q(138, 139, 140)),
     ]},
]

chapter = json.loads((ROOT / "data" / "ch07.json").read_text())
ids = [q["id"] for q in chapter["questions"]]
covered = [i for p in pages for e in p["elements"] for i in e["questionIds"]]
assert covered == ids, "manifest must list every question exactly once in printed order"

manifest = {
    "chapter": 7,
    "reviewedAt": "2026-09-22",
    "status": "reviewed-with-source-caveats",
    "pdf": PDF,
    "pdfSha256": hashlib.sha256((ROOT / PDF).read_bytes()).hexdigest(),
    "pdfOffset": 692,
    "pageRange": "740-747",
    "contentSha256": content_digest(chapter),
    "method": ("All eight printed pages read from the supplied Part 1 PDF (2x whole-page renders plus 6x crops of table "
               "rows, numbers and captions). Every stored answer index checked against the print: all 135 pre-existing "
               "keys were correct; one printed value was wrong in the bank (DI osmolality) and fixed; questions "
               "re-sequenced to the traversal; five uncovered captions/rows/boxes given items (140 total)."),
    "caveats": [
        "p740: prints 'Imepenem + cilastatin' (standard: imipenem); taught as printed with the standard spelling in the stem.",
        "p741: 'Sweet - Beta ketothiolase deficiency' is printed without the article; the abnormal-values table prints urine osmolality '< 200 mOsm/kg' for diabetes insipidus (the earlier bank said 300 - corrected).",
        "p743: prints 'leucocyte' in the factors heading and 'leukocytes' in the table; both forms accepted in stems.",
        "p746: prints 'Acute Interstitial Necrosis (AIN)' - the usual expansion is nephritis; taught as printed and flagged in MED-C7-116.",
        "p745/p746: photograph content (cast images) is not tested beyond its printed captions.",
    ],
    "pages": pages,
}

out = ROOT / "data" / "source_review" / "ch07.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"wrote {out} ({sum(len(p['elements']) for p in pages)} elements)")
