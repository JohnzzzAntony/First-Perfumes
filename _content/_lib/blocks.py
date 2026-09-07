#!/usr/bin/env python3
"""Reusable section builders for page fragments in `_content/`.

The first pass of this site generated the product and expertise sub-pages from a
single skeleton, so eight pages ended up with an identical section spine. These
builders exist so each page can be given its *own* structure while still being
assembled from components that already exist in `css/style.css` — no invented
class names, which `check.py` would reject.

Every function returns a fragment indented to the 16-space base that `build.py`
expects. Import from a one-off script; nothing here runs at build time.
"""

import html
import re

IND = " " * 16


def esc(s):
    return html.escape(str(s), quote=False)


def _ind(block, level=0):
    """Re-indent a triple-quoted block to the fragment base indentation."""
    lines = block.strip("\n").split("\n")
    pad = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    out = []
    for l in lines:
        out.append((IND + " " * (4 * level) + l[pad:]).rstrip() if l.strip() else "")
    return "\n".join(out)


# --- shared inline SVGs, copied verbatim from _content/index.html ------------

ARROW_BTN = (
    '<svg width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"> <g> '
    '<path d="M6.36416 4.94971C6.37964 5.45636 8.04642 6.14449 8.42737 6.15336L12.6752 6.15336L4.95937 '
    "13.8691C4.68614 14.1424 4.68613 14.5854 4.95937 14.8586C5.23261 15.1319 5.67561 15.1319 5.94884 "
    "14.8586L13.6646 7.14283L13.6646 11.3906C13.6647 11.777 14.4631 13.4349 14.8494 13.435C15.2358 "
    "13.4349 15.0638 11.777 15.0638 11.3906L15.0638 5.45375C15.0637 5.06741 14.7506 4.75424 14.3642 "
    '4.75416L8.42738 4.75416C8.0235 4.75908 6.35447 4.48628 6.36416 4.94971Z" /> </g> </svg>'
)

VIEW_MORE_RULE = (
    '<svg class="border" width="88" height="1" viewBox="0 0 88 1" '
    'xmlns="http://www.w3.org/2000/svg"><rect width="88" height="1" /></svg>'
)

DETAIL_ARROW = (
    '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" '
    'xmlns="http://www.w3.org/2000/svg"><path d="M4.5 15.5L15.5 4.5M15.5 4.5H6.5M15.5 4.5V13.5" '
    'stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

PROCESS_VECTOR = (
    '<svg class="vector" width="75" height="75" viewBox="0 0 75 75" fill="none" '
    'xmlns="http://www.w3.org/2000/svg"><rect width="25" height="25" fill="#df2341" />'
    '<rect x="25" y="25" width="25" height="25" fill="#df2341" />'
    '<rect y="50" width="25" height="25" fill="#df2341" />'
    '<rect x="50" y="50" width="25" height="25" fill="#df2341" /></svg>'
)


ARROW10 = (
    '<svg width="10" height="10" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M1 9L9 1M9 1C7.22222 1.33333 3.33333 2 1 1M9 1C8.66667 2.66667 8 6.33333 9 9" '
    'stroke-width="1.5" stroke-linecap="round"></path></svg>'
)

# The plain `<g>` variant of the card icon. The homepage's copy wraps it in a
# <mask> with a document-unique id; this one has no ids, so it is safe to repeat.
CARD_VECTOR = (
    '<svg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"><g>'
    '<path d="M21.3331 29.9998C21.3331 25.2212 25.2209 21.3331 29.9998 21.3331C34.7788 21.3331 '
    "38.6666 25.2209 38.6666 29.9998C38.6666 34.7787 34.7784 38.6666 29.9998 38.6666V56C44.3592 "
    "56 56 44.3595 56 29.9998C56 15.6405 44.3595 4 29.9998 4C15.6405 4 4 15.6405 4 29.9998H21.3331Z"
    '"></path></g></svg>'
)


def primary_btn2(label, href):
    return (
        '<a class="primary-btn2 transparent" href="%s">'
        '<span class="icon">%s</span>'
        '<span class="content">%s</span>'
        '<span class="icon two">%s</span></a>' % (href, ARROW10, esc(label), ARROW10)
    )


def primary_btn1(label, href, extra=""):
    """`.primary-btn1` duplicates its label — the second span is the hover swap."""
    inner = "<span>%s %s</span><span>%s %s</span>" % (esc(label), ARROW_BTN, esc(label), ARROW_BTN)
    cls = ("primary-btn1 " + extra).strip()
    return '<a class="%s" href="%s">%s</a>' % (cls, href, inner)


# --- section builders -------------------------------------------------------


def cta_banner(heading, label, href="contact.html"):
    return _ind(
        """
<div class="portfolio-details-page mb-120">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="portfolio-details-banner text-center fade_anim" data-delay=".2">
                    <h3>%s</h3>
                    %s
                </div>
            </div>
        </div>
    </div>
</div>
"""
        % (esc(heading), primary_btn1(label, href))
    )


def compliance_marquee(title_html):
    logos = [
        ("fda.webp", "US FDA registered manufacturing facility", "manufacturing.html"),
        ("iso.webp", "ISO 22716:2007 Cosmetics GMP certified", "manufacturing.html"),
        ("cpnp.webp", "EU CPNP cosmetic product notification compliant", "faq.html"),
        ("cgmp.webp", "cGMP compliant production standards", "manufacturing.html"),
        ("scpn.webp", "UK SCPN cosmetic product notification compliant", "faq.html"),
    ]

    def group(hidden):
        rows = "\n".join(
            '            <a href="%s"><img src="images/%s" alt="%s" loading="lazy" decoding="async"></a>'
            % (href, f, alt)
            for f, alt, href in logos
        )
        attr = ' aria-hidden="true"' if hidden else ""
        return '        <div class="marquee__group"%s>\n%s\n        </div>' % (attr, rows)

    return _ind(
        """
<div class="partner-section mb-120">
    <div class="container">
        <div class="partner-title">
            <h5>%s</h5>
        </div>
    </div>
    <div class="partner-wrap">
        <div class="marquee">
%s
%s
        </div>
    </div>
</div>
"""
        % (title_html, group(False), group(True))
    )


def key_features(items):
    variants = ["", "two", "three", "four"]
    lis = "\n".join(
        '                    <li%s>%s</li>'
        % ((' class="%s"' % variants[i % 4]) if variants[i % 4] else "", esc(t))
        for i, t in enumerate(items)
    )
    return _ind(
        """
<div class="service-details-page mb-120">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="key-features-area fade_anim" data-delay=".2">
                    <ul class="key-features-list">
%s
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
"""
        % lis
    )


def process_section(eyebrow, heading, intro, cta_label, cta_href, steps, uid):
    """`home4-process-section` — dark panel, four numbered cards with SVG connectors.

    Four cards is the only count the CSS defines (`.single-process` + `.two`/`.three`/`.four`).
    Every SVG id must be unique within the page, hence `uid`.
    """
    assert len(steps) == 4, "home4-process-section is designed for exactly four steps"

    def connector(n, reverse=False):
        pid = "theMotionPath%s%d" % (uid, n)
        gid = "paint_%s_%d" % (uid, n)
        keys = ' keyPoints="1;0" keyTimes="0;1"' if reverse else ""
        return (
            '                <svg class="animated-vector" width="65" height="100" viewBox="0 0 181 124" '
            'fill="none" xmlns="http://www.w3.org/2000/svg">\n'
            '                    <path opacity="0.2" id="%s" d="M0 123H67.5C84.0685 123 97.5 109.569 '
            '97.5 93V31C97.5 14.4315 110.931 1 127.5 1H181" stroke="black" />\n'
            '                    <path d="M0 0 L13 0" stroke="url(#%s)" stroke-linecap="round" '
            'stroke-width="20">\n'
            '                        <animateMotion dur="4s" begin="0s" repeatCount="indefinite" '
            'rotate="auto"%s>\n'
            '                            <mpath href="#%s"></mpath>\n'
            "                        </animateMotion>\n"
            "                    </path>\n"
            "                    <defs>\n"
            '                        <linearGradient id="%s" x1="10" y1="0" x2="0" y2="0" '
            'gradientUnits="userSpaceOnUse">\n'
            '                            <stop stop-color="#CB0000" offset="0" />\n'
            '                            <stop offset="1" stop-color="white" stop-opacity="0" />\n'
            "                        </linearGradient>\n"
            "                    </defs>\n"
            "                </svg>" % (pid, gid, keys, pid, gid)
        )

    layout = [
        ("single-process mt-30", "fadeInLeft", "after", False),
        ("single-process two", "fadeInUp", None, False),
        ("single-process three mt-30", "fadeInRight", "before", True),
        ("single-process four", "fadeInUp", "before", False),
    ]
    cards = []
    for i, ((title, body), (cls, wow, conn, rev)) in enumerate(zip(steps, layout), start=1):
        card = (
            '                <div class="process-card wow animate %s" data-wow-delay="%dms" '
            'data-wow-duration="1500ms">\n'
            '                    <div class="step-no">\n'
            "                        <span>STEP : %02d</span>\n"
            "                    </div>\n"
            "                    <h3>%s</h3>\n"
            "                    <p>%s</p>\n"
            "                    %s\n"
            "                </div>" % (wow, 200 * i, i, esc(title), esc(body), PROCESS_VECTOR)
        )
        parts = [card]
        if conn == "after":
            parts.append(connector(i, rev))
        elif conn == "before":
            parts.insert(0, connector(i, rev))
        cards.append(
            '            <div class="%s">\n%s\n            </div>' % (cls, "\n".join(parts))
        )

    return _ind(
        """
<div class="home4-process-section mb-120">
    <div class="container-fluid two">
        <div class="process-section-wrap">
            <div class="section-title-wrap">
                <div class="container">
                    <div class="row gy-3 mb-60 justify-content-between">
                        <div class="col-lg-7">
                            <div class="section-title home4-section-title three">
                                <span>%s</span>
                                <div class="left-content">
                                    <h2 class="text-anim">%s</h2>
                                    <p class="text-anim">%s</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-5">
                            <div class="right-content">
                                <a href="%s" class="view-more-btn style-2">%s %s</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="process-wrapper">
%s
            </div>
        </div>
    </div>
</div>
"""
        % (
            esc(eyebrow),
            esc(heading),
            esc(intro),
            cta_href,
            VIEW_MORE_RULE,
            esc(cta_label),
            "\n".join(cards),
        )
    )


def award_list(heading, rows, images):
    """`.award-section` — hover-linked list and image pair.

    custom.js matches by index, so the two lists must be the same length and order.
    """
    assert len(rows) == len(images), "award list and image list must be parallel"
    imgs = "\n".join(
        '                        <li%s><div class="single-img"><img src="images/%s" alt="%s" '
        'loading="lazy" decoding="async"></div></li>'
        % (' class="active"' if i == 0 else "", f, esc(alt))
        for i, (f, alt) in enumerate(images)
    )
    lis = "\n".join(
        '                        <li%s>\n'
        '                            <div class="award-history">\n'
        "                                <h3>%s</h3>\n"
        "                                <h3>%s</h3>\n"
        "                            </div>\n"
        "                        </li>" % (' class="active"' if i == 0 else "", esc(a), esc(b))
        for i, (a, b) in enumerate(rows)
    )
    return _ind(
        """
<div class="award-section font-alt mb-120">
    <div class="container">
        <div class="section-title mb-60 fade_anim" data-delay=".2">
            <h2 class="text-anim">%s</h2>
        </div>
        <div class="row gy-4">
            <div class="col-lg-5 fade_anim" data-fade-from="left" data-delay=".2">
                <div class="award-img">
                    <ul>
%s
                    </ul>
                </div>
            </div>
            <div class="col-lg-7 fade_anim" data-fade-from="right" data-delay=".3">
                <div class="award-list">
                    <ul>
%s
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
"""
        % (esc(heading), imgs, lis)
    )


def industries_list(eyebrow, heading, rows):
    """`.industries-section` — big text links with a hover image pair."""
    lis = "\n".join(
        '                        <li>\n'
        '                            <a href="%s">\n'
        "                                <span>%s</span>\n"
        '                                <div class="hover-img">\n'
        '                                    <img class="img1" src="images/%s" alt="%s" loading="lazy" decoding="async">\n'
        '                                    <img class="img2" src="images/%s" alt="" role="presentation" loading="lazy" decoding="async">\n'
        "                                </div>\n"
        "                            </a>\n"
        "                        </li>" % (href, esc(label), a, esc(alt), b)
        for label, href, a, b, alt in rows
    )
    return _ind(
        """
<div class="industries-section mb-120">
    <div class="container">
        <div class="row gy-4">
            <div class="col-lg-4 fade_anim" data-fade-from="left" data-delay=".2">
                <div class="section-title">
                    <span>%s</span>
                    <h2 class="text-anim">%s</h2>
                </div>
            </div>
            <div class="col-lg-8 divider fade_anim" data-fade-from="right" data-delay=".3">
                <ul class="industries-list">
%s
                </ul>
            </div>
        </div>
    </div>
</div>
"""
        % (esc(eyebrow), esc(heading), lis)
    )


def spec_table(heading, intro, headers, rows):
    """`.table-container` — responsive table; every td needs data-label for mobile."""
    ths = "\n".join("                    <th>%s</th>" % esc(h) for h in headers)
    trs = []
    for r in rows:
        tds = "\n".join(
            '                    <td class="%s" data-label="%s">%s</td>'
            % (cls, esc(headers[i]), esc(v))
            for i, (v, cls) in enumerate(r)
        )
        trs.append("                <tr>\n%s\n                </tr>" % tds)
    return _ind(
        """
<div class="careers-details-page mb-120">
    <div class="container">
        <div class="service-details-title mb-30 fade_anim" data-delay=".2">
            <h2 class="text-anim">%s</h2>
        </div>
        <div class="details-content mb-60 fade_anim" data-delay=".3">
            <p>%s</p>
        </div>
        <div class="table-container fade_anim" data-delay=".2">
            <table>
                <thead>
                <tr>
%s
                </tr>
                </thead>
                <tbody>
%s
                </tbody>
            </table>
        </div>
    </div>
</div>
"""
        % (esc(heading), esc(intro), ths, "\n".join(trs))
    )


def faq_accordion(heading, items, uid):
    """`.faq-page` + Bootstrap accordion. ids must be unique within the page."""
    entries = []
    for i, (q, a) in enumerate(items, start=1):
        show = i == 1
        entries.append(
            '                <div class="accordion-item">\n'
            '                    <h2 class="accordion-header" id="%s-h%d">\n'
            '                        <button class="accordion-button%s" type="button" '
            'data-bs-toggle="collapse" data-bs-target="#%s-c%d" aria-expanded="%s" '
            'aria-controls="%s-c%d">%s</button>\n'
            "                    </h2>\n"
            '                    <div id="%s-c%d" class="accordion-collapse collapse%s" '
            'aria-labelledby="%s-h%d" data-bs-parent="#%s">\n'
            '                        <div class="accordion-body">\n'
            "                            <p>%s</p>\n"
            "                        </div>\n"
            "                    </div>\n"
            "                </div>"
            % (
                uid, i,
                "" if show else " collapsed",
                uid, i,
                "true" if show else "false",
                uid, i,
                esc(q),
                uid, i,
                " show" if show else "",
                uid, i, uid,
                esc(a),
            )
        )
    return _ind(
        """
<div class="faq-page mb-120">
    <div class="container">
        <div class="service-details-title mb-60 fade_anim" data-delay=".2">
            <h2 class="text-anim">%s</h2>
        </div>
        <div class="faq-wrap fade_anim" data-delay=".3">
            <div class="accordion" id="%s">
%s
            </div>
        </div>
    </div>
</div>
"""
        % (esc(heading), uid, "\n".join(entries))
    )


def contact_strip(heading, label="Talk to Production", href="contact.html"):
    return _ind(
        """
<div class="pricing-plan-section mb-120">
    <div class="container">
        <div class="contact-area fade_anim" data-delay=".2">
            <h4>%s</h4>
            %s
        </div>
    </div>
</div>
"""
        % (esc(heading), primary_btn1(label, href))
    )


def service_grid(eyebrow, heading, cards, cta=None, anchored=False):
    """`home3-service-section` — 3-across cards.

    `anchored=True` puts each card's id on its **column**, so a nav link like
    `fine-fragrances.html#eau-de-parfum` lands on a block that is always visible
    (unlike a Bootstrap tab pane, which would be display:none until clicked).
    """
    cols = []
    for i, c in enumerate(cards):
        delay = ".%d" % (3 + (i % 3))
        cid = (' id="%s"' % c["id"]) if anchored and c.get("id") else ""
        cols.append(
            '            <div class="col-lg-4 col-md-6 fade_anim"%s data-delay="%s" '
            'data-duration="2" data-ease="bounce">\n'
            '                <div class="home3-service-card">\n'
            '                    <h3><a href="%s">%s</a></h3>\n'
            "                    <p>%s</p>\n"
            "                    %s\n"
            '                    <div class="vector-icon">%s</div>\n'
            "                </div>\n"
            "            </div>"
            % (cid, delay, c["href"], esc(c["title"]), esc(c["body"]),
               primary_btn2(c.get("cta", "View Details"), c["href"]), CARD_VECTOR)
        )

    right = ""
    if cta:
        right = (
            '            <div class="col-lg-5">\n'
            '                <div class="right-content">\n'
            '                    <a href="%s" class="view-more-btn style-2">%s %s</a>\n'
            "                </div>\n"
            "            </div>" % (cta[1], VIEW_MORE_RULE, esc(cta[0]))
        )

    return _ind(
        """
<div class="home3-service-section mb-120">
    <div class="container">
        <div class="row gy-3 mb-60 justify-content-between">
            <div class="col-lg-7">
                <div class="section-title home3-section-title three">
                    <span>%s</span>
                    <h2 class="text-anim">%s</h2>
                </div>
            </div>
%s
        </div>
        <div class="row gy-4">
%s
        </div>
    </div>
</div>
"""
        % (esc(eyebrow), esc(heading), right, "\n".join(cols))
    )


def pricing_tiers(heading, intro, tiers, footnote=None):
    """`.pricing-plan-section` + `.pricing-card`.

    No monthly/yearly toggle here — these are programme tiers, not subscriptions,
    so `.pricing-plan-tab-area` is deliberately left out and the cards sit directly
    in a row. `.pricing-card.two` / `.three` are the background variants.
    """
    tick = (
        '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" '
        'xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M3.5 8.5L6.5 11.5L12.5 5.5" '
        'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    )
    variants = ["", " two", " three"]
    cols = []
    for i, t in enumerate(tiers):
        lis = "\n".join(
            '                                <li%s>%s %s</li>'
            % ("" if inc else ' class="close"', tick, esc(txt))
            for txt, inc in t["features"]
        )
        cols.append(
            '            <div class="col-lg-4 col-md-6 fade_anim"%s data-delay=".%d">\n'
            '                <div class="pricing-card%s">\n'
            '                    <div class="pricing-top">\n'
            "                        <span>%s</span>\n"
            "                        <h2>%s</h2>\n"
            "                        <p>%s</p>\n"
            '                        <a href="%s" class="pricing-btn"><span>%s</span></a>\n'
            "                    </div>\n"
            '                    <div class="pricing-content">\n'
            "                        <h3>What is included</h3>\n"
            "                        <ul>\n%s\n                        </ul>\n"
            "                    </div>\n"
            '                    <div class="pay-btn-area">%s</div>\n'
            "                </div>\n"
            "            </div>"
            % (
                (' id="%s"' % t["id"]) if t.get("id") else "",
                2 + i,
                variants[i % 3],
                esc(t["name"]),
                esc(t["headline"]),
                esc(t["note"]),
                t.get("href", "contact.html"),
                esc(t.get("btn", "Enquire")),
                lis,
                primary_btn1(t.get("cta", "Start a Brief"), t.get("href", "contact.html")),
            )
        )

    foot = ""
    if footnote:
        foot = (
            '        <div class="contact-area fade_anim" data-delay=".2">\n'
            "            <h4>%s</h4>\n            %s\n        </div>"
            % (esc(footnote[0]), primary_btn1(footnote[1], footnote[2]))
        )

    return _ind(
        """
<div class="pricing-plan-section mb-120">
    <div class="container">
        <div class="service-details-title mb-30 fade_anim" data-delay=".2">
            <h2 class="text-anim">%s</h2>
        </div>
        <div class="details-content mb-60 fade_anim" data-delay=".3">
            <p>%s</p>
        </div>
        <div class="row gy-4 mb-60">
%s
        </div>
%s
    </div>
</div>
"""
        % (esc(heading), esc(intro), "\n".join(cols), foot)
    )


def split(section_cls, anchor, heading, paras, image, alt, img_left=True,
          heading_level="h3", img_cls=None, bullets=None, bullet_heading=None):
    """Two-column image + copy block. `section_cls` picks the visual family:
    `service-details-page` (tighter) vs `industries-details-page` (framed image)."""
    img_cls = img_cls or (
        "service-details-img" if section_cls == "service-details-page" else "industries-details-img"
    )
    body = "\n".join("                        <p>%s</p>" % esc(p) for p in paras)
    if bullets:
        if bullet_heading:
            body += "\n                        <h4>%s</h4>" % esc(bullet_heading)
        body += (
            '\n                        <ul class="approach-list">\n'
            + "\n".join("                            <li>%s</li>" % esc(b) for b in bullets)
            + "\n                        </ul>"
        )

    img_col = (
        '            <div class="col-lg-6 fade_anim" data-fade-from="%s" data-delay=".2">\n'
        '                <div class="%s">\n'
        '                    <img src="images/%s" alt="%s" loading="lazy" decoding="async">\n'
        "                </div>\n"
        "            </div>" % ("left" if img_left else "right", img_cls, image, esc(alt))
    )
    txt_col = (
        '            <div class="col-lg-6 fade_anim" data-fade-from="%s" data-delay=".3">\n'
        '                <div class="details-content">\n'
        "                    <%s>%s</%s>\n%s\n"
        "                </div>\n"
        "            </div>"
        % ("right" if img_left else "left", heading_level, esc(heading), heading_level, body)
    )
    cols = (img_col, txt_col) if img_left else (txt_col, img_col)
    aid = (' id="%s"' % anchor) if anchor else ""
    return _ind(
        """
<div class="%s mb-120"%s>
    <div class="container">
        <div class="row gy-5 align-items-center">
%s
%s
        </div>
    </div>
</div>
"""
        % (section_cls, aid, cols[0], cols[1])
    )


def intro_split(heading, paras, image, alt, img_left=True):
    """Page-opening statement block — the hero image gets fetchpriority, not lazy."""
    img = (
        '            <div class="col-lg-6 fade_anim" data-fade-from="%s" data-delay=".2">\n'
        '                <div class="service-details-thumb-img">\n'
        '                    <img src="images/%s" alt="%s" fetchpriority="high" decoding="async">\n'
        "                </div>\n"
        "            </div>" % ("left" if img_left else "right", image, esc(alt))
    )
    body = "\n".join(
        '                    <div class="details-content mb-30">\n'
        "                        <p>%s</p>\n"
        "                    </div>" % esc(p)
        for p in paras
    )
    txt = (
        '            <div class="col-lg-6 fade_anim" data-fade-from="%s" data-delay=".3">\n'
        '                <div class="service-details-content-wrap">\n'
        '                    <div class="service-details-title mb-30">\n'
        '                        <h2 class="text-anim">%s</h2>\n'
        "                    </div>\n%s\n"
        "                </div>\n"
        "            </div>" % ("right" if img_left else "left", esc(heading), body)
    )
    cols = (img, txt) if img_left else (txt, img)
    return _ind(
        """
<div class="service-details-page mb-120">
    <div class="container">
        <div class="row gy-5 align-items-center">
%s
%s
        </div>
    </div>
</div>
"""
        % cols
    )


def two_col_lists(heading, columns, wrapper="industries-details-page"):
    """One title over two `approach-list` columns."""
    title_cls = (
        "industries-details-title"
        if wrapper == "industries-details-page"
        else "service-details-title"
    )
    wrap_cls = (
        "industries-details-content-wrap"
        if wrapper == "industries-details-page"
        else "service-details-content-wrap"
    )
    cols = "\n".join(
        '                <div class="col-lg-6 fade_anim" data-delay=".%d">\n'
        '                    <div class="details-content">\n'
        "                        <h3>%s</h3>\n"
        '                        <ul class="approach-list">\n%s\n                        </ul>\n'
        "                    </div>\n"
        "                </div>"
        % (
            2 + i,
            esc(title),
            "\n".join("                            <li>%s</li>" % esc(x) for x in items),
        )
        for i, (title, items) in enumerate(columns)
    )
    return _ind(
        """
<div class="%s mb-120">
    <div class="container">
        <div class="%s">
            <div class="row">
                <div class="col-lg-12">
                    <div class="%s mb-60 fade_anim" data-delay=".2">
                        <h2 class="text-anim">%s</h2>
                    </div>
                </div>
            </div>
            <div class="row gy-5">
%s
            </div>
        </div>
    </div>
</div>
"""
        % (wrapper, wrap_cls, title_cls, esc(heading), cols)
    )


def tag_nav(links):
    lis = "\n".join(
        '                    <li><a href="%s">%s</a></li>' % (href, esc(label))
        for label, href in links
    )
    return _ind(
        """
<div class="industries-details-page mb-120">
    <div class="container">
        <div class="industries-details-content-wrap">
            <div class="tag-navigation-area">
                <ul class="tag-list">
%s
                </ul>
            </div>
        </div>
    </div>
</div>
"""
        % lis
    )


def write(slug, sections):
    """Join sections with a blank line between them and write the fragment."""
    import io
    import os

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    body = "\n\n".join(s.rstrip() for s in sections if s and s.strip()) + "\n"
    path = os.path.join(root, slug + ".html")
    io.open(path, "w", encoding="utf-8", newline="\n").write(body)
    return path
