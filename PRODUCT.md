# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS, no build step, no framework, no dependencies — a single
scrolling page with anchor-link sections (`#projects`, `#about`, `#contact`),
a fixed floating nav, and mostly hover-only interaction. One deliberate,
minimal exception to an otherwise no-JavaScript site: a ~20-line vanilla
script (no dependencies) that fades/rises `[data-reveal]` elements into
place as they scroll into view, using `IntersectionObserver`. It degrades
safely — every element is fully visible immediately if JS is unavailable or
`prefers-reduced-motion` is set — so it never blocks content. Deployed to
Netlify from GitHub (`vanruth/personal-site`, `main` branch, auto-deploy on
push). Live at `ruthvan.netlify.app`.

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
- Effectively no JavaScript. Nav, project-card hover, and section anchors
  are all plain HTML/CSS. The one exception — the `[data-reveal]` scroll
  animation script at the end of `index.html` — was added on explicit
  request after confirming with the user that it's worth breaking the
  no-JS rule for; keep it that way (one small inline script, no build step,
  no dependencies) rather than growing it into more JS over time.
- SEO is a first-class technical requirement, not an afterthought: `<title>`/
  meta description, canonical tag, Open Graph tags, JSON-LD `Person` schema,
  hand-maintained `sitemap.xml`, `robots.txt`.
- The Projects section now carries real content — do not pad it further with
  invented projects, and do not let a future edit quietly turn a real entry
  into a placeholder-sounding one.

## Brand Commitments

- Goes by first name only, **"Ruth"** — no surname anywhere on the site.
  Reaffirmed a second time after the user's own Figma mockup showed "Ruth
  Van" in the footer; declined again. Do not add a surname without asking
  again — this has now been asked and declined twice.
- **A real photo is live in the hero** (`img/headshot.png`) — reverses the
  original no-photo choice, confirmed explicitly, sourced from the user's own
  Figma design rather than a separate upload. Not a placeholder.
- **LinkedIn is live**: `https://www.linkedin.com/in/ruth-van/`, in the
  contact section and in the JSON-LD `sameAs`. Reverses the original
  no-social-links choice, confirmed explicitly with the URL supplied.
- **No GitHub link.** Still an explicit choice. Don't add without asking.
- **Footer carries "Privacy Policy" and "Terms & Conditions"**, confirmed as
  **deliberately non-clickable placeholder text** (plain `<span>`s, not
  `<a>`s) — no real pages exist. Do not turn these into real links without
  either real page content or asking again.
- **Visual identity recreated faithfully from a Figma design**
  (figma.com/design/EFHezz15epD0friES2o9TS, node 157:8) — supersedes the
  earlier from-scratch "tech + handwritten" pass, which itself superseded
  "editorial + tech + handwritten," which superseded the original
  brown-accent/system-font identity. Each recorded here so the reasoning
  stays legible, not because any but the current one is live:
  - **Fonts changed from the previous pass**: IBM Plex Mono (not JetBrains
    Mono) carries nav/body/data; La Belle Aurore (not Caveat) is the
    handwritten face, reserved for the same three moments — nav wordmark,
    hero greeting, "contact me" — never body copy or data.
  - **Accent changed from ballpoint-blue to warm taupe.** The source
    specified `#a48670`, which measured 2.72:1 against the page background —
    under AA even at the large-text 3:1 allowance. Darkened to `#7d5738`
    light / `#d1b596` dark, same hue, clears 4.5:1 comfortably. If the accent
    is ever revisited, keep it AA-checked; don't silently restore the exact
    source value.
  - **Project cards now show a detailed browser-chrome mockup** (tabs dots +
    window controls, using real downloaded SVG icons on the first card;
    skeleton content bars + a status chip on all four) on one of four tinted
    backgrounds (`--tint-1..4`, exact values from the source) — a more
    literal "screenshot" stand-in than the previous plain skeleton bars.
    Still illustrative chrome, not a claim of a real product screenshot.
    Re-verified against the source's exact node geometry (not just the
    screenshot): only the tinted mockup box is a "card" — the title and
    description sit as plain text below it, not inside a bordered/shadowed
    container. The eyebrow + heading form a narrow left rail beside the 2x2
    card grid (not a full-width header above it), a layout the flattened
    React/Tailwind export doesn't make obvious from bounding boxes alone.
  - **Hero photo sits in a straight (non-tilted) white mat**, not the
    rotated/tilted polaroid treatment from an earlier pass. Tilts a few
    degrees on hover as a small interactive touch (not shown in the static
    source, since it can't show hover states).
  - Removed the woven "linen paper" background texture and the decorative
    SVG marginalia from the previous pass — the texture made the hero's
    large empty area read as a visibly different shade from the nav's
    solid-filled background; the user asked for both gone.
  - Contact pill uses a literal black/`--text`-coloured border (not the
    muted `--rule` tone used elsewhere) — a deliberate stronger accent
    around the one clearly interactive cluster on the page, per the source.
  - **About/Contact/Footer re-verified against exact node geometry.** The
    About body copy is one continuous paragraph in the source (not the two
    separate `<p>` tags an earlier pass split it into) — merged back to one.
    About/Contact/Footer all independently measure an ~80px side gutter in
    the source (Projects measures a distinctly narrower 55px) — each section
    keeps its own gutter rather than sharing one value. Contact's heading/
    body/pill block totals exactly 400px tall at the 1512px design width,
    matching the source's tinted background rectangle exactly once the
    real 100px/70px-line-height "contact me" size (not a smaller clamp) is
    used — a good cross-check that the numbers are right.
- Only contact channels: email (`vanruth123@gmail.com`) and LinkedIn (above).
  No phone.

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
