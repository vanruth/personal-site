# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS, no build step, no framework, no dependencies. Vanilla JS
used sparingly (scroll/blur interaction on the homepage), never required for
core content to be readable. Deployed to Netlify from GitHub
(`vanruth/personal-site`, `main` branch, auto-deploy on push). Live at
`ruthvan.netlify.app`.

## Users

No single priority audience — deliberately serves a mix evenly:

- Recruiters or hiring managers who land on the site after searching her name
  (the Experience section reads as an early-career CV: internships at
  Tradeweb, Hatch, MFA Singapore).
- Potential collaborators interested in the small digital products/side
  projects she builds (the Works/Experiments section, currently empty).
- General professional contacts or acquaintances looking her up after meeting
  her, or before a conversation.

## Product Purpose

A personal identity site whose primary job is to make "Ruth" resolve to
something real and legible when searched on Google — a combined lightweight
CV, personal introduction, and (eventually) project showcase in one place.

## Positioning

Not applicable in the competitive-product sense — this is a personal, not
commercial, site. What distinguishes it is voice and restraint, not market
position: plain, fast, honest about what's real and what's still empty.

## Operating Context

Typical visit: arrives via a Google search of her name, skims in well under a
minute, likely cross-references LinkedIn or other search results alongside
it. Not a destination people browse deeply or return to often.

## Capabilities and Constraints

- Every page hand-written HTML with a shared `css/style.css`; no CMS, no
  templating — editing means editing the HTML directly.
- No JavaScript required for content to render or be readable; where JS adds
  interaction (scroll centering/blur on the homepage), it degrades to a plain,
  fully-readable page without it.
- SEO is a first-class technical requirement, not an afterthought: per-page
  `<title>`/meta description, canonical tags, Open Graph tags, JSON-LD
  `Person` schema, hand-maintained `sitemap.xml`, `robots.txt`.
- The Works/Experiments page is intentionally empty ("coming soon") and
  marked `noindex` until real projects exist. Do not fabricate example
  projects to fill it — an indexed empty page actively hurts the rest of the
  site's search standing, which is the opposite of this site's purpose.

## Brand Commitments

- Goes by first name only, **"Ruth"** — no surname anywhere on the site.
  This was chosen deliberately, against the explicit advice that it makes the
  name far harder to rank for. Do not add a surname without asking again.
- **No LinkedIn or GitHub links**, and **no `sameAs` entries** in the JSON-LD.
  Explicit choice, made knowingly against the advice that this is the
  strongest available signal for Google to connect the site to a single
  identity. Do not add profile links without asking again.
- **No headshot or photo** anywhere on the site. Explicit choice.
- **Visual identity is "editorial + tech + handwritten"** (superseded the
  original brown-accent/system-font-only identity below on explicit request).
  Editorial leads; tech and handwritten are accents on top, not equal thirds:
  - **Editorial**: Libre Caslon Text (incl. italic) carries body copy and
    headings — chosen specifically to avoid the "AI-default" serif cluster
    (Fraunces/Playfair/Lora/Cormorant/Newsreader) and the "warm cream +
    high-contrast serif + terracotta" look those defaults tend to produce.
  - **Tech**: JetBrains Mono labels section running heads (`§ 01`, etc.), the
    nav, career-history years, and metadata — real data/structure, not
    decoration.
  - **Handwritten**: Caveat, used only for small marginal annotation notes
    beside the section currently in focus (desktop, ≥78rem, where there's
    real margin to hold them) and a hand-drawn underline SVG on the tagline's
    two key verbs. Never used for headings or body copy.
  - Accent is now a ballpoint-blue ink color (`#1f4a94` light / `#89aee6`
    dark) — deliberately not brown, not terracotta, not a warm cream+serif
    combination, to sit outside the common AI-generated-interface palette
    clusters. The previous brown accent (`#8a5638` / `#cf9f7c`) and the
    system-font-only rule are both **superseded**, not standing constraints —
    don't revert to either without asking again.
  - Sections are bound by a hairline rule, not a filled card — a deliberate
    anti-pattern avoidance (don't wrap everything in card chrome).
- Only contact channel listed is a single email (`vanruth123@gmail.com`). No
  phone, no other social channels, by choice.

## Evidence on Hand

Real, current content (not placeholder) lives in `index.html`:

- Bio: multidisciplinary background in Philosophy, Politics & Economics with
  Social Data Science.
- Career history: Tradeweb (2024, product management intern), Hatch (2023,
  marketing intern), MFA Singapore (2022, information services assistant).
- Education: UCL, BSc Philosophy, Politics & Economics with Social Data
  Science, 2022–25.

Works/Experiments has **no real projects yet** — stated absence, not a gap to
fill with invented ones.

## Product Principles

1. **Findability over polish for its own sake.** Structural decisions (page
   count, meta tags, JSON-LD, sitemap, what stays `noindex`) optimize for
   Google search visibility of her name above other concerns.
2. **Restraint over decoration.** Plain HTML/CSS, system fonts, no build
   tooling. Simplicity is the intended feature, not a limitation to grow out
   of.
3. **Real content only.** Never fabricate experience, projects, testimonials,
   or credentials. An honestly empty, `noindex`ed section beats a padded one.
4. **Serves a mixed audience evenly.** No single visitor type — recruiter,
   collaborator, general lookup — gets primary billing over the others.
5. **Personal-brand choices here are sticky, not oversights.** First-name-only,
   no photo, no social links, the brown accent: several of these were made
   deliberately against advice that a "better" SEO/design default exists.
   Future work should not silently revert them.

## Accessibility & Inclusion

No specific documented user need. AA text-contrast has been actively
maintained through past design iterations in both light and dark mode — treat
that as a standing bar to hold, not a one-time pass.
