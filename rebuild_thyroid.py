import json
from pathlib import Path

ROOT = Path("/home/user/Medicine")

# ==============================================================================
# CHAPTER 41: Thyroid Function Tests (p902–904)
# ==============================================================================

c41_order = ["p902a", "p903a", "p904a"]

c41_units = [
    {
        "title": "Hormone Levels, Hyperthyroxinemia & Resistance to Thyroid Hormone",
        "sec": "Thyroid Hormone Levels, Disorders & RTH · p902",
        "guide": "Cover circulating T4:T3 ratio, binding proteins (TBG, albumin, transthyretin), thyrotoxicosis vs euthyroid hyperthyroxinemia, causes of TBG excess, RTH pathogenesis and TR-β resistance, and MCT8 neuronal transporter defect (Allan-Herndon-Dudley syndrome).",
        "parts": ["p902a"]
    },
    {
        "title": "Thyroid Hormone Functions, Metabolic Actions & Scintigraphy",
        "sec": "Thyroid Scintigraphy & Metabolic Actions · p903",
        "guide": "Cover Tc-99m ectopic thyroid scintigraphy, BMR regulation, cardiac actions, thermogenesis via uncoupling of oxidative phosphorylation, carbohydrate/fat/protein metabolism, CNS myelination, beta-carotene conversion, and fertility maintenance.",
        "parts": ["p903a"]
    },
    {
        "title": "Drugs Affecting TFT, Testing & Lab Interpretations",
        "sec": "Drugs & TFT, Reference Ranges & Interpretations · p904",
        "guide": "Learn deiodinase inhibitors, enzyme inducers, drugs causing hypothyroidism or impairing absorption, 4th-gen CLIA TSH reference range (0.5-5 mIU/L), the 7-pattern TFT interpretation grid, and thyroglobulin as a marker for factitious thyrotoxicosis.",
        "parts": ["p904a"]
    }
]

p902a = {
    "page": 902,
    "sec": "Thyroid Hormone Levels, Disorders & RTH",
    "items": [
        {
            "fmt": "fillup",
            "q": "In circulating blood, thyroid hormone levels show that T4 is present in maximum concentration, approximately ___ that of T3.",
            "opts": [
                "10-fold (10 x T3)",
                "2-fold (2 x T3)",
                "50-fold (50 x T3)",
                "100-fold (100 x T3)"
            ],
            "ans": 0,
            "exp": "Circulating T4 is present in maximum concentration, approximately 10 times that of T3 (10 x T3). (Book p902)"
        },
        {
            "fmt": "match",
            "q": "Match the thyroid hormone carrier proteins to their respective binding percentages — 1) Thyroid Binding Globulin (TBG) 2) Albumin 3) Transthyretin … A) 70% B) 20% C) 10%",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Thyroid hormone carrier proteins bind circulating hormone in the proportions: TBG 70%, Albumin 20%, and Transthyretin 10%. (Book p902)"
        },
        {
            "fmt": "recall",
            "q": "In the opening classification of hyperthyroxinemia (elevated T3 and T4 levels), what biochemical finding defines thyrotoxicosis rather than euthyroid hyperthyroxinemia?",
            "opts": [
                "Elevated free T3 and free T4 levels",
                "Elevated total T3 and total T4 levels with normal free hormone",
                "Isolated elevated thyroglobulin with normal TSH",
                "Elevated thyroid binding globulin (TBG) levels"
            ],
            "ans": 0,
            "exp": "Hyperthyroxinemia branches into thyrotoxicosis (defined by elevated free T3/free T4) and euthyroid hyperthyroxinemia (elevated total T3/total T4). (Book p902)"
        },
        {
            "fmt": "match",
            "q": "Under thyrotoxicosis with elevated free hormone levels, match the gland status to its underlying mechanism — 1) Overworking gland 2) Normal gland … A) Hyperthyroidism B) Stored hormones released / Hormone supplement",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "In thyrotoxicosis, an overworking gland corresponds to true hyperthyroidism, whereas a normal gland releases stored hormones (thyroiditis) or receives exogenous hormone supplementation. (Book p902)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess these causes of euthyroid hyperthyroxinemia (elevated total T3 and total T4): I TBG excess. II Drugs that inhibit deiodinase-2 (D1-2), Sick euthyroid syndrome, and RTH.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Causes of euthyroid hyperthyroxinemia listed on page 902 include: 1) TBG excess, 2) Drugs that inhibit deiodinase-2, 3) Sick euthyroid syndrome, and 4) RTH. (Book p902)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed on page 902 as a cause of TBG excess?",
            "opts": [
                "Nephrotic syndrome",
                "Oral contraceptive pills (OCPs) and estrogen",
                "Pregnancy and steroids",
                "Chronic active hepatitis and inherited TBG excess (rare)"
            ],
            "ans": 0,
            "exp": "Causes of TBG excess on page 902 are OCPs, estrogen, pregnancy, steroids, chronic active hepatitis, and inherited TBG excess (rare). Nephrotic syndrome causes urinary protein loss and low TBG. (Book p902)"
        },
        {
            "fmt": "scenario",
            "q": "A 24-year-old woman taking oral contraceptive pills has high total T4 and total T3 on routine screening. Free T4, free T3, and TSH are normal. What is the diagnosis?",
            "opts": [
                "Euthyroid hyperthyroxinemia due to TBG excess",
                "Primary thyrotoxicosis from an overworking gland",
                "Resistance to thyroid hormone (RTH)",
                "Subclinical hyperthyroidism"
            ],
            "ans": 0,
            "exp": "OCPs raise TBG levels, leading to elevated total T3/T4 with normal free hormone levels, classified as euthyroid hyperthyroxinemia. (Book p902)"
        },
        {
            "fmt": "recall",
            "q": "What is the primary pathogenesis of Resistance to Thyroid Hormone (RTH)?",
            "opts": [
                "Partial or complete resistance of T3/T4 receptors leading to uninhibited increase of TSH with high T3/T4 but no action",
                "Activating mutation in the TSH receptor causing autonomous thyroid follicle hyperplasia",
                "Deiodinase-2 deficiency in the liver preventing peripheral hormone degradation",
                "Circulating autoantibodies that block thyroid binding globulin clearance"
            ],
            "ans": 0,
            "exp": "In RTH, partial or completely resistant T3/T4 receptors cause uninhibited increase of TSH, producing high T3 and T4 that fail to exert downstream action. (Book p902)"
        },
        {
            "fmt": "match",
            "q": "Match the clinical presentation of Resistance to Thyroid Hormone (RTH) to its relative frequency — 1) Euthyroid state 2) Toxicosis … A) Most common (m/c) B) Rare (due to resistance to TR-β forms)",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Clinically in RTH, patients are most commonly euthyroid; toxicosis is rare and occurs due to resistance to beta forms (TR-β). (Book p902)"
        },
        {
            "fmt": "fillup",
            "q": "In Resistance to Thyroid Hormone (RTH), the rare occurrence of toxicosis is due to resistance specifically involving ___ forms of the receptor.",
            "opts": [
                "TR-β (thyroid hormone receptor beta)",
                "TR-α1 (thyroid hormone receptor alpha 1)",
                "G-protein coupled TSH receptor",
                "OATP1C1 neuronal transporter"
            ],
            "ans": 0,
            "exp": "Toxicosis in RTH is rare and develops due to selective resistance to beta forms (TR-β). (Book p902)"
        },
        {
            "fmt": "scenario",
            "q": "A male infant presents with severe cognitive impairment and hypotonia. Molecular genetic testing identifies a loss-of-function defect in the neuronal MCT8 transporter. What is the diagnosis?",
            "opts": [
                "Allan-Herndon-Dudley syndrome",
                "Pendred syndrome",
                "Hoffman syndrome",
                "De Quervain syndrome"
            ],
            "ans": 0,
            "exp": "MCT8 defect causes impaired entry of T3 into neurons, producing Allan-Herndon-Dudley syndrome characterized by severe cognitive impairment. (Book p902)"
        },
        {
            "fmt": "truefalse",
            "q": "In the CNS thyroid hormone transport pathway: I T4 crosses the blood-brain barrier via OATP1C1 and MCT8 into astrocytes, where D2 converts it to T3. II T3 enters neurons via MCT8 to activate T3-responsive genes.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "T4 crosses the blood-brain barrier via OATP1C1/MCT8 into astrocytes where deiodinase-2 (D2) converts T4 to T3; T3 then enters neurons via MCT8 to regulate T3-responsive genes. (Book p902)"
        },
        {
            "fmt": "recall",
            "q": "Which transporter protein is shown alongside MCT8 at the blood-brain barrier for thyroid hormone transport into astrocytes on page 902?",
            "opts": [
                "OATP1C1",
                "Pendrin",
                "SGLT-2",
                "GLUT-4"
            ],
            "ans": 0,
            "exp": "The blood-brain barrier diagram depicts OATP1C1 and MCT8 facilitating thyroid hormone transport into astrocytes. (Book p902)"
        }
    ]
}

p903a = {
    "page": 903,
    "sec": "Thyroid Scintigraphy & Metabolic Actions",
    "items": [
        {
            "fmt": "scenario",
            "q": "A patient with a midline neck swelling undergoes Technetium-99m (Tc^99m) scintigraphy. The scan demonstrates no uptake in the normal anatomical location and prominent uptake in an abnormal subhyoid region. What is the diagnosis?",
            "opts": [
                "Ectopic thyroid tissue",
                "Toxic adenoma of the left lobe",
                "Acute suppurative thyroiditis",
                "Graves disease with cold nodule"
            ],
            "ans": 0,
            "exp": "The scintigraphy image on page 903 shows a Tc-99m scan of ectopic thyroid, with 'No uptake in normal location' and 'Uptake in ectopic location'. (Book p903)"
        },
        {
            "fmt": "match",
            "q": "Match the thyroid disorder to its effect on the Basal Metabolic Rate (BMR) — 1) Hypothyroidism 2) Hyperthyroidism … A) Decreased (↓) BMR B) Increased (↑) BMR",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Thyroid hormone maintains BMR: hypothyroidism leads to decreased BMR, whereas hyperthyroidism causes increased BMR. (Book p903)"
        },
        {
            "fmt": "recall",
            "q": "Which receptor family is explicitly listed under 'Cardiac actions' of thyroid hormone on page 903?",
            "opts": [
                "α-receptors",
                "β-2 receptors only",
                "Nicotinic acetylcholine receptors",
                "Dopaminergic D1 receptors"
            ],
            "ans": 0,
            "exp": "Page 903 explicitly notes: 'Cardiac actions (α-receptors): ↑ Cardiac output (CO), ↑ O2 utilization, ↑ heart rate'. (Book p903)"
        },
        {
            "fmt": "fillup",
            "q": "Thyroid hormone stimulates tissue oxygen (O2) utilization throughout the body, with the explicit exception of the ___ and ___.",
            "opts": [
                "Brain and gonads",
                "Heart and lungs",
                "Liver and skeletal muscle",
                "Kidneys and spleen"
            ],
            "ans": 0,
            "exp": "Thyroid hormone causes increased O2 utilization '(Except brain & gonads)'. (Book p903)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding the vascular and hemodynamic effects on page 903: I Toxicosis leads directly to increased cardiac output (CO). II Hyperthyroidism increases peripheral resistance, leading to increased blood pressure (BP).",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Page 903 notes: 'Toxicosis -> ↑ CO' and 'Hyperthyroidism -> ↑ peripheral resistance -> ↑ BP'. (Book p903)"
        },
        {
            "fmt": "fillup",
            "q": "Thyroid hormone drives thermogenesis by acting as an uncoupler of ___; a severe deficiency in myxedema coma causes ___.",
            "opts": [
                "Oxidative phosphorylation; hypothermia",
                "Glycolytic phosphorylation; hyperthermia",
                "The citric acid cycle; heat stroke",
                "Beta-oxidation; ketoacidosis"
            ],
            "ans": 0,
            "exp": "Thyroid hormone acts as an uncoupler of oxidative phosphorylation producing thermogenesis; its lack in myxedema coma results in hypothermia. (Book p903)"
        },
        {
            "fmt": "recall",
            "q": "What two key effects of thyroid hormone on carbohydrate metabolism are outlined on page 903?",
            "opts": [
                "Gluconeogenesis stimulation and glucose uptake into cells (with insulin resistance in hypothyroidism)",
                "Glycogen synthesis stimulation and peripheral insulin sensitization",
                "Direct inhibition of hepatic glucokinase and activation of intestinal SGLT-1",
                "Suppression of pancreatic glucagon release and acceleration of glycolysis"
            ],
            "ans": 0,
            "exp": "In carbohydrate metabolism, thyroid hormone drives: 1. Gluconeogenesis, and 2. Glucose uptake into cells (with hypothyroidism predisposing to insulin resistance). (Book p903)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding fat metabolism: I Thyroid hormone causes minimal lipolysis. II Thyroid hormone stimulates cholesterol clearance; therefore, hypothyroidism results in hypercholesterolemia.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Under fat metabolism: 1. Lipolysis (minimal), 2. Cholesterol clearance (Hypothyroidism : Hypercholesterolemia). (Book p903)"
        },
        {
            "fmt": "scenario",
            "q": "A patient with severe long-standing thyrotoxicosis develops proximal muscle wasting, osteopenia with pathological fractures, and hypercalcemia with nephrolithiasis. What catabolic mechanism explains these findings?",
            "opts": [
                "Potent catabolic proteolysis causing myopathy, osteopenia/osteoporosis, and hypercalcemia leading to hypercalciuria and stones",
                "Severe uncoupling of oxidative phosphorylation causing muscular lactic acidosis and stone deposition",
                "Enhanced gluconeogenesis depleting muscle glycogen and causing secondary hyperparathyroidism",
                "Impaired cholesterol clearance inducing osteoclast atheromatous emboli"
            ],
            "ans": 0,
            "exp": "In significant toxicosis, thyroid hormone acts as a potent catabolic hormone driving proteolysis -> myopathy, osteopenia -> osteoporosis, and hypercalcemia -> hypercalciuria -> stones. (Book p903)"
        },
        {
            "fmt": "match",
            "q": "Match the physiological action of thyroid hormone to its target organ — 1) CNS 2) Vitamin metabolism 3) Bone marrow … A) Myelination B) β-Carotene conversion to Vitamin A C) Stimulates erythropoiesis",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Thyroid hormone promotes myelination of the CNS, converts beta-carotene to vitamin A, and stimulates erythropoiesis in bone marrow. (Book p903)"
        },
        {
            "fmt": "recall",
            "q": "Why can hypothyroid patients exhibit yellowish-orange skin discoloration while sparing the sclerae?",
            "opts": [
                "Impaired conversion of β-carotene to Vitamin A leads to carotenemia",
                "Increased hepatic bilirubin glucuronidation failure",
                "Extensive accumulation of glycosaminoglycans in the sclerae",
                "Accelerated breakdown of red blood cells from erythropoietic arrest"
            ],
            "ans": 0,
            "exp": "Thyroid hormone is responsible for converting beta-carotene to vitamin A; in hypothyroidism this conversion is impaired, leading to hypercarotenemia and yellowing of skin. (Book p903)"
        },
        {
            "fmt": "fillup",
            "q": "Thyroid hormone maintains reproductive fertility; the sequential menstrual derangement noted in untreated hypothyroidism is: menorrhagia → ___ → infertility.",
            "opts": [
                "Oligo/amenorrhea",
                "Polymenorrhea",
                "Dysmenorrhea",
                "Continuous metrorrhagia"
            ],
            "ans": 0,
            "exp": "Under fertility maintenance: 'Hypothyroidism -> menorrhagia -> Oligo/amenorrhea -> Infertility'. (Book p903)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed on page 903 as a physiologic function or target of thyroid hormone?",
            "opts": [
                "Inhibition of erythropoiesis in bone marrow",
                "Myelination of the central nervous system",
                "Conversion of β-carotene to vitamin A",
                "Maintenance of basal metabolic rate (BMR)"
            ],
            "ans": 0,
            "exp": "Thyroid hormone stimulates erythropoiesis, not inhibits it. It also maintains BMR, promotes CNS myelination, and converts beta-carotene to vitamin A. (Book p903)"
        }
    ]
}

p904a = {
    "page": 904,
    "sec": "Drugs & TFT, Reference Ranges & Interpretations",
    "items": [
        {
            "fmt": "match",
            "q": "Match the drug categories affecting thyroid function tests — 1) Deiodinase inhibitors 2) Enzyme inducers (↑ hormone metabolism) … A) Steroids, Propranolol, Iodine, Amiodarone, Propylthiouracil B) Phenytoin, Carbamazepine, Rifampicin, Sertraline, Ritonavir",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Deiodinase inhibitors listed are steroids, propranolol, iodine, amiodarone, PTU; enzyme inducers increasing metabolism are phenytoin, carbamazepine, rifampicin, sertraline, ritonavir. (Book p904)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following drugs is NOT listed on page 904 as a deiodinase inhibitor?",
            "opts": [
                "Rifampicin",
                "Steroids",
                "Propranolol",
                "Propylthiouracil"
            ],
            "ans": 0,
            "exp": "Rifampicin is an enzyme inducer that increases hormone metabolism; steroids, propranolol, iodine, amiodarone, and PTU are deiodinase inhibitors. (Book p904)"
        },
        {
            "fmt": "match",
            "q": "Match the drug to its specific effect on thyroid hormone economy — 1) Lithium 2) Al(OH)3, Cholestyramine, Calcium carbonate, Ferrous sulfate … A) Directly causes hypothyroidism B) Decreases thyroid hormone absorption",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Lithium causes hypothyroidism, while aluminum hydroxide, cholestyramine, calcium carbonate, and ferrous sulfate decrease thyroid hormone absorption. (Book p904)"
        },
        {
            "fmt": "numeric",
            "q": "What is the normal reference range for TSH tested by 4th-generation CLIA as specified on page 904?",
            "opts": [
                "0.5 - 5 mIU/L",
                "0.1 - 2.5 mIU/L",
                "2.0 - 10.0 mIU/L",
                "0.01 - 0.5 mIU/L"
            ],
            "ans": 0,
            "exp": "Page 904 states: 'TSH (Thyroid Stimulating Hormone) : 0.5 - 5 mIU/L (by CLIA 4th generation)'. (Book p904)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding thyroid testing rules on page 904: I Clinicians should always look for all three: fT3, fT4, and TSH. II Thyroid function tests should not be checked in critically ill patients.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Under TESTS: 'Always look for all of: fT3, fT4, TSH' and 'Do not check in critically ill patients'. (Book p904)"
        },
        {
            "fmt": "scenario",
            "q": "A patient's laboratory report reveals: TSH elevated (↑), while total T4, free T4, total T3, and free T3 are all normal (N). What is the condition?",
            "opts": [
                "Subclinical 1° hypothyroidism",
                "Primary overt hypothyroidism",
                "Resistance to thyroid hormone (RTH)",
                "Central hypothalamo-pituitary hypothyroidism"
            ],
            "ans": 0,
            "exp": "TSH ↑ with normal T4, FT4, T3, and FT3 represents Subclinical 1° hypothyroidism. (Book p904)"
        },
        {
            "fmt": "recall",
            "q": "In overt primary hypothyroidism (TSH ↑, T4 ↓, FT4 ↓, T3 ↓, FT3 ↓), what is the most common etiology and clinical association noted on page 904?",
            "opts": [
                "Autoimmune etiology, associated with Hashimoto's thyroiditis",
                "Dietary iodine deficiency, associated with endemic goiter",
                "Consumptive hemangioma, associated with deiodinase-3 excess",
                "Pituitary mass lesion, associated with Sheehan syndrome"
            ],
            "ans": 0,
            "exp": "For primary hypothyroidism, page 904 notes: 'm/c : Autoimmune' and 'A/w : Hashimoto\'s thyroiditis'. (Book p904)"
        },
        {
            "fmt": "scenario",
            "q": "A patient's thyroid panel shows elevation of all parameters: TSH ↑, T4 ↑, FT4 ↑, T3 ↑, and FT3 ↑. Clinically, the patient is euthyroid. What is the diagnosis?",
            "opts": [
                "Resistance to thyroid hormone (RTH)",
                "TSH secreting pituitary adenoma",
                "Graves disease thyrotoxicosis",
                "Subacute de Quervain thyroiditis"
            ],
            "ans": 0,
            "exp": "When TSH, T4, FT4, T3, and FT3 are all elevated, the condition is RTH if the patient is euthyroid, or TSH-secreting adenoma if toxic features are present. (Book p904)"
        },
        {
            "fmt": "match",
            "q": "When TSH, T4, FT4, T3, and FT3 are all simultaneously elevated, match the clinical presentation to the diagnosis — 1) Euthyroid state 2) Toxic features present … A) RTH (Resistance to Thyroid Hormone) B) TSH secreting adenoma",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "For elevated TSH + elevated T4/FT4/T3/FT3: RTH presents as euthyroid; TSH secreting adenoma presents with toxic features. (Book p904)"
        },
        {
            "fmt": "truefalse",
            "q": "In hypothalamo-pituitary (secondary) hypothyroidism: I TSH is normal or decreased (N/↓). II T4, FT4, T3, and FT3 are all decreased (↓).",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "In hypothalamo-pituitary hypothyroidism, TSH is normal or low (N/↓) while peripheral hormones T4, FT4, T3, and FT3 are all low (↓). (Book p904)"
        },
        {
            "fmt": "scenario",
            "q": "A patient has TSH ↓, total T4 normal, free T4 ↑, total T3 normal, and free T3 ↑. Which causes does the page 904 interpretation table list for this pattern?",
            "opts": [
                "Overworking gland (Autoimmune Graves) or stored hormone release (Thyroiditis, Hydatidiform mole/pregnancy)",
                "Subclinical hypothyroidism or sick euthyroid syndrome",
                "TSH-secreting pituitary macroadenoma or RTH",
                "Factitious hypothyroidism or severe cirrhosis"
            ],
            "ans": 0,
            "exp": "Under thyrotoxicosis (TSH ↓, T4 N, FT4 ↑, T3 N, FT3 ↑), causes include overworking gland (Autoimmune Graves) and stored hormone release (Thyroiditis, Hydatidiform mole/pregnancy). (Book p904)"
        },
        {
            "fmt": "fillup",
            "q": "Serum thyroglobulin is elevated in all forms of thyrotoxicosis EXCEPT ___, where exogenous hormone suppresses endogenous thyroglobulin release.",
            "opts": [
                "Thyrotoxicosis factitia (hormone supplementation)",
                "Graves disease",
                "Subacute de Quervain thyroiditis",
                "Toxic multinodular goiter"
            ],
            "ans": 0,
            "exp": "Serum thyroglobulin is increased in all thyrotoxicosis except thyrotoxicosis factitia (hormone supplementation). (Book p904)"
        }
    ]
}

# ==============================================================================
# CHAPTER 42: Hypothyroidism (p905–909)
# ==============================================================================

c42_order = ["p905a", "p906a", "p907a", "p908a", "p909a"]

c42_units = [
    {
        "title": "Hypothyroidism Classification & Causes",
        "sec": "Primary, Secondary, Consumptive & Congenital Hypothyroidism · p905",
        "guide": "Master primary causes (Hashimoto, APS-2 check prior to L-thyroxine, drugs including lithium, IFN-α, and amiodarone), secondary causes (lymphocytic hypophysitis mass effect), consumptive hypothyroidism (hemangioma D3 overexpression), and newborn congenital signs.",
        "parts": ["p905a"]
    },
    {
        "title": "Hashimoto's Thyroiditis Features, Pathology & Mediators",
        "sec": "Hashimoto Features, Histology & Associated Malignancy · p906",
        "guide": "Cover demographics (middle-aged females), HLA associations (DR3/DR4/DR5, CTLA-4, PTPN-22), gross and microscopic features (Hürthle cells, lymphoid follicles with germinal centers, absence of colloid), extranodal marginal zone lymphoma risk, and immune mediators (CD8/CD4 T-cells, IFN-γ).",
        "parts": ["p906a"]
    },
    {
        "title": "Clinical Presentation, Signs & Complications of Hypothyroidism",
        "sec": "Symptoms, Signs, GAG Deposition & Complications · p907",
        "guide": "Examine generalized slowing, TSH-stimulated GAG deposition causing myxedema (periorbital edema, macroglossia, OSA), young female symptoms, false-positive Addison's, Hoffman syndrome, polyserositis, and carpal tunnel syndrome.",
        "parts": ["p907a"]
    },
    {
        "title": "Hashimoto Workup, Diagnostic Cut-offs & L-Thyroxine Dosing",
        "sec": "Autoantibodies, Treatment Indications & L-Thyroxine Titration · p908",
        "guide": "Work through autoantibody prevalence (TPO 90-100%, Tg 80-90%, TSH-R 10-20%), subclinical vs overt cut-offs, treatment threshold (TSH > 10 or 5-10 with risks), starting doses (< 60 yrs 1.6-1.8 µg/kg/day vs elderly 25 µg/day), and titration increments.",
        "parts": ["p908a"]
    },
    {
        "title": "L-Thyroxine Administration, Follow-up, Myxedema Coma & SREAT",
        "sec": "Patient Instructions, Myxedema Coma & SREAT / Hashimoto Encephalopathy · p909",
        "guide": "Review morning empty-stomach dosing, drugs to avoid, 3-month review, myxedema coma presentation (hypothermia, low voltage ECG) and IV protocol, and SREAT (euthyroid vasculitis, anti-enolase antibodies, steroid response).",
        "parts": ["p909a"]
    }
]

p905a = {
    "page": 905,
    "sec": "Primary, Secondary, Consumptive & Congenital Hypothyroidism",
    "items": [
        {
            "fmt": "recall",
            "q": "What is the most common (m/c) cause of primary hypothyroidism on page 905?",
            "opts": [
                "Autoimmune hypothyroidism (AKA Hashimoto thyroiditis)",
                "Iatrogenic radioiodine ablation",
                "Severe endemic dietary iodine deficiency",
                "Lithium-induced thyroiditis"
            ],
            "ans": 0,
            "exp": "Under Primary Hypothyroidism: '1. Autoimmune hypothyroidism (m/c) AKA Hashimoto thyroiditis'. (Book p905)"
        },
        {
            "fmt": "fillup",
            "q": "Autoimmune hypothyroidism is associated with Autoimmune Polyendocrine Syndromes (APS); clinicians should specifically check for ___ before initiating treatment.",
            "opts": [
                "APS-2 (Autoimmune polyendocrine syndrome type 2)",
                "APS-1 (Autoimmune polyendocrine syndrome type 1)",
                "Multiple Endocrine Neoplasia type 1 (MEN-1)",
                "Pendred syndrome"
            ],
            "ans": 0,
            "exp": "Autoimmune hypothyroidism is associated with APS-1/2; clinicians 'Should check for APS2 before treatment'. (Book p905)"
        },
        {
            "fmt": "scenario",
            "q": "A patient with undetected coexisting adrenal insufficiency (APS-2) is prescribed L-thyroxine without prior cortisol supplementation. What acute consequence is cautioned on page 905?",
            "opts": [
                "Adrenal insufficiency: shock in children, profound adrenal insufficiency in adults",
                "Sudden thyrotoxic crisis with hyperpyrexia and delirium",
                "Acute hypocalcemic tetany from suppressed parathyroid reserve",
                "Severe hypertensive emergency with encephalopathy"
            ],
            "ans": 0,
            "exp": "If L-thyroxine is given without cortisol supplementation in APS-2, it precipitates adrenal insufficiency: shock in children, and profound adrenal insufficiency in adults. (Book p905)"
        },
        {
            "fmt": "match",
            "q": "Match the pharmacologic agent causing hypothyroidism to its specific clinical characteristic — 1) Lithium 2) Interferon-alpha (IFN-α) 3) Amiodarone … A) Associated with nephrogenic diabetes insipidus (DI) B) Drug-associated thyroid destruction (irreversible side effect) C) Can produce both hypothyroidism and hyperthyroidism",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Lithium causes hypothyroidism and nephrogenic DI; IFN-α causes irreversible thyroid destruction; amiodarone can produce both hypothyroidism and hyperthyroidism. (Book p905)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding side effects of interferon-alpha (IFN-α): I Thyroid destruction is an irreversible side effect. II Flu-like syndrome is a reversible side effect.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Page 905 notes for IFN-α: 'Irreversible S/E: thyroid destruction' and 'Reversible S/E : Flu like syndrome'. (Book p905)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed under causes of primary hypothyroidism on page 905?",
            "opts": [
                "Pituitary mass effect from lymphocytic hypophysitis",
                "Autoimmune Hashimoto thyroiditis",
                "Lithium and interferon-alpha therapy",
                "Iodine deficiency and post-surgical state"
            ],
            "ans": 0,
            "exp": "Pituitary mass effect is a cause of secondary hypothyroidism, not primary hypothyroidism. (Book p905)"
        },
        {
            "fmt": "recall",
            "q": "In secondary hypothyroidism due to a pituitary mass effect, what is the most common (m/c) underlying etiology listed?",
            "opts": [
                "Lymphocytic hypophysitis",
                "Craniopharyngioma",
                "Pituitary apoplexy (Sheehan syndrome)",
                "Infiltrative sarcoidosis"
            ],
            "ans": 0,
            "exp": "Under Secondary Hypothyroidism: 'Pituitary cause : No significant hypothyroidism; Primary Cause - MASS effect - (m/c) Lymphocytic hypophysitis'. (Book p905)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess secondary hypothyroidism from pituitary disease: I It characteristically causes severe, profound isolated hypothyroidism. II Its primary mechanism is mass effect, most commonly from lymphocytic hypophysitis.",
            "opts": [
                "I is false; II is true",
                "Both I and II are true",
                "I is true; II is false",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Page 905 states: 'No significant hypothyroidism' for pituitary cause, and its primary cause is mass effect, most commonly lymphocytic hypophysitis. (Book p905)"
        },
        {
            "fmt": "scenario",
            "q": "A 2-month-old infant with a large hepatic hemangioma develops profound hypothyroidism requiring massive doses of levothyroxine. What is the mechanism of this consumptive hypothyroidism?",
            "opts": [
                "Increased deiodinase-III expression in the hemangioma converting active hormone to reverse T3",
                "Direct destruction of the infant thyroid follicles by hemangioma-derived antibodies",
                "Failure of intestinal absorption of thyroid hormone due to splanchnic steal",
                "Suppression of hypothalamic TRH secretion by circulating angiogenin"
            ],
            "ans": 0,
            "exp": "Consumptive hypothyroidism in hemangioma is driven by increased deiodinase-III expression leading to decreased active hormones and increased reverse T3. (Book p905)"
        },
        {
            "fmt": "fillup",
            "q": "Consumptive hypothyroidism associated with hemangioma is mediated by increased expression of ___, which accelerates the formation of ___.",
            "opts": [
                "Deiodinase-III; reverse T3",
                "Deiodinase-II; active T3",
                "Deiodinase-I; free T4",
                "Thyroid peroxidase; thyroglobulin"
            ],
            "ans": 0,
            "exp": "Hemangioma -> ↑ Deiodinase-III expression -> ↓ Hormones (↑ formation of Reverse T3). (Book p905)"
        },
        {
            "fmt": "recall",
            "q": "What is the primary underlying cause of congenital hypothyroidism on page 905?",
            "opts": [
                "Thyroid dysgenesis",
                "Maternal anti-TPO transplacental passage",
                "Inborn error of iodine organification",
                "Pituitary aplasia"
            ],
            "ans": 0,
            "exp": "Under Congenital Hypothyroidism: 'mostly due to thyroid dysgenesis'. (Book p905)"
        },
        {
            "fmt": "match",
            "q": "Match the newborn physical sign of congenital hypothyroidism to its system — 1) Cranial sign 2) Gastrointestinal sign 3) Hepatic sign … A) Open posterior fontanelle B) Delay in passing meconium C) Prolonged physiological jaundice",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Features of congenital hypothyroidism listed on page 905 are: open posterior fontanelle, delay in passing meconium, and prolonged physiological jaundice. (Book p905)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed on page 905 as a feature of congenital hypothyroidism?",
            "opts": [
                "Continuous high-pitched crying and hyperalertness",
                "Open posterior fontanelle",
                "Delay in passing meconium and prolonged physiological jaundice",
                "Very little crying and excessive sleep"
            ],
            "ans": 0,
            "exp": "Features of congenital hypothyroidism are open posterior fontanelle, delay in passing meconium, prolonged physiological jaundice, very little crying, and excessive sleep. (Book p905)"
        }
    ]
}

p906a = {
    "page": 906,
    "sec": "Hashimoto Features, Histology & Associated Malignancy",
    "items": [
        {
            "fmt": "recall",
            "q": "In which demographic group is Hashimoto's thyroiditis most common?",
            "opts": [
                "Middle-aged female",
                "Elderly male",
                "Adolescent male",
                "Infant female"
            ],
            "ans": 0,
            "exp": "Under Hashimoto's Thyroiditis FEATURES: 'most common in middle-aged female'. (Book p906)"
        },
        {
            "fmt": "match",
            "q": "Match the immunogenetic associations of Hashimoto's thyroiditis — 1) HLA alleles 2) Immune checkpoint polymorphisms … A) HLA-DR3, DR4, DR5 (can be ANA positive) B) CTLA-4 and PTPN-22 polymorphisms",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "HLA associations are DR-3 / DR-4 / DR5 (can be ANA +ve); non-HLA gene polymorphisms are CTLA-4 / PTPN-22. (Book p906)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess gland changes in Hashimoto's thyroiditis: I The thyroid gland is commonly not enlarged. II When goitre is present, it is characteristically an irregular, firm, heterogeneous, non-tender enlargement.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Gland changes: 'Commonly not enlarged' and 'If goitre present : Irregular/ firm/ heterogeneous non tender enlargement of gland'. (Book p906)"
        },
        {
            "fmt": "scenario",
            "q": "On gross examination of a resected thyroid from a middle-aged woman with autoimmune hypothyroidism, the gland appears fibrosed, pale, and firm. What accounts for the pale appearance?",
            "opts": [
                "Dense lymphoid infiltration",
                "Massive accumulation of colloid lakes",
                "Extensive acute bacterial suppuration",
                "Diffuse fatty infiltration of stromal tissue"
            ],
            "ans": 0,
            "exp": "Under Gross appearance: 'Fibrosed gland' and 'Pale gland d/t lymphoid infiltration'. (Book p906)"
        },
        {
            "fmt": "fillup",
            "q": "On microscopic examination of Hashimoto's thyroiditis, the prominent lymphocytic infiltration characteristically organizes into ___ formation.",
            "opts": [
                "Germinal center",
                "Caseating granuloma",
                "Psammoma body",
                "Papillary vascular core"
            ],
            "ans": 0,
            "exp": "Microscopic appearance: 'Lymphocytic infiltration -> Germinal center formation'. (Book p906)"
        },
        {
            "fmt": "recall",
            "q": "What are the transformed, hypereosinophilic epithelial cells with abundant granular cytoplasm seen in Hashimoto's thyroiditis called?",
            "opts": [
                "Hürthle cells (oxyphilic metaplasia)",
                "Parafollicular C cells",
                "Orphan Annie cells",
                "Askanazy giant multinucleated cells"
            ],
            "ans": 0,
            "exp": "Page 906 notes: 'Hypereosinophilic cells : Hürthle cells' and 'Oxyphilic metaplasia'. (Book p906)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding the microscopic findings in Hashimoto's thyroiditis: I The follicular lumen characteristically shows an absence of colloid. II Oxyphilic metaplasia with Hürthle cells is a key hallmark.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Microscopic hallmarks on page 906 include: 'Absence of colloid' and 'Oxyphilic metaplasia' with Hürthle cells. (Book p906)"
        },
        {
            "fmt": "recall",
            "q": "Which malignancy has the highest associated relative risk in patients with longstanding Hashimoto's thyroiditis?",
            "opts": [
                "Extranodal marginal zone lymphoma > papillary carcinoma thyroid",
                "Medullary thyroid carcinoma > follicular carcinoma",
                "Anaplastic thyroid carcinoma > squamoid carcinoma",
                "Primary thyroid sarcoma > metastatic melanoma"
            ],
            "ans": 0,
            "exp": "Under Associated malignancy: 'Extranodal marginal zone lymphoma > papillary carcinoma thyroid'. (Book p906)"
        },
        {
            "fmt": "match",
            "q": "Match the malignancy associated with Hashimoto's thyroiditis to its relative frequency order — 1) Most strongly associated malignancy 2) Secondary associated thyroid carcinoma … A) Extranodal marginal zone lymphoma B) Papillary carcinoma thyroid",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Associated malignancy hierarchy: Extranodal marginal zone lymphoma is more strongly associated than papillary carcinoma of thyroid. (Book p906)"
        },
        {
            "fmt": "fillup",
            "q": "The cellular and cytokine mediators driving thyroid destruction in Hashimoto's include T-cells (both CD-8 and ___), plasma cells, and the cytokine ___.",
            "opts": [
                "CD-4; IFN-gamma",
                "CD-20; IL-4",
                "CD-56; TNF-alpha",
                "FoxP3; TGF-beta"
            ],
            "ans": 0,
            "exp": "Pathological mediators: 'T-cell (CD-8, CD-4)', 'IFN-gamma', and 'Plasma cell'. (Book p906)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed on page 906 as a histological feature or mediator of Hashimoto's thyroiditis?",
            "opts": [
                "Abundant colloid retention in dilated follicles",
                "Hürthle cells (hypereosinophilic cells)",
                "Lymphocytic infiltration with germinal center formation",
                "Interferon-gamma (IFN-γ) and T-cell mediators (CD-4, CD-8)"
            ],
            "ans": 0,
            "exp": "In Hashimoto's, there is characteristically an 'Absence of colloid', not abundant colloid retention. (Book p906)"
        },
        {
            "fmt": "scenario",
            "q": "A 50-year-old woman with a 15-year history of Hashimoto's thyroiditis presents with a rapidly enlarging thyroid goiter. Biopsy demonstrates extranodal marginal zone B-cell lymphoma. What is the classic risk hierarchy noted on page 906?",
            "opts": [
                "Extranodal marginal zone lymphoma > papillary carcinoma thyroid",
                "Papillary carcinoma thyroid > follicular carcinoma thyroid",
                "Medullary thyroid carcinoma > anaplastic thyroid carcinoma",
                "Follicular thyroid carcinoma > marginal zone lymphoma"
            ],
            "ans": 0,
            "exp": "Page 906 explicitly highlights: 'Associated malignancy : Extranodal marginal zone lymphoma > papillary carcinoma thyroid'. (Book p906)"
        }
    ]
}

p907a = {
    "page": 907,
    "sec": "Symptoms, Signs, GAG Deposition & Complications",
    "items": [
        {
            "fmt": "recall",
            "q": "What is the most common (m/c) presenting symptom of generalized slowing (decreased BMR) in primary and secondary hypothyroidism?",
            "opts": [
                "Fatigue / tiredness",
                "Constipation",
                "Cold intolerance",
                "Delayed deep tendon reflexes"
            ],
            "ans": 0,
            "exp": "Under Classical Symptoms: '1. Generalized slowing (↓ BMR) : Fatigue/tiredness (m/c)'. (Book p907)"
        },
        {
            "fmt": "match",
            "q": "Match the manifestations of generalized slowing in hypothyroidism — 1) Speech & Gait 2) Bowel movements 3) Neurologic reflexes 4) Body weight … A) Slow speech and slow gait B) Constipation C) Delayed deep tendon reflexes (DTR) D) Poor appetite with weight gain",
            "opts": [
                "1-A, 2-B, 3-C, 4-D",
                "1-B, 2-A, 3-D, 4-C",
                "1-C, 2-A, 3-B, 4-D",
                "1-A, 2-C, 3-B, 4-D"
            ],
            "ans": 0,
            "exp": "Generalized slowing affects: speech/gait (slow), bowel (constipation), reflexes (delayed DTR), and weight (poor appetite with weight gain). (Book p907)"
        },
        {
            "fmt": "fillup",
            "q": "In primary hypothyroidism, elevated TSH stimulates fibroblasts to produce matrix ___, which trap water and cause non-pitting myxedema.",
            "opts": [
                "Glycosaminoglycans (GAGs)",
                "Collagen type I fibrils",
                "Elastin fibers",
                "Fibronectin lattices"
            ],
            "ans": 0,
            "exp": "In 1° Hypothyroidism: ↑ TSH elevation -> Stimulates Fibroblast -> Stimulates Accumulation of matrix GAG's -> Traps water -> Nonpitting edema. (Book p907)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess the clinical consequences of matrix GAG accumulation trapping water in 1° hypothyroidism: I Facial puffiness, periorbital edema, and hoarse voice. II Macroglossia leading to obstructive sleep apnea syndrome.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Trapped water from matrix GAGs causes puffiness (face), periorbital edema, macroglossia -> obstructive sleep apnea syndrome, hoarse voice, and nonpitting edema. (Book p907)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed on page 907 as a symptom predominant in young females with hypothyroidism?",
            "opts": [
                "Profuse diaphoresis and hyperactive tremors",
                "Hair loss",
                "Irregular menstrual cycle",
                "Dry skin and mood swings"
            ],
            "ans": 0,
            "exp": "Symptoms predominant in young females are hair loss, irregular menstrual cycle, dry skin, and mood swings. (Book p907)"
        },
        {
            "fmt": "recall",
            "q": "Which endocrine disorder is noted on page 907 as causing 'False positive Hypothyroidism' (transiently elevated TSH)?",
            "opts": [
                "Addison's disease",
                "Cushing's syndrome",
                "Conn's syndrome",
                "Pheochromocytoma"
            ],
            "ans": 0,
            "exp": "Page 907 explicitly contains the note: 'Note : False positive Hypothyroidism -> Addison\'s disease'. (Book p907)"
        },
        {
            "fmt": "scenario",
            "q": "An adult with severe longstanding primary hypothyroidism presents with prominent pseudohypertrophy of both calf muscles accompanied by slowness and muscle stiffness. What eponymous disorder is depicted in the photo on page 907?",
            "opts": [
                "Hoffman syndrome",
                "Pendred syndrome",
                "Allan-Herndon-Dudley syndrome",
                "De Quervain syndrome"
            ],
            "ans": 0,
            "exp": "The clinical photo on page 907 demonstrates: 'Hoffman syndrome Pseudohypertrophy in calf muscle'. (Book p907)"
        },
        {
            "fmt": "match",
            "q": "Match the serous cavity effusions seen in hypothyroid polyserositis — 1) Pleural cavity 2) Pericardial space 3) Peritoneal cavity … A) Pleural effusion B) Pericardial effusion C) Ascites",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Complications of hypothyroidism include serous effusions in three spaces: pleural effusion, pericardial effusion, and ascites. (Book p907)"
        },
        {
            "fmt": "recall",
            "q": "What is the most common cause of Carpal Tunnel Syndrome (CTS) in females versus males on page 907?",
            "opts": [
                "Females: Hypothyroidism; Males: Amyloidosis",
                "Females: Amyloidosis; Males: Hypothyroidism",
                "Females: Diabetes mellitus; Males: Gout",
                "Females: Pregnancy; Males: Rheumatoid arthritis"
            ],
            "ans": 0,
            "exp": "Carpal tunnel syndrome (CTS): 'm/c cause in females : Hypothyroidism' and 'm/c cause in males : Amyloidosis'. (Book p907)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding Carpal Tunnel Syndrome (CTS) epidemiology on page 907: I Hypothyroidism is the most common cause in females. II Amyloidosis is the most common cause in males.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Page 907 notes for CTS: - m/c cause in females : Hypothyroidism, - m/c cause in males : Amyloidosis. (Book p907)"
        },
        {
            "fmt": "scenario",
            "q": "A 48-year-old obese woman with untreated hypothyroidism presents with severe loud snoring, daytime sleepiness, and witnessed nocturnal apneas. What anatomical mechanism links this to her thyroid disease?",
            "opts": [
                "Macroglossia secondary to TSH-induced matrix GAG accumulation causing obstructive sleep apnea syndrome",
                "Bilateral recurrent laryngeal nerve compression from thyroid fibrosis",
                "Direct neuromuscular weakness of the diaphragm from hypothyroid myopathy",
                "Tracheal deviation from subacute granulomatous expansion"
            ],
            "ans": 0,
            "exp": "GAG accumulation traps water, producing macroglossia that leads directly to obstructive sleep apnea syndrome. (Book p907)"
        },
        {
            "fmt": "fillup",
            "q": "Although page 907 prints 'Hypocholesterolaemia' among complications (an editorial misprint in the scan), the classical metabolic consequence of reduced LDL clearance in hypothyroidism is ___.",
            "opts": [
                "Hypercholesterolemia",
                "Severe hypolipidemia",
                "Isolated hypertriglyceridemia with low LDL",
                "Abetalipoproteinemia"
            ],
            "ans": 0,
            "exp": "Page 907 lists 'Hypocholesterolemia' in its complications column, but clinically and on page 903, impaired cholesterol clearance classically causes hypercholesterolemia. (Book p907)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed on page 907 as a complication of hypothyroidism?",
            "opts": [
                "Hypercalcemic nephrolithiasis",
                "Myxedema coma and Hashimoto encephalopathy",
                "Bradycardia and polyserositis (pleural/pericardial effusion, ascites)",
                "Obstructive sleep apnea syndrome and Carpal tunnel syndrome"
            ],
            "ans": 0,
            "exp": "Hypercalcemia and nephrolithiasis are complications of severe thyrotoxicosis (p903), not hypothyroidism. Complications on p907 are myxedema coma, encephalopathy, bradycardia, effusions, OSA, and CTS. (Book p907)"
        }
    ]
}

p908a = {
    "page": 908,
    "sec": "Autoantibodies, Treatment Indications & L-Thyroxine Titration",
    "items": [
        {
            "fmt": "recall",
            "q": "In a patient presenting with newly identified hypothyroidism, autoantibody screening returns completely negative. What diagnostic entity is considered on page 908?",
            "opts": [
                "Transient hypothyroidism due to thyroiditis (postviral or post-vaccine)",
                "Confirmed lifelong Hashimoto's disease",
                "TSH-secreting pituitary macroadenoma",
                "Consumptive hemangioma deiodinase excess"
            ],
            "ans": 0,
            "exp": "In the workup for Hashimoto's, negative autoantibodies indicate: 'Transient Hypothyroidism : Thyroiditis (Postviral / Post vaccine) -> may/may not require treatment'. (Book p908)"
        },
        {
            "fmt": "match",
            "q": "Match the autoantibody in Hashimoto's disease to its percentage association on page 908 — 1) Thyroid peroxidase (TPO) antibody 2) Thyroglobulin antibody 3) TSH Receptor Antibody … A) 90 - 100% B) 80 - 90% C) 10 - 20%",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Autoantibody associations in Hashimoto's: TPO Ab 90 - 100%, Thyroglobulin Ab 80 - 90%, and TSH Receptor Ab 10 - 20%. (Book p908)"
        },
        {
            "fmt": "fillup",
            "q": "The single most sensitive and prevalent autoantibody in Hashimoto's disease is ___, present in ___ of cases.",
            "opts": [
                "Thyroid peroxidase (TPO) antibody; 90 - 100%",
                "Thyroglobulin antibody; 50 - 60%",
                "TSH Receptor Antibody; 75 - 85%",
                "Anti-enolase antibody; 30 - 40%"
            ],
            "ans": 0,
            "exp": "Thyroid peroxidase antibody is the most strongly associated antibody, present in 90 - 100% of Hashimoto's patients. (Book p908)"
        },
        {
            "fmt": "match",
            "q": "Match the combination of elevated TSH (↑ TSH) and free T4 level to the diagnosis — 1) ↓ Free T4 2) ↑ Free T4 3) Normal Free T4 … A) 1° Hypothyroidism B) TSH Secreting Adenoma C) Subclinical 1° Hypothyroidism",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "↑ TSH + ↓ Free T4 = 1° Hypothyroidism; ↑ TSH + ↑ Free T4 = TSH Secreting Adenoma; ↑ TSH + Normal Free T4 = Subclinical 1° Hypothyroidism. (Book p908)"
        },
        {
            "fmt": "recall",
            "q": "What is the definitive TSH cut-off value that provides an absolute indication for L-thyroxine treatment in confirmed Hashimoto's disease regardless of symptoms?",
            "opts": [
                "TSH value > 10 mcu/ltr (mIU/L)",
                "TSH value > 5 mcu/ltr (mIU/L)",
                "TSH value > 20 mcu/ltr (mIU/L)",
                "TSH value > 2.5 mcu/ltr (mIU/L)"
            ],
            "ans": 0,
            "exp": "Under Treatment Indications: 'Confirmed Hashimoto\'s (TSH value > 10 mcu/ltr)'. (Book p908)"
        },
        {
            "fmt": "truefalse",
            "q": "For patients with a TSH value between 5 and 10 mcu/ltr: I Treatment is indicated if vague symptoms are present with TPO positivity, positive family history, or pregnancy. II Treatment is indicated if severe symptoms are present.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "When TSH is 5 - 10 mcu/ltr, treatment is indicated for vague symptoms + (TPO +ve, Family history, Pregnancy) or severe symptoms. (Book p908)"
        },
        {
            "fmt": "scenario",
            "q": "A 27-year-old woman in early pregnancy is found to have a TSH of 6.8 mcu/ltr with normal free T4. Her anti-TPO antibody titre is elevated. What is the correct management per page 908?",
            "opts": [
                "Initiate L-thyroxine replacement immediately",
                "Defer treatment and recheck TSH postpartum",
                "Wait until TSH exceeds 10 mcu/ltr before treating",
                "Prescribe potassium iodide drops only"
            ],
            "ans": 0,
            "exp": "In pregnancy with TSH 5 - 10 mcu/ltr and TPO positivity, L-thyroxine treatment is explicitly indicated. (Book p908)"
        },
        {
            "fmt": "numeric",
            "q": "What is the recommended starting dose of L-thyroxine for a symptomatic hypothyroid patient under 60 years of age?",
            "opts": [
                "1.6 - 1.8 µg/kg/day (approximately 100 µg/day)",
                "0.5 - 0.8 µg/kg/day (approximately 50 µg/day)",
                "2.2 - 2.5 µg/kg/day (approximately 150 µg/day)",
                "25 µg/day flat dose"
            ],
            "ans": 0,
            "exp": "For < 60 yr + symptomatic: 'L-Thyroxine 1.6-1.8 µg/kg/day (Approx 100µg/day)'. (Book p908)"
        },
        {
            "fmt": "fillup",
            "q": "In patients under 60 years of age on L-thyroxine, subsequent dosage adjustments should be titrated by ___ µg/day.",
            "opts": [
                "25 - 50 µg/day",
                "5 - 10 µg/day",
                "75 - 100 µg/day",
                "100 - 150 µg/day"
            ],
            "ans": 0,
            "exp": "Under drugs: 'Dose change can be by 25-50 µg/day' for patients under 60 years. (Book p908)"
        },
        {
            "fmt": "numeric",
            "q": "In elderly patients (> 60 years of age), what is the recommended starting dose and dose adjustment step for L-thyroxine?",
            "opts": [
                "Starting dose 25 µg/day; dose change by 25 µg/day",
                "Starting dose 50 µg/day; dose change by 50 µg/day",
                "Starting dose 100 µg/day; dose change by 25 µg/day",
                "Starting dose 10 µg/day; dose change by 5 µg/day"
            ],
            "ans": 0,
            "exp": "In elderly (>60 yr): starting dose is '25 µg/day' and 'Dose change by 25 µg/day'. (Book p908)"
        },
        {
            "fmt": "recall",
            "q": "Why must elderly patients (> 60 years) be started on a low dose of L-thyroxine (25 µg/day)?",
            "opts": [
                "Due to the risk of cardiotoxicity (e.g., precipitating angina or arrhythmias)",
                "Because of rapid hepatic clearance of levothyroxine in older adults",
                "Due to the high risk of nephrogenic diabetes insipidus",
                "Because older patients do not convert T4 to T3"
            ],
            "ans": 0,
            "exp": "Elderly patients start at 25 µg/day explicitly '(Due to cardiotoxicity)'. (Book p908)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT an indication to treat subclinical hypothyroidism with TSH 5 - 10 mcu/ltr on page 908?",
            "opts": [
                "Isolated subclinical hypercholesterolemia without symptoms",
                "Vague symptoms with TPO positivity",
                "Vague symptoms with a positive family history",
                "Pregnancy or presence of severe symptoms"
            ],
            "ans": 0,
            "exp": "Indications for TSH 5-10 mcu/ltr are: vague symptoms + TPO +ve, family history, pregnancy, or severe symptoms. (Book p908)"
        }
    ]
}

p909a = {
    "page": 909,
    "sec": "Patient Instructions, Myxedema Coma & SREAT / Hashimoto Encephalopathy",
    "items": [
        {
            "fmt": "recall",
            "q": "What specific administration instructions must be given to patients taking oral L-thyroxine on page 909?",
            "opts": [
                "Take on an empty stomach in the morning (7 - 7:30 am) with a glass of water, and wait 30 minutes before meals",
                "Take with a full meal at dinner time to maximize lipid-phase absorption",
                "Take at bedtime co-administered with calcium and iron supplements",
                "Take dissolved in hot milk twice daily after meals"
            ],
            "ans": 0,
            "exp": "Instructions: 'Empty stomach (morning 7-7:30 am) with glass of water. Take meal after 30 minutes'. (Book p909)"
        },
        {
            "fmt": "match",
            "q": "Match the drug that inhibits L-thyroxine absorption to its formulation — 1) FeSO4 2) CaCO3 3) Al(OH)3 / Sucralfate … A) Ferrous sulfate iron salt B) Calcium carbonate C) Aluminum hydroxide antacid / mucosal protectant",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Drugs to be avoided because they inhibit absorption include FeSO4, CaCO3, Al(OH)3, and Sucralfate. (Book p909)"
        },
        {
            "fmt": "fillup",
            "q": "The single most common (m/c) cause of treatment failure in hypothyroid patients prescribed L-thyroxine is ___.",
            "opts": [
                "Non-compliance",
                "Autoimmune malabsorption syndrome",
                "Genetic deiodinase-2 inactivation",
                "Accelerated renal excretion"
            ],
            "ans": 0,
            "exp": "Under follow-up: 'm/c cause of treatment failure : Non-compliance'. (Book p909)"
        },
        {
            "fmt": "numeric",
            "q": "How long after the serum TSH value normalizes does the patient typically achieve clinical symptomatic relief?",
            "opts": [
                "3 - 6 months",
                "1 - 2 weeks",
                "24 - 48 hours",
                "12 - 18 months"
            ],
            "ans": 0,
            "exp": "Page 909 explicitly notes: 'Clinical relief : 3-6 months after TSH value becomes normal'. (Book p909)"
        },
        {
            "fmt": "numeric",
            "q": "What is the mortality rate of myxedema coma reported on page 909?",
            "opts": [
                "40%",
                "10%",
                "75%",
                "5%"
            ],
            "ans": 0,
            "exp": "Under Emergency Conditions: 'myxedema coma : mortality 40%'. (Book p909)"
        },
        {
            "fmt": "recall",
            "q": "What are the primary trigger factors listed for precipitating myxedema coma?",
            "opts": [
                "Non-compliance and infection (e.g., COVID-19 or lower respiratory tract infection - LRI)",
                "Excessive dietary iodine and strenuous physical exertion",
                "Abrupt initiation of high-dose corticosteroids",
                "Accidental overdose of antithyroid medications"
            ],
            "ans": 0,
            "exp": "Trigger factors for myxedema coma: 'Non-compliance, infection (i.e. covid, LRI)'. (Book p909)"
        },
        {
            "fmt": "match",
            "q": "Match the characteristic 'Hypo' presenting features of myxedema coma — 1) Respiratory 2) Glucose metabolism 3) Electrolytes 4) Body temperature … A) Hypoventilation B) Hypoglycemia C) Hyponatremia D) Hypothermia",
            "opts": [
                "1-A, 2-B, 3-C, 4-D",
                "1-B, 2-A, 3-D, 4-C",
                "1-C, 2-A, 3-B, 4-D",
                "1-A, 2-D, 3-B, 4-C"
            ],
            "ans": 0,
            "exp": "The 'Hypo' tetrad of myxedema coma consists of Hypoventilation, Hypoglycemia, Hyponatremia, and Hypothermia. (Book p909)"
        },
        {
            "fmt": "scenario",
            "q": "An elderly woman with myxedema coma is admitted with severe bradycardia, hypothermia (34°C), and low-voltage ECG complexes. Which intravenous fluid is indicated, and which must be avoided?",
            "opts": [
                "Hypertonic saline indicated; hypotonic saline strictly avoided",
                "Hypotonic saline indicated; hypertonic saline strictly avoided",
                "5% Dextrose in water indicated; hypertonic saline strictly avoided",
                "Albumin colloid indicated; normal saline strictly avoided"
            ],
            "ans": 0,
            "exp": "Treatment specifies: 'Hypertonic saline (Avoid hypotonic saline)'. (Book p909)"
        },
        {
            "fmt": "management",
            "q": "What is the complete medical treatment regimen for myxedema coma on page 909?",
            "opts": [
                "IV L-thyroxine 500 µg OD -> 50-100 µg/day, Steroid, IV T3 5-20 µg, Hypertonic saline",
                "Oral PTU 1000 mg stat, Propranolol 60 mg Q4H, Iopanoic acid, Normal saline",
                "External active warming with heated blankets, Hydrocortisone, Hypotonic saline",
                "IV Levothyroxine 25 µg daily, Furosemide infusion, Potassium chloride"
            ],
            "ans": 0,
            "exp": "Treatment for myxedema coma: IV L-thyroxine 500 µg OD -> 50-100 µg/day, Steroid, IV T3 5-20 µg, and Hypertonic saline. (Book p909)"
        },
        {
            "fmt": "fillup",
            "q": "Steroid-responsive encephalopathy associated with autoimmune thyroid illness (SREAT / Hashimoto encephalopathy) is an autoimmune vasculitis that is ___ to thyroid function, and can be seen in ___ status.",
            "opts": [
                "Unrelated; euthyroid",
                "Proportional; hyperthyroid",
                "Secondary; myxedema coma",
                "Inversely related; post-thyroidectomy"
            ],
            "ans": 0,
            "exp": "SREAT: 'Can be seen in euthyroid status' and is an 'Autoimmune vasculitis unrelated to thyroid function'. (Book p909)"
        },
        {
            "fmt": "recall",
            "q": "Which autoantibody and HLA allele are characteristically elevated and associated with SREAT on page 909?",
            "opts": [
                "Anti-enolase antibody; HLA-B8",
                "Anti-TPO antibody; HLA-B27",
                "TSH receptor antibody; HLA-DR3",
                "Anti-ganglioside antibody; HLA-B35"
            ],
            "ans": 0,
            "exp": "SREAT is characterized by '↑↑ Antibodies (Anti-enolase Ab)' and 'HLA -B8'. (Book p909)"
        },
        {
            "fmt": "match",
            "q": "Match the clinical presentations of SREAT — 1) Progressive cognitive decline 2) Paroxysmal motor events 3) Vascular mimic … A) Altered level of consciousness B) Seizure & myoclonus C) Stroke-like presentation",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Presentations of SREAT include: slowly progressive cognitive decline (altered level of consciousness), seizure & myoclonus, and stroke-like presentation. (Book p909)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess SREAT management on page 909: I The primary and definitive pharmacologic management is corticosteroids (steroids). II Patients must immediately receive high-dose intravenous levothyroxine.",
            "opts": [
                "I is true; II is false",
                "Both I and II are true",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Management of SREAT is explicitly stated as 'management : Steroids'. Thyroid hormone therapy is not the primary treatment since SREAT is vasculitic and unrelated to thyroid function. (Book p909)"
        }
    ]
}

# ==============================================================================
# CHAPTER 43: Thyrotoxicosis and Thyroiditis (p910–916)
# ==============================================================================

c43_order = ["p910a", "p911a", "p912a", "p913a", "p914a", "p915a", "p916a"]

c43_units = [
    {
        "title": "Causes of Thyrotoxicosis, Graves Disease & Iodine Effects",
        "sec": "Thyrotoxicosis vs Euthyroid Hyperthyroxinemia & Iodine Effects · p910",
        "guide": "Distinguish overworking vs normal gland thyrotoxicosis, demographics and associations of Graves (smoking, postpartum, HAART, HLA-DR2), Wolff-Chaikoff effect (transient 5-7 day inhibition by excess iodide), and Jod-Basedow phenomenon.",
        "parts": ["p910a"]
    },
    {
        "title": "Graves Antibodies, Manifestations & Systemic Features",
        "sec": "Antibodies, Triad of Manifestations & Clinical Presentation · p911",
        "guide": "Cover TRAb (80-95%) driving ophthalmopathy, pretibial myxedema, and acropachy; common hyperadrenergic symptoms; elderly apathetic thyrotoxicosis; protein catabolism (proximal myopathy without fasciculations, osteopenia, stones); and hypokalemic periodic paralysis.",
        "parts": ["p911a"]
    },
    {
        "title": "Scintigraphy Patterns, Ophthalmopathy Mnemonic & Eye Signs",
        "sec": "Scintigraphy Grid, Ophthalmopathy Progression & Eponymous Signs · p912",
        "guide": "Anchor the scintigraphy table, microscopic scalloped appearance, the 40/40/20 rule, the IM SLOW extraocular muscle mnemonic, eponymous eye signs (Von Graefe, Joffroy, Stellwag, Dalrymple, Möbius), and non-palpable gland causes.",
        "parts": ["p912a"]
    },
    {
        "title": "Laboratory Findings, Anti-Thyroid Drugs, Relapse, RAI & Surgery",
        "sec": "Ancillary Labs, Thionamides, RAI & Surgical Indications · p913",
        "guide": "Master thionamide equivalency (methimazole 6 mg = carbimazole 10 mg = PTU 100 mg), PTU in pregnancy, carbimazole 5 mg TDS, methimazole teratogenicity, side effects (rash m/c, agranulocytosis most dangerous), RAI precautions, and surgical indications.",
        "parts": ["p913a"]
    },
    {
        "title": "Thyrotoxic Crisis & Classification of Thyroiditis",
        "sec": "Thyroid Storm Protocol & Acute, Subacute, Chronic Thyroiditis · p914",
        "guide": "Review thyroid storm presentation and 4-drug emergency regimen (PTU 1000 mg stat -> 250 mg Q4H, steroid, propranolol 60 mg Q4H, iopanoic acid 500 mg BD), acute suppurative thyroiditis (piriform sinus fistula), de Quervain HLA-B35, and Riedel IgG4 fibrous disease.",
        "parts": ["p914a"]
    },
    {
        "title": "Subacute Thyroiditis Mechanism, Timeline & Postpartum Thyroiditis",
        "sec": "Subacute Thyroiditis Triphasic Curve & Postpartum Comparison · p915",
        "guide": "Follow the stored hormone release mechanism (T3/T4 < 15, neck/ear pain, high ESR), aspirin 600 mg Q6H DOC, the 18-week three-phase curve, and the comparison grid with postpartum silent thyroiditis.",
        "parts": ["p915a"]
    },
    {
        "title": "Effects of Amiodarone on Thyroid & Thyroiditis Comparison Grid",
        "sec": "Amiodarone Type I vs Type II & Differential Diagnosis Grid · p916",
        "guide": "Contrast Amiodarone-induced thyrotoxicosis Type I (underlying disease, Jod-Basedow, high vascularity, thionamides) vs Type II (destructive, no antibodies, low vascularity, steroids), and master the summary comparison table (subacute vs Graves vs toxic MNG).",
        "parts": ["p916a"]
    }
]

p910a = {
    "page": 910,
    "sec": "Thyrotoxicosis vs Euthyroid Hyperthyroxinemia & Iodine Effects",
    "items": [
        {
            "fmt": "recall",
            "q": "How does page 910 distinguish thyrotoxicosis from euthyroid hyperthyroxinemia in patients with elevated T3 and T4 levels?",
            "opts": [
                "Thyrotoxicosis has elevated free T3 and free T4, whereas euthyroid hyperthyroxinemia has elevated total T3 and total T4",
                "Thyrotoxicosis has suppressed total hormones, whereas euthyroid hyperthyroxinemia has elevated free hormones",
                "Thyrotoxicosis has normal free hormones, whereas euthyroid hyperthyroxinemia has elevated free T4 only",
                "Thyrotoxicosis always features high TSH, whereas euthyroid hyperthyroxinemia features low TSH"
            ],
            "ans": 0,
            "exp": "Hyperthyroxinemia (↑ T3, ↑ T4) branches into: ↑ free T3, T4 = Thyrotoxicosis; and ↑ total T3, T4 = Euthyroid Hyperthyroxinemia. (Book p910)"
        },
        {
            "fmt": "match",
            "q": "Under thyrotoxicosis, match the functional gland status to its etiologies — 1) Overworking thyroid gland (Hyperthyroidism) 2) Normal working thyroid gland … A) Autoimmune Graves (m/c), Nodular toxic adenoma, Toxic MNG, TSH adenoma, Struma ovarii B) Thyroiditis, Thyrotoxicosis factitia, Amiodarone",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Overworking gland includes Graves, toxic adenoma, toxic MNG, TSH adenoma, and struma ovarii; normal gland includes thyroiditis, factitia, and amiodarone. (Book p910)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed under euthyroid hyperthyroxinemia (↑ total T3, T4) on page 910?",
            "opts": [
                "Struma ovarii",
                "Thyroid binding globulin (TBG) excess",
                "Resistant to Thyroid Hormone (RTH)",
                "Deiodinase deficiency and Sick Euthyroid syndrome"
            ],
            "ans": 0,
            "exp": "Struma ovarii is a cause of thyrotoxicosis from an overworking gland; euthyroid hyperthyroxinemia includes TBG excess, RTH, deiodinase deficiency, and sick euthyroid syndrome. (Book p910)"
        },
        {
            "fmt": "numeric",
            "q": "What percentage of all thyrotoxicosis cases are caused by Graves' disease on page 910?",
            "opts": [
                "75%",
                "25%",
                "50%",
                "95%"
            ],
            "ans": 0,
            "exp": "Under Graves disease Features: '75% Thyrotoxicosis cases -> Graves disease'. (Book p910)"
        },
        {
            "fmt": "recall",
            "q": "What is the peak population age and gender predilection for Graves' disease?",
            "opts": [
                "20 - 50 years; Females > Males",
                "60 - 80 years; Males > Females",
                "5 - 15 years; Females = Males",
                "> 65 years; Females > Males"
            ],
            "ans": 0,
            "exp": "Under Graves disease: 'Population at risk : 20-50 years (F > m)'. (Book p910)"
        },
        {
            "fmt": "match",
            "q": "Match the clinical risk associations of Graves' disease — 1) Lifestyle factor 2) Reproductive period 3) Antiviral therapy … A) Smoking B) Post partum C) HAART (Highly active antiretroviral therapy)",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Associations listed on page 910 for Graves' disease include: Smoking, Post partum, HAART, and HLA: DR-2, CTLA-4, PTPN-22. (Book p910)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding immunogenetic associations of Graves' disease on page 910: I HLA association is HLA-DR2. II Non-HLA gene associations include CTLA-4 and PTPN-22.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Under Graves disease: 'HLA : DR-2, CTLA-4, PTPN-22'. (Book p910)"
        },
        {
            "fmt": "fillup",
            "q": "The Wolff-Chaikoff effect occurs when excess iodide transiently inhibits thyroid synthesis for ___ days, followed by ___.",
            "opts": [
                "5 - 7 days; escape",
                "2 - 3 weeks; thyroid storm",
                "24 - 48 hours; permanent hypothyroidism",
                "30 days; follicular hyperplasia"
            ],
            "ans": 0,
            "exp": "Wolff Chaikoff effect: 'Excess iodide -> Inhibits Transiently Thyroid synthesis (5-7 days) -> Followed by Escape'. (Book p910)"
        },
        {
            "fmt": "recall",
            "q": "Which medication is specifically noted on page 910 as precipitating the Wolff-Chaikoff effect?",
            "opts": [
                "Amiodarone",
                "Lithium",
                "Phenytoin",
                "Carbamazepine"
            ],
            "ans": 0,
            "exp": "Under Wolff Chaikoff effect: 'Seen with Amiodarone'. (Book p910)"
        },
        {
            "fmt": "scenario",
            "q": "A patient with nodular thyroid disease residing in an iodine-deficient area receives an iodine-containing radiographic contrast agent and promptly develops thyrotoxicosis. What iodine-induced disorder explains this?",
            "opts": [
                "Jod-Basedow phenomenon",
                "Wolff-Chaikoff effect",
                "De Quervain thyroiditis",
                "Allan-Herndon-Dudley syndrome"
            ],
            "ans": 0,
            "exp": "Jod Basedow phenomenon: 'Patient with Nodular or TSH-R Antibody in iodine deficient area -> Iodine Supply (+) -> Thyrotoxicosis'. (Book p910)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess these two iodine-related effects: I Wolff-Chaikoff effect is transient synthesis inhibition by excess iodide (seen with amiodarone). II Jod-Basedow phenomenon is thyrotoxicosis induced by iodine supply in patients with nodular disease or TSH-R antibodies in iodine-deficient areas.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Both statements represent the exact definitions of the Wolff-Chaikoff effect and Jod-Basedow phenomenon on page 910. (Book p910)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following causes of thyrotoxicosis represents ectopic thyroid tissue outside the neck?",
            "opts": [
                "Struma ovarii",
                "Graves disease",
                "Toxic multinodular goiter",
                "Nodular toxic adenoma"
            ],
            "ans": 0,
            "exp": "Struma ovarii is an ovarian teratoma containing functioning thyroid tissue that causes hyperthyroidism. (Book p910)"
        }
    ]
}

p911a = {
    "page": 911,
    "sec": "Antibodies, Triad of Manifestations & Clinical Presentation",
    "items": [
        {
            "fmt": "match",
            "q": "Match the autoantibody to its percentage positivity on page 911 — 1) Thyroid Stimulating Hormone-Receptor Ab (TRAb) 2) Thyroglobulin Ab 3) TPO Ab … A) +ve 80 - 95% (most important in Graves) B) +ve 50 - 70% (most important in Hashimoto) C) +ve 50 - 80%",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "TRAb is positive in 80-95% (most important in Graves); Thyroglobulin Ab in 50-70% (most important in Hashimoto); TPO Ab in 50-80%. (Book p911)"
        },
        {
            "fmt": "recall",
            "q": "TSH-Receptor antibodies stimulate T-cells, fibroblasts, and GAG synthesis to produce which triad of unique clinical findings in Graves' disease?",
            "opts": [
                "Thyroid ophthalmopathy, Thyroid dermopathy (pretibial myxedema), and Thyroid acropachy",
                "Periorbital edema, macroglossia, and hoarse voice",
                "Carpal tunnel syndrome, delayed reflexes, and bradycardia",
                "Sensorineural hearing loss, goiter, and periodic paralysis"
            ],
            "ans": 0,
            "exp": "TRAb stimulates T-cells, fibroblasts, and GAGs, leading to the unique triad of Graves: Thyroid ophthalmopathy, Thyroid Dermopathy (Pretibial myxedema), and Thyroid Acropachy. (Book p911)"
        },
        {
            "fmt": "match",
            "q": "Match the unique physical findings of Graves' disease shown in the photographs — 1) Eye pathology 2) Lower extremity dermopathy 3) Digits … A) Severe proptosis, eyelid retraction, and exophthalmos B) Pretibial myxedema (thick nodular infiltrative dermopathy) C) Acropachy",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "The photographs illustrate proptosis/eyelid retraction/exophthalmos, acropachy, and thick nodular infiltrative dermopathy (pretibial myxedema). (Book p911)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess common symptoms of thyrotoxicosis: I Restlessness, irritability, tremulousness, nervousness, and tachycardia. II Sweating, diarrhea, polyuria, warm moist skin, and oligomenorrhea/amenorrhea.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "All listed features are documented under Common Features of thyrotoxicosis on page 911. (Book p911)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed among the common features of thyrotoxicosis on page 911?",
            "opts": [
                "Severe constipation and dry cold coarse skin",
                "Restlessness, irritability, and tremulousness",
                "Tachycardia, sweating, and warm moist skin",
                "Diarrhea, polyuria, and oligomenorrhea/amenorrhea"
            ],
            "ans": 0,
            "exp": "Constipation and dry cold skin are classic hypothyroid features; thyrotoxicosis features diarrhea, warm moist skin, tachycardia, and sweating. (Book p911)"
        },
        {
            "fmt": "scenario",
            "q": "An 76-year-old man presents with profound lethargy, fatigue, and unintentional weight loss without tremors or hyperactive behavior. TFTs confirm thyrotoxicosis. What clinical entity does this represent?",
            "opts": [
                "Apathetic thyrotoxicosis (in elderly population)",
                "Hashimoto encephalopathy (SREAT)",
                "Myxedema madness",
                "Consumptive deiodinase-3 deficiency"
            ],
            "ans": 0,
            "exp": "Under In Elder Population: 'Apathetic thyrotoxicosis : Fatigue and weight loss'. (Book p911)"
        },
        {
            "fmt": "recall",
            "q": "In an elderly patient with elevated T3 and T4 levels, which cardiac manifestation is emphasized on page 911?",
            "opts": [
                "Atrial fibrillation and worsening of heart failure",
                "Complete third-degree heart block",
                "Ventricular fibrillation and cardiac tamponade",
                "Aortic valve stenosis with low-voltage complexes"
            ],
            "ans": 0,
            "exp": "Under Other Features: 'Atrial fibrillation ↑ T3 T4 (mainly elderly)' and 'Worsening of heart failure'. (Book p911)"
        },
        {
            "fmt": "scenario",
            "q": "A 32-year-old male with severe thyrotoxicosis has proximal muscle weakness of the hips and shoulders. Muscle examination demonstrates NO fasciculations. What is the clinical significance of absent fasciculations per page 911?",
            "opts": [
                "Confirms thyrotoxic proximal myopathy from protein catabolism; presence of fasciculations would indicate anterior horn cell disease",
                "Confirms concurrent Guillain-Barré syndrome",
                "Rules out myopathy and indicates psychogenic conversion weakness",
                "Establishes primary polymyositis requiring muscle biopsy"
            ],
            "ans": 0,
            "exp": "Under Severe Thyrotoxicosis: 'Proximal myopathy: No fasciculations (If fasciculations +ve -> Anterior horn cell disease)'. (Book p911)"
        },
        {
            "fmt": "truefalse",
            "q": "In severe thyrotoxicosis: I Protein catabolism leads to bone pain, fractures, and hypercalcemia with hypercalciuria (stones). II Thyrotoxicosis-associated periodic paralysis presents like hypokalemic paralysis.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Severe thyrotoxicosis causes protein catabolism -> proximal myopathy, bone pain/fractures, hypercalcemia -> hypercalciuria -> stones; periodic paralysis presents like hypokalemia paralysis. (Book p911)"
        },
        {
            "fmt": "match",
            "q": "Match the clinical triad to the diagnosis in the page 911 contrast note — 1) Weight loss + good appetite 2) Weight gain + loss of appetite … A) Graves' disease B) Hypothyroidism",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Page 911 notes: 'Wt loss + good appetite -> Graves disease' and 'Wt gain + loss of appetite -> Hypothyroid'. (Book p911)"
        },
        {
            "fmt": "fillup",
            "q": "Thyrotoxicosis-associated periodic paralysis presents with acute episodic flaccid quadriparesis resembling ___ paralysis.",
            "opts": [
                "Hypokalemia",
                "Hyperkalemia",
                "Hypocalcemia",
                "Hypercalcemia"
            ],
            "ans": 0,
            "exp": "Under Thyrotoxicosis Associated Periodic paralysis: 'Presents like hypokalemia paralysis'. (Book p911)"
        },
        {
            "fmt": "recall",
            "q": "Which guidelines for Graves' disease symptoms are cited at the base of page 911?",
            "opts": [
                "Endocrine Society of India guidelines",
                "American Thyroid Association guidelines",
                "European Thyroid Association guidelines",
                "British Thyroid Association guidelines"
            ],
            "ans": 0,
            "exp": "At the bottom of page 911: 'Endocrine Society of India - Guidelines for Graves : Above mentioned symptoms'. (Book p911)"
        }
    ]
}

p912a = {
    "page": 912,
    "sec": "Scintigraphy Grid, Ophthalmopathy Progression & Eponymous Signs",
    "items": [
        {
            "fmt": "match",
            "q": "Match the scintigraphy finding to the diagnosis on page 912 — 1) Diffuse symmetrical uptake (75-80%), reduced salivary uptake 2) Low or absent uptake, prominent salivary uptake 3) Increased uptake in nodule with contralateral reduced uptake … A) Graves' disease B) Thyroiditis C) Toxic adenoma",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Scintigraphy table: Graves shows diffuse 75-80% uptake with reduced salivary uptake; Thyroiditis shows low/absent uptake with prominent salivary uptake; Toxic adenoma shows increased uptake in nodule with contralateral reduced uptake. (Book p912)"
        },
        {
            "fmt": "numeric",
            "q": "On radionuclide scintigraphy, compare physiological uptake against the diffuse uptake seen in Graves' disease:",
            "opts": [
                "25% normal; 75 - 80% elevated",
                "10% normal; 40 - 50% elevated",
                "50% normal; 95 - 100% elevated",
                "5% normal; 30% elevated"
            ],
            "ans": 0,
            "exp": "Scintigraphy table: Normal uptake is 25%; in Graves' disease, diffuse uptake reaches 75 - 80%. (Book p912)"
        },
        {
            "fmt": "fillup",
            "q": "On histopathology of Graves' disease, follicular epithelial cells appear tall columnar with resorbed colloid producing a characteristic ___ appearance.",
            "opts": [
                "Scalloped",
                "Psammoma body",
                "Orphan Annie eye",
                "Ground-glass"
            ],
            "ans": 0,
            "exp": "The histological caption on page 912 states: 'Tall Columnar cell resorbed colloid (Scalloped appearance)'. (Book p912)"
        },
        {
            "fmt": "numeric",
            "q": "What percentage of the hyperthyroid population presents with ophthalmopathy?",
            "opts": [
                "30%",
                "10%",
                "75%",
                "50%"
            ],
            "ans": 0,
            "exp": "Under Graves Ophthalmopathy: '30% Hyperthyroid population can present ophthalmopathy'. (Book p912)"
        },
        {
            "fmt": "match",
            "q": "According to the '40/40/20 rule' of Graves' ophthalmopathy, match the presentation category to its percentage — 1) Graves symptoms elsewhere, followed later by ophthalmopathy 2) Graves with ophthalmopathy present at diagnosis 3) Ophthalmopathy as initial presentation (unilateral to bilateral) … A) 40% B) 40% C) 20%",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "The 40/40/20 rule: 40% develop ophthalmopathy later; 40% have ophthalmopathy at presentation; 20% have ophthalmopathy as initial presentation (U/L -> B/L). (Book p912)"
        },
        {
            "fmt": "fillup",
            "q": "According to the mnemonic 'IM SLOW' for extraocular muscle involvement in Graves' ophthalmopathy, the first muscle affected is the ___ rectus, followed next by the ___ rectus.",
            "opts": [
                "Inferior; medial",
                "Superior; lateral",
                "Medial; superior",
                "Lateral; inferior"
            ],
            "ans": 0,
            "exp": "Under mnemonic IM SLOW: 'First muscle affected : Inferior rectus -> next: medial rectus -> next: Superior rectus -> next: Obliques'. (Book p912)"
        },
        {
            "fmt": "recall",
            "q": "What is the full muscle involvement sequence in the 'IM SLOW' mnemonic for Graves' orbitopathy?",
            "opts": [
                "Inferior rectus → Medial rectus → Superior rectus → Obliques",
                "Internal rectus → Middle rectus → Superior rectus → Lateral rectus",
                "Inferior oblique → Medial rectus → Superior oblique → Lateral rectus",
                "Inferior rectus → Superior rectus → Medial rectus → Lateral rectus"
            ],
            "ans": 0,
            "exp": "The mnemonic IM SLOW expands to: Inferior rectus -> Medial rectus -> Superior rectus -> Obliques. (Book p912)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding active Graves' ophthalmopathy: I Radioactive iodine treatment is contraindicated. II Medical management includes smoking cessation and high-dose intravenous steroids.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Page 912 states: 'Radioactive treatment C/I' and 'Rx : stop smoking, High dose IV steroid'. (Book p912)"
        },
        {
            "fmt": "match",
            "q": "Match the eponymous Graves' eye signs — 1) Von Graefe's 2) Joffroy's 3) Stellwag's 4) Dalrymple's … A) Lid lag in down gaze B) Absent creases in the forehead on superior gaze C) Incomplete and infrequent blinking D) Widened palpebral fissure during fixation",
            "opts": [
                "1-A, 2-B, 3-C, 4-D",
                "1-B, 2-A, 3-D, 4-C",
                "1-C, 2-A, 3-B, 4-D",
                "1-A, 2-C, 3-B, 4-D"
            ],
            "ans": 0,
            "exp": "Eye signs: Von Graefe's = Lid lag in down gaze; Joffroy = Absent creases in forehead on superior gaze; Stellwag = Incomplete and infrequent blinking; Dalrymple's = Widened palpebral fissure during fixation. (Book p912)"
        },
        {
            "fmt": "fillup",
            "q": "The eponymous sign defined by impairment of ocular convergence in Graves' disease is ___ sign.",
            "opts": [
                "Möbius",
                "Kocher",
                "Von Graefe's",
                "Stellwag's"
            ],
            "ans": 0,
            "exp": "Page 912 lists: 'Möbius sign : Convergence'. (Book p912)"
        },
        {
            "fmt": "scenario",
            "q": "A 28-year-old female presents with biochemical thyrotoxicosis (suppressed TSH, elevated free T3 and T4). On careful neck examination, the thyroid gland is completely non-palpable. What does this suggest per page 912?",
            "opts": [
                "Exogenous hormone cause or thyroiditis",
                "Graves disease with retrosternal extension",
                "Toxic multinodular goiter",
                "TSH-secreting pituitary macroadenoma"
            ],
            "ans": 0,
            "exp": "Page 912 contains the note: 'Note : Non palpable gland with thyrotoxicosis = Exogenous cause / thyroiditis'. (Book p912)"
        },
        {
            "fmt": "recall",
            "q": "In the Graves' disease management flowchart on page 912, what T3/T4 ratio is characteristic alongside suppressed TSH and elevated free hormones before confirming TRAb positivity?",
            "opts": [
                "T3 / T4 ratio > 20",
                "T3 / T4 ratio < 15",
                "T3 / T4 ratio between 5 and 10",
                "T3 / T4 ratio < 1"
            ],
            "ans": 0,
            "exp": "Under management: 'On Investigations : TSH ↓, free T3 ↑, free T4 ↑, T3/T4 > 20 -> Next: Antibody : TSH-(R) Ab +ve -> Next: Diagnosis : Graves disease'. (Book p912)"
        }
    ]
}

p913a = {
    "page": 913,
    "sec": "Ancillary Labs, Thionamides, RAI & Surgical Indications",
    "items": [
        {
            "fmt": "recall",
            "q": "Which ancillary laboratory abnormalities are listed under 'Other laboratory findings' in thyrotoxicosis on page 913?",
            "opts": [
                "Hyperglycemia, Hypercalcemia, Leukocytosis, ALP ↑, LFT ↑",
                "Hypoglycemia, severe hypocalcemia, and leukopenia",
                "Hyperkalemia, hyperphosphatemia, and isolated amylase elevation",
                "Hyponatremia, metabolic alkalosis, and thrombocytosis"
            ],
            "ans": 0,
            "exp": "Other laboratory findings on page 913: Hyperglycemia, Hypercalcemia, Leucocytosis, ALP ↑, and LFT ↑. (Book p913)"
        },
        {
            "fmt": "numeric",
            "q": "What is the expected remission rate with anti-thyroid drug therapy in Graves' disease after 12 to 18 months?",
            "opts": [
                "60 - 70%",
                "20 - 30%",
                "40 - 50%",
                "90 - 95%"
            ],
            "ans": 0,
            "exp": "Under Treatment: Anti-thyroid drugs achieve '60-70% : Remission In 12-18 months'. (Book p913)"
        },
        {
            "fmt": "match",
            "q": "Match the equivalent thionamide doses from the potency equivalence formula on page 913 — 1) Methimazole 2) Carbimazole 3) Propylthiouracil (PTU) … A) 6 mg B) 10 mg C) 100 mg",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Dose equivalence formula: 'methimazole (6 mg) = Carbimazole (10 mg) = Propylthiouracil (100 mg)'. (Book p913)"
        },
        {
            "fmt": "recall",
            "q": "Why is Propylthiouracil (PTU) preferred in pregnancy despite being hepatotoxic?",
            "opts": [
                "Increased plasma protein binding reduces transplacental transfer to the fetus",
                "It has an exceptionally long 24-hour half-life",
                "It is an irreversible inhibitor of iodide uptake",
                "It has zero risk of causing maternal agranulocytosis"
            ],
            "ans": 0,
            "exp": "Under Propylthiouracil: 'Preferred in Pregnancy', '↑ Plasma protein binding', and 'Hepatotoxic (Not preferred now)'. (Book p913)"
        },
        {
            "fmt": "truefalse",
            "q": "Compare Carbimazole and Methimazole properties on page 913: I Carbimazole is preferred over PTU, dosed 5 mg TDS daily, with a half-life of 6-8 hours. II Methimazole is an irreversible inhibitor with a 6-hour half-life, but is teratogenic causing aplasia cutis and choanal atresia.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Both statements match the descriptions of Carbimazole and Methimazole on page 913. (Book p913)"
        },
        {
            "fmt": "match",
            "q": "Match the thionamide adverse effect to its clinical status — 1) Rash 2) Agranulocytosis 3) Hepatobiliary / Autoimmune … A) Most common (m/c) side effect B) Most dangerous side effect C) Cholestasis, Drug-induced lupus",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Side effects: Rash (m/c), Agranulocytosis (most dangerous), Cholestasis, and Drug-induced lupus. (Book p913)"
        },
        {
            "fmt": "scenario",
            "q": "A 30-year-old woman with Graves' disease started on carbimazole 2 weeks ago presents with high fever, mouth ulcers, and a severe sore throat. What is the most critical and dangerous side effect to rule out immediately?",
            "opts": [
                "Agranulocytosis",
                "Drug-induced lupus",
                "Intrahepatic cholestasis",
                "Allergic maculopapular rash"
            ],
            "ans": 0,
            "exp": "Agranulocytosis is noted as the 'most dangerous' side effect of thionamides; high fever and sore throat require an urgent complete blood count. (Book p913)"
        },
        {
            "fmt": "fillup",
            "q": "In the titration regimen for antithyroid drugs, the patient should be revisited at ___ weeks to monitor ___ and ___ values.",
            "opts": [
                "4 - 6 weeks; free T3 and free T4",
                "1 - 2 weeks; TSH only",
                "3 months; anti-TPO titers",
                "6 months; urinary iodine excretion"
            ],
            "ans": 0,
            "exp": "Under Titration regimen: 'Revisit : 4-6 weeks, monitor free T3 and free T4 values'. (Book p913)"
        },
        {
            "fmt": "recall",
            "q": "What is the recommended dose and schedule of propranolol for thyrotoxic symptom control on page 913?",
            "opts": [
                "40 mg Q6H",
                "10 mg once daily",
                "80 mg at bedtime",
                "20 mg TDS"
            ],
            "ans": 0,
            "exp": "Item 2 under Treatment: 'Propranolol : 40 mg Q6H'. (Book p913)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding Radioactive Iodine (RAI) in relapsed Graves': I Patient must be made euthyroid with minimum 1 month of antithyroid drugs prior to RAI to prevent thyrotoxic crisis. II RAI has a proven direct association with secondary malignancy risk.",
            "opts": [
                "I is true; II is false",
                "Both I and II are true",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Page 913 specifies: 'Before initiating make patient euthyroid: minimum 1 month anti-thyroid drugs (to prevent thyrotoxicosis)' and 'No association with cancer risk'. (Book p913)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following is NOT listed as a disadvantage or contraindication of radioactive iodine (RAI) on page 913?",
            "opts": [
                "High risk of subsequent thyroid carcinoma",
                "Contraindicated in pregnancy",
                "Increased risk / aggravation of eye disease",
                "Lifelong L-thyroxine required in 10% of the population"
            ],
            "ans": 0,
            "exp": "Page 913 explicitly notes: 'No association with cancer risk'. Disadvantages listed are C/I in pregnancy, eye disease (↑ risk), and lifelong L-thyroxine required (10%). (Book p913)"
        },
        {
            "fmt": "management",
            "q": "In a patient with Graves' disease and severe, active ophthalmopathy, what medical regimen is recommended on page 913?",
            "opts": [
                "IV Steroid + Rituximab ± Radiotherapy",
                "Radioactive iodine ablation with high-dose aspirin",
                "Propylthiouracil monotherapy with external cold compresses",
                "Immediate total thyroidectomy preceded by potassium perchlorate"
            ],
            "ans": 0,
            "exp": "Under In relapse cases: 'In Severe Ophthalmopathy : IV Steroid + Rituximab ± Radiotherapy'. (Book p913)"
        },
        {
            "fmt": "oddoneout",
            "q": "If radiotherapy is contraindicated or not possible, surgery is indicated for all of the following EXCEPT:",
            "opts": [
                "Mild asymptomatic euthyroid ophthalmopathy alone",
                "Biopsy suspicious of malignancy",
                "Concurrent hyperparathyroidism or compressive symptoms",
                "Pregnancy / lactation and young children"
            ],
            "ans": 0,
            "exp": "Surgical indications on page 913: biopsy suspicious of malignancy, hyperparathyroidism, pregnancy/lactation, young children, and compressive symptoms. (Book p913)"
        }
    ]
}

p914a = {
    "page": 914,
    "sec": "Thyroid Storm Protocol & Acute, Subacute, Chronic Thyroiditis",
    "items": [
        {
            "fmt": "match",
            "q": "Match the clinical features of thyrotoxic crisis (thyroid storm) — 1) Predisposing factors 2) Presenting features … A) Inadequate treatment before radiotherapy, surgery, acute illness B) Arrhythmia, fever with delirium, seizures",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Predisposing factors: inadequate treatment before radiotherapy, surgery, illness; Presenting features: arrhythmia, fever with delirium, seizure. (Book p914)"
        },
        {
            "fmt": "management",
            "q": "What is the specific dosing regimen of Propylthiouracil (PTU) in the management of thyrotoxic crisis on page 914?",
            "opts": [
                "1000 mg stat loading dose, followed by 250 mg Q4H",
                "100 mg stat, followed by 50 mg TDS",
                "500 mg BD with meals",
                "2000 mg as a single daily dose"
            ],
            "ans": 0,
            "exp": "Under thyrotoxic crisis management: 'Propylthiouracil : 1000mg stat -> 250mg Q4H'. (Book p914)"
        },
        {
            "fmt": "fillup",
            "q": "In thyrotoxic crisis management, oral iodine is administered as ___ (500 mg BD) to exploit the ___ effect.",
            "opts": [
                "Iopanoic acid; Wolff-Chaikoff",
                "Lugol's iodine; Jod-Basedow",
                "Potassium iodide; escape",
                "Radioactive I-131; ablative"
            ],
            "ans": 0,
            "exp": "Under management: 'Oral iodine : Iopanoic acid 500mg BD (Wolff-Chaikoff effect)'. (Book p914)"
        },
        {
            "fmt": "recall",
            "q": "What is the propranolol dose specified for thyrotoxic crisis on page 914?",
            "opts": [
                "60 mg Q4H",
                "40 mg Q6H",
                "10 mg Q8H",
                "80 mg once daily"
            ],
            "ans": 0,
            "exp": "For thyrotoxic crisis, propranolol is dosed at '60mg Q4H' (compared to 40 mg Q6H in routine thyrotoxicosis). (Book p914)"
        },
        {
            "fmt": "match",
            "q": "Match the etiology of acute thyroiditis to its clinical features — 1) Post-infection 2) Non-infectious acute causes … A) Children, follows staph/strep, pyriform sinus site, normal TFT, pain B) Radiation induced, trauma induced",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Acute thyroiditis branches into: Post-infection (children, follows staph/strep, site: piriform sinus, TFT normal, pain), Radiation induced, and Trauma induced. (Book p914)"
        },
        {
            "fmt": "scenario",
            "q": "An 8-year-old child presents with sudden severe anterior neck tenderness and fever following streptococcal pharyngitis. TFTs are completely normal. Scintigraphy reveals an infected tract originating from the piriform sinus. What is the diagnosis?",
            "opts": [
                "Acute post-infection thyroiditis",
                "Subacute de Quervain thyroiditis",
                "Riedel's chronic thyroiditis",
                "Graves thyrotoxic crisis"
            ],
            "ans": 0,
            "exp": "Acute post-infection thyroiditis occurs in children, follows staph/strep, arises from a piriform sinus fistula, presents with pain, and has normal TFTs. (Book p914)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess acute thyroiditis: I Thyroid function tests (TFT) are characteristically normal. II Local pain is the primary presenting symptom.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "For Acute Thyroiditis: 'TFT : Normal' and 'Symptom : Pain'. (Book p914)"
        },
        {
            "fmt": "match",
            "q": "Match the synonymous names for Subacute Thyroiditis — 1) Eponymous designation 2) Pathological designation 3) Viral relationship … A) De Quervain's thyroiditis B) Granulomatous thyroiditis C) Post-viral (with no direct viral association established)",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Under Subacute Thyroiditis: 'De Quervain\'s/Subacute thyroiditis : AKA Granulomatous/viral thyroiditis. Post-viral (no viral association)'. (Book p914)"
        },
        {
            "fmt": "recall",
            "q": "Which HLA allele is strongly associated with subacute (de Quervain's) thyroiditis on page 914?",
            "opts": [
                "HLA-B35",
                "HLA-DR2",
                "HLA-B8",
                "HLA-B27"
            ],
            "ans": 0,
            "exp": "Under Subacute Thyroiditis Features: 'HLA : B-35'. (Book p914)"
        },
        {
            "fmt": "fillup",
            "q": "On radionuclide scintigraphy, subacute (de Quervain's) thyroiditis characteristically shows ___ uptake.",
            "opts": [
                "No uptake (absent uptake)",
                "Intense diffuse uptake (75-80%)",
                "Solitary 'hot' nodule uptake",
                "Patchy hyperfunctioning uptake"
            ],
            "ans": 0,
            "exp": "Features of subacute thyroiditis: 'No uptake in Scintigraphy', also depicted in the scan image 'Subacute thyroiditis : No uptake in scintigraphy'. (Book p914)"
        },
        {
            "fmt": "scenario",
            "q": "A 52-year-old man presents with a stony hard, painless neck mass with dense fibrous tissue infiltrating adjacent soft tissues. Serology reveals elevated IgG4 levels. What is the diagnosis?",
            "opts": [
                "Riedel's thyroiditis (IgG4-related disease)",
                "Subacute granulomatous thyroiditis",
                "Acute suppurative thyroiditis",
                "Anaplastic thyroid carcinoma"
            ],
            "ans": 0,
            "exp": "Chronic Thyroiditis includes Riedel's thyroiditis: 'AKA IgG4-related disease, Painless hard thyroid, Dense fibrosis'. (Book p914)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess Riedel's thyroiditis on page 914: I It is recognized as an IgG4-related disease. II The physical hallmark is a painless, hard thyroid with dense fibrosis.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Riedel's thyroiditis: AKA IgG4-related disease, Painless hard thyroid, Dense fibrosis. (Book p914)"
        }
    ]
}

p915a = {
    "page": 915,
    "sec": "Subacute Thyroiditis Triphasic Curve & Postpartum Comparison",
    "items": [
        {
            "fmt": "recall",
            "q": "What initial mechanism triggers the clinical presentation and thyrotoxic phase of subacute thyroiditis?",
            "opts": [
                "Stored hormone release from damaged thyroid follicles",
                "New autonomous hormone hyper-synthesis driven by TRAb",
                "Excessive peripheral T4 to T3 conversion by deiodinase-2",
                "Ectopic thyroid tissue activation in ovarian teratoma"
            ],
            "ans": 0,
            "exp": "Under mechanism: 'Stored hormone release -> ↑ Free T3, ↑ Free T4, ↓ TSH, T3/T4 < 15'. (Book p915)"
        },
        {
            "fmt": "match",
            "q": "Match the early presentation findings of subacute thyroiditis — 1) Systemic sign 2) Gland pain 3) Inflammatory marker … A) Fever > 2 weeks B) Neck pain / sore throat / ear pain C) Markedly elevated ESR (↑↑ ESR)",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Early presentation: Fever > 2 weeks; Pain in the gland: Neck pain / Sore throat / Ear pain; and ↑↑ ESR. (Book p915)"
        },
        {
            "fmt": "numeric",
            "q": "Once stored hormones are exhausted in subacute thyroiditis, what percentage of patients develop permanent hypothyroidism?",
            "opts": [
                "15%",
                "50%",
                "2%",
                "85%"
            ],
            "ans": 0,
            "exp": "Under mechanism: 'Stored hormone exhausted -> Hypothyroid (In 15% Permanent hypothyroid) -> Recovery'. (Book p915)"
        },
        {
            "fmt": "scenario",
            "q": "A 38-year-old woman presents with severe neck pain radiating to her ears, fever for 2 weeks, high ESR, and suppressed TSH with high free T4 (T3/T4 ratio < 15). What is the drug of choice (DOC) and its dose?",
            "opts": [
                "Aspirin 600 mg Q6H (DOC)",
                "Carbimazole 20 mg TDS",
                "Propylthiouracil 500 mg stat",
                "Levothyroxine 100 µg daily"
            ],
            "ans": 0,
            "exp": "Under management: 'Aspirin 600 mg Q6H (DOC)', NSAIDS, Steroids. (Book p915)"
        },
        {
            "fmt": "match",
            "q": "On the clinical course graph of subacute thyroiditis, match the time interval to its corresponding phase — 1) 0 - 6 weeks 2) 6 - 12 weeks 3) 12 - 18 weeks … A) Thyrotoxic phase (high urinary/serum T4, high ESR, low TSH) B) Hypothyroid phase (TSH rising, T4 falling) C) Recovery phase (normalization)",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "The graph shows: 0-6 weeks is the toxic phase; 6-12 weeks is the hypothyroid phase; 12-18 weeks is the recovery phase. (Book p915)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following conditions is NOT associated with an elevated TSH level in the summary note on page 915?",
            "opts": [
                "Central (secondary) hypothyroidism",
                "1° Hypothyroid",
                "Resistance to Thyroid hormone (RTH)",
                "TSH Adenoma and recovery phase of thyroiditis"
            ],
            "ans": 0,
            "exp": "Central hypothyroidism has a 'Normal TSH level' (with low peripheral hormones); elevated TSH is seen in 1° hypothyroid, RTH, TSH adenoma, and recovery phase of thyroiditis. (Book p915)"
        },
        {
            "fmt": "recall",
            "q": "Per the summary note on page 915, what does a normal TSH level signify in a patient with low circulating thyroid hormones?",
            "opts": [
                "Central hypothyroidism",
                "Primary autoimmune hypothyroidism",
                "Early toxic phase of subacute thyroiditis",
                "Graves disease in complete remission"
            ],
            "ans": 0,
            "exp": "Page 915 explicitly states: 'Normal TSH level : Central hypothyroidism'. (Book p915)"
        },
        {
            "fmt": "fillup",
            "q": "Postpartum thyroiditis is also known as ___ or ___ thyroiditis.",
            "opts": [
                "Painless; silent",
                "Subacute; granulomatous",
                "Dense; fibrous",
                "Suppurative; pyogenic"
            ],
            "ans": 0,
            "exp": "Under Postpartum thyroiditis: 'AKA Painless / silent thyroiditis'. (Book p915)"
        },
        {
            "fmt": "match",
            "q": "Match the autoimmune diseases associated with postpartum thyroiditis — 1) Systemic Lupus Erythematosus (SLE) 2) Sjogren's syndrome 3) Endocrine / skin autoimmune … A) Connective tissue disease B) Exocrine gland sicca syndrome C) Type 1 Diabetes Mellitus (T1DM) / Vitiligo",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Postpartum thyroiditis is seen in association with autoimmune diseases: SLE, Sjogren's syndrome, T1DM, and Vitiligo. (Book p915)"
        },
        {
            "fmt": "truefalse",
            "q": "Compare pain and pregnancy timing in Subacute vs Postpartum thyroiditis: I Neck pain is present in subacute thyroiditis, but absent/silent in postpartum thyroiditis. II Subacute thyroiditis has no association with pregnancy, whereas postpartum thyroiditis occurs post partum.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Table comparisons: Pain is Present in subacute, Absent/silent in postpartum; Association with pregnancy is No in subacute, Post Partum in postpartum. (Book p915)"
        },
        {
            "fmt": "match",
            "q": "From the subacute vs postpartum thyroiditis comparison table, match the lab/treatment characteristics — 1) ESR 2) Anti-TPO antibody 3) Role of steroids … A) Subacute: ↑↑ ESR; -ve TPO Ab; Steroids: Yes B) Postpartum: Normal ESR; +ve TPO Ab; Steroids: No (β-blocker can be used)",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Subacute has ↑↑ ESR, -ve TPO Ab, and steroids are useful (Yes); Postpartum has normal ESR, +ve TPO Ab, and no steroids (β-blockers used). (Book p915)"
        },
        {
            "fmt": "truefalse",
            "q": "Assess autoimmunity in these thyroiditides: I Subacute thyroiditis is an autoimmune disease. II Postpartum thyroiditis is an autoimmune disease with positive anti-TPO antibodies.",
            "opts": [
                "I is false; II is true",
                "Both I and II are true",
                "I is true; II is false",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Table shows: Autoimmune is 'No' for Subacute thyroiditis, and 'Yes' for Postpartum thyroiditis. (Book p915)"
        }
    ]
}

p916a = {
    "page": 916,
    "sec": "Amiodarone Type I vs Type II & Differential Diagnosis Grid",
    "items": [
        {
            "fmt": "recall",
            "q": "Amiodarone-induced hypothyroidism is typically a transient phenomenon mediated by which physiological mechanism?",
            "opts": [
                "Wolff-Chaikoff phenomenon due to massive iodine load",
                "Jod-Basedow hyperfunctioning autonomous activation",
                "Lysosomal-mediated destructive follicular necrosis",
                "Direct antibody-mediated TSH receptor blockade"
            ],
            "ans": 0,
            "exp": "Under Amiodarone induces: Hypothyroidism is a 'Transient phenomenon' 'D/t Wolff chaikoff phenomenon'. (Book p916)"
        },
        {
            "fmt": "match",
            "q": "Match the type of amiodarone-induced thyrotoxicosis to its underlying pathophysiology — 1) Amiodarone-induced thyrotoxicosis Type-I 2) Amiodarone-induced thyrotoxicosis Type-II … A) Patient with underlying thyroid disease (Graves or MNG); Jod-Basedow phenomenon; ↑↑ vascularity B) No underlying disease; lysosomal-mediated destruction; no antibodies; ↓↓ vascularity",
            "opts": [
                "1-A, 2-B",
                "1-B, 2-A",
                "1-A, 2-A",
                "1-B, 2-B"
            ],
            "ans": 0,
            "exp": "Type I occurs in underlying disease via Jod-Basedow with ↑↑ vascularity; Type II occurs without underlying disease via lysosomal destruction with ↓↓ vascularity. (Book p916)"
        },
        {
            "fmt": "management",
            "q": "What is the medical drug of choice (DOC) for Amiodarone-Induced Thyrotoxicosis Type I versus Type II?",
            "opts": [
                "Type I: Thionamides (DOC); Type II: Corticosteroids (Steroids)",
                "Type I: Corticosteroids; Type II: Thionamides",
                "Type I: Radioactive iodine; Type II: High-dose aspirin",
                "Type I: Lithium carbonate; Type II: Potassium iodide"
            ],
            "ans": 0,
            "exp": "Management: Type-I -> Stop treatment, Start Thionamide (DOC); Type-II -> Drug should be stopped, Rx -> Steroid. (Book p916)"
        },
        {
            "fmt": "scenario",
            "q": "A 62-year-old man on chronic amiodarone therapy develops thyrotoxicosis. Color Doppler ultrasound demonstrates absent/markedly decreased thyroid vascularity (↓↓ vascularity), and autoantibodies are negative. What is the diagnosis and treatment?",
            "opts": [
                "Amiodarone-induced thyrotoxicosis Type II; stop drug and treat with steroids",
                "Amiodarone-induced thyrotoxicosis Type I; treat with thionamides",
                "Graves disease; treat with radioactive iodine ablation",
                "Subacute de Quervain thyroiditis; treat with aspirin"
            ],
            "ans": 0,
            "exp": "Type II has no underlying disease, no antibodies, markedly decreased vascularity, and is treated by stopping amiodarone and starting steroids. (Book p916)"
        },
        {
            "fmt": "match",
            "q": "In the comparison table on page 916, match the condition to its typical symptom duration — 1) Subacute Thyroiditis 2) Graves' Disease 3) Toxic MNG … A) Days to weeks B) 2 - 3 months C) Months to years",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Duration: Subacute Thyroiditis lasts days to weeks; Graves' Disease lasts 2-3 months; Toxic MNG lasts months to years. (Book p916)"
        },
        {
            "fmt": "recall",
            "q": "In which entity alone is local neck pain characteristically present in the page 916 comparison grid?",
            "opts": [
                "Subacute Thyroiditis",
                "Graves' Disease",
                "Toxic Multinodular Goiter",
                "Toxic Adenoma"
            ],
            "ans": 0,
            "exp": "Under Neck pain: Present in Subacute Thyroiditis; Absent in Graves' Disease; Absent in Toxic MNG. (Book p916)"
        },
        {
            "fmt": "match",
            "q": "Match the goiter physical characteristics on page 916 — 1) Subacute Thyroiditis 2) Graves' Disease 3) Toxic MNG … A) Small goiter B) Diffuse goiter C) Nodular goiter",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Goiter type: Subacute Thyroiditis = Small; Graves' Disease = Diffuse; Toxic MNG = Nodular. (Book p916)"
        },
        {
            "fmt": "truefalse",
            "q": "Regarding extrathyroidal manifestations (ophthalmopathy and dermopathy): I Present in Graves' disease. II Absent in both Subacute thyroiditis and Toxic multinodular goiter.",
            "opts": [
                "Both I and II are true",
                "I is true; II is false",
                "I is false; II is true",
                "Both I and II are false"
            ],
            "ans": 0,
            "exp": "Ophthalmopathy / Dermopathy is Absent in Subacute Thyroiditis, Present in Graves' Disease, and Absent in Toxic MNG. (Book p916)"
        },
        {
            "fmt": "fillup",
            "q": "In differentiating hyperthyroid conditions on page 916, the serum T3/T4 ratio is ___ in subacute thyroiditis, but ___ in both Graves' disease and toxic MNG.",
            "opts": [
                "< 15; > 20",
                "> 20; < 15",
                "> 50; < 10",
                "= 1; > 100"
            ],
            "ans": 0,
            "exp": "T3/T4 ratio is < 15 in Subacute Thyroiditis, and > 20 in both Graves' Disease and Toxic MNG. (Book p916)"
        },
        {
            "fmt": "recall",
            "q": "TSH-receptor stimulating antibodies are characteristically present in which of the three conditions?",
            "opts": [
                "Graves' disease only",
                "Subacute thyroiditis only",
                "Toxic multinodular goiter only",
                "Both subacute thyroiditis and toxic MNG"
            ],
            "ans": 0,
            "exp": "TSH-R stimulating Ab is Absent in Subacute Thyroiditis, Present in Graves' Disease, and Absent in Toxic MNG. (Book p916)"
        },
        {
            "fmt": "recall",
            "q": "On ultrasound and color Doppler, what is described as the best test to diagnose Graves' disease on page 916?",
            "opts": [
                "Diffusely enlarged gland with markedly increased vascularity (↑↑ vascularity)",
                "Small shrunken gland with absent vascularity",
                "Multiple hypoechoic nodules with peripheral flow",
                "Thick calcified thyroid capsule with acoustic shadowing"
            ],
            "ans": 0,
            "exp": "Ultrasound for Graves' Disease: 'Diffusely enlarged gland, ↑↑ vascularity (Best test to diagnose)'. (Book p916)"
        },
        {
            "fmt": "match",
            "q": "Match the radioiodine (RAI) uptake finding to the condition on page 916 — 1) Subacute Thyroiditis 2) Graves' Disease 3) Toxic MNG … A) Low uptake B) Markedly increased (↑↑) uptake C) Depends on functional status of nodules (cold or hot nodules)",
            "opts": [
                "1-A, 2-B, 3-C",
                "1-B, 2-A, 3-C",
                "1-C, 2-B, 3-A",
                "1-A, 2-C, 3-B"
            ],
            "ans": 0,
            "exp": "Radioiodine uptake: Subacute Thyroiditis = Low uptake; Graves' Disease = ↑↑ uptake; Toxic MNG = Depends on functional status of nodules (cold or hot nodules). (Book p916)"
        },
        {
            "fmt": "oddoneout",
            "q": "Which of the following features is NOT characteristic of Toxic Multinodular Goiter (MNG) in the page 916 table?",
            "opts": [
                "Prominent infiltrative ophthalmopathy and pretibial dermopathy",
                "Duration of symptoms spanning months to years",
                "Commonly occurs in the elderly population (Females > Males)",
                "Nodular goiter with enlarged nodules on ultrasound"
            ],
            "ans": 0,
            "exp": "Ophthalmopathy and dermopathy are absent in toxic MNG; they are present only in Graves' disease. (Book p916)"
        }
    ]
}

# ==============================================================================
# WRITE FILES
# ==============================================================================

def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Wrote {path}")

# Write C41
write_json(ROOT / "data" / "parts" / "c41" / "_order.json", c41_order)
write_json(ROOT / "data" / "parts" / "c41" / "p902a.json", p902a)
write_json(ROOT / "data" / "parts" / "c41" / "p903a.json", p903a)
write_json(ROOT / "data" / "parts" / "c41" / "p904a.json", p904a)
write_json(ROOT / "data" / "units" / "c41.json", c41_units)

# Write C42
write_json(ROOT / "data" / "parts" / "c42" / "_order.json", c42_order)
write_json(ROOT / "data" / "parts" / "c42" / "p905a.json", p905a)
write_json(ROOT / "data" / "parts" / "c42" / "p906a.json", p906a)
write_json(ROOT / "data" / "parts" / "c42" / "p907a.json", p907a)
write_json(ROOT / "data" / "parts" / "c42" / "p908a.json", p908a)
write_json(ROOT / "data" / "parts" / "c42" / "p909a.json", p909a)
write_json(ROOT / "data" / "units" / "c42.json", c42_units)

# Write C43
write_json(ROOT / "data" / "parts" / "c43" / "_order.json", c43_order)
write_json(ROOT / "data" / "parts" / "c43" / "p910a.json", p910a)
write_json(ROOT / "data" / "parts" / "c43" / "p911a.json", p911a)
write_json(ROOT / "data" / "parts" / "c43" / "p912a.json", p912a)
write_json(ROOT / "data" / "parts" / "c43" / "p913a.json", p913a)
write_json(ROOT / "data" / "parts" / "c43" / "p914a.json", p914a)
write_json(ROOT / "data" / "parts" / "c43" / "p915a.json", p915a)
write_json(ROOT / "data" / "parts" / "c43" / "p916a.json", p916a)
write_json(ROOT / "data" / "units" / "c43.json", c43_units)

print("All Thyroid part files and unit files written successfully!")
