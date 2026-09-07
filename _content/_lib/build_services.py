#!/usr/bin/env python3
"""Generate the three remaining expertise detail pages."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import (section, hero_split, two_lists, img_text, key_features,
                 why_choose, accordion, industries_block, partner_strip,
                 service_grid, cta, title_row, write, btn2)

SERVICES = {
    "fragrance-development": ("Fragrance Development",
        "Bespoke accords developed in our own laboratory, from written brief to signed formula."),
    "perfume-manufacturing": ("Perfume Manufacturing",
        "Automated compounding, batching, filling and bottling at any volume you need."),
    "private-label-solutions": ("Private Label Solutions",
        "Your brand on the bottle, our infrastructure behind it — formula to freight."),
    "cosmetics-personal-care": ("Cosmetics &amp; Personal Care",
        "Cleanroom lines for creams, lotions, oils and hair mists under ISO 22716."),
    "packaging-filling": ("Packaging &amp; Filling",
        "Luxury presentation engineered for the shelf and for the planet."),
    "bottle-decoration": ("Bottle &amp; Decoration",
        "Lacquering, silk-screen, hot foil and specialty finishes done in house."),
}


def related(exclude):
    cards = [(t, b, "%s.html" % s) for s, (t, b) in SERVICES.items() if s != exclude][:5]
    return service_grid("Related Expertise", "The Rest of the Floor",
                        "expertise.html", cards)


TAGS = [("Fine Fragrances", "fine-fragrances.html"),
        ("Oriental Fragrances", "oriental-fragrances.html"),
        ("Home &amp; Lifestyle", "home-lifestyle.html"),
        ("Personal Care", "cosmetics-personal-care.html"),
        ("Private Label", "private-label.html")]

# ---------------------------------------------------------------- private label
write("private-label-solutions", [
    section("service-details-page", hero_split(
        "images/home4-portfolio-img.webp",
        "Finished private label fragrance bottles arranged before final packing",
        "Your Brand On The Bottle, Our Name Nowhere On It",
        ["A private label programme at First Perfumes covers everything between a brand idea and "
         "a pallet of saleable stock: accord development, alcohol and concentrate supply, primary "
         "and secondary packaging, regulatory registration for your target markets, and export "
         "documentation. You own the formula, the artwork and the customer relationship.",
         "We have run programmes for houses launching their first thirty-bottle sampling round "
         "and for distributors placing repeat orders in the tens of thousands. The difference "
         "between those two is scheduling, not standards — the same batch records and the same "
         "release testing apply to both."],
        eager=True), "Private label overview"),

    section("service-details-page", "\n\n".join([
        two_lists("What A Programme Includes",
                  "We handle",
                  ["Accord development or matching to a reference you supply",
                   "Concentrate compounding, maceration and cold filtration",
                   "Bottle, pump, collar and cap sourcing to your specification",
                   "Secondary packaging: cartons, inserts, cellophane and labels",
                   "Product registration for UAE, EU, UK and US markets",
                   "Export documentation, palletisation and freight booking"],
                  "You keep",
                  ["Full ownership of the approved formula and its number",
                   "All artwork, trademarks and brand assets you supply",
                   "Your own distributor and retail relationships",
                   "Freedom to move volumes up or down between orders",
                   "Direct access to the perfumer who built your accord",
                   "The right to audit your batch records at any time"]),
        img_text("images/our-work-img4.webp",
                 "Private label range prepared for export in branded outer cartons",
                 "One Point Of Contact, Not A Relay",
                 ["Every programme gets a named account contact who sits between you and the floor. "
                  "That person carries your brief into the laboratory, chases the stability results, "
                  "flags a closure that will not seal against your chosen neck finish, and tells you "
                  "when a shipping date is going to move before it moves. You are not re-explaining "
                  "your brand to a new person on every order."], flip=True),
        key_features(["Formula Ownership", "Market Registration",
                      "Flexible Volumes", "Single Contact"]),
        why_choose([
            ("Invisible by design.", "Nothing we produce carries our name. Cartons, inserts and "
             "documentation reference your brand only."),
            ("Registration handled.", "CPNP and SCPN notification, INCI-compliant labelling and "
             "safety assessments are prepared as part of the programme, not billed as an afterthought."),
            ("Costed before you commit.", "You see a landed unit cost broken down by juice, bottle, "
             "closure, carton and labour before the first production order is written."),
            ("Scale without re-tooling.", "The same formula runs on the same line at thirty litres "
             "or four hundred kilos, so a successful launch does not force a reformulation."),
            ("Documented for audit.", "Batch records, release certificates and material traceability "
             "are retained and available to you on request."),
            ("Freight arranged.", "Palletised, wrapped and booked to your forwarder or ours, with "
             "the paperwork your destination customs will actually ask for."),
        ])]), "Programme scope"),

    section("faq-page", "\n\n".join([
        title_row("How It Runs", "From First Call To First Pallet", "contact.html", "Start a Brief"),
        accordion("plProgramme", [
            ("01. Discovery and brief",
             "We establish your market, price point, target volumes and launch date, and agree what "
             "you are supplying versus what we are sourcing. This is where an unrealistic timeline "
             "gets corrected, while correcting it is still cheap."),
            ("02. Accord development or matching",
             "Our perfumers either build to your brief or match a reference you provide. You receive "
             "numbered submissions and we iterate until one is approved in writing."),
            ("03. Packaging selection and compatibility",
             "Bottle, closure and secondary packaging are selected and then tested against the "
             "concentrate. Gasket swell, colour drift and print adhesion are checked before the "
             "purchase order for components goes out."),
            ("04. Regulatory registration",
             "Safety assessment, allergen declaration and market notification are prepared for each "
             "destination. Nothing ships to the EU or UK without its notification reference in hand."),
            ("05. Pilot batch and approval",
             "A pilot runs on the production line that will make the commercial batch. You approve "
             "against a retained reference sample before scale-up is scheduled."),
            ("06. Production, release and dispatch",
             "The commercial batch runs, quality control releases it against the master batch record, "
             "and the consignment is palletised and booked."),
        ])]), "Programme stages"),

    section("industries-details-page", industries_block(
        "Where Private Label Programmes Land",
        "A private label programme is not one product type. The same infrastructure serves a niche "
        "house launching a six-bottle discovery set and a hospitality group scenting four hundred "
        "rooms, and the constraints are genuinely different.",
        "Programmes we run most often",
        ["Niche fragrance houses launching a first commercial range",
         "Retail and department store own-label fragrance lines",
         "Hospitality and spa amenity ranges in bespoke packaging",
         "Corporate gifting and limited seasonal editions",
         "Distributor-owned brands for regional exclusivity",
         "Celebrity and influencer launches under compressed timelines"],
        "If your programme does not obviously fit one of those, it is still worth a call. Most of "
        "what we build is a variation on infrastructure that already exists on the floor.",
        "images/compliance-global.webp",
        "Regulatory documentation prepared for international market registration",
        TAGS), "Programme types"),

    partner_strip("Registered and notified across", "five", "regulatory frameworks"),
    related("private-label-solutions"),
    cta("Tell us what you want to launch, and we will tell you what it takes.",
        "Start Your Programme", "contact.html", "Private label CTA"),
])

# ------------------------------------------------------------ packaging filling
write("packaging-filling", [
    section("service-details-page", hero_split(
        "images/packaging-unit.webp",
        "Assembly line running finished cartons through the First Perfumes packaging hall",
        "Packaging That Survives The Shelf And The Shipping Lane",
        ["Our packaging hall handles primary filling and secondary assembly on the same floor as "
         "compounding, so juice never travels between sites to be bottled. Filling lines are set up "
         "for glass and PET across a wide range of neck finishes, with crimping, screw and press-on "
         "closures all supported.",
         "Sustainability is a specification here, not a slogan. We default to recyclable mono-material "
         "cartons, run the hall on energy-efficient equipment, and measure component waste per batch "
         "so it can be argued about and reduced rather than estimated."],
        eager=True), "Packaging overview"),

    section("service-details-page", "\n\n".join([
        two_lists("Formats And Finishes",
                  "Filling capability",
                  ["Glass and PET from 5 ml samples to 500 ml home fragrance",
                   "Crimp, screw and press-on closures with torque verification",
                   "Alcohol-based, oil-based and water-based fills",
                   "Candle wax pouring with controlled cooling",
                   "Reed diffuser filling with sealed transit closures",
                   "Nitrogen purge for oxidation-sensitive concentrates"],
                  "Secondary assembly",
                  ["Rigid and folding cartons with foil and emboss options",
                   "Cellophane wrapping and tamper-evident sealing",
                   "Insert forming for multi-piece discovery sets",
                   "Label application, batch coding and date marking",
                   "Retail-ready outer cases and display trays",
                   "Palletisation to your destination's pallet standard"]),
        img_text("images/sustainability-env.webp",
                 "Recyclable packaging materials staged for a sustainable assembly run",
                 "Sustainability As A Line Item",
                 ["Every programme gets a packaging specification that states material, recyclability "
                  "and expected waste rate before the first component is ordered. Mono-material cartons "
                  "are the default because mixed laminates cannot be recycled in most destination "
                  "markets, and a beautiful box that ends up in landfill is a brand problem waiting to "
                  "happen. Where a client wants a finish that compromises recyclability, we say so in "
                  "writing and let them decide with the trade-off in front of them."], flip=True),
        key_features(["Filling Lines", "Rigid Cartons",
                      "Recyclable Default", "Retail Ready"]),
        why_choose([
            ("Filled where it is made.", "Concentrate does not leave the site to be bottled, which "
             "removes a transfer step and a contamination risk."),
            ("Compatibility tested first.", "Closure, gasket and juice are tested together before "
             "components are purchased, not after a leaking pallet arrives."),
            ("Waste measured per batch.", "Component waste is recorded against each run so reduction "
             "targets are based on numbers rather than intentions."),
            ("Mono-material by default.", "Cartons are specified to be recyclable in the destination "
             "market unless you explicitly choose otherwise."),
            ("Coded for traceability.", "Batch and date coding is applied inline, so any unit can be "
             "traced back to its master batch record."),
            ("Packed for the journey.", "Transit testing covers the drop, vibration and temperature "
             "your consignment will actually meet."),
        ])]), "Formats and finishes"),

    section("faq-page", "\n\n".join([
        title_row("Packaging Path", "How A Pack Gets Specified", "contact.html", "Start a Brief"),
        accordion("pkStages", [
            ("01. Format and volume",
             "Bottle size, material and neck finish are chosen against your price point and the "
             "shelf you are selling from. This decision constrains almost everything downstream, "
             "so it is made first and deliberately."),
            ("02. Component sourcing",
             "We source glass, closures and cartons to specification, or receive components you "
             "have sourced yourself and inspect them on goods-in against an agreed standard."),
            ("03. Compatibility and transit testing",
             "Juice and closure are tested together; the packed unit is tested for drop, vibration "
             "and temperature against the route it will travel."),
            ("04. Line trial",
             "A short run proves the fill volume, torque, label placement and carton fit before the "
             "full order is scheduled. Adjustments are cheap at this stage."),
            ("05. Production and inline QC",
             "Fill weight, closure torque and coding are checked at set intervals through the run "
             "and recorded against the batch."),
            ("06. Case packing and palletisation",
             "Units are cased, palletised to your destination standard, wrapped and labelled for "
             "the forwarder."),
        ])]), "Packaging stages"),

    section("industries-details-page", industries_block(
        "Packaging Formats We Run",
        "Presentation is where most of a fragrance brand's perceived value sits, and it is also "
        "where most of the avoidable cost sits. These are the formats we run most often and the "
        "constraints worth knowing before you commit to a design.",
        "Formats in regular production",
        ["Standard fragrance bottles from 30 ml to 100 ml in glass",
         "Discovery and sampling sets with formed inserts",
         "Travel sprays and refillable atomisers",
         "Reed diffusers with sealed transit closures",
         "Poured candles in glass and tin with fitted lids",
         "Amenity formats for hospitality in PET and glass"],
        "If your design needs a component we do not stock, we will quote the tooling and the lead "
        "time honestly rather than quietly substituting something close.",
        "images/bottle-decor.webp",
        "Decorated bottles staged for final packing after lacquering and printing",
        TAGS), "Packaging formats"),

    partner_strip("Packed to", "five", "international compliance standards"),
    related("packaging-filling"),
    cta("Bring us a design, or a rough idea and a budget. Both work.",
        "Discuss Your Pack", "contact.html", "Packaging CTA"),
])

# --------------------------------------------------------------- bottle & decor
write("bottle-decoration", [
    section("service-details-page", hero_split(
        "images/bottle-decor.webp",
        "Robotic spray arm applying coloured lacquer to fragrance bottles in the decoration section",
        "Where A Container Becomes A Brand Statement",
        ["Our decoration section handles bottle colouring and finishing in house: spray lacquering "
         "in gloss, matte and soft-touch, multi-colour silk-screen printing, hot foil stamping, "
         "vacuum metallising and frosting. Keeping it on site means a decorated bottle can go "
         "straight to filling without a second transport leg and a second chance to arrive chipped.",
         "Decoration is also where compatibility problems surface late and expensively. A lacquer "
         "that looks perfect on day one can craze after four weeks against a particular alcohol "
         "grade, so we test finishes against your actual juice before a production order is placed."],
        eager=True), "Decoration overview"),

    section("service-details-page", "\n\n".join([
        two_lists("Finishes And Techniques",
                  "Surface finishes",
                  ["Spray lacquering in gloss, matte and soft-touch",
                   "Gradient and two-tone colour transitions",
                   "Acid-free frosting and satin etch effects",
                   "Vacuum metallising in gold, silver and bronze tones",
                   "Soft-touch rubberised coating for premium ranges",
                   "Colour matching to a supplied Pantone reference"],
                  "Applied decoration",
                  ["Multi-colour silk-screen printing up to six passes",
                   "Hot foil stamping in gloss and matte foils",
                   "Embossed and debossed detailing on compatible glass",
                   "UV curing for scratch and solvent resistance",
                   "Selective masking for partial-coverage effects",
                   "Cap, collar and pump finishing to match the bottle"]),
        img_text("images/our-work-img6.webp",
                 "Range of custom decorated bottles showing lacquer, foil and screen-print finishes",
                 "Tested Against Your Juice, Not A Standard",
                 ["A finish is only approved once it has sat against the actual concentrate, in the "
                  "actual bottle, for the duration we agree. We check for crazing, colour drift, "
                  "adhesion loss at the closure line and print rub through simulated handling. Where "
                  "a requested finish will not survive the product it is wrapping, we say so and "
                  "propose an alternative that will, rather than shipping something that fails in "
                  "month three on a distributor's shelf."], flip=True),
        key_features(["Spray Lacquering", "Silk-Screen",
                      "Hot Foil", "Metallising"]),
        why_choose([
            ("Decorated on site.", "No transport leg between decoration and filling, which removes "
             "the most common source of chipped and scuffed stock."),
            ("Pantone matched.", "Colour is matched to a supplied reference and signed off against a "
             "physical sample, not a screen render."),
            ("Solvent tested.", "Every finish is tested against your concentrate and alcohol grade "
             "before the production order is placed."),
            ("Six-colour screen.", "Multi-pass silk-screen registration is checked on every setup, "
             "so fine detail does not drift across the run."),
            ("Masked and selective.", "Partial-coverage effects, gradients and windows are achieved "
             "with tooled masks rather than hand work that varies unit to unit."),
            ("Rejects caught inline.", "Decorated units are inspected before filling, so a cosmetic "
             "defect never reaches a filled bottle."),
        ])]), "Finishes and techniques"),

    section("faq-page", "\n\n".join([
        title_row("Decoration Path", "How A Finish Gets Approved", "contact.html", "Start a Brief"),
        accordion("bdStages", [
            ("01. Reference and target",
             "You supply a Pantone, a physical sample or a render. We tell you what is achievable "
             "on your chosen glass and where the reference will need to shift."),
            ("02. Sample decoration",
             "A small set of bottles is decorated to the target so colour, coverage and print "
             "registration can be judged in the hand rather than on a screen."),
            ("03. Compatibility soak",
             "Decorated samples are filled with your concentrate and held for the agreed period to "
             "check for crazing, adhesion loss and colour drift."),
            ("04. Written approval",
             "You approve a retained physical reference. That sample becomes the standard the "
             "production run is inspected against."),
            ("05. Tooling and setup",
             "Screens, masks and foil dies are prepared. Setup is proofed and signed before the "
             "run releases."),
            ("06. Run and inline inspection",
             "Units are inspected against the retained reference through the run, and rejects are "
             "pulled before filling."),
        ])]), "Decoration stages"),

    section("industries-details-page", industries_block(
        "What We Decorate",
        "Decoration is not limited to the bottle. Caps, collars, pumps and secondary components all "
        "carry finish, and a range only reads as considered when they agree with each other.",
        "Components we finish",
        ["Fragrance bottles in flint, extra-flint and coloured glass",
         "Caps and collars in Surlyn, Zamak and moulded resin",
         "Pump shrouds and actuator sleeves",
         "Candle vessels and diffuser bottles",
         "Travel atomiser bodies and refill cases",
         "Sampling vials for discovery sets"],
        "Where a component comes from your own supplier, we inspect it on goods-in and confirm it "
        "will take the finish before it enters the decoration queue.",
        "images/project-img2.webp",
        "Detail of a hot foil stamped and screen printed fragrance bottle",
        TAGS), "Components decorated"),

    partner_strip("Finishes verified against", "five", "compliance frameworks"),
    related("bottle-decoration"),
    cta("Send us a Pantone and a bottle. We will send back something worth putting on a shelf.",
        "Discuss a Finish", "contact.html", "Decoration CTA"),
])

print("generated: private-label-solutions, packaging-filling, bottle-decoration")
