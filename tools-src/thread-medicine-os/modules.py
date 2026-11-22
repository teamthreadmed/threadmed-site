import html
def b(g, checked=False):
    names={'A':'strong support','B':'moderate support','C':'weak support, individualize','I':'insufficient evidence','X':'not supported'}
    cls='g g'+g+(' ok' if checked else '')
    return f'<span class="{cls}" role="img" aria-label="Grade {g}, {names[g]}, {"checked against source" if checked else "verification pending"}">{g}</span>'
def row(kind, text, g=None, checked=False):
    return f'<li><span class="k">{kind}</span><span class="t">{text}</span>{b(g,checked) if g else "<span></span>"}</li>'
L,M,D,P,C,N='Lifestyle','Medication','Device or procedure','Psychological','Complementary','Navigate'
domains=[
("FN.FALL","Falls","STEADI questions, Timed Up and Go, orthostatic blood pressure",[
 (L,"Structured gait, balance and strength exercise","A",True),
 (L,"Tai chi: may reduce falls, low-certainty evidence","C",True),
 (M,"Deprescribe sedatives, anticholinergics and excess antihypertensives","B"),
 (M,"Vitamin D to prevent falls in community-dwelling older adults","X",True),
 (D,"Home hazard reduction by an occupational therapist, for people at high risk","A",True),
 (D,"Cataract surgery","B"),
 (C,"Acupuncture: no fall-prevention trials identified","I"),
 (N,"Exercise programme first. Multifactorial assessment is an individual decision","C",True)]),
("FN.BONE","Bone and fragility fracture","DXA, FRAX, vertebral imaging. A prior fragility fracture is itself the diagnosis",[
 (M,"Antiresorptive or anabolic therapy matched to fracture risk","A"),
 (L,"Progressive resistance and impact training","B"),
 (L,"Adequate protein, calcium and vitamin D","B"),
 (C,"No modality with fracture-outcome evidence","I"),
 (N,"Fracture liaison service after any fragility fracture: fewer subsequent fractures in observational comparisons","B",True)]),
("FN.MUSC","Muscle and frailty","SARC-F, grip strength, gait speed, chair stand, Clinical Frailty Scale",[
 (L,"Progressive resistance training","A",True),
 (L,"Protein-rich diet or protein supplementation","B",True),
 (M,"Anabolic hormones for sarcopenia: no guideline recommendation","I",True),
 (M,"Protect lean mass during incretin-based weight loss","C"),
 (N,"Comprehensive geriatric assessment when a frailty screen is positive","B",True)]),
("FN.COG","Cognition","Mini-Cog or MoCA when there is a concern. Check hearing, vision, mood, sleep and drugs first",[
 (L,"Structured multidomain programme: exercise, diet, cognitive and social challenge","B",True),
 (M,"Intensive blood pressure control: less mild cognitive impairment, dementia not significantly reduced","B",True),
 (M,"LDL and diabetes control","C"),
 (M,"Deprescribe anticholinergics and sedatives","C"),
 (M,"Anti-amyloid antibodies in selected early Alzheimer disease, with ARIA monitoring","C"),
 (C,"Ginkgo for dementia prevention","X",True),
 (C,"Acupuncture","I"),
 (N,"Dementia care navigation with caregiver support, as in the CMS GUIDE model","B")]),
("FN.HEAR","Hearing","Ask, then audiometry, app-based or formal",[
 (D,"Hearing aids with audiology support, for communication and participation","A"),
 (D,"Hearing intervention to slow cognitive decline: benefit only in the higher-risk subgroup","C",True),
 (D,"Cerumen removal; over-the-counter aids for mild to moderate loss","B"),
 (M,"Review ototoxic medicines","C"),
 (N,"Audiology referral, device cost and fitting support",None)]),
("FN.VIS","Vision","Acuity at each review. Dilated eye examination on schedule in diabetes",[
 (D,"Cataract surgery","A"),
 (D,"Updated refraction; single-vision distance lenses outdoors for people who fall","C"),
 (M,"AREDS2 for intermediate macular degeneration; anti-VEGF for neovascular disease","A"),
 (L,"Smoking cessation; glucose and blood pressure control","B"),
 (N,"Eye care referral and low-vision rehabilitation",None)]),
("FN.MOOD","Mood","PHQ-9 and GAD-7",[
 (P,"CBT, behavioural activation, problem-solving therapy","A"),
 (M,"Antidepressants for moderate to severe depression","A"),
 (L,"Exercise","B"),
 (C,"Acupuncture for depression: low-certainty evidence","C"),
 (N,"Collaborative care: care manager plus structured, scheduled follow-up","A",True)]),
("FN.REST","Stress, sleep and connection","Perceived Stress Scale, insomnia questions, three-item loneliness scale",[
 (P,"CBT for insomnia as initial treatment","A",True),
 (L,"Mindfulness-based stress reduction; regular physical activity","B"),
 (M,"Avoid benzodiazepines and Z-drugs for chronic insomnia where possible","A",True),
 (C,"Acupuncture for insomnia: low-certainty evidence","C"),
 (N,"Social prescribing, community groups, caregiver respite","C")]),
("FN.PAIN","Pain and mobility","PEG pain-interference scale, gait speed",[
 (L,"Exercise, and weight loss when overweight, for knee and hip osteoarthritis","A",True),
 (L,"Tai chi for knee and hip osteoarthritis","A",True),
 (M,"Topical NSAIDs for knee osteoarthritis","A",True),
 (M,"Oral NSAIDs: lowest dose, shortest course. Opioids: avoid as routine therapy","B"),
 (C,"Acupuncture for chronic back, neck, osteoarthritis and headache pain: small gain over sham","B",True),
 (P,"Pain-focused CBT","C",True),
 (N,"Physical therapy. Medicare covers acupuncture only for chronic low back pain: 12 visits in 90 days",None)]),
]
