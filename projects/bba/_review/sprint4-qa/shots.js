const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/BBA-68-79_wireframes.html');await p.waitForTimeout(300);
fs.mkdirSync('png',{recursive:true});let n=0;
for(const s of await p.evaluate('window.WF_SCREENS'))for(const st of s.states){await p.evaluate(([a,b])=>window.showWireframe(a,b),[s.id,st]);
 const el=(await p.$('#frame .app'))||(await p.$('#frame > div'));await el.screenshot({path:`png/${s.code}--${st}.png`});n++;}
console.log('shots',n,'errors',errs);await b.close();})();
