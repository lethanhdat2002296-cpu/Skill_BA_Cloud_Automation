const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const R=process.argv[2];
for(let t=68;t<=79;t++){const errs=[];p.removeAllListeners('pageerror');p.on('pageerror',e=>errs.push(e.message));
 await p.goto(`file://${R}/by-frd/BBA-${t}/wireframe.html`);await p.waitForTimeout(150);
 const s=await p.evaluate('window.WF_SCREENS.map(x=>x.id+":"+x.states.join("/")).join(" ")');console.log(t,s,errs.length?errs:'');}
await b.close();})();
