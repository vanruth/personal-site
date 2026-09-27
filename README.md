# Ruth — personal site

Plain HTML and CSS. No build step, no dependencies, and effectively no
JavaScript — the only exception is a small inline scroll-reveal script at
the end of `index.html` (fades/rises `[data-reveal]` elements into view;
degrades safely with no JS). Every file in this repo is served to the
browser exactly as written.

A single scrolling page — floating nav, hero, projects, about, contact — all
as anchor sections on `/`.

## Files

- `index.html` — the whole site
- `css/style.css` — all styling. Colours are CSS variables at the top of the
  file; change them there and both light and dark mode follow.
- `serve.py` — local preview only, never runs in production

## Preview locally

```bash
python3 serve.py
```

Then open <http://localhost:8000>. Use this rather than opening `index.html`
directly: the page uses root-relative paths (`/css/style.css`) that only
resolve over HTTP.

## Deploying

Netlify watches the `main` branch. Push and it deploys in about 30 seconds:

```bash
git add -A && git commit -m "Describe the change" && git push
```

Netlify settings: **build command empty**, **publish directory `.`**.
Everything else lives in `netlify.toml`.

## Before launch

The real host (`ruthvan.netlify.app`) is already in canonical tags, OG tags,
the JSON-LD block, `sitemap.xml`, and `robots.txt`.

Still to add:

- **A real photo.** `index.html`'s hero currently points at
  `img/headshot-placeholder.svg` (a generic silhouette). Replace the `<img
  src>` with a real photo (portrait, roughly 4:5 works best with
  `.hero__photo-frame`), update its `alt` text to just `"Ruth"`, and delete
  the placeholder SVG.
- `img/og-image.jpg`, 1200×630, used for link previews in social posts and
  chat apps. The `<head>` already points at it, so the file just needs to
  exist.
- A LinkedIn profile link in the contact section, if you want one — there's
  a commented-out `<a class="pill-link">` right next to the email link ready
  to uncomment once you have the URL.

## SEO notes

One thing would meaningfully improve how findable this site is, left out by
choice:

- **A surname.** "Ruth" alone is one of the hardest possible queries to rank
  for. A full name is what gives Google a distinctive string to attach an
  identity to.

Otherwise: the Projects section now has real, indexable content (no more
`noindex` placeholder page to work around), and the JSON-LD `Person` block
carries current role/employer facts. After deploying, verify the site in
[Google Search Console](https://search.google.com/search-console) and submit
`/sitemap.xml` — that's what gets you indexed in days rather than months.

## Moving to a custom domain later

1. Add the domain in Netlify under *Domain management*.
2. Point the registrar's nameservers at Netlify; SSL is automatic.
3. Find-and-replace `ruthvan.netlify.app` with the new domain, then push.
