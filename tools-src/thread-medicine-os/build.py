"""Build tools/thread-medicine-os.html from the node graph. Run: python3 build.py"""
import json, os
here = os.path.dirname(os.path.abspath(__file__)); os.chdir(here)
from nodes import N, n
ns = {}
exec(open('modules.py').read(), ns)          # function-module rows and grades
FT = {'fn-fall':[('fn-bone','falls cause most fractures'),('fn-vis','vision'),('risky-drugs','fall-risk drugs'),('frax','FRAX omits falls'),('rehab','exercise')],
'fn-bone':[('frax','baseline risk'),('impact-chain','predicted effect of treatment'),('time-to-benefit','about 12 months'),('m-structure','matrix element'),('care-models','fracture liaison service'),('fn-fall','falls')],
'fn-musc':[('competing-risk','frailty changes the horizon'),('m-energy','matrix element'),('rehab','resistance training'),('fn-fall','weakness and falls')],
'fn-cog':[('neuro','disease lane'),('fn-hear','hearing'),('fn-vis','vision'),('care-models','dementia navigation'),('risky-drugs','anticholinergics')],
'fn-hear':[('fn-cog','cognition'),('procedures','hearing aids')],
'fn-vis':[('fn-fall','falls'),('procedures','cataract surgery')],
'fn-mood':[('psychological','therapies'),('care-models','collaborative care'),('m-mind','matrix element')],
'fn-rest':[('allostasis','stress physiology'),('risky-drugs','sedatives'),('social','connection'),('psychological','CBT for insomnia')],
'fn-pain':[('acupuncture','where its evidence sits'),('rehab','exercise'),('fn-fall','mobility')]}
for mid, name, screen, rows in ns['domains']:
    i = 'fn-' + mid.split('.')[1].lower()
    n(i, name, 'Function module \u00b7 ' + mid, 'Screen: ' + screen + '.', l=FT[i], w='grades')
    N[i]['g'] = [[r[0], r[1], r[2], bool(r[3]) if len(r) > 3 else False] for r in rows]
for i, v in N.items():                        # every child and thread must exist
    for c in v['c']: assert c in N, (i, c)
    for t, _ in v['l']: assert t in N, (i, t)
reach, st = set(), ['os']
while st:
    x = st.pop()
    if x in reach: continue
    reach.add(x); st += N[x]['c']
assert reach == set(N), set(N) - reach       # no orphan nodes
out = open('explorer.html').read().replace('/*NODES*/', json.dumps(N, ensure_ascii=False)).replace('<!--CONTROLSVG-->', open('control.svg').read())
open('../../tools/thread-medicine-os.html', 'w').write(out)
print(len(N), 'nodes ->', 'tools/thread-medicine-os.html')
