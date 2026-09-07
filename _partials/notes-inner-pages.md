# Inner-page CSS inventory (Softro template) — First Perfumes Ind LLC

Every class name, data-attribute and element below was verified against
`css/style.css`, `css/site-fixes.css` and `js/custom.js` before being written down.
Long SVG path data is replaced with `<!-- icon svg -->`; wrapper elements and their
classes are kept verbatim.

**Nothing here is used on the homepage** (`_content/index.html`) except where noted.
The homepage only touches sections 05–12, 15, 17–19, 22–23, 25–27, 29, 31–33, 35–38.

---

## 0. Ground rules before you write any inner-page markup

### 0.1 Vendor JS is already loaded (see `_partials/chrome-bottom.html`)

`bootstrap.min.js` **is** loaded, so Bootstrap 5 `collapse` (accordion),
`tab` (nav-pills / nav-tabs) and `modal` all work with plain data-attributes —
no extra JS needed. Also available: jQuery 3.7.1, jQuery UI, Swiper,
`jquery.counterup.min.js` + `waypoints.js`, `wow.min.js`,
`jquery.nice-select.min.js`, `jquery.marquee.min.js` (unused by `custom.js`),
GSAP + ScrollTrigger + ScrollSmoother + SplitText, fancybox, three.js +
hover-effect.umd.js.

### 0.2 Shared primitives that inner pages reuse (all verified)

| Class | Where defined | Markup contract |
|---|---|---|
| `.section-title` (+ `.two` `.three` `.text-center` `.white-color` `.home3-section-title` `.home4-section-title`) | style.css:756+ | `> span`, `> h2`, `> p`; the `.three` variant expects `.left-content` / `.right-content` children |
| `.primary-btn1` | style.css:1110 | needs **two** `> span` children (the second is the hover-slide duplicate) |
| `.primary-btn2` (+ `.transparent`) | homepage uses it | `<span class="icon">svg</span><span class="content">Label</span><span class="icon two">svg</span>` |
| `.view-more-btn` (+ `.style-2`) | style.css:1351 | inline `<svg class="border">` then text; optional `.arrow` svg |
| `.form-inner` | style.css:1390 | `label` + `input` / `textarea` |
| `.form-inner2` | style.css:1463 | `.form-check > .form-check-input` + `.form-check-label` |
| `.pagination-area` | style.css:13690 | see §41b |
| `.breadcrumb-section` (+ `.style-2` `.style-3` `.style-4`) | style.css:13448 | `.breadcrumb-content > h1 + .breadcrumb-list + .para`; optional `.breadcrumd-title` (note the template's typo) wrapper with `.breadcrumb-social` |
| spacing utils | style.css:70+ | `pt-120 pb-120 pt-100 pb-100 pt-90 pb-90 pb-80 pb-65 pb-15 pb-10 mt-120 mb-120 mb-100 mb-60 mb-50 mb-40 mb-30` |

### 0.3 Two traps

1. **`.social-list` has no global rule.** It is only styled inside
   `.team-card .team-img .social-area`, `.article-details-page .post-author-meta .social-area-wrap .social-area`,
   `.careers-details-page .careers-details-sidebar .social-area-wrap .social-area`,
   `.team-details-page .team-details-content .name-social-area`,
   `.case-study-details-page .social-area`, `.footer-section`, and
   `.breadcrumb-section .breadcrumd-title .breadcrumb-social`.
   Drop a bare `.social-list` anywhere else and it renders as an unstyled `<ul>`.
   Icons are **Bootstrap Icons `<i>` elements** (`.bi-twitter-x` gets a special size).
2. **`.details-contnt-wrap` is misspelled in style.css** (missing the "e").
   Write it exactly as `details-contnt-wrap` or the article body loses all typography.

---

## 39. Portfolio Inner Page — `.nav-tab-page`

style.css:13774. A Bootstrap **pills** filter bar (rounded outline chips). This is
the *only* thing section 39 styles; the grid below it is your choice of card.

```html
<div class="nav-tab-page">
    <ul class="nav nav-pills" id="pills-tab" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active" id="pills-all-tab" data-bs-toggle="pill"
                    data-bs-target="#pills-all" type="button" role="tab"
                    aria-controls="pills-all" aria-selected="true">All</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="pills-edp-tab" data-bs-toggle="pill"
                    data-bs-target="#pills-edp" type="button" role="tab"
                    aria-controls="pills-edp" aria-selected="false">Eau de Parfum</button>
        </li>
    </ul>
</div>

<div class="tab-content" id="pills-tabContent">
    <div class="tab-pane fade show active" id="pills-all" role="tabpanel" aria-labelledby="pills-all-tab">
        <div class="row gy-4"><!-- cards --></div>
    </div>
    <div class="tab-pane fade" id="pills-edp" role="tabpanel" aria-labelledby="pills-edp-tab">
        <div class="row gy-4"><!-- cards --></div>
    </div>
</div>
```

IDs are author-chosen; only `data-bs-toggle="pill"` + `data-bs-target` are required.
`.tab-content` / `.tab-pane` come from Bootstrap, not style.css.

**Suits:** products category filter (4 categories), insights list category filter.

---

## 41. News & article page — `.blog-card2`

style.css:14062. The list card for the blog index. Distinct from the homepage's
`.blog-card`. Hover reveals a round `.icon` badge top-right of the image.

```html
<div class="col-md-6">
    <div class="blog-card2">
        <div class="blog-image-wrap">
            <a href="insight-detail.html" class="blog-img">
                <img src="images/blog-img.png" alt="" />
            </a>
            <div class="icon">
                <a href="insight-detail.html"><!-- icon svg --></a>
            </div>
        </div>
        <div class="blog-content-wrap">
            <ul class="blog-meta">
                <li><a href="#">Formulation</a></li>
                <li><!-- icon svg --> 12 March, 2026</li>
            </ul>
            <h2><a href="insight-detail.html">How UAE oud accords are built</a></h2>
        </div>
    </div>
</div>
```

Notes: `.blog-img` must be the element with `overflow:hidden` (it is `display:block`).
`.blog-image-wrap .icon` starts at `opacity:0` and appears on `.blog-image-wrap:hover`.
A `<canvas>` inside `.blog-img` is supported (hover-effect.umd.js distortion) but optional.

**Suits:** insights list.

### 41b. `.pagination-area` (style.css:13690 — lives just above section 39)

`justify-content: space-between`, so it expects **two** children: the numbered list
and the next/prev button group.

```html
<div class="pagination-area">
    <ul class="paginations">
        <li class="page-item active"><a href="#">1</a></li>
        <li class="page-item"><a href="#">2</a></li>
        <li class="page-item"><a href="#">3</a></li>
    </ul>
    <div class="paginations-button">
        <a href="#">Next Page <!-- icon svg --></a>
    </div>
</div>
```

`.page-item.active a` gets the primary fill. The `a` itself is the 36px circle —
do not nest a span inside it.

**Suits:** insights list, products list.

---

## 42. News & article sidebar — `.news-article-sidebar-area`

style.css:14195. A bordered 372px-max column. Contains a search box then any number
of `.single-widget` blocks. `.widget-title` is a heading element **outside**
`.single-widget` for the search, and **inside** each widget after that.

```html
<div class="col-lg-4">
    <div class="news-article-sidebar-area">
        <h4 class="widget-title">Search</h4>
        <div class="search-box">
            <input type="text" placeholder="Search here" />
            <button type="submit"><i class="bi bi-search"></i></button>
        </div>

        <div class="single-widget mb-30">
            <h4 class="widget-title">Categories</h4>
            <ul class="category-list">
                <li>
                    <a href="#"><span><!-- icon svg --> Formulation</span></a>
                </li>
                <li>
                    <a href="#"><span><!-- icon svg --> Regulatory</span></a>
                </li>
            </ul>
        </div>

        <div class="single-widget mb-30">
            <h4 class="widget-title">Recent Posts</h4>
            <div class="recent-post-widget mb-30">
                <div class="recent-post-img">
                    <img src="images/blog-img2.png" alt="" />
                </div>
                <div class="recent-post-content">
                    <h5><a href="insight-detail.html">Cold-blend stability testing</a></h5>
                    <a href="#">12 March, 2026</a>
                </div>
            </div>
        </div>

        <div class="single-widget">
            <h4 class="widget-title">Tags</h4>
            <ul class="tag-list">
                <li><a href="#">Oud</a></li>
                <li><a href="#">Attar</a></li>
            </ul>
        </div>
    </div>
</div>
```

Notes: the search `button` uses a Bootstrap Icons `<i>`, not an svg.
`.recent-post-content h5` *or* `h4` both work (both are in the selector list); the
plain `> a` directly under `.recent-post-content` is the date line.
`.recent-post-img img` is forced to 65x92.

**Suits:** insights list sidebar, article detail sidebar.

---

## 43. Service details page — `.service-details-page`

style.css:14489. The richest inner-page layout in the template and the closest
match to our service detail pages.

```html
<div class="service-details-page pt-120 pb-120">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="service-details-thumb-img">
                    <img src="images/service-details-thumb.png" alt="" />
                </div>
            </div>
        </div>

        <div class="service-details-content-wrap">
            <div class="service-details-title">
                <h2>Fragrance Development</h2>
            </div>

            <div class="details-content">
                <h3>Our Approach</h3>
                <p>Lead paragraph.</p>
                <ul class="approach-list">
                    <li>Brief intake and olfactive direction</li>
                    <li>Accord construction and bench trials</li>
                </ul>
            </div>

            <div class="service-details-img">
                <img src="images/service-details-img.png" alt="" />
            </div>

            <div class="key-features-area">
                <ul class="key-features-list">
                    <li>Custom Accords</li>
                    <li class="two">Stability Testing</li>
                    <li class="three">IFRA Compliance</li>
                    <li class="four">Scale-Up</li>
                </ul>
            </div>

            <div class="why-choose-area-wrap">
                <div class="why-choose-area">
                    <ul class="why-choose-list">
                        <li>
                            <div class="icon"><!-- icon svg --></div>
                            <div class="content">
                                <p><span>In-house lab.</span> Bench-to-batch under one roof.</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```

Notes:
- `.approach-list` is `list-style: disc` with `padding-left: 20px` — it is a real bullet list.
- `.key-features-list` is a 4-across tile grid; `li:nth-child(even)` is pushed down 55px
  on desktop. Plain text inside the `li` — no inner wrapper.
  **Ancestor chain:** `style.css` only styles this under the full
  `.service-details-page .service-details-content-wrap .key-features-area` chain, and eleven
  of the fourteen pages using the component did not have the `.service-details-content-wrap`
  link — so the tiles rendered as a bare bulleted list. `site-fixes.css` §10 restates the
  rule on `.key-features-area` alone, so **the chain no longer matters**; a
  `.container > .row > .col > .key-features-area` is enough.
  **Colours:** the template's `#e7e9fa` / `#fef7cf` / `#e9ffdd` pastels are overridden in
  `site-fixes.css` §10 to the site's neutrals — `li` and `li.three` are `#f6f4f3`, `li.four`
  is white, and `li.two` is the dark accent tile. Order your items so the one worth
  emphasising lands second.
- `.why-choose-list li` needs exactly `.icon` (svg) + `.content > p`; bold the lead-in
  with a `<span>` inside the `p`.
- `.why-choose-area-wrap::before` draws the vertical rule, so keep the extra wrapper.

**Suits:** all 6 service detail pages, manufacturing.

---

## 44. Industries details page — `.industries-details-page`

style.css:14700. A leaner sibling of §43 with a tag row + prev/next footer.

```html
<div class="industries-details-page pt-120 pb-120">
    <div class="container">
        <div class="industries-details-thumb-img">
            <img src="images/industries-details-thumb.png" alt="" />
        </div>

        <div class="industries-details-content-wrap">
            <div class="industries-details-title">
                <h2>Private Label Manufacturing</h2>
            </div>

            <div class="details-content">
                <p>Intro paragraph.</p>
                <h3>What we handle</h3>
                <ul>
                    <li><!-- icon svg --> Filling and crimping</li>
                    <li><!-- icon svg --> Secondary packaging</li>
                </ul>
                <p>Closing paragraph.</p>
            </div>

            <div class="industries-details-img">
                <img src="images/industries-details-img.png" alt="" />
            </div>

            <div class="tag-navigation-area">
                <ul class="tag-list">
                    <li><a href="#">Private Label</a></li>
                    <li><a href="#">OEM</a></li>
                </ul>
                <div class="details-navigation">
                    <a href="#" class="navigation-arrow"><!-- icon svg --></a>
                    <p>Contract Manufacturing</p>
                    <a href="#" class="navigation-arrow"><!-- icon svg --></a>
                </div>
            </div>
        </div>
    </div>
</div>
```

Notes: `.details-content ul li` here carries an inline `svg` as its bullet (the
selector `... ul li svg` exists), unlike §43's disc list.
`.navigation-arrow` is a 36px circle `<a>` containing only an svg.

**Suits:** products category pages, manufacturing.

---

## 45. Pricing plan page — `.pricing-card` / `.pricing-plan-tab-area` / `.pricing-plan-section`

style.css:14852. Three independent blocks.

```html
<div class="pricing-plan-section pt-120 pb-120">
    <div class="container">

        <!-- monthly/yearly toggle -->
        <div class="pricing-plan-tab-area">
            <div class="nav-area">
                <span>Monthly</span>
                <nav>
                    <div class="nav nav-tabs" id="nav-tab" role="tablist">
                        <button class="nav-link active" id="nav-monthly-tab" data-bs-toggle="tab"
                                data-bs-target="#nav-monthly" type="button" role="tab"
                                aria-controls="nav-monthly" aria-selected="true"></button>
                        <button class="nav-link" id="nav-yearly-tab" data-bs-toggle="tab"
                                data-bs-target="#nav-yearly" type="button" role="tab"
                                aria-controls="nav-yearly" aria-selected="false"></button>
                    </div>
                </nav>
                <span>Yearly <strong>Save 20%</strong></span>
            </div>
        </div>

        <div class="tab-content" id="nav-tabContent">
            <div class="tab-pane fade show active" id="nav-monthly" role="tabpanel" aria-labelledby="nav-monthly-tab">
                <div class="row gy-4">
                    <div class="col-lg-4">
                        <div class="pricing-card">
                            <div class="pricing-top">
                                <span>Starter</span>
                                <h2>$499 <sub><del>$699</del></sub></h2>
                                <p>Per project <span>excl. VAT</span></p>
                                <a href="#" class="pricing-btn"><span>Get Started</span></a>
                            </div>
                            <div class="pricing-content">
                                <h3>What's included</h3>
                                <ul>
                                    <li><!-- icon svg --> 3 accord trials</li>
                                    <li class="close"><!-- icon svg --> Custom packaging</li>
                                </ul>
                            </div>
                            <div class="pay-btn-area">
                                <a href="#" class="primary-btn1"><span>Enquire</span><span>Enquire</span></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- footnote strip -->
        <div class="contact-area">
            <h4>Need a custom volume? Talk to our team.</h4>
            <a href="contact.html" class="primary-btn1"><span>Contact Us</span><span>Contact Us</span></a>
        </div>
    </div>
</div>
```

Notes:
- The tab `.nav-link`s are 16x16 **dots** (no label text) — the "Monthly"/"Yearly"
  words are the `<span>`s either side of `<nav>`.
- `.pricing-card.two` and `.pricing-card.three` exist as background variants.
- `li.close` flips the tick svg to the "not included" colour.
- `.pricing-card .pricing-form .form-inner` also exists (input + textarea + `.primary-btn2`)
  if you want a quote form in the card instead of a price.
- `.pricing-btn` needs a single `> span` (it has its own `::before`/`::after` slide).

**Suits:** a "request a quote" tier block if we ever add one; otherwise the
`.contact-area` strip alone is reusable at the foot of expertise / products.

---

## 46. Contact page — `.contact-page-top` + `.contact-form-wrap.inner-contact-from`

style.css:15228 for the address blocks, style.css:5932 for the form.
**The form itself lives in section 12, not section 46** — `.contact-form-wrap` is
shared, and the inner-page skin is the `.inner-contact-from` modifier.

### 46a. Address / phone / email columns

```html
<div class="contact-page-top pt-120">
    <div class="container">
        <div class="contact-page-top-wrapper">
            <div class="row gy-4">
                <div class="col-lg-4 col-md-6">
                    <div class="single-contact">
                        <div class="content-top">
                            <h2>Dubai, UAE</h2>
                            <a href="#" class="view-map-btn">View Map</a>
                        </div>
                        <ul class="contact-list">
                            <li>
                                <div class="icon"><!-- icon svg --></div>
                                <div class="content">
                                    <a href="#">Warehouse 7, Al Quoz Industrial 3, Dubai</a>
                                </div>
                            </li>
                            <li>
                                <div class="icon"><!-- icon svg --></div>
                                <div class="content">
                                    <ul class="single-contact-list">
                                        <li><a href="tel:+97141234567">+971 4 123 4567</a></li>
                                        <li><a href="mailto:info@firstperfumes.ae">info@firstperfumes.ae</a></li>
                                    </ul>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

`.contact-list > li` is the flex row; the direct-child selector means
`.single-contact-list` (nested inside `.content`) is *not* affected by the row layout —
that is exactly why the nested list class exists.

### 46b. The contact form (verified markup contract)

```html
<div class="contact-form-wrap inner-contact-from">
    <form action="#" method="post">
        <div class="row gy-4">
            <div class="col-md-6">
                <div class="form-inner">
                    <label for="fullName">Full Name</label>
                    <input type="text" id="fullName" name="fullName" placeholder="Your name" />
                </div>
            </div>
            <div class="col-md-6">
                <div class="form-inner">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" placeholder="you@company.com" />
                </div>
            </div>
            <div class="col-lg-12">
                <div class="form-inner">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" placeholder="Tell us about your project"></textarea>
                </div>
            </div>

            <div class="col-lg-12">
                <div class="form-inner2">
                    <label>I'm interested in</label>
                    <ul>
                        <li>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="int1" />
                                <label class="form-check-label" for="int1">Private label</label>
                            </div>
                        </li>
                        <li>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="int2" />
                                <label class="form-check-label" for="int2">Custom fragrance</label>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="col-lg-12">
                <div class="form-inner2">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="consent" />
                        <label class="form-check-label" for="consent">
                            I agree to the <a href="privacy-policy.html">Privacy Policy</a>
                        </label>
                    </div>
                </div>
            </div>

            <div class="col-lg-12">
                <button type="submit" class="primary-btn1">
                    <span>Send Message <!-- icon svg --></span>
                    <span>Send Message <!-- icon svg --></span>
                </button>
            </div>
        </div>
    </form>
</div>
```

Hard requirements, all verified:
- `.form-inner2 > label` is only styled when it is a **direct child** of `.form-inner2`
  (style.css:5958) — the group heading. Checkbox labels must be `.form-check-label`.
- The checkbox-group markup is `.form-inner2 > ul > li > .form-check` (style.css:5983).
  A bare `.form-check` without the `ul/li` still works but loses the 25px gap row.
- Checked state pulls `images/check-icon.svg`; the `.inner-contact-from` skin swaps to
  `images/check-icon-white.svg`. **Both files must exist in `images/`.**
- `.inner-contact-from` sets the panel background to `#e2f6db` and inverts `.primary-btn1`
  to a dark fill. On our red-primary brand, check this against `site-fixes.css` before shipping.
- `.primary-btn1` **must** have two `<span>` children.

**Suits:** contact (both blocks), plus the form alone on service detail pages.

---

## 48. FAQ page — `.faq-wrap` + `.faq-page`

style.css:15697. This is a **standard Bootstrap 5 accordion**, restyled. It needs
the real `data-bs-toggle="collapse"` attributes, and the IDs are author-chosen —
style.css hard-codes no IDs at all.

```html
<div class="faq-page pt-120 pb-120">
    <div class="container">
        <div class="row">
            <div class="col-lg-4">
                <div class="nav-links-and-contact-area">
                    <div class="nav-links-wrapper">
                        <ul class="nav nav-pills" id="faq-tab" role="tablist">
                            <li class="nav-item" role="presentation">
                                <button class="nav-link active" id="faq-general-tab" data-bs-toggle="pill"
                                        data-bs-target="#faq-general" type="button" role="tab"
                                        aria-controls="faq-general" aria-selected="true">General</button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link" id="faq-orders-tab" data-bs-toggle="pill"
                                        data-bs-target="#faq-orders" type="button" role="tab"
                                        aria-controls="faq-orders" aria-selected="false">Orders &amp; MOQ</button>
                            </li>
                        </ul>
                    </div>
                    <div class="contact-area">
                        <div class="contact-img-area">
                            <img src="images/faq-contact.png" alt="" />
                            <div class="contact-title">
                                <h2>Still have a question?</h2>
                                <a href="contact.html" class="primary-btn1">
                                    <span>Contact Us <!-- icon svg --></span>
                                    <span>Contact Us <!-- icon svg --></span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-8">
                <div class="tab-content" id="faq-tabContent">
                    <div class="tab-pane fade show active" id="faq-general" role="tabpanel" aria-labelledby="faq-general-tab">
                        <div class="faq-wrap">
                            <div class="accordion" id="faqAccordionGeneral">
                                <div class="accordion-item">
                                    <h2 class="accordion-header" id="faqHeadingOne">
                                        <button class="accordion-button" type="button"
                                                data-bs-toggle="collapse" data-bs-target="#faqCollapseOne"
                                                aria-expanded="true" aria-controls="faqCollapseOne">
                                            What is your minimum order quantity?
                                        </button>
                                    </h2>
                                    <div id="faqCollapseOne" class="accordion-collapse collapse show"
                                         aria-labelledby="faqHeadingOne" data-bs-parent="#faqAccordionGeneral">
                                        <div class="accordion-body">
                                            Our standard MOQ is 1,000 units per SKU.
                                        </div>
                                    </div>
                                </div>

                                <div class="accordion-item">
                                    <h2 class="accordion-header" id="faqHeadingTwo">
                                        <button class="accordion-button collapsed" type="button"
                                                data-bs-toggle="collapse" data-bs-target="#faqCollapseTwo"
                                                aria-expanded="false" aria-controls="faqCollapseTwo">
                                            Do you handle IFRA compliance?
                                        </button>
                                    </h2>
                                    <div id="faqCollapseTwo" class="accordion-collapse collapse"
                                         aria-labelledby="faqHeadingTwo" data-bs-parent="#faqAccordionGeneral">
                                        <div class="accordion-body">Yes — every formulation ships with an IFRA certificate.</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

Accordion specifics, all verified:
- The `+` / `-` marker is a **Bootstrap Icons glyph injected via `::after`**
  (`content: "\f64d"` closed, `content: "\f2ea"` open, `font-family: bootstrap-icons`).
  `background-image: none` kills Bootstrap's default chevron. So `bootstrap-icons.min.css`
  must stay loaded (it is).
- The closed button relies on Bootstrap's `.collapsed` class — the rule is
  `.accordion-button:not(.collapsed)`. **The first/open item must NOT have `.collapsed`;
  every other button must.** Get this wrong and the open item shows the wrong glyph
  and the wrong 22px font size.
- `data-bs-parent` on `.accordion-collapse` gives single-open behaviour. Each tab pane
  needs its **own** accordion id.
- Variants: `.faq-wrap.two` (underlined rows, no side padding),
  `.faq-wrap.style-2` (borders between items, kills the `::after` vertical rule).
- `.faq-wrap::after` draws a 614px vertical rule at `left: -45px` — it is hidden below
  1400px. Use `.style-2` if you do not want it.
- If you don't need the left rail, `.faq-wrap` works standalone inside any column;
  `.faq-page` only styles the rail.

**Suits:** faq (whole page), plus a `.faq-wrap.style-2` block on service detail pages.

---

## 49. Careers Details Page — `.careers-details-page` + `.job-form-modal`

style.css:15984.

```html
<div class="careers-details-page pt-120 pb-120">
    <div class="container">
        <div class="careers-details-thumb-img mb-60">
            <img src="images/careers-details-thumb.png" alt="" />
        </div>
        <div class="row gy-5">
            <div class="col-lg-8">
                <div class="career-details-content">
                    <h2>Senior Perfumer</h2>
                    <p>Role summary.</p>
                    <span class="line-break"></span>
                    <h3>Responsibilities</h3>
                    <ul>
                        <li>Develop and refine fine-fragrance accords</li>
                        <li>Own bench-to-batch scale-up</li>
                    </ul>
                    <span class="line-break2"></span>
                </div>
            </div>

            <div class="col-lg-4">
                <div class="careers-details-sidebar">
                    <div class="sidebar-card">
                        <ul>
                            <li><span>Location</span><span class="style-2">Dubai, UAE</span></li>
                            <li><span>Job Type</span><span class="style-2">Full time</span></li>
                            <li><span>Experience</span><span class="style-2">5+ years</span></li>
                        </ul>
                        <div class="button-area">
                            <a href="#" class="primary-btn1" data-bs-toggle="modal" data-bs-target="#jobApplyModal">
                                <span>Apply Now</span><span>Apply Now</span>
                            </a>
                        </div>
                    </div>

                    <div class="social-area-wrap">
                        <div class="social-area-title">
                            <h4><a href="#">Share this job <!-- icon svg --></a></h4>
                        </div>
                        <div class="social-area">
                            <h5>Follow us</h5>
                            <ul class="social-list">
                                <li><a href="#"><i class="bi bi-linkedin"></i></a></li>
                                <li><a href="#"><i class="bi bi-twitter-x"></i></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

`.line-break` / `.line-break2` are empty spacer elements (20px / 10px) — keep them
as `<span>`s, they are `display:block` by rule only in `.article-details-page`, so
in careers give them a block-level tag such as `<div>` if you need guaranteed height.

### 49b. Application modal — `.job-form-modal` (Bootstrap modal)

```html
<div class="modal fade job-form-modal" id="jobApplyModal" tabindex="-1"
     aria-labelledby="jobApplyModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="jobApplyModalLabel">Apply for Senior Perfumer</h5>
                <button type="button" class="modal-close" data-bs-dismiss="modal" aria-label="Close">
                    <i class="bi bi-x"></i>
                </button>
            </div>
            <div class="modal-body">
                <form action="#" method="post" enctype="multipart/form-data">
                    <div class="single-info mb-30">
                        <h4 class="info-title">Personal details</h4>
                        <div class="form-inner mb-30">
                            <label for="applicantName">Full Name</label>
                            <input type="text" id="applicantName" name="name" placeholder="Your name" />
                        </div>
                        <div class="form-inner mb-30">
                            <label for="cv">Upload CV</label>
                            <div class="file-upload-area">
                                <div class="icon"><!-- icon svg --></div>
                                <input class="custom-upload" type="file" id="cv" name="cv" />
                                <div class="check-icon"><i class="bi bi-check"></i></div>
                            </div>
                        </div>
                        <div class="form-inner">
                            <label for="cover">Cover note</label>
                            <textarea id="cover" name="cover"></textarea>
                        </div>
                    </div>
                    <div class="form-inner2">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="applyConsent" />
                            <label class="form-check-label" for="applyConsent">
                                I agree to the <a href="privacy-policy.html">Privacy Policy</a>
                            </label>
                        </div>
                    </div>
                    <button type="submit" class="primary-btn1"><span>Submit</span><span>Submit</span></button>
                </form>
            </div>
        </div>
    </div>
</div>
```

Note the close button is `.modal-close` (**not** Bootstrap's `.btn-close`) with a
Bootstrap Icons `<i>`. `.file-upload-area` expects exactly `.icon` + `input.custom-upload` + `.check-icon`.

**Suits:** careers (job detail + apply modal).

---

## 50. Article details page — `.article-details-page` + `.comment-and-form-area`

style.css:16407. The full article body vocabulary. **`.details-contnt-wrap` is
spelled without the second "e" in style.css — copy it verbatim.**

```html
<div class="article-details-page pt-120 pb-120">
    <div class="container">
        <div class="row">
            <div class="col-lg-8">

                <div class="post-author-meta mb-40">
                    <div class="author-area">
                        <div class="author-img"><img src="images/author.png" alt="" /></div>
                        <div class="author-content">
                            <span>Written by</span>
                            <h2>Layla Haddad</h2>
                        </div>
                    </div>
                    <div class="post-date">
                        <span>Published</span>
                        <h2>12 March, 2026</h2>
                    </div>
                    <div class="social-area-wrap">
                        <div class="social-area">
                            <h2>Share</h2>
                            <ul class="social-list">
                                <li><a href="#"><i class="bi bi-linkedin"></i></a></li>
                                <li><a href="#"><i class="bi bi-twitter-x"></i></a></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="article-details-thumb-img mb-40">
                    <img src="images/article-thumb.png" alt="" />
                </div>

                <div class="details-contnt-wrap">
                    <h2>Building an oud accord that survives the UAE summer</h2>
                    <p>Body copy. <span>Emphasised run-in.</span></p>
                    <span class="line-break"></span>

                    <h3>Heat and headspace</h3>
                    <p>More body copy.</p>

                    <blockquote>
                        <!-- icon svg -->
                        <div class="content">
                            <h4>Stability is a formulation decision, not a packaging one.</h4>
                            <div class="author-area">
                                <h5>Layla Haddad</h5>
                                <span>Head Perfumer</span>
                            </div>
                        </div>
                        <!-- large decorative quote svg with class="quote" -->
                    </blockquote>

                    <span class="line-break two"></span>

                    <div class="details-image-area">
                        <div class="row gy-4">
                            <div class="col-md-6">
                                <div class="img-area"><img src="images/article-1.png" alt="" /></div>
                            </div>
                            <div class="col-md-6">
                                <div class="img-area"><img src="images/article-2.png" alt="" /></div>
                            </div>
                        </div>
                    </div>

                    <h2 class="style-2">Key takeaways</h2>
                    <ul class="details-list">
                        <li>Test at 45C, not 25C</li>
                        <li>Choose UV-blocking glass early</li>
                    </ul>
                </div>

                <div class="tag-navigation-area">
                    <ul class="tag-list">
                        <li><a href="#">Oud</a></li>
                        <li><a href="#">Stability</a></li>
                    </ul>
                    <div class="details-navigation">
                        <a href="#" class="navigation-arrow"><!-- icon svg --></a>
                        <p>Previous article title</p>
                        <a href="#" class="navigation-arrow"><!-- icon svg --></a>
                    </div>
                </div>

                <div class="comment-and-form-area">
                    <div class="comment-title"><h3>02 Comments</h3></div>
                    <div class="comment-area">
                        <ul class="comment">
                            <li>
                                <div class="single-comment-area">
                                    <div class="author-img"><img src="images/comment-1.png" alt="" /></div>
                                    <div class="comment-content">
                                        <div class="author-name-deg">
                                            <h3>Omar Rashid</h3>
                                            <span>12 March, 2026</span>
                                        </div>
                                        <p>Great breakdown of the heat-cycling protocol.</p>
                                        <a href="#" class="replay-btn">Reply <!-- icon svg --></a>
                                    </div>
                                </div>
                                <ul class="comment-replay">
                                    <li>
                                        <div class="single-comment-area">
                                            <div class="author-img"><img src="images/comment-2.png" alt="" /></div>
                                            <div class="comment-content">
                                                <div class="author-name-deg">
                                                    <h3>Layla Haddad</h3>
                                                    <span>13 March, 2026</span>
                                                </div>
                                                <p>Thanks Omar.</p>
                                                <a href="#" class="replay-btn">Reply <!-- icon svg --></a>
                                            </div>
                                        </div>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>

                    <div class="inquiry-form">
                        <h4>Leave a comment</h4>
                        <form action="#" method="post">
                            <div class="row gy-4">
                                <div class="col-md-6"><input type="text" placeholder="Name" /></div>
                                <div class="col-md-6"><input type="email" placeholder="Email" /></div>
                                <div class="col-lg-12"><textarea placeholder="Comment"></textarea></div>
                                <div class="col-lg-12">
                                    <button type="submit" class="primary-btn1"><span>Post Comment</span><span>Post Comment</span></button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>

            <div class="col-lg-4">
                <!-- §42 .news-article-sidebar-area -->
            </div>
        </div>
    </div>
</div>
```

Article-body vocabulary summary (this is the whole set — nothing else is styled):
`h2`, `h2.style-2` (smaller sub-heading), `h3`, `p`, `p > span` (emphasis),
`blockquote` (+ inner `.content > h4`, `.content .author-area > h5 + span`, and a
decorative `svg.quote`), `.details-image-area .img-area img`, `ul.details-list`,
`.line-break` / `.line-break.two` spacers.
`.inquiry-form` styles bare `input` / `textarea` directly — it does **not** use `.form-inner`.

**Suits:** article detail, and the 3 policy pages (use `.details-contnt-wrap` for the body).

---

## 53. Team details page — `.team-details-page`

style.css:17038.

```html
<div class="team-details-page pt-120 pb-120">
    <div class="container">
        <div class="row gy-5">
            <div class="col-lg-5">
                <div class="profile-area">
                    <div class="profile-img"><img src="images/team-img.png" alt="" /></div>
                    <div class="profile-content">
                        <div class="signature-icon">
                            <img class="white-logo" src="images/signature-white.png" alt="" />
                            <img class="dark-logo" src="images/signature-dark.png" alt="" />
                        </div>
                        <div class="para">
                            <!-- icon svg -->
                            <p>25 years shaping Middle Eastern fine fragrance.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-7">
                <div class="team-details-content">
                    <div class="name-social-area">
                        <span>Head Perfumer</span>
                        <h2>Layla Haddad</h2>
                        <ul class="social-list">
                            <li><a href="#"><i class="bi bi-linkedin"></i></a></li>
                            <li><a href="#"><i class="bi bi-twitter-x"></i></a></li>
                        </ul>
                    </div>

                    <div class="content">
                        <p>Bio paragraph.</p>
                    </div>

                    <div class="experience-achievements-list">
                        <h3>Experience &amp; Achievements</h3>
                        <ul class="experience-area">
                            <li>Lead perfumer, 400+ commercial launches</li>
                            <li>IFRA compliance lead since 2018</li>
                        </ul>
                    </div>

                    <div class="skills-expertise-list">
                        <div class="skills-container">
                            <h4>Skills &amp; Expertise</h4>
                            <div class="skill-item">
                                <div class="skill-info"><span>Oriental accords</span><span>95%</span></div>
                                <div class="progress-track">
                                    <div class="progress-bar" data-progress="95%"></div>
                                </div>
                            </div>
                            <div class="skill-item">
                                <div class="skill-info"><span>Stability testing</span><span>88%</span></div>
                                <div class="progress-track">
                                    <div class="progress-bar" data-progress="88%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

**Verified JS contract:** `custom.js` (~line 1041) runs on `window.onload`, selects
`.progress-bar` and does `bar.style.width = bar.getAttribute("data-progress")`.
So `data-progress` **must include the unit** (`"95%"`, not `"95"`). The CSS starts
the bar at `width: 0` with a 1.5s transition.

`.white-logo` / `.dark-logo` are the light/dark signature swap — since the
light/dark toggle was removed (commit a99b32a), ship only `.dark-logo` or check
`site-fixes.css` first.

**Suits:** an optional team-member detail page if our-team ever links through.

---

## 54. Team Page — `.team-img-page` (photo collage) and `.team-card` (the actual grid)

style.css:17280 is a scroll-triggered **collage**, not a card grid. The card grid
you almost certainly want is `.team-card` from section 30 (style.css:11714), which
is unused on the homepage.

### 54a. The team grid — `.team-card`

```html
<div class="row gy-4">
    <div class="col-lg-3 col-md-6">
        <div class="team-card">
            <div class="team-img">
                <img src="images/team-img.png" alt="" />
                <div class="social-area">
                    <ul class="social-list">
                        <li><a href="#"><i class="bi bi-linkedin"></i></a></li>
                        <li><a href="#"><i class="bi bi-twitter-x"></i></a></li>
                        <li><a href="#"><i class="bi bi-instagram"></i></a></li>
                    </ul>
                </div>
            </div>
            <div class="team-content">
                <h5><a href="team-detail.html">Layla Haddad</a></h5>
                <span>Head Perfumer</span>
            </div>
        </div>
    </div>
</div>
```

`h3` and `h5` are both styled identically inside `.team-content` — pick one.
The social list slides in on `.team-card:hover`. `.team-card.style-2` is a
lighter variant with a different social-list treatment.
Sliders `.team-card-slider` and `.creative-team-card-slider` are already wired in
`custom.js` if you want a carousel instead of a grid.

### 54b. The collage — `.team-img-page`

```html
<div class="team-img-page pb-150">
    <div class="container">
        <div class="team-img-wrapper">
            <div class="team-img-area">
                <div class="team-img"><img src="images/team-hero.png" alt="" /></div>
                <ul class="img-list">
                    <li><img src="images/team-img2.png" alt="" /></li>
                    <li><img src="images/team-img3.png" alt="" /></li>
                    <!-- exactly 9 li: nth-child(1)..(9) are individually positioned -->
                </ul>
            </div>
        </div>
    </div>
</div>
```

**Verified JS contract:** `custom.js` (~line 1315) uses a GSAP `matchMedia("(min-width: 768px)")`
+ `ScrollTrigger` to add/remove `.active` on `document.querySelector(".team-img-area")`
— **`querySelector`, singular**, so only the first `.team-img-area` on the page animates.
The CSS positions `li:nth-child(1)` through `:nth-child(9)`, so the list should hold
exactly 9 images.

### 54c. Join-the-team CTA — `.team-page-join-team-section`

```html
<div class="team-page-join-team-section">
    <div class="container">
        <div class="join-team-wrapper">
            <div class="outer-circle"></div>
            <div class="inner-circle"></div>
            <div class="join-team-content">
                <h2>Join our team</h2>
                <p>We are hiring perfumers, QC analysts and production leads.</p>
                <a href="careers.html" class="primary-btn1"><span>See Openings</span><span>See Openings</span></a>
            </div>
        </div>
    </div>
</div>
```

`.outer-circle` and `.inner-circle` are pure-CSS decorative rings (each draws its own
`::before` / `::after`); leave them empty.

**Suits:** our-team (54a grid + 54c CTA; 54b collage for the about page hero).

---

## 55. Job openings area — `.table-container`

style.css:17915. A responsive table that collapses to stacked cards below 576px.

```html
<div class="table-container">
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
            <tr>
                <td class="position-name" data-label="Position">Senior Perfumer</td>
                <td class="vacancies" data-label="Vacancies">02</td>
                <td class="job-type" data-label="Job Type">Full time</td>
                <td class="arrow-icon">
                    <a href="careers-detail.html" class="circle-btn"><!-- icon svg --></a>
                </td>
            </tr>
        </tbody>
    </table>
</div>
```

**`data-label` is required on every `<td>`.** Below 576px `thead` is hidden and
`td:before { content: attr(data-label); }` becomes the row label — omit it and the
mobile view loses all field names. `.circle-btn` fills on `tr:hover`.

**Suits:** careers (openings list).

---

## 58. Industries Section — `.industries-section` + `.industries-thum-img-area`

style.css:18242. A big text link list with a cursor-following image pair on hover.

```html
<div class="industries-section pt-120 pb-120">
    <div class="container">
        <div class="row">
            <div class="col-lg-4">
                <div class="section-title">
                    <span>Sectors</span>
                    <h2>Who we manufacture for</h2>
                </div>
            </div>
            <div class="col-lg-8 divider">
                <ul class="industries-list">
                    <li>
                        <a href="products-fine-fragrance.html">
                            <span>Fine Fragrance</span>
                            <div class="hover-img">
                                <img class="img1" src="images/industry-1.png" alt="" />
                                <img class="img2" src="images/industry-2.png" alt="" />
                            </div>
                        </a>
                    </li>
                    <li>
                        <a href="products-personal-care.html">
                            <span>Personal Care</span>
                            <div class="hover-img">
                                <img class="img1" src="images/industry-3.png" alt="" />
                                <img class="img2" src="images/industry-4.png" alt="" />
                            </div>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
```

`.divider` draws the vertical rule via `::after` — it goes on the **column**, not
the list. Hidden below 992px. `.hover-img` is `display:none` below 992px, so the
mobile experience is a plain link list.

**Warning:** `custom.js` (~line 1023) has a cursor-follow handler bound to
`.industries-wrap .single-industries` — **neither of those classes exists in
style.css or site-fixes.css.** That handler is dead for this build; the hover effect
you get is the pure-CSS `.img1` / `.img2` scale-in. Do not invent `.industries-wrap`.

`.industries-thum-img-area .img-area img` (style.css:18244) is a separate,
standalone rule for a rounded hero image — useful above the list.

**Suits:** products landing (4 category links), expertise landing.

---

## 59. Case study details page — `.case-study-details-page`

style.css:18433.

```html
<div class="case-study-details-page pt-120 pb-120">
    <div class="container">
        <div class="case-study-details-thumb-img">
            <img src="images/case-study-thumb.png" alt="" />
            <div class="img-details-wrap">
                <ul class="img-details">
                    <li><span class="style-2">Client</span><span>Aurelia Group</span></li>
                    <li><span class="style-2">Scope</span><span>Private label, 12 SKUs</span></li>
                </ul>
                <ul class="img-details">
                    <li><span class="style-2">Year</span><span>2025</span></li>
                    <li><span class="style-2">Market</span><span>GCC</span></li>
                </ul>
            </div>
        </div>

        <div class="section-title">
            <h2>From brief to 60,000 filled units in 14 weeks</h2>
        </div>

        <div class="case-study-details-content">
            <div class="details-section-title"><h3>The challenge</h3></div>
            <ul>
                <li>Compressed launch window</li>
                <li>Three concurrent concentrations</li>
            </ul>

            <ul class="style-2">
                <li><!-- icon svg --><div class="content"><p>Blocked by a 9-week glass lead time.</p></div></li>
            </ul>
            <ul class="style-3">
                <li><!-- icon svg --><div class="content"><p>Solved with a dual-supplier split.</p></div></li>
            </ul>
        </div>

        <div class="case-study-details-img">
            <img src="images/case-study-1.png" alt="" />
        </div>

        <div class="row">
            <div class="col-md-4">
                <div class="case-details-result-area">
                    <span>Lead time cut</span>
                    <h3>42%</h3>
                </div>
            </div>
            <div class="col-md-4">
                <div class="case-details-result-area style-2">
                    <span>Units shipped</span>
                    <h3>60k</h3>
                </div>
            </div>
            <div class="col-md-4">
                <div class="case-details-result-area style-3">
                    <span>Reject rate</span>
                    <h3>0.4%</h3>
                </div>
            </div>
        </div>

        <div class="social-area">
            <h4>Share</h4>
            <ul class="social-list">
                <li><a href="#"><i class="bi bi-linkedin"></i></a></li>
            </ul>
        </div>

        <div class="details-navigation">
            <a href="#" class="navigation-arrow"><!-- icon svg --></a>
            <p>Previous case study</p>
            <a href="#" class="navigation-arrow"><!-- icon svg --></a>
        </div>
    </div>
</div>
```

List variants: default `ul` is a disc list; `ul.style-2` is icon-led with a red
(`#de2342`) svg; `ul.style-3` is icon-led with a green (`#01aa26`) svg — natural
"problem / solution" pairing. `.case-details-result-area` has `.style-2`, `.style-3`,
`.style-4` corner-radius variants for a 3–4 across strip.
`.img-details-wrap` is absolutely positioned and overhangs the image by 70px — the
parent `.case-study-details-thumb-img` must stay `position: relative` (it is).

**Suits:** manufacturing (process story), a future case-study page.

---

## 60. Portfolio Details Page — `.portfolio-details-page`

style.css:18766. Very close to §59 but with a Swiper hero.

```html
<div class="portfolio-details-page pt-120 pb-120">
    <div class="container">
        <div class="swiper portfolio-details-slider">
            <div class="swiper-wrapper">
                <div class="swiper-slide">
                    <div class="details-img">
                        <img src="images/portfolio-1.png" alt="" />
                        <div class="details-img-content">
                            <ul>
                                <li><span class="style-2">Client</span><span>Aurelia Group</span></li>
                                <li><span class="style-2">Category</span><span>Eau de Parfum</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="swiper-pagination1 banner-pagi"></div>
        <div class="slider-btn-grp">
            <div class="slider-btn slider-prev"><!-- icon svg --></div>
            <div class="slider-btn slider-next"><!-- icon svg --></div>
        </div>

        <div class="section-title"><h2>Project title</h2></div>

        <div class="portfolio-details-content">
            <div class="details-section-title"><h3>Overview</h3></div>
            <p>Body copy.</p>
            <ul>
                <li>Bullet</li>
            </ul>
            <ul class="style-2">
                <li><!-- icon svg --><div class="content"><p>Icon-led bullet.</p></div></li>
            </ul>
        </div>

        <div class="portfolio-details-img"><img src="images/portfolio-2.png" alt="" /></div>

        <div class="results-impact-list">
            <ul>
                <li><span>42%</span> shorter lead time</li>
                <li><span>60k</span> units shipped</li>
            </ul>
        </div>

        <div class="portfolio-details-banner">
            <h3>Want the same result for your line?</h3>
            <a href="contact.html" class="primary-btn1"><span>Talk to us</span><span>Talk to us</span></a>
        </div>

        <ul class="tag-list">
            <li><a href="#">Private label</a></li>
        </ul>

        <div class="details-navigation">
            <a href="#" class="navigation-arrow"><!-- icon svg --></a>
            <p>Previous project</p>
            <a href="#" class="navigation-arrow"><!-- icon svg --></a>
        </div>
    </div>
</div>
```

**Verified JS contract:** `custom.js:368` initialises `new Swiper(".portfolio-details-slider", …)`
with `pagination.el: ".banner-pagi"` and `navigation: { nextEl: ".slider-next", prevEl: ".slider-prev" }`.
`.banner-pagi` and `.slider-prev`/`.slider-next` are the **JS hooks**; the visual
styling comes from `.swiper-pagination1` and `.slider-btn`. That is why the homepage
writes `<div class="swiper-pagination1 banner-pagi"></div>` (index.html:98) — copy
that double-class pattern.
`.portfolio-details-banner` has a hard-coded background image:
`url(../images/portfolio-details-banner-card.webp)` — swap it in `site-fixes.css`.

**Suits:** product category pages with a gallery, manufacturing capability showcase.

---

## 61. Join section — `.circle-wrapper`

style.css:19127. A decorative rotating dot ring around a circular content panel.
Fixed 420px / 560px / 514px dimensions — desktop only, there are no media queries.

```html
<div class="circle-wrapper">
    <div class="circle-border"></div>
    <div class="dot-rotate inner-dots">
        <span class="dot" style="--i: 0"></span>
        <span class="dot" style="--i: 60"></span>
        <span class="dot" style="--i: 120"></span>
    </div>
    <div class="dot-rotate outer-dots">
        <span class="dot" style="--i: 30"></span>
        <span class="dot" style="--i: 150"></span>
    </div>
    <div class="content">
        <h2>Join the First Perfumes network</h2>
        <a href="contact.html" class="primary-btn1"><span>Get in touch</span><span>Get in touch</span></a>
    </div>
</div>
```

Each `.dot` **must carry a `--i` custom property** (degrees) — the transform is
`rotate(calc(var(--i) * 1deg)) translateX(170px)` for inner dots and `210px` for outer.
Without `--i` all dots stack at the centre. `.dot-rotate` spins with a 12s `rotate` keyframe.
Dot colour is hard-coded `#b7f57b` — override in `site-fixes.css` for our red brand.

**Suits:** a CTA band on careers or about. Needs a mobile fallback (no responsive rules exist).

---

## 13. Testimonial — `.testimonial-card`

style.css:6030. The card itself is unused on the homepage (the homepage carries
`swiper-pagination1` but no `.testimonial-card`). Designed to live inside
`.home1-testimonial-slider`.

```html
<div class="home1-testimonial-section">
    <div class="container">
        <div class="testimonial-slider-area">
            <div class="swiper home1-testimonial-slider">
                <div class="swiper-wrapper">
                    <div class="swiper-slide">
                        <div class="testimonial-card">
                            <div class="testimonial-img-wrap">
                                <div class="testimonial-img">
                                    <img src="images/testimonial-author-img.png" alt="" />
                                    <div class="shape-area">
                                        <div class="single-shape"><!-- icon svg --></div>
                                        <div class="single-shape"><!-- icon svg --></div>
                                        <div class="single-shape"><!-- icon svg --></div>
                                        <div class="single-shape"><!-- icon svg --></div>
                                        <div class="single-shape"><!-- icon svg --></div>
                                    </div>
                                </div>
                            </div>
                            <div class="testimonial-content-wrap">
                                <div class="icon"><!-- icon svg --></div>
                                <div class="testimonial-content">
                                    <ul class="rating-area">
                                        <li><i class="bi bi-star-fill"></i></li>
                                        <li><i class="bi bi-star-fill"></i></li>
                                    </ul>
                                    <h3>Consistent batches, every time</h3>
                                    <p>Quote body. <span>Emphasis.</span></p>
                                </div>
                                <div class="author-area">
                                    <h5>Omar Rashid</h5>
                                    <span>Brand Director, Aurelia</span>
                                </div>
                                <img class="company-logo" src="images/client-logo.png" alt="" />
                                <!-- decorative svgs: class="quote", class="joint1", class="joint2" -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="swiper-pagination1"></div>
        </div>
    </div>
</div>
```

**Verified JS contract:** `custom.js:154` initialises `.home1-testimonial-slider`.
The `.shape-area .single-shape` items, `.company-logo` and `.author-area` are all
animated **only on `.swiper-slide-active`** (style.css:6032–6056) — outside a Swiper
they will look static/hidden. Exactly 5 `.single-shape` children are individually
delayed (`nth-child(1)`..`(5)`).

**Suits:** about, manufacturing, a service detail page social-proof band.

---

## 14. Partner — `.partner-section`

style.css:6366. A pure-CSS infinite marquee (no JS — `jquery.marquee.min.js` is
loaded but never called in `custom.js`).

```html
<div class="partner-section pt-90 pb-90">
    <div class="container">
        <div class="partner-title">
            <h5>Trusted by <span>120+</span> brands across the GCC</h5>
        </div>
    </div>
    <div class="partner-wrap">
        <div class="marquee">
            <div class="marquee__group">
                <a href="#"><img src="images/partner-1.png" alt="" /></a>
                <a href="#"><img src="images/partner-2.png" alt="" /></a>
                <a href="#"><img src="images/partner-3.png" alt="" /></a>
            </div>
            <div class="marquee__group" aria-hidden="true">
                <a href="#"><img src="images/partner-1.png" alt="" /></a>
                <a href="#"><img src="images/partner-2.png" alt="" /></a>
                <a href="#"><img src="images/partner-3.png" alt="" /></a>
            </div>
        </div>
    </div>
</div>
```

**You must duplicate `.marquee__group`** — both run `animation: scroll-x-reverse 30s linear infinite`
and the second (`aria-hidden="true"`) is what makes the loop seamless.
`.partner-title` draws the two 493px horizontal rules via `::before` / `::after`
(hidden below 768px). Logos are forced to 145px wide.

**Suits:** about, manufacturing (certifications strip), homepage-adjacent trust bands.

---

## 16. Case study section — `.case-study-section` / `.case-study-card`

style.css:6626.

```html
<div class="case-study-section style-1 pt-120 pb-120">
    <!-- optional decorative: <div class="vector1"><!-- icon svg --></div>
                              <div class="vector2"><!-- icon svg --></div> -->
    <div class="container">
        <div class="section-title three">
            <div class="left-content"><span>Case Studies</span><h2>Proof in production</h2></div>
            <div class="right-content">
                <a href="#" class="view-more-btn">
                    <svg class="border" width="88" height="1" viewBox="0 0 88 1" xmlns="http://www.w3.org/2000/svg"><rect width="88" height="1"></rect></svg>
                    View All
                </a>
            </div>
        </div>

        <div class="row gy-4">
            <div class="col-lg-6">
                <div class="case-study-card">
                    <div class="case-study-img-wrap">
                        <div class="batch"><span>Private Label</span></div>
                        <a href="#" class="case-study-img"><img src="images/case-study-1.png" alt="" /></a>
                    </div>
                    <div class="case-study-content">
                        <h3><a href="#">60,000 units in 14 weeks</a></h3>
                        <p>Short summary.</p>
                        <ul>
                            <li>
                                <div class="counter-content">
                                    <div class="number"><h2 class="counter">42</h2><span>%</span></div>
                                    <p>Lead time cut</p>
                                </div>
                            </li>
                            <li>
                                <div class="counter-content">
                                    <div class="number"><h2 class="counter">60</h2><span>k</span></div>
                                    <p>Units shipped</p>
                                </div>
                            </li>
                        </ul>
                        <a href="#" class="view-details-btn">View Details <span class="arrow"><!-- icon svg --></span></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

Section variants: `.style-1` (adds `.vector1` / `.vector2` decorative svgs),
`.style-2`, `.home4-case-study-section`.
Card variants: `.case-study-card.style-2` (content offset, different `.batch`),
`.case-study-card.style-3` (uses `h4` instead of `h3` in `.case-study-content`).
Counters: `.counter` is wired to counterUp (`custom.js:105`); `.counter_number`
is the GSAP alternative (`custom.js:1089`). Use one, not both.
A `<canvas>` inside `.case-study-img` is supported for the hover-distortion effect.

**Suits:** manufacturing, about (track record), expertise landing.

---

## 28. Award section — `.award-section`

style.css:11323. A hover-linked list ↔ image pair. **Verified JS contract**
(`custom.js:1331`): hovering `.award-list ul li` reads its index, clears `.active`
from every `.award-img ul li`, and sets `.active` on the matching index inside
**each** `.award-img` container. So the two lists must be the same length and in
the same order.

```html
<div class="award-section font-alt pt-120 pb-120">
    <div class="container">
        <div class="section-title"><h2>Certifications &amp; recognition</h2></div>
        <div class="row">
            <div class="col-lg-5">
                <div class="award-img">
                    <ul>
                        <li class="active"><div class="single-img"><img src="images/award-img.png" alt="" /></div></li>
                        <li><div class="single-img"><img src="images/award-img2.png" alt="" /></div></li>
                        <li><div class="single-img"><img src="images/award-img3.png" alt="" /></div></li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-7">
                <div class="award-list">
                    <ul>
                        <li class="active">
                            <div class="award-history">
                                <h3>ISO 22716 GMP Certified</h3>
                                <h3>2024</h3>
                            </div>
                        </li>
                        <li>
                            <div class="award-history">
                                <h3>IFRA Compliance Member</h3>
                                <h3>2023</h3>
                            </div>
                        </li>
                        <li>
                            <div class="award-history">
                                <h3>Dubai Municipality Approved</h3>
                                <h3>2022</h3>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```

`.award-history` is `justify-content: space-between` and styles both `h2` and `h3`
identically — the two headings are the label and the year.
`.award-section.font-alt` swaps Funnel Display for Space Grotesk.

Related: **§52 `.award-slider-section`** (style.css:17023) is a separate Swiper strip
(`custom.js:324` initialises `.award-slider`, up to 6.5 slides, `pagination.el: ".testimonial-section-pagi"`
— note that pagination class has **no CSS rule**, so add `swiper-pagination1` alongside it
the same way the homepage does with `banner-pagi`):

```html
<div class="award-slider-section">
    <div class="swiper award-slider">
        <div class="swiper-wrapper">
            <div class="swiper-slide">
                <div class="award-img"><img src="images/award-img.png" alt="" /></div>
            </div>
        </div>
    </div>
    <div class="swiper-pagination1 testimonial-section-pagi"></div>
</div>
```

**Suits:** about (certifications), manufacturing (GMP / IFRA / Dubai Municipality credentials).

---

## Page → section mapping (quick reference)

| Our page | Reuse |
|---|---|
| about | §14 partner, §13 testimonial, §16 case study, §28 award/certs, §54b collage, §61 CTA |
| expertise (landing) | §58 industries list, §16 case study, §45 `.contact-area` strip |
| 6 service detail pages | **§43 service details** (primary), §48 `.faq-wrap.style-2`, §46b form |
| manufacturing | §43, §59 case study details, §16, §28 award, §14 partner |
| products (landing) | §58 industries list, §39 `.nav-tab-page` filter |
| 4 product category pages | §44 industries details, §60 portfolio details (gallery) |
| insights list | §41 `.blog-card2`, §41b `.pagination-area`, §42 sidebar, §39 filter |
| article detail | §50 article details + comments, §42 sidebar |
| our-team | §54a `.team-card` grid, §54c join CTA, §53 for member detail |
| careers | §55 `.table-container` openings, §49 detail + apply modal, §61 CTA |
| contact | §46a `.contact-page-top`, §46b `.contact-form-wrap.inner-contact-from` |
| faq | §48 full page (rail + tabs + accordion) |
| 3 policy pages | §50 `.details-contnt-wrap` body only |
| 404 | §38 `.breadcrumb-section` + `.primary-btn1` (no dedicated 404 CSS exists) |

**No 404-specific CSS exists in style.css.** Build it from `.breadcrumb-section` plus
a centred `.section-title.text-center` and a `.primary-btn1`.
