#!/usr/bin/env python3
"""Static page assembler for the First Perfumes site.

The site ships as plain .html files with no server-side includes, so the
header, nav and footer would otherwise be copy-pasted into every page and
drift apart. This script keeps one copy of that chrome in _partials/ and
stamps it onto each page's body fragment from _content/.

    python build.py            # rebuild every page in _content/pages.json
    python build.py contact    # rebuild one page
    python build.py --check    # assemble to memory and report drift, write nothing

Editing content: change _content/<slug>.html and re-run.
Editing nav/footer/head: change _partials/*.html and re-run — every page picks it up.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PARTIALS = os.path.join(ROOT, "_partials")
CONTENT = os.path.join(ROOT, "_content")
SITE_URL = "https://www.firstperfumes.com/"

# Chevron between breadcrumb crumbs, matching the template's icon weight.
CHEVRON = (
    '<svg width="25" height="8" viewBox="0 0 25 8" fill="none" xmlns="http://www.w3.org/2000/svg" '
    'aria-hidden="true"><path d="M24.3536 4.35355C24.5488 4.15829 24.5488 3.84171 24.3536 3.64645'
    'L21.1716 0.464466C20.9763 0.269204 20.6597 0.269204 20.4645 0.464466C20.2692 0.659728 20.2692 '
    '0.976311 20.4645 1.17157L23.2929 4L20.4645 6.82843C20.2692 7.02369 20.2692 7.34027 20.4645 '
    '7.53553C20.6597 7.7308 20.9763 7.7308 21.1716 7.53553L24.3536 4.35355ZM0 4.5H24V3.5H0V4.5Z" '
    'fill="currentColor"/></svg>'
)

# Small quill/scent mark that sits left of the breadcrumb intro paragraph.
PARA_ICON = (
    '<svg width="60" height="8" viewBox="0 0 60 8" fill="none" xmlns="http://www.w3.org/2000/svg" '
    'aria-hidden="true"><path d="M0 4H58M58 4L54 1M58 4L54 7" stroke="currentColor" '
    'stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)


def esc(s):
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def breadcrumb(page):
    """Hero block at the top of every inner page, generated from the manifest
    so the crumb trail and heading can never disagree between pages."""
    crumbs = ['<li><a href="index.html">Home</a></li>']
    for label, href in page.get("trail", []):
        crumbs.append(
            '<li>%s<a href="%s">%s</a></li>' % (CHEVRON, href, esc(label))
        )
    crumbs.append("<li>%s%s</li>" % (CHEVRON, esc(page["breadcrumb"])))
    intro = page.get("intro", "")
    para = ""
    if intro:
        para = (
            '\n                        <div class="para fade_anim" data-fade-from="bottom" '
            'data-delay=".35">\n                            %s\n'
            "                            <p>%s</p>\n"
            "                        </div>" % (PARA_ICON, esc(intro))
        )
    return """                <!-- Breadcrumb Section Start -->
                <div class="breadcrumb-section %s mb-60">
                    <div class="container">
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="breadcrumb-content">
                                    <ul class="breadcrumb-list fade_anim" data-fade-from="top" data-delay=".15">
                                        %s
                                    </ul>
                                    <h1 class="text-anim">%s</h1>%s
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Breadcrumb Section End -->

""" % (
        page.get("breadcrumb_style", "style-2"),
        "\n                                        ".join(crumbs),
        esc(page["h1"]),
        para,
    )


def assemble(page, top, bottom):
    slug = page["slug"]
    frag_path = os.path.join(CONTENT, slug + ".html")
    if not os.path.exists(frag_path):
        return None, "missing _content/%s.html" % slug
    body = open(frag_path, encoding="utf-8").read().rstrip("\n")

    head = top
    head = head.replace("{{TITLE}}", esc(page["title"]))
    head = head.replace("{{DESCRIPTION}}", esc(page["description"]))
    head = head.replace(
        "{{CANONICAL}}", SITE_URL + ("" if slug == "index" else slug + ".html")
    )
    preload = page.get("preload", "")
    head = head.replace(
        "{{PRELOAD}}",
        '<link rel="preload" as="image" href="%s" type="image/webp" />' % preload
        if preload
        else "",
    )
    # mark the active top-level nav item
    nav = page.get("nav")
    if nav:
        head = re.sub(
            r'<li class="(menu-item-has-children[^"]*)" data-nav="%s"' % re.escape(nav),
            lambda m: '<li class="%s active" data-nav="%s"' % (m.group(1), nav),
            head,
            count=1,
        )

    crumb = "" if page.get("breadcrumb") is None else breadcrumb(page)
    return head + "\n" + crumb + body + "\n" + bottom, None


def write_sitemap(pages):
    """sitemap.xml + robots.txt. 404 is excluded: it must not be indexable."""
    urls = []
    for p in pages:
        if p["slug"] == "404":
            continue
        loc = SITE_URL + ("" if p["slug"] == "index" else p["slug"] + ".html")
        prio = "1.0" if p["slug"] == "index" else ("0.8" if p.get("nav") else "0.5")
        urls.append(
            "    <url>\n        <loc>%s</loc>\n        <changefreq>monthly</changefreq>\n"
            "        <priority>%s</priority>\n    </url>" % (loc, prio)
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(xml)
    robots = "User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % SITE_URL
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(robots)
    print("wrote sitemap.xml (%d urls) and robots.txt" % len(urls))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    check = "--check" in sys.argv[1:]

    top = open(os.path.join(PARTIALS, "chrome-top.html"), encoding="utf-8").read()
    bottom = open(os.path.join(PARTIALS, "chrome-bottom.html"), encoding="utf-8").read()
    pages = json.load(open(os.path.join(CONTENT, "pages.json"), encoding="utf-8"))
    if args:
        pages = [p for p in pages if p["slug"] in args]
        if not pages:
            sys.exit("no page in pages.json matches %s" % args)

    written, skipped, drift = 0, [], []
    for page in pages:
        out, err = assemble(page, top, bottom)
        if err:
            skipped.append(err)
            continue
        dest = os.path.join(ROOT, page["slug"] + ".html")
        if check:
            cur = open(dest, encoding="utf-8").read() if os.path.exists(dest) else None
            if cur != out:
                drift.append(page["slug"])
            continue
        with open(dest, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(out)
        written += 1

    if check:
        print("out of date: %s" % (", ".join(drift) if drift else "nothing"))
    else:
        print("built %d page(s)" % written)
        if not args:
            write_sitemap(json.load(open(os.path.join(CONTENT, "pages.json"), encoding="utf-8")))
    for s in skipped:
        print("  skipped: %s" % s)
    return 1 if (check and drift) else 0


if __name__ == "__main__":
    sys.exit(main())
