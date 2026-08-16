# Ruth — personal site

Plain HTML and CSS. No build step, no dependencies, no JavaScript. Every file
in this repo is served to the browser exactly as written.

## Files

- `index.html` — the whole site: hero, Who I am, Career history, contact
- `experiments.html` — placeholder, currently `noindex` (see below)
- `css/style.css` — all styling. Colours are CSS variables at the top of the
  file; change them there and both light and dark mode follow.
- `serve.py` — local preview only, never runs in production

There is no templating, so the header and footer are duplicated in both pages.
Change one, change both.

## Preview locally

```bash
python3 serve.py
```

Then open <http://localhost:8000>. Use this rather than opening the `.html`
files directly: the pages use root-relative paths (`/css/style.css`) that only
resolve over HTTP, and `serve.py` resolves `/experiments` → `experiments.html`
the way Netlify does, so local preview matches production.

## Deploying

Netlify watches the `main` branch. Push and it deploys in about 30 seconds:

```bash
git add -A && git commit -m "Describe the change" && git push
```

Netlify settings: **build command empty**, **publish directory `.`**.
Everything else lives in `netlify.toml`.

## Before launch

Replace `YOURNAME.netlify.app` with the real host once Netlify is connected.
It appears in canonical tags, OG tags, the JSON-LD block, `sitemap.xml`, and
`robots.txt`:

```bash
grep -rn "YOURNAME.netlify.app" --include=*.html --include=*.xml --include=*.txt .
```

Also still to add: `img/og-image.jpg`, 1200×630, used for link previews in
social posts and chat apps. Every page's `<head>` already points at it, so the
file just needs to exist.

## Adding your first experiment

`experiments.html` has a commented-out template block — copy it per entry.
Then two things must change, or the page stays invisible to Google:

1. Delete the `<meta name="robots" content="noindex, follow">` line.
2. Add the page back into `sitemap.xml`:

```xml
  <url>
    <loc>https://YOURNAME.netlify.app/experiments</loc>
    <lastmod>2026-08-16</lastmod>
    <priority>0.8</priority>
  </url>
```

It's held back deliberately: an empty page that Google indexes drags down how
it judges the rest of the site.

## SEO notes

Two things would meaningfully improve how findable this site is, both currently
left out by choice:

- **A surname.** "Ruth" alone is one of the hardest possible queries to rank
  for. A full name is what gives Google a distinctive string to attach an
  identity to.
- **The `sameAs` array** in the JSON-LD block in `index.html`, currently
  absent. It's how Google connects this site, a LinkedIn profile, and a GitHub
  account into a single person. Adding profile URLs there — and linking back to
  this site from those profiles — is the single highest-impact change
  available.

Otherwise: each page has a hand-written `<meta name="description">`, which is
the text that shows under the title in search results. After deploying, verify
the site in [Google Search Console](https://search.google.com/search-console)
and submit `/sitemap.xml` — that's what gets you indexed in days rather than
months.

## Moving to a custom domain later

1. Add the domain in Netlify under *Domain management*.
2. Point the registrar's nameservers at Netlify; SSL is automatic.
3. Find-and-replace `YOURNAME.netlify.app` with the new domain, then push.
