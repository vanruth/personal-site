# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS, no build step, no framework, no dependencies, no JavaScript
at all — a single scrolling page with anchor-link sections (`#projects`,
`#about`, `#contact`), a fixed floating nav, and hover-only interaction.
Deployed to Netlify from GitHub (`vanruth/personal-site`, `main` branch,
auto-deploy on push). Live at `ruthvan.netlify.app`.

## Users

No single priority audience — deliberately serves a mix evenly:

- Recruiters or hiring managers who land on the site after searching her name
  (the About section reads as an early-career CV: Standard Chartered (SC
  Ventures), Tradeweb, Knovel Engineering (Hatch)).
- Potential collaborators interested in the small digital products/side
  projects she builds (the Projects section — now real, not a placeholder).
- General professional contacts or acquaintances looking her up after meeting
  her, or before a conversation.

## Product Purpose

A personal identity site whose primary job is to make "Ruth" resolve to
something real and legible when searched on Google — a combined lightweight
CV, personal introduction, and project showcase in one place.

## Positioning

Not applicable in the competitive-product sense — this is a personal, not
commercial, site. What distinguishes it is voice and restraint, not market
position: plain, fast, honest about what's real.

## Operating Context

Typical visit: arrives via a Google search of her name, skims in well under a
minute, likely cross-references LinkedIn or other search results alongside
it. Not a destination people browse deeply or return to often.

## Capabilities and Constraints

- Single `index.html` with a shared `css/style.css`; no CMS, no templating —
  editing means editing the HTML directly.
- No JavaScript anywhere. Nav, project-card hover, and section anchors are
  all plain HTML/CSS.
- SEO is a first-class technical requirement, not an afterthought: `<title>`/
  meta description, canonical tag, Open Graph tags, JSON-LD `Person` schema,
  hand-maintained `sitemap.xml`, `robots.txt`.
- The Projects section now carries real content — do not pad it further with
  invented projects, and do not let a future edit quietly turn a real entry
  into a placeholder-sounding one.

## Brand Commitments

- Goes by first name only, **"Ruth"** — no surname anywhere on the site,
  **reaffirmed** after a design reference that showed "Ruth Van" in the
  footer was explicitly declined. Do not add a surname without asking again;
  this has now been asked and declined twice.
- **A real photo has been added to the hero** (reverses the prior no-photo
  choice, confirmed explicitly). As of this writing the `<img>` still points
  at `img/headshot-placeholder.svg` pending the actual file — replace it
  first before treating "has a photo" as true in front of a visitor.
- **LinkedIn: still undecided.** A commented-out `<a class="pill-link">` sits
  next to the email link in the contact section, ready to uncomment once a
  URL is confirmed. Do not add it from a guess.
- **No GitHub link**, and **no `sameAs` entries** in the JSON-LD. Still an
  explicit choice. Don't add without asking again.
- **Visual identity is "tech + handwritten"** (superseded an earlier
  "editorial + tech + handwritten" identity, which itself superseded the
  original brown-accent/system-font identity — each recorded here so the
  reasoning stays legible, not because any is still live):
  - **Tech (leads)**: JetBrains Mono carries nearly everything — nav, hero
    bio, project cards, career-history table. Not a "labels only" accent
    role anymore; it's the primary voice.
  - **Handwritten (accent, three moments only)**: Caveat, used for the nav
    wordmark ("ruth"), the hero greeting ("hey! i'm ruth"), and the contact
    heading ("contact me"). Never for body copy or data.
  - No editorial serif in the current identity — Libre Caslon Text (used in
    the prior "editorial + tech + handwritten" pass) has been dropped
    entirely, not just de-emphasized.
  - Accent stays the ballpoint-blue ink color (`#1f4a94` light / `#89aee6`
    dark) carried over from the previous identity.
  - Sections are plain, no card fill (kept from the previous identity);
    Projects is the one exception — project cards use a filled, tinted card
    treatment with a hover-lift, matching the reference this identity was
    recreated from.
  - Background carries a woven "linen paper" texture (layered diagonal
    hairline crosshatch + fractal noise grain, CSS-only) — more pronounced
    than the previous pass's barely-there grain, per explicit request.
- Only contact channel currently live is a single email
  (`vanruth123@gmail.com`); LinkedIn is pending (see above). No phone.

## Evidence on Hand

Real, current content (not placeholder) lives in `index.html`:

- Bio: multidisciplinary background in political science, economics & data
  science; currently working in innovation.
- Career history: Standard Chartered (SC Ventures) — Venture Building
  Graduate (2026); Tradeweb — Product Management Intern (2024); Knovel
  Engineering (Hatch) — Marketing Intern (2023). MFA Singapore no longer
  listed (dropped on explicit confirmation, not an oversight).
- Education: UCL, BSc (Hons) PPE with Social Data Science.
- Projects (real, confirmed): Language Learning Pro (Notion template),
  Pomodoro Widget (HTML widget), Notification Bot (Telegram automation),
  Habit Tracker Pro (Notion habit tracker). The per-card badges ("Live",
  "25 min", "7 days") and the abstract skeleton-UI card graphics are
  illustrative chrome, not a claim of an actual product screenshot.

## Product Principles

1. **Findability over polish for its own sake.** Structural decisions (meta
   tags, JSON-LD, sitemap) optimize for Google search visibility of her name
   above other concerns.
2. **Restraint over decoration.** Plain HTML/CSS, no build tooling, no JS.
   Simplicity is the intended feature, not a limitation to grow out of.
3. **Real content only.** Never fabricate experience, projects, testimonials,
   or credentials.
4. **Serves a mixed audience evenly.** No single visitor type — recruiter,
   collaborator, general lookup — gets primary billing over the others.
5. **Personal-brand choices here are sticky, not oversights — but they do
   change when the user explicitly changes them.** First-name-only has now
   been reconfirmed twice; the photo and career-history choices have
   reversed on explicit request. Read this file's current state as truth,
   not any single past choice — but still don't revert a recorded choice
   without asking again.

## Accessibility & Inclusion

No specific documented user need. AA text-contrast has been actively
maintained through past design iterations in both light and dark mode — treat
that as a standing bar to hold, not a one-time pass. Re-verify contrast
whenever a new accent/tint colour is introduced (e.g. the four project-card
tints) rather than assuming it inherits the base palette's clearance.
