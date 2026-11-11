/* Pendamping Akademik — Navigasi pembelajaran tanpa dependensi eksternal */
(function(){
'use strict';
const data=window.PA_MATERI;
const page=document.getElementById('page'), toc=document.getElementById('toc');
if(!data || !Array.isArray(data.chapters)){page.innerHTML='<p>Data materi belum dimuat. Pastikan materi.js ada pada folder yang sama dengan index.html.</p>';return;}
const key='pa-matematika-umum-xii-v1';
function load(){try {return JSON.parse(localStorage.getItem(key))||{}}catch(_){return {}}}
let st={done:[],seen:[],last:null,answers:{},...load()};
if(!Array.isArray(st.done)) st.done=[];
if(!Array.isArray(st.seen)) st.seen=[];
if(!st.answers || typeof st.answers!=='object') st.answers={};
function save(){try {localStorage.setItem(key,JSON.stringify(st))}catch(_){}}
const all=[];
data.chapters.forEach((c,ci)=>c.sections.forEach((s,si)=>s.lessons.forEach((l,li)=>all.push({c,ci,s,si,l,li}))));
const $=(tag,classes,text)=>{const e=document.createElement(tag);if(classes)e.className=classes;if(text!==undefined)e.textContent=text;return e};
const append=(p,...children)=>{children.filter(Boolean).forEach(ch=>p.appendChild(ch));return p};
const linkBtn=(label,hash,css='btn btn-ghost')=>{const b=$('button',css,label);b.type='button';b.addEventListener('click',()=>navigate(hash));return b};
function addPara(p,content,cls){return append(p,$('p',cls,content))}
function hashForLesson(x){return '#materi-'+x.l.id}
function findLesson(id){return all.find(x=>x.l.id===id)}
function navigate(hash){if(location.hash===hash){render();window.scrollTo({top:0,behavior:'smooth'})}else location.hash=hash}
function getRoute(){const h=decodeURIComponent(location.hash||'');if(h==='#beranda'||!h)return {type:'home'};let m=h.match(/^#bab-(\d+)$/);if(m&&+m[1]>=1&&+m[1]<=4)return {type:'chapter',ci:+m[1]-1};m=h.match(/^#materi-(\d+-\d+-\d+)$/);if(m&&findLesson(m[1]))return {type:'lesson',x:findLesson(m[1])};return {type:'home'}}
function updateProgress(){const count=all.filter(x=>st.done.includes(x.l.id)).length;document.getElementById('progressText').textContent=`${count} dari ${all.length} materi selesai`;
 const t=document.getElementById('progressTrack'),f=document.getElementById('progressFill');t.setAttribute('aria-valuenow',String(Math.round(count/all.length*100)));f.style.width=(count/all.length*100)+'%';}
function makeToc(query=''){
 toc.replaceChildren();let matches=0;const q=query.toLocaleLowerCase('id-ID').trim();
 data.chapters.forEach((c,ci)=>{
  const holder=$('div','toc-chap');const btn=$('button','toc-chapter',`BAB ${ci+1} · ${c.title}`);btn.type='button';btn.addEventListener('click',()=>navigate('#bab-'+(ci+1)));holder.append(btn);
  let chapHas=false;
  c.sections.forEach((s,si)=>{
   const relevant=s.lessons.filter(l=>!q||[c.title,s.title,l.title,l.explain,l.analogy,l.subtopics.join(' ')].join(' ').toLocaleLowerCase('id-ID').includes(q));
   if(!relevant.length)return;chapHas=true;const sec=$('div','toc-section');const sbtn=$('button','toc-section-btn',`${ci+1}.${si+1} ${s.title}`);sbtn.type='button';sbtn.addEventListener('click',()=>navigate('#materi-'+relevant[0].id));sec.append(sbtn);
   relevant.forEach(l=>{matches++;const b=$('button','toc-lesson',`${l.code} ${l.title}`);b.type='button';b.dataset.id=l.id;if(st.done.includes(l.id))b.classList.add('done');else if(st.seen.includes(l.id))b.classList.add('viewed');b.addEventListener('click',()=>navigate('#materi-'+l.id));sec.append(b)});holder.append(sec);
  });
  if(chapHas||!q)toc.append(holder);
 });
 document.getElementById('searchCount').textContent=q?`${matches} materi sesuai pencarian`: 'Hijau = selesai · Titik emas = pernah dibuka';
 if(matches===0 && q)toc.append($('p','empty-result','Tidak ada hasil. Coba kata kunci lain.'));
 const route=getRoute();if(route.type==='lesson')toc.querySelectorAll('.toc-lesson').forEach(b=>b.classList.toggle('active',b.dataset.id===route.x.l.id));
}
function breadcrumbs(items){const d=$('div','breadcrumb');items.forEach((x,i)=>{if(i)d.append($('span',null,'/'));d.append(x.hash?linkBtn(x.label,x.hash,'crumb'):$('span',null,x.label))});return d}
function firstLesson(ci){return '#materi-'+data.chapters[ci].sections[0].lessons[0].id}
function renderHome(){
 const box=$('article','panel');box.append($('p','kicker','PETA BELAJAR LENGKAP'));
 box.append($('h2',null,'Daftar Isi Matematika Umum XII'));
 addPara(box,'Buka bab sesuai urutan jika baru belajar dari awal. Setiap bab terdiri atas pembahasan sederhana, contoh langkah demi langkah, pertanyaan C2, tantangan C4, dan proyek PjBL.');
 const cards=$('div','chapter-list');data.chapters.forEach((c,ci)=>{
 const b=$('button','chapter-card');b.type='button';const im=$('img');im.src=c.image;im.alt='Foto nyata terkait '+c.title;im.loading='lazy';im.onerror=()=>im.remove();b.append(im,$('small',null,`BAB ${ci+1} • ${c.sections.length} SUBBAB • ${c.sections.length*2} MATERI`),$('strong',null,c.title),$('small',null,c.overview));b.addEventListener('click',()=>navigate('#bab-'+(ci+1)));cards.append(b)
 });box.append(cards);
 const info=$('div','concept');info.append($('h3',null,'Cara menggunakan halaman ini'));const ul=$('ol');[
 'Pilih BAB, lalu Subbab dan Materi pada daftar isi.','Baca penjelasan dan contoh yang dijabarkan satu langkah demi satu langkah.','Jawab pertanyaan Memahami (C2). Coba sampai benar; baca pembahasan yang muncul.','Kerjakan tantangan analisis (C4) pada akhir subbab dan proyek (C5) pada setiap bab.','Klik “Tandai selesai” untuk menyimpan kemajuan di perangkat ini.'
 ].forEach(t=>ul.append($('li',null,t)));info.append(ul);box.append(info);
 box.append(linkBtn('Mulai dari Materi 1.1.1',firstLesson(0),'btn btn-primary'));return box;
}
function renderChapter(ci){const c=data.chapters[ci],card=$('article','panel');card.append(breadcrumbs([{label:'Daftar isi',hash:'#beranda'},{label:'Bab '+(ci+1)}]));card.append($('p','kicker',`BAB ${ci+1} · MATEMATIKA UMUM`),$('h2',null,c.title));const im=$('img','chapter-photo');im.src=c.image;im.alt='Foto realistis untuk bab '+c.title;im.loading='lazy';im.onerror=()=>im.remove();card.append(im,$('p','photo-credit',c.credit));addPara(card,c.overview);const note=$('div','chapter-overview');note.append($('strong',null,'Garis besar yang perlu dipahami'));addPara(note,c.essential);card.append(note);
 card.append($('h3',null,'Daftar subbab dan materi'));const index=$('div','section-index');c.sections.forEach((s,si)=>{const d=$('div');d.append($('strong',null,`${ci+1}.${si+1} · ${s.title}`));const ol=$('ol');s.lessons.forEach(l=>{const li=$('li');const b=$('button',null,`${l.code} ${l.title}`);b.type='button';b.addEventListener('click',()=>navigate('#materi-'+l.id));li.append(b);ol.append(li)});d.append(ol);index.append(d)});card.append(index);
 const p=$('div','project');p.append($('h3',null,c.project));const ul=$('ol');c.project_steps.forEach(a=>ul.append($('li',null,a)));p.append(ul);card.append(p);
 const nav=$('div','nav-row');if(ci>0)nav.append(linkBtn('Bab sebelumnya','#bab-'+ci));nav.append(linkBtn('Mulai materi bab ini',firstLesson(ci),'btn btn-primary'));if(ci<3)nav.append(linkBtn('Bab berikutnya','#bab-'+(ci+2)));card.append(nav);return card;
}
function concept(title,content,tag='p'){const a=$('div','concept');a.append($('h3',null,title),$(tag,null,content));return a}
function renderLesson(x){
 const {c,ci,s,si,l}=x;st.last=l.id;if(!st.seen.includes(l.id))st.seen.push(l.id);save();
 const article=$('article','panel');article.append(breadcrumbs([{label:'Daftar isi',hash:'#beranda'},{label:'Bab '+(ci+1),hash:'#bab-'+(ci+1)},{label:`Subbab ${ci+1}.${si+1}`,hash:'#bab-'+(ci+1)},{label:`Materi ${l.code}`} ]));
 article.append($('p','kicker',`BAB ${ci+1} · ${c.title.toUpperCase()}`));article.append($('h2',null,`${l.code} · ${l.title}`),$('p','section-subtitle',`Subbab ${ci+1}.${si+1}: ${s.title}`));
 const lead=$('div','topic-lead');lead.append($('strong',null,'Pelajari perlahan: '));lead.append(document.createTextNode(s.goal));article.append(lead);
 article.append($('h3',null,'Apa yang akan dipahami?'));const ul=$('ul','subtopics');l.subtopics.forEach(z=>ul.append($('li',null,z.trim())));article.append(ul);
 article.append(concept('Penjelasan dengan bahasa sederhana',l.explain));article.append(concept('Bayangkan dalam kehidupan sehari-hari',l.analogy));
 const formula=$('div','formula');formula.append($('span',null,'RUMUS / IDE KUNCI'));formula.append($('div',null,l.formula));article.append(formula);
 const example=$('section','example');example.append($('span','pill-level','C3 • MENGGUNAKAN'),$('h3',null,'Contoh soal dengan langkah lengkap'),$('p',null,l.example.problem));const ol=$('ol','steps');l.example.steps.forEach(t=>ol.append($('li',null,t)));example.append(ol,$('div','answer','Jawaban: '+l.example.answer));article.append(example);
 const quiz=$('section','quiz');quiz.append($('span','pill-level','C2 • MEMAHAMI'),$('h3',null,'Uji pemahaman singkat'),$('p',null,l.check.question));const choices=$('div');const feedback=$('div','quiz-feedback');const current=st.answers[l.id];
 function selectChoice(chosen){st.answers[l.id]=chosen;save();const correct=chosen===l.check.correct;choices.querySelectorAll('button').forEach((b,j)=>{b.disabled=true;b.classList.toggle('correct',j===l.check.correct);b.classList.toggle('wrong',j===chosen&&!correct)});feedback.className='quiz-feedback '+(correct?'ok':'no');feedback.textContent=(correct?'Benar. ':'Belum tepat. ')+l.check.feedback;}
 l.check.options.forEach((t,j)=>{const b=$('button','choice',`${String.fromCharCode(65+j)}. ${t}`);b.type='button';b.addEventListener('click',()=>selectChoice(j));choices.append(b)});quiz.append(choices,feedback);article.append(quiz);if(typeof current==='number')selectChoice(current);
 article.append($('div','trap','Perhatikan: '+l.trap));
 if(x.li===1){const challenge=$('div','challenge');challenge.append($('strong',null,`C4 • ANALISIS SUBBAB ${ci+1}.${si+1}`),$('p',null,s.c4));article.append(challenge)}
 const idx=all.findIndex(e=>e.l.id===l.id);const end=$('div','end-actions');const completed=$('span','done-status');const doneBtn=$('button','btn btn-primary');function doneState(){const ok=st.done.includes(l.id);doneBtn.textContent=ok?'Batalkan tanda selesai':'Tandai materi selesai';completed.textContent=ok?'Materi ini sudah ditandai selesai.':'Kemajuan disimpan di perangkat ini.'}
 doneBtn.type='button';doneBtn.addEventListener('click',()=>{if(st.done.includes(l.id))st.done=st.done.filter(id=>id!==l.id);else st.done.push(l.id);save();updateProgress();makeToc(document.getElementById('searchInput').value);doneState()});doneState();end.append(doneBtn,completed,linkBtn('Daftar bab','#beranda'));
 article.append(end);
 const nav=$('div','nav-row');nav.append(idx>0?linkBtn('Sebelumnya: '+all[idx-1].l.title,hashForLesson(all[idx-1])):linkBtn('Kembali ke Bab 1','#bab-1'));
 if(idx<all.length-1)nav.append(linkBtn('Lanjut: '+all[idx+1].l.title,hashForLesson(all[idx+1]),'btn btn-secondary'));else nav.append(linkBtn('Selesai • Lihat daftar bab','#beranda','btn btn-secondary'));
 article.append(nav);
 if(x.li===1){const sub=$('div','concept');sub.append($('h3',null,'Rangkuman subbab'),$('p',null,s.goal+' Renungkan kembali pertanyaan analisis C4, lalu jelaskan dengan kata-katamu sendiri kepada orang lain.'));article.append(sub)}
 if(x.li===1 && si===c.sections.length-1){const proj=$('div','project');proj.append($('h3',null,'C5 • Evaluasi dan proyek: '+c.project));const olp=$('ol');c.project_steps.forEach(t=>olp.append($('li',null,t)));proj.append(olp);article.append(proj)}
 return article;
}
function closeDrawer(){document.querySelector('.sidebar').classList.remove('open');document.getElementById('sidebarBackdrop').hidden=true}
function render(){const route=getRoute();page.replaceChildren(route.type==='home'?renderHome():route.type==='chapter'?renderChapter(route.ci):renderLesson(route.x));updateProgress();makeToc(document.getElementById('searchInput').value);closeDrawer();document.title=(route.type==='lesson'?route.x.l.title+' | ':route.type==='chapter'?data.chapters[route.ci].title+' | ':'')+'Matematika Umum XII — Pendamping Akademik';window.scrollTo({top:0,behavior:'instant'});}
function sourceList(){const container=document.getElementById('sources');container.replaceChildren();const refs=$('ul','source-list');[...data.sources,...data.photos.map(p=>({name:'Foto: '+p.credit,url:p.url}))].forEach(s=>{const a=$('a',null,s.name);a.href=s.url;a.target='_blank';a.rel='noopener noreferrer';refs.append(append($('li'),a))});container.append(refs)}
sourceList();document.getElementById('homeBtn').addEventListener('click',()=>navigate('#beranda'));
document.getElementById('resumeBtn').addEventListener('click',()=>navigate(st.last?'#materi-'+st.last:firstLesson(0)));
document.getElementById('searchInput').addEventListener('input',e=>makeToc(e.target.value));
document.getElementById('sidebarOpen').addEventListener('click',()=>{document.querySelector('.sidebar').classList.add('open');document.getElementById('sidebarBackdrop').hidden=false;document.getElementById('searchInput').focus()});
document.getElementById('sidebarClose').addEventListener('click',closeDrawer);document.getElementById('sidebarBackdrop').addEventListener('click',closeDrawer);
window.addEventListener('hashchange',render);render();
})();
