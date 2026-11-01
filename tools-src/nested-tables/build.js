// Builds the standalone Nested Tables page from this folder:
//   node build.js            -> ../../private/nested-tables/index.html (the live page at www.threadmed.org/private/nested-tables/)
//   node build.js out.html   -> a dated copy anywhere
// Inputs: index.html (app source), js/* (libraries), seed.json (the five sample projects, pre-loaded on first run and merged into existing data by name).
const fs=require('fs'),path=require('path');
const here=__dirname; const out=process.argv[2]||path.join(here,'..','..','private','nested-tables','index.html');
let src=fs.readFileSync(path.join(here,'index.html'),'utf8');
const o=JSON.parse(fs.readFileSync(path.join(here,'seed.json'),'utf8'));
for(const [id,p] of Object.entries(o.projects)){ if(p.name==='Project 1'){ for(const [tid,t] of Object.entries(o.tables)) if(t.p===id) delete o.tables[tid]; delete o.projects[id]; delete o.curTable[id]; } }
const order=['How to use Nested Tables','Clinical logic: how reasoning works','Osteoporosis: clinical history','Hypertension: evaluation','Lipidology: decision support'];
order.forEach((n,i)=>{ const p=Object.values(o.projects).find(p=>p.name===n); if(p) p.n=i+1; });
o.cur=(Object.values(o.projects).find(p=>p.n===1)||Object.values(o.projects)[0]).id; o.fresh=false;
const libs=['js/jspdf.umd.min.js','js/jspdf.plugin.autotable.min.js','js/jszip.min.js'].map(f=>fs.readFileSync(path.join(here,f),'utf8'));
const noClose=s=>s.replace(/<\/script/gi,'<\\/script'); const b64e=t=>Buffer.from(t,'utf8').toString('base64');
const SO='<scr'+'ipt>',SC='</scr'+'ipt>';
const inject='\n'+SO+'window.__standalone=true;window.__seed='+noClose(JSON.stringify(o))+';'+SC+'\n'+libs.map((l,i)=>'<script id="ntlib'+i+'">'+noClose(l)+SC).join('\n')+'\n<script type="text/plain" id="ntsrc">'+b64e(src)+SC+'\n';
const i=src.indexOf('<body>')+6; let html=src.slice(0,i)+inject+src.slice(i);
html=html.replace('<meta charset="utf-8">','<meta charset="utf-8">\n<meta name="robots" content="noindex, nofollow">');
fs.mkdirSync(path.dirname(out),{recursive:true}); fs.writeFileSync(out,html);
const v=(src.match(/APP_VERSION='([^']+)'/)||[])[1]; console.log('built v'+v,'→',out,(html.length/1024|0)+' KB');
