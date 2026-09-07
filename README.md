# First Perfumes — static site

Marketing site for First Perfumes Ind LLC. Plain HTML, CSS and jQuery — no framework, no
bundler, no server-side rendering. The `*.html` files at the repo root are the deployable
artefact: upload the root directory to any static host and it works.

## The one rule

**Never hand-edit a `*.html` file at the repo root.** They are generated. Edit the source and
re-run the build:

```bash
python build.py
```

The site has no shared-include mechanism of its own, so `build.py` stamps one copy of the
header, nav, mega menu and footer onto every page. Editing a built page directly means your
change is silently reverted by the next build, and the 25 pages drift apart.

## Layout

```
build.py              assembles _partials/ + _content/ -> root *.html, and writes
                      sitemap.xml + robots.txt
check.py              pre-deploy validator (see below)

_content/
  pages.json          the page manifest: slug, title, description, nav, breadcrumb, preload.
                      Adding a page starts here.
  <slug>.html         the body fragment for one page — everything between the header and
                      the footer. This is the source of truth for page copy.

_partials/
  chrome-top.html     doctype, <head>, header, nav, mega menu, opening wrappers
  chrome-bottom.html  footer, closing wrappers, the whole <script> block
  notes-*.md          authoring reference (see below)

css/                  vendor stylesheets + style.css (the purchased theme) +
                      site-fixes.css (all First Perfumes overrides — put new CSS here)
js/                   vendor libraries + custom.js (theme behaviour, largely untouched)
images/               all site imagery
fonts/                icon-font faces for boxicons / bootstrap-icons
media/                the homepage video, its poster frames, and the company profile PDF
```

## Building

| command | does |
|---|---|
| `python build.py` | rebuild all 25 pages, then regenerate `sitemap.xml` and `robots.txt` |
| `python build.py contact` | rebuild one page by slug |
| `python build.py --check` | assemble in memory and report which built pages are stale; writes nothing, non-zero exit if any drift |

`--check` is the one to run in CI or before committing — it catches a built page that was
edited by hand or left un-rebuilt after a partials change.

## Checking

```bash
python check.py            # every page
python check.py contact    # one page
```

`check.py` catches what a browser will not shout about:

* class names in the markup that no stylesheet defines (→ unstyled markup)
* `<img src>`, `<source>`, `<video>`, CSS `url()` and `href` assets missing from disk
* internal links to pages that were never built
* `#fragment` links whose target id does not exist on the destination page
* unbalanced or mis-nested block tags, and duplicate `id` attributes
* images with no `alt`, and pages with no title, description or `<h1>`

Non-zero exit on any error; warnings do not fail. It currently passes clean on all 25 pages.

`check.py` reads the markup; it cannot see layout. For that, serve the site and open
`/_audit.html`, then from the browser console:

```js
await runBatch(0, PAGES.length, 375, 800)    // mobile
await runBatch(0, PAGES.length, 768, 900)    // tablet
await runBatch(0, PAGES.length, 1440, 900)   // desktop
```

It loads each page in an iframe at that viewport and reports horizontal overflow, images
that failed to load, tall empty containers, and flex/grid containers that swallow the
whitespace between a text node and an inline child. `{}` means every page passed. The
harness is `noindex` and nothing links to it, but it is not part of the site — delete it
if you would rather not upload it.

## Previewing

```bash
python -m http.server 8123
```

Then open <http://localhost:8123>. Prefer this over opening a file directly: the video and the
WebGL hover effect both behave differently under `file://`.

`.claude/launch.json` starts the same server on the same port.

## Adding a page

1. Add an entry to `_content/pages.json` (`slug`, `title`, `description`, `breadcrumb`, and
   optionally `nav`, `trail`, `intro`, `preload`).
2. Create `_content/<slug>.html` with just the body fragment, indented to 16 spaces to match
   the existing fragments.
3. `python build.py <slug> && python check.py <slug>`.

Read `_partials/notes-authoring-rules.md` first — the theme's CSS only styles class names it
already knows, so inventing markup gets you an unstyled block and a `check.py` error.

## The notes files

`_partials/notes-*.md` are the authoring reference for this theme. They are long because the
purchased template's JavaScript is undocumented and full of hooks that only fire under
specific markup.

| file | covers |
|---|---|
| `notes-authoring-rules.md` | the hard rules: what you may and may not invent |
| `notes-components.md` | the section components available, with the exact markup each needs |
| `notes-inner-pages.md` | per-page structure of the 24 inner pages |
| `notes-motion-and-assets.md` | every animation hook (`fade_anim`, `text-anim`, Swiper, ScrollSmoother, …), the script load order, and a full inventory of `images/` and `media/` |

`notes-motion-and-assets.md` sections A20 ("safe vs. do-not-copy") and A21 ("known defects in
`custom.js`") are the two worth reading before touching any interactive section.

## Known weight

The site ships a 1.8 MB unminified `js/three.js` on every page for one WebGL hover effect on
the homepage, and a 1.2 MB `images/boxicons.svg`. Neither is dead — both are wired up — but
both are the obvious next optimisation. See section B10 of the motion-and-assets notes.

## Historical

`_content/_lib/` holds the one-shot Python generators that produced the first draft of the
page fragments in `_content/`. **They are not part of the build** — `build.py` does not import
them, and re-running them would overwrite hand-edited content with regenerated markup. They
are kept only as a record of how the fragments were originally derived. Treat `_content/*.html`
as the source of truth.
