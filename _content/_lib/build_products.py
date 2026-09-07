#!/usr/bin/env python3
"""Generate the expertise/products hubs and the four product category pages."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import (section, hero_split, two_lists, img_text, key_features,
                 why_choose, accordion, industries_block, partner_strip,
                 service_grid, cta, title_row, write)

TAGS = [("Fine Fragrances", "fine-fragrances.html"),
        ("Oriental Fragrances", "oriental-fragrances.html"),
        ("Home &amp; Lifestyle", "home-lifestyle.html"),
        ("Personal Care", "cosmetics-personal-care.html"),
        ("Private Label", "private-label.html")]

# ------------------------------------------------------------------- expertise
write("expertise", [
    section("service-details-page", hero_split(
        "images/production-lines.webp",
        "Production lines running inside the First Perfumes facility in Jebel Ali",
        "Six Disciplines That Never Leave The Building",
        ["Most fragrance brands assemble a product from four suppliers in three countries and spend "
         "their launch schedule reconciling them. We built the opposite: development, compounding, "
         "filling, decoration, packaging and quality control all sit on one floor in Jebel Ali, "
         "under one set of batch records.",
         "That integration is not just convenient. It means a perfumer can walk a trial to the "
         "filling line the same morning, a closure incompatibility surfaces in the laboratory "
         "instead of in a container, and a reorder two years later reproduces the same weight sheet."],
        eager=True), "Expertise overview"),

    service_grid("Our Expertise", "What We Do Under One Roof", None, [
        ("Fragrance Development",
         "Bespoke accords built to your brief, market and price point, with IFRA conformity and "
         "stability testing before anything is signed.",
         "fragrance-development.html"),
        ("Perfume Manufacturing",
         "Automated compounding, batching, filling and bottling, from thirty-litre exclusive runs "
         "to full-scale commercial production.",
         "perfume-manufacturing.html"),
        ("Private Label Solutions",
         "End-to-end programmes covering formula, packaging, market registration and freight, with "
         "your brand on everything and ours on nothing.",
         "private-label-solutions.html"),
        ("Cosmetics &amp; Personal Care",
         "Dedicated cleanroom lines for creams, body lotions, oils and hair mists, formulated to "
         "ISO 22716 cosmetics GMP.",
         "cosmetics-personal-care.html"),
        ("Packaging &amp; Filling",
         "Luxury primary and secondary packaging assembled in house, specified for recyclability "
         "in the destination market.",
         "packaging-filling.html"),
        ("Bottle &amp; Decoration",
         "Lacquering, multi-colour silk-screen, hot foil and metallising, tested against your own "
         "concentrate before production.",
         "bottle-decoration.html"),
    ], "Expertise grid"),

    section("faq-page", "\n\n".join([
        title_row("How We Work", "The Route Every Programme Takes", "contact.html", "Start a Brief"),
        accordion("expHow", [
            ("01. We understand the brief properly",
             "Market, audience, price point, volume and launch date. Most programmes that go wrong "
             "go wrong here, because an unrealistic date was accepted rather than challenged."),
            ("02. The laboratory develops and proves",
             "Accords are built or matched, then tested for stability and compatibility against the "
             "actual base, alcohol grade and closure the product will ship with."),
            ("03. Packaging is specified and tested",
             "Bottle, closure and carton are selected, then soak-tested together. Components are "
             "only purchased once the combination is proven."),
            ("04. Compliance is prepared in parallel",
             "IFRA conformity, allergen declarations and market notifications for UAE, EU, UK and US "
             "are prepared alongside development, not after it."),
            ("05. A pilot batch proves the scale-up",
             "The pilot runs in the same hall as the commercial batch, so maceration, filtration and "
             "settling behaviour are recorded before a production date is committed."),
            ("06. Production, release and dispatch",
             "Quality control releases against the master batch record. The consignment is palletised, "
             "documented and booked."),
        ])]), "How we work"),

    section("industries-details-page", industries_block(
        "Who We Build For",
        "The floor is set up so a first-time house and an established distributor can be served by "
        "the same equipment without either compromising. What changes between them is scheduling "
        "and volume, not the standard applied.",
        "Partners we work with",
        ["Niche and independent fragrance houses",
         "Retail and department store own-label ranges",
         "Regional distributors building proprietary brands",
         "Hospitality, spa and amenity programmes",
         "Cosmetics brands extending into fragrance",
         "Corporate gifting and limited edition projects"],
        "Whatever the category, the same batch records, the same release testing and the same "
        "traceability apply. There is no economy tier on quality.",
        "images/facility-jebel-ali.webp",
        "Exterior of the First Perfumes manufacturing facility in Jebel Ali Industrial First",
        TAGS), "Who we build for"),

    partner_strip("Operating under", "five", "international standards"),
    cta("Tell us what you are building. We will tell you what it takes to make it.",
        "Start a Conversation", "contact.html", "Expertise CTA"),
])

# -------------------------------------------------------------------- products
write("products", [
    section("service-details-page", hero_split(
        "images/our-work-img.webp",
        "Finished fine fragrance bottles produced for a private label client",
        "Four Product Families, One Standard",
        ["We manufacture across four families: fine fragrances, oriental compositions, home and "
         "lifestyle products, and complete private label programmes. They share a laboratory, a "
         "compounding hall and a quality control function, which is why a candle from us behaves "
         "as predictably as an Eau de Parfum does.",
         "Each family has its own constraints — an oil concentrate is not an alcohol base, and wax "
         "is neither — but none of them gets a lighter standard of testing or a shorter batch record."],
        eager=True), "Products overview"),

    service_grid("Product Families", "What We Manufacture", None, [
        ("Fine Fragrances",
         "Eau de Parfum, Eau de Toilette and Extrait de Parfum, built to hold their character from "
         "first spray through dry-down.",
         "fine-fragrances.html"),
        ("Oriental Fragrances",
         "Oud, bakhoor and Arabic perfumery made the way the region expects, at the volumes modern "
         "brands need.",
         "oriental-fragrances.html"),
        ("Home &amp; Lifestyle",
         "Room sprays, poured candles and reed diffusers that carry a signature scent beyond the body.",
         "home-lifestyle.html"),
        ("Private Label",
         "Three engagement depths, from filling a formula you already own to building a fragrance "
         "brand from a blank page.",
         "private-label.html"),
        ("Cosmetics &amp; Personal Care",
         "Creams, body lotions, oils and hair mists produced on dedicated cleanroom lines.",
         "cosmetics-personal-care.html"),
    ], "Product families"),

    section("service-details-page", "\n\n".join([
        two_lists("What Every Product Gets",
                  "Before production",
                  ["A numbered formula with percentages and material references",
                   "IFRA conformity for the declared product category",
                   "Stability testing at elevated and ambient temperature",
                   "Compatibility testing against the actual closure and juice",
                   "Allergen declaration prepared for EU and UK labelling",
                   "A pilot batch run on the commercial line"],
                  "With every batch",
                  ["A master batch record retained and available to you",
                   "Raw material traceability to supplier lot",
                   "Fill weight and closure torque checks through the run",
                   "Inline batch and date coding on every unit",
                   "Release testing against a retained reference sample",
                   "Export documentation prepared for the destination"]),
        key_features(["Stability Tested", "IFRA Conformity",
                      "Batch Traceable", "Export Ready"])]),
        "Quality band"),

    partner_strip("Every family produced under", "five", "compliance frameworks"),
    cta("Not sure which family your idea belongs in? That is a good first conversation.",
        "Talk It Through", "contact.html", "Products CTA"),
])


# ------------------------------------------------------- category page template
def category(slug, hero_img, hero_alt, hero_h2, hero_paras, anchors,
             standards_h2, left_h3, left, right_h3, right, features,
             ind_block, cta_line, cta_btn):
    parts = [section("service-details-page",
                     hero_split(hero_img, hero_alt, hero_h2, hero_paras, eager=True),
                     "%s overview" % slug)]
    for aid, img, alt, h3, paras, flip in anchors:
        parts.append(section("service-details-page",
                             img_text(img, alt, h3, paras, flip=flip),
                             h3, anchor=aid))
    parts.append(section("service-details-page", "\n\n".join([
        two_lists(standards_h2, left_h3, left, right_h3, right),
        key_features(features)]), "Standards"))
    parts.append(section("industries-details-page", ind_block, "Category detail"))
    parts.append(partner_strip("Produced under", "five", "regulatory frameworks"))
    parts.append(cta(cta_line, cta_btn, "contact.html", "%s CTA" % slug))
    write(slug, parts)


category(
    "fine-fragrances",
    "images/our-work-img.webp",
    "Fine fragrance bottles produced on the First Perfumes filling line",
    "Concentration Is A Decision, Not A Label",
    ["The difference between an Eau de Toilette and an Extrait is not marketing. It is the "
     "percentage of concentrate in the base, and it changes how the accord opens, how long it "
     "lasts and what it costs to make. We build each concentration deliberately rather than "
     "diluting one formula three ways and hoping.",
     "Every fine fragrance we produce is macerated, cold-filtered and held before filling, because "
     "a juice that is rushed to the bottle reads thin no matter how good the accord underneath is."],
    [
        ("eau-de-parfum", "images/our-work-right-img1.webp",
         "Eau de Parfum bottles filled and capped ready for inspection",
         "Eau de Parfum",
         ["Typically fifteen to twenty per cent concentrate in a high-grade ethanol base. This is "
          "the workhorse concentration for most commercial ranges: enough depth to carry a complex "
          "accord through a full dry-down, without the material cost of an Extrait. Expect six to "
          "eight hours of wear on skin from a well-built composition."], False),
        ("eau-de-toilette", "images/our-work-img5.webp",
         "Eau de Toilette production run moving through the filling hall",
         "Eau de Toilette",
         ["Typically eight to twelve per cent concentrate. Brighter on the opening and shorter on "
          "the skin, which suits daytime, warm-climate and higher-frequency use. An accord designed "
          "for Extrait rarely works here unmodified — the top notes need rebalancing or the "
          "composition reads hollow once the initial lift burns off."], True),
        ("extrait-de-parfum", "images/project-img3.webp",
         "Extrait de Parfum concentrate being weighed against a formula sheet",
         "Extrait de Parfum",
         ["Twenty to thirty per cent concentrate and sometimes higher. The richest and most "
          "expensive expression, usually reserved for a flagship or limited release. Extrait "
          "demands the longest maceration and the most careful filtration, because at this "
          "concentration any instability in the composition is immediately visible in the bottle."], False),
    ],
    "How We Build A Fine Fragrance",
    "Formulation", ["Accord development or matching to a supplied reference",
                    "Concentration set deliberately per product, not diluted down",
                    "High-grade ethanol with controlled water content",
                    "Maceration held for the period the composition needs",
                    "Cold filtration to remove haze without stripping character",
                    "Stability held at elevated and ambient temperature"],
    "Verification", ["IFRA conformity for the declared category",
                     "Allergen declaration for EU CPNP and UK SCPN",
                     "Compatibility against closure, gasket and bottle",
                     "Colour and clarity checked against a retained reference",
                     "Fill weight verified through the production run",
                     "Release testing before the batch is dispatched"],
    ["Macerated", "Cold Filtered", "Stability Held", "IFRA Conform"],
    industries_block(
        "Getting The Concentration Right",
        "Brands often arrive asking for an Eau de Parfum because it sounds premium, when their "
        "price point and their market actually call for an Eau de Toilette. Getting this wrong is "
        "expensive, because the concentrate is the single largest cost in the bottle.",
        "What drives the decision",
        ["Target retail price and the margin your channel needs",
         "Climate and wear expectations in the destination market",
         "How the accord behaves as concentration rises",
         "Whether the range needs a flagship at a higher concentration",
         "Regulatory limits on specific materials at higher loads",
         "Whether a lighter flanker will follow the main launch"],
        "We will model the unit cost at each concentration before you decide, so the choice is made "
        "against numbers rather than instinct.",
        "images/perfume-compounding.webp",
        "Compounding vessel and control panel during a fine fragrance batch",
        TAGS),
    "Tell us the price point and the market. We will tell you the concentration.",
    "Discuss a Fine Fragrance")


category(
    "oriental-fragrances",
    "images/our-work-img2.webp",
    "Oriental fragrance packaging produced at the First Perfumes facility",
    "Oriental Perfumery, Made Where It Is Understood",
    ["Oud, bakhoor and Arabic perfumery are not a category we added to a catalogue. They are the "
     "tradition this business grew out of, and the expectations around them are specific: depth "
     "over brightness, longevity measured in days rather than hours, and materials that reward "
     "patience in the maceration tank.",
     "We produce oriental compositions in both alcohol and oil bases, and in traditional formats "
     "that a Western-configured plant is usually not set up to handle at all."],
    [
        ("oud", "images/our-work-right-img2.webp",
         "Oud concentrate and traditional attar bottles arranged for inspection",
         "Oud",
         ["Oud is the most demanding material we work with and the easiest to get wrong. Quality "
          "varies enormously by origin and by distillation, and the difference between a good lot "
          "and a poor one is obvious in the finished product but not on a specification sheet. We "
          "buy against retained references and evaluate every lot on the blotter before it is "
          "approved into stock, whether it is destined for an alcohol base or a pure oil attar."], False),
        ("bakhoor", "images/project-img4.webp",
         "Bakhoor blend prepared with resins and wood chips before compression",
         "Bakhoor",
         ["Bakhoor production is a different discipline entirely — wood chips, resins and binders "
          "compounded and cured rather than compounded and filtered. Burn behaviour, smoke "
          "character and how evenly a piece holds together through handling all have to be tested "
          "physically, because none of it can be predicted from the formula alone."], True),
        ("arabic-perfumes", "images/legacy-perfumer.webp",
         "Traditional Arabic perfume bottles with decorative gold detailing",
         "Arabic Perfumes",
         ["Traditional Arabic compositions lean on amber, musk, rose and resins at concentrations "
          "that would overwhelm a Western fine fragrance. They are frequently presented as "
          "alcohol-free oil concentrates, which changes the stability profile completely and "
          "requires its own compatibility testing against the closure and the bottle."], False),
    ],
    "How We Build An Oriental Composition",
    "Materials", ["Oud evaluated by origin and distillation against references",
                  "Natural resins, ambers and musks held in a working library",
                  "Alcohol-free oil bases for traditional attar formats",
                  "Wood and binder selection for bakhoor compression",
                  "Extended maceration for heavy resinous compositions",
                  "Colour and sediment managed rather than filtered flat"],
    "Verification", ["IFRA conformity applied to the declared category",
                     "Allergen declaration for export markets",
                     "Compatibility of oil bases against closure and gasket",
                     "Burn testing for bakhoor formats",
                     "Longevity assessed on skin and on blotter",
                     "Release against a retained reference for every batch"],
    ["Oud Sourcing", "Oil Bases", "Extended Maceration", "Burn Tested"],
    industries_block(
        "Formats Beyond The Spray Bottle",
        "Oriental perfumery is presented in formats a standard fragrance line cannot fill. If your "
        "range needs any of these, it is worth confirming early — the packaging and the filling "
        "setup differ from an alcohol spray in ways that affect lead time.",
        "Traditional formats we produce",
        ["Alcohol-free oil concentrates and roll-on attars",
         "Compressed bakhoor in tablet and chip formats",
         "Concentrated perfume oils in decorative glass",
         "Alcohol-based oriental Eau de Parfum",
         "Incense and home fragrance in traditional profiles",
         "Gift and presentation sets combining several formats"],
        "Traditional does not mean undocumented. Every format carries the same batch record and the "
        "same release testing as our fine fragrance lines.",
        "images/our-work-img2.webp",
        "Oriental fragrance range prepared in decorative presentation packaging",
        TAGS),
    "If oud is central to your range, start the conversation early. Good material takes time to secure.",
    "Discuss an Oriental Range")


category(
    "home-lifestyle",
    "images/our-work-img3.webp",
    "Home fragrance diffusers and candles moving through the assembly line",
    "Scent That Lives In A Room, Not On Skin",
    ["Home fragrance is where a lot of brands underestimate the technical work. A composition that "
     "performs beautifully on skin can throw badly from a candle, discolour in a diffuser base or "
     "separate in a room spray, because the delivery medium changes everything about how the "
     "molecules behave.",
     "We develop home and lifestyle products as their own formulations rather than repurposing a "
     "fine fragrance accord and hoping it translates."],
    [
        ("home-fragrances", "images/our-work-right-img3.webp",
         "Room spray bottles filled and capped on the home fragrance line",
         "Home Fragrances",
         ["Room sprays and linen mists are formulated for throw and for surface safety, which are "
          "sometimes in tension. We test against the fabrics and finishes a product is likely to "
          "meet, because a mist that stains a linen cushion generates returns no amount of good "
          "scent will offset."], False),
        ("scented-candles", "images/project-img5.webp",
         "Poured candles cooling in glass vessels after filling",
         "Scented Candles",
         ["Candle work is as much thermal as olfactory. Wax system, fragrance load, wick size and "
          "vessel diameter have to be matched together, then burn-tested through the full life of "
          "the candle. We check for tunnelling, sooting, hot throw at realistic room volumes and "
          "adhesion between wax and glass as it cools."], True),
        ("diffusers", "images/our-work-img3.webp",
         "Reed diffusers assembled with rattan reeds and sealed transit closures",
         "Diffusers",
         ["Reed diffusers are a solvent problem before they are a scent problem. The base has to "
          "carry the composition up the reed at a controlled rate without discolouring, clouding "
          "or degrading the reed itself. We test throw and longevity over the stated life of the "
          "product rather than the first fortnight."], False),
    ],
    "How We Build A Home Product",
    "Development", ["Formulation designed for the delivery medium, not adapted",
                    "Wax system and fragrance load matched to vessel and wick",
                    "Diffuser bases tested for clouding and reed degradation",
                    "Room spray checked against common fabrics and finishes",
                    "Throw assessed at realistic room volumes",
                    "Colour stability under light exposure"],
    "Verification", ["Full-life burn testing for every candle format",
                     "Tunnelling, sooting and hot throw recorded",
                     "Diffuser longevity measured over the stated life",
                     "Transit testing for sealed diffuser closures",
                     "Allergen declaration for the declared category",
                     "Release against a retained reference sample"],
    ["Burn Tested", "Throw Measured", "Reed Verified", "Light Stable"],
    industries_block(
        "Where Home Products Are Sold",
        "The channel shapes the product more than the scent does. A candle for a hotel turndown "
        "service and a candle for a department store gift table have different burn times, "
        "different vessels and different unit economics.",
        "Channels we produce for",
        ["Retail and department store home fragrance ranges",
         "Hospitality turndown, lobby and spa programmes",
         "Corporate gifting and seasonal limited editions",
         "Fragrance houses extending an existing signature",
         "Interior and lifestyle brands adding scent",
         "Subscription and direct-to-consumer boxes"],
        "Tell us the channel and the price point first. It narrows the vessel, the wax and the "
        "fragrance load faster than any other question.",
        "images/our-work-img6.webp",
        "Home and lifestyle product range presented in retail packaging",
        TAGS),
    "Bring us a scent you love and the room you want it in. We will make it work in wax or in reeds.",
    "Discuss a Home Range")


category(
    "private-label",
    "images/our-work-img4.webp",
    "Private label fragrance range prepared for a client launch",
    "Three Ways To Work With Us",
    ["Private label covers a wide range of involvement, from filling a formula you already own to "
     "building a brand from a blank page. Being clear about which one you need changes the cost, "
     "the timeline and how much of your own team's attention the project will absorb.",
     "These are engagement models, not price tiers. What you pay depends on volume, materials and "
     "packaging, and we quote it against your actual specification rather than a published rate."],
    [
        ("custom-products", "images/our-work-img5.webp",
         "Custom product range filled and packed for a private label programme",
         "Custom Products",
         ["The lightest engagement. You bring a formula you own, or ask us to match a reference, "
          "and we handle compounding, filling and packing into components you have already chosen. "
          "Fastest route to stock, and the right choice when your brand and packaging are already "
          "settled and you simply need reliable manufacturing behind them."], False),
        ("custom-packaging", "images/home4-portfolio-img2.webp",
         "Custom packaging and decorated bottles staged for assembly",
         "Custom Packaging",
         ["The middle engagement. We take on component sourcing and decoration alongside "
          "manufacturing: bottle, closure, carton, lacquering, screen printing and foil. You keep "
          "creative control over the design; we own compatibility, tooling and the supply chain "
          "that has to deliver it repeatably."], True),
        ("brand-development", "images/home4-portfolio-img3.webp",
         "Brand development samples and packaging concepts laid out for review",
         "Brand Development",
         ["The full engagement. Accord development from a written brief, packaging design and "
          "sourcing, regulatory registration for your target markets, and export logistics. Suited "
          "to a first launch, or to an established brand entering fragrance for the first time and "
          "wanting one accountable partner rather than five suppliers."], False),
    ],
    "What Changes Between Models",
    "You provide", ["Custom Products: an owned formula or a reference to match",
                    "Custom Products: chosen components, or a spec for us to buy against",
                    "Custom Packaging: artwork, brand assets and design direction",
                    "Custom Packaging: target price point and volume commitment",
                    "Brand Development: a written brief and a market",
                    "Brand Development: trademark and brand ownership"],
    "We provide", ["Compounding, filling and packing in every model",
                   "Component sourcing and decoration from Custom Packaging up",
                   "Compatibility and stability testing in every model",
                   "Market registration from Brand Development, or on request",
                   "Batch records and release testing in every model",
                   "Export documentation and freight booking on request"],
    ["Formula Owned", "Components Sourced", "Markets Registered", "Freight Booked"],
    industries_block(
        "Choosing The Right Depth",
        "Most brands come in expecting one model and leave with another, usually because the "
        "conversation surfaces work they had not accounted for — market registration, closure "
        "compatibility or artwork that will not print at the size the carton allows.",
        "Questions that decide the model",
        ["Do you already own a formula, or does one need building?",
         "Are your components sourced, or do they need specifying?",
         "Which markets are you registering in, and who prepares that?",
         "Is your artwork production-ready or still conceptual?",
         "What is your first order volume, and your reorder cadence?",
         "How much of this does your own team want to carry?"],
        "There is no penalty for starting light and going deeper on the next order. Several of our "
        "longest-running programmes began as a single matched formula.",
        "images/compliance-global.webp",
        "Market registration and compliance documentation prepared for export",
        TAGS),
    "Not sure which model fits? Describe the project and we will tell you honestly.",
    "Find Your Model")

print("generated: expertise, products, fine-fragrances, oriental-fragrances, "
      "home-lifestyle, private-label")
