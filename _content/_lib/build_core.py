#!/usr/bin/env python3
"""Generate the about and manufacturing pages (the two heavily anchored pages)."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import (section, hero_split, two_lists, img_text, key_features,
                 why_choose, accordion, industries_block, partner_strip,
                 service_grid, cta, title_row, team_grid, write)

TAGS = [("Fine Fragrances", "fine-fragrances.html"),
        ("Oriental Fragrances", "oriental-fragrances.html"),
        ("Home &amp; Lifestyle", "home-lifestyle.html"),
        ("Personal Care", "cosmetics-personal-care.html"),
        ("Private Label", "private-label.html")]

# ------------------------------------------------------------------------ about
write("about", [
    section("service-details-page", hero_split(
        "images/about.webp",
        "Perfumer assessing a fragrance blend at the First Perfumes laboratory bench",
        "Founded In 2006, On A Single Production Line",
        ["First Perfumes Ind LLC was founded in 2006 by Mr. Abdullah Karji with one production line "
         "in Jebel Ali and a conviction that the UAE could manufacture fragrance to a standard the "
         "region was then importing. Nearly two decades later the facility integrates development, "
         "compounding, filling, decoration, packaging and quality control under one roof.",
         "What has not changed is the reason clients stay: a formula approved here can be reproduced "
         "here years later, from records we kept, by people who were in the room the first time."],
        eager=True), "Our story", anchor="our-story"),

    section("service-details-page", "\n\n".join([
        img_text("images/legacy-perfumer.webp",
                 "Traditional perfumery materials alongside modern laboratory glassware",
                 "Heritage That Informs The Method",
                 ["The business grew out of a regional perfumery tradition where oud, amber and "
                  "resins are judged by nose against a retained reference rather than by "
                  "specification sheet. That habit stayed with us as the equipment modernised. "
                  "Every incoming lot of a critical material is still evaluated on the blotter "
                  "before it is approved into stock, and every approved formula still has a "
                  "physical reference sample held against it.",
                  "It is an unfashionable amount of manual judgement to keep in an automated plant. "
                  "It is also the reason a reorder in 2026 smells like the one approved in 2019."],
                 flip=True),
        key_features(["Founded 2006", "Jebel Ali, Dubai",
                      "One Integrated Site", "Retained References"])]),
        "Our heritage", anchor="our-heritage"),

    section("service-details-page", two_lists(
        "Where We Are Going, And How We Get There",
        "Our vision",
        ["To be the manufacturing partner the region's fragrance brands build on",
         "To prove that integrated production beats a chain of specialist suppliers",
         "To make sustainable packaging the default rather than the premium option",
         "To keep formulation judgement in human hands, supported by instruments",
         "To grow capacity without diluting the standard applied to any batch",
         "To remain a manufacturer brands can name without embarrassment"],
        "Our mission",
        ["Develop and produce fragrance and cosmetics to international standards",
         "Hold one quality standard across every volume and every client",
         "Keep formulas, records and references retrievable for the long term",
         "Register products properly for the markets they are sold into",
         "Reduce measured waste per batch year on year",
         "Tell clients the truth about timelines before they commit to them"]),
        "Vision and mission", anchor="vision-mission"),

    section("service-details-page", "\n\n".join([
        two_lists("What We Hold Ourselves To",
                  "In the laboratory",
                  ["Judgement over shortcuts, even when a shortcut would ship faster",
                   "Every claim tested before it reaches a specification sheet",
                   "Materials evaluated by origin and lot, not just by price",
                   "Stability proven at the concentration that will actually ship"],
                  "On the floor and with clients",
                  ["One standard of batch record regardless of order size",
                   "Bad news delivered early, while it is still cheap to act on",
                   "Client formulas treated as client property, without exception",
                   "Sustainability specified in writing, not claimed in marketing"]),
        why_choose([
            ("Integrity of the formula.", "A client's formula is theirs. We do not reuse an "
             "accord developed for one brand in a product for another."),
            ("Honest timelines.", "We would rather lose an order to a realistic schedule than "
             "win it on a date we know we cannot hold."),
            ("Traceability by default.", "Every batch traces to its materials and its records "
             "without anyone having to go looking."),
            ("Sustainability as specification.", "Recyclability is written into the packaging "
             "spec, with the trade-offs stated where a client chooses otherwise."),
            ("People who stay.", "The perfumers and line supervisors who approved your first "
             "batch are generally the ones running your fifth."),
            ("Standards that do not flex.", "A thirty-litre exclusive run gets the same release "
             "testing as a four-hundred-kilo commercial batch."),
        ])]), "Our values", anchor="our-values"),

    section("service-details-page", "\n\n".join([
        title_row("Leadership", "The People Accountable For It", "our-team.html", "Meet the Team"),
        "<!-- Placeholder team members: names and photographs are stand-in content "
        "for the client to replace before launch. -->",
        team_grid([
            ("images/team-img.webp", "A. Karji", "Founder &amp; Managing Director",
             "Portrait placeholder for the founder and managing director"),
            ("images/team-img2.webp", "Head of Perfumery", "Master Perfumer",
             "Portrait placeholder for the head of perfumery"),
            ("images/team-img3.webp", "Head of Operations", "Production Director",
             "Portrait placeholder for the head of operations"),
            ("images/team-img4.webp", "Head of Quality", "QA &amp; Regulatory Director",
             "Portrait placeholder for the head of quality and regulatory affairs"),
        ])]), "Leadership", anchor="leadership"),

    section("industries-details-page", industries_block(
        "Nearly Two Decades, In Numbers",
        "The figures below are the ones we are asked for most often in a first conversation. They "
        "are placeholder values for the client to confirm against current records before launch.",
        "Where the business stands today",
        ["Founded in 2006 and operating continuously since",
         "One integrated facility in Jebel Ali Industrial First, Dubai",
         "Fine fragrance, oriental, home and personal care lines",
         "Registered for UAE, EU, UK and US market supply",
         "Batch volumes from thirty litres to full commercial production",
         "Long-term programmes with brands across the GCC and beyond"],
        "If you need verified figures for a tender or a due diligence pack, ask and we will supply "
        "them with the supporting documentation rather than a marketing number.",
        "images/facility-jebel-ali.webp",
        "The First Perfumes manufacturing facility in Jebel Ali Industrial First, Dubai",
        TAGS), "By the numbers"),

    partner_strip("Operating under", "five", "international standards"),
    cta("Come and see the floor. Most decisions get easier after a walk through it.",
        "Arrange a Visit", "contact.html", "About CTA"),
])

# ---------------------------------------------------------------- manufacturing
MFG = [
    ("facility", "images/facility-jebel-ali.webp",
     "Exterior of the First Perfumes facility in Jebel Ali Industrial First, Dubai",
     "Our Manufacturing Facility",
     ["The plant sits in Jebel Ali Industrial First, purpose-built so that development, compounding, "
      "filling, decoration, packaging and quality control occupy one continuous floor. Nothing in "
      "production leaves the site between stages, which removes the transfer steps where damage, "
      "contamination and paperwork gaps usually occur.",
      "Layout matters more than it sounds. A perfumer can carry a trial to the compounding hall in "
      "under a minute, and a quality issue on the line can be looked at by the person who wrote the "
      "formula the same hour it is found."], False),
    ("research-development", "images/rnd-lab.webp",
     "Analytical instruments and glassware in the First Perfumes R&D laboratory",
     "Research &amp; Development",
     ["The R&amp;D laboratory develops fragrance accords and cosmetic formulations, maintains our "
      "natural extract and synthetic material libraries, and runs the stability and compatibility "
      "programmes that decide whether a formula is fit to scale.",
      "It also handles reformulation: matching a legacy composition whose original supplier is gone, "
      "or rebuilding a formula around a material that has become restricted. That work is "
      "unglamorous and it is a large part of what the laboratory actually does."], True),
    ("fragrance-creation", "images/perfume-compounding.webp",
     "Perfumer weighing materials against a formula sheet during accord creation",
     "Fragrance Creation",
     ["Accords are built in house by our own perfumers rather than brokered to an external house. "
      "Briefs are interpreted against the market, the price point and the base the composition will "
      "eventually live in, because an accord designed in isolation from its medium usually "
      "disappoints once it meets one.",
      "Submissions are numbered and logged. A composition approved years ago can be reproduced from "
      "its weight sheet without reverse-engineering anything."], False),
    ("production-process", "images/production-lines.webp",
     "Automated compounding and filling lines running a commercial batch",
     "Production Process",
     ["Compounding is automated and batch-controlled, with maceration, cold filtration and settling "
      "held for the period each composition requires. Filling supports glass and PET across crimp, "
      "screw and press-on closures, with fill weight and torque verified through the run.",
      "Volumes run from thirty-litre exclusive batches to full commercial production on the same "
      "equipment, so a product that succeeds does not need reformulating to scale."], True),
    ("quality-control", "images/quality-lab.webp",
     "Analyst performing release testing in the quality control laboratory",
     "Quality Control",
     ["Quality control tests incoming raw materials, in-process batches and finished goods against "
      "ISO 22716:2007 cosmetics GMP and US FDA registered standards. Every batch is released against "
      "a retained reference sample before it is permitted to ship.",
      "Records are the point. Batch records, material traceability to supplier lot and release "
      "certificates are retained and available to clients on request, including for audit."], False),
    ("packaging-filling", "images/packaging-unit.webp",
     "Secondary packaging and assembly running in the packaging hall",
     "Packaging &amp; Filling",
     ["Primary filling and secondary assembly run on the same floor as compounding. Cartoning, "
      "cellophane wrapping, insert forming, labelling, batch coding and case packing are all handled "
      "in house, with transit testing against the route a consignment will actually travel.",
      "Packaging specifications default to recyclable mono-material cartons, and component waste is "
      "measured per batch so reduction targets rest on recorded numbers."], True),
    ("capabilities", "images/sustainability-env.webp",
     "Energy-efficient equipment and recyclable materials in the sustainable assembly area",
     "Capabilities",
     ["Taken together the site covers accord development, cosmetic formulation, automated "
      "compounding, alcohol and oil-based filling, candle pouring, diffuser assembly, bottle "
      "lacquering and printing, secondary packaging, market registration and export documentation.",
      "The sustainability programme runs across all of it: energy-efficient equipment, recyclable "
      "material defaults and per-batch waste measurement, reported rather than asserted."], False),
]

mfg_parts = [section("service-details-page", hero_split(
    "images/facility-jebel-ali.webp",
    "The First Perfumes manufacturing facility in Jebel Ali Industrial First, Dubai",
    "Every Key Function, One Continuous Floor",
    ["Most fragrance production is a relay: a house develops the accord, a filler bottles it, a "
     "decorator finishes the glass and a packer boxes it, each in a different building. Every "
     "handover is a chance for a specification to drift and for accountability to blur.",
     "Our facility in Jebel Ali was built to remove those handovers. Development, compounding, "
     "filling, decoration, packaging and quality control sit on one floor, under one set of batch "
     "records, with one team accountable end to end."],
    eager=True), "Facility overview")]

for aid, img, alt, h3, paras, flip in MFG:
    mfg_parts.append(section("service-details-page",
                             img_text(img, alt, h3, paras, flip=flip),
                             h3.replace("&amp;", "and"), anchor=aid))

mfg_parts += [
    section("service-details-page", "\n\n".join([
        two_lists("Standards We Manufacture To",
                  "Certifications and frameworks",
                  ["ISO 22716:2007 Cosmetics Good Manufacturing Practice",
                   "US FDA registered manufacturing facility",
                   "EU CPNP cosmetic product notification",
                   "UK SCPN cosmetic product notification",
                   "cGMP compliant production and documentation",
                   "IFRA conformity for every declared product category"],
                  "What that means in practice",
                  ["Written procedures for every production and cleaning step",
                   "Raw material traceability to supplier lot on every batch",
                   "Release testing against a retained reference before dispatch",
                   "Retained records available to clients for audit",
                   "Trained operators with documented competency",
                   "Deviations investigated and recorded, not quietly corrected"]),
        key_features(["ISO 22716", "US FDA Registered",
                      "CPNP &amp; SCPN", "IFRA Conform"])]),
        "Standards"),

    section("faq-page", "\n\n".join([
        title_row("Common Questions", "What Clients Ask About The Plant",
                  "faq.html", "All Questions"),
        accordion("mfgFaq", [
            ("What is your minimum order quantity?",
             "It depends on the format and the components, but exclusive runs from around thirty "
             "litres of concentrate are routine. Packaging minimums are usually the real "
             "constraint rather than the juice, because component suppliers set their own floors."),
            ("Can we visit the facility before committing?",
             "Yes, and we encourage it. Most technical conversations get shorter after a walk "
             "through the compounding hall and the quality control laboratory."),
            ("Who owns the formula you develop for us?",
             "You do. An accord developed for your brief is yours, recorded under your programme, "
             "and it is never reused in a product for another client."),
            ("How long does a programme take end to end?",
             "Eight to fourteen weeks from brief to approved formula is typical, with production "
             "and packaging lead times on top. Component sourcing is usually the longest pole."),
            ("Do you handle registration for export markets?",
             "Yes. Safety assessment, allergen declaration and notification for UAE, EU, UK and US "
             "markets are prepared as part of the programme."),
            ("Can we audit your records?",
             "Yes. Batch records, material traceability and release certificates for your "
             "programme are available on request."),
        ])]), "Facility FAQ"),

    partner_strip("Manufacturing under", "five", "international standards"),
    cta("The fastest way to understand the plant is to stand in it. Come and look.",
        "Arrange a Facility Visit", "contact.html", "Manufacturing CTA"),
]
write("manufacturing", mfg_parts)

print("generated: about, manufacturing")
