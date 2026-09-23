from pathlib import Path
from html import escape
import re
root=Path('/mnt/data/professional_site')
css='''
:root{--bg:#07111f;--surface:#0c1a2b;--surface2:#102238;--line:rgba(255,255,255,.09);--text:#f4f8ff;--muted:#9fb0c7;--primary:#5eead4;--primary2:#60a5fa;--shadow:0 24px 70px rgba(0,0,0,.35)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:radial-gradient(circle at 15% 0%,#123052 0,transparent 34%),radial-gradient(circle at 90% 15%,#162a4d 0,transparent 30%),linear-gradient(135deg,#06101d,#081321 55%,#07111f);min-height:100vh}a{color:inherit}.top{position:sticky;top:0;z-index:50;background:rgba(5,14,25,.82);backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}.nav{max-width:1240px;margin:auto;padding:15px 24px;display:flex;align-items:center;justify-content:space-between;gap:18px}.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:850;letter-spacing:-.02em}.brand-mark{width:36px;height:36px;display:grid;place-items:center;border-radius:11px;background:linear-gradient(135deg,var(--primary),var(--primary2));color:#06101d;box-shadow:0 8px 28px rgba(96,165,250,.25)}.links{display:flex;gap:8px;flex-wrap:wrap}.links a{padding:9px 13px;border:1px solid transparent;border-radius:10px;text-decoration:none;color:#c8d5e7;font-size:.9rem}.links a:hover{background:rgba(255,255,255,.06);border-color:var(--line);color:#fff}
main{max-width:1240px;margin:auto;padding:54px 24px 70px}.hero{padding:8px 0 34px}.eyebrow{display:inline-flex;align-items:center;gap:8px;padding:7px 11px;border:1px solid rgba(94,234,212,.2);border-radius:999px;background:rgba(94,234,212,.06);color:#8ff6e6;font-size:.75rem;font-weight:800;text-transform:uppercase;letter-spacing:.12em}.eyebrow:before{content:"";width:6px;height:6px;border-radius:50%;background:var(--primary);box-shadow:0 0 14px var(--primary)}h1{font-size:clamp(2.25rem,6vw,4.8rem);line-height:1.02;letter-spacing:-.055em;margin:18px 0 16px;max-width:950px}h2{letter-spacing:-.025em}p{color:var(--muted);line-height:1.75}.hero p{max-width:820px;font-size:1.05rem}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}.card{position:relative;background:linear-gradient(145deg,rgba(16,34,56,.96),rgba(9,23,39,.96));border:1px solid var(--line);border-radius:22px;padding:24px;box-shadow:var(--shadow);transition:.25s ease}.card:hover{transform:translateY(-5px);border-color:rgba(94,234,212,.32)}.card h2{margin:13px 0 8px}.badge{display:inline-flex;padding:6px 10px;border-radius:999px;background:rgba(96,165,250,.1);color:#a9c9ff;font-size:.78rem;font-weight:800}.btn{display:inline-flex;align-items:center;gap:8px;margin-top:15px;padding:11px 15px;border-radius:11px;background:linear-gradient(135deg,var(--primary),var(--primary2));color:#06101d;text-decoration:none;font-weight:850;border:0;cursor:pointer}.btn.alt{background:rgba(255,255,255,.06);color:#e7eef9;border:1px solid var(--line)}
.list{display:grid;gap:10px}.item{display:flex;align-items:center;gap:14px;padding:15px 17px;border:1px solid var(--line);border-radius:15px;background:rgba(255,255,255,.025);text-decoration:none;transition:.2s}.item:hover{background:rgba(94,234,212,.055);border-color:rgba(94,234,212,.25);transform:translateX(3px)}.num{flex:0 0 36px;width:36px;height:36px;border-radius:10px;display:grid;place-items:center;background:rgba(96,165,250,.1);color:#b8d4ff;font-weight:850;font-size:.82rem}.item span:last-child{line-height:1.45;color:#d8e2ef}
.demo{margin-top:24px;padding:28px;border:1px solid var(--line);border-radius:24px;background:linear-gradient(145deg,rgba(16,34,56,.82),rgba(7,18,31,.9));box-shadow:var(--shadow)}.demo h2{margin-bottom:6px}.controls{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}.input,select,textarea{width:auto;background:#081624;color:#f4f8ff;border:1px solid var(--line);border-radius:11px;padding:11px 13px;outline:none}.input:focus,select:focus,textarea:focus{border-color:rgba(94,234,212,.6)}.output{margin-top:15px;padding:16px;border-radius:13px;background:#06111e;border:1px solid var(--line);min-height:48px;color:#dce8f6}.table{width:100%;border-collapse:collapse}.table th,.table td{border:1px solid var(--line);padding:10px;text-align:left}.pill{display:inline-block;padding:7px 11px;border-radius:999px;background:rgba(255,255,255,.06)}.success{color:#7ff0c0}.danger{color:#ff9aaa}.center{text-align:center}.footer{max-width:1240px;margin:10px auto 0;padding:28px 24px 40px;text-align:center;color:#71839c;border-top:1px solid var(--line)}
.section-head{display:flex;align-items:end;justify-content:space-between;gap:20px;margin-bottom:22px}.section-head p{margin:0}.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:8px 0 30px}.stat{padding:18px;border:1px solid var(--line);border-radius:16px;background:rgba(255,255,255,.025)}.stat strong{display:block;font-size:1.5rem;margin-bottom:4px}.stat span{font-size:.82rem;color:var(--muted)}.question{padding:22px 24px;margin-bottom:20px;border:1px solid rgba(94,234,212,.15);background:linear-gradient(135deg,rgba(94,234,212,.055),rgba(96,165,250,.045));border-radius:20px}.question-label{font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:#83e8dc;font-weight:850}.question h2{font-size:1.25rem;line-height:1.5;margin:9px 0 0}.backbar{display:flex;justify-content:space-between;gap:12px;align-items:center;margin-bottom:22px}.backbar a{text-decoration:none;color:#a9c1dc;font-size:.9rem}.backbar a:hover{color:#fff}
@media(max-width:720px){.nav{padding:13px 16px;align-items:flex-start;flex-direction:column}.links{width:100%}.links a{flex:1;text-align:center}.links a:first-child{flex:0 0 auto}main{padding:36px 16px 55px}h1{font-size:clamp(2.1rem,12vw,3.5rem)}.stat-row{grid-template-columns:1fr}.card{padding:20px}.demo{padding:20px}.item{align-items:flex-start}.num{margin-top:1px}}
'''
(root/'shared/style.css').write_text(css,encoding='utf-8')

# Add a polished brand mark to every page and upgrade program pages without exposing source code.
for p in root.rglob('*.html'):
    if p.name=='index.html' and p.parent==root: continue
    s=p.read_text(encoding='utf-8')
    s=s.replace('<a class="brand" href="', '<a class="brand" href="')
    s=re.sub(r'<a class="brand" href="([^"]+)">⚡ Practical Lab</a>', r'<a class="brand" href="\1"><span class="brand-mark">&lt;/&gt;</span><span>Practical Lab</span></a>', s)
    # Remove any source/code sections if present in any future variant.
    s=re.sub(r'<(?:pre|code)[^>]*>.*?</(?:pre|code)>','',s,flags=re.S|re.I)
    s=re.sub(r'<[^>]*>\s*(?:Source Code|Copy Code)\s*</[^>]*>','',s,flags=re.I)
    p.write_text(s,encoding='utf-8')

# Improve main dashboard.
(root/'index.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Practical Lab | HTML CSS JavaScript</title><link rel="stylesheet" href="shared/style.css"></head><body>
<header class="top"><nav class="nav"><a class="brand" href="index.html"><span class="brand-mark">&lt;/&gt;</span><span>Practical Lab</span></a><div class="links"><a href="html/index.html">HTML</a><a href="css/index.html">CSS</a><a href="javascript/index.html">JavaScript</a></div></nav></header>
<main><section class="hero"><span class="eyebrow">Academic Practical Laboratory</span><h1>HTML, CSS &amp; JavaScript<br>Practical Programs</h1><p>A professional, browser-ready practical laboratory for your complete assignment. Explore each experiment separately, view the working demonstration, and navigate between sections without exposing source code on the website.</p></section>
<div class="stat-row"><div class="stat"><strong>15</strong><span>HTML Experiments</span></div><div class="stat"><strong>270</strong><span>CSS Experiments</span></div><div class="stat"><strong>270</strong><span>JavaScript Experiments</span></div></div>
<div class="grid"><a class="card" href="html/index.html"><span class="badge">15 Experiments</span><h2>HTML Laboratory</h2><p>Foundations, lists, tables, forms, media, semantic HTML, input types, timetables and portfolio design.</p><span class="btn">Explore HTML →</span></a><a class="card" href="css/index.html"><span class="badge">270 Experiments</span><h2>CSS Laboratory</h2><p>Core CSS, UI components, responsive layouts, dashboards, AI/ML interfaces and modern SaaS projects.</p><span class="btn">Explore CSS →</span></a><a class="card" href="javascript/index.html"><span class="badge">270 Experiments</span><h2>JavaScript Laboratory</h2><p>Programming fundamentals, DOM, events, validation, browser features, storage and practical mini projects.</p><span class="btn">Explore JavaScript →</span></a></div>
<section class="demo"><div class="section-head"><div><span class="eyebrow">Student Submission</span><h2>Practical Record</h2></div></div><div class="grid"><div class="card"><span class="badge">Student</span><h2>B.Meganadh Reddy</h2><p>Register Number: 250200531</p></div><div class="card"><span class="badge">Class / Section</span><h2>6</h2><p>Subject: HTML, CSS &amp; JavaScript</p></div><div class="card"><span class="badge">Experience</span><h2>Offline Ready</h2><p>Open <strong>index.html</strong> directly in a browser. No server is required.</p></div></div></section></main>
<footer class="footer">HTML • CSS • JavaScript Practical Laboratory<br><span>Designed as a clean academic submission portal</span></footer></body></html>''',encoding='utf-8')

# Fix category index copy/counts and add search box to large lists.
for p in [root/'css/index.html', root/'javascript/index.html']:
    s=p.read_text(encoding='utf-8')
    s=s.replace('269 separate experiments','270 separate experiments').replace('269 programs','270 programs')
    marker='<div class="list">'
    if marker in s:
        s=s.replace(marker,'<div class="controls"><input class="input" id="search" placeholder="Search experiments..." oninput="filterExperiments()"></div><div class="list" id="experimentList">',1)
        s=s.replace('</div><div class="footer"><a href="../index.html">Home</a></div>', '</div><div class="footer"><a href="../index.html">Home</a></div>',1)
        s=s.replace('</div></main></body></html>', '</div><script>function filterExperiments(){const q=document.getElementById("search").value.toLowerCase();document.querySelectorAll("#experimentList .item").forEach(e=>e.style.display=e.innerText.toLowerCase().includes(q)?"flex":"none")}</script></main></body></html>',1)
    p.write_text(s,encoding='utf-8')

# Program pages: turn existing hero into explicit question panel and add navigation polish.
for p in root.rglob('*.html'):
    if p in [root/'index.html'] or p.name=='index.html': continue
    s=p.read_text(encoding='utf-8')
    # Find h1 and convert its containing hero heading into a question panel while keeping demo.
    m=re.search(r'<div class="hero"><span class="eyebrow">(.*?)</span><h1>(.*?)</h1><p>(.*?)</p></div>',s,re.S)
    if m:
        eyebrow,h1,desc=m.groups()
        desc=re.sub(r'\s*This page contains.*','',desc,flags=re.I)
        replacement=f'<div class="backbar"><a href="../../index.html">← Home</a><a href="index.html">Back to section →</a></div><div class="question"><div class="question-label">{eyebrow}</div><h2>{h1}</h2><p>{desc}</p></div>'
        s=s[:m.start()]+replacement+s[m.end():]
    p.write_text(s,encoding='utf-8')
