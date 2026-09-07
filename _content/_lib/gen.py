#!/usr/bin/env python3
"""Component library for generating First Perfumes page fragments.

Every function returns markup built from classes that already exist in
css/style.css. The icon SVGs are lifted verbatim from the verified
fragrance-development page so buttons animate exactly as they do elsewhere.

Fragments are written at 16-space base indentation to match _content/index.html.
"""

import json
import os
import re

LIB = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.dirname(LIB)
ROOT = os.path.dirname(CONTENT)
ICONS = json.load(open(os.path.join(LIB, "icons.json"), encoding="utf-8"))

# The 20x20 arrow that lives inside .primary-btn1 spans.
ARROW20 = re.search(r"(<svg\s+width=\"20\".*?</svg>)", ICONS["btn1span"], re.S).group(1)
ARROW20 = re.sub(r"\s+", " ", ARROW20)
ARROW10 = re.sub(r"\s+", " ", ICONS["arrow10"])
BORDER = re.sub(r"\s+", " ", ICONS["borderline"])
WHYICON = re.sub(r"\s+", " ", ICONS["whyicon"])
VECTOR = re.sub(r"\s+", " ", ICONS["vector"])

I = " " * 16  # base indent


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def ind(block, level):
    """Indent every non-empty line of block by level*4 spaces past the base."""
    pad = I + "    " * level
    return "\n".join((pad + ln) if ln.strip() else "" for ln in block.split("\n"))


# --------------------------------------------------------------------------
# buttons
# --------------------------------------------------------------------------

def btn1(text, href):
    """.primary-btn1 — needs exactly two identical <span> children."""
    span = "<span>%s %s</span>" % (esc(text), ARROW20)
    return '<a class="primary-btn1" href="%s">%s%s</a>' % (href, span, span)


def btn1_submit(text):
    span = "<span>%s %s</span>" % (esc(text), ARROW20)
    return '<button type="submit" class="primary-btn1">%s%s</button>' % (span, span)


def btn2(text, href):
    """.primary-btn2.transparent — .icon + .content + .icon.two."""
    return (
        '<a class="primary-btn2 transparent" href="%s">'
        '<span class="icon">%s</span>'
        '<span class="content">%s</span>'
        '<span class="icon two">%s</span></a>'
    ) % (href, ARROW10, esc(text), ARROW10)


def viewmore(text, href):
    return '<a href="%s" class="view-more-btn style-2">%s %s</a>' % (href, BORDER, esc(text))


# --------------------------------------------------------------------------
# section scaffolding
# --------------------------------------------------------------------------

def title_row(eyebrow, heading, right_href=None, right_text="View All"):
    right = ""
    if right_href:
        right = """
        <div class="col-lg-5">
            <div class="right-content">
                %s
            </div>
        </div>""" % viewmore(right_text, right_href)
    return """    <div class="row gy-3 mb-60 justify-content-between">
        <div class="col-lg-7">
            <div class="section-title home3-section-title three">
                <span>%s</span>
                <h2 class="text-anim">%s</h2>
            </div>
        </div>%s
    </div>""" % (esc(eyebrow), esc(heading), right)


def section(cls, inner, comment, anchor=None, spacing="mb-120"):
    aid = ' id="%s"' % anchor if anchor else ""
    return """%s<!-- %s Start -->
%s<div class="%s %s"%s>
%s    <div class="container">
%s
%s    </div>
%s</div>
%s<!-- %s End -->
""" % (I, comment, I, cls, spacing, aid, I, ind(inner, 2), I, I, I, comment)


# --------------------------------------------------------------------------
# content blocks
# --------------------------------------------------------------------------

def hero_split(img, alt, heading, paras, eager=False):
    """service-details-page: image left, heading + paragraphs right."""
    load = ('fetchpriority="high" decoding="async"' if eager
            else 'loading="lazy" decoding="async"')
    body = "\n".join(
        '        <div class="details-content%s">\n            <p>%s</p>\n        </div>'
        % (" mb-30" if i < len(paras) - 1 else "", p) for i, p in enumerate(paras))
    return """<div class="row gy-5 align-items-center">
    <div class="col-lg-6 fade_anim" data-fade-from="left" data-delay=".2">
        <div class="service-details-thumb-img">
            <img src="%s" alt="%s" %s>
        </div>
    </div>
    <div class="col-lg-6 fade_anim" data-fade-from="right" data-delay=".3">
        <div class="service-details-content-wrap">
            <div class="service-details-title mb-30">
                <h2 class="text-anim">%s</h2>
            </div>
%s
        </div>
    </div>
</div>""" % (img, esc(alt), load, esc(heading), body)


def two_lists(heading, left_h3, left_items, right_h3, right_items):
    def ul(items):
        return "\n".join("                <li>%s</li>" % x for x in items)
    return """<div class="service-details-content-wrap">
    <div class="row">
        <div class="col-lg-12">
            <div class="service-details-title mb-60 fade_anim" data-delay=".2">
                <h2 class="text-anim">%s</h2>
            </div>
        </div>
    </div>
    <div class="row gy-5">
        <div class="col-lg-6 fade_anim" data-delay=".2">
            <div class="details-content">
                <h3>%s</h3>
                <ul class="approach-list">
%s
                </ul>
            </div>
        </div>
        <div class="col-lg-6 fade_anim" data-delay=".3">
            <div class="details-content">
                <h3>%s</h3>
                <ul class="approach-list">
%s
                </ul>
            </div>
        </div>
    </div>
</div>""" % (esc(heading), esc(left_h3), ul(left_items), esc(right_h3), ul(right_items))


def img_text(img, alt, h3, paras, flip=False):
    """Alternating image / copy row inside a details wrapper."""
    imgcol = """    <div class="col-lg-6 fade_anim" data-fade-from="%s" data-delay=".2">
        <div class="service-details-img">
            <img src="%s" alt="%s" loading="lazy" decoding="async">
        </div>
    </div>""" % ("right" if flip else "left", img, esc(alt))
    # .details-content is only styled inside .service-details-content-wrap or
    # .industries-details-content-wrap — without one, the copy falls back to
    # browser defaults. Keep the full ancestor chain.
    txtcol = """    <div class="col-lg-6 fade_anim" data-fade-from="%s" data-delay=".3">
        <div class="service-details-content-wrap">
            <div class="details-content">
                <h3>%s</h3>
%s
            </div>
        </div>
    </div>""" % ("left" if flip else "right", esc(h3),
                 "\n".join("                <p>%s</p>" % p for p in paras))
    inner = (txtcol + "\n" + imgcol) if flip else (imgcol + "\n" + txtcol)
    return '<div class="row gy-5 align-items-center">\n%s\n</div>' % inner


def key_features(items):
    ordinals = ["", "two", "three", "four"]
    lis = "\n".join(
        '            <li%s>%s</li>' % ((' class="%s"' % ordinals[i]) if i else "", esc(x))
        for i, x in enumerate(items[:4]))
    return """<div class="row">
    <div class="col-lg-12">
        <div class="key-features-area fade_anim" data-delay=".2">
            <ul class="key-features-list">
%s
            </ul>
        </div>
    </div>
</div>""" % lis


def why_choose(pairs):
    """pairs: list of (bold_lead, rest). Split evenly across two columns."""
    def col(items, delay):
        lis = "\n".join("""                    <li>
                        <div class="icon">%s</div>
                        <div class="content">
                            <p><span>%s</span> %s</p>
                        </div>
                    </li>""" % (WHYICON, esc(a), b) for a, b in items)
        return """    <div class="col-lg-6 fade_anim" data-delay="%s">
        <div class="why-choose-area">
            <ul class="why-choose-list">
%s
            </ul>
        </div>
    </div>""" % (delay, lis)
    half = (len(pairs) + 1) // 2
    return """<div class="why-choose-area-wrap">
    <div class="row gy-4">
%s
%s
    </div>
</div>""" % (col(pairs[:half], ".2"), col(pairs[half:], ".3"))


def accordion(dom_id, items, prefix=None):
    """Bootstrap 5 accordion. First item open; every other button .collapsed."""
    prefix = prefix or dom_id
    out = []
    for n, (q, a) in enumerate(items):
        first = n == 0
        hid = "%sHeading%d" % (prefix, n)
        cid = "%sCollapse%d" % (prefix, n)
        out.append("""            <div class="accordion-item">
                <h2 class="accordion-header" id="%s">
                    <button class="accordion-button%s" type="button" data-bs-toggle="collapse" data-bs-target="#%s" aria-expanded="%s" aria-controls="%s">%s</button>
                </h2>
                <div id="%s" class="accordion-collapse collapse%s" aria-labelledby="%s" data-bs-parent="#%s">
                    <div class="accordion-body">%s</div>
                </div>
            </div>""" % (hid, "" if first else " collapsed", cid,
                         "true" if first else "false", cid, esc(q),
                         cid, " show" if first else "", hid, dom_id, a))
    return """<div class="row">
    <div class="col-lg-12 fade_anim" data-delay=".2">
        <div class="faq-wrap style-2">
            <div class="accordion" id="%s">
%s
            </div>
        </div>
    </div>
</div>""" % (dom_id, "\n".join(out))


def industries_block(heading, intro, h3, items, outro, img, alt, tags):
    lis = "\n".join("                    <li>%s</li>" % x for x in items)
    taglis = "\n".join('                <li><a href="%s">%s</a></li>' % (h, esc(t))
                       for t, h in tags)
    return """<div class="industries-details-content-wrap">
    <div class="row">
        <div class="col-lg-12">
            <div class="industries-details-title mb-60 fade_anim" data-delay=".2">
                <h2 class="text-anim">%s</h2>
            </div>
        </div>
    </div>
    <div class="row gy-5 align-items-center mb-60">
        <div class="col-lg-7 fade_anim" data-delay=".3">
            <div class="details-content">
                <p>%s</p>
                <h3>%s</h3>
                <ul>
%s
                </ul>
                <p>%s</p>
            </div>
        </div>
        <div class="col-lg-5 fade_anim" data-fade-from="right" data-delay=".4">
            <div class="industries-details-img">
                <img src="%s" alt="%s" loading="lazy" decoding="async">
            </div>
        </div>
    </div>
    <div class="tag-navigation-area">
        <ul class="tag-list">
%s
        </ul>
    </div>
</div>""" % (esc(heading), intro, esc(h3), lis, outro, img, esc(alt), taglis)


CERTS = [
    ("images/fda.webp", "US FDA registered manufacturing facility", "manufacturing.html"),
    ("images/iso.webp", "ISO 22716:2007 Cosmetics GMP certified", "manufacturing.html"),
    ("images/cpnp.webp", "EU CPNP cosmetic product notification compliant", "faq.html"),
    ("images/cgmp.webp", "cGMP compliant production standards", "manufacturing.html"),
    ("images/scpn.webp", "UK SCPN cosmetic product notification compliant", "faq.html"),
]


def partner_strip(pre, emphasis, post):
    def group(hidden=False):
        rows = "\n".join(
            '                <a href="%s"><img src="%s" alt="%s" loading="lazy" decoding="async"></a>'
            % (h, s, esc(a)) for s, a, h in CERTS)
        return '            <div class="marquee__group"%s>\n%s\n            </div>' % (
            ' aria-hidden="true"' if hidden else "", rows)
    return """%s<!-- Compliance strip Start -->
%s<div class="partner-section mb-120">
%s    <div class="container">
%s        <div class="partner-title">
%s            <h5>%s <span>%s</span> %s</h5>
%s        </div>
%s    </div>
%s    <div class="partner-wrap">
%s        <div class="marquee">
%s
%s
%s        </div>
%s    </div>
%s</div>
%s<!-- Compliance strip End -->
""" % (I, I, I, I, I, esc(pre), esc(emphasis), esc(post), I, I, I, I,
       ind(group(), 2), ind(group(True), 2), I, I, I, I)


def service_grid(eyebrow, heading, right_href, cards, comment="Related expertise"):
    """cards: list of (title, blurb, href)."""
    out = []
    for n, (t, b, h) in enumerate(cards):
        out.append("""    <div class="col-lg-4 col-md-6 fade_anim" data-delay=".%d" data-duration="2" data-ease="bounce">
        <div class="home3-service-card">
            <h3><a href="%s">%s</a></h3>
            <p>%s</p>
            %s
            <div class="vector-icon">%s</div>
        </div>
    </div>""" % (2 + (n % 3), h, esc(t), b, btn2("View Details", h), VECTOR))
    inner = "%s\n<div class=\"row gy-4\">\n%s\n</div>" % (
        title_row(eyebrow, heading, right_href), "\n".join(out))
    return section("home3-service-section", inner, comment)


def cta(heading, btn_text="Talk to Our Team", href="contact.html",
        comment="Page CTA"):
    inner = """<div class="row">
    <div class="col-lg-12">
        <div class="portfolio-details-banner text-center fade_anim" data-delay=".2">
            <h3>%s</h3>
            %s
        </div>
    </div>
</div>""" % (esc(heading), btn1(btn_text, href))
    return section("portfolio-details-page", inner, comment)


def team_grid(members):
    """members: list of (img, name, role, alt)."""
    out = []
    for n, (img, name, role, alt) in enumerate(members):
        out.append("""    <div class="col-lg-3 col-md-6 fade_anim" data-delay=".%d">
        <div class="team-card">
            <div class="team-img">
                <img src="%s" alt="%s" loading="lazy" decoding="async">
                <div class="social-area">
                    <ul class="social-list">
                        <li><a href="https://www.linkedin.com/" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a></li>
                        <li><a href="https://www.instagram.com/" aria-label="Instagram"><i class="bi bi-instagram"></i></a></li>
                    </ul>
                </div>
            </div>
            <div class="team-content">
                <h5><a href="contact.html">%s</a></h5>
                <span>%s</span>
            </div>
        </div>
    </div>""" % (2 + (n % 4), img, esc(alt), esc(name), esc(role)))
    return '<div class="row gy-4">\n%s\n</div>' % "\n".join(out)


def job_table(rows):
    """rows: list of (position, vacancies, jobtype)."""
    circle = '<a href="contact.html" class="circle-btn" aria-label="Apply">%s</a>' % ARROW20
    body = "\n".join("""                <tr>
                    <td class="position-name" data-label="Position">%s</td>
                    <td class="vacancies" data-label="Vacancies">%s</td>
                    <td class="job-type" data-label="Job Type">%s</td>
                    <td class="arrow-icon" data-label="Apply">%s</td>
                </tr>""" % (esc(p), esc(v), esc(t), circle) for p, v, t in rows)
    return """<div class="table-container fade_anim" data-delay=".2">
    <table>
        <thead>
            <tr>
                <th>Position</th>
                <th>Vacancies</th>
                <th>Job Type</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
%s
        </tbody>
    </table>
</div>""" % body


def longform(blocks):
    """blocks: list of (h3_or_None, [paragraph_or_ul, ...]) for policy pages."""
    out = []
    for h3, parts in blocks:
        chunk = []
        if h3:
            chunk.append("            <h3>%s</h3>" % esc(h3))
        for p in parts:
            if isinstance(p, list):
                chunk.append("            <ul class=\"approach-list\">")
                chunk += ["                <li>%s</li>" % x for x in p]
                chunk.append("            </ul>")
            else:
                chunk.append("            <p>%s</p>" % p)
        out.append("\n".join(chunk))
    return """<div class="row">
    <div class="col-lg-10 fade_anim" data-delay=".2">
        <div class="details-content">
%s
        </div>
    </div>
</div>""" % "\n".join(out)


def write(slug, parts):
    """Join section blocks and write the fragment."""
    body = "\n".join(parts).rstrip("\n") + "\n"
    path = os.path.join(CONTENT, slug + ".html")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    return len(body.split("\n"))
