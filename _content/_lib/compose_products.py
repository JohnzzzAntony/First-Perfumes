#!/usr/bin/env python3
"""Rebuild the four Products & Solutions sub-pages, each with its own spine.

The first generation pass gave all four an identical seven-section skeleton, so
the range read as one page with the nouns swapped. Each page now leads with a
different component:

    fine-fragrances      3-across card grid  -> spec table
    oriental-fragrances  framed splits       -> award hover list
    home-lifestyle       industries link list -> numbered process panel
    private-label        pricing tiers       -> FAQ accordion

Run from the site root:  python _content/_lib/compose_products.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blocks as b  # noqa: E402

RANGE_NAV = [
    ("Fine Fragrances", "fine-fragrances.html"),
    ("Oriental Fragrances", "oriental-fragrances.html"),
    ("Home & Lifestyle", "home-lifestyle.html"),
    ("Personal Care", "cosmetics-personal-care.html"),
    ("Private Label", "private-label.html"),
]

FIVE_FRAMEWORKS = "Produced under <span>five</span> regulatory frameworks"


# ---------------------------------------------------------------- fine fragrances

def fine_fragrances():
    return [
        b.intro_split(
            "Concentration Is A Decision, Not A Label",
            [
                "The difference between an Eau de Toilette and an Extrait is not marketing. It is "
                "the percentage of concentrate in the base, and it changes how the accord opens, "
                "how long it lasts and what it costs to make. We build each concentration "
                "deliberately rather than diluting one formula three ways and hoping.",
                "Every fine fragrance we produce is macerated, cold-filtered and held before "
                "filling, because a juice that is rushed to the bottle reads thin no matter how "
                "good the accord underneath it is.",
            ],
            "legacy-perfumer.webp",
            "Finished First Perfumes bottles arranged on a marble surface",
        ),
        b.service_grid(
            "Concentrations",
            "Three Ways To Wear The Same Accord",
            [
                {
                    "id": "eau-de-parfum",
                    "title": "Eau de Parfum",
                    "href": "contact.html",
                    "cta": "Discuss EDP",
                    "body": "Fifteen to twenty per cent concentrate in a high-grade ethanol base. "
                    "The workhorse concentration for most commercial ranges: enough depth to "
                    "carry a complex accord through a full dry-down without the material cost of "
                    "an Extrait. Expect six to eight hours of wear from a well-built composition.",
                },
                {
                    "id": "eau-de-toilette",
                    "title": "Eau de Toilette",
                    "href": "contact.html",
                    "cta": "Discuss EDT",
                    "body": "Eight to twelve per cent concentrate. Brighter on the opening and "
                    "shorter on the skin, which suits daytime, warm-climate and higher-frequency "
                    "use. An accord designed for Extrait rarely works here unmodified — the top "
                    "notes need rebalancing or the composition reads hollow.",
                },
                {
                    "id": "extrait-de-parfum",
                    "title": "Extrait de Parfum",
                    "href": "contact.html",
                    "cta": "Discuss Extrait",
                    "body": "Twenty to thirty per cent concentrate and sometimes higher. The "
                    "richest expression, usually reserved for a flagship or limited release. "
                    "Extrait demands the longest maceration and the most careful filtration, "
                    "because any instability is immediately visible in the bottle.",
                },
            ],
            cta=("See the full range", "products.html"),
            anchored=True,
        ),
        b.spec_table(
            "The Numbers Behind The Choice",
            "Brands often ask for an Eau de Parfum because it sounds premium, when their price "
            "point and their market actually call for an Eau de Toilette. The concentrate is the "
            "single largest cost in the bottle, so we model the unit cost at each concentration "
            "before you commit to one.",
            ["Concentration", "Concentrate load", "Typical wear", "Suits"],
            [
                [("Eau de Toilette", "position-name"), ("8–12%", "vacancies"),
                 ("3–4 hours", "job-type"), ("Daytime and warm-climate ranges", "job-type")],
                [("Eau de Parfum", "position-name"), ("15–20%", "vacancies"),
                 ("6–8 hours", "job-type"), ("Core commercial ranges", "job-type")],
                [("Extrait de Parfum", "position-name"), ("20–30%", "vacancies"),
                 ("8–12 hours", "job-type"), ("Flagship and limited releases", "job-type")],
                [("Body mist", "position-name"), ("3–5%", "vacancies"),
                 ("1–2 hours", "job-type"), ("Range extensions and gifting sets", "job-type")],
            ],
        ),
        b.two_col_lists(
            "How We Build A Fine Fragrance",
            [
                ("Formulation", [
                    "Accord development, or matching to a supplied reference",
                    "Concentration set deliberately per product, not diluted down",
                    "High-grade ethanol with controlled water content",
                    "Maceration held for the period the composition needs",
                    "Cold filtration to remove haze without stripping character",
                    "Stability held at elevated and ambient temperature",
                ]),
                ("Verification", [
                    "IFRA conformity for the declared category",
                    "Allergen declaration for EU CPNP and UK SCPN",
                    "Compatibility against closure, gasket and bottle",
                    "Colour and clarity checked against a retained reference",
                    "Fill weight verified through the production run",
                    "Release testing before the batch is dispatched",
                ]),
            ],
            wrapper="service-details-page",
        ),
        b.key_features(["Macerated", "Cold Filtered", "Stability Held", "IFRA Conform"]),
        b.compliance_marquee(FIVE_FRAMEWORKS),
        b.cta_banner(
            "Tell us the price point and the market. We will tell you the concentration.",
            "Discuss a Fine Fragrance",
        ),
    ]


# ------------------------------------------------------------- oriental fragrances

def oriental_fragrances():
    return [
        b.intro_split(
            "Regional Perfumery, Built For Modern Volumes",
            [
                "Oriental perfumery is not a style we adopted for the market — it is the tradition "
                "this facility grew out of. Oud, amber, saffron and rose have been on our bench "
                "since 2006, and the buying expectations that come with them are unforgiving.",
                "What has changed is scale. The same depth a regional customer expects from a "
                "hand-blended attar now has to survive a production run of eighty thousand units "
                "with no drift between the first bottle and the last.",
            ],
            "legacy-perfumer.webp",
            "The First Perfumes bottle range, including oriental compositions",
            img_left=False,
        ),
        b.split(
            "industries-details-page", "oud",
            "Oud",
            [
                "Agarwood in its many grades, from cultivated Southeast Asian material through to "
                "the darker, more resinous profiles the Gulf market associates with quality. We "
                "work with both natural oud oil and reconstructed accords, and we will tell you "
                "plainly which one your price point supports.",
            ],
            "perfume-compounding.webp",
            "Operator at the compounding control panel with an amber bottle on the line",
            bullet_heading="What we handle",
            bullets=[
                "Natural oud oil sourcing with documented origin",
                "Reconstructed oud accords for volume production",
                "Blending into Eau de Parfum and Extrait bases",
                "Concentrated oil formats for the regional market",
            ],
        ),
        b.split(
            "industries-details-page", "bakhoor",
            "Bakhoor",
            [
                "Compressed incense blends built on agarwood chips, resins, sugars and fragrance "
                "oil. Bakhoor is judged on how it burns as much as how it smells, so we control "
                "moisture content and binder ratio tightly — a blend that smoulders unevenly is a "
                "failed batch regardless of the accord.",
            ],
            "home4-portfolio-img3.webp",
            "Operator loading empty bottles into the filling machine",
            img_left=False,
            bullet_heading="What we handle",
            bullets=[
                "Chip, tablet and loose-blend formats",
                "Moisture and binder control for an even burn",
                "Fragrance oil loading matched to the base material",
                "Foil, tin and gift-box presentations",
            ],
        ),
        b.split(
            "industries-details-page", "arabic-perfumes",
            "Arabic Perfumes",
            [
                "Alcohol-free concentrated oils and mukhallat blends, layered in the way regional "
                "customers actually wear them. These compositions are built for depth on the skin "
                "over hours rather than a bright opening, which changes both the material choice "
                "and the maceration schedule.",
            ],
            "home4-portfolio-img4.webp",
            "Stainless dosing head lowered over a compounding vessel",
            bullet_heading="What we handle",
            bullets=[
                "Mukhallat blending with layered material profiles",
                "Alcohol-free oil bases for regional preference",
                "Roll-on, dab and spray presentations",
                "Extended maceration for depth on the skin",
            ],
        ),
        b.award_list(
            "The Materials This Bench Is Built On",
            [
                ("Agarwood — cultivated and wild-origin grades", "Oud"),
                ("Ambergris accords and amber resins", "Amber"),
                ("Taif and Damask rose absolutes", "Rose"),
                ("Saffron, from thread to tincture", "Saffron"),
                ("White musk and macrocyclic musks", "Musk"),
            ],
            [
                ("award-img.webp", "Agarwood chips prepared for distillation"),
                ("award-img2.webp", "Amber resin material on the formulation bench"),
                ("award-img3.webp", "Rose absolute being measured into a blend"),
                ("award-img4.webp", "Saffron threads weighed for a tincture"),
                ("award-img5.webp", "Musk base materials in the raw material store"),
            ],
        ),
        b.faq_accordion(
            "Sourcing Questions We Are Asked Most",
            [
                ("Is your oud natural or reconstructed?",
                 "Both, and the choice is yours. Natural oud oil carries documented origin and a "
                 "cost per kilogram that only works above a certain retail price. Reconstructed "
                 "accords give you a stable, repeatable profile at volume. We will cost both "
                 "against your target margin before you decide."),
                ("Can you match an existing regional bestseller?",
                 "We can work from a physical reference and build towards it. We will not "
                 "represent the result as a copy, and we will flag any material in the reference "
                 "that is restricted in your destination markets."),
                ("Do alcohol-free oils need the same compliance work?",
                 "Yes. IFRA limits apply to the composition regardless of the carrier, and EU "
                 "CPNP and UK SCPN notification is driven by the finished product. The allergen "
                 "declaration changes, but the obligation does not."),
                ("What is the minimum run for a mukhallat?",
                 "Three thousand units for a standard presentation. Below that the setup and "
                 "cleandown time dominates the unit cost and you are paying for our schedule "
                 "rather than for product."),
            ],
            "oriental-faq",
        ),
        b.tag_nav(RANGE_NAV),
        b.compliance_marquee(FIVE_FRAMEWORKS),
        b.cta_banner(
            "Bring us a reference, a price point, or just a direction. We will build from there.",
            "Discuss an Oriental Range",
        ),
    ]


# ------------------------------------------------------------------ home & lifestyle

def home_lifestyle():
    return [
        b.intro_split(
            "Scent That Has To Fill A Room, Not A Wrist",
            [
                "A composition that works beautifully on skin can disappear in a living room. "
                "Home fragrance is a different formulation problem: the accord has to project "
                "into open air, survive heat or a reed, and hold its character for weeks rather "
                "than hours.",
                "We develop home and lifestyle products on the same bench and to the same "
                "standards as our fine fragrances, then re-engineer the composition for the "
                "delivery format rather than pouring an existing juice into a new vessel.",
            ],
            "home4-portfolio-img.webp",
            "Luxury rigid gift boxes from the First Perfumes packaging range",
        ),
        b.industries_list(
            "Formats",
            "Three Ways To Scent A Space",
            [
                ("Home Fragrances", "#home-fragrances", "our-work-right-img3.webp",
                 "our-work-img3.webp", "Room spray and linen mist production run"),
                ("Scented Candles", "#scented-candles", "home4-portfolio-img2.webp",
                 "home4-portfolio-img3.webp", "Stainless compounding tanks used to batch candle fragrance"),
                ("Diffusers", "#diffusers", "quality-lab.webp",
                 "our-work-img6.webp", "Graduated cylinders of diffuser base under laboratory check"),
            ],
        ),
        b.split(
            "service-details-page", "home-fragrances",
            "Home Fragrances",
            [
                "Room sprays, linen mists and fabric refreshers built on water-tolerant bases. "
                "The formulation challenge here is projection without harshness — a room spray "
                "that reads sharp on the first pass will not be used twice, no matter how good "
                "the dry-down is.",
                "We test on the actual substrates the product will meet: upholstery, cotton, "
                "painted surfaces and glass, because staining complaints are far more expensive "
                "than reformulation.",
            ],
            "packaging-unit.webp",
            "Home fragrance bottles moving along the packaging conveyor",
        ),
        b.split(
            "service-details-page", "scented-candles",
            "Scented Candles",
            [
                "Soy, coconut and paraffin blends poured into glass, ceramic and tin. Fragrance "
                "load, wick specification and vessel diameter have to be solved together — a "
                "candle that tunnels or sends up soot is a wick problem long before it is a "
                "fragrance problem.",
                "Every candle format we ship has been burn-tested to completion, with hot and "
                "cold throw assessed at each stage and the melt pool measured against the vessel.",
            ],
            "home4-portfolio-img2.webp",
            "Stainless compounding tanks used to batch home fragrance bases",
            img_left=False,
        ),
        b.split(
            "service-details-page", "diffusers",
            "Diffusers",
            [
                "Reed and no-flame diffusers on carriers selected for wicking rate rather than "
                "cost. The reed draws at a fixed speed, so the composition has to be balanced for "
                "what evaporates first — otherwise the top notes are gone in a week and the "
                "customer smells only base for the next two months.",
                "We specify the reed count and diameter alongside the fluid, and we quote a "
                "realistic room size rather than an optimistic one.",
            ],
            "quality-lab.webp",
            "Graduated cylinders of diffuser base under laboratory check",
        ),
        b.process_section(
            "Development",
            "From Room Brief To Shipped Case",
            "Home fragrance moves faster than fine fragrance because the compliance surface is "
            "smaller — but the burn and wicking work cannot be rushed.",
            "Start a Home Brief",
            "contact.html",
            [
                ("Format & Brief", "Vessel, delivery method, room size and target burn or "
                 "wicking life are agreed before any scent work begins."),
                ("Accord & Load", "The composition is built for the format and the fragrance "
                 "load is set against the base, not carried over from a skin product."),
                ("Burn & Wick Trials", "Candles are burned to completion and diffusers run for "
                 "eight weeks; wick, reed and load are adjusted against the results."),
                ("Production & Pack", "Pouring, curing, filling and assembly on our own lines, "
                 "with cure time treated as a scheduled stage rather than a delay."),
            ],
            "hl",
        ),
        b.key_features(["Burn Tested", "Throw Measured", "Substrate Safe", "Cure Scheduled"]),
        b.tag_nav(RANGE_NAV),
        b.cta_banner(
            "Tell us the room and the format. We will engineer the throw to match.",
            "Discuss a Home Range",
        ),
    ]


# --------------------------------------------------------------------- private label

def private_label():
    return [
        b.intro_split(
            "Your Brand On The Bottle, Our Infrastructure Behind It",
            [
                "Private label covers a wide range of arrangements, from filling a formula you "
                "already own to building a fragrance brand from a blank page. The three "
                "programmes below are the shapes most of our partners land on.",
                "All three run through the same laboratory, the same lines and the same "
                "compliance process. What changes is how much of the work sits with us.",
            ],
            "cosmetics-care.webp",
            "Laboratory technicians measuring a batch for a private label programme",
            img_left=False,
        ),
        b.pricing_tiers(
            "Three Ways To Work With Us",
            "These are programme shapes rather than fixed packages — every quote is built against "
            "your volumes, formats and destination markets. Use them to work out which "
            "conversation to start.",
            [
                {
                    "id": "custom-products",
                    "name": "Custom Products",
                    "headline": "Formula first",
                    "note": "You bring the direction, we build the juice",
                    "btn": "Enquire",
                    "cta": "Start a Product Brief",
                    "features": [
                        ("Accord development from a written brief", True),
                        ("Concentration modelled against your price point", True),
                        ("Stability and compatibility testing", True),
                        ("Filling, capping and assembly on our lines", True),
                        ("Stock bottle and closure selection", True),
                        ("Bespoke bottle tooling", False),
                        ("Brand identity and naming", False),
                    ],
                },
                {
                    "id": "custom-packaging",
                    "name": "Custom Packaging",
                    "headline": "Product and presentation",
                    "note": "Everything above, plus the pack",
                    "btn": "Enquire",
                    "cta": "Start a Packaging Brief",
                    "features": [
                        ("Everything in Custom Products", True),
                        ("Bottle, closure and carton specification", True),
                        ("Lacquering, silk-screen and hot foil in house", True),
                        ("Structural packaging and insert design", True),
                        ("Recyclable and reduced-material options", True),
                        ("Bespoke bottle tooling where volumes justify it", True),
                        ("Brand identity and naming", False),
                    ],
                },
                {
                    "id": "brand-development",
                    "name": "Brand Development",
                    "headline": "Blank page to launch",
                    "note": "The full programme, end to end",
                    "btn": "Enquire",
                    "cta": "Start a Brand Brief",
                    "features": [
                        ("Everything in Custom Packaging", True),
                        ("Range architecture and flanker planning", True),
                        ("Market and channel positioning support", True),
                        ("Registration for UAE, EU, UK and US markets", True),
                        ("Launch and reorder scheduling", True),
                        ("Export documentation and logistics", True),
                        ("Retail and distribution introductions", True),
                    ],
                },
            ],
            footnote=(
                "Not sure which shape fits? Send us the volumes and the timeline and we will tell you.",
                "Talk to a Programme Lead",
                "contact.html",
            ),
        ),
        b.two_col_lists(
            "What We Need From You, And What You Get Back",
            [
                ("What we need", [
                    "Target retail price and the margin your channel needs",
                    "Destination markets, so registration can start early",
                    "Volume for the first run and your expected reorder cadence",
                    "Any reference product you want us to work towards",
                    "Brand assets, or a decision to have us develop them",
                    "A realistic launch date we can schedule backwards from",
                ]),
                ("What you get", [
                    "A costed formula with the concentration justified",
                    "Retained references for every approved batch",
                    "Full compliance dossier for each destination market",
                    "Batch traceability from raw material to shipped case",
                    "A named contact who stays with the account after launch",
                    "Reorder lead times quoted against real line capacity",
                ]),
            ],
        ),
        b.faq_accordion(
            "Before You Start A Programme",
            [
                ("What is the minimum order quantity?",
                 "Three thousand units per SKU for a standard presentation, and one thousand for "
                 "a repeat run on tooling we already hold. Below that, setup and cleandown "
                 "dominate the unit cost."),
                ("Who owns the formula?",
                 "You do, for any accord developed to your brief and paid for under the "
                 "programme. We retain the right to use general techniques and our own base "
                 "materials, but the composition is yours and it is written down as such."),
                ("How long does a first run take?",
                 "Twelve to eighteen weeks from approved brief to shipped case for a "
                 "straightforward programme. Registration for a new market is usually the "
                 "critical path, not production."),
                ("Can you ship direct to our distributor?",
                 "Yes. We handle export documentation from Jebel Ali and can ship to your "
                 "distributor, your 3PL or your own warehouse."),
            ],
            "pl-faq",
        ),
        b.contact_strip(
            "Ready to talk volumes? We reply to every enquiry within one business day.",
            "Start a Private Label Brief",
        ),
        b.tag_nav(RANGE_NAV),
        b.cta_banner(
            "Bring us the brand. We will bring the laboratory, the lines and the paperwork.",
            "Discuss Private Label",
        ),
    ]


PAGES = {
    "fine-fragrances": fine_fragrances,
    "oriental-fragrances": oriental_fragrances,
    "home-lifestyle": home_lifestyle,
    "private-label": private_label,
}


if __name__ == "__main__":
    targets = sys.argv[1:] or sorted(PAGES)
    for slug in targets:
        print("wrote", b.write(slug, PAGES[slug]()))
