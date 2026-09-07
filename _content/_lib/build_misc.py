#!/usr/bin/env python3
"""Generate insights, article, team, careers, contact, faq, policies and 404."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import (section, hero_split, two_lists, img_text, key_features,
                 why_choose, accordion, industries_block, partner_strip,
                 service_grid, cta, title_row, team_grid, job_table,
                 longform, write)
from gen_extra import (blog_grid, pagination, article_body, contact_form,
                       contact_details, map_embed)

TAGS = [("Fine Fragrances", "fine-fragrances.html"),
        ("Oriental Fragrances", "oriental-fragrances.html"),
        ("Home &amp; Lifestyle", "home-lifestyle.html"),
        ("Personal Care", "cosmetics-personal-care.html"),
        ("Private Label", "private-label.html")]

UPDATED = "Last updated: 1 September 2026"

# ----------------------------------------------------------------- insights
POSTS = [
    ("images/blog-img.webp", "Sustainably sourced botanical raw materials for fragrance production",
     "Sustainability", "28 August, 2026",
     "Eco-friendly sourcing: what actually changes in the formula"),
    ("images/blog-img2.webp", "Regulatory documentation prepared for international cosmetic compliance",
     "Global Compliance", "14 August, 2026",
     "US FDA, ISO 22716 and EU CPNP: what each one really asks for"),
    ("images/blog-img3.webp", "Private label fragrance bottles prepared for a brand launch",
     "Private Label", "31 July, 2026",
     "From concept to shelf: the twelve weeks nobody plans for"),
    ("images/rnd-lab.webp", "Analyst running a stability trial in the laboratory",
     "Formulation", "17 July, 2026",
     "Why an accord that works on skin can fail in a candle"),
    ("images/quality-lab.webp", "Quality control analyst performing release testing",
     "Quality", "3 July, 2026",
     "Release testing: the checks that happen after you approve the sample"),
    ("images/bottle-decor.webp", "Decorated bottles after lacquering and silk-screen printing",
     "Formulation", "19 June, 2026",
     "Lacquer, alcohol and time: how finishes fail in month three"),
    ("images/packaging-unit.webp", "Sustainable packaging assembly in the packaging hall",
     "Sustainability", "5 June, 2026",
     "Mono-material cartons and the recyclability claim you can defend"),
    ("images/perfume-compounding.webp", "Compounding vessel during a commercial fragrance batch",
     "Quality", "22 May, 2026",
     "Maceration is not a delay, it is part of the formula"),
    ("images/compliance-global.webp", "Export documentation prepared for multiple markets",
     "Global Compliance", "8 May, 2026",
     "Registering one product for four markets without four timelines"),
]

write("insights", [
    section("home1-blog-section", "\n\n".join([
        title_row("From The Lab Floor", "Notes On Making Fragrance Properly",
                  "contact.html", "Talk to Us"),
        blog_grid(POSTS[:6], cols="col-lg-4 col-md-6"),
    ]), "Insights grid"),
    section("home1-blog-section", "\n\n".join([
        blog_grid(POSTS[6:], cols="col-lg-4 col-md-6"),
        pagination(3),
    ]), "Insights page two", spacing="mb-120"),
    partner_strip("Written by a team working under", "five", "international standards"),
    cta("Have a question these do not answer? Ask us directly.",
        "Ask the Team", "contact.html", "Insights CTA"),
])

# ----------------------------------------------------------- article details
write("article-details", [
    section("article-details-page", article_body(
        "First Perfumes Laboratory", "Fragrance Development Team", "28 August, 2026",
        "images/blog-img.webp",
        "Botanical raw materials and laboratory glassware during accord development",
        [
            ("h2", "A brief is a constraint document, not a wish list",
             ["The most useful fragrance brief we receive is rarely the most poetic one. It states "
              "the market, the retail price, the volume for the first order, the launch date and "
              "the format. Everything creative flows from those five numbers, because they decide "
              "what the concentrate can cost and therefore which materials are available at all.",
              "A brief that opens with a mood board and closes without a price point produces "
              "beautiful submissions that cannot be manufactured to margin. We would rather have "
              "the awkward conversation in week one."]),
            ("h3", "Stage one: intake and constraint setting",
             ["We establish the target market, the price point, the volume and the date. If the date "
              "is not achievable we say so immediately, because every downstream stage inherits that "
              "assumption. Component lead times, not formulation, are usually what makes a launch "
              "date impossible."]),
            ("h3", "Stage two: accord construction",
             ["Our perfumers build to the brief or match a reference you supply. Submissions are "
              "numbered and logged against your programme. Two to four rounds is typical; more than "
              "six usually means the brief itself was unresolved rather than the work being wrong."]),
            ("h3", "Stage three: base and medium testing",
             ["An accord is not a product until it has met its medium. The same composition behaves "
              "differently in an alcohol base, an oil concentrate, a candle wax and a diffuser "
              "solvent. We test the accord in the base it will actually ship in, at the "
              "concentration it will actually ship at."]),
            ("h3", "Stage four: stability and compatibility",
             ["Samples are held at elevated and ambient temperature and checked for colour drift, "
              "haze and separation. In parallel the juice is tested against the closure, gasket and "
              "bottle. Gasket swell and lacquer crazing are the two failures that most often surface "
              "late, and both are cheap to catch here and expensive to catch in a container."]),
            ("h3", "Stage five: compliance documentation",
             ["IFRA conformity is calculated for the declared category, allergens are declared for "
              "EU CPNP and UK SCPN labelling, and a safety data sheet and transport classification "
              "are prepared. This runs alongside stability rather than after it."]),
            ("h3", "Stage six: pilot batch and sign-off",
             ["A pilot runs in the same hall as the commercial batch so maceration, filtration and "
              "settling behaviour are recorded at something close to real scale. You approve against "
              "a retained physical reference, and that sample becomes the standard every future "
              "batch is released against."]),
            ("h2", "Twelve weeks, and where they actually go",
             ["Eight to fourteen weeks from brief to approved formula is the honest range. Roughly "
              "a third of that is submission rounds, a third is stability holding time that cannot "
              "be compressed, and a third is compliance and pilot work. Production and packaging "
              "lead times sit on top of it.",
              "The single most common way a programme slips is a brief that changes in week six. "
              "The second is component sourcing that started too late."]),
        ],
        "Stability is a formulation decision, not a packaging one. If the juice is wrong, no "
        "closure will save it.",
        TAGS), "Article body"),

    section("home1-blog-section", "\n\n".join([
        title_row("Related Reading", "More From The Lab Floor", "insights.html", "All Insights"),
        blog_grid(POSTS[3:6], cols="col-lg-4 col-md-6"),
    ]), "Related articles"),

    cta("Ready to write a brief? We will tell you what is missing from it.",
        "Start Your Brief", "contact.html", "Article CTA"),
])

# ------------------------------------------------------------------ our team
write("our-team", [
    section("service-details-page", hero_split(
        "images/team-img.webp",
        "Member of the First Perfumes production team on the compounding floor",
        "Perfumers, Chemists And Line Engineers",
        ["A fragrance is made by a laboratory, a compounding hall, a filling line and a quality "
         "function that all have to agree. The people below span those four, and most of them have "
         "been here long enough that the person who approved your first batch is still the person "
         "running your fifth.",
         "That continuity is the least glamorous thing about this business and the one clients "
         "mention most often when they explain why they stayed."],
        eager=True), "Team overview"),

    section("home3-team-section", "\n\n".join([
        title_row("The Team", "Who You Will Actually Work With", "careers.html", "Join Us"),
        "<!-- PLACEHOLDER CONTENT: the names, roles and photographs below are stand-in\n"
        "     content for the client to replace with real team members before launch. -->",
        team_grid([
            ("images/team-img.webp", "A. Karji", "Founder &amp; Managing Director",
             "Portrait placeholder for the founder and managing director"),
            ("images/team-img2.webp", "Team Member Two", "Master Perfumer",
             "Portrait placeholder for the master perfumer"),
            ("images/team-img3.webp", "Team Member Three", "Production Director",
             "Portrait placeholder for the production director"),
            ("images/team-img4.webp", "Team Member Four", "QA &amp; Regulatory Director",
             "Portrait placeholder for the quality and regulatory director"),
            ("images/team-img5.webp", "Team Member Five", "Senior Perfumer",
             "Portrait placeholder for a senior perfumer"),
            ("images/team-img6.webp", "Team Member Six", "Laboratory Manager",
             "Portrait placeholder for the laboratory manager"),
            ("images/team-img7.webp", "Team Member Seven", "Packaging Lead",
             "Portrait placeholder for the packaging lead"),
            ("images/team-img8.webp", "Team Member Eight", "Compliance Specialist",
             "Portrait placeholder for the compliance specialist"),
        ])]), "Team grid"),

    section("service-details-page", "\n\n".join([
        two_lists("How The Floor Is Organised",
                  "Laboratory and development",
                  ["Perfumers who build and match accords in house",
                   "Application chemists for cosmetic and home formats",
                   "Stability and compatibility technicians",
                   "Regulatory specialists preparing market notifications"],
                  "Production and quality",
                  ["Compounding operators running batch-controlled vessels",
                   "Filling line supervisors across glass, PET and wax",
                   "Decoration technicians for lacquer, screen and foil",
                   "Quality control analysts performing release testing"]),
        key_features(["In-House Perfumery", "Application Chemistry",
                      "Line Supervision", "Release Testing"])]),
        "How the floor works"),

    cta("We are usually hiring for at least one of these disciplines.",
        "See Open Roles", "careers.html", "Team CTA"),
])

# ------------------------------------------------------------------- careers
write("careers", [
    section("service-details-page", hero_split(
        "images/team-area-bg.webp",
        "The First Perfumes team at work in the Jebel Ali production facility",
        "We Hire For Curiosity And Precision, In That Order",
        ["Fragrance manufacturing rewards people who are interested in why something behaves the "
         "way it does and disciplined enough to write it down afterwards. Most of what we do can be "
         "taught; neither of those two traits can.",
         "Roles here are hands-on. A perfumer walks trials to the compounding hall, a quality "
         "analyst talks to the line supervisor directly, and nobody is more than a short walk from "
         "the product they are responsible for."],
        eager=True), "Careers intro"),

    section("service-details-page", "\n\n".join([
        two_lists("What We Offer",
                  "The work",
                  ["A fully integrated site, so you see a product end to end",
                   "Training against documented competency, not by osmosis",
                   "Real ownership of a discipline rather than a narrow task",
                   "Exposure to international regulatory frameworks"],
                  "The package",
                  ["Competitive salary reviewed annually",
                   "Medical cover in line with UAE requirements",
                   "Annual leave and return flight entitlement",
                   "Support toward relevant professional certification"]),
        key_features(["Integrated Site", "Documented Training",
                      "Real Ownership", "Certification Support"])]),
        "What we offer"),

    section("service-details-page", "\n\n".join([
        title_row("Open Roles", "Where We Are Hiring Right Now",
                  "contact.html", "Send a CV"),
        "<!-- PLACEHOLDER CONTENT: replace these openings with your live vacancies. -->",
        job_table([
            ("Junior Perfumer", "01", "Full time"),
            ("Quality Control Analyst", "02", "Full time"),
            ("Production Line Supervisor", "01", "Full time"),
            ("Regulatory Affairs Specialist", "01", "Full time"),
            ("Packaging Designer", "01", "Contract"),
            ("Maintenance Technician", "02", "Full time"),
        ])]), "Job openings"),

    section("faq-page", "\n\n".join([
        title_row("Applying", "How Hiring Works Here", "contact.html", "Get in Touch"),
        accordion("careersFaq", [
            ("How do I apply?",
             "Send your CV and a short note about which discipline interests you to "
             "info@firstperfumes.com, or use the contact form and select the relevant enquiry type. "
             "We read everything that arrives."),
            ("Do I need fragrance industry experience?",
             "For perfumery and regulatory roles, usually yes. For laboratory, production and "
             "maintenance roles we regularly hire from adjacent industries — food, pharmaceutical "
             "and cosmetics manufacturing all transfer well."),
            ("What does the process look like?",
             "A screening conversation, a technical discussion with the relevant lead, and for most "
             "roles a practical assessment on site. We aim to complete it inside three weeks."),
            ("Do you sponsor visas?",
             "For most full-time roles, yes, in line with UAE employment regulations. This is "
             "confirmed at offer stage rather than assumed."),
            ("I do not see my role listed. Should I still write?",
             "Yes. We keep speculative applications on file and a reasonable number of our hires "
             "started as one."),
        ])]), "Careers FAQ"),

    cta("If the work sounds like yours, we would like to read your CV.",
        "Apply Now", "contact.html", "Careers CTA"),
])

# ------------------------------------------------------------------- contact
write("contact", [
    section("contact-page-top", "\n\n".join([
        title_row("Get In Touch", "Tell Us What You Want To Make", None),
        contact_details()]), "Contact details"),
    section("contact-page-top", contact_form([
        "Private label programme", "Custom fragrance development",
        "Cosmetics and personal care", "Packaging and decoration",
        "Facility visit", "Careers",
    ]), "Contact form"),
    section("service-details-page", map_embed(), "Location map"),
    section("faq-page", "\n\n".join([
        title_row("Before You Write", "Things Worth Including", "faq.html", "Read the FAQ"),
        accordion("contactFaq", [
            ("What should a first enquiry include?",
             "Your target market, an approximate retail price, the volume you expect for a first "
             "order and a launch date if you have one. Those four things let us answer usefully "
             "instead of asking four more questions."),
            ("How quickly will you reply?",
             "Within one business day. Our working week is Sunday to Thursday, 8:00 to 18:00 Gulf "
             "Standard Time."),
            ("Can we visit the facility?",
             "Yes, and we recommend it. Say so in your enquiry and we will propose some dates."),
            ("Do you sign non-disclosure agreements?",
             "Routinely. Send yours with the enquiry, or ask for ours."),
        ])]), "Contact FAQ"),
])

# ----------------------------------------------------------------------- faq
write("faq", [
    section("faq-page", "\n\n".join([
        title_row("Getting Started", "Before You Commit To Anything",
                  "contact.html", "Ask a Question"),
        accordion("faqStart", [
            ("What is your minimum order quantity?",
             "Exclusive runs from around thirty litres of concentrate are routine. In practice the "
             "packaging minimum is usually the binding constraint, because glass and carton "
             "suppliers set their own floors, often in the low thousands of units."),
            ("How long does a full programme take?",
             "Eight to fourteen weeks from brief to approved formula, plus production and packaging "
             "lead times. Component sourcing is the longest pole in most programmes."),
            ("Can we get samples before committing?",
             "Yes. Development submissions come at 30 ml, 100 ml and 500 ml. Sampling rounds are "
             "part of every development programme rather than an extra."),
            ("Who owns the formula?",
             "You do. An accord developed to your brief is recorded under your programme, and it is "
             "never reused in a product for another client."),
        ])]), "Getting started"),

    section("faq-page", "\n\n".join([
        title_row("Production", "How Manufacturing Actually Runs", None),
        accordion("faqProd", [
            ("What volumes can you run?",
             "From thirty-litre exclusive batches to full commercial production on the same "
             "equipment, so a product that succeeds does not need reformulating to scale."),
            ("Can you match an existing fragrance?",
             "Yes. Matching and reformulation of legacy compositions is routine work for the "
             "laboratory, including rebuilding around materials that have become restricted."),
            ("Do you supply packaging, or do we?",
             "Either. We source glass, closures and cartons to specification, or receive components "
             "you have sourced and inspect them on goods-in against an agreed standard."),
            ("What testing happens before a batch ships?",
             "Stability and compatibility during development; fill weight, closure torque and coding "
             "checks through the run; and release testing against a retained reference sample before "
             "dispatch."),
        ])]), "Production"),

    section("faq-page", "\n\n".join([
        title_row("Compliance", "Standards And Registration", None),
        accordion("faqComp", [
            ("Which standards do you manufacture to?",
             "ISO 22716:2007 cosmetics GMP, as a US FDA registered facility, with cGMP compliant "
             "documentation and IFRA conformity for every declared product category."),
            ("Do you handle EU and UK registration?",
             "Yes. Safety assessment, allergen declaration and CPNP or SCPN notification are "
             "prepared as part of the programme. Nothing ships to those markets without its "
             "notification reference in hand."),
            ("Can we audit your records?",
             "Yes. Batch records, raw material traceability to supplier lot and release certificates "
             "for your programme are available on request."),
            ("What about sustainability claims?",
             "Packaging specifications state material and recyclability in the destination market, "
             "and component waste is measured per batch. We will not sign off a claim we cannot "
             "evidence."),
        ])]), "Compliance"),

    section("faq-page", "\n\n".join([
        title_row("Logistics", "Getting Stock To Where It Sells", None),
        accordion("faqLog", [
            ("Do you arrange freight?",
             "On request. Consignments are palletised to your destination standard, wrapped, "
             "labelled and booked to your forwarder or ours, with the documentation destination "
             "customs will actually ask for."),
            ("What are your payment terms?",
             "Terms are agreed per programme and depend on volume and history. A deposit against "
             "component purchase is standard for a first order."),
            ("Can you hold stock for us?",
             "Short-term staging between production and dispatch is normal. Longer-term warehousing "
             "is arranged case by case."),
            ("What happens if a batch is rejected?",
             "It does not ship. Deviations are investigated and recorded, and we agree a remedy with "
             "you before anything moves."),
        ])]), "Logistics"),

    cta("Still unanswered? Ask us directly and we will reply within a business day.",
        "Ask Your Question", "contact.html", "FAQ CTA"),
])

# ------------------------------------------------------------------ policies
write("privacy-policy", [
    section("service-details-page", longform([
        (None, ["<!-- Placeholder legal copy. Have your legal counsel review and adapt "
                "this before launch. -->" + UPDATED + "."]),
        ("Who we are", [
            "First Perfumes Ind LLC is a fragrance and cosmetics manufacturer registered in Dubai, "
            "United Arab Emirates, at Land Area Industrial First, Plot No 969, Jebel Ali. This "
            "policy explains how we handle personal data submitted through this website."]),
        ("What we collect", [
            "We collect only what you give us and what the site needs to function:",
            ["Contact details you submit through the enquiry form: name, company, email, phone",
             "The content of your enquiry, including any project details you choose to share",
             "Technical data such as IP address, browser type and pages visited, via analytics",
             "Any correspondence that follows from your enquiry"]]),
        ("Why we use it", [
            "Enquiry data is used to respond to you and, if a project proceeds, to administer it. "
            "Analytics data is used in aggregate to understand which pages are useful. We do not "
            "sell personal data, and we do not use enquiry data for unrelated marketing without "
            "asking you first."]),
        ("Lawful basis", [
            "We process enquiry data on the basis of your consent and, once a project begins, on "
            "the basis of performing a contract. Analytics data is processed on the basis of "
            "legitimate interest in maintaining the website."]),
        ("How long we keep it", [
            "Enquiries that do not lead to a project are retained for twenty-four months and then "
            "deleted. Records relating to an active or completed manufacturing programme are "
            "retained for as long as commercial and regulatory obligations require."]),
        ("Who we share it with", [
            "We share personal data only with service providers who help us operate — website "
            "hosting, email and analytics — and only to the extent needed. We do not share enquiry "
            "content with other clients or with third parties for their own purposes."]),
        ("International transfer", [
            "Some service providers process data outside the United Arab Emirates. Where that "
            "happens we take reasonable steps to ensure an appropriate level of protection."]),
        ("Your rights", [
            "You may ask us to:",
            ["Confirm what personal data we hold about you",
             "Provide a copy of that data",
             "Correct data that is inaccurate or incomplete",
             "Delete data where we have no continuing obligation to retain it",
             "Withdraw consent to further contact at any time"]]),
        ("Cookies", [
            "This site uses cookies necessary for it to function and, where enabled, analytics "
            "cookies. You can block cookies in your browser settings; the site will still work, "
            "though some conveniences may not."]),
        ("Contact", [
            "For any request under this policy, write to info@firstperfumes.com or call "
            "+971 4 221 1787. We aim to respond within thirty days."]),
    ]), "Privacy policy"),
    cta("Questions about how we handle your data? Ask.",
        "Contact Us", "contact.html", "Privacy CTA"),
])

write("terms-conditions", [
    section("service-details-page", longform([
        (None, ["<!-- Placeholder legal copy. These are WEBSITE terms only, not supply or "
                "manufacturing contract terms. Have your legal counsel review before "
                "launch. -->" + UPDATED + "."]),
        ("Acceptance", [
            "By using this website you accept these terms. If you do not accept them, please do "
            "not use the site. These terms govern use of the website only. Manufacturing, supply "
            "and private label work are governed by a separate written agreement."]),
        ("About the content", [
            "Information on this site describes our capabilities in general terms. Product "
            "specifications, lead times, volumes and prices shown or implied here are indicative "
            "and do not constitute an offer. Nothing on this site forms part of any contract "
            "unless repeated in a signed agreement."]),
        ("Intellectual property", [
            "The content of this site — text, images, layout, logos and marks — belongs to First "
            "Perfumes Ind LLC or is used with permission. You may view and print pages for your "
            "own reference. You may not republish, sell or systematically extract content without "
            "written permission."]),
        ("Acceptable use", [
            "You agree not to:",
            ["Use the site in any unlawful or fraudulent way",
             "Attempt to gain unauthorised access to the site or its infrastructure",
             "Introduce malicious code or interfere with the site's operation",
             "Scrape or harvest content or contact details in bulk",
             "Misrepresent your identity when submitting an enquiry"]]),
        ("Third-party links", [
            "Where we link to external sites, we do so for convenience. We do not control them and "
            "are not responsible for their content or their privacy practices."]),
        ("No warranty", [
            "The site is provided as is. While we take care to keep it accurate, we do not warrant "
            "that it is complete, current or uninterrupted."]),
        ("Limitation of liability", [
            "To the extent permitted by law, we are not liable for indirect or consequential loss "
            "arising from use of this website. Nothing in these terms limits liability that cannot "
            "lawfully be limited."]),
        ("Governing law", [
            "These terms are governed by the laws of the United Arab Emirates as applied in the "
            "Emirate of Dubai, and the courts of Dubai have exclusive jurisdiction."]),
        ("Changes", [
            "We may update these terms. The date at the top of this page shows when they were last "
            "revised, and continued use of the site after a change constitutes acceptance."]),
        ("Contact", [
            "Questions about these terms: info@firstperfumes.com, +971 4 221 1787."]),
    ]), "Terms and conditions"),
    cta("Need our supply terms rather than our website terms? Ask and we will send them.",
        "Request Supply Terms", "contact.html", "Terms CTA"),
])

write("support-policy", [
    section("service-details-page", longform([
        (None, ["<!-- Placeholder policy copy. Confirm the response targets below against "
                "what your team can actually commit to before launch. -->" + UPDATED + "."]),
        ("Who this covers", [
            "This policy applies to clients with an active or recently completed manufacturing "
            "programme. It sets out how to reach us, how quickly we aim to respond and how issues "
            "escalate if a first response does not resolve them."]),
        ("How to reach us", [
            "Every active programme has a named account contact who is your first point of call. "
            "For anything urgent, or if your contact is unavailable:",
            ["Email: info@firstperfumes.com, monitored Sunday to Thursday",
             "Telephone: +971 4 221 1787, 8:00 to 18:00 Gulf Standard Time",
             "In person: Land Area Industrial First, Plot No 969, Jebel Ali, Dubai"]]),
        ("Response targets", [
            "We aim to acknowledge within these targets during working hours. Acknowledgement means "
            "a named person owns it, not that it is resolved:",
            ["Critical — production stopped or a shipped batch in question: within 4 working hours",
             "High — an in-progress batch or an imminent dispatch affected: within 1 working day",
             "Normal — specification questions, documentation, scheduling: within 2 working days",
             "Low — general enquiries and future planning: within 5 working days"]]),
        ("Escalation", [
            "If a response does not resolve the issue, escalation runs from your account contact to "
            "the relevant department head, then to the production director, then to the managing "
            "director. You may ask to escalate at any point without going through each step."]),
        ("Changes to a live formula", [
            "Any change to an approved formula, component or specification is handled as a written "
            "change request. We will confirm the technical impact, whether re-testing or "
            "re-notification is required, and the effect on lead time before the change is "
            "actioned. Nothing changes on a verbal instruction."]),
        ("Non-conformance and complaints", [
            "If a delivered batch does not meet its specification, tell us as soon as you find it "
            "and retain the affected units. We will:",
            ["Acknowledge and assign an owner within one working day",
             "Retrieve the batch record and retained reference sample",
             "Investigate and give you a written finding",
             "Agree a remedy — replacement, rework or credit — before acting",
             "Record the deviation and any corrective action taken"]]),
        ("Documentation requests", [
            "Batch records, certificates of analysis, material traceability and release "
            "certificates for your programme are available on request, normally within two working "
            "days. Audit visits are arranged by appointment."]),
        ("What this policy does not cover", [
            "This is a service commitment, not a warranty. Contractual remedies, liability and "
            "warranty terms are governed by your signed supply agreement."]),
    ]), "Support policy"),
    cta("Already working with us and need something? Your account contact is the fastest route.",
        "Contact Support", "contact.html", "Support CTA"),
])

# ----------------------------------------------------------------------- 404
write("404", [
    section("service-details-page", "\n\n".join([
        """<div class="row">
    <div class="col-lg-8 fade_anim" data-delay=".2">
        <div class="details-content">
            <h3>The page you asked for is not here</h3>
            <p>It may have moved, been renamed, or never existed. Nothing is broken on your side.</p>
            <p>If you followed a link from our own site and landed here, we would genuinely like to know — it means something needs fixing.</p>
        </div>
    </div>
</div>""",
        key_features(["Check the URL", "Use the Menu",
                      "Try the Links", "Ask Us"])]), "Not found"),

    service_grid("Popular Destinations", "Try One Of These Instead", None, [
        ("Our Expertise", "The six disciplines we run under one roof in Jebel Ali.",
         "expertise.html"),
        ("Manufacturing", "A tour of the facility, from R&amp;D through to packaging.",
         "manufacturing.html"),
        ("Products &amp; Solutions", "Fine, oriental, home and private label families.",
         "products.html"),
        ("About Us", "Founded 2006, and what has stayed the same since.", "about-us.html"),
        ("Insights", "Notes on formulation, compliance and manufacturing.", "insights.html"),
        ("Contact", "Tell us what you want to make.", "contact.html"),
    ], "Helpful links"),

    cta("Or just tell us what you were looking for and we will point you at it.",
        "Get in Touch", "contact.html", "404 CTA"),
])

print("generated: insights, article-details, our-team, careers, contact, faq, "
      "privacy-policy, terms-conditions, support-policy, 404")
