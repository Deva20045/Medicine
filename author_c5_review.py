#!/usr/bin/env python3
"""Rebuild Ch 5 (Glomerulus — Anatomy, p730-733) in strict source order.

Source review 2026-09-21: all four pages read from the Part 1 scan (PDF pp38-41)
at 2x-16x zoom (whole-page renders plus glyph-level checks of every number).
Repairs vs the 56-question bank:
  * MED-C5-006 (PSGN expansion, printed on the disease line) sat after the
    sub-bullet items → moved ahead of them (new positions 4-6).
  * MED-C5-007 option A omitted the printed 'capillary pore diameter' step.
  * p730 figure labels were only partially questioned (one odd-one-out) →
    every printed label (9 labels + caption) now directly questioned.
  * The Size rule's first line ('< 4 mm : passes through') was uncovered → new
    item before the '> 8-10mm' item.
  * The 'mm' units printed for all filtration sizes are a repeated print error
    (nm meant) → taught as printed and flagged in the explanations.
  * The GBM visualisation tree's first branch (1. Electron m/s) was uncovered;
    the printed '1.'/'a.' numbering oddity is flagged.
  * The light-microscope image legend (PT/CL), its caption, and every
    juxtaglomerular-apparatus figure label + caption are now directly
    questioned (old bank tested only the two parenthetical synonyms).
  * MED-C5-035 silently corrected the printed 'Inside : alpha actin 4' to
    'alpha actinin 4' → re-authored to teach the print with a flag.
  * p732 figure (a) was UNTESTED → all 12 printed labels questioned.
  * p732 figure (b) covered only laminin-11/alpha3beta1 → F-actin, slit
    diaphragm, foot process, beta/alpha dystroglycan, 'Argin'/'Agrin', GEC,
    GBM label, the 13-name protein legend and the shared caption added.
  * 'Function : Filtration.' (slits) was uncovered → new item.
  * The podocyte-loss chain steps (podocyte detached / podocyturia /
    podocytopenia) were only inside MED-C5-041's option → own scenario item;
    MED-C5-041 (whole-chain match) is now a consolidation AFTER the step items
    (it previously sat before items re-testing later steps).
  * p733 congenital-NS table was tested cross-row before the row-1 cells
    (within-page order fault) → strict row order: row 1, row 2, row 3 cells,
    then the two cross-row consolidations. Histology/management cells and the
    inheritance cells now directly questioned.
  * MED-C5-051's answer moved into the new Finnish-type histology/management
    item; it is re-authored as a different cross-row consolidation.
Result: 88 questions in 8 retained units. Unit guides carry the revision note
(previous badges/XP retained; replay recommended), as in the Ch 1-4 repairs.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = json.loads((ROOT / "data" / "ch05.json").read_text())
# One-shot repair script: the input must be the pre-review 56-question bank.
if len(OLD["questions"]) != 56 or "Source-order revision" in OLD["units"][0].get("guide", ""):
    raise SystemExit("author_c5_review.py expects the pre-review 56-question data/ch05.json as input; refusing to re-run.")
BY_ID = {q["id"]: dict(q) for q in OLD["questions"]}

REVISION = ("Source-order revision, 21 Sep 2026: questions have been repaired, "
            "expanded and reordered. Previous completion badges and XP are retained; "
            "replay this unit to cover the revised questions. ")


def keep(old_id, **over):
    q = dict(BY_ID[old_id])
    q.update(over)
    return q


def new(sec, page, fmt, q, opts, ans, exp):
    return {"id": None, "sec": sec, "page": page, "q": q, "opts": opts,
            "ans": ans, "exp": exp, "fmt": fmt}


SEC_FB = "Parts of Filtration Barrier · p730"
SEC_CKD = "Pathophysiology of CKD · p730"
SEC_PASS = "Factors: passage through filtration barrier · p730"
SEC_FIG730 = "Glomerular capillary figure · p730"
SEC_GBM = "Glomerular Basement Membrane · p731"
SEC_MES = "Mesangial cells & microscopy figures · p731"
SEC_SD = "Slit Diaphragm / Filtration Slits · p732"
SEC_FIG732 = "Slit diaphragm podocytes figure · p732"
SEC_ANG = "Angiotensin-podocyte chain & Rx · p732"
SEC_CNS = "Congenital Nephrotic Syndrome · p733"
SEC_SITE = "Site-disease table · p733"

MM_FLAG = ("The scan prints 'mm' for every value on these size lines "
           "(nanometres are meant; the fenestration sizes on the same page correctly print 'nm') — "
           "taught as printed, flagged not corrected. ")

seq = [
    # ---- p730: CAPILLARY ENDOTHELIUM WITH FENESTRATIONS, Fenestration Slits ----
    keep("MED-C5-001"),
    keep("MED-C5-002"),
    keep("MED-C5-003"),
    # disease line (with the PSGN parenthesis) precedes its sub-bullets: old MED-C5-006 moved up
    keep("MED-C5-006",
         exp="PSGN = Post Streptococcal Glomerulo Nephritis (printed as three words), the disease of "
             "the capillary endothelium. (Book p730)"),
    keep("MED-C5-004"),
    keep("MED-C5-005",
         exp="The PSGN sub-bullet prints 'No risk for CKD.' — an absolute source claim taught as "
             "printed (with microhematuria, minimal proteinuria and exudative neutrophilic infiltration). (Book p730)"),
    # ---- p730: Pathophysiology of CKD chain ----
    keep("MED-C5-007",
         opts=["↓ functional nephrons → hyperfiltration by remaining nephrons → intraglomerular HTN → capillary stretching → ↑ pore diameter → proteinuria",
               "Hyperfiltration → ↓ functional nephrons → proteinuria → intraglomerular HTN → capillary stretching",
               "Proteinuria → ↓ functional nephrons → hyperfiltration → capillary stretching → intraglomerular HTN",
               "Intraglomerular HTN → ↓ functional nephrons → hyperfiltration → proteinuria → capillary stretching"]),
    keep("MED-C5-008"),
    keep("MED-C5-009",
         q="Fill up: In the CKD chain, the interstitial-inflammation branch of proteinuria leads to formation of TGF-______.",
         exp="Proteinuria splits into tubulotoxicity and interstitial inflammation; the inflammation "
             "branch gives TGF-β formation → tubulo interstitial fibrosis. (Book p730)"),
    keep("MED-C5-010"),
    # ---- p730: Factors determining passage (Size branch, then Charge branch) ----
    new(SEC_PASS, 730, "numeric",
        "By the size rule, effective diameter below which value (as printed) passes through the filtration barrier?",
        ["4 mm", "8–10 mm", "7.6 mm", "2 mm"], 0,
        "Size rule: effective diameter < 4 mm passes through. " + MM_FLAG + "(Book p730)"),
    keep("MED-C5-011",
         opts=["8–10 mm", "4 mm", "7.6 mm", "2 mm"],
         exp="Size: effective diameter < 4 mm passes through; > 8–10 mm doesn't pass. " + MM_FLAG + "(Book p730)"),
    keep("MED-C5-012",
         opts=["Molecules of effective diameter 4–8 mm are repelled if they carry a negative charge",
               "Molecules of effective diameter 4–8 mm are repelled if positively charged",
               "Charge plays no role between 4 and 8 mm",
               "Only molecules above 10 mm are charge-repelled"],
         exp="Charge: effective diameter 4–8 mm is repelled if −ve charge (the 'repelled' note sits above "
             "the arrow). " + MM_FLAG + "(Book p730)"),
    keep("MED-C5-013",
         opts=["7.6 mm and a negative charge", "4 mm and a positive charge", "10 mm and no charge", "2 mm and a negative charge"],
         exp="Eg: albumin 7.6 mm, -vely charged — hence repelled despite sitting in the 4-8 mm window. "
             + MM_FLAG + "(Book p730)"),
    # ---- p730: glomerular-capillary figure, labels top-to-bottom, then caption ----
    new(SEC_FIG730, 730, "match",
        "Match each label in the glomerular-capillary figure with the structure it marks — "
        "1) Glomerular basement membrane 2) Podocyte 3) Foot processes ... "
        "A) Cell body whose label prints with a stray '7' B) Projections hugging the capillary C) Membrane beneath the tuft cells",
        ["1-C, 2-A, 3-B", "1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"], 0,
        "Glomerular basement membrane → the membrane beneath the tuft; podocyte → its cell body (the "
        "printed label reads 'Podocyte 7' — a stray '7' glyph sits just before the leader line); "
        "foot processes → the projections hugging the capillary. (Book p730)"),
    new(SEC_FIG730, 730, "match",
        "Match each label in the glomerular-capillary figure with the structure it marks — "
        "1) Capillary 2) Capillary endothelium 3) Mesangial angle ... "
        "A) Corner between capillary and mesangium B) Lining of the capillary lumen C) The lumen seen in cross-section",
        ["1-C, 2-B, 3-A", "1-B, 2-C, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B"], 0,
        "Capillary → the lumen in cross-section; capillary endothelium → its cellular lining; "
        "mesangial angle → the corner between capillary and mesangium. (Book p730)"),
    new(SEC_FIG730, 730, "match",
        "Match each label in the glomerular-capillary figure with the structure it marks — "
        "1) Microfilaments 2) Mesangium 3) Mesangial matrix ... "
        "A) The mesangial region proper B) Matrix material at the tuft base C) Cytoskeletal elements labelled inside the mesangial region",
        ["1-C, 2-A, 3-B", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"], 0,
        "Microfilaments → cytoskeletal elements inside the mesangial region; mesangium → the mesangial "
        "region proper; mesangial matrix → the matrix at the tuft base. (Book p730)"),
    new(SEC_FIG730, 730, "recall",
        "The glomerular cross-section figure on this page carries the caption:",
        ["Glomerular capillary", "Filtration barrier", "Glomerular tuft", "Renal corpuscle"], 0,
        "Caption as printed: 'Glomerular capillary'. (Book p730)"),
    keep("MED-C5-014",
         opts=["Slit diaphragm", "Glomerular basement membrane", "Foot processes", "Mesangial matrix"],
         exp="Figure labels: podocyte (printed with a stray '7'), glomerular basement membrane, foot "
             "processes, capillary, mesangial angle, capillary endothelium, microfilaments, mesangium and "
             "mesangial matrix; no slit diaphragm (that is diagrammed later with podocytes). (Book p730)"),
    # ---- p731: GBM section ----
    keep("MED-C5-015"),
    keep("MED-C5-016"),
    keep("MED-C5-017"),
    keep("MED-C5-018",
         opts=["1-B, 2-A", "1-A, 2-B", "Both are X-linked with absent stain", "Both are AD/AR with normal stain"],
         exp="85% X-linked with alpha5 defect and absent skin/epidermal stain; 10-15% AD/AR with the "
             "printed 'alpha3+/ alpha4' defect cell and normal stain. The column header prints "
             "'Immunoflorescence' (one u) — taught as printed. (Book p731)"),
    keep("MED-C5-019",
         exp="Negative charge: heparin sulfate proteoglycans (eg: perlecan, agrin) — 'Heparin sulfate' is "
             "the printed spelling; standard nomenclature is heparan sulfate. (Book p731)"),
    new(SEC_GBM, 731, "recall",
        "In the GBM visualisation tree, the method listed first (printed as '1.') is:",
        ["Electron m/s (microscope)", "Gomori methenamine silver stain", "Masson's trichrome", "Immunofluorescence"], 0,
        "Visualisation of GBM: 1. Electron m/s (microscope), paired with what is printed as "
        "'a. Stains under light m/s' — the mixed '1.'/'a.' numbering is a source oddity, flagged not "
        "corrected. (Book p731)"),
    keep("MED-C5-020",
         exp="Stains under light m/s (printed 'a.'): Gomori methenamine Silver Stain > masson's Trichrome "
             "('masson's' lowercase is the printed form). (Book p731)"),
    keep("MED-C5-021"),
    keep("MED-C5-022"),
    keep("MED-C5-023"),
    # ---- p731: Note (mesangial cells) ----
    keep("MED-C5-024"),
    keep("MED-C5-025"),
    keep("MED-C5-026"),
    keep("MED-C5-027"),
    keep("MED-C5-028"),
    keep("MED-C5-029"),
    # ---- p731: light-microscope image (legend, labels, caption) ----
    new(SEC_MES, 731, "fillup",
        "Fill up: In the light-microscope image legend, PT = proximal tubule and CL = ______.",
        ["Capillary lumen", "Collecting loop", "Cellular layer", "Central lumen"], 0,
        "Legend as printed: 'CL = capillary lumen' and 'PT = proximal tubule'; the photo also labels "
        "PT and CL directly. (Book p731)"),
    new(SEC_MES, 731, "match",
        "Match each label in the light-microscope image with what its arrows mark — "
        "1) Mesangial cells 2) Bowman's space 3) PT ... "
        "A) The urinary space around the tuft B) Proximal tubule profiles C) Cells in the mesangial regions",
        ["1-C, 2-A, 3-B", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"], 0,
        "Mesangial cells → cells in the mesangial regions; Bowman's space → the urinary space around "
        "the tuft; PT → proximal tubule profiles (legend: PT = proximal tubule). (Book p731)"),
    new(SEC_MES, 731, "match",
        "Match the remaining light-microscope image labels — 1) Open capillary loops 2) CL (four labels) ... "
        "A) Abbreviation for capillary lumen used on the lumens B) Arrows marking the patent capillary profiles",
        ["1-B, 2-A", "1-A, 2-B", "Both mark tubular profiles", "Both are parts of Bowman's capsule"], 0,
        "Open capillary loops → arrows onto the patent capillary profiles; CL → the lumen abbreviation "
        "printed on those spaces (capillary lumen). (Book p731)"),
    keep("MED-C5-030",
         opts=["Macula densa", "Mesangial cells", "Bowman's space", "Open capillary loops"],
         exp="Light microscope image labels mesangial cells, Bowman's space, PT (proximal tubule), CL "
             "(capillary lumen) and open capillary loops; the macula densa appears in the JGA figure. (Book p731)"),
    new(SEC_MES, 731, "recall",
        "The left-hand figure on this page (the histology photograph) is captioned:",
        ["Light microscope image", "Glomerular capillary", "Slit diaphragm podocytes", "Mesangial proliferative disease"], 0,
        "Caption as printed: 'Light microscope image'. (Book p731)"),
    # ---- p731: juxtaglomerular-apparatus figure (labels, bracket synonyms, caption) ----
    new(SEC_MES, 731, "match",
        "Match each label in the juxtaglomerular-apparatus figure with the structure it names — "
        "1) PCT 2) GC 3) AA ... "
        "A) Afferent arteriole B) The four capillary circles inside the tuft C) Proximal convoluted tubule",
        ["1-C, 2-B, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B", "1-B, 2-C, 3-A"], 0,
        "JGA figure abbreviations: PCT = proximal convoluted tubule; GC = the four glomerular capillary "
        "circles inside the tuft; AA = afferent arteriole. (Book p731)"),
    new(SEC_MES, 731, "match",
        "Match each label in the juxtaglomerular-apparatus figure with the structure it names — "
        "1) Parietal layer 2) DCT 3) Visceral layer ... "
        "A) Distal convoluted tubule B) Outer layer of Bowman's capsule C) Podocyte layer of the capsule",
        ["1-B, 2-A, 3-C", "1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"], 0,
        "Parietal layer → outer layer of Bowman's capsule; DCT → distal convoluted tubule; "
        "visceral layer → podocyte layer of the capsule. (Book p731)"),
    new(SEC_MES, 731, "match",
        "Match the remaining juxtaglomerular-apparatus labels — 1) EA 2) Macula densa ... "
        "A) The plaque facing the glomerular tuft B) Efferent arteriole",
        ["1-B, 2-A", "1-A, 2-B", "Both label arterioles", "Both are part of the proximal tubule"], 0,
        "EA = efferent arteriole; the macula densa plaque faces the glomerular tuft at the vascular "
        "pole. (Book p731)"),
    keep("MED-C5-031"),
    new(SEC_MES, 731, "recall",
        "The right-hand figure on this page is captioned:",
        ["Juxtaglomerular apparatus", "Glomerular capillary", "Light microscope image", "Vascularity of nephron"], 0,
        "Caption as printed: 'Juxtaglomerular apparatus'. (Book p731)"),
    # ---- p732: slit diaphragm / filtration slits text ----
    keep("MED-C5-032",
         exp="Slit diaphragm/filtration slits: space btw 2 podocytes (the digit is a script '2', "
             "confirmed at 16x zoom; background OCR misread it as 'a'). (Book p732)"),
    keep("MED-C5-033"),
    keep("MED-C5-034"),
    keep("MED-C5-035",
         opts=["1-B, 2-A", "1-A, 2-B", "Both compartments hold podocin", "Both compartments hold 'α actin 4'"],
         exp="Proteins: inside = 'alpha actin 4' exactly as printed (standard nomenclature is "
             "alpha-actinin-4; flagged, not silently corrected); surface = podocin and TRPC6. (Book p732)"),
    keep("MED-C5-036"),
    new(SEC_SD, 732, "recall",
        "The function of the slit diaphragm / filtration slits is given as:",
        ["Filtration", "Prevention of protein leak", "Anchoring podocytes to the GBM", "Mesangial contraction"], 0,
        "Function: filtration (preventing protein leak is the separately listed role of nephrins; "
        "anchoring is the job of podocyte foot processes). (Book p732)"),
    keep("MED-C5-037"),
    # ---- p732: figure panel (a) labels top-to-bottom ----
    new(SEC_FIG732, 732, "match",
        "Match each label in figure (a) with what its leader marks — "
        "1) Macula densa 2) Distal convoluted tubule 3) Afferent arteriole ... "
        "A) Vessel entering the tuft at the vascular pole B) Specialized plaque at the vascular pole "
        "C) Tubule section drawn beside the plaque at the top",
        ["1-B, 2-C, 3-A", "1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"], 0,
        "Macula densa → the specialized plaque at the vascular pole; distal convoluted tubule → the "
        "tubule section drawn beside it; afferent arteriole → the vessel entering the tuft. (Book p732)"),
    new(SEC_FIG732, 732, "match",
        "Match each label in figure (a) with what its leader marks — "
        "1) Efferent arteriole 2) Bowman's capsule 3) Mesangium ... "
        "A) Cup surrounding the tuft B) Vessel leaving the tuft C) Central tissue between capillary loops",
        ["1-B, 2-A, 3-C", "1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"], 0,
        "Efferent arteriole → the vessel leaving the tuft; Bowman's capsule → the cup surrounding the "
        "tuft; mesangium → the central tissue between capillary loops. (Book p732)"),
    new(SEC_FIG732, 732, "match",
        "Match each label in figure (a) with what its leader marks — "
        "1) Podocyte 2) Capillary 3) Fenestrated endothelium ... "
        "A) Inner lining of the capillary profile B) Cells draped over the capillaries C) The capillary profiles inside the tuft",
        ["1-B, 2-C, 3-A", "1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"], 0,
        "Podocyte → the cells draped over the capillaries; capillary → the capillary profiles inside "
        "the tuft; fenestrated endothelium → the inner lining of each profile. (Book p732)"),
    new(SEC_FIG732, 732, "match",
        "Match the remaining labels in figure (a) — 1) Glomerular basement membrane 2) Proximal tubule (labelled twice) ... "
        "A) Tubule drawn at the bottom, labelled on both sides B) Membrane beneath the podocyte and endothelium",
        ["1-B, 2-A", "1-A, 2-B", "Both label Bowman's capsule", "Both label the same capillary wall layer"], 0,
        "Glomerular basement membrane → the membrane beneath the podocyte/endothelium; proximal tubule "
        "→ the tubule drawn at the bottom (the label is printed twice, on both sides). (Book p732)"),
    # ---- p732: figure panel (b) labels top-to-bottom ----
    new(SEC_FIG732, 732, "match",
        "Match each label in figure (b) with what it marks — "
        "1) F-actin 2) Slit diaphragm 3) Podocyte foot process ... "
        "A) The two foot processes facing across the slit B) Cytoskeletal core inside the foot process "
        "C) The bridge spanning the filtration slit",
        ["1-B, 2-C, 3-A", "1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"], 0,
        "F-actin → the cytoskeletal core inside the foot process; slit diaphragm → the bridge spanning "
        "the filtration slit; podocyte foot process → the pair of processes facing across it. (Book p732)"),
    new(SEC_FIG732, 732, "recall",
        "In figure (b), the transmembrane proteoglycan pair labelled with beta and alpha subunits at the foot-process base is:",
        ["Beta/alpha dystroglycan", "Alpha3beta1 integrin", "Nephrin-NEPH1 pair", "Podocin-TRPC6 pair"], 0,
        "Figure (b) labels 'beta / alpha dystro-glycan' at both foot-process bases (the agrin labels "
        "below read 'Agrin' on the left but print 'Argin' on the right — a figure misspelling, flagged "
        "not corrected). (Book p732)"),
    keep("MED-C5-038",
         opts=["11", "1", "5", "332"],
         exp="Figure (b): alpha3beta1 integrin with Laminin-11 links the podocyte foot process to the "
             "glomerular basement membrane. 'Laminin-11' is the printed figure label (standard laminin "
             "nomenclature uses names like laminin-521/111) — taught as printed. (Book p732)"),
    new(SEC_FIG732, 732, "match",
        "Match the remaining labels in figure (b) — 1) 'Argin' (right label) 2) GEC 3) Glomerular basement membrane ... "
        "A) The endothelial cells drawn at the diagram base B) The membrane on which the foot processes rest "
        "C) The heparan-sulfate proteoglycan printed with a misspelled name",
        ["1-C, 2-A, 3-B", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"], 0,
        "'Argin' (right; the left label spells 'Agrin') → the agrin proteoglycan of the GBM; "
        "GEC → the glomerular endothelial cells drawn at the base; glomerular basement membrane → the "
        "membrane on which the foot processes rest (labelled at the diagram base). (Book p732)"),
    # ---- p732: protein legend (column by column), consolidation, shared caption ----
    new(SEC_FIG732, 732, "match",
        "Match each group of slit-diaphragm legend proteins with its legend column — "
        "1) Nephrin, NEPH1, CD2AP, ZO-1, Podocin 2) Fat-1, NCK, ACTN4, ILK 3) CD151, TRPC6, Podocalyxin, Synaptopodin ... "
        "A) Column 2 B) Column 3 C) Column 1",
        ["1-C, 2-A, 3-B", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"], 0,
        "Legend reads column by column: column 1 = nephrin, NEPH1, CD2AP, ZO-1, podocin; column 2 = "
        "Fat-1, NCK, ACTN4, ILK; column 3 = CD151, TRPC6, podocalyxin, synaptopodin (names as printed). (Book p732)"),
    new(SEC_FIG732, 732, "oddoneout",
        "All of the following appear in the figure's protein legend EXCEPT:",
        ["Laminin-11", "Synaptopodin", "ACTN4", "Podocalyxin"], 0,
        "Laminin-11 is a diagram label, not a legend entry; synaptopodin, ACTN4 and podocalyxin are "
        "legend entries. (Book p732)"),
    new(SEC_FIG732, 732, "recall",
        "The two panels on this page share the single caption:",
        ["Slit diaphragm podocytes", "Glomerular capillary", "Juxtaglomerular apparatus", "Filtration barrier"], 0,
        "Shared caption as printed: 'Slit diaphragm podocytes'. (Book p732)"),
    # ---- p732: angiotensin-podocyte chain, then the Rx line ----
    keep("MED-C5-039"),
    keep("MED-C5-040"),
    new(SEC_ANG, 732, "scenario",
        "A patient with steroid-resistant nephrotic syndrome is found to have podocytes in the urine. "
        "In the book's angiotensin-podocyte chain, podocyturia is the stage immediately after:",
        ["Podocyte detached", "Podocytopenia", "Synechiae formation", "Downregulation of nephrin"], 0,
        "Chain: loss of podocyte integrity (podocytopathies) → podocyte detached → podocyturia → "
        "podocytopenia → GBM attaches to parietal epithelial cells. (Book p732)"),
    keep("MED-C5-042"),
    keep("MED-C5-043"),
    keep("MED-C5-041",
         exp="Full chain: angiotensin binds the podocyte angiotensin II binding receptor → "
             "downregulation of nephrin → loss of podocyte integrity (podocytopathies) → podocyte "
             "detached → podocyturia → podocytopenia → GBM attaches to parietal epithelial cells → "
             "synechiae formation → glomerulosclerosis → CKD. (Book p732)"),
    keep("MED-C5-044",
         exp="ARBs /ACEI(-)'s used in Rx of diabetic nephropathy to block Angiotensin II Receptor, as "
             "printed. Source simplification flagged: ARBs block the angiotensin II receptor while ACE "
             "inhibitors reduce angiotensin II formation. (Book p732)"),
    # ---- p733: congenital nephrotic syndrome ----
    keep("MED-C5-045",
         exp="Congenital nephrotic syndrome: DMS = diffuse mesangial Sclerosis (capital S printed mid-line). (Book p733)"),
    # row 1: Finnish type (cells left to right)
    new(SEC_CNS, 733, "match",
        "Match each cell of the Finnish-type nephrotic-syndrome row — 1) Inheritance 2) Defect 3) Age ... "
        "A) Birth B) AR C) Nephrin : NPHS1",
        ["1-B, 2-C, 3-A", "1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-B, 3-A"], 0,
        "Finnish-type row: inheritance AR; defect nephrin (printed 'Nephrin : NPHS1' with a subscript 1); "
        "age — birth. (Book p733)"),
    keep("MED-C5-047"),
    new(SEC_CNS, 733, "truefalse",
        "Which of the following statements about the Finnish-type row is TRUE?",
        ["Histology ≡ DMS with the management cell a dash",
         "Histology ≡ FSGS with renal transplant listed",
         "The outcome is 100% steroid resistance",
         "The defect is podocin"], 0,
        "Finnish-type row: histology ≡ DMS (printed with the equivalence sign) and the management "
        "cell is a bare dash (nothing listed). (Book p733)"),
    # row 2: podocin type
    new(SEC_CNS, 733, "match",
        "Match each cell of the podocin-type row — 1) Inheritance 2) Defect 3) Age ... "
        "A) 3-5 years B) Podocin C) AR",
        ["1-C, 2-B, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B", "1-B, 2-C, 3-A"], 0,
        "Podocin-type row: inheritance AR; defect podocin; age — 3-5 years. (Book p733)"),
    new(SEC_CNS, 733, "fillup",
        "Fill up: The outcome of the podocin type is 100% steroid resistance progressing to ______.",
        ["CKD", "DMS", "Full remission", "mCD"], 0,
        "Podocin-type outcome cell: '100% Steroid resistance → CKD'. (Book p733)"),
    new(SEC_CNS, 733, "scenario",
        "A 4-year-old has nephrotic syndrome with 100% steroid resistance and FSGS-equivalent histology. "
        "The table's listed management is:",
        ["Renal transplant", "Steroid taper only", "Cyclophosphamide pulses", "No treatment listed"], 0,
        "Podocin-type row: histology ≡ FSGS, management = renal transplant (the autosomal "
        "dominant type repeats these cells). (Book p733)"),
    # row 3: autosomal dominant type
    new(SEC_CNS, 733, "match",
        "Match each cell of the autosomal dominant-type row — 1) Inheritance 2) Defect 3) Age ... "
        "A) Adolescence B) alpha actinin 4/TRPC6 C) AD",
        ["1-C, 2-B, 3-A", "1-A, 2-B, 3-C", "1-C, 2-A, 3-B", "1-B, 2-C, 3-A"], 0,
        "Autosomal dominant-type row: inheritance AD; defect 'alpha actinin 4/TRPC6' as printed (TRPC6 "
        "with a subscript 6); age — adolescence. (Book p733)"),
    new(SEC_CNS, 733, "truefalse",
        "Which of the following statements about the autosomal dominant-type row is TRUE?",
        ["Its outcome, histology and management match the podocin type",
         "Its outcome is 100% mortality",
         "Its histology is ≡ DMS",
         "It is inherited as AR"], 0,
        "The AD-type outcome/histology/management cells repeat the podocin-type cells: 100% steroid "
        "resistance → CKD, ≡ FSGS, renal transplant. (Book p733)"),
    # cross-row consolidations, after all rows
    keep("MED-C5-046"),
    keep("MED-C5-051",
         q="Which of the following statements about the congenital nephrotic syndrome table is TRUE?",
         opts=["The Finnish type is the only type with 100% mortality",
               "All three types are inherited as AR",
               "The podocin type presents at birth",
               "The autosomal dominant type has histology ≡ DMS"],
         exp="Only the Finnish-type row lists 100% mortality; the AD type is AD (not AR); the podocin "
             "type presents at 3-5 years; the AD type is ≡ FSGS. (Book p733)"),
    # post-table line and note
    keep("MED-C5-049"),
    keep("MED-C5-050",
         exp="Note as printed: DMS also seen in 'Denys Drash Syndrome' (no hyphen in the print). (Book p733)"),
    # ---- p733: site-disease table (columns left to right, then consolidations) ----
    keep("MED-C5-052"),
    keep("MED-C5-053"),
    keep("MED-C5-054",
         opts=["mCD", "FSGS", "Membranous nephropathy", "Diabetes"],
         exp="Without podocytopenia: mCD (printed with a lowercase m). (Book p733)"),
    keep("MED-C5-055"),
    keep("MED-C5-056"),
]

assert len(seq) == 88, len(seq)

questions = []
for i, q in enumerate(seq, 1):
    q["id"] = f"MED-C5-{i:03d}"
    questions.append(q)

unit_specs = [
    ("MED-U5-1", "Filtration barrier: capillary endothelium", "Parts of Filtration Barrier · p730",
     "The fenestration-slits bullets (50-100 nm, podocalyxin coating, antiproteinuric function) and the "
     "capillary-endothelium disease PSGN with its expansion and four findings.", 1, 6),
    ("MED-U5-2", "CKD pathophysiology, passage factors & the capillary figure", "Parts of Filtration Barrier · p730",
     "The complete CKD chain to tubulo-interstitial fibrosis, the size and charge passage rules with their "
     "printed units, and every label plus the caption of the glomerular-capillary figure.", 7, 19),
    ("MED-U5-3", "GBM: type-4 collagen, Alport & thickness", "Glomerular Basement Membrane · p731",
     "Type-4 collagen configurations and the Alport defect table, heparin sulfate charge, both GBM "
     "visualisation branches, and the normal/thin thickness values.", 20, 29),
    ("MED-U5-4", "Mesangial cells & the microscopy figures", "Mesangial cells & microscopy figures · p731",
     "The mesangial-cell note (constituent, violent-contraction branches, proliferative definition, IgA "
     "prototype) and every legend, label and caption of both bottom figures.", 30, 45),
    ("MED-U5-5", "Podocytes, the slit diaphragm & the figure panel", "Slit Diaphragm / Filtration Slits · p732",
     "The slit definition and all podocyte bullets including printed protein names, the nephrin roles, "
     "and every label of panels (a) and (b) with the 13-name legend and shared caption.", 46, 63),
    ("MED-U5-6", "Angiotensin-podocyte chain & its Rx", "Angiotensin-podocyte chain & Rx · p732",
     "The full angiotensin-to-CKD chain in printed order (nephrin downregulation to glomerulosclerosis) "
     "and the ARB/ACE-inhibitor line for diabetic nephropathy.", 64, 70),
    ("MED-U5-7", "Congenital nephrotic syndromes", "Congenital Nephrotic Syndrome · p733",
     "The DMS line and the full congenital-NS table read row by row (Finnish, podocin, autosomal "
     "dominant), the premature/large-placenta line and the Denys Drash note.", 71, 83),
    ("MED-U5-8", "Site-disease table", "Site-disease table · p733",
     "The site-disease table read row by row (endothelium, GBM, mesangium, podocyte with and without "
     "podocytopenia) with pairwise consolidations.", 84, 88),
]

units = []
for uid, title, sec, guide, a, b in unit_specs:
    units.append({"id": uid, "ch": 5, "n": int(uid.rsplit("-", 1)[1]), "title": title,
                  "sec": sec, "guide": REVISION + guide,
                  "qs": [f"MED-C5-{i:03d}" for i in range(a, b + 1)]})

out = {"chapter": 5, "title": "Glomerulus - Anatomy", "pageRange": "730-733",
       "questions": questions, "units": units}
(ROOT / "data" / "ch05.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")

# Sanity: pages non-decreasing, citations match, 4 distinct options.
pages = [q["page"] for q in questions]
assert all(b >= a for a, b in zip(pages, pages[1:])), "page order"
import re
for q in questions:
    m = re.search(r"\(Book p(\d+)\)$", q["exp"])
    assert m and int(m.group(1)) == q["page"], q["id"]
    assert len(q["opts"]) == 4 and len({o.strip().casefold() for o in q["opts"]}) == 4, q["id"]
print(f"ch05: {len(questions)} questions, {len(units)} units")
