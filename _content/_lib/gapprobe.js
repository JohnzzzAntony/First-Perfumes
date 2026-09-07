window.__gaps=function(detail,TH){
  TH=TH||100;
  try{ScrollTrigger.getAll().forEach(t=>t.kill())}catch(e){}
  try{ScrollSmoother.get().kill()}catch(e){}
  const w=document.querySelector('#smooth-wrapper'),c=document.querySelector('#smooth-content');
  [w,c].forEach(el=>{if(el)el.style.cssText+=';position:static!important;height:auto!important;overflow:visible!important;transform:none!important;'});
  document.querySelectorAll('.fade_anim,.text-anim,.wow,.process-card').forEach(el=>{el.style.opacity='1';el.style.transform='none';el.style.visibility='visible'});
  document.querySelectorAll('.text-anim *,.fade_anim *').forEach(el=>{el.style.opacity='1';el.style.transform='none';el.style.visibility='visible'});
  document.querySelectorAll('.right-sidebar-menu,#magic-cursor,#scroll-percentage').forEach(el=>el.style.display='none');
  const root=document.querySelector('#smooth-content')||document.body;
  const Y=window.scrollY, boxes=[];
  const push=(r,el)=>{if(r&&r.height>0&&r.width>0)boxes.push({t:r.top+Y,b:r.bottom+Y,el});};
  const vis=el=>{const cs=getComputedStyle(el);
    return !(cs.display==='none'||cs.visibility==='hidden'||cs.position==='fixed'||+cs.opacity===0);};
  // 1. real painted TEXT, via ranges over non-empty text nodes
  const tw=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode(n){
    if(!n.textContent.trim())return NodeFilter.FILTER_REJECT;
    const p=n.parentElement; if(!p||!vis(p))return NodeFilter.FILTER_REJECT;
    if(['SCRIPT','STYLE','NOSCRIPT'].includes(p.tagName))return NodeFilter.FILTER_REJECT;
    return NodeFilter.FILTER_ACCEPT;}});
  let n; while(n=tw.nextNode()){const rg=document.createRange(); rg.selectNodeContents(n);
    for(const r of rg.getClientRects())push(r,n.parentElement);}
  // 2. replaced / embedded elements
  root.querySelectorAll('img,svg,video,canvas,iframe,picture,object,embed').forEach(el=>{
    if(vis(el))push(el.getBoundingClientRect(),el);});
  // 3. painted surfaces (background colour or image)
  root.querySelectorAll('*').forEach(el=>{if(!vis(el))return;const cs=getComputedStyle(el);
    const bg=cs.backgroundColor, hasBg=bg&&bg!=='rgba(0, 0, 0, 0)'&&bg!=='transparent';
    const hasImg=(cs.backgroundImage||'none')!=='none';
    const hasBorder=parseFloat(cs.borderTopWidth)>0||parseFloat(cs.borderBottomWidth)>0;
    if(hasBg||hasImg||hasBorder)push(el.getBoundingClientRect(),el);});
  boxes.sort((a,b)=>a.t-b.t);
  const m=[];
  for(const x of boxes){
    if(m.length&&x.t<=m[m.length-1].b+1){const L=m[m.length-1]; if(x.b>L.b){L.b=x.b;L.lastEl=x.el;}}
    else m.push({t:x.t,b:x.b,firstEl:x.el,lastEl:x.el});}
  const name=el=>{if(!el)return '?'; el=el.nodeType===3?el.parentElement:el;
    const tag=el.tagName.toLowerCase()+(typeof el.className==='string'&&el.className.trim()?'.'+el.className.trim().split(/\s+/).slice(0,2).join('.'):'');
    let a=el,sec='';
    while(a&&a!==document.body){const cn=(typeof a.className==='string'?a.className:'');
      if(/-section|-page|-area/.test(cn)){sec=cn.trim().split(/\s+/)[0];break;} a=a.parentElement;}
    return sec?sec+' > '+tag:tag;};
  const gaps=[];
  for(let i=1;i<m.length;i++){const g=m[i].t-m[i-1].b;
    if(g>=TH)gaps.push({at:Math.round(m[i-1].b),px:Math.round(g),after:name(m[i-1].lastEl),before:name(m[i].firstEl)});}
  const r={docH:Math.round(document.documentElement.scrollHeight),n:gaps.length,total:gaps.reduce((s,g)=>s+g.px,0)};
  r.gaps=detail?gaps:gaps.map(g=>({at:g.at,px:g.px}));
  return r;
};
