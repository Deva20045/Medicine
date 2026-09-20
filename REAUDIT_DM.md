# Strict visual re-audit — Diabetes Mellitus, Chapters 44–46

**Source:** `uploads/Medicine_Vol3_Part4_pages_894-964.pdf`  
**Offset:** Book page = PDF page + 893  
**Audited PDF pages:** 24–42  
**Audited book pages:** 917–935  
**Date:** 2026-09-20

## Scope and method

I rendered every source page in the requested range with the repository renderer:

```bash
python3 _render/render.py \
  uploads/Medicine_Vol3_Part4_pages_894-964.pdf 24 42 893 2.5
```

This produced `_render/_917.png` through `_render/_935.png` (the render images
are scratch artifacts covered by `.gitignore`). I read each page visually from
its upper-left content through its lower-right footer, including the handwritten
arrows, algorithm branches, table cells, graph captions, dose ladders and
illustrations. The editable source was then rebuilt into one page part per book
page. Within each part, questions follow the vertical order of the scanned page;
the `_order.json` files preserve page order.

No outside clinical guideline, trial name, drug, or correction was used to fill a
source gap. Where the scan uses an unusual abbreviation, label, range or diagram
arrow, the question and explanation retain the page's literal teaching point.

## Page-by-page coverage

### Chapter 44 — Introduction to Diabetes Mellitus and Classification (pp917–926)

| Book page | Rebuilt coverage, in scan order | Part |
|---|---|---|
| 917 | Common endocrinopathy and hyperglycemia; Type 1, Type 2 (90–95%), hybrid/Type 1.5, Type 3 branches, Type 4/MARD, MODY and GDM; IDE/APO-Ba Alzheimer’s drawing; artificial-pancreas sensor, pump and smartphone sequence. | `data/parts/c44/p917a.json` |
| 918 | Three pillars (liver, pancreas, skeletal muscle); GLUT-4 tissue box; ominous-octet labels and renal/adipose/FFA flow; CPT-1 drawing; insulin/HSL note. | `data/parts/c44/p918a.json` |
| 919 | Dirty dozen, Treacherous 13 and Faithless 14; four diagnostic branches (HbA1c, FPG, 2-hour 75-g PPBG, RBS plus symptoms); hyperosmotic symptom arrows; normal/pre-diabetes table and 10–15% annual progression note. | `data/parts/c44/p919a.json` |
| 920 | Pre-diabetes metformin profile (age 40–60, HbA1c ≥6%, FBS ≥110, overweight); gestational-DM note; pioglitazone/PPAR-γ and adverse list; six-month screening indications; HbA1c/FBS/PPBS tests, 6–8-week control and interference table. | `data/parts/c44/p920a.json` |
| 921 | KPD/Flatbush versus LADA table: sex, age/course, insulin requirement, C-peptide, antibodies and clinical features; GAD, ICA, IAA and ZnT8 sensitivity/specificity table; C-peptide/antibody diagnostic algorithm. | `data/parts/c44/p921a.json` |
| 922 | Type 2 natural-history graph (beta-cell function, hyperinsulinemia, insulin resistance, IFG/IGT, macro-/microvascular complications); comorbidities; five metabolic-syndrome criteria; WHO/Indian BMI cut-offs; Indian diabesity/adiposopathy list. | `data/parts/c44/p922a.json` |
| 923 | T-cell-mediated beta-cell destruction and insulinitis; GAD, ZnT8 and anti-insulin markers; HLA association; complete Type 1-versus-Type 2 table and parent/twin risk percentages. | `data/parts/c44/p923a.json` |
| 924 | Type A/Type B resistance and Rabson–Mendenhall table; Type 4/MARD and T-regulatory-cell arrow; MODY definition, inheritance, age, SGLT2/glycosuria and no-complication notes; MODY 1–5 table. | `data/parts/c44/p924a.json` |
| 925 | Young-onset diagnostic flow using fasting C-peptide and antibodies; Type 3 causes; Type 3a/3c labels; TCCP pathophysiology, clinical features, ERCP gold-standard note; Type 3d drug groups and examples. | `data/parts/c44/p925a.json` |
| 926 | Complete endocrinopathy list (Cushing’s through somatostatinoma) and complete genetic-disease list (Down’s through Laurence–Moon–Biedl syndrome). | `data/parts/c44/p926a.json` |

**Chapter 44 output:** 123 questions, 10 units. Formats: fillup 13,
match 26, truefalse 20, scenario 12, oddoneout 11, numeric 14, management
10, recall 17.

### Chapter 45 — Insulin Physiology and Acute Complications (pp927–932)

| Book page | Rebuilt coverage, in scan order | Part |
|---|---|---|
| 927 | Islets (2% of pancreatic volume), 51-amino-acid insulin, disulphide chains and tyrosine-kinase receptor; GLUT-4, gluconeogenesis/glycogenolysis, protein/fat effects; diabetic-specific infection bracket; insulin-production diagram. | `data/parts/c45/p927a.json` |
| 928 | GLUT1–5 and SGLT1/2 tissue/function table; glucose/C-peptide condition table; GLP-1/GIP incretin branch; intrajejunal effect graph; recombinant GLP-1, exenatide, liraglutide, semaglutide and tirzepatide notes. | `data/parts/c45/p928a.json` |
| 929 | GLP-1 versus GIP source, effects and half-life table; recombinant GLP-1 advantages; nephron-underdosing/Bartter note; acute/chronic/macrovascular insulin-deficiency complications; DKA precipitating factors. | `data/parts/c45/p929a.json` |
| 930 | DKA flow from absolute insulin deficiency and counter-regulatory hormones through CPT-1, lipolysis, beta-oxidation, acetyl-CoA and ketone bodies; cerebral-edema note; symptoms, signs and investigation list. | `data/parts/c45/p930a.json` |
| 931 | DKA two-line/fluid ladder (6–9 L; 3 L over 3, 9 and 12 hours), KCl and regular-insulin stat/infusion doses, hourly glucose and 5% dextrose switch; HHS pathophysiology, time course, no ketosis/acidosis and prognosis. | `data/parts/c45/p931a.json` |
| 932 | DKA-versus-HHS table for glucose, sodium, electrolytes, creatinine, osmolality, ketones, bicarbonate, pH, PCO2 and anion gap; slow 1/2-NS correction, 12-L replacement, IV-to-SC transition, overlap schedules and prognosis. | `data/parts/c45/p932a.json` |

**Chapter 45 output:** 72 questions, 6 units. Formats: fillup 9, match 16,
truefalse 12, scenario 6, oddoneout 6, numeric 7, management 7, recall 9.

### Chapter 46 — Management of Diabetes Mellitus — 2024 Guidelines (pp933–935)

| Book page | Rebuilt coverage, in scan order | Part |
|---|---|---|
| 933 | ADA 2024 oral-drug columns: metformin, gliclazide, oral GLP-1 analogues, SGLT-2 antagonists and linagliptin/gliptin note; exact HbA1c ranges, contraindication and mechanism notes; insulin indications, types and CGM-before-insulin line. | `data/parts/c46/p933a.json` |
| 934 | Dawn-phenomenon and Somogyi graphs and treatment directions; 8–8–8/16-U insulin regimens; six pre/post-meal glucose checks; increase-by-2/decrease-by-4 adjustment; CGMS components and equipment labels. | `data/parts/c46/p934a.json` |
| 935 | Diabetic-treatment flow; heart/HF/ASCVD and kidney/albuminuria macro priorities; SGLT-2 adverse counselling; BP targets; LDL target ladder and statin doses; aspirin 75 mg risk-factor branch; NASH and proteinuria regimens. | `data/parts/c46/p935a.json` |

**Chapter 46 output:** 36 questions, 3 units. Formats: fillup 3, match 9,
truefalse 6, scenario 3, oddoneout 3, numeric 5, management 4, recall 3.

## Integrity and anti-predictability checks

All authored items place the source-truth answer at option index 0 in the page
parts. `author.py` applies the deterministic SHA-256 rotation when assembling
chapter files, so the shipped answer positions are not predictable.

For the rebuilt chapters, the generated audit reports:

| Chapter | Questions | Filler distractors | Answer-term leak | Longest-option answer | Reused option sets |
|---:|---:|---:|---:|---:|---:|
| 44 | 123 | 0.0% | 0.0% | 15.4% | 40 |
| 45 | 72 | 0.0% | 0.0% | 11.1% | 23 |
| 46 | 36 | 0.0% | 0.0% | 11.1% | 12 |

Every question has four distinct medical options; no item uses “all of the
above”, “none of the above”, or other filler. Every explanation ends with the
exact page citation `(Book pNN)`. Every page unit contains fillup, match,
truefalse, scenario, oddoneout, numeric, management and recall items.

## Verification run

```text
$ python3 author.py 44 && python3 author.py 45 && python3 author.py 46
Ch44: 123 questions, 10 units
Ch45: 72 questions, 6 units
Ch46: 36 questions, 3 units

$ python3 build_content.py
Embedded 3533 questions and 296 units across 48 live chapter(s) of 74 roadmap chapters.

$ python3 check_integrity.py
PASS: 48 live chapter(s) of 74; 3533 questions; 296 units; all 240 in-scope
Book pages represented; IDs, four-option structure, citations, order, source
artifacts, UI hooks, and JavaScript syntax verified.

$ node check_app_smoke.js
PASS: 492 new-question answer paths across 19 units; matching boards, blanks,
feedback, locking and completion verified.

$ python3 audit_variety.py > AUDIT.md
PASS: chapters 44, 45 and 46 show all eight requested formats; filler and
answer-term leak are 0.0% for each rebuilt chapter.
```

The final shipped artifacts are the page parts, chapter unit manifests,
assembled `data/ch44.json`, `data/ch45.json`, `data/ch46.json`, the rebuilt
standalone `pulse-medicine.html`, `AUDIT.md`, and this report.
