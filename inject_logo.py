import re

with open('/home/user/GEMCA/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# PREMIUM GEMCA CRYSTAL HEXAGON SVG (220x220 viewBox)
# Flat-top hexagon, crystal facets, 3D gold G letterform
# ============================================================

ICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 220" role="img" aria-label="GEMCA Logo">
  <defs>
    <!-- Crystal facet gradients — light source upper-left -->
    <linearGradient id="gL-tl" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4AABF5"/><stop offset="100%" stop-color="#1C66C4"/>
    </linearGradient>
    <linearGradient id="gL-t" x1="30%" y1="0%" x2="70%" y2="100%">
      <stop offset="0%" stop-color="#3498E8"/><stop offset="100%" stop-color="#1255B0"/>
    </linearGradient>
    <linearGradient id="gL-tr" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1E6DC8"/><stop offset="100%" stop-color="#0A3C90"/>
    </linearGradient>
    <linearGradient id="gL-br" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0A3070"/><stop offset="100%" stop-color="#041540"/>
    </linearGradient>
    <linearGradient id="gL-b" x1="50%" y1="100%" x2="50%" y2="0%">
      <stop offset="0%" stop-color="#031030"/><stop offset="100%" stop-color="#07255C"/>
    </linearGradient>
    <linearGradient id="gL-bl" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#041848"/><stop offset="100%" stop-color="#0C3A85"/>
    </linearGradient>
    <!-- Outer frame gradient -->
    <linearGradient id="gL-frame" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A5090"/><stop offset="100%" stop-color="#020C28"/>
    </linearGradient>
    <!-- Gold G gradient (front face) -->
    <linearGradient id="gL-gold" x1="10%" y1="5%" x2="90%" y2="95%">
      <stop offset="0%" stop-color="#F2DC9A"/><stop offset="35%" stop-color="#D4AB6A"/>
      <stop offset="70%" stop-color="#C09050"/><stop offset="100%" stop-color="#9A6C2E"/>
    </linearGradient>
    <!-- Gold G side/extrude gradient -->
    <linearGradient id="gL-gside" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#9A6C2E"/><stop offset="100%" stop-color="#60400C"/>
    </linearGradient>
    <!-- Gold G highlight -->
    <linearGradient id="gL-ghi" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF0C8" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#E8C070" stop-opacity="0"/>
    </linearGradient>
    <!-- Inner glow radial -->
    <radialGradient id="gL-glow" cx="35%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#6AC8FF" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#6AC8FF" stop-opacity="0"/>
    </radialGradient>
    <!-- Drop shadow filter -->
    <filter id="gL-shadow" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000820" flood-opacity="0.65"/>
    </filter>
    <!-- G inner glow filter -->
    <filter id="gL-glow-f" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="1.5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- Bevel edge light filter -->
    <filter id="gL-bevel" x="-5%" y="-5%" width="110%" height="110%">
      <feGaussianBlur stdDeviation="1" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- ── OUTER SHADOW ── -->
  <polygon filter="url(#gL-shadow)"
    points="205,110 158,28 62,28 15,110 62,192 158,192"
    fill="#020A1E" opacity="0.5" transform="translate(2,5)"/>

  <!-- ── OUTER HEXAGON FRAME ── -->
  <polygon
    points="205,110 158,28 62,28 15,110 62,192 158,192"
    fill="url(#gL-frame)" stroke="#0A2258" stroke-width="2"/>

  <!-- ── CRYSTAL FACETS (6 triangles from center 110,110) ── -->
  <!-- Top-left facet: BRIGHTEST (primary light source upper-left) -->
  <polygon points="110,110 15,110 62,28"  fill="url(#gL-tl)"/>
  <!-- Top facet: medium-bright -->
  <polygon points="110,110 62,28 158,28"  fill="url(#gL-t)"/>
  <!-- Top-right facet: medium -->
  <polygon points="110,110 158,28 205,110" fill="url(#gL-tr)"/>
  <!-- Bottom-right facet: dark -->
  <polygon points="110,110 205,110 158,192" fill="url(#gL-br)"/>
  <!-- Bottom facet: darkest -->
  <polygon points="110,110 158,192 62,192" fill="url(#gL-b)"/>
  <!-- Bottom-left facet: medium-dark -->
  <polygon points="110,110 62,192 15,110" fill="url(#gL-bl)"/>

  <!-- ── CRYSTAL FACET DIVIDER LINES ── -->
  <g stroke-width="0.8" opacity="0.6">
    <line x1="110" y1="110" x2="15"  y2="110" stroke="rgba(255,255,255,0.18)"/>
    <line x1="110" y1="110" x2="62"  y2="28"  stroke="rgba(255,255,255,0.22)"/>
    <line x1="110" y1="110" x2="158" y2="28"  stroke="rgba(255,255,255,0.10)"/>
    <line x1="110" y1="110" x2="205" y2="110" stroke="rgba(255,255,255,0.05)"/>
    <line x1="110" y1="110" x2="158" y2="192" stroke="rgba(0,0,0,0.15)"/>
    <line x1="110" y1="110" x2="62"  y2="192" stroke="rgba(0,0,0,0.12)"/>
  </g>

  <!-- ── EDGE HIGHLIGHTS / BEVEL EFFECT ── -->
  <!-- Top flat edge — brightest highlight -->
  <line x1="62" y1="28" x2="158" y2="28"
        stroke="rgba(180,225,255,0.85)" stroke-width="3" filter="url(#gL-bevel)"/>
  <!-- Upper-left edge — bright -->
  <line x1="15" y1="110" x2="62" y2="28"
        stroke="rgba(150,210,255,0.65)" stroke-width="2.5"/>
  <!-- Upper-right edge — medium-light -->
  <line x1="158" y1="28" x2="205" y2="110"
        stroke="rgba(100,170,235,0.35)" stroke-width="2"/>
  <!-- Left edge — medium -->
  <line x1="15" y1="110" x2="62" y2="192"
        stroke="rgba(80,140,210,0.25)" stroke-width="1.5"/>
  <!-- Lower-right edge — dark -->
  <line x1="205" y1="110" x2="158" y2="192"
        stroke="rgba(0,10,40,0.55)" stroke-width="2"/>
  <!-- Bottom flat edge — darkest -->
  <line x1="158" y1="192" x2="62" y2="192"
        stroke="rgba(0,5,25,0.65)" stroke-width="2.5"/>
  <!-- Lower-left edge — dark -->
  <line x1="62" y1="192" x2="15" y2="110"
        stroke="rgba(0,8,35,0.40)" stroke-width="1.5"/>

  <!-- ── CORNER BEVEL CHIPS (crystal cut corners) ── -->
  <!-- Top-left corner highlight -->
  <polygon points="62,28 15,110 28,110 68,42"
           fill="rgba(180,225,255,0.20)"/>
  <!-- Top-right corner (slightly darker) -->
  <polygon points="158,28 205,110 192,110 152,42"
           fill="rgba(80,140,210,0.10)"/>
  <!-- Inner edge ring (thin, defines crystal depth) -->
  <polygon points="198,110 154,36 66,36 22,110 66,184 154,184"
           fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- ── INNER GLOW (upper-left ambient light) ── -->
  <polygon points="205,110 158,28 62,28 15,110 62,192 158,192"
           fill="url(#gL-glow)"/>

  <!-- ── G LETTERFORM 3D EXTRUSION ── -->
  <!-- G centre: (112, 110), outer R=50, inner R=32                    -->
  <!-- Gap: upper-right quadrant (from 3-o'clock up to 12-o'clock)     -->
  <!-- outer-right=(162,110) outer-top=(112,60) inner-top=(112,78) inner-right=(144,110) -->

  <!-- Layer 1: deepest shadow (most offset) -->
  <path fill="#4A2C06" opacity="0.45" transform="translate(8,9)"
    d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>

  <!-- Layer 2: mid extrusion side walls (dark gold) -->
  <path fill="url(#gL-gside)" opacity="0.85" transform="translate(4,5)"
    d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>

  <!-- Layer 3: side-wall faces visible at the gap edges -->
  <!-- Top-cap side wall (where the G is cut at 12 o'clock) -->
  <polygon fill="#8A5C22" opacity="0.9"
    points="112,60 116,65 116,83 112,78"/>
  <!-- Shelf top face (visible top of shelf at 3 o'clock) -->
  <polygon fill="#A07028" opacity="0.85"
    points="144,110 162,110 166,115 148,115"/>

  <!-- Layer 4: MAIN G front face (bright gold gradient) -->
  <path fill="url(#gL-gold)" filter="url(#gL-glow-f)"
    d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>

  <!-- Layer 5: G highlight shimmer (top-left arc of G) -->
  <path fill="url(#gL-ghi)" opacity="0.9"
    d="M 112,60 L 112,78 A 32,32 0 0,0 80,110 A 50,50 0 0,1 112,60 Z"/>

  <!-- Layer 6: bright edge on G inner top-left arc (catch light) -->
  <path fill="none" stroke="rgba(255,245,200,0.55)" stroke-width="2.5"
        stroke-linecap="round"
    d="M 110,79 A 31,31 0 0,0 81,109"/>
</svg>'''

# ============================================================
# NAVBAR LOGO (44×44 icon + GEMCA wordmark with gold A)
# ============================================================

NAVBAR_LOGO_NEW = '''    <!-- GEMCA Premium Crystal Hexagon Logo -->
    <svg width="44" height="44" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <linearGradient id="nL-tl" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#4AABF5"/><stop offset="100%" stop-color="#1C66C4"/></linearGradient>
    <linearGradient id="nL-t"  x1="30%" y1="0%" x2="70%" y2="100%"><stop offset="0%" stop-color="#3498E8"/><stop offset="100%" stop-color="#1255B0"/></linearGradient>
    <linearGradient id="nL-tr" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#1E6DC8"/><stop offset="100%" stop-color="#0A3C90"/></linearGradient>
    <linearGradient id="nL-br" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#0A3070"/><stop offset="100%" stop-color="#041540"/></linearGradient>
    <linearGradient id="nL-b"  x1="50%" y1="100%" x2="50%" y2="0%"><stop offset="0%" stop-color="#031030"/><stop offset="100%" stop-color="#07255C"/></linearGradient>
    <linearGradient id="nL-bl" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#041848"/><stop offset="100%" stop-color="#0C3A85"/></linearGradient>
    <linearGradient id="nL-fr" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1A5090"/><stop offset="100%" stop-color="#020C28"/></linearGradient>
    <linearGradient id="nL-gd" x1="10%" y1="5%" x2="90%" y2="95%"><stop offset="0%" stop-color="#F2DC9A"/><stop offset="35%" stop-color="#D4AB6A"/><stop offset="70%" stop-color="#C09050"/><stop offset="100%" stop-color="#9A6C2E"/></linearGradient>
    <linearGradient id="nL-gs" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#9A6C2E"/><stop offset="100%" stop-color="#60400C"/></linearGradient>
    <linearGradient id="nL-gh" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#FFF0C8" stop-opacity="0.6"/><stop offset="100%" stop-color="#E8C070" stop-opacity="0"/></linearGradient>
    <radialGradient id="nL-gw" cx="35%" cy="30%" r="60%"><stop offset="0%" stop-color="#6AC8FF" stop-opacity="0.22"/><stop offset="100%" stop-color="#6AC8FF" stop-opacity="0"/></radialGradient>
    <filter id="nL-sh" x="-15%" y="-15%" width="130%" height="130%"><feDropShadow dx="0" dy="5" stdDeviation="9" flood-color="#000820" flood-opacity="0.6"/></filter>
  </defs>
  <polygon filter="url(#nL-sh)" points="205,110 158,28 62,28 15,110 62,192 158,192" fill="#020A1E" opacity="0.45" transform="translate(2,4)"/>
  <polygon points="205,110 158,28 62,28 15,110 62,192 158,192" fill="url(#nL-fr)" stroke="#0A2258" stroke-width="2"/>
  <polygon points="110,110 15,110 62,28"  fill="url(#nL-tl)"/>
  <polygon points="110,110 62,28 158,28"  fill="url(#nL-t)"/>
  <polygon points="110,110 158,28 205,110" fill="url(#nL-tr)"/>
  <polygon points="110,110 205,110 158,192" fill="url(#nL-br)"/>
  <polygon points="110,110 158,192 62,192" fill="url(#nL-b)"/>
  <polygon points="110,110 62,192 15,110"  fill="url(#nL-bl)"/>
  <g stroke-width="0.7" opacity="0.5">
    <line x1="110" y1="110" x2="15"  y2="110" stroke="rgba(255,255,255,0.18)"/>
    <line x1="110" y1="110" x2="62"  y2="28"  stroke="rgba(255,255,255,0.22)"/>
    <line x1="110" y1="110" x2="158" y2="28"  stroke="rgba(255,255,255,0.09)"/>
    <line x1="110" y1="110" x2="205" y2="110" stroke="rgba(255,255,255,0.04)"/>
    <line x1="110" y1="110" x2="158" y2="192" stroke="rgba(0,0,0,0.12)"/>
    <line x1="110" y1="110" x2="62"  y2="192" stroke="rgba(0,0,0,0.10)"/>
  </g>
  <line x1="62" y1="28" x2="158" y2="28"   stroke="rgba(180,225,255,0.82)" stroke-width="3"/>
  <line x1="15" y1="110" x2="62" y2="28"    stroke="rgba(150,210,255,0.60)" stroke-width="2.5"/>
  <line x1="158" y1="28" x2="205" y2="110"  stroke="rgba(100,170,235,0.30)" stroke-width="1.8"/>
  <line x1="205" y1="110" x2="158" y2="192" stroke="rgba(0,10,40,0.50)"     stroke-width="1.8"/>
  <line x1="158" y1="192" x2="62" y2="192"  stroke="rgba(0,5,25,0.60)"      stroke-width="2.5"/>
  <line x1="62" y1="192" x2="15" y2="110"   stroke="rgba(0,8,35,0.35)"      stroke-width="1.5"/>
  <polygon points="62,28 15,110 28,110 68,42"  fill="rgba(180,225,255,0.18)"/>
  <polygon points="158,28 205,110 192,110 152,42" fill="rgba(80,140,210,0.08)"/>
  <polygon points="205,110 158,28 62,28 15,110 62,192 158,192" fill="url(#nL-gw)"/>
  <path fill="#4A2C06" opacity="0.40" transform="translate(7,8)"  d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <path fill="url(#nL-gs)" opacity="0.80" transform="translate(4,5)" d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <polygon fill="#8A5C22" opacity="0.88" points="112,60 116,65 116,83 112,78"/>
  <polygon fill="#A07028" opacity="0.82" points="144,110 162,110 166,115 148,115"/>
  <path fill="url(#nL-gd)" d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <path fill="url(#nL-gh)" opacity="0.85" d="M 112,60 L 112,78 A 32,32 0 0,0 80,110 A 50,50 0 0,1 112,60 Z"/>
  <path fill="none" stroke="rgba(255,245,200,0.50)" stroke-width="2" stroke-linecap="round" d="M 110,79 A 31,31 0 0,0 81,109"/>
</svg>'''

# ============================================================
# FOOTER LOGO (38×38 icon)
# ============================================================

FOOTER_LOGO_NEW = '''<svg width="38" height="38" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="fL-tl" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#4AABF5"/><stop offset="100%" stop-color="#1C66C4"/></linearGradient>
    <linearGradient id="fL-t"  x1="30%" y1="0%" x2="70%" y2="100%"><stop offset="0%" stop-color="#3498E8"/><stop offset="100%" stop-color="#1255B0"/></linearGradient>
    <linearGradient id="fL-tr" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#1E6DC8"/><stop offset="100%" stop-color="#0A3C90"/></linearGradient>
    <linearGradient id="fL-br" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#0A3070"/><stop offset="100%" stop-color="#041540"/></linearGradient>
    <linearGradient id="fL-b"  x1="50%" y1="100%" x2="50%" y2="0%"><stop offset="0%" stop-color="#031030"/><stop offset="100%" stop-color="#07255C"/></linearGradient>
    <linearGradient id="fL-bl" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#041848"/><stop offset="100%" stop-color="#0C3A85"/></linearGradient>
    <linearGradient id="fL-fr" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1A5090"/><stop offset="100%" stop-color="#020C28"/></linearGradient>
    <linearGradient id="fL-gd" x1="10%" y1="5%" x2="90%" y2="95%"><stop offset="0%" stop-color="#F2DC9A"/><stop offset="35%" stop-color="#D4AB6A"/><stop offset="70%" stop-color="#C09050"/><stop offset="100%" stop-color="#9A6C2E"/></linearGradient>
    <linearGradient id="fL-gs" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#9A6C2E"/><stop offset="100%" stop-color="#60400C"/></linearGradient>
    <linearGradient id="fL-gh" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#FFF0C8" stop-opacity="0.5"/><stop offset="100%" stop-color="#E8C070" stop-opacity="0"/></linearGradient>
  </defs>
  <polygon points="205,110 158,28 62,28 15,110 62,192 158,192" fill="url(#fL-fr)" stroke="#0A2258" stroke-width="1.5"/>
  <polygon points="110,110 15,110 62,28"  fill="url(#fL-tl)"/>
  <polygon points="110,110 62,28 158,28"  fill="url(#fL-t)"/>
  <polygon points="110,110 158,28 205,110" fill="url(#fL-tr)"/>
  <polygon points="110,110 205,110 158,192" fill="url(#fL-br)"/>
  <polygon points="110,110 158,192 62,192" fill="url(#fL-b)"/>
  <polygon points="110,110 62,192 15,110"  fill="url(#fL-bl)"/>
  <line x1="62" y1="28" x2="158" y2="28"   stroke="rgba(180,225,255,0.75)" stroke-width="2.5"/>
  <line x1="15" y1="110" x2="62" y2="28"    stroke="rgba(150,210,255,0.55)" stroke-width="2"/>
  <line x1="158" y1="28" x2="205" y2="110"  stroke="rgba(100,170,235,0.25)" stroke-width="1.5"/>
  <line x1="205" y1="110" x2="158" y2="192" stroke="rgba(0,10,40,0.45)"     stroke-width="1.5"/>
  <line x1="158" y1="192" x2="62" y2="192"  stroke="rgba(0,5,25,0.55)"      stroke-width="2"/>
  <line x1="62" y1="192" x2="15" y2="110"   stroke="rgba(0,8,35,0.30)"      stroke-width="1.5"/>
  <path fill="url(#fL-gs)" opacity="0.75" transform="translate(4,5)" d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <polygon fill="#8A5C22" opacity="0.85" points="112,60 116,65 116,83 112,78"/>
  <polygon fill="#A07028" opacity="0.80" points="144,110 162,110 166,115 148,115"/>
  <path fill="url(#fL-gd)" d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <path fill="url(#fL-gh)" opacity="0.80" d="M 112,60 L 112,78 A 32,32 0 0,0 80,110 A 50,50 0 0,1 112,60 Z"/>
</svg>'''

# ============================================================
# SVG FAVICON data URI (32x32)
# ============================================================

FAVICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 220"><defs><linearGradient id="v-tl" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#4AABF5"/><stop offset="100%" stop-color="#1C66C4"/></linearGradient><linearGradient id="v-t" x1="30%" y1="0%" x2="70%" y2="100%"><stop offset="0%" stop-color="#3498E8"/><stop offset="100%" stop-color="#1255B0"/></linearGradient><linearGradient id="v-tr" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#1E6DC8"/><stop offset="100%" stop-color="#0A3C90"/></linearGradient><linearGradient id="v-br" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#0A3070"/><stop offset="100%" stop-color="#041540"/></linearGradient><linearGradient id="v-b" x1="50%" y1="100%" x2="50%" y2="0%"><stop offset="0%" stop-color="#031030"/><stop offset="100%" stop-color="#07255C"/></linearGradient><linearGradient id="v-bl" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#041848"/><stop offset="100%" stop-color="#0C3A85"/></linearGradient><linearGradient id="v-fr" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1A5090"/><stop offset="100%" stop-color="#020C28"/></linearGradient><linearGradient id="v-gd" x1="10%" y1="5%" x2="90%" y2="95%"><stop offset="0%" stop-color="#F2DC9A"/><stop offset="35%" stop-color="#D4AB6A"/><stop offset="70%" stop-color="#C09050"/><stop offset="100%" stop-color="#9A6C2E"/></linearGradient><linearGradient id="v-gs" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#9A6C2E"/><stop offset="100%" stop-color="#60400C"/></linearGradient></defs><polygon points="205,110 158,28 62,28 15,110 62,192 158,192" fill="url(#v-fr)" stroke="#0A2258" stroke-width="1"/><polygon points="110,110 15,110 62,28" fill="url(#v-tl)"/><polygon points="110,110 62,28 158,28" fill="url(#v-t)"/><polygon points="110,110 158,28 205,110" fill="url(#v-tr)"/><polygon points="110,110 205,110 158,192" fill="url(#v-br)"/><polygon points="110,110 158,192 62,192" fill="url(#v-b)"/><polygon points="110,110 62,192 15,110" fill="url(#v-bl)"/><line x1="62" y1="28" x2="158" y2="28" stroke="rgba(180,225,255,0.8)" stroke-width="3"/><line x1="15" y1="110" x2="62" y2="28" stroke="rgba(150,210,255,0.6)" stroke-width="2.5"/><path fill="url(#v-gs)" opacity="0.75" transform="translate(4,5)" d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/><path fill="url(#v-gd)" d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/></svg>'''

import urllib.parse
favicon_encoded = urllib.parse.quote(FAVICON_SVG, safe='')
FAVICON_LINK = f'<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,{favicon_encoded}">'

# ============================================================
# CUSTOM GOLD A — add to CSS
# ============================================================

GOLD_A_CSS = '''
    /* Custom gold A in wordmark */
    .logo-text .gold-a {
      color: #C8A96E;
      font-style: normal;
    }
    .logo-text-wordmark {
      display: flex;
      align-items: baseline;
      gap: 0;
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      letter-spacing: 0.1em;
      color: white;
      font-weight: 600;
      line-height: 1;
    }
    .logo-text-wordmark .part-gemc {
      color: white;
    }
    .logo-text-wordmark .part-a {
      color: #C8A96E;
    }
'''

# ============================================================
# HERO LOGO DISPLAY (large, centered above tagline)
# Add after hero badge, before h1
# ============================================================

HERO_LOGO_SVG = '''<div class="reveal" style="display:flex;flex-direction:column;align-items:flex-start;gap:1.25rem;margin-bottom:2rem">
  <div style="display:flex;align-items:center;gap:1.25rem">
    <svg width="72" height="72" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="flex-shrink:0;filter:drop-shadow(0 8px 24px rgba(200,169,110,0.25))">
  <defs>
    <linearGradient id="hL-tl" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#4AABF5"/><stop offset="100%" stop-color="#1C66C4"/></linearGradient>
    <linearGradient id="hL-t"  x1="30%" y1="0%" x2="70%" y2="100%"><stop offset="0%" stop-color="#3498E8"/><stop offset="100%" stop-color="#1255B0"/></linearGradient>
    <linearGradient id="hL-tr" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#1E6DC8"/><stop offset="100%" stop-color="#0A3C90"/></linearGradient>
    <linearGradient id="hL-br" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#0A3070"/><stop offset="100%" stop-color="#041540"/></linearGradient>
    <linearGradient id="hL-b"  x1="50%" y1="100%" x2="50%" y2="0%"><stop offset="0%" stop-color="#031030"/><stop offset="100%" stop-color="#07255C"/></linearGradient>
    <linearGradient id="hL-bl" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#041848"/><stop offset="100%" stop-color="#0C3A85"/></linearGradient>
    <linearGradient id="hL-fr" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1A5090"/><stop offset="100%" stop-color="#020C28"/></linearGradient>
    <linearGradient id="hL-gd" x1="10%" y1="5%" x2="90%" y2="95%"><stop offset="0%" stop-color="#F2DC9A"/><stop offset="35%" stop-color="#D4AB6A"/><stop offset="70%" stop-color="#C09050"/><stop offset="100%" stop-color="#9A6C2E"/></linearGradient>
    <linearGradient id="hL-gs" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#9A6C2E"/><stop offset="100%" stop-color="#60400C"/></linearGradient>
    <linearGradient id="hL-gh" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#FFF0C8" stop-opacity="0.6"/><stop offset="100%" stop-color="#E8C070" stop-opacity="0"/></linearGradient>
    <radialGradient id="hL-gw" cx="35%" cy="30%" r="60%"><stop offset="0%" stop-color="#6AC8FF" stop-opacity="0.22"/><stop offset="100%" stop-color="#6AC8FF" stop-opacity="0"/></radialGradient>
    <filter id="hL-sh" x="-15%" y="-15%" width="130%" height="130%"><feDropShadow dx="0" dy="5" stdDeviation="9" flood-color="#000820" flood-opacity="0.6"/></filter>
  </defs>
  <polygon filter="url(#hL-sh)" points="205,110 158,28 62,28 15,110 62,192 158,192" fill="#020A1E" opacity="0.45" transform="translate(2,4)"/>
  <polygon points="205,110 158,28 62,28 15,110 62,192 158,192" fill="url(#hL-fr)" stroke="#0A2258" stroke-width="2"/>
  <polygon points="110,110 15,110 62,28"  fill="url(#hL-tl)"/>
  <polygon points="110,110 62,28 158,28"  fill="url(#hL-t)"/>
  <polygon points="110,110 158,28 205,110" fill="url(#hL-tr)"/>
  <polygon points="110,110 205,110 158,192" fill="url(#hL-br)"/>
  <polygon points="110,110 158,192 62,192" fill="url(#hL-b)"/>
  <polygon points="110,110 62,192 15,110"  fill="url(#hL-bl)"/>
  <line x1="62" y1="28" x2="158" y2="28"   stroke="rgba(180,225,255,0.82)" stroke-width="3"/>
  <line x1="15" y1="110" x2="62" y2="28"    stroke="rgba(150,210,255,0.60)" stroke-width="2.5"/>
  <line x1="158" y1="28" x2="205" y2="110"  stroke="rgba(100,170,235,0.30)" stroke-width="1.8"/>
  <line x1="205" y1="110" x2="158" y2="192" stroke="rgba(0,10,40,0.50)"     stroke-width="1.8"/>
  <line x1="158" y1="192" x2="62" y2="192"  stroke="rgba(0,5,25,0.60)"      stroke-width="2.5"/>
  <line x1="62" y1="192" x2="15" y2="110"   stroke="rgba(0,8,35,0.35)"      stroke-width="1.5"/>
  <polygon points="62,28 15,110 28,110 68,42"  fill="rgba(180,225,255,0.18)"/>
  <polygon points="158,28 205,110 192,110 152,42" fill="rgba(80,140,210,0.08)"/>
  <polygon points="205,110 158,28 62,28 15,110 62,192 158,192" fill="url(#hL-gw)"/>
  <path fill="#4A2C06" opacity="0.40" transform="translate(7,8)"  d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <path fill="url(#hL-gs)" opacity="0.80" transform="translate(4,5)" d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <polygon fill="#8A5C22" opacity="0.88" points="112,60 116,65 116,83 112,78"/>
  <polygon fill="#A07028" opacity="0.82" points="144,110 162,110 166,115 148,115"/>
  <path fill="url(#hL-gd)" d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <path fill="url(#hL-gh)" opacity="0.85" d="M 112,60 L 112,78 A 32,32 0 0,0 80,110 A 50,50 0 0,1 112,60 Z"/>
  <path fill="none" stroke="rgba(255,245,200,0.50)" stroke-width="2" stroke-linecap="round" d="M 110,79 A 31,31 0 0,0 81,109"/>
</svg>
    <div>
      <div style="font-family:\'Cormorant Garamond\',serif;font-size:2.25rem;font-weight:600;letter-spacing:0.12em;color:white;line-height:1">GEM<span style="color:#C8A96E">C</span><span style="color:#C8A96E;font-weight:700">A</span></div>
      <div style="font-size:10px;letter-spacing:0.22em;text-transform:uppercase;color:rgba(255,255,255,0.45);margin-top:4px">Goraya Education &amp; Migration Consultant Australia</div>
      <div style="font-size:9px;letter-spacing:0.15em;text-transform:uppercase;color:#C8A96E;margin-top:4px;opacity:0.8">Excellence &nbsp;·&nbsp; Integrity &nbsp;·&nbsp; Collaboration &nbsp;·&nbsp; Impact</div>
    </div>
  </div>
</div>'''

# ============================================================
# NOW DO THE REPLACEMENTS
# ============================================================

# 1. Add SVG favicon link in <head> after <title>
html = html.replace(
    '<link rel="preconnect" href="https://fonts.googleapis.com">',
    FAVICON_LINK + '\n  <link rel="preconnect" href="https://fonts.googleapis.com">',
    1
)

# 2. Add gold-A CSS to existing style block (before closing </style>)
html = html.replace(
    '    /* =====================',
    GOLD_A_CSS + '\n    /* =====================',
    1
)

# 3. Replace navbar SVG (the old 44x44 hexagon SVG)
old_navbar_svg_start = '    <!-- Premium hexagon SVG logo with stylized G -->'
old_navbar_svg_end = '</svg>\n    <div>'
idx_start = html.find(old_navbar_svg_start)
idx_end = html.find(old_navbar_svg_end, idx_start) + len(old_navbar_svg_end)
if idx_start != -1 and idx_end > idx_start:
    html = html[:idx_start] + NAVBAR_LOGO_NEW + '\n    <div>' + html[idx_end:]
    print('✓ Navbar SVG replaced')
else:
    print('✗ Navbar SVG not found')

# 4. Replace the wordmark spans with custom gold A version
html = html.replace(
    '<span class="logo-text">GEMCA</span>',
    '<span class="logo-text" style="font-family:\'Cormorant Garamond\',serif;font-size:22px;letter-spacing:0.1em;color:white;font-weight:600">GEM<span style="color:#C8A96E">CA</span></span>',
    1  # only first occurrence (navbar)
)

# 5. Replace footer SVG (the old simple hex SVG)
old_footer_svg = '<svg width="38" height="38" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">'
old_footer_svg_end = '</svg>'
idx_f = html.find(old_footer_svg)
if idx_f != -1:
    idx_f_end = html.find(old_footer_svg_end, idx_f) + len(old_footer_svg_end)
    html = html[:idx_f] + FOOTER_LOGO_NEW + html[idx_f_end:]
    print('✓ Footer SVG replaced')
else:
    print('✗ Footer SVG not found')

# 6. Insert hero logo display before the hero badge
# The hero badge starts with class="hero-badge"
HERO_BADGE_MARKER = '<div class="hero-badge'
idx_hb = html.find(HERO_BADGE_MARKER)
if idx_hb != -1:
    html = html[:idx_hb] + HERO_LOGO_SVG + '\n        ' + html[idx_hb:]
    print('✓ Hero logo inserted')
else:
    print('✗ Hero badge marker not found')

# 7. Write the updated file
with open('/home/user/GEMCA/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'✓ Done — file written, total lines: {html.count(chr(10))}')
