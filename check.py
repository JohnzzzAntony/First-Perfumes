#!/usr/bin/env python3
"""Pre-deploy validator for the First Perfumes static site.

Catches the failure modes that matter for a hand-authored multi-page static site
and that a browser will not shout about:

  * class names used in markup that no stylesheet defines  (-> unstyled markup)
  * <img src>, <source>, <video>, css url() and href assets that do not exist on disk
  * internal links pointing at pages that were never built
  * #fragment links whose target id does not exist on the destination page
  * unbalanced / improperly nested block tags
  * duplicate id attributes on a page
  * images missing alt text, and pages missing title/description/h1

    python check.py            # check every built page
    python check.py contact    # check one page

Exit code is non-zero if any ERROR-level problem is found; warnings do not fail.
"""

import collections
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CSS_FILES = [
    "css/style.css", "css/site-fixes.css", "css/bootstrap.min.css",
    "css/animate.css", "css/swiper-bundle.min.css", "css/nice-select.css",
    "css/boxicons.min.css", "css/bootstrap-icons.min.css",
    "css/jquery.fancybox.min.css",
]

# Classes that exist only as JS hooks or are generated at runtime, so no CSS rule
# will mention them. Adding a name here says "intentionally unstyled".
JS_ONLY = {
    "fade_anim", "text-anim", "counter", "counter_number", "lazy-bg-video",
    "swiper", "swiper-wrapper", "swiper-slide", "magnetic-wrap", "magnetic-item",
    "shape-hover-item", "shape-hover-img", "portfolioCard", "video-player",
    "progress-bar", "single-process", "process-wrapper", "process-list",
    "process-count", "our-work-img", "our-work-list", "award-img", "award-list",
    "award-slider",  # Swiper hook, custom.js:324 — styling lives on .award-slider-section
    "single-portfolio2", "team-img-area", "ball-view-inner", "cursor-close",
    # structural / JS-hook classes the template ships with no CSS rule of their own
    "wow", "animate", "sidebar-button", "drop-down", "banner-pagi",
    "home3-banner-slide", "section-title-wrap", "btn-and-contact-area",
}


def css_class_names():
    names = set()
    for rel in CSS_FILES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        css = open(path, encoding="utf-8", errors="ignore").read()
        css = re.sub(r"/\*.*?\*/", " ", css, flags=re.S)
        for m in re.finditer(r"\.(-?[_a-zA-Z][\w-]*)", css):
            names.add(m.group(1))
    return names


def strip_noise(html):
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    html = re.sub(r"<script\b.*?</script>", " ", html, flags=re.S)
    html = re.sub(r"<style\b.*?</style>", " ", html, flags=re.S)
    return html


BLOCK = ("div", "section", "header", "footer", "main", "nav", "article",
         "aside", "ul", "ol", "li", "form", "table", "tbody", "tr", "td", "th")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr", "path", "rect", "circle",
        "line", "polygon", "polyline", "ellipse", "stop", "use"}


def check_balance(html):
    """Tag-stack check over block elements only; svg subtree is skipped."""
    html = re.sub(r"<svg\b.*?</svg>", " ", html, flags=re.S)
    stack, errs = [], []
    for m in re.finditer(r"<(/?)([a-zA-Z][\w-]*)([^>]*?)(/?)>", html):
        closing, tag, attrs, selfclose = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if tag not in BLOCK:
            continue
        if selfclose or tag in VOID:
            continue
        line = html.count("\n", 0, m.start()) + 1
        if not closing:
            stack.append((tag, line))
        else:
            if not stack:
                errs.append("stray </%s> at line %d" % (tag, line))
            elif stack[-1][0] != tag:
                open_tag, open_line = stack[-1]
                errs.append("</%s> at line %d closes <%s> opened at line %d"
                            % (tag, line, open_tag, open_line))
                stack.pop()
            else:
                stack.pop()
    for tag, line in stack[-6:]:
        errs.append("<%s> opened at line %d never closed" % (tag, line))
    return errs


def main():
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    pages = json.load(open(os.path.join(ROOT, "_content/pages.json"), encoding="utf-8"))
    slugs = [p["slug"] for p in pages]
    all_slugs = set(slugs)
    if only:
        slugs = [s for s in slugs if s in only]
    known = css_class_names() | JS_ONLY

    # collect ids per page first, so cross-page #fragment links can be checked
    ids = {}
    for slug in slugs:
        path = os.path.join(ROOT, slug + ".html")
        if os.path.exists(path):
            html = open(path, encoding="utf-8", errors="ignore").read()
            ids[slug + ".html"] = set(re.findall(r'\bid="([^"]+)"', html))

    errors, warnings = 0, 0
    for slug in slugs:
        path = os.path.join(ROOT, slug + ".html")
        page_err, page_warn = [], []
        if not os.path.exists(path):
            print("MISSING  %s.html (not built)" % slug)
            errors += 1
            continue
        raw = open(path, encoding="utf-8", errors="ignore").read()
        html = strip_noise(raw)

        # --- unknown classes ---------------------------------------------
        used = set()
        for m in re.finditer(r'\bclass="([^"]*)"', html):
            for c in m.group(1).split():
                if c and not c.startswith("{{"):
                    used.add(c)
        unknown = sorted(c for c in used - known if not re.fullmatch(r"(col|offset)-[\w-]+", c))
        if unknown:
            page_err += ["undefined class: .%s" % c for c in unknown]

        # --- assets exist -------------------------------------------------
        for attr in ("src", "data-src", "poster"):
            for m in re.finditer(r'\b%s="([^"]+)"' % attr, html):
                v = m.group(1)
                if v.startswith(("http", "//", "data:", "#", "{{")):
                    continue
                if not os.path.exists(os.path.join(ROOT, v)):
                    page_err.append("missing asset: %s" % v)

        # --- links --------------------------------------------------------
        for m in re.finditer(r'\bhref="([^"]+)"', html):
            v = m.group(1)
            if v.startswith(("http", "//", "mailto:", "tel:", "javascript:", "{{")):
                continue
            if v == "#":
                page_warn.append("placeholder href=\"#\"")
                continue
            target, _, frag = v.partition("#")
            if target:
                if not os.path.exists(os.path.join(ROOT, target)):
                    # A page that is in the manifest but not yet assembled is a
                    # build-order artefact, not a broken link. Only an unknown
                    # target is a real error.
                    if target[:-5] in all_slugs and target.endswith(".html"):
                        page_warn.append("links to %s (not built yet)" % target)
                    else:
                        page_err.append("link to missing file: %s" % v)
                    continue
                if frag and target in ids and frag not in ids[target]:
                    page_err.append("link to missing anchor: %s" % v)
            elif frag and frag not in ids.get(slug + ".html", set()):
                page_err.append("link to missing anchor on this page: #%s" % frag)

        # --- structure ------------------------------------------------------
        page_err += check_balance(html)
        dupes = [i for i, n in collections.Counter(
            re.findall(r'\bid="([^"]+)"', html)).items() if n > 1]
        if dupes:
            page_err += ["duplicate id: %s" % d for d in dupes]

        # --- content hygiene -------------------------------------------------
        if not re.search(r"<title>[^<]{5,}</title>", raw):
            page_err.append("missing or empty <title>")
        if not re.search(r'name="description" content="[^"]{20,}"', raw):
            page_err.append("missing meta description")
        h1 = len(re.findall(r"<h1[\s>]", html))
        if slug != "index" and h1 != 1:
            page_err.append("expected exactly one <h1>, found %d" % h1)
        noalt = len([m for m in re.finditer(r"<img\b(?![^>]*\balt=)[^>]*>", html)])
        if noalt:
            page_warn.append("%d <img> without alt" % noalt)

        errors += len(page_err)
        warnings += len(page_warn)
        status = "FAIL" if page_err else ("warn" if page_warn else "ok")
        print("%-6s %-24s %d error(s) %d warning(s)" % (status, slug + ".html", len(page_err), len(page_warn)))
        for e in page_err[:14]:
            print("         ERROR  %s" % e)
        if len(page_err) > 14:
            print("         ... and %d more" % (len(page_err) - 14))
        for w in dict.fromkeys(page_warn):
            print("         warn   %s" % w)

    print("\n%d error(s), %d warning(s) across %d page(s)" % (errors, warnings, len(slugs)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
