#!/usr/bin/env python3
"""Second-pass re-audit fixes for Ch 13-18 (September 2026).

Every source page p775-p804 was re-read against the bank. Content was found
faithful; the defect was structural - 50 items used shallow "Both A / Both B"
option sets or 2-row matches whose distractors gave the answer away. This script
replaces those items with 3-row matches (four real permutation keys) or with
scenario / recall / fill-up items carrying four substantive medical options, and
deletes one item (MED-C17-043) whose content is folded into MED-C17-042.

Run:  python fix_audit2.py       (patches data/parts/c13..c18 in place)
      python author.py 13 ... 18 (rebuild data/chNN.json)
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / "data" / "parts"

# id -> (fmt, q, opts, ans, exp)
FIX: dict[str, tuple] = {
    # ---------------- Ch 13 (Book p775-777) ----------------
    "MED-C13-005": ("match",
        "Match each PSGN table entry with its meaning — 1) Strains 1, 3, 4, 12  2) Strains 47, 49, 55, 57  3) Anti-DNAase B … "
        "A) Skin infection  B) Sore throat  C) Antibody that appears after a preceding skin infection",
        ["1-B, 2-A, 3-C", "1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"], 0,
        "The TYPES table splits nephritogenic GABHS strains by the infection they follow: strains 1, 3, 4 and 12 cause sore throat, "
        "strains 47, 49, 55 and 57 cause skin infection, and anti-DNAase B is the antibody highlighted after a preceding skin infection. (Book p775)"),
    "MED-C13-013": ("match",
        "Match each row of the TYPES table with its entry — 1) PSGN prognosis  2) PIGN/IRGN prognosis  3) C3 in PIGN/IRGN … "
        "A) Good, with no risk of CKD  B) Poor  C) Raised in 60% (as printed in this table)",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-A, 3-B"], 0,
        "The p775 TYPES table gives PSGN a good prognosis with no risk of CKD, PIGN/IRGN a poor prognosis, and prints '↑C3 in 60%' for "
        "PIGN/IRGN. Note that the text on p777 instead states serum C3 is low in 60% of PIGN/IRGN patients — the two pages disagree, so quote "
        "the page you are asked about. (Book p775)"),
    "MED-C13-055": ("scenario",
        "A 6-year-old treated for PSGN is reviewed at 8 weeks: haematuria persists but serum C3 has normalised. The correct interpretation is:",
        ["Persistent microhaematuria after PSGN has no significance, whereas a C3 still low beyond 8 weeks would suggest C3 GN and warrant biopsy",
         "Both findings indicate a recurrence of PSGN, which requires a second course of penicillin",
         "The persistent haematuria indicates progression to CKD, and C3 must be rechecked monthly for one year",
         "A normal C3 at 8 weeks excludes PSGN, so the original diagnosis must be revised"], 0,
        "Recovery point: 99% recover in 3-5 days with prompt treatment, and microhaematuria may persist after treatment with no significance; "
        "follow-up is by serum C3, normally normal by 8 weeks, and persistence beyond that points to C3 GN and biopsy. PSGN also does not recur. (Book p777)"),
    "MED-C13-059": ("scenario",
        "A 5-year-old with post-streptococcal GN has C3 measured at presentation, and his cousin with MRSA-related infection-associated GN is "
        "also tested. The expected results are:",
        ["↓C3 in 90% of PSGN versus ↓C3 in 60% of PIGN/IRGN (the p775 table printing ↑C3 in 60% for PIGN)",
         "↓C3 in 60% of PSGN versus ↓C3 in 90% of PIGN/IRGN",
         "Normal C3 in both conditions, since C3 falls only in RPGN",
         "↑C3 in 90% of PSGN versus ↓C3 in 60% of PIGN/IRGN"], 0,
        "PSGN shows a low C3 in 90% of patients; for PIGN/IRGN the text states a low C3 in 60% of patients, while the p775 table prints "
        "'↑C3 (in 60%)' — learn both printings and note the discrepancy. (Book p777)"),
    "MED-C13-065": ("match",
        "Match the onset and oedema of the nephrotic versus nephritic table — 1) Nephrotic onset  2) Nephritic onset  3) Nephrotic oedema "
        "compartment … A) Abrupt  B) Insidious  C) Extravascular (+++)",
        ["1-B, 2-A, 3-C", "1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"], 0,
        "Table rows: onset is insidious in nephrotic and abrupt in nephritic syndrome; nephrotic oedema is extravascular (+++) whereas "
        "nephritic oedema is intravascular (++). (Book p777)"),
    "MED-C13-066": ("match",
        "Match the BP and JVP entries of the nephrotic versus nephritic table — 1) Nephrotic BP  2) Nephritic BP  3) Nephritic JVP … "
        "A) Normal  B) High  C) Raised",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "In the table, nephrotic syndrome has a normal BP and normal JVP, while nephritic syndrome has a high BP with a raised JVP "
        "(intravascular volume expansion). (Book p777)"),
    "MED-C13-067": ("recall",
        "Regarding proteinuria, haematuria and casts in the nephrotic versus nephritic table, which statement is correct?",
        ["Proteinuria is greater and haematuria less in nephrotic syndrome, with RBC casts absent",
         "Proteinuria and haematuria are both greater in nephrotic syndrome, with RBC casts present",
         "Proteinuria is less in nephrotic syndrome, but RBC casts are still present",
         "Haematuria is greater in nephrotic syndrome while RBC casts are absent"], 0,
        "Table: proteinuria more, haematuria less and RBC casts absent in nephrotic syndrome; proteinuria less, haematuria more and RBC casts "
        "present in nephritic syndrome. (Book p777)"),

    # ---------------- Ch 14 (Book p778-782) ----------------
    "MED-C14-003": ("match",
        "Match each condition with its place in the renal-failure flowchart — 1) Acute tubular necrosis  2) Rapidly progressive GN  "
        "3) Hemolytic uremic syndrome  4) Atheroembolic renal disease … A) AKI (hours-days)  B) RPRF due to glomerular pathology  "
        "C) RPRF  D) RPRF in some cases",
        ["1-A, 2-B, 3-C, 4-D", "1-B, 2-A, 3-C, 4-D", "1-A, 2-B, 3-D, 4-C", "1-A, 2-C, 3-B, 4-D"], 0,
        "The flowchart puts acute tubular necrosis on the AKI (hours-days) limb, then lists for RPRF: rapidly progressive glomerulonephritis "
        "(due to glomerular pathology), hemolytic uremic syndrome, severe acute interstitial nephritis and atheroembolic renal disease "
        "(some cases). (Book p778)"),
    "MED-C14-019": ("match",
        "Match each immunofluorescence finding with its important association as listed beside the biopsy panels — 1) Linear IF  "
        "2) Granular IF  3) Negative IF … A) Goodpasture disease  B) Diabetes mellitus and light chain disease  C) No immune deposits (pauci-immune)",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "The page lists Goodpasture disease (linear), diabetes mellitus and light chain disease (granular); panel A of the figure is a negative "
        "IF, which corresponds to pauci-immune type III RPGN. (Book p779)"),
    "MED-C14-030": ("fillup",
        "Fill up: In the RPGN treatment algorithm, volume status is assessed by the ______ diameter on ultrasound and treated with diuretics.",
        ["inferior vena cava", "abdominal aorta", "portal vein", "main renal artery"], 0,
        "Volume status: check the inferior vena cava diameter on USG, the treatment being diuretics (with calcium gluconate for ECG signs of "
        "hyperkalaemia and NaHCO3 or dialysis for metabolic acidosis). (Book p780)"),
    "MED-C14-034": ("match",
        "Match the dialysis indications in RPGN with their category — 1) Absolute indication  2) Relative indication  3) Qualifier for the "
        "relative group … A) Uremic encephalopathy, halitosis, pruritis, pericarditis, bleeding, gastritis  B) Volume overload, hyperkalemia, "
        "metabolic acidosis  C) Resistant to treatment",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-A, 3-B"], 0,
        "Absolute (uremic) indications: encephalopathy, halitosis, pruritis, pericarditis, bleeding and gastritis. Relative indications: volume "
        "overload, hyperkalemia and metabolic acidosis, all qualified as resistant to treatment. (Book p780)"),
    "MED-C14-039": ("match",
        "Match each RPGN type with its label in the immunofluorescence flowchart — 1) Type II  2) Type III  3) Type II age note … "
        "A) Immune complex deposition  B) Pauci-immune, the commonest type  C) Commonest below 20 years",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Type II = immune complex deposition (commonest in those below 20 years); type III = pauci-immune, marked m/c i.e. the commonest type "
        "overall. (Book p780)"),
    "MED-C14-044": ("match",
        "Match each type II (immune-complex) RPGN example with the note printed beside it — 1) Systemic lupus erythematosus  "
        "2) Henoch-Schönlein purpura and IPGN  3) Membranoproliferative GN … A) Most important cause  B) Adult variety  C) 10%",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "In the type II list SLE carries '(most important cause)', HSP with IPGN is bracketed as the adult variety, and MPGN is annotated 10%. (Book p780)"),
    "MED-C14-047": ("match",
        "Match the serology with its type in the double-positive versus double-negative table — 1) Anti-GBM + and ANCA +  2) Anti-GBM - and "
        "ANCA -  3) Prognosis of the double-positive type … A) Type IV  B) Type V  C) Good",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-A, 3-B"], 0,
        "Type IV is double positive (anti-GBM +, ANCA +) with a good prognosis; type V is double negative (anti-GBM -, ANCA -) with a poor "
        "prognosis. (Book p780)"),
    "MED-C14-055": ("fillup",
        "Fill up: Besides smoking, hydrocarbon exposure and lung infection, the fourth 2nd/trigger factor listed for Goodpasture disease is ______.",
        ["fluid overload", "streptococcal pharyngitis", "hypercalcemia", "contrast exposure"], 0,
        "2nd/trigger factors for Goodpasture disease: smoking, hydrocarbon exposure, fluid overload and lung infection. (Book p781)"),
    "MED-C14-057": ("recall",
        "Which HLA pair carries the highest risk in Goodpasture disease?",
        ["DR2/15 and DR4", "DR1 and DR7", "DR3 and DR2", "DR10 and DR11"], 0,
        "HLA association in Goodpasture disease: high risk DR2/15 and DR4; low risk DR1 and DR7. (Book p781)"),

    # ---------------- Ch 15 (Book p783-785) ----------------
    "MED-C15-011": ("match",
        "Match each Alport inheritance pattern with its features — 1) X-linked (80%)  2) Autosomal recessive (15%)  3) Autosomal dominant "
        "(5%) … A) ESRD by 30 years in males; females are carriers  B) ESRD by 40 years in females and males  C) Mild disease in females and males",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Inheritance table: X-linked (80%, α5) gives ESRD by 30 years in males with females as carriers; AR (15%, α3/α4) gives ESRD by 40 years "
        "in both sexes; AD (5%, α3/α4) is mild in both sexes. (Book p783)"),
    "MED-C15-024": ("match",
        "Match each Alport syndrome finding with the investigation that shows it — 1) Splitting and lamellation of the lamina densa  "
        "2) No immune deposits  3) Normal glomerular architecture on routine staining … A) Electron microscopy  B) Immunofluorescence  C) Light microscopy",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-A, 3-B"], 0,
        "In Alport syndrome light microscopy and immunofluorescence are normal, the diagnosis resting on electron microscopy, which shows "
        "splitting and lamellation of the lamina densa with alternating thick and thin foci and a basket-weave appearance. (Book p784)"),
    "MED-C15-042": ("match",
        "Match each Fabry disease finding with its investigation — 1) Maltese cross deposits  2) Vacuolation of podocytes  3) Angiokeratoma "
        "in the 2nd decade … A) Urine under polarised light  B) Renal biopsy  C) Skin examination",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Fabry investigations: maltese cross lipid deposits in urine under polarised light and vacuolation of podocytes on renal biopsy; "
        "angiokeratoma appears in the 2nd decade. (Book p784)"),

    # ---------------- Ch 16 (Book p786-792) ----------------
    "MED-C16-011": ("match",
        "Match each ADPKD gene with its chromosome and product — 1) PKD1  2) PKD2  3) PKD3 … A) Chr16p - polycystin 1, 85% of cases  "
        "B) Chr4q - polycystin 2, milder disease  C) Printed as GANA B",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Gene defect: PKD1 on chr16p (85%) gives polycystin 1; PKD2 on chr4q (15%) gives polycystin 2 with milder disease; PKD3 is printed as "
        "GANA B. (Book p786)"),
    "MED-C16-028": ("match",
        "Match each ADPKD feature with its explanation — 1) Nocturia and polyuria  2) Less anaemia than other CKD causes  3) Biventricular "
        "diastolic dysfunction … A) Tubular involvement with impaired concentrating capacity  B) Preserved EPO production  C) Systemic hypertension",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Nocturia and polyuria come from tubular involvement with impaired concentrating capacity; anaemia is less common because EPO production "
        "is preserved (ADPKD has the least anaemia of the CKD causes); biventricular diastolic dysfunction is due to hypertension. (Book p787)"),
    "MED-C16-033": ("scenario",
        "A 27-year-old black man with ADPKD has haematuria at presentation and a BP of 150/95 mmHg. Which statement best reflects the book's "
        "list of prognostic indicators?",
        ["Four listed indicators of early ESRD are present — black race, diagnosis before 30 years, haematuria at presentation and hypertension below 35 years",
         "Only the haematuria matters; the other features do not affect renal prognosis once the creatinine is normal",
         "None of these features affects prognosis, because only the MRI kidney and cyst volume predicts renal decline",
         "These features indicate a PKD2 mutation, which is expected to give a milder course"], 0,
        "Indicators of bad prognosis/early ESRD: black males, diagnosis before 30 years, haematuria at presentation, HTN below 35 years and a "
        "PKD1 truncating mutation; kidney and cyst volume on MRI is the strongest predictor of renal function decline. (Book p787)"),
    "MED-C16-041": ("recall",
        "Which group of ADPKD complications is bracketed in the book as presenting with abdominal pain?",
        ["Cyst haemorrhage, cyst infection, renal stones and cyst rupture",
         "Cyst haemorrhage, biventricular diastolic dysfunction, renal stones and hepatic cysts",
         "Cyst infection, hepatic cysts, colonic diverticula and renal stones",
         "Renal stones, cyst rupture, aortic root dilatation and mitral valve prolapse"], 0,
        "The bracket 'presents with abdominal pain' covers cyst haemorrhage (can cause haematuria), cyst infection (m/c E. coli), renal stones "
        "(uric acid > calcium oxalate) and cyst rupture (rare, after blunt trauma). (Book p787)"),
    "MED-C16-053": ("match",
        "Match each ADPKD therapy with its role — 1) Tolvaptan  2) Everolimus and somatostatin analogues  3) ACE inhibitor or ARB … "
        "A) Oral V2 antagonist, 15 mg at night with LFT monitoring  B) Novel therapies  C) Tight BP control",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Treatment: tolvaptan (oral V2 antagonist, 15 mg at night, monitor LFT) is the DOC for cyst growth; somatostatin analogues and "
        "everolimus are novel therapies; tight BP control (SBP 95-110/DBP 60-75 mmHg) uses an ACE inhibitor or ARB. (Book p788)"),
    "MED-C16-072": ("match",
        "Complete the ARPKD flowchart — 1) Collecting duct  2) Biliary duct  3) Gene on chromosome 6 … A) Medullary cyst  B) Congenital "
        "hepatic fibrosis/Caroli's syndrome/biliary ectasia  C) PKHD1 leading to the fibrocystin-polyductin complex",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "ARPKD flowchart: PKHD1 on chromosome 6 forms the fibrocystin-polyductin complex; a defect affecting the cilia/centrosome complex "
        "produces medullary cysts in the collecting duct and congenital hepatic fibrosis/Caroli's syndrome/biliary ectasia in the biliary duct. (Book p789)"),
    "MED-C16-078": ("match",
        "Match each ARPKD ultrasound sign with its description — 1) Medulla  2) Corticomedullary differentiation  3) Kidney size … "
        "A) Hyperechoic  B) Lost  C) Bilaterally enlarged with small medullary cysts",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "ARPKD ultrasound: hyperechoic medulla and loss of corticomedullary differentiation in bilaterally enlarged kidneys with small "
        "medullary cysts, often with oligohydramnios. (Book p789)"),
    "MED-C16-083": ("match",
        "Match each disease with its inheritance and gene — 1) Juvenile nephronophthisis  2) MCDK1  3) MCDK2 … A) AR - NPHP1 on chromosome 2, "
        "nephrocystin  B) AD - chromosome 1  C) AD - chromosome 16, uromodulin",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "JN is autosomal recessive with NPHP1 on chromosome 2 producing nephrocystin; MCDK (ADTKD) is autosomal dominant — MCDK1 on chromosome 1 "
        "and MCDK2 on chromosome 16 producing uromodulin. (Book p790)"),
    "MED-C16-084": ("match",
        "Match each disease with its age group and ESRD timing — 1) Juvenile nephronophthisis  2) MCDK (ADTKD)  3) CTID abbreviation … "
        "A) Children - onset by 5-7 years, ESRD by 13 years  B) Adults - onset by 20-25 years, ESRD by 40-50 years  C) Chronic tubulointerstitial disease",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "JN affects children, starting by 5-7 years with ESRD by 13 years; MCDK affects adults, starting by 20-25 years with ESRD by 40-50 years. "
        "The page also expands CTID as chronic tubulointerstitial disease and ADTKD as autosomal dominant tubular kidney disease. (Book p790)"),
    "MED-C16-094": ("match",
        "Match the juvenile nephronophthisis / MCDK clinical-feature rows with their entries — 1) JN salt handling  2) JN growth  3) MCDK growth … "
        "A) Salt wasting  B) Failure to thrive  C) Growth complete, so failure to thrive is absent",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Clinical features of JN: salt wasting, polyuria and failure to thrive; MCDK is similar except for failure to thrive, because growth is "
        "complete in adults. (Book p790)"),
    "MED-C16-100": ("match",
        "Match each MCDK extrarenal association with its note — 1) Hyperuricemia and gout  2) Insulin resistance  3) Rickets-like changes in "
        "MCDK … A) Seen in the MCDK2 defect  B) Also listed for MCDK  C) Absent, because growth is complete",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "MCDK extrarenal associations: hyperuricemia and gout (in the MCDK2 defect) and insulin resistance; rickets-like changes are present in "
        "JN but absent in MCDK because growth is complete. (Book p790)"),
    "MED-C16-119": ("match",
        "Complete the sequence in medullary sponge kidney — 1) Primary event  2) Collecting-duct change  3) Cyst number … A) Malformation of the "
        "terminal collecting duct  B) Dilated spongy medullary and papillary collecting ducts  C) Few cysts in the medulla",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Pathogenesis of medullary sponge kidney: malformation of the terminal collecting duct leads to dilated spongy medullary and papillary "
        "collecting ducts with a few cysts in the medulla. (Book p791)"),
    "MED-C16-126": ("recall",
        "Which option correctly pairs the associations of medullary sponge kidney listed in the book?",
        ["Incomplete distal RTA in 50% (giving a Ca3(PO4)2 stone), Marfan's syndrome and Beckwith-Wiedemann syndrome",
         "Complete distal RTA in 50% (giving a calcium oxalate stone), Marfan's syndrome and Alport syndrome",
         "Incomplete proximal RTA in 5% (giving a uric acid stone), Beckwith-Wiedemann syndrome and Alport syndrome",
         "Distal RTA in 50% (giving a uric acid stone), Marfan's syndrome and nail-patella syndrome"], 0,
        "Associations of medullary sponge kidney: incomplete distal renal tubular acidosis in 50% (producing a Ca3(PO4)2 stone), Marfan's "
        "syndrome and Beckwith-Wiedemann syndrome. (Book p792)"),
    "MED-C16-129": ("match",
        "Match each medullary sponge kidney investigation with its finding — 1) RFT  2) NCCT  3) Excretory urography … A) Normal  "
        "B) Medullary nephrocalcinosis  C) Rounded densities in the medulla giving a paintbrush/bouquet of flower appearance",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "MSK investigations: RFT is normal, NCCT shows medullary nephrocalcinosis, and excretory urography shows rounded densities in the medulla "
        "described as a paintbrush or bouquet of flower appearance. (Book p792)"),
    "MED-C16-133": ("match",
        "Match each medullary sponge kidney treatment with the abnormality it corrects — 1) Potassium citrate  2) Increased fluid intake  "
        "3) The aim of both measures … A) Hypocitraturia  B) Hypercalciuria  C) Prevention of recurrent stones",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Treatment of MSK: potassium citrate for hypocitraturia and increased fluid intake for hypercalciuria, together preventing recurrent "
        "stone formation. (Book p792)"),
    "MED-C16-135": ("match",
        "Match each type of nephrocalcinosis with its causes — 1) Medullary  2) Cortical  3) Both medullary and cortical … A) Distal RTA, Bartter "
        "syndrome, sarcoid, MSK and conditions with hypercalciuria  B) Tuberculosis and chronic graft rejection  C) Oxalosis",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Medullary nephrocalcinosis: distal RTA, Bartter syndrome, sarcoid, MSK and hypercalciuric conditions. Cortical nephrocalcinosis: TB and "
        "chronic graft rejection. Oxalosis causes both. (Book p792)"),

    # ---------------- Ch 17 (Book p793-795) ----------------
    "MED-C17-015": ("match",
        "Match each toxin with its CTID picture — 1) Lead  2) Cadmium  3) Lithium … A) Saturnine gout with hyperuricemia  B) Ouch ouch "
        "nephropathy  C) Microcystic changes in distal tubules without interstitial inflammation",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Toxins in CTID: lead gives saturnine gout with hyperuricemia, cadmium the ouch ouch nephropathy, and lithium microcystic changes in "
        "distal tubules without interstitial inflammation. (Book p793)"),
    "MED-C17-018": ("match",
        "Match each CTID cause with its mechanism — 1) Hyperuricemia  2) Hypokalemia  3) Ciliopathies … A) Urate nephropathy  B) Vacuolization "
        "of PCT more than DCT  C) Hereditary cystic disorders (the first-listed etiology)",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Metabolic causes of CTID include hyperuricemia (urate nephropathy), hypercalcemia, hyperoxaluria and hypokalemia (vacuolization of PCT "
        "more than DCT); ciliopathies head the etiology list. (Book p793)"),
    "MED-C17-020": ("recall",
        "The histology panels for urate nephropathy and IgG4 disease in this section are both marked by an arrow labelled 'fibrosis'. Which "
        "statement about the two entities is correct?",
        ["Both cause chronic tubulointerstitial disease with interstitial fibrosis, but only urate nephropathy belongs to the metabolic group of the etiology list",
         "Both are glomerular diseases in which the fibrosis is confined to the mesangium",
         "IgG4 disease is a metabolic cause and urate nephropathy an autoimmune cause of CTID",
         "The fibrosis in urate nephropathy actually indicates acute tubular necrosis rather than CTID"], 0,
        "Both figures show interstitial fibrosis, the histological hallmark of chronic tubulointerstitial disease; urate nephropathy sits in the "
        "metabolic group of the etiology list while IgG4 disease is one of the autoimmune causes (sarcoidosis, Sjögren's, IgG4 disease). (Book p793)"),
    "MED-C17-022": ("fillup",
        "Fill up: The three autoimmune causes of chronic tubulointerstitial disease listed are sarcoidosis, Sjögren's syndrome and ______ disease.",
        ["IgG4", "anti-GBM", "Goodpasture", "lupus"], 0,
        "Etiology item 7 (autoimmune): sarcoidosis, Sjögren's and IgG4 disease, followed by item 8, CKD of unknown etiology (CKDu). (Book p794)"),
    "MED-C17-031": ("match",
        "Match each CKD condition with its anaemia severity in the book's note — 1) CTID  2) ADPKD  3) Reason ADPKD has the least anaemia … "
        "A) Maximum anaemia  B) Minimum anaemia  C) EPO production is preserved",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Note on anaemia in CKD: maximum in CTID and minimum in ADPKD, because EPO production is preserved in ADPKD. (Book p794)"),
    "MED-C17-042": ("recall",
        "In the CKDu theories flowchart, which set of factors is shown converging on 'CKDu interstitial fibrosis and tubular atrophy'?",
        ["Heat stress, agrochemicals, fluoride in ground water, heavy metals such as cadmium, and communicable disease",
         "Diabetes, hypertension, obesity, smoking and dyslipidaemia",
         "Heat stress, NSAIDs, lithium, contrast and aminoglycosides",
         "Agrochemicals, fluoride, uric acid, lead and multiple myeloma"], 0,
        "The flowchart places heat stress above, agrochemicals and fluoride in ground water on the left, and heavy metals (e.g. cadmium) and "
        "communicable disease on the right, all converging on CKDu interstitial fibrosis and tubular atrophy with ESRD as the outcome. (Book p795)"),

    # ---------------- Ch 18 (Book p796-804) ----------------
    "MED-C18-015": ("fillup",
        "Fill up: In the pre-renal causes list, burns, rhabdomyolysis and acute pancreatitis are grouped under ______ sequestration.",
        ["third-space", "intravascular", "intracellular", "effective intravascular"], 0,
        "Reduced effective intravascular volume from third-space sequestration is bracketed to list burns, rhabdomyolysis and acute pancreatitis. (Book p796)"),
    "MED-C18-021": ("recall",
        "The three conditions bracketed together as 'pre-renal >> ATN' in insult/drug-induced AKI are:",
        ["NSAIDs, rhabdomyolysis and polyuria (contrast-induced AKI)",
         "NSAIDs, aminoglycosides and contrast",
         "Sepsis, cirrhosis and cardiorenal syndrome",
         "Vancomycin, cisplatin and ethylene glycol"], 0,
        "The bracket 'pre-renal >> ATN' covers NSAIDs, rhabdomyolysis and polyuria (contrast-induced AKI) — in these the pre-renal component "
        "predominates over tubular necrosis. (Book p797)"),
    "MED-C18-024": ("match",
        "Complete the flowchart of long-standing profound pre-renal failure — 1) Tubular lesion  2) Feedback mediator  3) Result … "
        "A) Ischemic ATN  B) Tubuloglomerular feedback by the macula densa  C) Fall in GFR with decreased urine output",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Flowchart: long-standing profound pre-renal failure produces ischemic ATN; tubuloglomerular feedback by the macula densa then lowers "
        "GFR and urine output. (Book p797)"),
    "MED-C18-032": ("match",
        "Match each AIN cause with its AIN subgroup — 1) Leptospirosis and scrub typhus  2) Lymphoma and sarcoidosis  3) Beta-lactams and PPIs … "
        "A) Infections  B) Infiltration  C) Drugs",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "AIN is a hypersensitivity reaction to drugs, to infections (leptospirosis, scrub typhus) or to infiltration (lymphoma, sarcoidosis). (Book p797)"),
    "MED-C18-040": ("recall",
        "Which set lists the drugs appearing in the AIN column of the drug-induced AKI chart?",
        ["PPIs, beta-lactams, rifampicin, allopurinol/anticonvulsants, NSAIDs, diuretics",
         "Vancomycin, aminoglycosides, adefovir, amphotericin B, cisplatin, salicylates",
         "Methotrexate, indinavir, triamterene, acyclovir, sulfonamides",
         "NSAIDs, drugs causing raised calcium, ACE inhibitors/ARBs, calcineurin inhibitors"], 0,
        "The AIN column mnemonic is P-B-R-A-N-D: PPIs, beta-lactams, rifampicin, allopurinol with anticonvulsants, NSAIDs and diuretics. The other "
        "options are the ATN, intratubular-obstruction and pre-renal columns respectively. (Book p798)"),
    "MED-C18-056": ("recall",
        "In which conditions can ATN show a FeNa below 1% because a pre-renal component predominates?",
        ["NSAIDs, rhabdomyolysis and contrast-induced AKI",
         "Aminoglycosides, cisplatin and vancomycin",
         "Ethylene glycol, salicylates and acyclovir",
         "Sepsis, urinary obstruction and acute interstitial nephritis"], 0,
        "ATN with FeNa <1: NSAIDs, rhabdomyolysis and contrast AKI, grouped because the pre-renal component is predominant. (Book p798)"),
    "MED-C18-097": ("match",
        "Match each sepsis-AKI parameter with its interpretation — 1) S. lactate >1 mmol/L  2) S. lactate >4 mmol/L  3) IVC diameter "
        "2-2.5 cm … A) Organ hypoperfusion  B) Severe sepsis  C) Normal value, determining the amount of fluid required",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Investigations in sepsis-AKI: an IVC diameter of 2-2.5 cm is normal and determines the fluid requirement; lactate >1 mmol/L indicates "
        "organ hypoperfusion and >4 mmol/L severe sepsis. (Book p800)"),
    "MED-C18-120": ("fillup",
        "Fill up: In uric acid nephropathy the serum potassium, phosphate and magnesium are ______, while the serum calcium is ______.",
        ["all raised; low", "all low; raised", "raised only for potassium; normal", "normal; low"], 0,
        "Features of uric acid nephropathy (tumour lysis syndrome): oliguric AKI, markedly raised serum uric acid, raised S.K+/S.PO4(3-)/S.mg2+ "
        "and a low serum calcium. (Book p801)"),
    "MED-C18-122": ("match",
        "Match each aspect of uric acid nephropathy management — 1) Drug treatment  2) Renal replacement  3) Prevention … A) IV rasburicase  "
        "B) Dialysis  C) Hydration with 5-6 L/day, alkalinisation and allopurinol",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Treatment of uric acid nephropathy: IV rasburicase and dialysis. Prevention before chemotherapy: adequate hydration (5-6 L/day), "
        "adequate alkalinisation and allopurinol. (Book p802)"),    "MED-C18-136": ("match",
        "Match the urine findings in rhabdomyolysis — 1) Benzidine test  2) Urine microscopy  3) FeNa … A) Positive (3+) for blood  B) Pigmented granular brown casts and renal tubular epithelial cell casts, with no RBCs  C) Less than 1",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "In rhabdomyolysis the benzidine (dipstick) test is 3+ positive for blood while urine microscopy shows no RBCs but pigmented granular brown casts and renal tubular epithelial cell casts; FeNa is <1. (Book p802)"),
    "MED-C18-143": ("match",
        "Complete the aetiology of contrast-induced AKI — 1) Primary mechanism  2) Secondary mechanism  3) Histology … A) Medullary hypoxia  B) Tubular injury beside the medullary hypoxia  C) Vacuolar degeneration",
        ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"], 0,
        "Contrast-induced AKI: medullary hypoxia is written as the primary mechanism (>>>) with tubular injury beside it, and the histology figure shows vacuolar degeneration. (Book p803)"),    "MED-C18-125": ("scenario",
        "A patient with Burkitt lymphoma is due to start chemotherapy. Which preventive plan matches the book?",
        ["Hydration with 5-6 L/day, adequate alkalinisation and allopurinol",
         "IV rasburicase, dialysis and fluid restriction",
         "Hydration with 1-2 L/day and acidification of the urine",
         "Allopurinol plus rasburicase only, with free oral fluids"], 0,
        "Prevention of uric acid nephropathy before chemotherapy: adequate hydration (5-6 L/day), adequate alkalinisation and allopurinol; "
        "rasburicase and dialysis belong to treatment. (Book p802)"),
    "MED-C18-128": ("fillup",
        "Fill up: Besides electric shock, seizures, alcohol/cocaine/heroin, statins/zidovudine, hypothyroidism and polymyositis/dermatomyositis, "
        "the two electrolyte causes of rhabdomyolysis listed are ______ and hypophosphatemia.",
        ["hypokalemia", "hyperkalemia", "hypercalcemia", "hypernatremia"], 0,
        "Causes of rhabdomyolysis include decreased K+ and decreased PO4(3-); hyperkalemia is a consequence of rhabdomyolysis, not a cause. "
        "The list also includes glycogen storage disease type 5 (McArdle disease), hypothyroidism and polymyositis/dermatomyositis. (Book p802)"),
    "MED-C18-153": ("fillup",
        "Fill up: Besides angiography, anticoagulation, thrombolysis and surgery, athero-embolic renal disease can also occur ______.",
        ["spontaneously", "only after renal biopsy", "only with bacterial endocarditis", "only in patients already on dialysis"], 0,
        "Athero-embolism is seen in patients with extensive aortic atherosclerosis after endovascular intervention (angiography, "
        "anticoagulation, thrombolysis, surgery) and can also occur spontaneously. (Book p803)"),
}

# questions removed because their content is now fully carried by the rewritten item
DELETE = {"MED-C17-043": "content folded into MED-C17-042"}
# format fixes only (no content change)
RELABEL = {"MED-C18-008": "recall"}



def _positions() -> dict:
    """id -> (part_path, item_index) using the built chapter file as the index."""
    where = {}
    for ch in range(13, 19):
        built = json.loads((ROOT / "data" / f"ch{ch}.json").read_text(encoding="utf-8"))
        ids = [q["id"] for q in built["questions"]]
        order = json.loads((PARTS / f"c{ch}" / "_order.json").read_text(encoding="utf-8"))
        cursor = 0
        for key in order:
            path = PARTS / f"c{ch}" / f"{key}.json"
            part = json.loads(path.read_text(encoding="utf-8"))
            for i in range(len(part["items"])):
                where[ids[cursor]] = (path, i)
                cursor += 1
    return where


def patch() -> None:
    for slug, (fmt, q, opts, ans, exp) in FIX.items():
        assert fmt in {"fillup", "match", "truefalse", "scenario", "oddoneout", "recall", "numeric", "management"}, slug
        assert len(opts) == 4 and len(set(opts)) == 4 and all(opts), slug
        assert 0 <= ans <= 3, slug
        assert exp.strip().endswith(")"), slug
        longest = max(len(o) for i, o in enumerate(opts) if i != ans)
        assert len(opts[ans]) <= 3.0 * max(longest, 1), f"{slug}: answer-length giveaway"

    where = _positions()
    missing = [k for k in list(FIX) + list(DELETE) + list(RELABEL) if k not in where]
    if missing:
        raise SystemExit(f"ids not found in source parts: {missing}")

    touched: dict = {}
    for qid, (fmt, q, opts, ans, exp) in FIX.items():
        path, idx = where[qid]
        touched.setdefault(path, set()).add(idx)
    for qid in DELETE:
        path, idx = where[qid]
        touched.setdefault(path, set()).add(idx)
    for qid in RELABEL:
        path, idx = where[qid]
        touched.setdefault(path, set()).add(idx)

    for path, idxs in touched.items():
        part = json.loads(path.read_text(encoding="utf-8"))
        items = part["items"]
        for idx in sorted(idxs, reverse=True):
            qid = next(k for k, (p, i) in where.items() if p == path and i == idx)
            if qid in DELETE:
                del items[idx]
            elif qid in RELABEL:
                items[idx]["fmt"] = RELABEL[qid]
            else:
                fmt, q, opts, ans, exp = FIX[qid]
                items[idx] = {"fmt": fmt, "q": q, "opts": opts, "ans": ans, "exp": exp}
        path.write_text(json.dumps(part, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("patched", path.relative_to(ROOT), f"({len(items)} items)")
    print(f"replaced {len(FIX)}, relabelled {len(RELABEL)}, deleted {len(DELETE)}")


if __name__ == "__main__":
    patch()
