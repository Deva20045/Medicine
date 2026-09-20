# Report — Chapters 64–69 (Vol 3 Part 5/6, Book p1020–1038)

**219 new questions · 19 units · all 19 pages p1020–1038 covered in printed order, nothing skipped.**

| Chapter | Title | Pages | Units | Questions | Format mix (fill / match / tf / scen / odd / recall / num / mgmt) |
|---|---|---|---|---|---|
| 64 | Biliary Cirrhosis | 1020–1022 | 3 | 44 | 7 / 8 / 6 / 2 / 5 / 8 / 6 / 2 |
| 65 | Autoimmune Hepatitis | 1023–1025 | 3 | 34 | 6 / 5 / 2 / 2 / 7 / 4 / 4 / 4 |
| 66 | Alcoholic Liver Disease | 1026–1029 | 4 | 43 | 7 / 6 / 4 / 2 / 6 / 11 / 6 / 1 |
| 67 | Nonalcoholic Steatohepatitis | 1030–1032 | 3 | 28 | 3 / 7 / 3 / 2 / 5 / 2 / 5 / 1 |
| 68 | Vascular Diseases of Liver | 1033–1035 | 3 | 30 | 5 / 9 / 3 / 2 / 1 / 7 / 2 / 1 |
| 69 | Hepatitis B Virus : Part 1 | 1036–1038 | 3 | 40 | 3 / 12 / 3 / 4 / 5 / 5 / 8 / 0 |

Source: `uploads/Medicine_Vol3_Part5_pages_965-1034.pdf` (PDF 56–70 → Book p1020–1034, K=964) and
`uploads/Medicine_Vol3_Part6_pages_1035-1070.pdf` (PDF 1–4 → Book p1035–1038, K=1034). Every page was
rendered at 2× (`_render/_10NN.png`) and read visually; the scan has no text layer.

## Method (same pipeline as Ch 57–63)

- One part file per page (`data/parts/cNN/p10NNa.json`), items authored top-to-bottom, left column before
  right column where the page has two columns, each table row and flowchart arrow taken in turn. Units
  (`data/units/cNN.json`) are one page each; question order inside a unit is the page's reading order.
- Authoring scripts are kept for auditability: `author_c64.py` … `author_c69.py` (+ `itemwriter_64_69.py`).
  Re-running them then `python3 assemble.py 64 65 66 67 68 69` reproduces the banks byte-for-byte.
- Options are written correct-first and rotated deterministically by `author.py`; only options shuffle,
  never the question sequence.
- Every unit contains fill-up, match-the-following, true/false, clinical scenario and odd-one-out items
  alongside numeric / recall / management stems. Distractors are drawn from neighbouring book facts
  (e.g. the AIH steroid taper vs the alcoholic-hepatitis taper, PBC vs PSC table rows swapped, HBeAg
  thresholds 20,000 vs 2,000), not generic filler. No "all/none of the above".

## Page-by-page coverage (ordered element → first question ID)

| Page | Source content covered, in printed order | First ID |
|---|---|---|
| p1020 | Cardinal intrahepatic cholestasis; definition (autoimmune, non-suppurative, small intrahepatic/intralobular ducts, T-cell > B-cell); AMA 95% against PDHE2; Note table hepatic (jaundice predominant) vs cholestatic (fatigue & pruritus → complete duct destruction → jaundice poor prognosis); prevalence F>M 9:1, 4th–5th decade; associations (Sjogren with arthritis, distal RTA type 1, gallstones); diagnostic algorithm (USG duct dilatation −ve → AMA → PBC; +ve → surgery); presentation list (asymptomatic m/c, fatigue m/c symptom, pruritus, jaundice 10% late/poor, hypercholesterolemia bracket, xanthelasma, hyperpigmentation, hepatomegaly 30–40%, splenomegaly <15%, steatorrhea ↓bile acid); fat-malabsorption tree (diarrhoea, ↓fat-soluble vitamins, ↓vit D → metabolic bone disease) | MED-C64-001 |
| p1021 | Labs (raised ALP, AMA IgM 95%, ANA 50%); histology (canal of Hering loss earliest, ductopenia m/c, florid duct lesion with non-caseating granulomas most characteristic); UDCA ↓progression, obeticholic acid farnesoid agonist; PSC: fibrosing destruction intra+extra hepatic, IgG4 disease d/t leaky gut; M>F 2nd–3rd decade; HLA B-8, DR-3; presentation (fatigue, pruritus, leaky gut, cholestasis); cholangiocarcinoma; UC 2/3rd vs 5% with atypical p-ANCA, pancolitis with rectal sparing, colorectal carcinoma, transplant only; labs IgG4, atypical p-ANCA, AMA −ve | MED-C64-019 |
| p1022 | MRCP (IOC)/ERCP → strictures/ectasia (image caption); concentric periductal onion-skin fibrosis (micrograph); surgery 25% recurrence; PBC vs PSC table — all 8 rows (population, disease type, HLA, smoking, association, diagnostic feature, treatment, carcinoma) | MED-C64-034 |
| p1023 | AIH Type-1 F>>M 2nd–3rd decade; ANA 100% (also drug-induced erythematosus, MCTD); HLA-DR03 SLE/lupoid, HLA-DR04 RA/T1DM/autoimmune thyroid; lymphoplasmacytic inflammation; interface hepatitis (piecemeal necrosis), emporipolesis (engulfing without killing), rosette formation; acinus diagram legend (central vein, hepatocytes, portal track, bile duct, portal vein, hepatic artery), limiting plate, inflammation; "Interphase hepatitis" micrograph caption | MED-C65-001 |
| p1024 | Presentation tree: acute (waxing/waning jaundice, non-resolving; 1st rule out HAV/HBV/HEV; then Wilson's / autoimmune ANA+ / FHF rare), chronic (fatigue & hepatomegaly + RA/SLE background; jaundice + splenomegaly rare/slow progression; LFT <150 ALT>AST → fibroscan), cirrhosis (portal HTN, liver failure, HCC significant risk also in hemochromatosis); A/G reversal → immunoelectrophoresis polyclonal hypergammaglobulinemia; Type-I table (ANA 100%, SMA, AAA poor prognosis, SLA most specific/poor prognosis, atypical p-ANCA in AIH/PSC/UC); Type-II table (LKM-1 also HCV, liver cytosol-1 poor prognosis); note LKM-2 drug, LKM-3 HDV; note AMA = PBC, cholestasis triad not in AIH | MED-C65-011 |
| p1025 | Type-II AIH (children, poor prognosis, HLA DR-7, T1DM/vitiligo/APS-1); treatment flow (fibroscan for cirrhosis; steroid 1 mg/kg/day × 4 wk → taper 12 wk ± azathioprine; after 3–4 months remission criteria ×4 vs relapse → transplant → recurrence) | MED-C65-028 |
| p1026 | 1 peg = 60 ml 40%; cirrhogenic dose male 40–80 g (2 pegs) / female 20–40 g (1 peg), 5 days/week × 15 years; alcoholic hepatitis mortality 70%, CDT best marker; progression diagram (3–5 yr reversible fatty liver → cirrhosis micro→macro nodular nucleus to periphery, HCC risk; alcoholic hepatitis high mortality, binge drinking); alcohol metabolism enzymes (ALDH, CYP2E1, catalase); alcohol → acetaldehyde (toxic) → products; ALDH polymorphism efficient vs poor metaboliser prone to hepatitis | MED-C66-001 |
| p1027 | HESST mnemonic (hypoxia zone 3 mitochondria; ER stress Mallory hyaline; superoxide ROS via CYP2E1; ↓SAM/↑SAH ↑TNF-α most important, Rx pentoxifylline); acetaldehyde ↑NADH → ↓glutathione → leaky gut; both micrograph captions; fat >5% hepatocytes, nucleus to periphery; labs (neutrophilia, enzymes 300–500, AST:ALT >2:1 likely / >3:1 highly suggestive, albumin not significant, PT/INR ↑, MCV ↑, thiamine depletion blocking pyruvate→acyl-CoA and transketolase); clinical (jaundice, soft painful abdomen, hepatomegaly) | MED-C66-011 |
| p1028 | Histology (centrilobular zone III fat; ballooning/alcoholic hyaline with PMN infiltrate classical); note HCV steatosis; trichrome caption nodules with fibrous septation; complications chain to ↑ICT → death with portal HTN; prognostic scores (DF formula ≥32, MELD ≥18, Glasgow ≥9); steroid indication DF ≥32, 1 mg/kg × 7 d taper 3 wk; unfit (sepsis, renal failure, ongoing GI disease) → pentoxifylline inhibits TNF-α 400 mg TDS × 4 wk | MED-C66-022 |
| p1029 | NASH m/c cause of cirrhosis; micronodular causes ×6; macronodular Wilson's; "Pretty visits Jamaica with Alcohol and Acid" microvesicular ×7 vs macrovesicular (HCV, NASH, Wilson's); Reye's swollen fewer mitochondria; nutmeg liver chronic venous; Mallory–Denk ER-stress eosinophilic inclusions, seen-in list ×7, not in HBV/HCV | MED-C66-032 |
| p1030 | NAFLD ≥5% macrovesicular fat (micrograph caption); 80% IFL vs 20% NASH; NASH histology ×4 incl. chicken-wire zone 3; risk-factor table all 3 columns (8 + 6 + 6 entries); 2-hit hypothesis, 10–15% over 15 yr, cirrhosis → PHTN/liver failure/HCC, direct HCC only in NASH & HBV | MED-C67-001 |
| p1031 | Symptoms ×3; hepatomegaly + rare signs ×4 with brackets; investigations 1–4 (biopsy, ferritin, USG → MR elastography > transient, ALT/AST); fibroscan figure (Vs 1.1/1.7/3.6 m/s ≈ 3/9/40 kPa, F0–F4, 2.5 × 4 cm probe volume); enzyme algorithm (normal → IFL; ↑↑ <150 AST<ALT → NASH → fibroscan N / ↑↑; AST>ALT → cirrhosis) | MED-C67-013 |
| p1032 | Supportive (10% weight loss / 6 months; 30–45 min × 5 days/wk; omega-3, caffeine); vitamin E DOC 800–1000 U/day, three sub-bullets; saroglitazar 4 mg dual PPAR-α/γ; pioglitazone PPAR-γ may be tried; oral semaglutide GLP-1 RA | MED-C67-023 |
| p1033 | Classification tree (extrahepatic EHPVO non-cirrhotic; intrahepatic pre-sinusoidal 3rd-order/NCPF, sinusoidal cirrhosis PH, post-sinusoidal SOS veno-occlusive; post-hepatic BCS → cirrhosis); BCS pathogenesis (efferent ductule → IVC → RA); site hepatic vein m/c, terminal IVC 2nd; causes ×6 incl. AT3 > protein C/S; primary vs secondary (2°>>1°) inherited/acquired | MED-C68-001 |
| p1034 | m/c 30–40 yr post-partum female; zone 3 sinusoidal distension + pooling; subacute (m/c, refractory ascites + collaterals, high SAAG high protein); note high SAAG low protein = sinusoidal; acute hepatitis (pain + hepatomegaly + ascites, jaundice <10%, FHF rare); cirrhosis; prognosis 3-yr survival <10%; two-column mechanism flowchart in full; Doppler screening / CECT IOC / MRI; CECT caudate lobe hypertrophy caption; management (anticoagulate all; angioplasty ± stent → TIPSS) | MED-C68-010 |
| p1035 | EHPVO vs NCPF/IPH table header synonyms and all 8 rows (outcome, involvement, cause, presentation, prognosis, investigations, complications, treatment); note m/c PHTN Asia EHPVO vs world biliary atresia; image captions (CECT collaterals, colour Doppler cavernoma, obliterative portal venopathy with sclerotic non-patent tracts) | MED-C68-021 |
| p1036 | Structure (hepadnavirus, relaxed circular partially dsDNA, (+) primer / (−) RT, 42 nm Dane, 10 genotypes, 4 ORFs; genome figure labels); gene table 5 rows; progression (60-day IP, 95–99% / 1–5%, 95% vertical, cirrhosis → PHTN/HCC/liver failure, NASH also, no treatment); infectivity 100× HIV / 10× HCV; HAV 1, HEV 4 genotypes, A commonest, C HCC; all fluids except stool; pregnancy 90/10 rule | MED-C69-001 |
| p1037 | Transmission arms ×4 with percutaneous 6–30% (HCV 0.6–6.1%), sexual not established, transfusion 1:200,000 & 1:1,800,000 HBV>HBC; no feco-oral/breast milk; post-transfusion CMV>EBV>HCV; symptoms; investigations (anti-HAV IgM children, anti-HEV IgM adults → HBsAg/HBeAg/anti-HBc IgM); marker-curve legend and window period; interpretation table 2 columns; S/escape/occult mutants (no HBsAg, best test anti-HBc IgM); basal core mutant 30% HBeAg; HBV DNA best acute marker | MED-C69-015 |
| p1038 | Progression table 4 rows; follow-up timing and three conversions + chronic definition; chronic profile flow (HBeAg + → DNA >20,000; − → >2,000 vs <2,000 carriers no Rx, HCC risk); pre-core/basal core mutant poor prognosis ×3 risks; serological patterns table all 8 rows | MED-C69-027 |

## Source fidelity — printed wording kept, with clarification in explanations

- **p1020** "Hypercholesterolemia (Against : Dihydrolipoyl transacetylase)" — the bracket is the AMA target (E2), taught as printed with that clarification.
- **p1022** table prints "MRCP (IOP)" while the same page prints "MRCP (IOC)"; both are noted.
- **p1027** "Pyruvate ✗→ Acyl-CoA" is printed; explanation notes the physiological product is acetyl-CoA. "Fat pushes nucleus to periphery : macronodular" is printed (the usual term is macrovesicular); tested as printed.
- **p1037** "1 : 1800000 [HBV > HBC]" — HBC read as HCV, stated in the explanation.
- **p1038** follow-up bullet prints "Anti HBc IgG converts→ Anti HBc IgM"; taught as printed with an explicit note that this is the reverse of the usual class switch.
- **p1038** chronic-hepatitis carrier branch: "No need of Rx" and "Risk for HCC" both retained (the T/F item tests the trap).

## Verification

- `python3 build_content.py` → 4,933 questions · 390 units · 69 live chapters embedded.
- `python3 check_integrity.py` → PASS (all 334 in-scope pages p705–1038 represented; IDs, options, citations, order).
- `node check_app_smoke.js` → PASS, 9,866 answer paths across 390 units; zero new format warnings from Ch 64–69 (all match stems parse into the matching board).
- `python3 audit_variety.py` → every Ch 64–69 unit has all five requested formats; no filler options; "longest-option-is-answer" 9–30% (chance 25%).
- `python3 check_source_coverage.py` → existing manifests consistent; recorded source-review manifests remain at 3/74 (Ch 1–3). Ch 64–69 have the page-level checklist above but not yet the element-level JSON manifest in `data/source_review/`; they are LIVE, not certified under the `--require-all` gate.

**Next: Ch 70 "Hepatitis B Virus : Part 2" (p1039–1044).**
