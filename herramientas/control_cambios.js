// node tracked.js original.md corregido.md comentarios.json out.docx
const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,InsertedTextRun,DeletedTextRun,CommentRangeStart,CommentRangeEnd,CommentReference}=require('docx');
const [,,fo,fc,fj,out]=process.argv;
const L=f=>fs.readFileSync(f,'utf8').split('\n').filter(l=>l.trim());
const A=L(fo),C=L(fc);const coms=fs.existsSync(fj)?JSON.parse(fs.readFileSync(fj,'utf8')):[];
if(A.length!==C.length)throw new Error('distinto número de párrafos '+A.length+' vs '+C.length);
const AUTH='Redacción',DATE=new Date().toISOString();let rid=1;
function kind(l){if(l.startsWith('## '))return['h2',l.slice(3)];if(l.startsWith('# '))return['h1',l.slice(2)];const m=l.match(/^\*\*(.*)\*\*$/);if(m)return['sub',m[1]];return['p',l]}
function toks(s){const r=[];let it=false;s.split('*').forEach((seg,k)=>{if(k>0)it=!it;(seg.match(/\s+|[^\s]+/g)||[]).forEach(w=>r.push({raw:w+'|'+it,txt:w,it}))});return r}
function diff(a,b){const n=a.length,m=b.length,d=Array.from({length:n+1},()=>new Int32Array(m+1));
 for(let i=n-1;i>=0;i--)for(let j=m-1;j>=0;j--)d[i][j]=a[i].raw===b[j].raw?d[i+1][j+1]+1:Math.max(d[i+1][j],d[i][j+1]);
 const o=[];let i=0,j=0;while(i<n&&j<m){if(a[i].raw===b[j].raw){o.push(['=',a[i],b[j]]);i++;j++}else if(d[i+1][j]>=d[i][j+1])o.push(['-',a[i++]]);else o.push(['+',b[j++]])}
 while(i<n)o.push(['-',a[i++]]);while(j<m)o.push(['+',b[j++]]);return o}
const comments=[];let cid=0;
const kids=[];
for(let p=0;p<A.length;p++){const [ka,ta]=kind(A[p]),[kc,tc]=kind(C[p]);if(ka!==kc)throw new Error('tipo distinto en '+p);
 const base=kc==='sub'?{bold:true,color:'444444',size:26}:{};
 const ops=diff(toks(ta),toks(tc));
 // new-side plain text positions for comments
 let pos=0;const starts=[];ops.forEach((o,k)=>{if(o[0]!=='-'){const t=o[0]==='='?o[2]:o[1];starts.push([k,pos,pos+t.txt.length]);pos+=t.txt.length}});
 const plain=starts.length?ops.filter(o=>o[0]!=='-').map(o=>(o[0]==='='?o[2]:o[1]).txt).join(''):'';
 const before={},after={};
 for(const c of coms.filter(c=>c.parrafo===p)){const at=plain.indexOf(c.ancla);if(at<0){console.error('ancla no encontrada',p,c.ancla);continue}
  const e=at+c.ancla.length;const f=starts.find(s=>s[2]>at),l=[...starts].reverse().find(s=>s[1]<e);const id=cid++;
  comments.push({id,author:AUTH,date:new Date(),children:[new Paragraph({children:[new TextRun(c.texto)]})]});
  (before[f[0]]=before[f[0]]||[]).push(id);(after[l[0]]=after[l[0]]||[]).push(id)}
 const runs=[];ops.forEach((o,k)=>{(before[k]||[]).forEach(id=>runs.push(new CommentRangeStart(id)));
  const t=o[0]==='='?o[2]:o[1];const opt={text:t.txt,italics:t.it,...base};
  if(o[0]==='=')runs.push(new TextRun(opt));else if(o[0]==='+')runs.push(new InsertedTextRun({...opt,id:rid++,author:AUTH,date:DATE}));else runs.push(new DeletedTextRun({...opt,id:rid++,author:AUTH,date:DATE}));
  (after[k]||[]).forEach(id=>{runs.push(new CommentRangeEnd(id));runs.push(new TextRun({children:[new CommentReference(id)]}))})});
 if(kc==='h1')kids.push(new Paragraph({heading:HeadingLevel.TITLE,children:runs}));else if(kc==='h2')kids.push(new Paragraph({heading:HeadingLevel.HEADING_1,children:runs}));else kids.push(new Paragraph({spacing:{after:200,line:300},children:runs}))}
const F='Georgia';
const doc=new Document({comments:{children:comments},styles:{default:{document:{run:{font:F,size:24}}},paragraphStyles:[
{id:'Title',name:'Title',basedOn:'Normal',run:{size:40,bold:true,font:F},paragraph:{spacing:{after:160}}},
{id:'Heading1',name:'Heading 1',basedOn:'Normal',next:'Normal',quickFormat:true,run:{size:28,bold:true,font:F,color:'9B2C2C'},paragraph:{spacing:{before:320,after:140},outlineLevel:0}}]},
sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1440,right:1440,bottom:1440,left:1440}}},children:kids}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync(out,b);console.log('ok',comments.length,'comentarios',rid-1,'cambios')});
