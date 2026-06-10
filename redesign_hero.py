#!/usr/bin/env python3
"""Redesign the hero section right column and background for premium feel."""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)

# ============================================================
# 1. Replace Aurora CSS (make luxury hotel lobby — very slow,
#    deep navy, barely visible gold glow)
# ============================================================
OLD_AURORA_CSS = """    /* ============================================================
       AURORA BACKGROUND
    ============================================================ */
    .aurora {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .orb {
      position: absolute;
      border-radius: 50%;
      filter: blur(100px);
      animation: drift 20s ease-in-out infinite;
    }

    .orb-1 {
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, #0B2A6B 0%, transparent 70%);
      top: -200px;
      left: -200px;
      animation-delay: 0s;
    }

    .orb-2 {
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(200,169,110,0.15) 0%, transparent 70%);
      top: 50%;
      right: -200px;
      animation-delay: -7s;
    }

    .orb-3 {
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(11,42,107,0.6) 0%, transparent 70%);
      bottom: -100px;
      left: 30%;
      animation-delay: -14s;
    }

    @keyframes drift {
      0%, 100% {
        transform: translate(0, 0) scale(1);
      }
      33% {
        transform: translate(30px, -30px) scale(1.05);
      }
      66% {
        transform: translate(-20px, 20px) scale(0.95);
      }"""

NEW_AURORA_CSS = """    /* ============================================================
       AURORA BACKGROUND — luxury hotel lobby lighting
    ============================================================ */
    .aurora {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    /* Architectural blueprint line overlay */
    .aurora::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(rgba(200,169,110,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(200,169,110,0.025) 1px, transparent 1px);
      background-size: 80px 80px;
      pointer-events: none;
    }

    .orb {
      position: absolute;
      border-radius: 50%;
      filter: blur(140px);
      animation: drift 40s ease-in-out infinite;
    }

    .orb-1 {
      width: 900px;
      height: 700px;
      background: radial-gradient(ellipse, rgba(11,42,107,0.55) 0%, transparent 70%);
      top: -300px;
      left: -200px;
      animation-delay: 0s;
    }

    .orb-2 {
      width: 700px;
      height: 600px;
      background: radial-gradient(ellipse, rgba(200,169,110,0.06) 0%, transparent 70%);
      top: 40%;
      right: -250px;
      animation-delay: -15s;
    }

    .orb-3 {
      width: 600px;
      height: 500px;
      background: radial-gradient(ellipse, rgba(6,25,80,0.7) 0%, transparent 70%);
      bottom: -100px;
      left: 25%;
      animation-delay: -28s;
    }

    @keyframes drift {
      0%, 100% {
        transform: translate(0, 0) scale(1);
      }
      33% {
        transform: translate(18px, -18px) scale(1.03);
      }
      66% {
        transform: translate(-12px, 14px) scale(0.97);
      }"""

assert OLD_AURORA_CSS in html, "Aurora CSS not found"
html = html.replace(OLD_AURORA_CSS, NEW_AURORA_CSS, 1)
print("✓ Aurora CSS replaced")

# ============================================================
# 2. Replace Globe CSS with premium hero-right CSS
# ============================================================
OLD_GLOBE_CSS = """    /* ============================================================
       GLOBE
    ============================================================ */
    .globe-container {
      position: relative;
      width: 500px;
      height: 500px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .globe {
      position: relative;
      width: 360px;
      height: 360px;
      border-radius: 50%;
      border: 1px solid rgba(200, 169, 110, 0.15);
      animation: globe-spin 30s linear infinite;
    }

    @keyframes globe-spin {
      from {
        transform: rotateY(0deg);
      }
      to {
        transform: rotateY(360deg);
      }
    }

    .globe-ring {
      position: absolute;
      border-radius: 50%;
      border: 1px solid rgba(200, 169, 110, 0.12);
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    .globe-ring-1 {
      width: 100%;
      height: 100%;
      transform: translate(-50%, -50%) rotateX(75deg);
      border-color: rgba(200, 169, 110, 0.18);
    }

    .globe-ring-2 {
      width: 100%;
      height: 50%;
      transform: translate(-50%, -50%) rotateX(75deg) translateY(-25%);
      border-color: rgba(200, 169, 110, 0.1);
    }

    .globe-ring-3 {
      width: 75%;
      height: 75%;
      transform: translate(-50%, -50%) rotateX(70deg) rotateZ(30deg);
      border-color: rgba(200, 169, 110, 0.1);
    }

    .globe-ring-4 {
      width: 55%;
      height: 55%;
      transform: translate(-50%, -50%) rotateX(70deg);
      border-color: rgba(200, 169, 110, 0.1);
    }

    .globe-ring-5 {
      width: 30%;
      height: 100%;
      transform: translate(-50%, -50%) rotateY(60deg);
      border-color: rgba(200, 169, 110, 0.14);
    }

    .globe-ring-6 {
      width: 30%;
      height: 100%;
      transform: translate(-50%, -50%) rotateY(30deg);
      border-color: rgba(200, 169, 110, 0.14);
    }

    .globe-glow {
      position: absolute;
      inset: 0;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, rgba(11, 42, 107, 0.6) 0%, rgba(6, 14, 30, 0.3) 50%, transparent 70%);
    }

    .globe-outer-ring {
      position: absolute;
      inset: -20px;
      border-radius: 50%;
      border: 1px solid rgba(200, 169, 110, 0.08);
      animation: globe-spin 45s linear infinite reverse;
    }

    .globe-outer-ring-2 {
      position: absolute;
      inset: -40px;
      border-radius: 50%;
      border: 1px dashed rgba(200, 169, 110, 0.05);
      animation: globe-spin 60s linear infinite;
    }

    .country-dot {
      position: absolute;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #C8A96E;
      box-shadow: 0 0 15px #C8A96E;
      animation: country-pulse 2s ease-in-out infinite;
      transform: translate(-50%, -50%);
    }

    @keyframes country-pulse {
      0%, 100% {
        box-shadow: 0 0 5px #C8A96E;
        transform: translate(-50%, -50%) scale(1);
      }
      50% {
        box-shadow: 0 0 20px #C8A96E, 0 0 40px rgba(200, 169, 110, 0.3);
        transform: translate(-50%, -50%) scale(1.2);
      }
    }

    .dot-au { top: 72%; left: 80%; animation-delay: 0s; }
    .dot-uk { top: 25%; left: 45%; animation-delay: -0.5s; }
    .dot-ca { top: 22%; left: 20%; animation-delay: -1s; }
    .dot-us { top: 35%; left: 18%; animation-delay: -1.5s; }
    .dot-nz { top: 78%; left: 88%; animation-delay: -2s; }
    .dot-eu { top: 28%; left: 50%; animation-delay: -0.3s; }

    .dot-label {
      position: absolute;
      font-size: 10px;
      color: #C8A96E;
      white-space: nowrap;
      font-weight: 600;
      letter-spacing: 0.05em;
      font-family: var(--font-body);
      pointer-events: none;
    }

    .label-au { top: calc(72% + 8px); left: calc(80% + 5px); }
    .label-uk { top: calc(25% + 8px); left: calc(45% + 5px); }
    .label-ca { top: calc(22% - 18px); left: calc(20% - 5px); }
    .label-us { top: calc(35% + 8px); left: calc(18% - 10px); }
    .label-nz { top: calc(78% + 8px); left: calc(88% - 10px); }
    .label-eu { top: calc(28% - 18px); left: calc(50% + 5px); }"""

NEW_HERO_RIGHT_CSS = """    /* ============================================================
       HERO RIGHT — PREMIUM VISUAL
    ============================================================ */
    .hero-right-visual {
      position: relative;
      width: 100%;
      height: 560px;
      display: flex;
      align-items: flex-end;
      justify-content: center;
    }

    /* Gold particle field */
    .particle-field {
      position: absolute;
      inset: 0;
      overflow: hidden;
      border-radius: 20px;
    }

    .particle {
      position: absolute;
      width: 2px;
      height: 2px;
      background: #C8A96E;
      border-radius: 50%;
      opacity: 0;
      animation: particle-rise var(--dur, 8s) ease-in-out infinite;
      animation-delay: var(--delay, 0s);
    }

    @keyframes particle-rise {
      0%   { opacity: 0; transform: translateY(0) scale(0.5); }
      20%  { opacity: 0.6; }
      80%  { opacity: 0.3; }
      100% { opacity: 0; transform: translateY(-80px) scale(1); }
    }

    /* Sydney Opera House SVG container */
    .opera-house-wrap {
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 100%;
      max-width: 520px;
      z-index: 2;
    }

    /* Water reflection line */
    .water-line {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(200,169,110,0.35), rgba(200,169,110,0.5), rgba(200,169,110,0.35), transparent);
    }

    .water-reflection {
      position: absolute;
      bottom: -30px;
      left: 50%;
      transform: translateX(-50%);
      width: 70%;
      height: 30px;
      background: linear-gradient(to bottom, rgba(200,169,110,0.08), transparent);
      filter: blur(4px);
    }

    /* Premium flag cards */
    .flag-cards-wrap {
      position: absolute;
      inset: 0;
      pointer-events: none;
    }

    .flag-card {
      position: absolute;
      background: rgba(6, 14, 30, 0.75);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(200,169,110,0.22);
      border-radius: 14px;
      padding: 0.85rem 1.1rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.3rem;
      min-width: 90px;
      pointer-events: all;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
      animation: flag-float var(--fdur, 5s) ease-in-out infinite;
      animation-delay: var(--fdelay, 0s);
    }

    .flag-card:hover {
      border-color: rgba(200,169,110,0.6);
      box-shadow: 0 0 28px rgba(200,169,110,0.18), 0 12px 40px rgba(0,0,0,0.4);
    }

    @keyframes flag-float {
      0%, 100% { transform: translateY(0px); }
      50%       { transform: translateY(-10px); }
    }

    .flag-card .fc-emoji {
      font-size: 2.2rem;
      line-height: 1;
      filter: drop-shadow(0 3px 8px rgba(0,0,0,0.5));
    }

    .flag-card .fc-name {
      font-family: var(--font-body);
      font-size: 11px;
      font-weight: 700;
      color: rgba(255,255,255,0.9);
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }

    .flag-card .fc-badge {
      font-size: 9px;
      color: #C8A96E;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      border: 1px solid rgba(200,169,110,0.35);
      border-radius: 20px;
      padding: 1px 7px;
    }

    /* card positions */
    .fc-au { top: 8%;  left: 2%;   --fdur:5.2s; --fdelay:0s;    }
    .fc-uk { top: 2%;  left: 35%;  --fdur:6.0s; --fdelay:-1.5s; }
    .fc-ca { top: 8%;  right: 2%;  --fdur:5.6s; --fdelay:-3.0s; }
    .fc-us { bottom: 46%; left: 4%;  --fdur:4.8s; --fdelay:-0.8s; }
    .fc-nz { bottom: 46%; right: 4%; --fdur:5.4s; --fdelay:-2.2s; }
    .fc-eu { bottom: 48%; left: 38%; --fdur:6.2s; --fdelay:-4.0s; }

    /* Gold ambient glow behind opera house */
    .opera-glow {
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 420px;
      height: 220px;
      background: radial-gradient(ellipse at 50% 100%, rgba(200,169,110,0.13) 0%, transparent 70%);
      pointer-events: none;
      z-index: 1;
    }"""

assert OLD_GLOBE_CSS in html, "Globe CSS not found"
html = html.replace(OLD_GLOBE_CSS, NEW_HERO_RIGHT_CSS, 1)
print("✓ Globe CSS replaced with premium hero-right CSS")

# ============================================================
# 3. Replace Floating Cards CSS with particle + flag-label CSS
# ============================================================
OLD_FLOAT_CSS = """    /* ============================================================
       FLOATING CARDS
    ============================================================ */
    .floating-cards {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      pointer-events: none;
    }

    .float-card {
      position: absolute;
      background: rgba(6, 14, 30, 0.8);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(200, 169, 110, 0.25);
      border-radius: 14px;
      padding: 1rem 1.25rem;
      min-width: 180px;
    }

    .float-card-1 {
      top: 10%;
      right: -20px;
      animation: float1 4s ease-in-out infinite;
    }

    .float-card-2 {
      top: 45%;
      left: -30px;
      animation: float2 5s ease-in-out infinite;
      animation-delay: -2s;
    }

    .float-card-3 {
      bottom: 10%;
      right: 10%;
      animation: float1 4.5s ease-in-out infinite;
      animation-delay: -1s;
    }

    @keyframes float1 {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-15px); }
    }"""

NEW_FLOAT_CSS = """    /* ============================================================
       HERO FLAG LABELS (country flags row — left side)
    ============================================================ */
    .hero-flag-row {
      display: flex;
      gap: 0.9rem;
      flex-wrap: wrap;
      align-items: center;
      margin-top: 0.25rem;
    }

    .hero-flag-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.25rem;
      opacity: 0.9;
      transition: opacity 0.2s;
    }

    .hero-flag-item:hover { opacity: 1; }

    .hero-flag-emoji {
      font-size: 1.9rem;
      line-height: 1;
      filter: drop-shadow(0 2px 6px rgba(0,0,0,0.4));
      animation: flag-gentle var(--hfe-dur, 5s) ease-in-out infinite;
      animation-delay: var(--hfe-delay, 0s);
    }

    @keyframes flag-gentle {
      0%, 100% { transform: rotate(-2deg); }
      50%       { transform: rotate(2deg); }
    }

    .hero-flag-name {
      font-size: 9px;
      color: rgba(255,255,255,0.45);
      text-transform: uppercase;
      letter-spacing: 0.09em;
      font-family: var(--font-body);
    }

    @keyframes float1 {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-15px); }
    }"""

assert OLD_FLOAT_CSS in html, "Float card CSS not found"
html = html.replace(OLD_FLOAT_CSS, NEW_FLOAT_CSS, 1)
print("✓ Floating cards CSS replaced with flag-row CSS")

# ============================================================
# 4. Update responsive CSS — remove globe/float-card overrides,
#    add hero-right-visual override
# ============================================================
OLD_RESP_GLOBE = """      .globe-container {
        width: 100%;
        height: 400px;
      }

      .globe {
        width: 300px;
        height: 300px;
      }

      .float-card-1 {
        right: 0;
      }

      .float-card-2 {
        left: 0;
      }

"""

NEW_RESP_GLOBE = """      .hero-right-visual {
        height: 380px;
      }

      .fc-au, .fc-uk, .fc-ca { top: auto; bottom: auto; }

"""

assert OLD_RESP_GLOBE in html, "Responsive globe CSS not found"
html = html.replace(OLD_RESP_GLOBE, NEW_RESP_GLOBE, 1)
print("✓ Responsive globe overrides replaced")

# ============================================================
# 5. Replace hero right column HTML
# ============================================================
OLD_HERO_RIGHT = """    <!-- RIGHT COLUMN — GLOBE + FLOATING CARDS -->
    <div class="hero-right" style="display: flex; align-items: center; justify-content: center; position: relative;">
      <div class="globe-container">

        <!-- Outer decorative rings -->
        <div class="globe-outer-ring-2"></div>
        <div class="globe-outer-ring"></div>

        <!-- Globe sphere with latitude/longitude lines -->
        <div class="globe">
          <!-- Glow effect -->
          <div class="globe-glow"></div>

          <!-- Ring latitude lines -->
          <div class="globe-ring globe-ring-1"></div>
          <div class="globe-ring globe-ring-2"></div>
          <div class="globe-ring globe-ring-3"></div>
          <div class="globe-ring globe-ring-4"></div>
          <div class="globe-ring globe-ring-5"></div>
          <div class="globe-ring globe-ring-6"></div>

          <!-- Country dots -->
          <div class="country-dot dot-au" title="Australia"></div>
          <span class="dot-label label-au">AU</span>

          <div class="country-dot dot-uk" title="United Kingdom"></div>
          <span class="dot-label label-uk">UK</span>

          <div class="country-dot dot-ca" title="Canada"></div>
          <span class="dot-label label-ca">CA</span>

          <div class="country-dot dot-us" title="United States"></div>
          <span class="dot-label label-us">US</span>

          <div class="country-dot dot-nz" title="New Zealand"></div>
          <span class="dot-label label-nz">NZ</span>

          <div class="country-dot dot-eu" title="Europe"></div>
          <span class="dot-label label-eu">EU</span>
        </div>

        <!-- Floating status cards -->
        <div class="floating-cards">

          <!-- Card 1: Visa Granted -->
          <div class="float-card float-card-1">
            <div class="card-status granted">
              <span class="card-dot green"></span>
              Visa Granted
            </div>
            <div class="card-value">Subclass 500</div>
            <div class="card-sub">Student Visa &mdash; Melbourne</div>
          </div>

          <!-- Card 2: Student Visa Processing -->
          <div class="float-card float-card-2">
            <div class="card-status student">
              <span class="card-dot blue"></span>
              In Progress
            </div>
            <div class="card-value">Skilled 189</div>
            <div class="card-sub">Points-tested Stream</div>
          </div>

          <!-- Card 3: PR Approved -->
          <div class="float-card float-card-3">
            <div class="card-status pr">
              <span class="card-dot gold"></span>
              PR Approved
            </div>
            <div class="card-value">Subclass 190</div>
            <div class="card-sub">State Nominated &mdash; VIC</div>
          </div>

        </div>

      </div>
    </div>"""

NEW_HERO_RIGHT = """    <!-- RIGHT COLUMN — PREMIUM VISUAL -->
    <div class="hero-right" style="position:relative;">
      <div class="hero-right-visual">

        <!-- Particle field — gold stars -->
        <div class="particle-field" aria-hidden="true">
          <div class="particle" style="left:8%;  top:70%; --dur:9s;  --delay:0s;"></div>
          <div class="particle" style="left:15%; top:55%; --dur:7s;  --delay:-2s;"></div>
          <div class="particle" style="left:22%; top:80%; --dur:11s; --delay:-5s;"></div>
          <div class="particle" style="left:30%; top:40%; --dur:8s;  --delay:-1s;"></div>
          <div class="particle" style="left:40%; top:65%; --dur:10s; --delay:-3s;"></div>
          <div class="particle" style="left:52%; top:75%; --dur:7s;  --delay:-6s;"></div>
          <div class="particle" style="left:60%; top:50%; --dur:9s;  --delay:-0.5s;"></div>
          <div class="particle" style="left:70%; top:60%; --dur:12s; --delay:-4s;"></div>
          <div class="particle" style="left:78%; top:45%; --dur:8s;  --delay:-7s;"></div>
          <div class="particle" style="left:85%; top:72%; --dur:10s; --delay:-2.5s;"></div>
          <div class="particle" style="left:92%; top:35%; --dur:6s;  --delay:-1.5s;"></div>
          <div class="particle" style="left:48%; top:30%; --dur:9s;  --delay:-8s;"></div>
          <div class="particle" style="left:25%; top:25%; --dur:11s; --delay:-3.5s;"></div>
          <div class="particle" style="left:65%; top:85%; --dur:7s;  --delay:-9s;"></div>
          <div class="particle" style="left:5%;  top:30%; --dur:13s; --delay:-4.5s;"></div>
          <div class="particle" style="left:90%; top:80%; --dur:8s;  --delay:-6.5s;"></div>
          <div class="particle" style="left:35%; top:90%; --dur:10s; --delay:-1.2s;"></div>
          <div class="particle" style="left:72%; top:20%; --dur:9s;  --delay:-7.5s;"></div>
          <div class="particle" style="left:12%; top:15%; --dur:12s; --delay:-5.5s;"></div>
          <div class="particle" style="left:55%; top:18%; --dur:8s;  --delay:-0.8s;"></div>
        </div>

        <!-- Premium flag cards — floating asymmetric layout -->
        <div class="flag-cards-wrap" aria-hidden="true">

          <div class="flag-card fc-au">
            <span class="fc-emoji">🇦🇺</span>
            <span class="fc-name">Australia</span>
            <span class="fc-badge">Visas Available</span>
          </div>

          <div class="flag-card fc-uk">
            <span class="fc-emoji">🇬🇧</span>
            <span class="fc-name">United Kingdom</span>
            <span class="fc-badge">Visas Available</span>
          </div>

          <div class="flag-card fc-ca">
            <span class="fc-emoji">🇨🇦</span>
            <span class="fc-name">Canada</span>
            <span class="fc-badge">Visas Available</span>
          </div>

          <div class="flag-card fc-us">
            <span class="fc-emoji">🇺🇸</span>
            <span class="fc-name">United States</span>
            <span class="fc-badge">Visas Available</span>
          </div>

          <div class="flag-card fc-nz">
            <span class="fc-emoji">🇳🇿</span>
            <span class="fc-name">New Zealand</span>
            <span class="fc-badge">Visas Available</span>
          </div>

          <div class="flag-card fc-eu">
            <span class="fc-emoji">🇪🇺</span>
            <span class="fc-name">Europe</span>
            <span class="fc-badge">Visas Available</span>
          </div>

        </div>

        <!-- Ambient glow behind Opera House -->
        <div class="opera-glow" aria-hidden="true"></div>

        <!-- Sydney Opera House SVG silhouette -->
        <div class="opera-house-wrap">
          <svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" aria-label="Sydney Opera House silhouette" style="width:100%;display:block;">
            <defs>
              <linearGradient id="oh-shell" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%"   stop-color="#E8C87A"/>
                <stop offset="40%"  stop-color="#C8A96E"/>
                <stop offset="100%" stop-color="#9A7040"/>
              </linearGradient>
              <linearGradient id="oh-shell2" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%"   stop-color="#D4B060"/>
                <stop offset="40%"  stop-color="#B89050"/>
                <stop offset="100%" stop-color="#8A6030"/>
              </linearGradient>
              <filter id="oh-glow" x="-10%" y="-30%" width="120%" height="160%">
                <feGaussianBlur stdDeviation="4" result="blur"/>
                <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
              <filter id="oh-softglow" x="-20%" y="-40%" width="140%" height="180%">
                <feGaussianBlur stdDeviation="8" result="blur"/>
                <feColorMatrix in="blur" type="matrix" values="1 0.8 0.3 0 0  0.8 0.6 0.2 0 0  0.2 0.1 0 0 0  0 0 0 0.4 0" result="gold"/>
                <feMerge><feMergeNode in="gold"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
            </defs>

            <!-- MAIN CONCERT HALL — large sweeping shells (left group) -->
            <!-- Shell 1 (tallest, outer left) -->
            <path filter="url(#oh-softglow)"
              d="M 60,190 Q 65,155 80,115 Q 100,65 130,35 Q 140,25 148,32 Q 155,40 148,75 Q 138,115 118,155 Q 100,178 85,190 Z"
              fill="url(#oh-shell)" opacity="0.95"/>
            <!-- Shell 1 inner edge highlight -->
            <path d="M 85,190 Q 100,178 118,155 Q 138,115 148,75 Q 155,40 148,32"
              fill="none" stroke="rgba(255,240,190,0.35)" stroke-width="1.2"/>

            <!-- Shell 2 -->
            <path filter="url(#oh-softglow)"
              d="M 85,190 Q 95,165 112,130 Q 130,90 150,62 Q 160,48 168,54 Q 176,62 168,92 Q 155,128 135,160 Q 118,180 100,190 Z"
              fill="url(#oh-shell)" opacity="0.88"/>
            <path d="M 100,190 Q 118,180 135,160 Q 155,128 168,92 Q 176,62 168,54"
              fill="none" stroke="rgba(255,240,190,0.28)" stroke-width="1"/>

            <!-- Shell 3 -->
            <path
              d="M 112,190 Q 122,170 138,140 Q 155,105 172,80 Q 180,66 186,72 Q 192,80 184,108 Q 172,140 152,165 Q 136,182 122,190 Z"
              fill="url(#oh-shell2)" opacity="0.80"/>

            <!-- Shell 4 (innermost left) -->
            <path
              d="M 135,190 Q 144,175 158,152 Q 172,124 184,102 Q 190,88 195,95 Q 200,104 192,128 Q 180,155 162,174 Q 150,185 140,190 Z"
              fill="url(#oh-shell2)" opacity="0.70"/>

            <!-- OPERA THEATRE — smaller shells (right group) -->
            <!-- Shell A (tallest of right group) -->
            <path filter="url(#oh-softglow)"
              d="M 260,190 Q 265,168 278,142 Q 296,106 316,82 Q 325,70 332,76 Q 340,84 332,110 Q 320,140 302,163 Q 286,180 272,190 Z"
              fill="url(#oh-shell)" opacity="0.90"/>
            <path d="M 272,190 Q 286,180 302,163 Q 320,140 332,110 Q 340,84 332,76"
              fill="none" stroke="rgba(255,240,190,0.30)" stroke-width="1"/>

            <!-- Shell B -->
            <path
              d="M 278,190 Q 286,172 300,150 Q 316,122 332,100 Q 340,88 345,94 Q 350,102 342,125 Q 330,152 312,170 Q 298,183 286,190 Z"
              fill="url(#oh-shell2)" opacity="0.78"/>

            <!-- Shell C (innermost right) -->
            <path
              d="M 298,190 Q 306,176 318,158 Q 332,134 344,114 Q 350,102 354,108 Q 358,116 350,138 Q 338,162 320,178 Q 308,188 300,190 Z"
              fill="url(#oh-shell2)" opacity="0.65"/>

            <!-- PODIUM / BASE PLATFORM -->
            <rect x="30" y="185" width="460" height="8" rx="2" fill="#8A6830" opacity="0.7"/>
            <rect x="20" y="190" width="480" height="5" rx="2" fill="#7A5820" opacity="0.5"/>

            <!-- FORECOURT STEPS (slight detail) -->
            <rect x="40"  y="182" width="440" height="3" rx="1" fill="rgba(200,169,110,0.25)"/>
            <rect x="55"  y="179" width="410" height="3" rx="1" fill="rgba(200,169,110,0.15)"/>

            <!-- Thin edge glint on shell tops -->
            <path d="M 130,35 Q 140,25 148,32" fill="none" stroke="rgba(255,248,210,0.7)" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M 316,82 Q 325,70 332,76" fill="none" stroke="rgba(255,248,210,0.55)" stroke-width="1.2" stroke-linecap="round"/>
          </svg>

          <!-- Water reflection -->
          <div class="water-line"></div>
          <div class="water-reflection"></div>
        </div>

      </div>
    </div>"""

assert OLD_HERO_RIGHT in html, "Hero right column HTML not found"
html = html.replace(OLD_HERO_RIGHT, NEW_HERO_RIGHT, 1)
print("✓ Hero right column replaced with Opera House + flag cards")

# ============================================================
# 6. Replace old country-flags / flag-item HTML with new flag row
# ============================================================
OLD_FLAGS_HTML = """      <!-- COUNTRY FLAGS -->
      <div class="country-flags">
        <div class="flag-item">
          <span class="flag-emoji">🇦🇺</span>
          <span class="flag-label">Australia</span>
        </div>
        <div class="flag-item">
          <span class="flag-emoji">🇬🇧</span>
          <span class="flag-label">UK</span>
        </div>
        <div class="flag-item">
          <span class="flag-emoji">🇨🇦</span>
          <span class="flag-label">Canada</span>
        </div>
        <div class="flag-item">
          <span class="flag-emoji">🇺🇸</span>
          <span class="flag-label">USA</span>
        </div>
        <div class="flag-item">
          <span class="flag-emoji">🇳🇿</span>
          <span class="flag-label">NZ</span>
        </div>
        <div class="flag-item">
          <span class="flag-emoji">🇪🇺</span>
          <span class="flag-label">Europe</span>
        </div>
      </div>"""

NEW_FLAGS_HTML = """      <!-- COUNTRY FLAGS — animated row -->
      <div class="hero-flag-row">
        <div class="hero-flag-item">
          <span class="hero-flag-emoji" style="--hfe-dur:5s;--hfe-delay:0s">🇦🇺</span>
          <span class="hero-flag-name">Australia</span>
        </div>
        <div class="hero-flag-item">
          <span class="hero-flag-emoji" style="--hfe-dur:5.5s;--hfe-delay:-1s">🇬🇧</span>
          <span class="hero-flag-name">UK</span>
        </div>
        <div class="hero-flag-item">
          <span class="hero-flag-emoji" style="--hfe-dur:4.8s;--hfe-delay:-2s">🇨🇦</span>
          <span class="hero-flag-name">Canada</span>
        </div>
        <div class="hero-flag-item">
          <span class="hero-flag-emoji" style="--hfe-dur:5.8s;--hfe-delay:-0.5s">🇺🇸</span>
          <span class="hero-flag-name">USA</span>
        </div>
        <div class="hero-flag-item">
          <span class="hero-flag-emoji" style="--hfe-dur:5.2s;--hfe-delay:-3s">🇳🇿</span>
          <span class="hero-flag-name">NZ</span>
        </div>
        <div class="hero-flag-item">
          <span class="hero-flag-emoji" style="--hfe-dur:6s;--hfe-delay:-1.5s">🇪🇺</span>
          <span class="hero-flag-name">Europe</span>
        </div>
      </div>"""

assert OLD_FLAGS_HTML in html, "Country flags HTML not found"
html = html.replace(OLD_FLAGS_HTML, NEW_FLAGS_HTML, 1)
print("✓ Country flags HTML updated")

# ============================================================
# 7. Remove unused .card-status / .card-value / .card-sub etc
#    from old float cards (keep in place — they may be used
#    elsewhere, so leave them in CSS). Nothing to do.
# ============================================================

# ============================================================
# 8. Add mobile responsive for hero-right-visual and flag cards
# ============================================================
OLD_480_HERO = """      .hero-ctas {
        flex-direction: column;
      }

      .hero-ctas a, .hero-ctas button {
        width: 100%;
        justify-content: center;
      }"""

NEW_480_HERO = """      .hero-ctas {
        flex-direction: column;
      }

      .hero-ctas a, .hero-ctas button {
        width: 100%;
        justify-content: center;
      }

      /* Hide opera house / flag cards on very small screens */
      .hero-right-visual {
        height: 320px;
      }

      .fc-au, .fc-uk, .fc-ca {
        display: none;
      }

      .fc-us, .fc-nz, .fc-eu {
        display: none;
      }"""

assert OLD_480_HERO in html, "480px responsive section not found"
html = html.replace(OLD_480_HERO, NEW_480_HERO, 1)
print("✓ Mobile responsive updated")

# ============================================================
# Write output
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✓ Done — {len(html.splitlines())} lines  (was {len(html.splitlines())} chars processed, original {original_len} chars)")
