# Chapters 60–61 — Build Report (Portal Hypertension, Ascites & Hepatorenal Syndrome)

Scope: **Book p1001–p1009** (Marrow Ed 8, Medicine Vol 3), covering Portal Hypertension and Ascites & Hepatorenal Syndrome:

| # | Chapter | Book pages | Units | Questions |
|---|---|---|---|---|
| 60 | Portal Hypertension | p1001–1004 | 8 | **86** |
| 61 | Ascites and Hepatorenal Syndrome | p1005–1009 | 8 | **81** |
| **Total** | | **9 pages** | **16** | **167** |

Bank total after this build:
**2169 questions · 198 units · 27 live chapters**, with all **134 in-scope Book pages** (p705–p829, p1001–p1009) represented.

Every page was rendered from high-resolution scan captures and read line-by-line before authoring — diagrams, flowcharts, anatomical orders, dosing ladders, tables, and diagnostic criteria included. Chapters were authored and validated via the page-anchored pipeline (`data/parts/c60…c61/<page><section>.json` → `author.py` → `data/chNN.json`).

---

## Detailed Line-by-Line Chapter Coverage

### Chapter 60: Portal Hypertension (p1001–1004) · 86 Questions · 8 Units
- **p1001 (Venous anatomy, pressures, survival & collateral systems)**:
  - Portal vein formed by confluence of Superior Mesenteric Vein (SMV) and Splenic Vein; Splenic Vein receives Inferior Mesenteric Vein (IMV).
  - Normal portal venous pressure: 5–10 mmHg.
  - Definition of portal hypertension: portal venous pressure > 10 mmHg or Hepatic Venous Pressure Gradient (HVPG) > 5 mmHg.
  - Natural history: compensated cirrhosis (median survival >12 years) versus decompensated cirrhosis (median survival printed as "a years", representing ~1 year).
  - Major consequences of decompensation: Portal hypertension, Ascites, Jaundice.
  - Caput medusae: recanalization of the umbilical vein in the falciform ligament, radiating outward from the umbilicus.
  - Anatomic branching tree verified via 28× zoom:
    - 1st order portal vein
    - 2nd order portal vein
    - 3rd order portal vein bifurcation
    - Entry label printed with degraded prefix as "ard order portal vein (Entry)".
- **p1002 (Hemodynamics, HVPG thresholds & anatomic classification)**:
  - Hemodynamic law: $\Delta P = Q \times R$ (Pressure = Flow × Resistance).
  - Sinusoidal vasoconstriction mechanisms:
    - Mechanical component: regenerative nodules compressing hepatic sinusoids.
    - Functional component: decreased endothelial nitric oxide (↓NO) causing stellate cell contraction and defenestration.
  - HVPG diagnostic cutoffs:
    - 1–5 mmHg: Normal.
    - ≥ 10 mmHg: Clinically significant portal hypertension.
    - ≥ 12 mmHg: Threshold for variceal rupture/bleeding.
    - ≥ 20 mmHg: High risk of early rebleeding and treatment failure / increased mortality.
  - Anatomic tree of causes:
    - Pre-hepatic: Extrahepatic Portal Venous Obstruction (EHPVO), presenting predominantly in children aged 3–8 years.
    - Post-hepatic: Budd–Chiari Syndrome (classic triad: hepatomegaly, ascites, abdominal pain); Right Heart Failure (RHF) from tricuspid regurgitation (TR), restrictive cardiomyopathy (RCM), constrictive pericarditis with elevated JVP.
    - Intra-hepatic (divided by 3rd order portal vein):
      - Pre-sinusoidal: Non-Cirrhotic Portal Fibrosis (NCPF), Schistosomiasis, Sarcoidosis.
      - Sinusoidal: Cirrhosis (most common).
      - Post-sinusoidal: Sinusoidal Obstruction Syndrome / Veno-Occlusive Disease (SOS/VOD), occurring 10–30 days post-hematopoietic stem cell transplant (HSCT) following high-dose alkylating conditioning regimens.
- **p1003 (Clinical evaluation, HVPG measurement & primary prophylaxis)**:
  - Work-up algorithm: elevated LFTs + fatty liver on USG with AST/ALT < 150 → NASH workup → Fibroscan stiffness ≥ 13.5 kPa indicating cirrhosis → splenomegaly with thrombocytopenia indicating portal hypertension → HVPG and upper GI endoscopy.
  - HVPG calculation: $\text{HVPG} = \text{WHVP} - \text{FHVP}$ (Wedged Hepatic Venous Pressure minus Free Hepatic Venous Pressure; note FHVP printed as "FWVP" in text).
  - Pressures across etiologies:
    - Cirrhosis: high WHVP, normal FHVP, high HVPG.
    - Budd–Chiari: high WHVP, high FHVP, normal or near-normal HVPG.
    - EHPVO: normal WHVP, normal FHVP, normal HVPG.
  - Primary prophylaxis: HVPG > 10 mmHg warrants non-selective beta-blockers (NSBB), with carvedilol identified as best/first choice.
  - Endoscopic Variceal Ligation (EVL) indications: intolerance/contraindications to NSBB (asthma/COPD, severe bradycardia) or failure to achieve target HVPG reduction.
  - Mild-to-moderate varices managed conservatively without band ligation.
  - Modified Child–Pugh scoring: 5 parameters (Bilirubin, Albumin, INR/PT, Ascites, Encephalopathy); Classes B and C grouped as "Requires transplant".
- **p1004 (Variceal hemorrhage pathophysiology, statistics & acute bleed ladder)**:
  - Determinants of variceal wall tension: Laplace's law (wall tension proportional to vessel diameter and transmural pressure/HVPG).
  - Variceal bleeding epidemiology: 50% prevalence in cirrhosis (as printed in book summary), 8%/year development rate, 5–15%/year occurrence of bleeding; small varices (≤5 mm) <10%/year bleeding risk, large varices 30%/year, index bleed mortality 15–30%.
  - Acute variceal bleed resuscitation ladder:
    1. Large-bore peripheral IV access and airway stabilization.
    2. Vasoactive therapy: Terlipressin first-line (printed as "a mg" stat, intended 2 mg stat, followed by "a mg" Q6h for 48 hours; octreotide 50 µg IV stat followed by 50 µg/hour infusion).
    3. Concomitant measures: prophylactic antibiotics, cautious blood transfusion (target Hb 7–8 g/dL), endotracheal intubation if encephalopathic.
    4. Urgent endoscopy within 12 hours: band ligation preferred over sclerotherapy.
    5. Salvage therapy: TIPSS (Transjugular Intrahepatic Portosystemic Shunt).

---

### Chapter 61: Ascites and Hepatorenal Syndrome (p1005–1009) · 81 Questions · 8 Units
- **p1005 (Ascites definition, epidemiology, fulminant hepatitis & SAAG map)**:
  - Definition: accumulation of free fluid within the peritoneal cavity; earliest clinical sign of hepatic decompensation.
  - Onset epidemiology: 90% due to portal hypertension (85% cirrhosis, 5% non-cirrhotic portal hypertension); 10% due to primary peritoneal causes.
  - Ascites in fulminant hepatitis: develops acutely without the chronic stigmata of portal hypertension; causes include paracetamol overdose, alcohol toxicity, mushroom poisoning (*Amanita phalloides*), and rat poison (yellow phosphorus).
  - Serum-Ascites Albumin Gradient (SAAG): $\text{SAAG} = \text{Serum Albumin} - \text{Ascitic Fluid Albumin}$.
  - SAAG classification:
    - High SAAG (≥ 1.1 g/dL, 90% of cases): indicates portal hypertension.
      - High protein: post-sinusoidal / hepatic vein outflow obstruction (Budd–Chiari syndrome).
      - Low protein: sinusoidal portal hypertension (cirrhosis).
    - Low SAAG (< 1.1 g/dL, 10% of cases): indicates increased peritoneal permeability or hypoalbuminemia.
      - High protein: peritoneal carcinomatosis, peritoneal tuberculosis.
      - Low protein: profound hypoproteinemia/nephrotic syndrome.
- **p1006 (Pathophysiology of fluid retention, chylous fluid table & tapping)**:
  - Hemodynamic cascade: sinusoidal portal hypertension → nitric oxide (NO) overproduction → splanchnic arterial vasodilation → decrease in effective intravascular volume → compensatory activation of ADH, Sympathetic Nervous System (SNS), and Renin-Angiotensin-Aldosterone System (RAAS) → avid renal sodium and water retention → ascites.
  - Downstream clinical sequelae: refractory ascites, dilutional hyponatremia, hepatorenal syndrome (HRS).
  - Chylous versus pseudochylous ascites comparative table:
    - Onset: Sudden (chylous) vs Gradual (pseudochylous).
    - Etiology: Lymphatic trauma/disruption vs Chronic inflammation (Rheumatoid arthritis, TB).
    - Gross appearance: Milky-white (or yellow-to-bloody) vs Milky or greenish with a metallic sheen.
    - Microscopy: Lymphocytosis vs Mixed cellular reaction with cholesterol crystals.
    - Triglycerides: > 110 mg/dL vs < 50 mg/dL.
    - Lipoprotein electrophoresis: Chylomicrons present vs Chylomicrons absent with cholesterol crystals (+).
  - Paracentesis tapping landmark: Left lower quadrant (LLQ), 3 cm cephalad and 2 cm medial to the anterior superior iliac spine (ASIS), or point of maximal dullness. Clinical rule: "Always look for JVP for constrictions."
  - Ascites clinical grading and management:
    - Grade 1 (Mild, detectable only on USG): No specific pharmacological treatment.
    - Grade 2 (Moderate, symmetrical abdominal distension): Dietary sodium restriction to 2 g/day (printed as "a g/day"); start spironolactone 100 mg/day (titrate up to max 400 mg/day); if inadequate response, add furosemide (Lasix) 40 mg/day (titrate up to max 160 mg/day).
    - Grade 3 (Large, marked abdominal distension): Large-volume paracentesis (LVP) followed by dietary sodium restriction and diuretics (unless refractory); if no response → TIPSS.
- **p1007 (Ascitic fluid detection, SBP criteria, variants & prophylaxis)**:
  - Fluid volume detection thresholds:
    - < 100 mL: Detectable by ultrasonography (USG).
    - 500 mL: Minimum volume to elicit clinical shifting dullness.
    - 1.5 L: Minimum volume to elicit a fluid thrill / wave.
  - Refractory ascites definition: lack of therapeutic response to maximum diuretic doses.
  - Large-volume paracentesis rule: must be accompanied by intravenous albumin replacement to prevent circulatory dysfunction.
  - Spontaneous Bacterial Peritonitis (SBP):
    - Causative microbiology: Gram-negative bacilli, predominantly *Escherichia coli*.
    - Diagnostic triad:
      1. Ascitic fluid WBC ≥ 500 cells/mL OR PMN (neutrophil) count ≥ 250 cells/mL.
      2. Positive monobacterial ascitic fluid culture.
      3. Absence of a surgically treatable intra-abdominal infection source.
    - Clinical variants (milder degrees of SBP seen in patients with minimal immunity and preserved opsonization):
      - Culture Negative Neutrocytic Ascites (CNNA): Criteria 1 and 3 present, Criterion 2 absent (elevated PMNs ≥ 250/mL, negative culture).
      - Monobacterial Non-Neutrocytic Ascites (MNNA): Criteria 2 and 3 present, Criterion 1 absent (positive culture, PMNs < 250/mL; Gram-positive organisms > Gram-negative organisms).
    - Secondary surgical peritonitis criteria: ascitic fluid protein > 1 g/dL, glucose < 50 mg/dL, and markedly elevated LDH (LDH ↑↑).
    - Empirical antimicrobial therapy: Inj Cefotaxime 2 g IV TDS for 5 days (printed as "ag IV TDS x 5days").
    - Secondary prophylaxis: Tab Norfloxacin 400 mg OD for life for:
      - Prior documented episode of SBP.
      - Child–Pugh score ≥ 9.
      - Ascitic fluid total protein < 1.5 g/dL in cirrhosis.
    - Prophylaxis in acute upper GI bleeding: Tab Norfloxacin 400 mg BD for 7 days.
- **p1008 (Refractory ascites subtypes, TIPSS & HRS pathogenesis/diagnosis)**:
  - Refractory ascites classification:
    - Diuretic Resistant Ascites: no response to full-dose diuretics (spironolactone 400 mg/day [printed as 40 mg] + furosemide 160 mg/day); directly progresses to hepatorenal syndrome (HRS).
    - Diuretic Intractable Ascites: inability to administer full diuretic doses due to therapy-limiting medical complications (hypokalemia, hyperkalemia, progressive renal failure).
    - Management of refractory ascites: TIPSS.
  - Hepatorenal Syndrome (HRS) pathogenesis:
    - Splanchnic vasodilation stimulates ADH, SNS, and RAAS.
    - Acute renal vasoconstriction causes pre-renal failure → HRS-AKI (terrible prognosis, 100% mortality without liver transplant).
    - Prolonged vasoconstriction over time with refractory ascites → HRS-NAKI (non-AKI).
  - Diagnostic criteria: HRS is a diagnosis of exclusion in a patient with Cirrhosis, Portal Hypertension, and Ascites.
  - Conditions that must be ruled out:
    - Pre-renal: Diuretic excess, severe hypoalbuminemia (marked reduction in serum albumin), acute upper GI bleeding.
    - Intra-renal: Proteinuria, hematuria.
    - Ultrasonography: Rule out structural kidney abnormality.
    - Shock / sepsis.
    - Nephrotoxic drugs: Diuretics, NSAIDs.
- **p1009 (HRS medical bridge & Hepatopulmonary syndrome)**:
  - Medical management of HRS before liver transplantation (reversal of splanchnic vasodilation):
    - Terlipressin: 1 mg IV every 4–6 hours, titrated up to 2 mg IV every 4–6 hours (maximum dose: 12 mg/day).
    - Alternative: Subcutaneous Octreotide + oral Midodrine (oral $\alpha$-agonist).
    - Norepinephrine infusion.
  - Definitive management of HRS: Orthotopic Liver Transplantation.
  - Hepatopulmonary Syndrome (HPS):
    - Pathophysiology: Chronic liver disease stimulates excess nitric oxide (NO) production, inducing severe intrapulmonary capillary dilatation from normal 8–15 µm up to 50–500 µm.
    - Consequences: Decreased oxygen diffusion across dilated vessels and anatomical arteriovenous (AV) shunting, causing hypoxia/hypoxemia via ventilation-perfusion (V/Q) mismatch.
    - Clinical hallmarks:
      - Platypnea: Dyspnea provoked by standing upright, caused by increased gravitational AV shunt activation and cephalad diaphragm motion.
      - Orthodeoxia: Arterial deoxygenation defined as a drop in SpO2 > 3% upon standing upright.
    - Investigation of Choice (IOC): Bubble Echocardiography / Contrast Transthoracic Echocardiography (demonstrates delayed microbubble transit into the left atrium after ≥3–4 cardiac cycles).
    - Definitive treatment: Liver transplantation.

---

## Question Quality & Audit Metrics

### Format Mix Across Chapter 60 and 61
- **Chapter 60 (86 items)**: fillup 24, recall 9, match 13, numeric 15, scenario 11, truefalse 8, oddoneout 5, management 1.
- **Chapter 61 (81 items)**: fillup 17, recall 16, match 13, numeric 10, scenario 10, truefalse 5, oddoneout 5, management 5.

### Predictability & Length Gates
- **Longest option is correct**:
  - Ch 60: 24.4% (below 25% expected chance)
  - Ch 61: 34.6% (well below the 40% ceiling)
- **Answer term leaked in stem**:
  - Ch 60: 0.0%
  - Ch 61: 0.0%
- **Reused option sets**:
  - Ch 60: 3 (all distractor sets unique)
  - Ch 61: 0 (completely unique distractor permutations)
- **Filler distractors**: 0.0% across both chapters.
- **Answer/distractor length ratio**: Pre-screened with strict ratio ≤ 1.8 scanner; author.py 3.0× hard gate passed with zero violations.

---

## Verification Pipeline Summary
- `author.py 60` and `author.py 61`: Clean generation, sequential IDs, correct answer hashing.
- `build_content.py`: Embedded 2169 questions and 198 units across 27 live chapters into `pulse-medicine.html`.
- `check_integrity.py`: PASS — all 134 in-scope pages verified, IDs sequential, sources match app.
- `check_app_smoke.js`: PASS — UI runtime and question rendering verified in Node.
- `audit_variety.py`: Complete report output stored in `AUDIT.md`.
