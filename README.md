# GEMCA Website

Premium marketing website for **Goraya Education & Migration Consultant Australia Pty Ltd (GEMCA)**.

Built with Astro + Tailwind CSS. Exports to a fully static `dist/` folder — no server required.

---

## Quick Start (Local Development)

1. Make sure you have **Node.js 18+** installed.
2. Open a terminal in this project folder.
3. Run:
   ```
   npm install
   npm run dev
   ```
4. Open `http://localhost:4321` in your browser.

To build the final files for upload:
```
npm run build
```
The ready-to-upload files will appear in the `dist/` folder.

---

## Hostinger Deployment (Step-by-Step)

You do **not** need any technical knowledge to deploy. Follow these steps:

1. **Run the build** on your computer (or this build environment):
   ```
   npm run build
   ```
   This creates a `dist/` folder with everything the website needs.

2. **Log in to Hostinger** at hpanel.hostinger.com.

3. In your hosting dashboard, find the domain **www.gemca.com.au** and click **Manage**.

4. In the left sidebar, click **Files → File Manager**.

5. Navigate into the **`public_html`** folder (this is where your live website lives).

6. **Delete any existing files** inside `public_html` (or move them to a backup folder first).

7. Click **Upload** in the file manager toolbar.

8. Upload the **entire contents** of the `dist/` folder:
   - `index.html`
   - `insights/` (whole folder)
   - `assets/` (whole folder)
   - `favicon.svg`
   - `robots.txt`
   - `sitemap.xml`

   > **Important:** Upload the *contents* of `dist/`, not the `dist/` folder itself. Your `public_html` should contain `index.html` at its root — not `dist/index.html`.

9. Visit `https://www.gemca.com.au` — your site is live.

---

## How to Edit Copy

All content lives in the component files inside `src/components/`. Each file is clearly named:

| File | What it controls |
|---|---|
| `src/components/Hero.astro` | Hero headline, subheading, trust badges |
| `src/components/TrustStrip.astro` | Stats (500+, 98%, etc.) and trust badge row |
| `src/components/Services.astro` | The six service cards |
| `src/components/VisaExplorer.astro` | Visa category tabs and subclass descriptions |
| `src/components/Pathway.astro` | The four-step Assess → Strategise → Lodge → Outcome section |
| `src/components/WhyGemca.astro` | Why GEMCA credentials and testimonials |
| `src/components/Insights.astro` | Article teaser cards on the homepage |
| `src/pages/insights.astro` | Full insights/articles page |
| `src/components/FAQ.astro` | Accordion FAQ items |
| `src/components/Contact.astro` | Contact details and enquiry form |
| `src/components/Footer.astro` | Footer links, social, MARA registration line, disclaimer |

To edit text, open the file, change the content inside the quotes, then run `npm run build` again and re-upload `dist/`.

---

## TODO Placeholders (Must Fill Before Launch)

These two items are marked with amber-dashed outlines in the live site. **Do not launch without completing them — the MARA Code of Conduct requires your registration number to be displayed.**

### 1. MARN — MARA Registration Number

**Where it appears:** Footer (`src/components/Footer.astro`, line ~50) and optionally in the hero trust strip.

**What to do:** Log in to the MARA portal, find your registration number, and replace the placeholder text:
```
CONFIRM — display MARN before launch (MARA Code requirement)
```
with the actual number, e.g.:
```
MARN: 1234567
```

### 2. Formspree Enquiry Form Endpoint

**Where it appears:** `src/components/Contact.astro`, in the `<form action="...">` attribute and the TODO notice above the form.

**What to do:**
1. Go to formspree.io and create a free account.
2. Create a new form and copy the endpoint URL (looks like `https://formspree.io/f/abcdefgh`).
3. In `src/components/Contact.astro`, replace:
   ```
   action="mailto:ansar@gemca.com.au"
   method="POST"
   enctype="text/plain"
   ```
   with:
   ```
   action="https://formspree.io/f/YOUR_ENDPOINT_ID"
   method="POST"
   ```
4. Remove the amber TODO notice div above the form.
5. Rebuild and re-upload.

**Current fallback:** Until you set up Formspree, form submissions open the user's email client pre-addressed to `ansar@gemca.com.au` — functional but not ideal.

---

## Brand Colours (for reference)

| Name | Hex | Usage |
|---|---|---|
| Royal Blue | `#0B2A6B` | Dominant (~70% of dark sections) |
| Royal Deep | `#05143a` | Darkest backgrounds |
| Royal Light | `#2E5BC7` | Buttons, links, hover states |
| Gold | `#C7A663` | Single accent — hairlines, nodes, tags |
| Platinum | `#C9D0DB` | Frames, dividers, light text on dark |
| Ink | `#11141A` | Body text on light backgrounds |
| Mist | `#F5F6F9` | Alternating section backgrounds |

---

## Compliance Notes

- GEMCA operates under the MARA Code of Conduct. The disclaimer in the footer must remain visible on all pages.
- The stats (500+ Visas, 98% Success, 10+ Years, 50+ Nationalities) and three named testimonials are carried from the original site. Only retain figures you can substantiate.
- Never guarantee visa outcomes in copy. All outcome language should include the qualifier: subject to eligibility and Department of Home Affairs requirements.
