#!/usr/bin/env python3
"""Give each expertise sub-page its own treatment of its "stages" section.

`packaging-filling`, `bottle-decoration` and `private-label-solutions` were
generated from one skeleton and are byte-identical in structure; `fragrance-
development` differs only in length. All four present their process as the same
Bootstrap accordion, so the set reads as one page with the nouns swapped.

The copy in those accordions is good and is kept verbatim. What changes is the
component it is rendered in — one per page, so no two of the four look alike:

    fragrance-development     -> home4-process-section  (dark numbered panel)
    packaging-filling         -> table-container        (spec table)
    bottle-decoration         -> award-section          (hover-linked list)
    private-label-solutions   -> home3-service-section  (phase cards)

    python _content/_lib/respine.py
"""

import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blocks as b  # noqa: E402

CONTENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_section(slug, name):
    """Return (whole_section_text, [(title, body), ...]) for a `<!-- name Start -->` block."""
    path = os.path.join(CONTENT, slug + ".html")
    s = io.open(path, encoding="utf-8", newline="").read()
    m = re.search(
        r"[ \t]*<!-- %s Start -->.*?<!-- %s End -->\n?" % (re.escape(name), re.escape(name)),
        s,
        re.S,
    )
    if not m:
        raise SystemExit("no %r section in %s" % (name, slug))
    block = m.group(0)
    items = []
    for it in re.finditer(
        r'<button class="accordion-button[^"]*"[^>]*>(.*?)</button>.*?'
        r'<div class="accordion-body">(.*?)</div>',
        block,
        re.S,
    ):
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", it.group(1))).strip()
        body = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", it.group(2))).strip()
        # Strip the leading ordinal ("01. " and "Stage 01 — ") — every replacement
        # component numbers its own items, and fragrance-development drops a stage,
        # so carrying the original numbers through would leave a visible gap.
        title = re.sub(r"^(?:stage\s*)?\d+\s*[.—–-]\s*", "", title, flags=re.I)
        items.append((title, body))
    return path, s, block, items


def swap(slug, name, build):
    path, s, block, items = read_section(slug, name)
    if not items:
        raise SystemExit("no accordion items found in %s / %s" % (slug, name))
    new = "                <!-- %s Start -->\n%s\n                <!-- %s End -->\n" % (
        name,
        build(items),
        name,
    )
    io.open(path, "w", encoding="utf-8", newline="").write(s.replace(block, new))
    print("  %-26s %d stage(s) -> %s" % (slug, len(items), build.__name__))


# ---------------------------------------------------------------------------


def as_process(items):
    """Dark numbered panel.

    `.single-process` only has `.two` / `.three` / `.four` variants, so the CSS
    supports exactly four cards. Fragrance development has five stages, and the
    one that is dropped here is stage 03, raw material sourcing — because the
    very next section on that page ("Raw material sourcing") already covers it
    at more length. Nothing else is discarded.
    """
    drop = "Raw material sourcing and qualification"
    kept = [it for it in items if drop.lower() not in it[0].lower()]
    if len(kept) != 4:
        raise SystemExit(
            "as_process needs exactly four stages after filtering, got %d: %s"
            % (len(kept), [t for t, _ in kept])
        )
    four = kept
    return b.process_section(
        "Development Path",
        "From Written Brief To Approved Formula",
        "Four stages, roughly twelve weeks, and a great deal of smelling. Nothing moves on "
        "until the stage before it is signed off.",
        "Start a Brief",
        "contact.html",
        [(t, bd) for t, bd in four],
        "fd",
    )


def as_table(items):
    """Spec table — the stage, what is decided, and what it constrains downstream."""
    rows = []
    for i, (title, body) in enumerate(items, start=1):
        first = body.split(". ")[0].rstrip(".") + "."
        rows.append([
            ("%02d" % i, "vacancies"),
            (title, "position-name"),
            (first, "job-type"),
        ])
    return b.spec_table(
        "How A Pack Gets Specified",
        "Every decision below constrains the ones after it, which is why the order matters "
        "more than the speed. A bottle chosen late is a bottle that forces the carton, the "
        "insert and the line speed to be reworked around it.",
        ["Stage", "Decision", "What it settles"],
        rows,
    )


def as_award(items):
    """Hover-linked list — the stage on the right, a process photo on the left.
    custom.js matches list and image by index, so both lists stay the same length."""
    photos = [
        ("bottle-decor.webp", "Gloved hand spray-lacquering a bottle behind the booth curtain"),
        ("home4-portfolio-img4.webp", "Stainless dosing head lowered over a compounding vessel"),
        ("packaging-unit.webp", "Empty conveyor running through the packaging hall"),
        ("home4-portfolio-img3.webp", "Operator loading empty bottles into the filling machine"),
        ("quality-lab.webp", "Graduated cylinders and a dropper on the quality bench"),
        ("production-lines.webp", "Gloved hands loading bottles onto the filling line"),
    ]
    rows = [(t, "%02d" % i) for i, (t, _) in enumerate(items, start=1)]
    return b.award_list(
        "How A Finish Gets Onto Glass",
        rows,
        [photos[i % len(photos)] for i in range(len(rows))],
    )


def as_cards(items):
    """Phase cards — three across, so the programme reads as parallel workstreams
    rather than a queue the client has to wait through."""
    cards = [
        {
            "id": None,
            "title": t,
            "href": "contact.html",
            "cta": "Discuss This Phase",
            "body": bd,
        }
        for t, bd in items
    ]
    return b.service_grid(
        "Programme Path",
        "What Happens, And In What Order",
        cards,
        cta=("Start a programme", "contact.html"),
    )


PLAN = [
    ("fragrance-development", "Development stages", as_process),
    ("packaging-filling", "Packaging stages", as_table),
    ("bottle-decoration", "Decoration stages", as_award),
    ("private-label-solutions", "Programme stages", as_cards),
]


if __name__ == "__main__":
    for slug, name, fn in PLAN:
        swap(slug, name, fn)
