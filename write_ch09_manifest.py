#!/usr/bin/env python3
"""Record the Ch 9 strict source-review manifest (run AFTER author_c9_review.py).
Checklist built by reading Part 1 PDF pp61-63 (Book p753-755) top-to-bottom at 2x.
Serialises the recorded review only; never invents coverage."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from check_source_coverage import content_digest

ROOT = Path(__file__).resolve().parent
PDF = "uploads/Medicine_Vol3_Part1_pages_705-759.pdf"


def Q(*ns):
    return [f"MED-C9-{n:03d}" for n in ns]


def el(page, index, source, ids):
    return {"element": f"p{page}-e{index:03d}", "page": page, "source": source, "questionIds": ids}


pages = [
    {"page": 753, "pdfPage": 61,
     "traversal": ("Title; Causes list: HUS; HELLP (expansion); rheumatological bracket catastrophic APS / diffuse scleroderma (anti RNA P) "
                   "-> smaller vessels v/s larger vessels (Takayasu, PAN); malignant hypertension = accelerated HTN + papilloedema (fundal "
                   "changes bracket, emergency HTN >=180/120); 'Hemolytic Uremic Syndrome' FEATURES triangle; Note TTP pentagon; TYPES table rows."),
     "elements": [
         el(753, 1, "Causes: HUS; HELLP syndrome (hemolysis, elevated liver enzyme, low platelet).", Q(1, 2)),
         el(753, 2, "Rheumatological condition: catastrophic APS; diffuse scleroderma (anti RNA P) - smaller vessels v/s larger vessels (Takayasu, PAN).", Q(3, 4, 5)),
         el(753, 3, "Malignant hypertension = accelerated HTN + papilloedema (new onset fundal changes: hemorrhage/exudate + emergency HTN: end organ damage + >=180/120).", Q(6, 7, 8)),
         el(753, 4, "FEATURES triad: thrombocytopenia, renal failure, MAHA.", Q(9, 10)),
         el(753, 5, "Note TTP pentagon: thrombocytopenia, fever, MAHA, neurological symptoms [Brain], GI symptoms.", Q(11, 12, 13, 14)),
         el(753, 6, "TYPES onset: childhood commonly <5 years / any age; cause: infection i.e dysentery / genetic (m/c), sporadic (drug induced).", Q(15, 16)),
         el(753, 7, "Prognosis: good / bad (50% progress to ESRD), up chances of recurrence after renal transplant.", Q(17, 18)),
     ]},
    {"page": 754, "pdfPage": 62,
     "traversal": ("PATHOPHYSIOLOGY chain; Causes: typical/childhood toxins (90% cases) three toxins; atypical/adult genetic (m/c) cause, A/w, "
                   "types factor H (m/c), B worst, MCP best, factor I; sporadic drug induced list (TTP also bracket); immune mediated HUS list; "
                   "INVESTIGATION smear, blood investigation; Note table atypical HUS vs SLE."),
     "elements": [
         el(754, 1, "Endothelial damage -> VWF release -> platelet plug formation; platelet trapped in plug -> thrombocytopenia.", Q(19, 20, 21)),
         el(754, 2, "Schistocyte formation (d/t platelet plug circulating erythrocytes damage) -> MAHA.", Q(22)),
         el(754, 3, "Typical/childhood toxins 90% cases: Shiga like toxin/verocytotoxin EHEC O157:H7 (m/c); Shiga toxin Shigella dysentery; neuraminidase toxin Streptococcus pneumonia.", Q(23, 24, 25)),
         el(754, 4, "Genetic (m/c): alternate complement pathway activation; A/w low C3, normal C4.", Q(26)),
         el(754, 5, "Types: complement factor-H (m/c) mutation; factor-B worst prognosis; MCP best prognosis; factor-I.", Q(27)),
         el(754, 6, "Sporadic drug induced: mitomycin, gemcitabine, bevacizumab, calcineurin inhibitors (tacrolimus, cyclosporine), ticlopidine/clopidogrel (TTP also), cisplatin.", Q(28, 29, 30)),
         el(754, 7, "Immune mediated HUS: quinine, gemcitabine, quetiapine, cotrimoxazole.", Q(31, 32)),
         el(754, 8, "INVESTIGATION: peripheral blood smear - schistocyte (>2% significant).", Q(33)),
         el(754, 9, "Blood investigation: up LDH, -ve Coombs, up indirect bilirubin, down haptoglobin, normal PT/APTT.", Q(34, 35)),
         el(754, 10, "Note: atypical HUS alternative pathway, low C3 (N) C4; SLE classical, low C3 low C4.", Q(36)),
     ]},
    {"page": 755, "pdfPage": 63,
     "traversal": ("PRESENTATION AND TREATMENT: typical HUS timeline (abdominal pain -2 days-> bloody dysentery (evaluate & start antibiotics) "
                   "-5 days-> 90-95% resolution / 5-10% HUS; treatment conservative); atypical HUS two features; treatment list; Note table "
                   "pre renal injury vs acute tubular necrosis, five rows."),
     "elements": [
         el(755, 1, "Typical HUS: abdominal pain -> 2 days -> bloody dysentery (evaluate & start antibiotics) -> 5 days -> 90-95% resolution / 5-10% HUS.", Q(37, 38, 39, 40)),
         el(755, 2, "Treatment: conservative.", Q(41)),
         el(755, 3, "Atypical HUS: features of 2 degree HTN (renal/endocrine); thrombocytopenia.", Q(42)),
         el(755, 4, "PLEX: within 24 hr; mainstay of treatment.", Q(43)),
         el(755, 5, "Eculizumab: costly; immunosuppressant: in complement factor H mutation; renal transplant.", Q(44, 45)),
         el(755, 6, "Recurrence post transplant: rituximab; eculizumab.", Q(46, 47)),
         el(755, 7, "Note table rows: urine output normal/decreased; edema -/+; BUN/creatinine >20:1 / <10:1; fluids given/withhold; tubular injury -/+.", Q(48, 49, 50, 51, 52)),
     ]},
]

chapter = json.loads((ROOT / "data" / "ch09.json").read_text())
ids = [q["id"] for q in chapter["questions"]]
assert [i for p in pages for e in p["elements"] for i in e["questionIds"]] == ids

manifest = {
    "chapter": 9, "reviewedAt": "2026-09-22", "status": "reviewed-with-source-caveats",
    "pdf": PDF, "pdfSha256": hashlib.sha256((ROOT / PDF).read_bytes()).hexdigest(), "pdfOffset": 692,
    "pageRange": "753-755", "contentSha256": content_digest(chapter),
    "method": ("All three printed pages read from the supplied Part 1 PDF at 2x, top-to-bottom, tables row by row. Every stored answer "
               "index checked against the print: 51/52 correct; one match item had a mis-built option (ATN BUN/creatinine offered as "
               "> 20:1) and was corrected to the printed < 10:1. Questions re-sequenced to the traversal."),
    "caveats": [
        "p753: prints 'Papilloedema' and 'Anti RNA P' (anti-RNA polymerase); TTP is presented as a five-cornered figure labelled only in the Note.",
        "p754: prints 'Streptococcus pneumonia', 'Worst progosis', 'Ecoli'; taught with standard spelling in stems.",
        "p755: 'Withhold' printed for ATN fluids; the note table is a general pre-renal vs ATN aide placed at the chapter end.",
        "Blood-smear photograph tested only via its printed legend.",
    ],
    "pages": pages,
}
out = ROOT / "data" / "source_review" / "ch09.json"
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"wrote {out} ({sum(len(p['elements']) for p in pages)} elements)")
