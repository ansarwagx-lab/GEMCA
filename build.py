#!/usr/bin/env python3
"""Build complete GEMCA website — single self-contained index.html"""

# ── helper functions ────────────────────────────────────────────────────────

def acc(title, badge_cls, badge_txt, desc, reqs, fee, proc, work, dur, pathway):
    req_html = "".join(f'<li>{r}</li>' for r in reqs)
    return f"""
<div class="acc-item">
  <button class="acc-hdr" onclick="toggleAcc(this)" aria-expanded="false">
    <span class="acc-title">{title}</span>
    <div class="acc-hdr-right">
      <span class="visa-badge {badge_cls}">{badge_txt}</span>
      <span class="acc-icon" aria-hidden="true">+</span>
    </div>
  </button>
  <div class="acc-body" role="region">
    <div class="acc-inner">
      <p class="acc-desc">{desc}</p>
      <ul class="req-list">{req_html}</ul>
      <div class="meta-row">
        <div class="meta-item"><span class="meta-label">Fee</span><span class="meta-val">{fee}</span></div>
        <div class="meta-item"><span class="meta-label">Processing</span><span class="meta-val">{proc}</span></div>
        <div class="meta-item"><span class="meta-label">Work Rights</span><span class="meta-val">{work}</span></div>
        <div class="meta-item"><span class="meta-label">Duration</span><span class="meta-val">{dur}</span></div>
        <div class="meta-item"><span class="meta-label">Pathway To</span><span class="meta-val">{pathway}</span></div>
      </div>
      <div class="acc-ctas">
        <a href="#assessment" class="btn-primary btn-sm">Book Free Assessment</a>
        <a href="#contact" class="btn-outline btn-sm">Ask a Question</a>
      </div>
    </div>
  </div>
</div>"""

def uni_grid(unis):
    cards = "".join(f'<div class="uni-card">{u}</div>' for u in unis)
    return f'<div class="uni-grid">{cards}</div>'

def country_panel(code, flag, name, intro, s1, s2, s3, visas_html, unis):
    return f"""
<div class="tab-panel" data-panel="{code}" {"" if code!="au" else 'style="display:block"'}>
  <div class="country-banner">
    <div class="country-banner-inner">
      <div class="country-flag-big">{flag}</div>
      <div>
        <h3 class="country-name">{name}</h3>
        <p class="country-intro">{intro}</p>
      </div>
      <div class="country-stats">
        <div class="c-stat"><span class="c-stat-n">{s1[0]}</span><span class="c-stat-l">{s1[1]}</span></div>
        <div class="c-stat"><span class="c-stat-n">{s2[0]}</span><span class="c-stat-l">{s2[1]}</span></div>
        <div class="c-stat"><span class="c-stat-n">{s3[0]}</span><span class="c-stat-l">{s3[1]}</span></div>
      </div>
    </div>
  </div>
  <div class="visa-accordions">{visas_html}</div>
  <div class="unis-section">
    <h4 class="unis-title">Partner Universities &amp; Institutions</h4>
    {uni_grid(unis)}
  </div>
</div>"""

# ── CSS ─────────────────────────────────────────────────────────────────────
CSS = """
:root{
  --bg:#060e1e;--navy:#0B2A6B;--sapphire:#1a5fb4;
  --gold:#C8A96E;--gold-l:#E2C48A;--gold-d:#a07840;
  --glass:rgba(6,14,30,.78);--glass-b:rgba(200,169,110,.17);
  --glass-bh:rgba(200,169,110,.45);
  --text:rgba(255,255,255,.88);--muted:rgba(255,255,255,.52);--faint:rgba(255,255,255,.28);
  --font-d:'Cormorant Garamond',Georgia,serif;
  --font-b:'DM Sans',system-ui,sans-serif;
  --ease:cubic-bezier(.4,0,.2,1);
  --r:16px;--rs:10px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:82px}
body{background:var(--bg);color:var(--text);font-family:var(--font-b);font-size:16px;line-height:1.65;overflow-x:hidden;-webkit-font-smoothing:antialiased}
::selection{background:rgba(200,169,110,.28)}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
button{background:none;border:none;cursor:pointer;font-family:inherit}
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:rgba(200,169,110,.35);border-radius:3px}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}}

/* ── AURORA ── */
.aurora{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.aurora::before{content:'';position:absolute;inset:0;
  background-image:linear-gradient(rgba(200,169,110,.022) 1px,transparent 1px),linear-gradient(90deg,rgba(200,169,110,.022) 1px,transparent 1px);
  background-size:72px 72px}
.orb{position:absolute;border-radius:50%;filter:blur(130px);animation:drift 42s ease-in-out infinite}
.orb-1{width:820px;height:680px;background:radial-gradient(ellipse,rgba(11,42,107,.52) 0%,transparent 70%);top:-260px;left:-180px;animation-delay:0s}
.orb-2{width:640px;height:560px;background:radial-gradient(ellipse,rgba(200,169,110,.055) 0%,transparent 70%);top:45%;right:-220px;animation-delay:-16s}
.orb-3{width:560px;height:480px;background:radial-gradient(ellipse,rgba(6,24,80,.68) 0%,transparent 70%);bottom:-80px;left:28%;animation-delay:-30s}
@keyframes drift{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(16px,-16px) scale(1.03)}66%{transform:translate(-12px,12px) scale(.97)}}

/* ── LAYOUT ── */
.container{max-width:1280px;margin:0 auto;padding:0 clamp(1rem,4vw,2.5rem)}
section{padding:clamp(4.5rem,9vw,9rem) 0}
.section-header{text-align:center;margin-bottom:4rem}
.section-eyebrow{font-family:var(--font-b);font-size:11px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);margin-bottom:.85rem;display:block}
.section-title{font-family:var(--font-d);font-size:clamp(2.1rem,4.5vw,3.4rem);font-weight:300;line-height:1.12;color:#fff}
.section-title em{font-style:italic;color:var(--gold)}
.section-sub{max-width:560px;margin:1.1rem auto 0;color:var(--muted);font-size:1.05rem}
.gold-divider{width:64px;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:1.5rem auto 0}

/* ── GLASS CARD ── */
.glass-card{background:var(--glass);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--glass-b);border-radius:var(--r);transition:border-color .35s var(--ease),transform .35s var(--ease),box-shadow .35s var(--ease)}
.glass-card:hover{border-color:var(--glass-bh);transform:translateY(-6px);box-shadow:0 24px 64px rgba(0,0,0,.45),0 0 0 1px rgba(200,169,110,.08)}

/* ── BUTTONS ── */
.btn-primary{display:inline-flex;align-items:center;gap:.55rem;background:linear-gradient(135deg,var(--gold),var(--gold-l));color:#060e1e;font-family:var(--font-b);font-size:14px;font-weight:700;letter-spacing:.06em;padding:.82rem 1.9rem;border-radius:var(--rs);border:none;cursor:pointer;transition:transform .28s var(--ease),box-shadow .28s var(--ease);text-decoration:none}
.btn-primary:hover{transform:translateY(-3px);box-shadow:0 12px 36px rgba(200,169,110,.38)}
.btn-outline{display:inline-flex;align-items:center;gap:.55rem;background:transparent;color:#fff;font-family:var(--font-b);font-size:14px;font-weight:600;letter-spacing:.06em;padding:.82rem 1.9rem;border-radius:var(--rs);border:1px solid rgba(255,255,255,.28);cursor:pointer;transition:border-color .28s,color .28s;text-decoration:none}
.btn-outline:hover{border-color:var(--gold);color:var(--gold)}
.btn-ghost{display:inline-flex;align-items:center;gap:.55rem;background:transparent;color:var(--gold);font-family:var(--font-b);font-size:14px;font-weight:600;letter-spacing:.06em;padding:.82rem 1.9rem;border-radius:var(--rs);border:1px solid rgba(200,169,110,.38);cursor:pointer;transition:background .28s,border-color .28s;text-decoration:none}
.btn-ghost:hover{background:rgba(200,169,110,.1);border-color:var(--gold)}
.btn-sm{font-size:13px;padding:.62rem 1.4rem}

/* ── REVEAL ── */
.reveal{opacity:0;transform:translateY(32px);transition:opacity .75s var(--ease),transform .75s var(--ease)}
.reveal.visible{opacity:1;transform:none}
.reveal-d1{transition-delay:.1s}.reveal-d2{transition-delay:.2s}.reveal-d3{transition-delay:.3s}.reveal-d4{transition-delay:.4s}.reveal-d5{transition-delay:.5s}

/* ── NAVBAR ── */
#navbar{position:sticky;top:0;z-index:900;padding:.9rem clamp(1rem,4vw,2.5rem);display:flex;align-items:center;justify-content:space-between;gap:1.5rem;background:rgba(6,14,30,.82);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border-bottom:1px solid rgba(200,169,110,.1);transition:padding .3s var(--ease),box-shadow .3s var(--ease)}
#navbar.scrolled{padding:.65rem clamp(1rem,4vw,2.5rem);box-shadow:0 4px 32px rgba(0,0,0,.45)}
.logo-link{display:inline-flex;align-items:center;gap:.75rem;text-decoration:none}
.logo-img{width:46px;height:46px;object-fit:contain}
.logo-wordmark .logo-name{font-family:var(--font-b);font-size:20px;font-weight:800;letter-spacing:.15em;text-transform:uppercase;line-height:1;color:#fff}
.logo-wordmark .logo-name .a-gold{color:var(--gold-l)}
.logo-wordmark .logo-tag{font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-top:3px;line-height:1;opacity:.85}
.nav-links{display:flex;align-items:center;gap:.15rem;list-style:none}
.nav-links a,.nav-links button{font-size:13.5px;font-weight:500;color:rgba(255,255,255,.75);padding:.5rem .85rem;border-radius:8px;transition:color .22s,background .22s;white-space:nowrap;display:flex;align-items:center;gap:.35rem}
.nav-links a:hover,.nav-links button:hover{color:#fff;background:rgba(255,255,255,.06)}
.nav-cta{background:linear-gradient(135deg,var(--gold),var(--gold-l));color:#060e1e!important;font-weight:700!important;padding:.5rem 1.1rem!important;border-radius:8px!important}
.nav-cta:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(200,169,110,.32)}
.dropdown{position:relative}
.dropdown-menu{position:absolute;top:calc(100% + .5rem);left:0;min-width:200px;background:rgba(6,14,30,.96);backdrop-filter:blur(24px);border:1px solid rgba(200,169,110,.2);border-radius:12px;padding:.5rem;opacity:0;visibility:hidden;transform:translateY(-8px);transition:opacity .22s var(--ease),transform .22s var(--ease),visibility .22s;z-index:100}
.dropdown:hover .dropdown-menu,.dropdown:focus-within .dropdown-menu{opacity:1;visibility:visible;transform:none}
.dropdown-menu a{display:flex;align-items:center;gap:.5rem;padding:.52rem .85rem;border-radius:8px;font-size:13px;color:rgba(255,255,255,.75);transition:background .18s,color .18s}
.dropdown-menu a:hover{background:rgba(200,169,110,.12);color:#fff}
.chevron{transition:transform .22s var(--ease);font-style:normal;display:inline-block;font-size:10px}
.dropdown:hover .chevron{transform:rotate(180deg)}
.hamburger{display:none;flex-direction:column;gap:5px;padding:6px;border-radius:8px;transition:background .2s}
.hamburger:hover{background:rgba(255,255,255,.08)}
.hamburger span{width:22px;height:2px;background:#fff;border-radius:2px;transition:transform .3s var(--ease),opacity .3s}
.hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.hamburger.open span:nth-child(2){opacity:0}
.hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}

/* ── MOBILE MENU ── */
#mobile-menu{position:fixed;inset:0;background:rgba(4,9,20,.97);backdrop-filter:blur(24px);z-index:800;padding:6rem 2rem 3rem;display:flex;flex-direction:column;gap:.5rem;transform:translateX(-100%);transition:transform .38s var(--ease)}
#mobile-menu.open{transform:none}
#mobile-menu a{font-size:1.3rem;font-weight:600;color:rgba(255,255,255,.8);padding:.7rem 0;border-bottom:1px solid rgba(255,255,255,.06);transition:color .2s}
#mobile-menu a:hover{color:var(--gold)}
.mm-cta{margin-top:1.5rem;background:linear-gradient(135deg,var(--gold),var(--gold-l));color:#060e1e!important;font-weight:700!important;text-align:center;border-radius:var(--rs);border-bottom:none!important;padding:.9rem!important}

/* ── HERO ── */
#hero{min-height:100vh;display:flex;align-items:center;padding-top:82px;position:relative;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(3rem,6vw,6rem);align-items:center;width:100%}
.hero-badge{display:inline-flex;align-items:center;gap:.55rem;background:rgba(200,169,110,.12);border:1px solid rgba(200,169,110,.28);border-radius:100px;padding:.38rem 1rem;font-size:11.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin-bottom:1.6rem}
.hero-badge-dot{width:7px;height:7px;background:var(--gold);border-radius:50%;animation:pulse-dot 2.2s ease-in-out infinite;flex-shrink:0}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.45;transform:scale(.75)}}
.hero-title{font-family:var(--font-d);font-size:clamp(2.6rem,5.5vw,4.2rem);font-weight:300;line-height:1.08;color:#fff;margin-bottom:1.4rem;letter-spacing:-.01em}
.hero-title em{font-style:italic;background:linear-gradient(135deg,var(--gold),var(--gold-l));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero-sub{font-size:1.1rem;color:var(--muted);line-height:1.72;max-width:480px;margin-bottom:2.2rem}
.hero-ctas{display:flex;gap:.85rem;flex-wrap:wrap;margin-bottom:1.8rem}
.flag-chips{display:flex;gap:.7rem;flex-wrap:wrap;align-items:center}
.flag-chip{display:inline-flex;align-items:center;gap:.35rem;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:100px;padding:.28rem .75rem;font-size:12px;font-weight:500;color:var(--muted);transition:border-color .22s,color .22s}
.flag-chip:hover{border-color:rgba(200,169,110,.4);color:var(--gold)}
.flag-chip .flag{font-size:1rem}
.hero-fine{font-size:11px;color:var(--faint);margin-top:1.4rem;max-width:440px;line-height:1.5}

/* ── HERO RIGHT ── */
.hero-right{position:relative;height:560px;display:flex;align-items:flex-end;justify-content:center}
.hero-right-inner{position:relative;width:100%;height:100%}
.hero-logo-float{position:absolute;top:5%;left:50%;transform:translateX(-50%);z-index:10;animation:logo-float 5s ease-in-out infinite}
.hero-logo-float img{width:88px;height:88px;object-fit:contain;filter:drop-shadow(0 8px 28px rgba(200,169,110,.4))}
@keyframes logo-float{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(-14px)}}
.opera-wrap{position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:100%;max-width:500px;z-index:2}
.opera-glow{position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:460px;height:200px;background:radial-gradient(ellipse at 50% 100%,rgba(200,169,110,.14) 0%,transparent 70%);pointer-events:none;z-index:1}
/* Flag cards */
.flag-cards-wrap{position:absolute;inset:0;pointer-events:none;z-index:5}
.fc{position:absolute;pointer-events:all;background:rgba(6,14,30,.86);backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);border:1px solid rgba(200,169,110,.26);border-radius:12px;padding:.8rem 1rem;display:flex;flex-direction:column;align-items:center;gap:.25rem;min-width:90px;transition:border-color .3s,box-shadow .3s;animation:fc-float var(--fdur,4s) ease-in-out infinite;animation-delay:var(--fdel,0s)}
.fc:hover{border-color:rgba(200,169,110,.6);box-shadow:0 0 28px rgba(200,169,110,.2)}
@keyframes fc-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.fc-emoji{font-size:2.2rem;line-height:1;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.fc-country{font-size:11px;font-weight:700;color:rgba(255,255,255,.9);letter-spacing:.06em;text-transform:uppercase}
.fc-label{font-size:9px;color:var(--gold);letter-spacing:.09em;text-transform:uppercase;border:1px solid rgba(200,169,110,.3);border-radius:20px;padding:1px 7px}
.fc-au{top:18%;left:2%;--fdur:3.7s;--fdel:0s}
.fc-uk{top:18%;right:2%;--fdur:4.2s;--fdel:-.8s}
.fc-ca{top:50%;left:2%;--fdur:4.8s;--fdel:-2s}
.fc-us{top:50%;right:2%;--fdur:4.1s;--fdel:-1.2s}
.fc-nz{bottom:18%;left:4%;--fdur:3.9s;--fdel:-3s}
.fc-eu{bottom:18%;right:4%;--fdur:4.5s;--fdel:-1.8s}
/* particles */
.particles{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.pt{position:absolute;width:2px;height:2px;background:var(--gold);border-radius:50%;opacity:0;animation:pt-rise var(--pdur,9s) ease-in-out infinite;animation-delay:var(--pdel,0s)}
@keyframes pt-rise{0%{opacity:0;transform:translateY(0) scale(.5)}20%{opacity:.55}80%{opacity:.25}100%{opacity:0;transform:translateY(-70px) scale(1)}}

/* ── STATS BAR ── */
.stats-bar{padding:3.5rem 0;border-top:1px solid rgba(200,169,110,.12);border-bottom:1px solid rgba(200,169,110,.12);background:rgba(11,42,107,.08)}
.stats-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:2rem;text-align:center}
.stat-num{font-family:var(--font-d);font-size:clamp(2.6rem,5vw,3.8rem);font-weight:300;background:linear-gradient(135deg,var(--gold),var(--gold-l));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1}
.stat-lbl{font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-top:.4rem}
.stat-sep{width:1px;background:rgba(200,169,110,.15);height:40px;margin:auto;display:none}

/* ── ABOUT ── */
#about .about-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(3rem,6vw,6rem);align-items:start}
.about-img-side{position:relative}
.about-card-visual{background:linear-gradient(135deg,rgba(11,42,107,.5),rgba(26,95,180,.2));border:1px solid rgba(200,169,110,.2);border-radius:20px;padding:2.5rem;aspect-ratio:1;display:flex;flex-direction:column;justify-content:space-between}
.about-quote{font-family:var(--font-d);font-size:1.6rem;font-style:italic;color:rgba(255,255,255,.9);line-height:1.35;flex:1;display:flex;align-items:center}
.about-quote-attr{font-size:12px;color:var(--gold);letter-spacing:.1em;text-transform:uppercase}
.about-text p{color:var(--muted);margin-bottom:1.1rem;line-height:1.75}
.info-boxes{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.8rem}
.info-box{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:var(--rs);padding:1rem 1.15rem}
.info-box-label{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:.4rem}
.info-box-val{font-size:13.5px;color:var(--text);line-height:1.5}
.about-banner{margin-top:2rem;background:linear-gradient(135deg,rgba(200,169,110,.12),rgba(200,169,110,.05));border:1px solid rgba(200,169,110,.25);border-radius:var(--rs);padding:1.1rem 1.5rem;display:flex;align-items:center;gap:1rem;flex-wrap:wrap}
.about-banner span{font-size:12px;color:var(--gold);font-weight:600;letter-spacing:.06em}
.about-banner .sep{color:rgba(200,169,110,.35)}

/* ── SERVICES ── */
#services .services-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem}
.srv-card{padding:2.2rem;position:relative;overflow:hidden}
.srv-icon{width:48px;height:48px;background:linear-gradient(135deg,rgba(200,169,110,.18),rgba(200,169,110,.05));border:1px solid rgba(200,169,110,.25);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:1.4rem;transition:transform .3s var(--ease)}
.srv-card:hover .srv-icon{transform:scale(1.1)}
.srv-title{font-family:var(--font-d);font-size:1.35rem;font-weight:400;color:#fff;margin-bottom:.65rem}
.srv-desc{font-size:14px;color:var(--muted);line-height:1.7}
.srv-link{display:inline-flex;align-items:center;gap:.4rem;font-size:13px;font-weight:600;color:var(--gold);margin-top:1rem;letter-spacing:.04em;transition:gap .2s}
.srv-link:hover{gap:.7rem}

/* ── COUNTRIES ── */
#countries .tab-bar{display:flex;gap:.5rem;border-bottom:1px solid rgba(200,169,110,.15);margin-bottom:3rem;overflow-x:auto;padding-bottom:0}
.tab-btn{flex-shrink:0;display:inline-flex;align-items:center;gap:.4rem;font-size:14px;font-weight:600;color:var(--muted);padding:.7rem 1.3rem;border-bottom:2px solid transparent;margin-bottom:-1px;border-radius:var(--rs) var(--rs) 0 0;transition:color .22s,border-color .22s,background .22s;white-space:nowrap}
.tab-btn:hover{color:#fff;background:rgba(255,255,255,.04)}
.tab-btn.active{color:var(--gold);border-bottom-color:var(--gold);background:rgba(200,169,110,.06)}
.tab-panel{display:none}
.tab-panel.active{display:block}
.country-banner{background:linear-gradient(135deg,rgba(11,42,107,.4),rgba(26,95,180,.15));border:1px solid rgba(200,169,110,.15);border-radius:var(--r);padding:2.2rem;margin-bottom:2rem}
.country-banner-inner{display:grid;grid-template-columns:auto 1fr auto;gap:1.5rem 2rem;align-items:center}
.country-flag-big{font-size:3.2rem;filter:drop-shadow(0 4px 12px rgba(0,0,0,.4))}
.country-name{font-family:var(--font-d);font-size:1.9rem;font-weight:300;color:#fff;margin-bottom:.35rem}
.country-intro{font-size:14px;color:var(--muted);line-height:1.65}
.country-stats{display:flex;gap:1.5rem}
.c-stat{text-align:center}
.c-stat-n{display:block;font-family:var(--font-d);font-size:1.6rem;font-weight:300;color:var(--gold)}
.c-stat-l{font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
/* Accordions */
.visa-accordions{display:flex;flex-direction:column;gap:.75rem;margin-bottom:2.5rem}
.acc-item{background:var(--glass);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--glass-b);border-radius:var(--rs);overflow:hidden;transition:border-color .3s}
.acc-item.open{border-color:rgba(200,169,110,.35)}
.acc-hdr{width:100%;display:flex;align-items:center;justify-content:space-between;padding:1.1rem 1.4rem;text-align:left;transition:background .22s}
.acc-hdr:hover{background:rgba(255,255,255,.03)}
.acc-title{font-size:15px;font-weight:600;color:#fff}
.acc-hdr-right{display:flex;align-items:center;gap:.75rem}
.visa-badge{font-size:10px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;padding:.2rem .65rem;border-radius:20px}
.badge-student{background:rgba(96,165,250,.15);color:#60a5fa;border:1px solid rgba(96,165,250,.25)}
.badge-skilled{background:rgba(200,169,110,.15);color:var(--gold);border:1px solid rgba(200,169,110,.25)}
.badge-employer{background:rgba(52,211,153,.12);color:#34d399;border:1px solid rgba(52,211,153,.22)}
.badge-partner{background:rgba(244,114,182,.12);color:#f472b6;border:1px solid rgba(244,114,182,.22)}
.badge-visitor{background:rgba(167,139,250,.12);color:#a78bfa;border:1px solid rgba(167,139,250,.22)}
.badge-parent{background:rgba(251,191,36,.12);color:#fbbf24;border:1px solid rgba(251,191,36,.22)}
.badge-work{background:rgba(52,211,153,.12);color:#34d399;border:1px solid rgba(52,211,153,.22)}
.badge-pr{background:rgba(200,169,110,.15);color:var(--gold);border:1px solid rgba(200,169,110,.25)}
.acc-icon{width:24px;height:24px;border-radius:50%;border:1px solid rgba(200,169,110,.3);display:flex;align-items:center;justify-content:center;font-size:14px;color:var(--gold);transition:transform .3s var(--ease),background .3s;flex-shrink:0}
.acc-item.open .acc-icon{transform:rotate(45deg);background:rgba(200,169,110,.15)}
.acc-body{max-height:0;overflow:hidden;transition:max-height .5s cubic-bezier(.4,0,.2,1)}
.acc-inner{padding:0 1.4rem 1.4rem}
.acc-desc{font-size:14.5px;color:var(--muted);line-height:1.75;margin-bottom:1.2rem;padding-top:.2rem}
.req-list{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:.45rem .75rem;margin-bottom:1.4rem}
.req-list li{font-size:13.5px;color:var(--text);line-height:1.55;padding-left:1.2rem;position:relative}
.req-list li::before{content:'→';position:absolute;left:0;color:var(--gold);font-size:12px}
.meta-row{display:grid;grid-template-columns:repeat(5,1fr);gap:1rem;background:rgba(255,255,255,.03);border-radius:var(--rs);padding:1rem;margin-bottom:1.2rem}
.meta-item{text-align:center}
.meta-label{display:block;font-size:9.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);margin-bottom:.3rem}
.meta-val{font-size:12.5px;font-weight:600;color:var(--gold-l);line-height:1.3}
.acc-ctas{display:flex;gap:.75rem}
/* Universities */
.unis-section{margin-top:1rem}
.unis-title{font-family:var(--font-d);font-size:1.15rem;font-weight:400;color:rgba(255,255,255,.7);margin-bottom:1rem;letter-spacing:.02em}
.uni-grid{display:flex;flex-wrap:wrap;gap:.6rem}
.uni-card{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);border-radius:8px;padding:.4rem .9rem;font-size:12.5px;color:rgba(255,255,255,.6);transition:border-color .22s,color .22s}
.uni-card:hover{border-color:rgba(200,169,110,.35);color:var(--gold)}

/* ── WHY GEMCA ── */
#why .why-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(3rem,6vw,6rem);align-items:center}
.reasons-list{display:flex;flex-direction:column;gap:1.35rem}
.reason-item{display:flex;gap:1rem;align-items:flex-start}
.reason-num{flex-shrink:0;width:36px;height:36px;background:linear-gradient(135deg,rgba(200,169,110,.2),rgba(200,169,110,.05));border:1px solid rgba(200,169,110,.3);border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:var(--font-d);font-size:1.1rem;color:var(--gold)}
.reason-title{font-size:15px;font-weight:700;color:#fff;margin-bottom:.3rem}
.reason-desc{font-size:13.5px;color:var(--muted);line-height:1.65}
/* 3D stacked card visual */
.card-stack{position:relative;height:320px;display:flex;align-items:center;justify-content:center}
.stack-card{position:absolute;width:300px;border-radius:16px;padding:1.6rem;animation:stack-float 4.5s ease-in-out infinite}
.stack-card-3{background:rgba(11,42,107,.4);border:1px solid rgba(200,169,110,.1);transform:rotate(-6deg) translateY(12px);animation-delay:-3s;z-index:1}
.stack-card-2{background:rgba(11,42,107,.6);border:1px solid rgba(200,169,110,.18);transform:rotate(-2.5deg) translateY(6px);animation-delay:-1.5s;z-index:2}
.stack-card-1{background:linear-gradient(135deg,rgba(11,42,107,.85),rgba(26,95,180,.5));border:1px solid rgba(200,169,110,.38);transform:rotate(.5deg);z-index:3}
@keyframes stack-float{0%,100%{transform:translateY(0) rotate(.5deg)}50%{transform:translateY(-10px) rotate(.5deg)}}
.stack-card-2-anim{animation-name:stack-float-2}
@keyframes stack-float-2{0%,100%{transform:translateY(0) rotate(-2.5deg)}50%{transform:translateY(-7px) rotate(-2.5deg)}}
.sc-badge{font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);background:rgba(200,169,110,.15);border:1px solid rgba(200,169,110,.3);border-radius:100px;padding:.28rem .8rem;display:inline-flex;align-items:center;gap:.4rem;margin-bottom:1rem}
.sc-badge::before{content:'●';font-size:8px;color:#4ade80}
.sc-number{font-family:var(--font-d);font-size:2.2rem;font-weight:300;color:#fff}
.sc-sub{font-size:13px;color:var(--muted);margin-top:.2rem}
.sc-divider{height:1px;background:linear-gradient(90deg,transparent,rgba(200,169,110,.3),transparent);margin:1rem 0}
.sc-pills{display:flex;gap:.5rem;flex-wrap:wrap}
.sc-pill{font-size:11px;font-weight:600;color:var(--gold);background:rgba(200,169,110,.1);border:1px solid rgba(200,169,110,.22);border-radius:100px;padding:.25rem .7rem}

/* ── TESTIMONIALS ── */
#testimonials .testi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem}
.testi-card{padding:2rem}
.testi-stars{color:var(--gold);font-size:14px;letter-spacing:.1em;margin-bottom:1rem}
.testi-quote{font-family:var(--font-d);font-size:1.1rem;font-style:italic;color:rgba(255,255,255,.85);line-height:1.65;margin-bottom:1.4rem}
.testi-author{display:flex;align-items:center;gap:.75rem}
.testi-avatar{width:42px;height:42px;border-radius:50%;background:linear-gradient(135deg,var(--sapphire),var(--navy));border:2px solid rgba(200,169,110,.3);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px;color:#fff;flex-shrink:0}
.testi-name{font-weight:700;font-size:14px;color:#fff}
.testi-visa{font-size:12px;color:var(--gold);margin-top:.1rem}

/* ── COMPLIANCE BANNER ── */
#compliance{padding:3rem 0}
.compliance-box{background:linear-gradient(135deg,rgba(200,169,110,.1),rgba(200,169,110,.04));border:1px solid rgba(200,169,110,.3);border-radius:var(--r);padding:2.2rem 2.5rem;display:grid;grid-template-columns:auto 1fr auto;gap:1.5rem;align-items:center}
.compliance-icon{font-size:2.4rem;filter:drop-shadow(0 4px 12px rgba(200,169,110,.3))}
.compliance-text h4{font-family:var(--font-d);font-size:1.2rem;color:#fff;margin-bottom:.4rem}
.compliance-text p{font-size:13px;color:var(--muted);line-height:1.7}
.compliance-marn{text-align:right}
.compliance-marn .marn-num{font-family:var(--font-d);font-size:1.5rem;color:var(--gold)}
.compliance-marn .marn-sub{font-size:11px;color:var(--muted);letter-spacing:.1em;text-transform:uppercase}

/* ── FORMS ── */
.form-section{padding:0}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(3rem,6vw,5rem);align-items:start}
.form-checklist{display:flex;flex-direction:column;gap:.75rem;margin:1.5rem 0}
.checklist-item{display:flex;align-items:center;gap:.65rem;font-size:14px;color:var(--muted)}
.checklist-item::before{content:'✓';color:var(--gold);font-weight:700;font-size:16px;flex-shrink:0}
.form-box{background:var(--glass);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--glass-b);border-radius:var(--r);padding:2.2rem}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.form-group{display:flex;flex-direction:column;gap:.45rem;margin-bottom:1rem}
.form-label{font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.form-input,.form-select,.form-textarea{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:var(--rs);padding:.78rem 1rem;font-family:var(--font-b);font-size:14px;color:#fff;transition:border-color .25s,background .25s;width:100%}
.form-input:focus,.form-select:focus,.form-textarea:focus{outline:none;border-color:rgba(200,169,110,.5);background:rgba(255,255,255,.07)}
.form-input::placeholder,.form-textarea::placeholder{color:rgba(255,255,255,.28)}
.form-select{appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath d='M6 8L1 3h10z' fill='%23C8A96E'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 1rem center}
.form-select option{background:#0d1e3a;color:#fff}
.form-textarea{resize:vertical;min-height:110px}
.form-consent{display:flex;align-items:flex-start;gap:.65rem;font-size:13px;color:var(--muted);line-height:1.55}
.form-consent input[type="checkbox"]{width:16px;height:16px;margin-top:2px;accent-color:var(--gold);flex-shrink:0}
.form-submit{margin-top:1.4rem}
.submit-btn{width:100%;position:relative;justify-content:center}
.spinner{display:none;width:18px;height:18px;border:2px solid rgba(0,0,0,.2);border-top-color:#060e1e;border-radius:50%;animation:spin .7s linear infinite;flex-shrink:0}
@keyframes spin{to{transform:rotate(360deg)}}
.form-success{display:none;text-align:center;padding:3rem 2rem}
.form-success .success-icon{font-size:3rem;margin-bottom:1rem}
.form-success h4{font-family:var(--font-d);font-size:1.6rem;color:#fff;margin-bottom:.5rem}
.form-success p{color:var(--muted)}

/* ── CONTACT ── */
#contact .contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(3rem,6vw,5rem);align-items:start}
.contact-cards{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.5rem}
.contact-card{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:var(--r);padding:1.3rem 1.5rem;transition:border-color .25s}
.contact-card:hover{border-color:rgba(200,169,110,.3)}
.cc-icon{font-size:1.6rem;margin-bottom:.6rem}
.cc-label{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:.35rem}
.cc-val{font-size:13.5px;color:var(--text);line-height:1.55}
.cc-val a{color:inherit;transition:color .2s}
.cc-val a:hover{color:var(--gold)}

/* ── FOOTER ── */
footer{background:rgba(6,14,30,.9);border-top:1px solid rgba(200,169,110,.12);padding:4.5rem 0 2rem}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1.2fr;gap:3rem;margin-bottom:3rem}
.footer-brand-logo{display:inline-flex;align-items:center;gap:.75rem;margin-bottom:1.1rem}
.footer-logo-img{width:44px;height:44px;object-fit:contain}
.footer-desc{font-size:13.5px;color:var(--muted);line-height:1.7;max-width:320px;margin-bottom:1.2rem}
.footer-disclaimer{font-size:11.5px;color:var(--faint);line-height:1.65;border-top:1px solid rgba(200,169,110,.1);padding-top:1rem;margin-top:1rem}
.footer-col h5{font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:1.1rem}
.footer-links{list-style:none;display:flex;flex-direction:column;gap:.55rem}
.footer-links a{font-size:13.5px;color:var(--muted);transition:color .2s}
.footer-links a:hover{color:var(--gold)}
.footer-bottom{border-top:1px solid rgba(200,169,110,.1);padding-top:1.5rem;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem}
.footer-bottom p{font-size:12px;color:var(--faint)}
.social-row{display:flex;gap:.6rem}
.social-btn{width:36px;height:36px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:9px;display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,.55);font-size:14px;transition:background .22s,border-color .22s,color .22s}
.social-btn:hover{background:rgba(200,169,110,.15);border-color:rgba(200,169,110,.4);color:var(--gold)}

/* ── WHATSAPP FLOAT ── */
.wa-float{position:fixed;bottom:2rem;right:2rem;z-index:999;width:58px;height:58px;background:linear-gradient(135deg,#25D366,#128C7E);border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 30px rgba(37,211,102,.4);animation:wa-pulse 2.8s ease-in-out infinite;transition:transform .25s,box-shadow .25s}
.wa-float:hover{transform:scale(1.12);box-shadow:0 12px 40px rgba(37,211,102,.55);animation:none}
@keyframes wa-pulse{0%,100%{box-shadow:0 8px 30px rgba(37,211,102,.4)}50%{box-shadow:0 8px 30px rgba(37,211,102,.4),0 0 0 10px rgba(37,211,102,.1)}}
.wa-float svg{color:#fff;width:28px;height:28px}

/* ── RESPONSIVE ── */
@media(max-width:1280px){
  .hero-right{display:none}
  .hero-grid{grid-template-columns:1fr;max-width:680px}
  .fc-au,.fc-uk,.fc-ca,.fc-us,.fc-nz,.fc-eu{display:none}
}
@media(max-width:1024px){
  .nav-links{display:none}
  .hamburger{display:flex}
  #about .about-grid,.why-grid,.form-grid,.contact-grid,.footer-grid{grid-template-columns:1fr}
  .services-grid{grid-template-columns:repeat(2,1fr)}
  .meta-row{grid-template-columns:repeat(3,1fr)}
  .country-banner-inner{grid-template-columns:auto 1fr;grid-template-rows:auto auto}
  .country-stats{grid-column:1/-1;justify-content:flex-start}
}
@media(max-width:768px){
  .services-grid{grid-template-columns:1fr}
  .testi-grid{grid-template-columns:1fr}
  .stats-grid{grid-template-columns:repeat(3,1fr)}
  .stats-grid .stat-item:nth-child(4),.stats-grid .stat-item:nth-child(5){grid-column:span 1}
  .req-list{grid-template-columns:1fr}
  .meta-row{grid-template-columns:repeat(2,1fr)}
  .form-row{grid-template-columns:1fr}
  .info-boxes{grid-template-columns:1fr}
  .contact-cards{grid-template-columns:1fr}
  .footer-grid{grid-template-columns:1fr 1fr}
  .compliance-box{grid-template-columns:1fr;text-align:center}
  .compliance-marn{text-align:center}
}
@media(max-width:480px){
  .stats-grid{grid-template-columns:repeat(2,1fr)}
  .hero-ctas{flex-direction:column}
  .hero-ctas .btn-primary,.hero-ctas .btn-outline,.hero-ctas .btn-ghost{width:100%;justify-content:center}
  .footer-grid{grid-template-columns:1fr}
  .acc-ctas{flex-direction:column}
  .acc-ctas .btn-primary,.acc-ctas .btn-outline{width:100%;justify-content:center}
}
"""


# ── COUNTRY CONTENT ─────────────────────────────────────────────────────────

AU_VISAS = (
  acc("Subclass 500 — Student Visa","badge-student","Student",
    "The Subclass 500 Student Visa allows international students to study full-time at a CRICOS-registered Australian education provider. It permits the holder and accompanying family members to live, study, and work in Australia for the duration of their studies. Applicants must demonstrate Genuine Temporary Entrant (GTE) intent, English proficiency, adequate funds, and Overseas Student Health Cover (OSHC). GEMCA provides end-to-end support from institutional selection to visa grant.",
    ["Enrolment in a CRICOS-registered course","Evidence of financial capacity (tuition + ~AUD $24,505/year living costs)","Overseas Student Health Cover (OSHC)","English proficiency: IELTS 5.5–6.5 depending on course level","Genuine Temporary Entrant (GTE) statement","Valid passport with at least 6 months validity","Health and character requirements"],
    "AUD $1,600","4–8 weeks","48 hrs/fortnight during study; full-time during scheduled breaks","Course length + 60 days","SC 485 Temporary Graduate")
+
  acc("Subclass 485 — Temporary Graduate Visa","badge-student","Post-Study Work",
    "The Subclass 485 Temporary Graduate Visa allows recent graduates from Australian institutions to live and work in Australia temporarily after their student visa expires. Two streams exist: Graduate Work (12 months, for skills on the SOL) and Post-Study Work (2–4 years for bachelor's degree holders and above). This visa provides valuable Australian work experience critical for future skilled migration applications and building CRS points for an EOI. It is non-renewable.",
    ["Graduated from an Australian institution within the last 6 months","Held a student visa while completing studies in Australia","Minimum 16 months of study in Australia (Post-Study Work stream)","Skills assessment required (Graduate Work stream only)","English proficiency: at least IELTS 6.0 overall","Under 50 years of age","Health and character requirements"],
    "AUD $2,300","3–5 months","Unrestricted (any employer, any occupation)","2–4 years (Post-Study Work)","SC 189 / 190 / 491 Skilled Migration")
+
  acc("Subclass 189 / 190 / 491 — Skilled Migration","badge-skilled","Points-Tested",
    "Australia's premier skilled migration visas — the Subclass 189 (Skilled Independent), 190 (State Nominated), and 491 (Skilled Work Regional) — provide permanent or long-term pathways for skilled workers through the points-tested SkillSelect system. Applicants must score a minimum 65 points and receive an Invitation to Apply (ITA). State nominations under the 190 and 491 add 5–15 bonus points. GEMCA assists with EOI submission, skills assessments, nomination applications, and full visa lodgement.",
    ["Positive skills assessment by the relevant Australian assessing authority","Nominated occupation listed on the relevant skilled occupations list","Minimum 65 points on the Points Test","Expression of Interest (EOI) submitted via SkillSelect","Competent English: IELTS 6.0 in each band","Under 45 years of age (exceptions apply for some state nominations)","Health and character requirements"],
    "AUD $4,765","6–24 months","Unrestricted (permanent)","Permanent (189/190); 5 years (491)","PR immediately (189/190); SC 191 Permanent after 3 years (491)")
+
  acc("Subclass 482 — Skills in Demand Visa","badge-employer","Employer Sponsored",
    "The Skills in Demand Visa (replacing the TSS SC 482) allows Australian employers to sponsor skilled overseas workers on a temporary basis when suitably skilled Australians cannot be found. From late 2024 it operates across three streams: Specialist Skills, Core Skills, and Essential Skills, replacing the old short-stay/medium-stay structure. The visa offers pathways to permanent residence via SC 186 or SC 191. GEMCA assists employers with sponsorship applications and workers with nomination and visa applications.",
    ["Approved sponsoring employer holding a valid Standard Business Sponsorship","Occupation aligned to the relevant stream occupation list","Two years relevant work experience in the nominated occupation","Salary at or above the TSMIT (currently AUD $73,150) or occupation minimum","English proficiency: IELTS 5.0 overall (Core Skills); 5.0 each band (Specialist)","Relevant qualifications or skills assessment where required","Health and character requirements"],
    "AUD $3,115","2–4 months","Full-time for sponsoring employer","4 years (Core/Specialist Skills)","SC 186 ENS Permanent / SC 191 Regional Permanent")
+
  acc("Subclass 186 — Employer Nominated Scheme","badge-pr","Permanent",
    "The Subclass 186 Employer Nominated Scheme visa grants permanent residence to skilled workers nominated by an approved Australian employer. Three streams are available: Temporary Residence Transition (for existing SC 482 holders with 3 years employment), Direct Entry (meeting skills, qualifications, and English requirements), and Labour Agreement. This is one of the most direct pathways to Australian permanent residence for employer-sponsored workers. GEMCA manages both employer nomination and individual visa applications.",
    ["Australian Standard Business Sponsor (ASBS) approved employer","Nomination by the employer in an eligible occupation","Relevant skills assessment (Direct Entry stream)","Under 45 years of age (exceptions for some occupations and regions)","Competent English: IELTS 6.0 in each band","3 years relevant work experience or 2 years on SC 482/457 (TRT stream)","Health and character requirements"],
    "AUD $4,765","6–18 months","Unrestricted (permanent)","Permanent","Australian Citizenship after 4 years PR")
+
  acc("Subclass 820/801 — Partner Visa","badge-partner","Partner",
    "Partner visas enable spouses or de facto partners of Australian citizens, permanent residents, or eligible New Zealand citizens to obtain permanent residence. The SC 820 is granted first as a temporary visa; the SC 801 permanent visa is granted after 2 years (or immediately for relationships of 3+ years with children). GEMCA assists with relationship evidence compilation, statutory declarations, and comprehensive documentation to maximise application quality and minimise delays.",
    ["Genuine spouse or de facto relationship of at least 12 months (de facto)","Sponsor who is an Australian citizen, PR, or eligible NZ citizen","Comprehensive evidence across four statutory relationship categories","Police clearances from all countries of residence in the past 10 years","Health examinations for all applicants","Joint financial evidence and cohabitation records","Community and social recognition of the relationship"],
    "AUD $9,365","12–24 months","Unrestricted from grant of SC 820","Until SC 801 decision","Permanent Residence (SC 801) → Australian Citizenship")
+
  acc("Parent 103 / 143 — Parent Migration","badge-parent","Parent",
    "Parent visas allow parents of Australian citizens, permanent residents, or eligible NZ citizens to migrate to Australia permanently. The Contributory Parent (SC 143) fast-tracks the process with a higher fee, while the non-contributory Parent (SC 103) joins a very long queue (20–30 year wait). GEMCA recommends a staged approach: temporary Parent SC 173 or 884 first, converting to permanent. The balance of family test requires at least half of your children to permanently reside in Australia.",
    ["Balance of family test: at least half of children reside permanently in Australia","Sponsorship by an eligible child settled in Australia","Assurance of Support (AoS) bond lodgement with the Commonwealth","Health and character requirements for all applicants","No outstanding debts to the Australian Government","Adequate private health insurance","Evidence of the sponsor's Australian residency status"],
    "AUD $4,890 (103) / AUD $48,430 (143)","20–30 yrs (103); 4–7 yrs (143)","Unrestricted (permanent)","Permanent","Australian Citizenship after 4 years PR")
+
  acc("Subclass 600 — Visitor Visa","badge-visitor","Visitor",
    "The Visitor Visa (Subclass 600) allows people to visit Australia for tourism, business visitor activities, or to see family and friends. Most applicants apply online via ImmiAccount. GEMCA assists with applications involving previous refusals, health waivers, or complex circumstances. We also handle condition 8503 (No Further Stay) waiver requests where circumstances have changed materially since the original visa was granted.",
    ["Genuine intention to visit Australia temporarily","Sufficient funds to support the visit without working illegally","Strong ties to the home country: employment, family, property, or business","No previous visa refusals or cancellations (or satisfactory explanation)","Valid passport with at least 6 months validity beyond intended stay","Health requirements if staying more than 12 months","Health insurance recommended for the duration of the visit"],
    "AUD $190","1–4 weeks","None (Business Visitor: limited activities only)","Up to 12 months (3–6 months typical)","N/A — temporary visit only")
)

UK_VISAS = (
  acc("Student Visa","badge-student","Student",
    "The UK Student Visa allows international students to study at a licensed UK student sponsor institution. Students must receive a Confirmation of Acceptance for Studies (CAS) from their university before applying. The visa also permits limited work rights during term time and full-time work during vacation periods. Students on RQF Level 7+ courses in London face stricter financial requirements. GEMCA provides pre-application coaching, documentation review, and CAS receipt guidance.",
    ["Unconditional offer and CAS number from a licensed student sponsor","English proficiency: IELTS UKVI Academic 5.5–6.5 or above","Financial proof: £1,334/month in London, £1,023/month outside for 9 months","ATAS security clearance for certain sensitive subjects and nationalities","Tuberculosis test for applicants from specified countries","Biometric Residence Permit (BRP) upon arrival","Genuine student intent assessment"],
    "£363 (outside UK)","3–8 weeks","20 hrs/week during term; full-time during official vacations","Course length + 4–6 months","Graduate Route visa")
+
  acc("Graduate Route","badge-student","Post-Study Work",
    "The Graduate Route allows international students who have completed a UK bachelor's degree or above (or an eligible postgraduate qualification) to remain in the UK after graduation to work or look for work. No employer sponsorship is required and there are no minimum salary requirements. PhD graduates receive 3 years; all others receive 2 years. GEMCA guides applicants through the seamless transition from Student to Graduate Route, including timing strategy for the application.",
    ["Successfully completed an eligible UK course (bachelor's degree minimum)","Studied at a licensed student sponsor throughout the course","Applied from within the UK while holding a valid Student Visa","Course must be a minimum of 12 months duration (post-2019 entry)","No significant absences from the UK during the course of study","Valid passport and biometrics","No serious criminal convictions"],
    "£822","1–8 weeks","Unrestricted (any employer, any job, self-employment allowed)","2 years (3 years for PhD graduates)","Skilled Worker Visa")
+
  acc("Skilled Worker Visa","badge-work","Skilled Work",
    "The UK Skilled Worker Visa is the primary route for skilled workers to live and work in the UK, replacing the old Tier 2 General visa. Applicants need sponsorship from a UK employer with a valid Sponsor Licence for a job at RQF Level 3 or above. Since April 2024, salary thresholds rose significantly to £38,700 for the general threshold. GEMCA assists with sponsor compliance, points-based self-assessment, and the full application preparation for both employers and applicants.",
    ["Certificate of Sponsorship (CoS) from a licensed UK employer","Job at RQF Level 3 (A-Level equivalent) or above","Salary at least £38,700 or the going rate for the occupation, whichever is higher","English language: B1 CEFR equivalent or above","No adverse immigration history in the UK or overseas","Valid travel document (passport)","Tuberculosis test for applicants from specified countries"],
    "£719–£1,420 (≤3 yrs)","3–8 weeks","Full-time for sponsoring employer only","Up to 5 years","UK Indefinite Leave to Remain (ILR) after 5 years")
+
  acc("Health & Care Worker Visa","badge-work","Healthcare",
    "The Health and Care Worker Visa is a fast-track dedicated route for doctors, nurses, healthcare professionals, and social care workers employed by the NHS, NHS-funded bodies, or eligible adult social care providers. Applicants are exempt from the Immigration Health Surcharge (saving up to £4,264 per person). Salary thresholds are lower than the standard Skilled Worker route for clinical roles. GEMCA supports healthcare professionals with professional registration, licensing, and the full visa application.",
    ["Job offer from the NHS, NHS-funded provider, or eligible adult social care employer","Occupation listed on the Health and Care Skilled Occupation List","Certificate of Sponsorship from a licensed healthcare sponsor","Minimum salary of £23,200 or the going rate for the specific role","Professional registration: GMC, NMC, HCPC, or relevant body","English language proficiency at the required level","No criminal record that would prevent registration"],
    "£247–£479","3 weeks (priority processing available)","Full-time for sponsoring employer","Up to 5 years","ILR after 5 years → British Citizenship")
)

CA_VISAS = (
  acc("Study Permit","badge-student","Study",
    "The Canadian Study Permit allows international students to study at a Designated Learning Institution (DLI) in Canada. Since 2024, most students require a Provincial Attestation Letter (PAL) from their province in addition to their acceptance letter, to address international enrolment caps. Students must demonstrate approximately CAD $20,635 per year in living funds beyond tuition. Work rights of 24 hours per week off-campus allow students to support themselves while studying. GEMCA provides PAL guidance and complete study permit application support.",
    ["Acceptance letter from a Designated Learning Institution (DLI)","Provincial Attestation Letter (PAL) — required for most provinces since January 2024","Proof of funds: CAD $20,635/year for living costs plus full tuition fees","English or French proficiency: IELTS Academic 6.0 or equivalent","Biometrics collection at a Visa Application Centre (VAC)","No serious criminal history","Genuine temporary student intent (letter of explanation recommended)"],
    "CAD $150","4–12 weeks","24 hrs/week off-campus; full-time on-campus and during scheduled breaks","Course length + 90 days","PGWP (Post-Graduation Work Permit)")
+
  acc("Express Entry — FSW / CEC","badge-skilled","Permanent Residence",
    "Express Entry is Canada's flagship points-based permanent residence system. The Federal Skilled Worker (FSW) stream targets internationally trained workers outside Canada, while the Canadian Experience Class (CEC) targets those with qualifying Canadian work experience. Candidates are ranked by the Comprehensive Ranking System (CRS) and invited in regular draws. With a PGWP and Canadian work experience, CEC candidates regularly receive ITAs with scores in the low 400s. GEMCA provides CRS optimisation strategy and complete PR application management.",
    ["At least one year of full-time (or equivalent) skilled work experience (NOC TEER 0–3)","Minimum CLB 7 English proficiency (IELTS 6.0 per band for FSW)","Educational Credential Assessment (ECA) by a IRCC-designated organisation","Minimum 67 points on the FSW six-factor grid (or meet CEC requirements)","Submit Expression of Interest (EOI) in the Express Entry pool","Medical examination and police certificates from all countries of residence","Proof of funds (unless you have a valid Canadian job offer)"],
    "CAD $1,365 (principal + spouse)","6 months after ITA","Unrestricted (permanent)","Permanent","Canadian Citizenship after 3 years (1,095 days) PR")
+
  acc("Provincial Nominee Program (PNP)","badge-skilled","Provincial PR",
    "The Provincial Nominee Program allows Canadian provinces and territories to select immigrants based on local economic needs. A provincial nomination adds 600 points to a candidate's CRS score in Express Entry, making an ITA virtually guaranteed at the next draw. Popular streams include OINP, BC PNP, AIPP, and Alberta Advantage. GEMCA provides expert analysis of which province and stream best fits your unique profile, and manages nomination and federal PR applications.",
    ["Meet the specific requirements of the nominating province's stream","Genuine intent and ability to settle and work in the nominating province","Job offer from a provincial employer (many streams require this)","Work experience in an eligible NOC occupation and TEER category","Language proficiency meeting provincial minimums (varies by stream)","Educational credentials assessed by a recognised body","Connection to the province: prior work, study, or family ties preferred"],
    "Varies (approx. CAD $1,500–$3,000)","Province 2–6 months + federal PR 6 months","Unrestricted (permanent)","Permanent","Canadian Citizenship after 3 years PR")
+
  acc("Post-Graduation Work Permit (PGWP)","badge-work","Open Work Permit",
    "The Post-Graduation Work Permit (PGWP) is a once-in-a-lifetime open work permit allowing international graduates from eligible Canadian DLIs to gain the Canadian work experience needed for the Canadian Experience Class stream of Express Entry. Since 2024, PGWP eligibility also depends on the field of study — graduates in STEM, trade, agriculture, and healthcare fields are prioritised. GEMCA advises students early in their study journey to select optimal programs and institutions for maximum PGWP eligibility.",
    ["Completed an eligible program at a PGWP-eligible DLI","Program meets post-2024 field-of-study requirements for PGWP","Program duration of at least 8 months","Maintained full-time enrolment throughout (with narrow exceptions)","Held a valid Study Permit at the time of graduation","Apply within 180 days of receiving official written confirmation of graduation","No previously held PGWP (granted only once in a lifetime)"],
    "CAD $255","3–5 months","Unrestricted open work permit (any employer, any occupation)","Up to 3 years (length of program, max 3 years)","CEC Express Entry → Permanent Residence")
)

US_VISAS = (
  acc("F-1 — Student Visa","badge-student","Student",
    "The F-1 visa is the primary non-immigrant visa for international students attending US colleges, universities, high schools, and language programs. Applicants must be enrolled as full-time students and demonstrate sufficient financial resources to cover all expenses. Optional Practical Training (OPT) allows work in a related field for 12 months after graduation, extendable to 36 months for STEM graduates on the STEM OPT extension. GEMCA provides institution selection guidance and pre-interview coaching for the US Embassy or Consulate interview.",
    ["Acceptance by a SEVP-certified school and receipt of Form I-20","Payment of SEVIS fee (Form I-901, currently USD $350)","Demonstrated financial support covering full cost of attendance","Strong non-immigrant intent: significant ties to home country","English proficiency as required by the institution (typically TOEFL 80+ iBT)","Valid passport with at least 6 months beyond intended period of stay","In-person visa interview at the US Embassy or Consulate"],
    "USD $185 + SEVIS $350","2–8 weeks post-interview","On-campus 20 hrs/week; OPT 12–36 months post-graduation","Duration of Status (D/S)","OPT → H-1B or EB employment-based green card")
+
  acc("J-1 — Exchange Visitor Visa","badge-student","Exchange",
    "The J-1 Exchange Visitor Visa enables cultural and educational exchange through programmes sponsored by US government-designated organisations. Categories include students, research scholars, professors, physicians, au pairs, and camp counsellors. Certain J-1 holders are subject to a two-year home country physical presence requirement before obtaining H or L visas or permanent residence. GEMCA advises on J-1 programme selection, home country rule applicability, and long-term immigration planning.",
    ["Acceptance into a J-1 Exchange Visitor Program from a designated sponsor","DS-2019 Certificate of Eligibility from the sponsoring programme organisation","Sufficient financial resources for the full duration of the programme","English proficiency as required by the specific exchange programme","Valid passport with at least 6 months validity","Non-immigrant intent (unless seeking a J-1 waiver of the two-year rule)","SEVIS fee payment (Form I-901)"],
    "USD $185","2–6 weeks","Varies by J-1 category; students may work on-campus","Duration of approved programme","Depends on J-1 category and two-year home country rule applicability")
+
  acc("H-1B — Specialty Occupation Visa","badge-work","Specialty Occupation",
    "The H-1B visa is for specialty occupation workers in fields requiring at least a US bachelor's degree (or equivalent), including IT, engineering, finance, accounting, architecture, and more. The annual cap is 65,000 regular visas plus 20,000 for US master's degree holders, allocated by electronic lottery. Recent lottery odds have been under 30%. GEMCA provides strategic advice on H-1B eligibility, lottery registration timing, employer petition filing, and long-term alternatives such as O-1, L-1, and EB green card pathways.",
    ["Job offer from a US employer for a qualifying specialty occupation","Bachelor's degree (or equivalent) in the specific relevant specialty field","Approved Labour Condition Application (LCA) from the Department of Labor","Employer files Form I-129 petition with USCIS after lottery selection","Selected in the H-1B electronic lottery (cap-subject petitions only)","Salary at or above the prevailing wage for the occupation and work location","No adverse US immigration history"],
    "USD $730–$4,730 (employer-paid)","3–6 months standard; 15 days premium","For the petitioning employer only (portability applies after 6 months)","3 years (extendable to 6 years and beyond with PERM)","EB-2 / EB-3 employment-based green card (PERM process)")
)

NZ_VISAS = (
  acc("Student Visa","badge-student","Study",
    "The New Zealand Student Visa allows international students to study at a New Zealand educational institution for courses longer than 3 months. Students must provide evidence of enrolment, sufficient funds (NZD $20,000 per year for living costs plus tuition), and adequate health insurance. New Zealand's student pathway is particularly attractive because of the accessible Post-Study Work Visa and Skilled Migrant Category routes. GEMCA provides tailored guidance for students considering New Zealand as both an educational and long-term migration destination.",
    ["Letter of offer from a New Zealand Tertiary Education Organisation (TEO)","Proof of funds: NZD $20,000/year for living costs plus full tuition fees","Acceptable English proficiency: IELTS 5.5–6.0 or course-specific requirement","Appropriate health and travel insurance for the duration of study","Chest X-ray (TB clearance) if from a high-risk country","Police certificate if required based on length of stay and nationality","Genuine temporary entrant intent"],
    "NZD $375","4–8 weeks","20 hrs/week part-time; full-time during scheduled institution breaks","Course length + 1 month grace period","Post-Study Work Visa then Skilled Migrant Category")
+
  acc("Accredited Employer Work Visa (AEWV)","badge-work","Employer Sponsored",
    "The Accredited Employer Work Visa (AEWV) is New Zealand's primary temporary work visa, replacing the Essential Skills Visa from 2022. Workers require a job offer from an Immigration New Zealand accredited employer who has completed a Job Check demonstrating the role could not be filled from within New Zealand. The visa duration depends on the ANZSCO skill level, and Green List occupations can transition to residency quickly. GEMCA supports both employers seeking INZ accreditation and workers requiring the full visa application.",
    ["Job offer from an Immigration New Zealand (INZ) accredited employer","Job check approval completed by the employer (employer's responsibility)","Qualifications and experience appropriate for the specific role","English proficiency at NZCEL Level 3 (equivalent to IELTS 5.0) or above","Minimum NZD $29.66 per hour (or the applicable minimum wage for the role)","Valid passport and travel documents","Health and character requirements (police certificates as required)"],
    "NZD $750","4–8 weeks","Full-time for the accredited employer only","Up to 5 years (Green List occupations)","Residency (Green List Tier 1 direct; Tier 2 after 2 years employment)")
+
  acc("Skilled Migrant Category (SMC)","badge-pr","Permanent Residence",
    "The Skilled Migrant Category is New Zealand's points-based permanent residence pathway for skilled workers. Since mid-2023, the SMC uses a streamlined 6-factor points system scoring age, employment in New Zealand, work experience, qualifications, and NZ-specific experience. EOIs are submitted to the pool and selected on merit. GEMCA provides comprehensive EOI strategy, points optimisation, and complete residency application support to maximise your chances of an ITA at the best possible time.",
    ["Skilled employment in New Zealand (or a credible job offer) — mandatory requirement","Minimum points threshold met on current SMC framework (employment is the key driver)","Qualifications recognised at NQF Level 4 or above by NZQA","English proficiency: IELTS 6.5 overall with no band below 6.0","Under 56 years of age at time of EOI submission","NZQA or relevant authority assessment for non-New Zealand qualifications","Health and character requirements (medical examinations and police certificates)"],
    "NZD $4,370","12–18 months after ITA","Unrestricted (permanent)","Permanent","New Zealand Citizenship after 5 years Permanent Residency")
)

EU_VISAS = (
  acc("Germany — Student Visa (National Visa D)","badge-student","Student",
    "Germany offers tuition-free education at public universities for most international students, making it Europe's premier study destination for STEM and engineering degrees. To study in Germany for more than 90 days, a National Visa (Category D) is required, applied for at the German Embassy. Applicants must demonstrate financial capacity via a German blocked account (Sperrkonto) holding €11,904 (€992/month × 12). After graduation, an 18-month residence permit is available to find skilled employment. GEMCA assists with university applications, blocked account setup, and complete visa documentation.",
    ["Admission letter (Zulassungsbescheid) from a German university or recognised institution","German blocked account (Sperrkonto) containing €11,904 from an approved provider","Language proficiency: German B2 for German-medium courses; IELTS 6.0+ for English-medium","Health insurance meeting German statutory requirements (public or equivalent private)","Proof of accommodation in Germany (university dormitory offer or rental agreement)","Valid passport plus two biometric passport photographs","Recognised academic qualifications (may require DAAD equivalency assessment)"],
    "€75","6–12 weeks","120 full days or 240 half-days per academic year","Duration of course of study","18-month job-search permit → EU Blue Card / Skilled Worker Visa → Permanent Residence")
+
  acc("Ireland — Critical Skills Employment Permit","badge-work","Critical Skills",
    "Ireland's Critical Skills Employment Permit fast-tracks highly skilled workers in roles on the Critical Skills Occupations List. The minimum salary threshold is €38,000 for most roles and €30,000 for specific scarce-skill occupations. Unlike the General Employment Permit, there is no Labour Market Needs Test for most Critical Skills roles. After 21 months, permit holders can apply for Stamp 4 (unrestricted right to work), and are eligible for long-term residency after 5 years. GEMCA assists with permit applications, employer documentation, and IDA Ireland requirements.",
    ["Job offer for an occupation listed on the Critical Skills Occupations List","Minimum annual salary of €38,000 (most roles) or €30,000 (specific shortage occupations)","Employer must be registered with Revenue Commissioners and actively trading in Ireland","Degree or higher qualification in the relevant field (or equivalent verifiable experience)","Employment contract for a minimum of 2 years with the sponsoring Irish employer","Application through the Employment Permits Online System (EPOS)","No serious criminal convictions"],
    "€1,000 (employer-paid)","6–8 weeks","Full-time with specified employer; spouse can obtain dependent permit","2 years (renewable)","Stamp 4 after 21 months → Long-term Residency (Permanent) after 5 years")
+
  acc("Netherlands — Highly Skilled Migrant (Kennismigrant)","badge-work","Highly Skilled",
    "The Netherlands Highly Skilled Migrant permit (Kennismigrant) is one of Europe's most competitive skilled worker routes, offering fast-track IND processing in just 2 weeks, no labour market test, and a clear pathway to Dutch citizenship. In 2025, salary requirements are €5,688/month for applicants aged 30+, €4,166/month for those under 30, and €2,989/month for recent graduates within 3 years of completing their degree. GEMCA assists both professionals and their sponsoring companies with IND applications and Dutch immigration compliance.",
    ["Job offer from an IND-recognised reference sponsor employer in the Netherlands","Salary meeting the 2025 Kennismigrant threshold for your age group","Employer must hold an IND reference sponsor status (granted by IND)","Relevant qualifications and experience commensurate with the role","Valid passport with at least 6 months validity beyond the intended residence period","Tuberculosis test if required based on nationality","Registration with the Dutch Municipal Personal Records Database (BRP) within 5 days of arrival"],
    "€345","2 weeks (fast-track IND processing)","Full-time with IND-registered sponsor employer","Up to 5 years (renewable)","Dutch Permanent Residency after 5 years → EU Citizenship eligible after 5 years PR")
)


# ── HTML ASSEMBLY ────────────────────────────────────────────────────────────

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GEMCA — Goraya Education &amp; Migration Consultant Australia | MARA Registered</title>
<meta name="description" content="GEMCA is a MARA-registered migration and education consultancy in Melbourne. Expert guidance for Australian and international visa pathways — student, skilled, partner, and more. MARN 1281745. Free assessment available.">
<link rel="canonical" href="https://www.gemca.com.au">
<meta property="og:title" content="GEMCA — Education &amp; Migration Consultant Australia">
<meta property="og:description" content="MARA-registered consultancy specialising in Australian and international visas. 500+ visas processed. MARN 1281745.">
<meta property="og:url" content="https://www.gemca.com.au">
<meta property="og:type" content="website">
<meta name="robots" content="index, follow">
<link rel="icon" href="LOGO_HERE" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,300;1,9..40,400&display=swap" rel="stylesheet">
"""

OPERA_SVG = """<svg viewBox="0 0 500 255" xmlns="http://www.w3.org/2000/svg" aria-label="Sydney Opera House line-art" style="width:100%;display:block">
  <defs>
    <filter id="og" x="-18%" y="-30%" width="136%" height="160%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feColorMatrix in="b" values="1 .85 .3 0 .04 .85 .65 .2 0 .02 .2 .1 0 0 0 0 0 0 .55 0" result="g"/>
      <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="sf" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E2C48A" stop-opacity=".18"/>
      <stop offset="100%" stop-color="#C8A96E" stop-opacity=".06"/>
    </linearGradient>
  </defs>
  <!-- subtle fill inside shells -->
  <path d="M78,232 C72,190 80,145 96,105 C114,58 138,26 156,20 C166,16 173,24 169,49 C162,82 148,122 128,163 C112,196 95,218 78,232Z" fill="url(#sf)"/>
  <path d="M105,232 C100,196 108,160 122,130 C139,93 159,61 174,50 C184,44 190,52 185,76 C178,105 163,141 147,173 C132,200 115,221 105,232Z" fill="url(#sf)"/>
  <path d="M130,232 C127,202 134,172 148,148 C165,118 183,91 196,80 C205,73 211,81 208,103 C203,131 188,163 172,191 C158,214 137,229 130,232Z" fill="url(#sf)"/>
  <path d="M154,232 C152,207 158,182 170,160 C184,133 201,108 213,98 C221,92 226,100 224,121 C219,148 205,177 190,202 C177,223 160,233 154,232Z" fill="url(#sf)"/>
  <path d="M266,232 C263,208 268,183 280,160 C294,133 312,108 325,100 C333,94 338,103 336,124 C331,152 317,178 302,202 C288,221 271,233 266,232Z" fill="url(#sf)"/>
  <path d="M285,232 C283,213 288,192 299,172 C313,148 329,128 339,120 C347,114 351,122 349,142 C345,166 332,190 318,210 C306,226 290,234 285,232Z" fill="url(#sf)"/>
  <path d="M303,232 C302,216 306,200 315,184 C327,163 341,146 350,139 C357,133 360,141 359,159 C356,182 345,203 332,218 C322,230 308,234 303,232Z" fill="url(#sf)"/>
  <!-- gold outline shells — concert hall (left group) -->
  <g filter="url(#og)" fill="none" stroke="#C8A96E" stroke-linecap="round" stroke-linejoin="round">
    <path stroke-width="2.5" d="M78,232 C72,190 80,145 96,105 C114,58 138,26 156,20 C166,16 173,24 169,49 C162,82 148,122 128,163 C112,196 95,218 78,232"/>
    <path stroke-width="2.2" d="M105,232 C100,196 108,160 122,130 C139,93 159,61 174,50 C184,44 190,52 185,76 C178,105 163,141 147,173 C132,200 115,221 105,232"/>
    <path stroke-width="1.9" d="M130,232 C127,202 134,172 148,148 C165,118 183,91 196,80 C205,73 211,81 208,103 C203,131 188,163 172,191 C158,214 137,229 130,232"/>
    <path stroke-width="1.6" d="M154,232 C152,207 158,182 170,160 C184,133 201,108 213,98 C221,92 226,100 224,121 C219,148 205,177 190,202 C177,223 160,233 154,232"/>
    <!-- opera theatre (right group) -->
    <path stroke-width="2.2" d="M266,232 C263,208 268,183 280,160 C294,133 312,108 325,100 C333,94 338,103 336,124 C331,152 317,178 302,202 C288,221 271,233 266,232"/>
    <path stroke-width="1.9" d="M285,232 C283,213 288,192 299,172 C313,148 329,128 339,120 C347,114 351,122 349,142 C345,166 332,190 318,210 C306,226 290,234 285,232"/>
    <path stroke-width="1.6" d="M303,232 C302,216 306,200 315,184 C327,163 341,146 350,139 C357,133 360,141 359,159 C356,182 345,203 332,218 C322,230 308,234 303,232"/>
  </g>
  <!-- bright tips on tallest shells -->
  <path d="M154,20 C162,13 170,19" fill="none" stroke="#F0D880" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M323,99 C331,93 337,101" fill="none" stroke="#F0D880" stroke-width="2" stroke-linecap="round"/>
  <!-- platform -->
  <line x1="48" y1="236" x2="430" y2="236" stroke="#C8A96E" stroke-width="1.6" opacity=".7"/>
  <line x1="38" y1="240" x2="440" y2="240" stroke="#C8A96E" stroke-width=".8" opacity=".4"/>
  <!-- steps -->
  <line x1="55" y1="233" x2="415" y2="233" stroke="rgba(200,169,110,.25)" stroke-width=".8"/>
  <line x1="62" y1="230" x2="410" y2="230" stroke="rgba(200,169,110,.15)" stroke-width=".6"/>
  <!-- water reflection dashes -->
  <g stroke="#C8A96E" stroke-linecap="round" opacity=".22">
    <line x1="110" y1="247" x2="160" y2="247" stroke-width="1.5"/>
    <line x1="175" y1="247" x2="225" y2="247" stroke-width="1.5"/>
    <line x1="240" y1="247" x2="290" y2="247" stroke-width="1.5"/>
    <line x1="305" y1="247" x2="355" y2="247" stroke-width="1.5"/>
    <line x1="130" y1="252" x2="190" y2="252" stroke-width="1"/>
    <line x1="210" y1="252" x2="270" y2="252" stroke-width="1"/>
    <line x1="290" y1="252" x2="340" y2="252" stroke-width="1"/>
  </g>
</svg>"""

PARTICLES = "".join(
  f'<div class="pt" style="left:{l}%;top:{t}%;--pdur:{d}s;--pdel:{dl}s"></div>'
  for l,t,d,dl in [
    (8,70,9,0),(15,55,7,-2),(22,80,11,-5),(30,40,8,-1),(40,65,10,-3),
    (52,75,7,-6),(60,50,9,-.5),(70,60,12,-4),(78,45,8,-7),(85,72,10,-2.5),
    (92,35,6,-1.5),(48,30,9,-8),(25,25,11,-3.5),(65,85,7,-9),(5,30,13,-4.5),
    (90,80,8,-6.5),(35,90,10,-1.2),(72,20,9,-7.5),(12,15,12,-5.5),(55,18,8,-.8)
  ]
)

BODY = f"""
<body>

<!-- AURORA -->
<div class="aurora" aria-hidden="true">
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>
</div>

<!-- MOBILE MENU -->
<nav id="mobile-menu" aria-label="Mobile navigation" aria-hidden="true">
  <a href="#about" onclick="closeMenu()">About</a>
  <a href="#services" onclick="closeMenu()">Services</a>
  <a href="#countries" onclick="closeMenu()">Countries &amp; Visas</a>
  <a href="#why" onclick="closeMenu()">Why GEMCA</a>
  <a href="#testimonials" onclick="closeMenu()">Testimonials</a>
  <a href="#assessment" onclick="closeMenu()">Free Assessment</a>
  <a href="#contact" onclick="closeMenu()">Contact</a>
  <a href="#assessment" onclick="closeMenu()" class="mm-cta">Book Free Assessment →</a>
</nav>

<!-- NAVBAR -->
<header>
<nav id="navbar" role="navigation" aria-label="Main navigation">
  <a href="#" class="logo-link" aria-label="GEMCA — Home">
    <img src="LOGO_HERE" alt="GEMCA Crystal Logo" class="logo-img" width="46" height="46">
    <div class="logo-wordmark">
      <div class="logo-name">GEMC<span class="a-gold">A</span></div>
      <div class="logo-tag">Excellence · Integrity · Collaboration · Impact</div>
    </div>
  </a>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li class="dropdown">
      <button class="dropdown-toggle" aria-haspopup="true" aria-expanded="false">
        Services <i class="chevron">▾</i>
      </button>
      <div class="dropdown-menu" role="menu">
        <a href="#services" role="menuitem">🎓 Student Visas</a>
        <a href="#services" role="menuitem">⭐ Skilled Migration</a>
        <a href="#services" role="menuitem">🏢 Employer Sponsored</a>
        <a href="#services" role="menuitem">❤️ Partner &amp; Family</a>
        <a href="#services" role="menuitem">⚖️ Appeals &amp; Reviews</a>
        <a href="#services" role="menuitem">📋 Skills Assessments</a>
      </div>
    </li>
    <li class="dropdown">
      <button class="dropdown-toggle" aria-haspopup="true" aria-expanded="false">
        Countries <i class="chevron">▾</i>
      </button>
      <div class="dropdown-menu" role="menu">
        <a href="#countries" onclick="showCountry('au')" role="menuitem">🇦🇺 Australia</a>
        <a href="#countries" onclick="showCountry('uk')" role="menuitem">🇬🇧 United Kingdom</a>
        <a href="#countries" onclick="showCountry('ca')" role="menuitem">🇨🇦 Canada</a>
        <a href="#countries" onclick="showCountry('us')" role="menuitem">🇺🇸 United States</a>
        <a href="#countries" onclick="showCountry('nz')" role="menuitem">🇳🇿 New Zealand</a>
        <a href="#countries" onclick="showCountry('eu')" role="menuitem">🇪🇺 Europe</a>
      </div>
    </li>
    <li><a href="#why">Why GEMCA</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#assessment" class="nav-cta">Free Assessment</a></li>
  </ul>
  <button class="hamburger" id="hamburger" onclick="toggleMenu()" aria-label="Toggle mobile menu" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
</nav>
</header>

<!-- ═══════════════════════ HERO ═══════════════════════ -->
<main>
<section id="hero" aria-label="Hero">
  <div class="container">
    <div class="hero-grid">

      <!-- LEFT -->
      <div class="hero-left">
        <div class="reveal">
          <div class="hero-badge">
            <span class="hero-badge-dot"></span>
            MARA Registered &nbsp;·&nbsp; Truganina VIC &nbsp;·&nbsp; Est. 2014
          </div>
        </div>
        <h1 class="hero-title reveal reveal-d1">
          Your Gateway to<br>
          <em>Global Education</em><br>
          &amp; Migration
        </h1>
        <p class="hero-sub reveal reveal-d2">
          GEMCA guides students, families, and professionals through every step of the visa journey — from free assessment to visa grant. MARA-registered, results-driven, Melbourne-based.
        </p>
        <div class="hero-ctas reveal reveal-d3">
          <a href="#assessment" class="btn-primary">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 1a7 7 0 110 14A7 7 0 018 1zm0 1.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zm.75 2.75a.75.75 0 010 1.5H8.75v2.5h1.5a.75.75 0 010 1.5H6.75a.75.75 0 010-1.5h.5v-2.5h-.5a.75.75 0 010-1.5h2z"/></svg>
            Book Free Assessment
          </a>
          <a href="#countries" class="btn-outline">Explore Countries</a>
          <a href="https://wa.me/61413769458" target="_blank" rel="noopener noreferrer" class="btn-ghost">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            WhatsApp Us
          </a>
        </div>
        <div class="flag-chips reveal reveal-d4">
          <span class="flag-chip"><span class="flag">🇦🇺</span> Australia</span>
          <span class="flag-chip"><span class="flag">🇬🇧</span> UK</span>
          <span class="flag-chip"><span class="flag">🇨🇦</span> Canada</span>
          <span class="flag-chip"><span class="flag">🇺🇸</span> USA</span>
          <span class="flag-chip"><span class="flag">🇳🇿</span> NZ</span>
          <span class="flag-chip"><span class="flag">🇪🇺</span> Europe</span>
        </div>
        <p class="hero-fine reveal reveal-d5">* All outcomes subject to eligibility and respective country immigration requirements.</p>
      </div>

      <!-- RIGHT -->
      <div class="hero-right" aria-hidden="true">
        <div class="hero-right-inner">
          <!-- particles -->
          <div class="particles">{PARTICLES}</div>
          <!-- floating logo -->
          <div class="hero-logo-float">
            <img src="LOGO_HERE" alt="" width="88" height="88">
          </div>
          <!-- flag cards -->
          <div class="flag-cards-wrap">
            <div class="fc fc-au"><span class="fc-emoji">🇦🇺</span><span class="fc-country">Australia</span><span class="fc-label">Visas Available</span></div>
            <div class="fc fc-uk"><span class="fc-emoji">🇬🇧</span><span class="fc-country">United Kingdom</span><span class="fc-label">Visas Available</span></div>
            <div class="fc fc-ca"><span class="fc-emoji">🇨🇦</span><span class="fc-country">Canada</span><span class="fc-label">Visas Available</span></div>
            <div class="fc fc-us"><span class="fc-emoji">🇺🇸</span><span class="fc-country">United States</span><span class="fc-label">Visas Available</span></div>
            <div class="fc fc-nz"><span class="fc-emoji">🇳🇿</span><span class="fc-country">New Zealand</span><span class="fc-label">Visas Available</span></div>
            <div class="fc fc-eu"><span class="fc-emoji">🇪🇺</span><span class="fc-country">Europe</span><span class="fc-label">Visas Available</span></div>
          </div>
          <!-- opera glow + building -->
          <div class="opera-glow"></div>
          <div class="opera-wrap">{OPERA_SVG}</div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ═══════════════════════ STATS ═══════════════════════ -->
<div class="stats-bar" role="region" aria-label="Key statistics">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-item reveal"><div class="stat-num">500+</div><div class="stat-lbl">Visas Processed</div></div>
      <div class="stat-item reveal reveal-d1"><div class="stat-num">98%</div><div class="stat-lbl">Success Rate</div></div>
      <div class="stat-item reveal reveal-d2"><div class="stat-num">6</div><div class="stat-lbl">Countries</div></div>
      <div class="stat-item reveal reveal-d3"><div class="stat-num">10+</div><div class="stat-lbl">Years Experience</div></div>
      <div class="stat-item reveal reveal-d4"><div class="stat-num">50+</div><div class="stat-lbl">Nationalities Served</div></div>
    </div>
  </div>
</div>

<!-- ═══════════════════════ ABOUT ═══════════════════════ -->
<section id="about" aria-labelledby="about-heading">
  <div class="container">
    <div class="about-grid">
      <div class="about-img-side reveal">
        <div class="about-card-visual glass-card">
          <div class="about-quote">"We don't just process paperwork — we invest in your future."</div>
          <div class="about-quote-attr">— GEMCA Team, Melbourne VIC</div>
        </div>
      </div>
      <div class="about-text reveal reveal-d1">
        <span class="section-eyebrow">About GEMCA</span>
        <h2 id="about-heading" class="section-title" style="text-align:left;margin-bottom:1rem">
          MARA-Registered Experts<br><em>Based in Melbourne</em>
        </h2>
        <p>Goraya Education &amp; Migration Consultant Australia (GEMCA) is a MARA-registered migration and education consultancy headquartered in Truganina, Melbourne. We specialise in Australian and international visa pathways, serving clients from over 50 nationalities.</p>
        <p>Our registered migration agent, Mubashar Ahmed Nizamani (MARN 1281745), brings over a decade of experience across student, skilled, employer-sponsored, partner, and family visa categories. Every case receives personalised strategy, full documentation support, and transparent communication from assessment to grant.</p>
        <p>We operate under the Migration Agents Code of Conduct and are committed to honest, ethical advice — never overpromising, always delivering our best professional effort.</p>
        <div class="info-boxes">
          <div class="info-box">
            <div class="info-box-label">Office Address</div>
            <div class="info-box-val">8 Tallis Circuit<br>Truganina VIC 3029</div>
          </div>
          <div class="info-box">
            <div class="info-box-label">Phone</div>
            <div class="info-box-val"><a href="tel:0413769458">0413 769 458</a> (Mobile)<br><a href="tel:0370203358">03 7020 3358</a> (Office)</div>
          </div>
          <div class="info-box">
            <div class="info-box-label">Email &amp; Web</div>
            <div class="info-box-val"><a href="mailto:ansar@gemca.com.au">ansar@gemca.com.au</a><br><a href="https://www.gemca.com.au">www.gemca.com.au</a></div>
          </div>
          <div class="info-box">
            <div class="info-box-label">Office Hours</div>
            <div class="info-box-val">Mon–Fri 9am–6pm<br>Sat 10am–3pm · Sun by appt</div>
          </div>
        </div>
        <div class="about-banner">
          <span>ABN 96 695 178 744</span>
          <span class="sep">·</span>
          <span>MARN 1281745</span>
          <span class="sep">·</span>
          <span>Migration Agents Code of Conduct</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════ SERVICES ═══════════════════════ -->
<section id="services" aria-labelledby="services-heading">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">What We Do</span>
      <h2 id="services-heading" class="section-title">Expert Guidance <em>Across Every Pathway</em></h2>
      <div class="gold-divider"></div>
    </div>
    <div class="services-grid">
      <div class="glass-card srv-card reveal">
        <div class="srv-icon">🎓</div>
        <h3 class="srv-title">Student Visas</h3>
        <p class="srv-desc">End-to-end support for international students applying to universities and colleges in Australia, UK, Canada, USA, New Zealand, and Europe. Institutional selection, GTE statements, and full application management.</p>
        <a href="#countries" class="srv-link">Explore student visas →</a>
      </div>
      <div class="glass-card srv-card reveal reveal-d1">
        <div class="srv-icon">⭐</div>
        <h3 class="srv-title">Skilled Migration</h3>
        <p class="srv-desc">Points-tested pathways including SC 189, 190, 491, and Express Entry Canada. We optimise your EOI, manage skills assessments, and prepare compelling applications for permanent residency.</p>
        <a href="#countries" class="srv-link">View skilled visas →</a>
      </div>
      <div class="glass-card srv-card reveal reveal-d2">
        <div class="srv-icon">🏢</div>
        <h3 class="srv-title">Employer Sponsored</h3>
        <p class="srv-desc">SC 482 Skills in Demand, SC 186 ENS, UK Skilled Worker, and Canada PNP. We work with both employers seeking sponsorship approval and employees seeking nomination — end-to-end.</p>
        <a href="#countries" class="srv-link">View work visas →</a>
      </div>
      <div class="glass-card srv-card reveal reveal-d1">
        <div class="srv-icon">❤️</div>
        <h3 class="srv-title">Partner &amp; Family</h3>
        <p class="srv-desc">SC 820/801 Partner visas, Parent visas (103/143), and dependent applications. We compile comprehensive relationship evidence packages and manage every aspect of your family's application.</p>
        <a href="#countries" class="srv-link">View family visas →</a>
      </div>
      <div class="glass-card srv-card reveal reveal-d2">
        <div class="srv-icon">⚖️</div>
        <h3 class="srv-title">Appeals &amp; Reviews</h3>
        <p class="srv-desc">Representation at the Administrative Review Tribunal (ART), merits review, and judicial review strategy. We also assist with ministerial intervention requests and character waiver applications.</p>
        <a href="#contact" class="srv-link">Get urgent help →</a>
      </div>
      <div class="glass-card srv-card reveal reveal-d3">
        <div class="srv-icon">📋</div>
        <h3 class="srv-title">Skills Assessments</h3>
        <p class="srv-desc">Guidance for assessments with Engineers Australia, VETASSESS, ACS, TRA, AHPRA, ANMAC, and other assessing authorities. We review your qualifications profile and maximise assessment outcomes.</p>
        <a href="#assessment" class="srv-link">Start free assessment →</a>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════ COUNTRIES ═══════════════════════ -->
<section id="countries" aria-labelledby="countries-heading">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Countries &amp; Visas</span>
      <h2 id="countries-heading" class="section-title">Global Pathways, <em>Expert Guidance</em></h2>
      <div class="gold-divider"></div>
    </div>
    <div class="tab-bar" role="tablist" aria-label="Country selection">
      <button class="tab-btn active" data-tab="au" onclick="showCountry('au')" role="tab" aria-selected="true" aria-controls="tab-au">🇦🇺 Australia</button>
      <button class="tab-btn" data-tab="uk" onclick="showCountry('uk')" role="tab" aria-selected="false" aria-controls="tab-uk">🇬🇧 United Kingdom</button>
      <button class="tab-btn" data-tab="ca" onclick="showCountry('ca')" role="tab" aria-selected="false" aria-controls="tab-ca">🇨🇦 Canada</button>
      <button class="tab-btn" data-tab="us" onclick="showCountry('us')" role="tab" aria-selected="false" aria-controls="tab-us">🇺🇸 United States</button>
      <button class="tab-btn" data-tab="nz" onclick="showCountry('nz')" role="tab" aria-selected="false" aria-controls="tab-nz">🇳🇿 New Zealand</button>
      <button class="tab-btn" data-tab="eu" onclick="showCountry('eu')" role="tab" aria-selected="false" aria-controls="tab-eu">🇪🇺 Europe</button>
    </div>
"""

AU_UNIS = ["University of Melbourne","University of Sydney","Australian National University","University of Queensland","Monash University","UNSW Sydney","Deakin University","RMIT University","Victoria University","La Trobe University","Swinburne University"]
UK_UNIS = ["University of Oxford","University of Cambridge","Imperial College London","University College London","University of Edinburgh","University of Manchester","King's College London","University of Bristol"]
CA_UNIS = ["University of Toronto","McGill University","University of British Columbia","University of Waterloo","Humber College","Seneca College","George Brown College","York University"]
US_UNIS = ["MIT","Harvard University","Stanford University","Yale University","Columbia University","University of Chicago","UCLA","UC Berkeley"]
NZ_UNIS = ["University of Auckland","Victoria University of Wellington","University of Otago","University of Canterbury","Auckland University of Technology","Massey University"]
EU_UNIS = ["ETH Zurich","TU Munich","University of Amsterdam","Trinity College Dublin","Sorbonne University","Heidelberg University","LMU Munich","TU Delft","Uppsala University","Sciences Po Paris"]

COUNTRIES_PANELS = (
  country_panel("au","🇦🇺","Australia",
    "Australia's migration system offers some of the world's most structured and transparent pathways — from student and graduate visas to permanent residency and citizenship. GEMCA is based in Melbourne and has deep expertise across all Australian visa categories.",
    ("8","Visa Subclasses"),("2025–26","Fees Updated"),("MARA","Registered Agent"),
    AU_VISAS, AU_UNIS)
+
  country_panel("uk","🇬🇧","United Kingdom",
    "The UK points-based immigration system offers competitive pathways for students, graduates, and skilled workers. Post-Brexit reforms have created clear routes via the Student, Graduate, and Skilled Worker visa categories.",
    ("4","Visa Pathways"),("£363+","Starting From"),("Top 6","Universities"),
    UK_VISAS, UK_UNIS)
+
  country_panel("ca","🇨🇦","Canada",
    "Canada's Express Entry and Provincial Nominee Programs are among the world's most welcoming immigration frameworks. The introduction of PAL requirements for study permits reflects Canada's focus on managed, high-quality international enrolment.",
    ("4","Visa Pathways"),("CAD $150+","Starting From"),("6","Partner Colleges"),
    CA_VISAS, CA_UNIS)
+
  country_panel("us","🇺🇸","United States",
    "The United States hosts the world's largest concentration of top-ranked universities. GEMCA provides strategic guidance on F-1 and J-1 visas, OPT planning, and H-1B lottery preparation for post-graduation work pathways.",
    ("3","Visa Categories"),("USD $185+","Starting From"),("Top 8","Universities"),
    US_VISAS, US_UNIS)
+
  country_panel("nz","🇳🇿","New Zealand",
    "New Zealand offers a welcoming environment for international students and skilled migrants. The Skilled Migrant Category and Green List provide clear pathways to permanent residence, especially for healthcare and engineering professionals.",
    ("3","Visa Pathways"),("NZD $375+","Starting From"),("6","Universities"),
    NZ_VISAS, NZ_UNIS)
+
  country_panel("eu","🇪🇺","Europe",
    "Europe's diverse study and work options include Germany's tuition-free universities, Ireland's Critical Skills permits, and the Netherlands' fast-track Highly Skilled Migrant route. GEMCA helps clients navigate each country's specific requirements.",
    ("3","Visa Routes"),("€75+","Starting From"),("10","Universities"),
    EU_VISAS, EU_UNIS)
)

COUNTRIES_SECTION_END = """
  </div>
</section>

<!-- ═══════════════════════ WHY GEMCA ═══════════════════════ -->
<section id="why" aria-labelledby="why-heading">
  <div class="container">
    <div class="why-grid">
      <div class="reveal">
        <span class="section-eyebrow">Why Choose Us</span>
        <h2 id="why-heading" class="section-title" style="text-align:left;margin-bottom:2rem">
          Five Reasons to Trust<br><em>GEMCA</em>
        </h2>
        <div class="reasons-list">
          <div class="reason-item">
            <div class="reason-num">1</div>
            <div>
              <div class="reason-title">MARA-Registered &amp; Fully Accountable</div>
              <div class="reason-desc">Our registered agent Mubashar Ahmed Nizamani (MARN 1281745) operates under the Migration Agents Code of Conduct. You receive legally protected, professionally accountable advice — not informal guidance.</div>
            </div>
          </div>
          <div class="reason-item">
            <div class="reason-num">2</div>
            <div>
              <div class="reason-title">98% Success Rate Across 500+ Cases</div>
              <div class="reason-desc">A decade of client outcomes across student, skilled, employer-sponsored, and partner visa categories. We only take cases we believe in and prepare every application to the highest standard.</div>
            </div>
          </div>
          <div class="reason-item">
            <div class="reason-num">3</div>
            <div>
              <div class="reason-title">6-Country Expertise</div>
              <div class="reason-desc">From Australian SC 189 to UK Graduate Route to Canadian Express Entry — we have active expertise in immigration to Australia, UK, Canada, USA, New Zealand, and Europe.</div>
            </div>
          </div>
          <div class="reason-item">
            <div class="reason-num">4</div>
            <div>
              <div class="reason-title">Multilingual, Multicultural Team</div>
              <div class="reason-desc">Serving 50+ nationalities from our Melbourne base. Consultations available in person, by phone, and online — in English, Urdu, Punjabi, and Hindi.</div>
            </div>
          </div>
          <div class="reason-item">
            <div class="reason-num">5</div>
            <div>
              <div class="reason-title">Transparent, Fixed Pricing</div>
              <div class="reason-desc">Clear fee agreements before any work begins. No hidden charges. Scope of services is documented in writing. Your trust is our most valuable asset.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="reveal reveal-d2">
        <div class="card-stack">
          <div class="stack-card stack-card-3 glass-card">
            <div class="sc-badge">● Processing</div>
            <div class="sc-number">SC 189</div>
            <div class="sc-sub">Skilled Independent — Perth WA</div>
          </div>
          <div class="stack-card stack-card-2 glass-card" style="animation-name:stack-float-2">
            <div class="sc-badge">● In Review</div>
            <div class="sc-number">SC 482</div>
            <div class="sc-sub">Skills in Demand — Sydney NSW</div>
            <div class="sc-divider"></div>
            <div class="sc-pills">
              <span class="sc-pill">CRS 478</span>
              <span class="sc-pill">Engineering</span>
            </div>
          </div>
          <div class="stack-card stack-card-1 glass-card">
            <div class="sc-badge">● Visa Approved</div>
            <div class="sc-number">SC 190</div>
            <div class="sc-sub">State Nominated — Melbourne VIC</div>
            <div class="sc-divider"></div>
            <div class="sc-pills">
              <span class="sc-pill">95 Points</span>
              <span class="sc-pill">Accountant</span>
              <span class="sc-pill">VIC Nominated</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════ TESTIMONIALS ═══════════════════════ -->
<section id="testimonials" aria-labelledby="testi-heading">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Client Stories</span>
      <h2 id="testi-heading" class="section-title">Trusted by Families <em>Across the Globe</em></h2>
      <div class="gold-divider"></div>
    </div>
    <div class="testi-grid">
      <div class="glass-card testi-card reveal">
        <div class="testi-stars">★★★★★</div>
        <p class="testi-quote">"GEMCA made what felt like an impossible process completely manageable. Our SC 190 was approved first time, and Mubashar kept us informed at every single step. I cannot recommend this team highly enough."</p>
        <div class="testi-author">
          <div class="testi-avatar">R</div>
          <div>
            <div class="testi-name">Rajpreet S.</div>
            <div class="testi-visa">SC 190 — State Nominated PR, VIC</div>
          </div>
        </div>
      </div>
      <div class="glass-card testi-card reveal reveal-d1">
        <div class="testi-stars">★★★★★</div>
        <p class="testi-quote">"As an international student with a complicated situation, I needed someone I could trust completely. GEMCA's advice on my SC 500 GTE statement was brilliant — visa granted with no further requests. Professional, responsive, outstanding."</p>
        <div class="testi-author">
          <div class="testi-avatar">A</div>
          <div>
            <div class="testi-name">Amira M.</div>
            <div class="testi-visa">SC 500 — Student Visa, Melbourne</div>
          </div>
        </div>
      </div>
      <div class="glass-card testi-card reveal reveal-d2">
        <div class="testi-stars">★★★★★</div>
        <p class="testi-quote">"We were devastated when our partner visa was delayed. GEMCA intervened with a detailed response, and our SC 820 was finalised within weeks. They treated our case as if it were their own family's. We are forever grateful."</p>
        <div class="testi-author">
          <div class="testi-avatar">K</div>
          <div>
            <div class="testi-name">Kofi &amp; Theresa A.</div>
            <div class="testi-visa">SC 820 / 801 — Partner Visa</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════ COMPLIANCE ═══════════════════════ -->
<section id="compliance" aria-label="Compliance information">
  <div class="container">
    <div class="compliance-box">
      <div class="compliance-icon">🛡️</div>
      <div class="compliance-text">
        <h4>Registered Migration Agent — Your Legal Protection</h4>
        <p>GEMCA's migration services are provided by Mubashar Ahmed Nizamani, a registered member of the Migration Agents Registration Authority (MARA). All advice is provided in accordance with the <strong>Migration Agents Code of Conduct</strong>. We never guarantee visa outcomes — all applications are subject to eligibility and the requirements of the relevant immigration authority. ABN 96 695 178 744.</p>
      </div>
      <div class="compliance-marn">
        <div class="marn-num">MARN 1281745</div>
        <div class="marn-sub">MARA Registered</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════ FREE ASSESSMENT ═══════════════════════ -->
<section id="assessment" aria-labelledby="assessment-heading">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Get Started</span>
      <h2 id="assessment-heading" class="section-title">Book Your <em>Free Assessment</em></h2>
      <div class="gold-divider"></div>
    </div>
    <div class="form-grid">
      <div class="reveal">
        <p style="color:var(--muted);margin-bottom:1.5rem;line-height:1.75">Our free 30-minute consultation covers your current situation, the best visa pathway for your goals, and a clear next-steps plan — all at no cost and no obligation.</p>
        <div class="form-checklist">
          <div class="checklist-item">Personalised pathway assessment based on your profile</div>
          <div class="checklist-item">Eligibility check across Australian and international options</div>
          <div class="checklist-item">Skills assessment strategy and timeline planning</div>
          <div class="checklist-item">Clear fee structure before any engagement</div>
          <div class="checklist-item">Available in person, by phone, or online</div>
          <div class="checklist-item">Response within 24 business hours, guaranteed</div>
        </div>
      </div>
      <div class="reveal reveal-d1">
        <div class="form-box" id="assessment-form-wrap">
          <form id="assessment-form" novalidate>
            <div class="form-row">
              <div class="form-group">
                <label class="form-label" for="a-fname">First Name *</label>
                <input type="text" id="a-fname" name="first_name" class="form-input" placeholder="First name" required autocomplete="given-name">
              </div>
              <div class="form-group">
                <label class="form-label" for="a-lname">Last Name *</label>
                <input type="text" id="a-lname" name="last_name" class="form-input" placeholder="Last name" required autocomplete="family-name">
              </div>
            </div>
            <div class="form-group">
              <label class="form-label" for="a-email">Email Address *</label>
              <input type="email" id="a-email" name="email" class="form-input" placeholder="your@email.com" required autocomplete="email">
            </div>
            <div class="form-group">
              <label class="form-label" for="a-phone">Phone Number</label>
              <input type="tel" id="a-phone" name="phone" class="form-input" placeholder="+61 4XX XXX XXX" autocomplete="tel">
            </div>
            <div class="form-group">
              <label class="form-label" for="a-country">Destination Country *</label>
              <select id="a-country" name="destination" class="form-select" required>
                <option value="" disabled selected>Select a country</option>
                <option value="australia">🇦🇺 Australia</option>
                <option value="uk">🇬🇧 United Kingdom</option>
                <option value="canada">🇨🇦 Canada</option>
                <option value="usa">🇺🇸 United States</option>
                <option value="newzealand">🇳🇿 New Zealand</option>
                <option value="europe">🇪🇺 Europe</option>
                <option value="other">🌍 Other / Not sure</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label" for="a-visa">Visa Type</label>
              <select id="a-visa" name="visa_type" class="form-select">
                <option value="" disabled selected>Select visa type</option>
                <option value="student">Student Visa</option>
                <option value="skilled">Skilled Migration / Points-tested</option>
                <option value="employer">Employer Sponsored</option>
                <option value="partner">Partner or Family</option>
                <option value="visitor">Visitor / Tourist</option>
                <option value="appeals">Appeals / Review</option>
                <option value="unsure">Not sure — need advice</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label" for="a-msg">Brief Description</label>
              <textarea id="a-msg" name="message" class="form-textarea" placeholder="Tell us a little about your situation and goals…"></textarea>
            </div>
            <div class="form-group">
              <label class="form-consent">
                <input type="checkbox" id="a-consent" name="consent" required>
                I consent to GEMCA contacting me about my assessment. I understand this is not legal advice and no fees are charged for this initial consultation. *
              </label>
            </div>
            <div class="form-submit">
              <button type="button" class="btn-primary submit-btn" onclick="submitAssessment()" id="a-submit-btn">
                <div class="spinner" id="a-spinner" aria-hidden="true"></div>
                <span class="btn-text" id="a-btn-text">Submit Assessment Request</span>
              </button>
            </div>
          </form>
          <div class="form-success" id="assessment-success" aria-live="polite">
            <div class="success-icon">✅</div>
            <h4>Received — Thank You!</h4>
            <p>We'll review your details and reply within 24 hours. For urgent matters call <a href="tel:0413769458" style="color:var(--gold)">0413 769 458</a>.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════ CONTACT ═══════════════════════ -->
<section id="contact" aria-labelledby="contact-heading">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Get in Touch</span>
      <h2 id="contact-heading" class="section-title">We're Here to <em>Help You</em></h2>
      <div class="gold-divider"></div>
    </div>
    <div class="contact-grid">
      <div class="reveal">
        <div class="contact-cards">
          <div class="contact-card">
            <div class="cc-icon">📍</div>
            <div class="cc-label">Office</div>
            <div class="cc-val">8 Tallis Circuit<br>Truganina VIC 3029</div>
          </div>
          <div class="contact-card">
            <div class="cc-icon">📱</div>
            <div class="cc-label">Mobile</div>
            <div class="cc-val"><a href="tel:0413769458">0413 769 458</a></div>
          </div>
          <div class="contact-card">
            <div class="cc-icon">☎️</div>
            <div class="cc-label">Landline</div>
            <div class="cc-val"><a href="tel:0370203358">03 7020 3358</a></div>
          </div>
          <div class="contact-card">
            <div class="cc-icon">✉️</div>
            <div class="cc-label">Email</div>
            <div class="cc-val"><a href="mailto:ansar@gemca.com.au">ansar@gemca.com.au</a></div>
          </div>
          <div class="contact-card">
            <div class="cc-icon">🕐</div>
            <div class="cc-label">Hours</div>
            <div class="cc-val">Mon–Fri 9am–6pm<br>Sat 10am–3pm<br>Sun by appointment</div>
          </div>
          <div class="contact-card">
            <div class="cc-icon">💬</div>
            <div class="cc-label">WhatsApp</div>
            <div class="cc-val"><a href="https://wa.me/61413769458" target="_blank" rel="noopener noreferrer">wa.me/61413769458</a></div>
          </div>
        </div>
      </div>
      <div class="reveal reveal-d1">
        <div class="form-box" id="contact-form-wrap">
          <h3 style="font-family:var(--font-d);font-size:1.5rem;font-weight:300;color:#fff;margin-bottom:1.5rem">Send Us a Message</h3>
          <form id="contact-form" novalidate>
            <div class="form-row">
              <div class="form-group">
                <label class="form-label" for="c-name">Full Name *</label>
                <input type="text" id="c-name" name="name" class="form-input" placeholder="Your full name" required autocomplete="name">
              </div>
              <div class="form-group">
                <label class="form-label" for="c-phone">Phone</label>
                <input type="tel" id="c-phone" name="phone" class="form-input" placeholder="+61 4XX XXX XXX" autocomplete="tel">
              </div>
            </div>
            <div class="form-group">
              <label class="form-label" for="c-email">Email Address *</label>
              <input type="email" id="c-email" name="email" class="form-input" placeholder="your@email.com" required autocomplete="email">
            </div>
            <div class="form-group">
              <label class="form-label" for="c-subject">Subject</label>
              <input type="text" id="c-subject" name="subject" class="form-input" placeholder="How can we help?">
            </div>
            <div class="form-group">
              <label class="form-label" for="c-msg">Message *</label>
              <textarea id="c-msg" name="message" class="form-textarea" placeholder="Please describe your situation or question…" style="min-height:140px" required></textarea>
            </div>
            <div class="form-group">
              <label class="form-consent">
                <input type="checkbox" id="c-consent" name="consent" required>
                I consent to GEMCA storing and using this information to respond to my enquiry. *
              </label>
            </div>
            <div class="form-submit">
              <button type="button" class="btn-primary submit-btn" onclick="submitContact()" id="c-submit-btn">
                <div class="spinner" id="c-spinner" aria-hidden="true"></div>
                <span class="btn-text" id="c-btn-text">Send Message</span>
              </button>
            </div>
          </form>
          <div class="form-success" id="contact-success" aria-live="polite">
            <div class="success-icon">✅</div>
            <h4>Received — we'll reply within 24 hours</h4>
            <p>Thank you for reaching out. A member of our team will be in contact shortly.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</main>

<!-- ═══════════════════════ FOOTER ═══════════════════════ -->
<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand-logo">
          <img src="LOGO_HERE" alt="GEMCA Logo" class="footer-logo-img" width="44" height="44">
          <div class="logo-wordmark">
            <div class="logo-name" style="font-size:17px">GEMC<span class="a-gold">A</span></div>
            <div class="logo-tag">Excellence · Integrity · Collaboration · Impact</div>
          </div>
        </div>
        <p class="footer-desc">Goraya Education &amp; Migration Consultant Australia — MARA-registered migration and education consultancy in Melbourne, Victoria. Expert, ethical guidance for every visa journey.</p>
        <p class="footer-disclaimer">MARA Agent: Mubashar Ahmed Nizamani · MARN 1281745 · ABN 96 695 178 744. Migration advice provided in accordance with the Migration Agents Code of Conduct. Visa outcomes are subject to eligibility and Department of Home Affairs requirements. GEMCA does not guarantee any visa outcome.</p>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <ul class="footer-links">
          <li><a href="#services">Student Visas</a></li>
          <li><a href="#services">Skilled Migration</a></li>
          <li><a href="#services">Employer Sponsored</a></li>
          <li><a href="#services">Partner &amp; Family</a></li>
          <li><a href="#services">Appeals &amp; Reviews</a></li>
          <li><a href="#services">Skills Assessments</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Countries</h5>
        <ul class="footer-links">
          <li><a href="#countries" onclick="showCountry('au')">🇦🇺 Australia</a></li>
          <li><a href="#countries" onclick="showCountry('uk')">🇬🇧 United Kingdom</a></li>
          <li><a href="#countries" onclick="showCountry('ca')">🇨🇦 Canada</a></li>
          <li><a href="#countries" onclick="showCountry('us')">🇺🇸 United States</a></li>
          <li><a href="#countries" onclick="showCountry('nz')">🇳🇿 New Zealand</a></li>
          <li><a href="#countries" onclick="showCountry('eu')">🇪🇺 Europe</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul class="footer-links">
          <li><a href="tel:0413769458">0413 769 458</a></li>
          <li><a href="tel:0370203358">03 7020 3358</a></li>
          <li><a href="mailto:ansar@gemca.com.au">ansar@gemca.com.au</a></li>
          <li><a href="https://wa.me/61413769458" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
          <li><a href="https://instagram.com/ansirgoraya" target="_blank" rel="noopener noreferrer">@ansirgoraya</a></li>
        </ul>
        <h5 style="margin-top:1.5rem">Locate Us</h5>
        <ul class="footer-links">
          <li style="color:var(--muted);font-size:13px">8 Tallis Circuit<br>Truganina VIC 3029</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 GEMCA — Goraya Education &amp; Migration Consultant Australia. All rights reserved.</p>
      <div class="social-row">
        <a href="https://instagram.com/ansirgoraya" target="_blank" rel="noopener noreferrer" class="social-btn" aria-label="Instagram">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        </a>
        <a href="https://wa.me/61413769458" target="_blank" rel="noopener noreferrer" class="social-btn" aria-label="WhatsApp">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        </a>
        <a href="mailto:ansar@gemca.com.au" class="social-btn" aria-label="Email">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        </a>
      </div>
    </div>
  </div>
</footer>

<!-- WHATSAPP FLOAT -->
<a href="https://wa.me/61413769458" target="_blank" rel="noopener noreferrer" class="wa-float" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
</a>
"""

JS = """
<script>
// ── NAVBAR SCROLL ──────────────────────────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
}, {passive: true});

// ── MOBILE MENU ────────────────────────────────────────────────────────────
const mobileMenu = document.getElementById('mobile-menu');
const hamburger  = document.getElementById('hamburger');
function toggleMenu() {
  const open = hamburger.classList.toggle('open');
  mobileMenu.classList.toggle('open', open);
  hamburger.setAttribute('aria-expanded', open);
  mobileMenu.setAttribute('aria-hidden', !open);
  document.body.style.overflow = open ? 'hidden' : '';
}
function closeMenu() {
  hamburger.classList.remove('open');
  mobileMenu.classList.remove('open');
  hamburger.setAttribute('aria-expanded', 'false');
  mobileMenu.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}
mobileMenu.addEventListener('click', e => { if (e.target === mobileMenu) closeMenu(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });

// ── SCROLL REVEAL ──────────────────────────────────────────────────────────
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); revealObserver.unobserve(e.target); }});
}, { threshold: 0.1, rootMargin: '0px 0px -48px 0px' });
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ── COUNTRY TABS ───────────────────────────────────────────────────────────
function showCountry(code) {
  document.querySelectorAll('.tab-btn').forEach(b => {
    const active = b.dataset.tab === code;
    b.classList.toggle('active', active);
    b.setAttribute('aria-selected', active);
  });
  document.querySelectorAll('.tab-panel').forEach(p => {
    const active = p.dataset.panel === code;
    p.style.display = active ? 'block' : 'none';
    p.classList.toggle('active', active);
    // Close all open accordions in newly hidden panels
    if (!active) p.querySelectorAll('.acc-item.open').forEach(item => closeAcc(item));
  });
}
// Show first tab on load
showCountry('au');

// ── ACCORDIONS ─────────────────────────────────────────────────────────────
function toggleAcc(btn) {
  const item = btn.closest('.acc-item');
  const body = item.querySelector('.acc-body');
  const wasOpen = item.classList.contains('open');
  // Close siblings in the same visa list
  const list = item.closest('.visa-accordions');
  if (list) list.querySelectorAll('.acc-item.open').forEach(i => closeAcc(i));
  if (!wasOpen) {
    item.classList.add('open');
    body.style.maxHeight = body.scrollHeight + 'px';
    btn.setAttribute('aria-expanded', 'true');
  }
}
function closeAcc(item) {
  item.classList.remove('open');
  item.querySelector('.acc-body').style.maxHeight = null;
  const btn = item.querySelector('.acc-hdr');
  if (btn) btn.setAttribute('aria-expanded', 'false');
}

// ── FORM: ASSESSMENT ───────────────────────────────────────────────────────
function submitAssessment() {
  const fname   = document.getElementById('a-fname').value.trim();
  const lname   = document.getElementById('a-lname').value.trim();
  const email   = document.getElementById('a-email').value.trim();
  const consent = document.getElementById('a-consent').checked;
  const country = document.getElementById('a-country').value;
  if (!fname)    { alert('Please enter your first name.'); document.getElementById('a-fname').focus(); return; }
  if (!lname)    { alert('Please enter your last name.'); document.getElementById('a-lname').focus(); return; }
  if (!email || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) { alert('Please enter a valid email address.'); document.getElementById('a-email').focus(); return; }
  if (!country)  { alert('Please select a destination country.'); document.getElementById('a-country').focus(); return; }
  if (!consent)  { alert('Please provide consent to continue.'); document.getElementById('a-consent').focus(); return; }
  const btn = document.getElementById('a-submit-btn');
  const spinner = document.getElementById('a-spinner');
  const btnText = document.getElementById('a-btn-text');
  btn.disabled = true;
  spinner.style.display = 'block';
  btnText.style.display = 'none';
  setTimeout(() => {
    document.getElementById('assessment-form').style.display = 'none';
    document.getElementById('assessment-success').style.display = 'block';
  }, 1300);
}

// ── FORM: CONTACT ──────────────────────────────────────────────────────────
function submitContact() {
  const name    = document.getElementById('c-name').value.trim();
  const email   = document.getElementById('c-email').value.trim();
  const msg     = document.getElementById('c-msg').value.trim();
  const consent = document.getElementById('c-consent').checked;
  if (!name)   { alert('Please enter your name.'); document.getElementById('c-name').focus(); return; }
  if (!email || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) { alert('Please enter a valid email address.'); document.getElementById('c-email').focus(); return; }
  if (!msg)    { alert('Please enter your message.'); document.getElementById('c-msg').focus(); return; }
  if (!consent){ alert('Please provide consent to continue.'); document.getElementById('c-consent').focus(); return; }
  const btn = document.getElementById('c-submit-btn');
  const spinner = document.getElementById('c-spinner');
  const btnText = document.getElementById('c-btn-text');
  btn.disabled = true;
  spinner.style.display = 'block';
  btnText.style.display = 'none';
  setTimeout(() => {
    document.getElementById('contact-form').style.display = 'none';
    document.getElementById('contact-success').style.display = 'block';
  }, 1300);
}

// ── DROPDOWN KEYBOARD NAV ──────────────────────────────────────────────────
document.querySelectorAll('.dropdown').forEach(dd => {
  const toggle = dd.querySelector('.dropdown-toggle');
  if (toggle) toggle.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    // close all
    document.querySelectorAll('.dropdown-toggle').forEach(t => t.setAttribute('aria-expanded', 'false'));
    toggle.setAttribute('aria-expanded', expanded ? 'false' : 'true');
  });
});
document.addEventListener('click', e => {
  if (!e.target.closest('.dropdown')) {
    document.querySelectorAll('.dropdown-toggle').forEach(t => t.setAttribute('aria-expanded', 'false'));
  }
});
</script>
</body>
</html>"""


# ── FINAL ASSEMBLY ──────────────────────────────────────────────────────────
html = (HEAD
        + "<style>" + CSS + "</style>\n</head>\n"
        + BODY
        + COUNTRIES_PANELS
        + COUNTRIES_SECTION_END
        + JS)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

lines = len(html.splitlines())
print(f"✓ Generated {lines} lines")
