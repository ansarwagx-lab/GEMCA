#!/usr/bin/env python3
"""Apply 3 specific changes to index.html:
1. New premium crystal hexagon logo (navbar, hero, footer, favicon)
2. Redesign hero right side (Opera House outline + repositioned flag cards + AU map)
3. Fix stats to static display
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# SHARED SVG LOGO BUILDER
# Each instance gets a unique gradient-ID prefix to avoid conflicts.
# ============================================================

def make_icon_svg(w, h, pfx):
    """Return the crystal hexagon icon SVG at given size with unique gradient prefix."""
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="flex-shrink:0;filter:drop-shadow(0 4px 16px rgba(26,95,180,0.30))">
  <defs>
    <!-- Facet gradients: TL/T bright blue, TR/BR/B/BL deepening navy -->
    <linearGradient id="{pfx}tl" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4AABF5"/>
      <stop offset="100%" stop-color="#1a5fb4"/>
    </linearGradient>
    <linearGradient id="{pfx}t" x1="30%" y1="0%" x2="70%" y2="100%">
      <stop offset="0%" stop-color="#2d7fd8"/>
      <stop offset="100%" stop-color="#1a5fb4"/>
    </linearGradient>
    <linearGradient id="{pfx}tr" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a5fb4"/>
      <stop offset="100%" stop-color="#0B2A6B"/>
    </linearGradient>
    <linearGradient id="{pfx}br" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0B2A6B"/>
      <stop offset="100%" stop-color="#041540"/>
    </linearGradient>
    <linearGradient id="{pfx}b" x1="50%" y1="100%" x2="50%" y2="0%">
      <stop offset="0%" stop-color="#020d2e"/>
      <stop offset="100%" stop-color="#041540"/>
    </linearGradient>
    <linearGradient id="{pfx}bl" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#041848"/>
      <stop offset="100%" stop-color="#0B2A6B"/>
    </linearGradient>
    <!-- Base hex fill -->
    <linearGradient id="{pfx}base" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1a5fb4"/>
      <stop offset="100%" stop-color="#020c28"/>
    </linearGradient>
    <!-- G letterform gradients -->
    <linearGradient id="{pfx}gf" x1="10%" y1="5%" x2="90%" y2="95%">
      <stop offset="0%" stop-color="#F0D880"/>
      <stop offset="35%" stop-color="#E2C48A"/>
      <stop offset="70%" stop-color="#C8A96E"/>
      <stop offset="100%" stop-color="#a07840"/>
    </linearGradient>
    <linearGradient id="{pfx}gt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F5E8A0"/>
      <stop offset="100%" stop-color="#E2C48A"/>
    </linearGradient>
    <linearGradient id="{pfx}gs" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a07840"/>
      <stop offset="100%" stop-color="#7a5820"/>
    </linearGradient>
    <linearGradient id="{pfx}gh" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF8D0" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#E8C070" stop-opacity="0"/>
    </linearGradient>
    <!-- White highlight radial on TL face -->
    <radialGradient id="{pfx}hl" cx="25%" cy="20%" r="55%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.28)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </radialGradient>
    <filter id="{pfx}sh" x="-12%" y="-12%" width="124%" height="124%">
      <feDropShadow dx="0" dy="4" stdDeviation="7" flood-color="#000820" flood-opacity="0.55"/>
    </filter>
  </defs>

  <!-- Drop shadow layer -->
  <polygon filter="url(#{pfx}sh)"
    points="205,110 158,28 62,28 15,110 62,192 158,192"
    fill="#010818" opacity="0.5" transform="translate(2,5)"/>

  <!-- Base hex -->
  <polygon points="205,110 158,28 62,28 15,110 62,192 158,192"
    fill="url(#{pfx}base)" stroke="#1255a0" stroke-width="1.5"/>

  <!-- Six crystal facets -->
  <!-- TL — brightest, light source upper-left -->
  <polygon points="110,110 15,110 62,28"  fill="url(#{pfx}tl)"/>
  <!-- T — medium-bright -->
  <polygon points="110,110 62,28 158,28"  fill="url(#{pfx}t)"/>
  <!-- TR — medium -->
  <polygon points="110,110 158,28 205,110" fill="url(#{pfx}tr)"/>
  <!-- BR — dark navy shadow -->
  <polygon points="110,110 205,110 158,192" fill="url(#{pfx}br)"/>
  <!-- B — darkest -->
  <polygon points="110,110 158,192 62,192" fill="url(#{pfx}b)"/>
  <!-- BL — medium-dark -->
  <polygon points="110,110 62,192 15,110"  fill="url(#{pfx}bl)"/>

  <!-- Edge highlights — bright edges catch the light -->
  <line x1="62"  y1="28"  x2="158" y2="28"   stroke="rgba(200,235,255,0.85)" stroke-width="2.8"/>
  <line x1="15"  y1="110" x2="62"  y2="28"    stroke="rgba(160,215,255,0.65)" stroke-width="2.2"/>
  <line x1="158" y1="28"  x2="205" y2="110"   stroke="rgba(80,150,220,0.30)"  stroke-width="1.8"/>
  <line x1="205" y1="110" x2="158" y2="192"   stroke="rgba(0,8,40,0.55)"      stroke-width="1.8"/>
  <line x1="158" y1="192" x2="62"  y2="192"   stroke="rgba(0,4,20,0.65)"      stroke-width="2.2"/>
  <line x1="62"  y1="192" x2="15"  y2="110"   stroke="rgba(0,6,30,0.40)"      stroke-width="1.5"/>

  <!-- Facet ridge lines from center (subtle) -->
  <line x1="110" y1="110" x2="15"  y2="110" stroke="rgba(255,255,255,0.14)" stroke-width="0.8"/>
  <line x1="110" y1="110" x2="62"  y2="28"  stroke="rgba(255,255,255,0.18)" stroke-width="0.8"/>
  <line x1="110" y1="110" x2="158" y2="28"  stroke="rgba(255,255,255,0.08)" stroke-width="0.8"/>

  <!-- White highlight bevel on TL+T faces -->
  <polygon points="62,28 15,110 30,110 70,42"  fill="rgba(200,235,255,0.17)"/>
  <polygon points="62,28 158,28 148,44 72,44"  fill="rgba(220,240,255,0.10)"/>

  <!-- White radial highlight -->
  <polygon points="205,110 158,28 62,28 15,110 62,192 158,192" fill="url(#{pfx}hl)"/>

  <!-- G letterform — 3D extruded gold -->
  <!-- Deep shadow layer -->
  <path fill="#6B3C08" opacity="0.38" transform="translate(8,9)"
    d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <!-- Side extrusion (darker gold — the visible side face) -->
  <path fill="url(#{pfx}gs)" opacity="0.82" transform="translate(4.5,5.5)"
    d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <!-- Top-cap extrusion walls (lighter gold) -->
  <polygon fill="url(#{pfx}gt)" opacity="0.90" points="112,60 117,64 117,82 112,78"/>
  <polygon fill="url(#{pfx}gt)" opacity="0.85" points="144,110 162,110 166.5,114.5 148.5,114.5"/>
  <!-- Front face (gold gradient) -->
  <path fill="url(#{pfx}gf)"
    d="M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z"/>
  <!-- Shimmer highlight on upper-left arc of G -->
  <path fill="url(#{pfx}gh)" opacity="0.80"
    d="M 112,60 L 112,78 A 32,32 0 0,0 80,110 A 50,50 0 0,1 112,60 Z"/>
  <!-- Bright edge on inner arc -->
  <path fill="none" stroke="rgba(255,248,200,0.55)" stroke-width="1.8" stroke-linecap="round"
    d="M 110,79 A 31,31 0 0,0 81,109"/>
</svg>'''


# ============================================================
# 1a. NAVBAR LOGO — replace existing SVG + text block
# ============================================================
OLD_NAVBAR_LOGO = '''  <a href="#" class="logo" aria-label="GEMCA Home">
    <!-- GEMCA Premium Crystal Hexagon Logo -->
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
</svg>
    <div>
      <span class="logo-text" style="font-family:\'Cormorant Garamond\',serif;font-size:22px;letter-spacing:0.1em;color:white;font-weight:600">GEM<span style="color:#C8A96E">CA</span></span>
      <span class="logo-sub">Education &amp; Migration</span>
    </div>
  </a>'''

NEW_NAVBAR_LOGO = '''  <a href="#" class="logo" aria-label="GEMCA Home">
    ''' + make_icon_svg(44, 44, 'n2-') + '''
    <div>
      <span class="logo-text" style="font-family:\'DM Sans\',sans-serif;font-size:20px;letter-spacing:0.14em;color:white;font-weight:700;text-transform:uppercase">GEM<span style="color:rgba(255,255,255,0.85)">C</span><span style="color:#E2C48A;font-weight:800">&#9651;</span></span>
      <span class="logo-sub">Education &amp; Migration</span>
    </div>
  </a>'''

# The triangle ▲ approach for A is a bit odd; use a styled SVG letter instead.
# Actually keep A as letter but gold, and use custom clip-path triangle or just clean gold text.
# Simplest & most professional: GEMC in white + A as gold with CSS clip trick.
# Let me use a cleaner approach: just make A gold text.

NEW_NAVBAR_LOGO = '''  <a href="#" class="logo" aria-label="GEMCA Home">
    ''' + make_icon_svg(44, 44, 'n2-') + '''
    <div>
      <div style="font-family:\'DM Sans\',sans-serif;font-size:19px;letter-spacing:0.16em;color:white;font-weight:700;text-transform:uppercase;line-height:1">GEM<span style="color:rgba(255,255,255,0.9)">C</span><svg width="14" height="19" viewBox="0 0 14 19" style="display:inline-block;vertical-align:middle;margin-bottom:1px" aria-hidden="true"><polygon points="7,0 14,18 0,18" fill="#E2C48A"/></svg></div>
      <span class="logo-sub">Education &amp; Migration</span>
    </div>
  </a>'''

assert OLD_NAVBAR_LOGO in html, "Navbar logo block not found"
html = html.replace(OLD_NAVBAR_LOGO, NEW_NAVBAR_LOGO, 1)
print("✓ Navbar logo replaced")

# ============================================================
# 1b. HERO LOGO — replace existing hero icon + wordmark block
# ============================================================
OLD_HERO_LOGO_START = '''<div class="reveal" style="display:flex;flex-direction:column;align-items:flex-start;gap:1.25rem;margin-bottom:2rem">
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

NEW_HERO_LOGO = '''<div class="reveal" style="display:flex;flex-direction:column;align-items:flex-start;gap:1.25rem;margin-bottom:2rem">
  <div style="display:flex;align-items:center;gap:1.5rem">
    ''' + make_icon_svg(80, 80, 'h2-') + '''
    <div>
      <div style="display:flex;align-items:center;gap:0;font-family:\'DM Sans\',sans-serif;font-size:2.4rem;font-weight:800;letter-spacing:0.18em;color:white;line-height:1;text-transform:uppercase">
        <span>GEM</span><span style="color:rgba(255,255,255,0.9)">C</span><svg width="22" height="30" viewBox="0 0 22 30" style="display:inline-block;vertical-align:middle;margin-bottom:2px" aria-hidden="true"><polygon points="11,0 22,29 0,29" fill="#E2C48A"/></svg>
      </div>
      <div style="font-size:10px;letter-spacing:0.22em;text-transform:uppercase;color:rgba(255,255,255,0.45);margin-top:5px;font-family:\'DM Sans\',sans-serif">Goraya Education &amp; Migration Consultant Australia</div>
      <div style="font-size:9px;letter-spacing:0.16em;text-transform:uppercase;color:#C8A96E;margin-top:4px;font-family:\'DM Sans\',sans-serif">Excellence &nbsp;·&nbsp; Integrity &nbsp;·&nbsp; Collaboration &nbsp;·&nbsp; Impact</div>
    </div>
  </div>
</div>'''

assert OLD_HERO_LOGO_START in html, "Hero logo block not found"
html = html.replace(OLD_HERO_LOGO_START, NEW_HERO_LOGO, 1)
print("✓ Hero logo replaced")

# ============================================================
# 1c. FOOTER LOGO — replace existing footer SVG + text
# ============================================================
OLD_FOOTER_LOGO = '''        <a href="#" class="logo" style="display:inline-flex;margin-bottom:1rem">
          <svg width="38" height="38" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">
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
</svg>
          <div style="margin-left:0.6rem">
            <div style="font-family:\'Cormorant Garamond\',serif;font-size:1.25rem;color:#C8A96E;letter-spacing:0.05em;line-height:1">GEMCA</div>
            <div style="font-size:9px;color:rgba(255,255,255,0.4);letter-spacing:0.12em;text-transform:uppercase;margin-top:2px">Migration &amp; Education</div>
          </div>
        </a>'''

NEW_FOOTER_LOGO = '''        <a href="#" class="logo" style="display:inline-flex;align-items:center;margin-bottom:1rem;gap:0.65rem">
          ''' + make_icon_svg(38, 38, 'f2-') + '''
          <div>
            <div style="display:flex;align-items:center;gap:0;font-family:\'DM Sans\',sans-serif;font-size:1.15rem;font-weight:800;letter-spacing:0.16em;color:white;text-transform:uppercase;line-height:1">
              <span>GEM</span><span>C</span><svg width="10" height="14" viewBox="0 0 10 14" style="display:inline-block;vertical-align:middle;margin-bottom:1px" aria-hidden="true"><polygon points="5,0 10,13 0,13" fill="#E2C48A"/></svg>
            </div>
            <div style="font-size:9px;color:rgba(255,255,255,0.4);letter-spacing:0.12em;text-transform:uppercase;margin-top:2px;font-family:\'DM Sans\',sans-serif">Migration &amp; Education</div>
          </div>
        </a>'''

assert OLD_FOOTER_LOGO in html, "Footer logo not found"
html = html.replace(OLD_FOOTER_LOGO, NEW_FOOTER_LOGO, 1)
print("✓ Footer logo replaced")

# ============================================================
# 1d. FAVICON — update to match new icon style
# ============================================================
OLD_FAVICON = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,'
# Find the full favicon link tag and replace it
import re
favicon_match = re.search(r'<link rel="icon" type="image/svg\+xml" href="[^"]*">', html)
if favicon_match:
    old_fav = favicon_match.group(0)
    # New favicon: simplified crystal hex with gold G, same design
    fav_svg = '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 220 220'><defs><linearGradient id='a' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%234AABF5'/><stop offset='1' stop-color='%231a5fb4'/></linearGradient><linearGradient id='b' x1='1' y1='0' x2='0' y2='1'><stop offset='0' stop-color='%230B2A6B'/><stop offset='1' stop-color='%23020d2e'/></linearGradient><linearGradient id='c' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%23E2C48A'/><stop offset='1' stop-color='%23a07840'/></linearGradient></defs><polygon points='205,110 158,28 62,28 15,110 62,192 158,192' fill='%23081840'/><polygon points='110,110 15,110 62,28' fill='url(%23a)'/><polygon points='110,110 62,28 158,28' fill='%231a5fb4'/><polygon points='110,110 158,28 205,110' fill='%230d4a9a'/><polygon points='110,110 205,110 158,192' fill='url(%23b)'/><polygon points='110,110 158,192 62,192' fill='%23020d2e'/><polygon points='110,110 62,192 15,110' fill='%23041848'/><line x1='62' y1='28' x2='158' y2='28' stroke='rgba(200,235,255,0.8)' stroke-width='3'/><line x1='15' y1='110' x2='62' y2='28' stroke='rgba(160,215,255,0.6)' stroke-width='2.5'/><path fill='%23704010' opacity='0.4' transform='translate(7,8)' d='M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z'/><path fill='url(%23c)' d='M 162,110 A 50,50 0 1,1 112,60 L 112,78 A 32,32 0 0,1 144,110 Z'/></svg>'''
    new_fav = f'<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,{fav_svg}">'
    html = html.replace(old_fav, new_fav, 1)
    print("✓ Favicon updated")
else:
    print("⚠ Favicon link not found — skipping")

# ============================================================
# CHANGE 2 — Hero right: fix flag card positions + Opera House
#             gold outline + add Australia map outline
# ============================================================

# 2a. Fix flag card CSS positions
OLD_FLAG_POS = '''    /* card positions */
    .fc-au { top: 8%;  left: 2%;   --fdur:5.2s; --fdelay:0s;    }
    .fc-uk { top: 2%;  left: 35%;  --fdur:6.0s; --fdelay:-1.5s; }
    .fc-ca { top: 8%;  right: 2%;  --fdur:5.6s; --fdelay:-3.0s; }
    .fc-us { bottom: 46%; left: 4%;  --fdur:4.8s; --fdelay:-0.8s; }
    .fc-nz { bottom: 46%; right: 4%; --fdur:5.4s; --fdelay:-2.2s; }
    .fc-eu { bottom: 48%; left: 38%; --fdur:6.2s; --fdelay:-4.0s; }'''

NEW_FLAG_POS = '''    /* card positions — AU:top-left, UK:top-right, CA:mid-left, US:mid-right, NZ:btm-left, EU:btm-right */
    .fc-au { top: 2%;  left: 1%;   --fdur:5.2s; --fdelay:0s;    }
    .fc-uk { top: 2%;  right: 1%;  --fdur:6.0s; --fdelay:-1.5s; }
    .fc-ca { top: 38%; left: 1%;   --fdur:5.6s; --fdelay:-3.0s; }
    .fc-us { top: 38%; right: 1%;  --fdur:4.8s; --fdelay:-0.8s; }
    .fc-nz { bottom: 3%; left: 1%;  --fdur:5.4s; --fdelay:-2.2s; }
    .fc-eu { bottom: 3%; right: 1%; --fdur:6.2s; --fdelay:-4.0s; }'''

assert OLD_FLAG_POS in html, "Flag card positions CSS not found"
html = html.replace(OLD_FLAG_POS, NEW_FLAG_POS, 1)
print("✓ Flag card positions fixed")

# 2b. Replace Opera House SVG with gold outline version + add AU map behind it
OLD_OPERA_SVG_START = '        <!-- Sydney Opera House SVG silhouette -->'
NEW_OPERA_BLOCK = '''        <!-- Australia map outline — barely visible at 10% opacity -->
        <svg viewBox="0 0 520 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"
          style="position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:100%;max-width:520px;opacity:0.1;pointer-events:none;z-index:1">
          <!-- Simplified Australia mainland outline -->
          <path fill="#1a5fb4" d="
            M 180,60 L 200,45 L 230,40 L 265,42 L 295,38 L 320,42 L 340,55 L 355,65
            L 370,60 L 385,50 L 400,55 L 415,70 L 420,90 L 415,110 L 420,130
            L 430,150 L 435,175 L 425,195 L 410,210 L 390,220 L 370,215
            L 350,205 L 335,195 L 320,200 L 305,210 L 285,215 L 265,210
            L 248,195 L 240,175 L 245,155 L 240,135 L 228,120 L 215,115
            L 200,120 L 185,130 L 175,145 L 165,140 L 158,125 L 155,108
            L 158,90 L 165,75 Z"/>
          <!-- Tasmania -->
          <ellipse cx="320" cy="245" rx="22" ry="16" fill="#1a5fb4"/>
        </svg>

        <!-- Sydney Opera House SVG — gold outline style -->'''

OLD_OPERA_SVG_BLOCK = '''        <!-- Sydney Opera House SVG silhouette -->
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
        </div>'''

NEW_OPERA_BLOCK2 = OLD_OPERA_SVG_START.replace(
    '        <!-- Sydney Opera House SVG silhouette -->',
    OLD_OPERA_SVG_START
)

# Replace the entire old opera block with new outline version + AU map
NEW_OPERA_SVG = '''        <!-- Australia map outline — barely visible at 10% opacity -->
        <svg viewBox="0 0 520 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"
          style="position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:90%;max-width:460px;opacity:0.10;pointer-events:none;z-index:1">
          <path fill="#1a5fb4" d="M 180,60 L 200,45 L 230,40 L 265,42 L 295,38 L 320,42 L 340,55 L 355,65 L 370,60 L 385,50 L 400,55 L 415,70 L 420,90 L 415,110 L 420,130 L 430,150 L 435,175 L 425,195 L 410,210 L 390,220 L 370,215 L 350,205 L 335,195 L 320,200 L 305,210 L 285,215 L 265,210 L 248,195 L 240,175 L 245,155 L 240,135 L 228,120 L 215,115 L 200,120 L 185,130 L 175,145 L 165,140 L 158,125 L 155,108 L 158,90 L 165,75 Z"/>
          <ellipse cx="320" cy="245" rx="22" ry="16" fill="#1a5fb4"/>
        </svg>

        <!-- Sydney Opera House SVG — gold outline style with glow -->
        <div class="opera-house-wrap">
          <svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" aria-label="Sydney Opera House silhouette" style="width:100%;display:block;">
            <defs>
              <filter id="oh2-glow" x="-15%" y="-30%" width="130%" height="160%">
                <feGaussianBlur stdDeviation="5" result="blur"/>
                <feColorMatrix in="blur" type="matrix"
                  values="1 0.85 0.3 0 0.05  0.85 0.65 0.2 0 0.03  0.2 0.1 0 0 0  0 0 0 0.5 0"
                  result="goldglow"/>
                <feMerge>
                  <feMergeNode in="goldglow"/>
                  <feMergeNode in="SourceGraphic"/>
                </feMerge>
              </filter>
              <linearGradient id="oh2-base" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#E2C48A" stop-opacity="0.18"/>
                <stop offset="100%" stop-color="#C8A96E" stop-opacity="0.06"/>
              </linearGradient>
            </defs>

            <!-- Faint fill inside shells for depth -->
            <path d="M 60,190 Q 65,155 80,115 Q 100,65 130,35 Q 140,25 148,32 Q 155,40 148,75 Q 138,115 118,155 Q 100,178 85,190 Z" fill="url(#oh2-base)"/>
            <path d="M 85,190 Q 95,165 112,130 Q 130,90 150,62 Q 160,48 168,54 Q 176,62 168,92 Q 155,128 135,160 Q 118,180 100,190 Z" fill="url(#oh2-base)"/>
            <path d="M 112,190 Q 122,170 138,140 Q 155,105 172,80 Q 180,66 186,72 Q 192,80 184,108 Q 172,140 152,165 Q 136,182 122,190 Z" fill="url(#oh2-base)"/>
            <path d="M 135,190 Q 144,175 158,152 Q 172,124 184,102 Q 190,88 195,95 Q 200,104 192,128 Q 180,155 162,174 Q 150,185 140,190 Z" fill="url(#oh2-base)"/>
            <path d="M 260,190 Q 265,168 278,142 Q 296,106 316,82 Q 325,70 332,76 Q 340,84 332,110 Q 320,140 302,163 Q 286,180 272,190 Z" fill="url(#oh2-base)"/>
            <path d="M 278,190 Q 286,172 300,150 Q 316,122 332,100 Q 340,88 345,94 Q 350,102 342,125 Q 330,152 312,170 Q 298,183 286,190 Z" fill="url(#oh2-base)"/>
            <path d="M 298,190 Q 306,176 318,158 Q 332,134 344,114 Q 350,102 354,108 Q 358,116 350,138 Q 338,162 320,178 Q 308,188 300,190 Z" fill="url(#oh2-base)"/>

            <!-- Gold outline shells — main concert hall (left group) -->
            <g filter="url(#oh2-glow)" fill="none" stroke="#C8A96E" stroke-linecap="round" stroke-linejoin="round">
              <!-- Shell 1 — tallest outer left -->
              <path stroke-width="1.8" d="M 60,190 Q 65,155 80,115 Q 100,65 130,35 Q 140,25 148,32 Q 155,40 148,75 Q 138,115 118,155 Q 100,178 85,190"/>
              <!-- Shell 2 -->
              <path stroke-width="1.6" d="M 85,190 Q 95,165 112,130 Q 130,90 150,62 Q 160,48 168,54 Q 176,62 168,92 Q 155,128 135,160 Q 118,180 100,190"/>
              <!-- Shell 3 -->
              <path stroke-width="1.4" d="M 112,190 Q 122,170 138,140 Q 155,105 172,80 Q 180,66 186,72 Q 192,80 184,108 Q 172,140 152,165 Q 136,182 122,190"/>
              <!-- Shell 4 innermost left -->
              <path stroke-width="1.2" d="M 135,190 Q 144,175 158,152 Q 172,124 184,102 Q 190,88 195,95 Q 200,104 192,128 Q 180,155 162,174 Q 150,185 140,190"/>

              <!-- Opera theatre shells (right group) -->
              <!-- Shell A -->
              <path stroke-width="1.6" d="M 260,190 Q 265,168 278,142 Q 296,106 316,82 Q 325,70 332,76 Q 340,84 332,110 Q 320,140 302,163 Q 286,180 272,190"/>
              <!-- Shell B -->
              <path stroke-width="1.4" d="M 278,190 Q 286,172 300,150 Q 316,122 332,100 Q 340,88 345,94 Q 350,102 342,125 Q 330,152 312,170 Q 298,183 286,190"/>
              <!-- Shell C innermost right -->
              <path stroke-width="1.2" d="M 298,190 Q 306,176 318,158 Q 332,134 344,114 Q 350,102 354,108 Q 358,116 350,138 Q 338,162 320,178 Q 308,188 300,190"/>
            </g>

            <!-- Bright edge on tallest shell tips -->
            <path d="M 130,35 Q 140,25 148,32" fill="none" stroke="#E8C87A" stroke-width="2" stroke-linecap="round"/>
            <path d="M 316,82 Q 325,70 332,76" fill="none" stroke="#E8C87A" stroke-width="1.8" stroke-linecap="round"/>

            <!-- Podium base — gold outline -->
            <rect x="30" y="185" width="460" height="6" rx="2" fill="none" stroke="#C8A96E" stroke-width="1" opacity="0.7"/>
            <rect x="40" y="182" width="440" height="3" rx="1" fill="none" stroke="rgba(200,169,110,0.35)" stroke-width="0.8"/>
            <rect x="55" y="179" width="410" height="3" rx="1" fill="none" stroke="rgba(200,169,110,0.20)" stroke-width="0.6"/>
          </svg>

          <!-- Water reflection -->
          <div class="water-line"></div>
          <div class="water-reflection"></div>
        </div>'''

assert OLD_OPERA_SVG_BLOCK in html, "Opera House SVG block not found"
html = html.replace(OLD_OPERA_SVG_BLOCK, NEW_OPERA_SVG, 1)
print("✓ Opera House replaced with gold outline + AU map")

# ============================================================
# CHANGE 3 — Fix stats counter: static values, remove JS
# ============================================================

# 3a. Replace HTML stat numbers (remove data-target, set static text)
OLD_STATS_HTML = '''    <div class="stat-item reveal">
      <div class="stat-number" data-target="500" data-suffix="+">0</div>
      <div class="stat-label">Visas Processed</div>
    </div>
    <div class="stat-item reveal reveal-delay-1">
      <div class="stat-number" data-target="98" data-suffix="%">0</div>
      <div class="stat-label">Success Rate</div>
    </div>
    <div class="stat-item reveal reveal-delay-2">
      <div class="stat-number" data-target="6" data-suffix="">0</div>
      <div class="stat-label">Countries</div>
    </div>
    <div class="stat-item reveal reveal-delay-3">
      <div class="stat-number" data-target="10" data-suffix="+">0</div>
      <div class="stat-label">Years Experience</div>
    </div>
    <div class="stat-item reveal reveal-delay-4">
      <div class="stat-number" data-target="50" data-suffix="+">0</div>
      <div class="stat-label">Nationalities Served</div>'''

NEW_STATS_HTML = '''    <div class="stat-item reveal">
      <div class="stat-number">500+</div>
      <div class="stat-label">Visas Processed</div>
    </div>
    <div class="stat-item reveal reveal-delay-1">
      <div class="stat-number">98%</div>
      <div class="stat-label">Success Rate</div>
    </div>
    <div class="stat-item reveal reveal-delay-2">
      <div class="stat-number">6</div>
      <div class="stat-label">Countries</div>
    </div>
    <div class="stat-item reveal reveal-delay-3">
      <div class="stat-number">10+</div>
      <div class="stat-label">Years Experience</div>
    </div>
    <div class="stat-item reveal reveal-delay-4">
      <div class="stat-number">50+</div>
      <div class="stat-label">Nationalities Served</div>'''

assert OLD_STATS_HTML in html, "Stats HTML not found"
html = html.replace(OLD_STATS_HTML, NEW_STATS_HTML, 1)
print("✓ Stats HTML set to static values")

# 3b. Remove the stats counter JS block
OLD_STATS_JS = '''// ===================== STATS COUNTER =====================
const statsObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.dataset.target, 10);
      const suffix = el.dataset.suffix || '';
      let start = 0;
      const duration = 2000;
      const step = Math.ceil(target / (duration / 16));
      const timer = setInterval(() => {
        start += step;
        if (start >= target) {
          el.textContent = target + suffix;
          clearInterval(timer);
        } else {
          el.textContent = start + suffix;
        }
      }, 16);
      statsObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-number[data-target]').forEach(el => statsObserver.observe(el));'''

NEW_STATS_JS = '// Stats: static display (no counter animation needed)'

assert OLD_STATS_JS in html, "Stats JS not found"
html = html.replace(OLD_STATS_JS, NEW_STATS_JS, 1)
print("✓ Stats counter JS removed")

# ============================================================
# Write output
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✓ All 3 changes applied — {len(html.splitlines())} lines total")
