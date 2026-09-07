# Component Notes — Page Sections & Shared Building Blocks

Source of truth: `_content/index.html` (homepage body fragment).
Styles: `css/style.css` (template) then `css/site-fixes.css` (project overrides, loaded last).
Behaviour: `js/custom.js` plus the vendor scripts listed in `_partials/chrome-bottom.html`.

**Rule for anyone extending this:** every class below was verified to exist in `css/style.css`
or `css/site-fixes.css`, or is documented explicitly as a *JS-only hook* / *inert*. Do not invent
new class names — the template has no utility layer, so an unrecognised class renders unstyled.

---

## 0. Cross-cutting facts you need before copying anything

### Containers

| Class | Defined in | Effect |
|---|---|---|
| `.container` | bootstrap + `site-fixes.css:19` | site-wide max width `calc(1600px + gutter*2)`, gutter `clamp(16px,4vw,60px)` |
| `.container-fluid.one` | `style.css:1949` (`max-width:1860px`) + `site-fixes.css:22` | wide bleed band — used by banner and video/counter |
| `.container-fluid.two` | `style.css:1952` (`max-width:1880px`) + `site-fixes.css:23` | widest bleed — used by the process panel |
| `.container.one` | `site-fixes.css:21` only | `one` adds nothing beyond the shared container rule in `style.css`; it exists only so the fixes file can group it. Harmless, kept for parity with the template. |

`site-fixes.css:31-36` zeroes the gutter on a nested container, so
`.container-fluid.two > … > .container` (the process section) does not double-indent.

### Spacing utilities that actually exist

* `.mb-120` → `margin-bottom:120px` (`style.css:186`, responsive step-downs below). **Every top-level section on this page uses it.**
* `.mb-70` → `margin-bottom:70px` (`style.css:330`)
* `.mb-60` → `margin-bottom:60px` (`style.css:316`) — the standard gap between a section title row and its card grid
* `.mb-40` (`:400`), `.mb-30` (`:404`) also exist
* `.mt-30` is **not** a global utility. It is only styled at
  `style.css:12175` and `site-fixes.css:270`, both scoped to
  `.home4-process-section .process-section-wrap .process-wrapper`. Using it elsewhere does nothing.

Row gutters (`gy-3`, `gy-4`, `gy-5`, `gx-3`, `gx-xxl-4`, `gy-sm-5`) are plain Bootstrap 5.

### Animation attributes — what drives what

| Hook | Where implemented | Notes |
|---|---|---|
| `class="text-anim"` | `custom.js:462-486` | GSAP `SplitText` per-char reveal on scroll (`start: "top 85%"`). Optional `data-delay="0.4"` (float seconds, default `0.25`). Put it on the `<h2>`/`<p>` itself. **No CSS** — JS-only hook. |
| `class="fade_anim"` | `custom.js:1052-1086` | GSAP fade-in. Optional `data-delay` (default `.15`), `data-duration` (default `0.75`), `data-fade-from` = `top`\|`bottom`\|`left`\|`right` (default `bottom`), `data-fade-offset` (default `40`), `data-ease` (default `power2.out`), `data-on-scroll` (`1` = ScrollTrigger, anything else = fire immediately). Goes on the **grid column**, not the card. **No CSS** — JS-only hook. |
| `class="wow animate fadeInLeft"` + `data-wow-delay` / `data-wow-duration` | `custom.js:431-442`, `js/wow.min.js`, `css/animate.css` | WOW.js with `boxClass:"wow"`, `animateClass:"animated"`, `offset:80`, `mobile:true`, `live:true`. `fadeInLeft` / `fadeInUp` / `fadeInRight` are real animate.css classes. **`animate` is inert** — there is no `.animate` rule in `animate.css` or `style.css`; it is template noise. Copy it or drop it, it changes nothing. |
| `data-eg-throwable-scene` / `data-eg-throwable-el` | `js/Throwable.min.js` (+ `js/matter.min.js`, `js/throwable-helper.js`) | Matter.js physics pile. Scene attribute on the container, element attribute on each `<p>`. |
| `class="shape-hover-item"` wrapping `.shape-hover-img[data-displacement]` | `custom.js:1173-1208`, `js/three.js`, `js/hover-effect.umd.js` | WebGL displacement hover. `.shape-hover-item` has **no CSS** (JS hook); `.shape-hover-img` is styled (`style.css`, 7 rules). Reads `data-displacement`, `data-intensity`, `data-speedin`, `data-speedout`, `data-easing`. |
| `class="counter"` | `custom.js:105` (`jquery.counterup` + `waypoints`) | Counts the element's own number text up on first scroll-in. |
| `class="lazy-bg-video" data-src="…"` | `custom.js:1511-1544` | IntersectionObserver (`rootMargin:400px`) swaps `data-src` → `src` on the `<video>` and its `<source>`, plays on enter, pauses on exit. **No CSS.** |

---

## 1. `home3-banner-section` — hero

Full-bleed hero: headline + accent paragraph + one CTA + trust-badge strip on the left,
fading Swiper image slider on the right.

**Good for:** the top of any landing/home-style page that needs a photographic hero with a slider.

### Wrapper

```html
<div class="home3-banner-section mb-120">
    <div class="container-fluid one">
        <div class="row">
            <div class="col-lg-12">
                <div class="banner-wrapper">
                    <div class="banner-content-wrap"> … </div>
                    <div class="banner-img-wrap"> … </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

`.home3-banner-section` (`style.css:10307`) → `.banner-wrapper` (`:10320`) → `.banner-content-wrap` (`:10349`).

### Heading block

This section does **not** use `.section-title`. It has a bespoke `h1` + `.para-area` pattern.

```html
<div class="banner-content-wrap">
    <h1>Crafting Signature Fragrances <span>for Global Brands.</span></h1>
    <div class="para-area">
        <div class="icon">
            <!-- icon svg (vertical 6x49 arrow rule) -->
        </div>
        <p>
            UAE's leading <span>perfume &amp; cosmetics</span> manufacturer since 2006 — …
        </p>
    </div>
    <div class="button-area">
        <!-- .primary-btn2 — see §9 -->
    </div>
    <ul class="btm-area">
        <li>
            <div class="author-area">
                <ul class="author-img-grp">
                    <li><img src="images/fda.webp" alt="" loading="lazy" decoding="async"></li>
                    <!-- repeat per badge -->
                </ul>
            </div>
        </li>
    </ul>
</div>
```

* `h1 span` is the emphasised second half (`style.css` `.banner-content-wrap h1 span`).
* `.para-area` / `.para-area svg` / `.para-area p` / `.para-area p span` all styled (`:10491`-`:10526`).
* `.btm-area > li` gets an automatic `::before` divider except `:first-child` (`:10578`-`:10595`).
  It also supports a `.rating-area` child (`.review`, `.rating .star`, `.light-logo`, `.dark-logo`) if you need the review variant — not used here.
* `.author-area` / `.author-img-grp` are only styled **inside** `.btm-area > li` (`:10550`ff). They overlap the badge images and un-round the first one.
* **`.button-area` has no rule inside this section** — it is a bare positioning div here. (It *is* styled in `home1-banner-section`, so do not assume it is portable.)

### Slider

```html
<div class="banner-img-wrap">
    <div class="swiper home3-banner-slide">
        <div class="swiper-wrapper">
            <div class="swiper-slide">
                <div class="img-area">
                    <img src="images/banner-img-slide.webp" alt="" fetchpriority="high" decoding="async">
                </div>
            </div>
            <!-- repeat .swiper-slide -->
        </div>
    </div>
    <div class="swiper-pagination1 banner-pagi"></div>
</div>
```

* `.home3-banner-slide` and `.banner-pagi` are **JS selectors only** (no CSS). Swiper is instantiated at `custom.js:174-191`: `slidesPerView:1`, `speed:1500`, `loop:true`, `effect:"fade"` with `crossFade:true`, autoplay `2500ms`, pagination `el:".banner-pagi", clickable:true`.
* The visible pagination styling comes from `.swiper-pagination1` (`style.css`, 13 rules) plus `.banner-img-wrap .swiper-pagination1` / `::after`.
* `.img-area` / `.img-area img` styled at `.banner-img-wrap .img-area`.
* First slide uses `fetchpriority="high"` (LCP); the rest `loading="lazy"`.
* **Animation:** none. No `text-anim` / `fade_anim` / `wow` here — the Swiper fade is the motion.

---

## 2. `home4-about-us-section` — about / intro split

Two-column: image + physics "throwable" chip pile on the left, eyebrow + heading + copy + button on the right.

**Good for:** an about-page intro, a company-story block, or any two-column "text + supporting visual" slot.

```html
<div class="home4-about-us-section mb-120 ">
    <div class="container">
        <div class="row gy-5">
            <div class="col-lg-6 order-lg-1 order-2">
                <div class="about-us-left-area">
                    <div class="feature-wrap">
                        <img src="images/about.webp" loading="lazy" decoding="async">
                        <div class="throwable-box-wrap">
                            <div class="throwable-item-wrap" data-eg-throwable-scene="true">
                                <p data-eg-throwable-el>
                                    <span class="throwable-item">End-to-End Expertise</span>
                                </p>
                                <p data-eg-throwable-el>
                                    <span class="terracotta throwable-item">Premium Quality</span>
                                </p>
                                <!-- repeat; colour modifiers below -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 order-lg-2 order-1">
                <div class="about-us-right-area">
                    <div class="section-title">
                        <span>About Us</span>
                        <h2 class="text-anim">Crafting Fragrances. Building Brands.</h2>
                        <p>Founded in 2006 …</p>
                        <!-- .primary-btn1.transparent — see §9 -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

* Heading block = **plain `.section-title`** (no `.three`, no `home*-section-title`), so the eyebrow is `.section-title > span` (`style.css:770` — pill with 1px `#c8c8c8` border, radius 16px). Overridden further by `.home4-about-us-section .about-us-right-area .section-title` (`:12964`-`:12987`).
* `.feature-wrap > img` sizing comes from `site-fixes.css:171`.
* Throwable chip colour modifiers — **all five exist, and only inside `.about-us-left-area .feature-wrap`**:
  `.terracotta` (`:12949`), `.periwinkle` (`:12952`), `.muted-green` (`:12955`), `.aqua-green` (`:12958`), `.green` (`:12961`). A chip with no modifier uses the base `.throwable-item` colour.
* `.feature-wrap .title-area > h3` also exists (`:12864`, `:12886`) — the homepage has it commented out; uncomment it if you want a heading above the chips.
* **Animation:** `text-anim` on the `<h2>`. The chip pile is driven by `data-eg-throwable-scene` / `data-eg-throwable-el` (Matter.js), not GSAP.

---

## 3. `home4-process-section` — numbered step flow

Dark full-bleed panel with a title row, then a horizontal row of numbered step cards joined by animated SVG connectors.

**Good for:** "how it works" / methodology / onboarding-steps pages. Four cards is the designed count (`.single-process`, `.two`, `.three`, `.four` are the only variants that exist).

### Wrapper + title block

```html
<div class="home4-process-section mb-120">
    <div class="container-fluid two">
        <div class="process-section-wrap">
            <div class="section-title-wrap">
                <div class="container">
                    <div class="row gy-3 mb-60 justify-content-between">
                        <div class="col-lg-7">
                            <div class="section-title home4-section-title three">
                                <span>Process</span>
                                <div class="left-content">
                                    <h2 class="text-anim">From Brief to Finished Product</h2>
                                    <p class="text-anim">Our structured 8-step process …</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-5">
                            <div class="right-content">
                                <a href="#footer" class="view-more-btn style-2">
                                    <svg class="border" width="88" height="1" viewBox="0 0 88 1"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <rect width="88" height="1" />
                                    </svg>
                                    Let’s Work Together</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="process-wrapper"> … cards … </div>
        </div>
    </div>
</div>
```

* `.process-section-wrap` (`style.css:12105`, `::after` at `:12128`; heavily re-tuned in `site-fixes.css:198`-`:212`) draws the dark panel.
* **`.section-title-wrap` has no CSS anywhere** — it is a pure structural div. Keep it for parity or drop it; it changes nothing.
* Title variant: `.section-title.home4-section-title.three` (`:1071`, `:1074`). Note the eyebrow `<span>` sits **outside** `.left-content`, so it matches `.section-title > span` (`:770`), while `.left-content` holds the h2 + p.
* The `.right-content` here is a **sibling column**, not a child of `.section-title`, so the `.section-title.three .right-content .view-more-btn::before` rule does **not** apply — that is why the rule is drawn with the inline `<svg class="border">` instead. `.home4-process-section .view-more-btn::before` (`:12102`) supplies the section-specific tweak.

### Repeating card (one representative step)

```html
<div class="single-process mt-30">
    <div class="process-card wow animate fadeInLeft" data-wow-delay="200ms"
        data-wow-duration="1500ms">
        <div class="step-no">
            <span>STEP : 01</span>
        </div>
        <h3>Briefing</h3>
        <p>We understand your client vision, market goals, target audience …</p>
        <svg class="vector" width="75" height="75" viewBox="0 0 75 75" fill="none"
            xmlns="http://www.w3.org/2000/svg">
            <rect width="25" height="25" fill="#df2341" />
            <rect x="25" y="25" width="25" height="25" fill="#df2341" />
            <rect y="50" width="25" height="25" fill="#df2341" />
            <rect x="50" y="50" width="25" height="25" fill="#df2341" />
        </svg>
    </div>
    <svg class="animated-vector" width="65" height="100" viewBox="0 0 181 124" fill="none"
        xmlns="http://www.w3.org/2000/svg">
        <path opacity="0.2" id="theMotionPath11"
            d="M0 123H67.5C84.0685 123 97.5 109.569 97.5 93V31C97.5 14.4315 110.931 1 127.5 1H181"
            stroke="black" />
        <path d="M0 0 L13 0" stroke="url(#paint0_linear_354_7441)" stroke-linecap="round"
            stroke-width="20">
            <animateMotion dur="4s" begin="0s" repeatCount="indefinite" rotate="auto">
                <mpath href="#theMotionPath11"></mpath>
            </animateMotion>
        </path>
        <defs>
            <linearGradient id="paint0_linear_354_7441" x1="10" y1="0" x2="0" y2="0"
                gradientUnits="userSpaceOnUse">
                <stop stop-color="#CB0000" offset="0" />
                <stop offset="1" stop-color="white" stop-opacity="0" />
            </linearGradient>
        </defs>
    </svg>
</div>
```

Sequencing rules as built on the homepage:

| Item | Classes | Connector SVG | WOW class |
|---|---|---|---|
| 1 | `single-process mt-30` | **after** the card, path id `theMotionPath11` | `fadeInLeft` |
| 2 | `single-process two` | none | `fadeInUp` |
| 3 | `single-process three mt-30` | **before** the card, `theMotionPath12` (reversed via `keyPoints="1;0" keyTimes="0;1"`) | `fadeInRight` |
| 4 | `single-process four` | **before** the card, `theMotionPath13` | `fadeInUp` |

* `.step-no` + `.step-no::before` + `.step-no span` (`:12260`-`:12303`), `.process-card h3` (`:12312`), `.process-card p` (`:12333`), `.process-card .vector` (`:12254`), `.animated-vector` (`:12351`, sized by `site-fixes.css:246-249` via `--process-connector`).
* **Every `id` in the connector SVG must be unique per card** (`theMotionPathNN`, `paint0_linear_…`). Duplicating ids across cards breaks `<mpath>` and the gradient.
* **Animation:** WOW.js on `.process-card` (`data-wow-delay="200ms"`, `data-wow-duration="1500ms"`); `text-anim` on the h2 *and* the p in the title block; SMIL `<animateMotion>` inside the connectors.

---

## 4. `home3-service-section` — 3-across service/expertise grid

**Good for:** services, capabilities, expertise, or any "six short cards with a Read/View link" grid.

```html
<div class="home3-service-section mb-120">
    <div class="container">
        <div class="row gy-3 mb-60 justify-content-between">
            <div class="col-lg-7">
                <div class="section-title home3-section-title three">
                    <span>Our Expertise</span>
                    <h2 class="text-anim">Expertise That Shapes Every Fragrance</h2>
                </div>
            </div>
            <div class="col-lg-5">
                <div class="right-content">
                    <a href="#" class="view-more-btn style-2">
                        <svg class="border" width="88" height="1" viewBox="0 0 88 1"
                            xmlns="http://www.w3.org/2000/svg">
                            <rect width="88" height="1"></rect>
                        </svg>
                        View All</a>
                </div>
            </div>
        </div>
        <div class="row gy-4">
            <!-- repeat the column below -->
        </div>
    </div>
</div>
```

Repeating card:

```html
<div class="col-lg-4 col-md-6 fade_anim" data-delay=".3" data-duration="2" data-ease="bounce">
    <div class="home3-service-card">
        <h3><a href="#">Fragrance Development</a></h3>
        <p>Custom fragrance accords and formulations …</p>
        <a class="primary-btn2 transparent" href="#">
            <!-- see §9 for the exact inner spans -->
        </a>
        <div class="vector-icon">
            <!-- icon svg, 60x60, uses <mask> + <g> -->
        </div>
    </div>
</div>
```

* `.home3-service-card` (`:10923`); `h2`/`h3` are both styled the same (`:10937`), so either heading level works. `h3 a` and `h3 a:hover` styled.
* `.vector-icon` + `.vector-icon svg` (`:10990`, `:11001`); on `.home3-service-card:hover` the icon svg and the `.primary-btn2.transparent` invert (`:11010`-`:11021`).
* `.home3-service-section` itself has **almost no rules** (only `.font-alt` heading overrides at `:10913`). All visual weight lives in `.home3-service-card` — so the card is portable into any `.container` + Bootstrap row.
* Title variant: `.section-title.home3-section-title.three` (`:1039`-`:1045`) with the eyebrow as a direct `<span>` child.
* **Animation:** `fade_anim` on each **column** with staggered `data-delay` of `.3` / `.4` / `.5` per row of three, `data-duration="2"`, `data-ease="bounce"`. `text-anim` on the h2.

---

## 5. `home4-portfolio-section` — stacked scroll-pinned case cards

Seven full-width cards that pin and scale-down as you scroll, each a 50/50 text + image split.

**Good for:** capability deep-dives, case studies, facility/process tours — anything where each item deserves a full viewport and a photo.

```html
<div class="home4-portfolio-section mb-120">
    <div class="container">
        <div class="row gy-3 mb-60 justify-content-between">
            <div class="col-lg-8">
                <div class="section-title home4-section-title three">
                    <span>Manufacturing Capabilities</span>
                    <div class="left-content">
                        <h2 class="text-anim">Advanced Fragrance Manufacturing</h2>
                        <p class="text-anim">State-of-the-art facility in Jebel Ali, Dubai …</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="right-content">
                    <a href="#" class="view-more-btn style-2">
                        <svg class="border" width="88" height="1" viewBox="0 0 88 1"
                            xmlns="http://www.w3.org/2000/svg">
                            <rect width="88" height="1" />
                        </svg>
                        View All</a>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12 mb-70">
                <div class="porfolio-card-wrapper">
                    <!-- cards -->
                </div>
            </div>
        </div>
    </div>
</div>
```

> Note the template's spelling: the wrapper is **`porfolio-card-wrapper`** (missing the first `t`) while the card is **`portfolioCard`** (camelCase). Both are exactly as defined in `style.css:13252`ff — do not "correct" them.

Repeating card:

```html
<div class="portfolioCard">
    <div class="row">
        <div class="col-lg-6">
            <div class="portfolio-content">
                <div class="portfolio-content-top">
                    <h3><a href="#">Our Manufacturing Facility</a></h3>
                    <p>Located in Jebel Ali Industrial First, Dubai …</p>
                </div>
                <div class="portfolio-content-btm">
                    <a href="#" class="view-details-btn">View
                        Details
                        <svg class="arrow" width="20" height="20" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <g>
                                <path d="…" />
                            </g>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="portfolio-img">
                <img src="images/facility-jebel-ali.webp" alt="…" loading="lazy" decoding="async">
            </div>
        </div>
    </div>
</div>
```

* Card 1 is bare `portfolioCard`; cards 2-7 add an ordinal modifier: `.two` `.three` `.four` `.five` `.six` `.seven` (`style.css:13383`-`:13398`) — these set each card's background/offset so the stack reads as distinct layers. **There is no `.eight`.** If you need more than seven cards, add a CSS rule first.
* `.portfolio-content-top` supports an optional `<ul><li>` tag list (`:13334`, `:13341`) — unused on the homepage.
* **Animation:** GSAP ScrollTrigger at `custom.js:971-1002` — only above `991px` width. Each `.portfolioCard` is pinned (`pin:true, pinSpacing:false`) from `top 100px` until the last card, and scaled to `1 - (count - index) * 0.025`. No `wow` / `fade_anim` / `text-anim` on the cards; `text-anim` only on the title block.

---

## 6. `video-and-counter-section` — full-bleed video + stat band

Lazy-loaded looping background video with an overlapping panel holding a paragraph, a CTA and four counters.

**Good for:** a mid-page brand/credibility break, or an "about us by the numbers" band.

```html
<div class="video-and-counter-section mb-120">
    <div class="container-fluid one">
        <div class="row">
            <div class="col-lg-12">
                <div class="video-area">
                    <video loop="loop" muted="muted" playsinline="playsinline" preload="none"
                           poster="media/video-poster.webp" class="lazy-bg-video"
                           data-src="media/first-perfumes-web.mp4">
                        <source data-src="media/first-perfumes-web.mp4" type="video/mp4" />
                    </video>
                </div>
                <div class="counter-area-wrap">
                    <div class="container">
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="counter-content">
                                    <div class="left-content">
                                        <p>For nearly two decades … <span>UAE's fragrance and cosmetics manufacturing</span> …</p>
                                    </div>
                                    <div class="right-content">
                                        <!-- .primary-btn2 (solid) — see §9 -->
                                    </div>
                                </div>
                                <div class="counter-wrap">
                                    <div class="row gy-sm-5 gy-4">
                                        <div class="col-lg-3 col-md-4 col-sm-6 divider">
                                            <div class="single-countdown">
                                                <div class="number">
                                                    <h2 class="counter">20</h2><span>+</span>
                                                </div>
                                                <span>Years of Expertise</span>
                                            </div>
                                        </div>
                                        <!-- 3 more, see alignment note -->
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

* `.video-area` (`:11437`), `.video-and-counter-section video` (`:11455`), `.counter-area-wrap` + `::after` overlay (`:11472`, `:11493`).
* `.counter-content .left-content p` and `… p span` (`:11513`, `:11522`) — wrap the emphasised phrases in `<span>`.
* `.counter-content .right-content .primary-btn2 .content` / `.icon` get section-specific colours (`:11526`, `:11529`).
* `.counter-wrap` + `::before` top rule (`:11534`, `:11538`); `.divider` + `.divider::before` draws the vertical rule (`:11547`, `:11550`) — put `divider` on the first three columns and **omit it on the last**, exactly as the homepage does.
* `.single-countdown .number h2, … .number span` are styled together (`:11586`) and `.single-countdown > span` is the label (`:11601`).
* Column alignment on the homepage uses plain Bootstrap flex utilities per stat:
  `1` → `col-lg-3 col-md-4 col-sm-6 divider`
  `2` → `… d-flex justify-content-md-center divider`
  `3` → `… d-flex justify-content-lg-center justify-content-md-end justify-content-start divider`
  `4` → `… d-flex justify-content-lg-end`
* **Animation:** `class="counter"` on the `<h2>` (counterUp, `custom.js:105`) and `class="lazy-bg-video"` + `data-src` on both the `<video>` and its `<source>` (`custom.js:1511`). No GSAP hooks.

---

## 7. `home2-our-work-section` — hover-linked list + image swap

A vertical list of products/services on the right; hovering an item cross-fades a large image column on the left and a small image column on the right.

**Good for:** a product-range or offer overview where each item has a short description and a supporting photo.

```html
<div class="home2-our-work-section mb-120">
    <div class="container one">
        <div class="row">
            <div class="col-lg-12 mb-60">
                <div class="section-title three">
                    <div class="left-content">
                        <span>Products &amp; Solutions</span>
                        <h2 class="text-anim">Premium Fragrance Solutions, Crafted for Your Brand</h2>
                    </div>
                    <div class="right-content">
                        <p>Manufacturing excellence across fine fragrances, personal care, and cosmetics</p>
                        <a href="#" class="view-more-btn">View More
                            <svg class="arrow" width="20" height="20" viewBox="0 0 20 20"
                                xmlns="http://www.w3.org/2000/svg">
                                <g><path d="…" /></g>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="our-work-wrapper">
                <div class="row justify-content-between align-items-center">
                    <div class="col-lg-4 col-md-5 d-md-block d-none">
                        <div class="our-work-img"> … </div>
                    </div>
                    <div class="col-lg-7 col-md-6">
                        <div class="row justify-content-between align-items-center">
                            <div class="col-xxl-8 col-lg-7">
                                <div class="our-work-list"> … </div>
                            </div>
                            <div class="col-lg-4 d-lg-block d-none">
                                <div class="our-work-img two"> … </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

**This is the only section where `.right-content` lives *inside* `.section-title.three`.** That is what activates
`.section-title.three .right-content .view-more-btn::before` (`style.css:892`, section tweak at `:9822`), which draws the
rule via CSS — hence this button uses a bare `.view-more-btn` with an inline `<svg class="arrow">` and **no** `.style-2` / `<svg class="border">`.

Left image column item (`.our-work-img ul li`):

```html
<div class="our-work-img">
    <ul>
        <li class="active">
            <div class="single-img">
                <img src="images/our-work-img.webp" alt="" loading="lazy" decoding="async">
            </div>
            <div class="counter-wrap">
                <div class="counter-content">
                    <div class="number">
                        <h3>98</h3>
                        <span>%</span>
                    </div>
                    <span>Success Rate</span>
                </div>
                <svg class="arrow" width="15" height="15" viewBox="0 0 15 15"
                    xmlns="http://www.w3.org/2000/svg">
                    <path d="…" stroke-width="2" stroke-linecap="round" />
                </svg>
            </div>
        </li>
        <!-- one <li> per list item, same order -->
    </ul>
</div>
```

> Known template quirk: the CSS sizes `.counter-wrap .counter-content .number h4` (`style.css:9871`, 28px/700), but the homepage markup uses `<h3>`. The number therefore falls back to the global `h3` size instead of the intended 28px. Left as-is (documented, not "fixed") — if you want the designed size, use `<h4>`.

Right small image column is the same `<ul><li><div class="single-img">` structure on `.our-work-img.two` (`:9922`) with **no** `.counter-wrap`.

List column:

```html
<div class="our-work-list">
    <ul>
        <li class="active fade_anim" data-delay=".2" data-fade-from="top">
            <h2><a href="#">Fine Fragrances</a></h2>
            <div class="our-work-content">
                <p>Eau de Parfum, Eau de Toilette &amp; niche blends crafted through
                   <strong>expert compounding and batching</strong>, …</p>
            </div>
        </li>
        <!-- repeat -->
    </ul>
</div>
```

* `.our-work-content p strong` is styled (`:10030`) — use `<strong>` for the emphasised phrase.
* `li.active` opens the description (`:10034`, `:10040`); mark the first item `active` in the markup.
* **The three `<ul>`s must have the same number of `<li>`s in the same order** — `custom.js:1150-1170` matches by index: hovering `.our-work-list ul li` sets `active` on it and on `ul li:eq(index)` inside **every** `.our-work-img`.
* **Animation:** `fade_anim` with `data-fade-from="top"` on each list `<li>` (`data-delay` `.2`/`.2`/`.3`/`.4` on the homepage); `text-anim` on the h2.

---

## 8. `home1-blog-section` — 3-across article cards

**Good for:** blog/news/insights teasers on any page.

```html
<div class="home1-blog-section mb-120">
    <div class="container">
        <div class="row gy-3 mb-60 justify-content-between">
            <div class="col-lg-7">
                <div class="section-title home3-section-title three">
                    <span>Industry Insights</span>
                    <h2 class="text-anim">Insights &amp; Trends In Fragrance</h2>
                </div>
            </div>
            <div class="col-lg-5">
                <div class="right-content">
                    <a href="#" class="view-more-btn style-2">
                        <svg class="border" width="88" height="1" viewBox="0 0 88 1"
                            xmlns="http://www.w3.org/2000/svg">
                            <rect width="88" height="1"></rect>
                        </svg>
                        View All</a>
                </div>
            </div>
        </div>
        <div class="row gy-4 gx-xxl-4 gx-3">
            <!-- repeat the column below -->
        </div>
    </div>
</div>
```

Repeating card:

```html
<div class="col-lg-4 col-md-6 fade_anim" data-delay=".2">
    <div class="blog-card style-2 home3-blog-card">
        <div class="blog-image-wrap">
            <a class="blog-img shape-hover-item" href="#">
                <div
                    class="shape-hover-img"
                    data-displacement="images/start-up/hover-img-shape2.webp"
                    data-intensity="0.6"
                    data-speedin="1"
                    data-speedout="1"
                >
                    <img src="images/blog-img.webp" alt="" loading="lazy" decoding="async">
                </div>
            </a>
            <div class="icon">
                <a href="#">
                    <!-- icon svg, 23x23 diagonal arrow -->
                </a>
            </div>
        </div>
        <div class="blog-content">
            <ul class="blog-meta">
                <li><a href="#">Sustainability</a></li>
                <li>
                    <!-- icon svg, 37x6 double-ended rule separator -->
                </li>
                <li><a href="#">September, 2026</a></li>
            </ul>
            <h3>
                <a href="#">Eco-Friendly Sourcing: The Future of Responsible Fragrance Manufacturing</a>
            </h3>
            <a class="primary-btn2 transparent" href="#">
                <!-- see §9 -->
            </a>
        </div>
    </div>
</div>
```

* Three classes are all required: `.blog-card` (base, `:5162`ff), `.style-2` (layout + meta, `:5287`ff), `.home3-blog-card` (typography, `:5361`ff).
* `.blog-image-wrap .icon` is the corner arrow badge; it reveals on `.blog-image-wrap:hover` (`:5187`, `:5204`).
* `.blog-img canvas` is styled (`:5297`) because the WebGL hover replaces the `<img>` with a `<canvas>` — that is why the `<img>` must sit inside `.shape-hover-img`.
* `.blog-card.style-2 .blog-content .view-details-btn` also exists (`:5345`) if you prefer that link style over `.primary-btn2.transparent`.
* **Animation:** `fade_anim` on each column with `data-delay` `.2` / `.4` / `.6`; `text-anim` on the h2; `shape-hover-item` + `shape-hover-img[data-displacement]` for the image hover.

---

## 9. Shared building blocks

### 9.1 `.section-title` and its variants

Base `.section-title` (`style.css:756`) is `display:flex; align-items:start; justify-content:space-between; gap:50px`,
collapsing to a column below `1199px`. So its **direct children** are the flex items.

Three shapes are used on this page:

**(a) Stacked — plain `.section-title`** (about-us section). Eyebrow is a direct `<span>` → `.section-title > span` (`:770`, pill).

```html
<div class="section-title">
    <span>About Us</span>
    <h2 class="text-anim">Crafting Fragrances. Building Brands.</h2>
    <p>…</p>
    <!-- optional button -->
</div>
```

**(b) Eyebrow + heading only — `.section-title home3-section-title three`** (service + blog sections).

```html
<div class="section-title home3-section-title three">
    <span>Our Expertise</span>
    <h2 class="text-anim">Expertise That Shapes Every Fragrance</h2>
</div>
```

**(c) Eyebrow + heading + supporting paragraph — `.section-title home4-section-title three`** (process + portfolio sections).
The `<span>` stays a direct child; `h2` + `p` go inside `.left-content`.

```html
<div class="section-title home4-section-title three">
    <span>Process</span>
    <div class="left-content">
        <h2 class="text-anim">From Brief to Finished Product</h2>
        <p class="text-anim">Our structured 8-step process …</p>
    </div>
</div>
```

**(d) Title + right column inside the title — `.section-title three`** (our-work section only).
Here the eyebrow goes **inside** `.left-content` so it picks up `.section-title.three .left-content > span` (`:860`), and `.right-content` becomes a flex sibling.

```html
<div class="section-title three">
    <div class="left-content">
        <span>Products &amp; Solutions</span>
        <h2 class="text-anim">Premium Fragrance Solutions, Crafted for Your Brand</h2>
    </div>
    <div class="right-content">
        <p>…</p>
        <a href="#" class="view-more-btn">View More <svg class="arrow" …>…</svg></a>
    </div>
</div>
```

Also present in `style.css` but unused on the homepage: `.section-title.two` (`:841`), `.section-title.text-center` (`:838`), `.section-title.white-color.three` (`:1027`), and the `.right-content .review-area` rating block (`:909`ff).

**Standard title row** — the pattern all four grid sections share:

```html
<div class="row gy-3 mb-60 justify-content-between">
    <div class="col-lg-7"><!-- .section-title … --></div>
    <div class="col-lg-5"><div class="right-content"><!-- .view-more-btn.style-2 --></div></div>
</div>
```

(The portfolio section uses `col-lg-8` / `col-lg-4` because its heading has a paragraph.)

---

### 9.2 `.primary-btn1` — filled pill with a vertical text swap

`style.css:1110`. Requires **exactly two sibling `<span>` children with identical content**: the second is absolutely
positioned below and slides up on hover while the first slides out. Any `<svg>` goes *inside* each span
(`.primary-btn1 > span svg` sets `fill`). The dark wipe is the `::after` pseudo-element — do not add a child for it.

```html
<a class="primary-btn1 transparent" href="#">
    <span>
        Explore More
        <svg width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <g><path d="…" /></g>
        </svg>
    </span>
    <span>
        Explore More
        <svg width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <g><path d="…" /></g>
        </svg>
    </span>
</a>
```

Modifiers that exist: `.white-bg` (`:1185`), `.black-bg` (`:1198`), `.transparent` (`:1214` — no fill, 1px `var(--title-color)` border, `padding:16px 17px`, primary-colour wipe on hover).
Omitting the second `<span>` leaves the button visually fine at rest but with no hover animation.

---

### 9.3 `.primary-btn2` — pill label with sliding circular icons

`style.css:1234`. Requires **three children in this exact order**: `.icon`, `.content`, `.icon.two`.
At rest `.icon` is scaled to 0.5 / opacity 0 / `margin-inline-end:-32px` and `.icon.two` is visible;
on hover they swap. Each `.icon` holds a 10×10 stroked arrow `<svg>` (`fill="none"`, `stroke-width="1.5"`).

```html
<a class="primary-btn2 transparent" href="#">
    <span class="icon">
        <svg width="10" height="10" viewBox="0 0 10 10" fill="none"
             xmlns="http://www.w3.org/2000/svg">
            <path d="M1 9L9 1M9 1C7.22222 1.33333 3.33333 2 1 1M9 1C8.66667 2.66667 8 6.33333 9 9"
                  stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
    </span>
    <span class="content">View Details</span>
    <span class="icon two">
        <svg width="10" height="10" viewBox="0 0 10 10" fill="none"
             xmlns="http://www.w3.org/2000/svg">
            <path d="M1 9L9 1M9 1C7.22222 1.33333 3.33333 2 1 1M9 1C8.66667 2.66667 8 6.33333 9 9"
                  stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
    </span>
</a>
```

* Default (no modifier): solid `var(--primary-color1)` pill, inverts to `var(--black-color)` on hover. Used in the banner and the video/counter band.
* `.black-bg` (`:1306`): black at rest, primary on hover.
* `.transparent` (`:1326`): outlined at rest, fills with primary on hover. Used in the service cards and blog cards.
* The svg colour is set via **`stroke`**, not `fill` (`.primary-btn2 .icon svg { fill:none; stroke:… }`) — keep `fill="none"` on the svg.
* Dropping `.icon.two` breaks the swap: nothing is visible at rest on the trailing side.

---

### 9.4 `.view-more-btn` — text + rule "see all" link

`style.css:1351`. Two child shapes exist:

**Inline arrow form** (used inside `.section-title.three .right-content`, where CSS supplies the rule via `::before`):

```html
<a href="#" class="view-more-btn">View More
    <svg class="arrow" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
        <g><path d="…" /></g>
    </svg>
</a>
```

**`.style-2` form** (used when `.right-content` is a *sibling* column, so no `::before` applies — the rule is an explicit svg):

```html
<a href="#" class="view-more-btn style-2">
    <svg class="border" width="88" height="1" viewBox="0 0 88 1" xmlns="http://www.w3.org/2000/svg">
        <rect width="88" height="1"></rect>
    </svg>
    View All</a>
```

* `.view-more-btn .arrow` gets `fill: var(--title-color)` and rotates 45° on hover (`:1369`, `:1386`).
* `.view-more-btn .border` gets `fill:#979797`, shrinking to 60px below 576px (`:1373`).
* `.style-2` adds `align-items:end; gap:10px; margin-top:10px` (`:1381`).
* Pick the form by asking: **is `.right-content` a child of `.section-title.three`?** Yes → inline arrow form. No → `.style-2` + `<svg class="border">`.

---

### 9.5 `.view-details-btn` — context-scoped text link

**There is no standalone `.view-details-btn` rule in `style.css`.** It is only styled through a full ancestor chain,
so it renders unstyled outside a known parent. The two contexts relevant here:

* `.home4-portfolio-section .porfolio-card-wrapper .portfolioCard .portfolio-content .portfolio-content-btm .view-details-btn` (`:13352`)
* `.blog-card.style-2 .blog-content .view-details-btn` (`:5345`)

(Also defined under `.service-card .service-card-content`, `.case-study-card .case-study-content`, and `.single-portfolio2 .portfolio-content`.)

```html
<a href="#" class="view-details-btn">View
    Details
    <svg class="arrow" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
        <g>
            <path d="…" />
        </g>
    </svg>
</a>
```

The `<svg class="arrow">` child is required — it takes `fill: var(--title-color)` and `transform: rotate(45deg)` on hover.
If you need this link in a *new* section, either nest it in one of the parents above or add a scoped rule to `site-fixes.css`.

---

### 9.6 `.magnetic-item` / `.magnetic-wrap` — magnetic cursor hook

**JS-only, and not currently used anywhere on this site** (0 occurrences in `_content/index.html`, `_partials/chrome-top.html`, `_partials/chrome-bottom.html`).

* You author **only** `.magnetic-item`. `custom.js:494` does `$(".magnetic-item").wrap('<div class="magnetic-wrap"></div>')` — **never write `.magnetic-wrap` by hand.**
* Neither class has any CSS rule. The only related style is `#ball.magnetic-active` (`style.css:613`).
* It activates only when **all** of these hold (`custom.js:488-497`):
  * `<body class="tt-magic-cursor">` — already set in `_partials/chrome-top.html:34`
  * body does **not** have `.is-mobile`
  * `$(window).width() > 1024`
  * the cursor element `<div id="ball"></div>` exists — already present at `_partials/chrome-top.html:36`
* `<a class="magnetic-item">` additionally gets `not-hide-cursor` added automatically.
* On hover the generated wrap grows the cursor ball to 70×70 and GSAP-translates the item toward the pointer (movement factor 25), resetting with `clearProps:"all"` on leave.

```html
<a class="primary-btn1 magnetic-item" href="#">
    <span>Contact Us</span>
    <span>Contact Us</span>
</a>
```

---

## 10. Quick picker

| Need | Use |
|---|---|
| Photographic hero with a slider | §1 `home3-banner-section` |
| Two-column story / intro | §2 `home4-about-us-section` |
| Numbered "how it works" flow (4 steps) | §3 `home4-process-section` |
| 3-across services / capabilities grid | §4 `home3-service-section` |
| Scroll-pinned deep-dive cards (≤7) | §5 `home4-portfolio-section` |
| Video break + stat counters | §6 `video-and-counter-section` |
| Hover-linked product/offer list | §7 `home2-our-work-section` |
| Article / news teasers | §8 `home1-blog-section` |
