# Motion System & Asset Inventory — First Perfumes (Softro template)

Reference notes for page authors. Everything below was read out of
`js/custom.js`, `css/style.css`, `css/site-fixes.css`, `_partials/chrome-top.html`,
`_partials/chrome-bottom.html`, `_content/index.html` and `build.py`.

**Rule that produced this document: every class name, id and data-attribute here was
grepped and confirmed present in the source. If a name is not in this file, assume it
does not exist.** Long SVG `d=""` path data is replaced with `<!-- icon svg -->` in the
skeletons; the wrapper elements and their classes are verbatim.

---

# PART A — MOTION

## A0. What is loaded, and in what order

`_partials/chrome-bottom.html` ends with this exact script order. `js/custom.js` is last
and is a single `(function($){ ... })(jQuery)` IIFE that runs at parse time (end of body,
**not** on DOMContentLoaded), so every hook below binds against markup that is already in
the document.

```
js/jquery-3.7.1.min.js
js/bootstrap.min.js
js/swiper-bundle.min.js
js/waypoints.js
js/jquery.counterup.min.js
js/wow.min.js
js/jquery.nice-select.min.js
js/jquery.marquee.min.js        <- loaded but NEVER initialised (see A12)
js/gsap.min.js
js/ScrollTrigger.min.js
js/ScrollSmoother.min.js
js/SplitText.min.js
js/matter.min.js                <- physics engine for the throwable box
js/Throwable.min.js
js/throwable-helper.js
js/jquery.fancybox.min.js
js/three.js                     <- required by hover-effect
js/hover-effect.umd.js
js/custom.js
```

`js/jquery-ui.js` (341 KB) and `js/moment.min.js` (51 KB) used to sit between jQuery and
Bootstrap. Nothing in `custom.js` or any page fragment called a single API from either, so
both the tags and the files are gone.

Consequence: **a page that omits any of these breaks every hook after it.** Page bodies are
assembled by `build.py` from `_partials/chrome-top.html` + `_content/<slug>.html` +
`_partials/chrome-bottom.html`, so the script block is automatic — never hand-edit a built
`*.html` at the repo root, edit `_content/<slug>.html` and re-run `python build.py`.

## A1. The scroll container — ScrollSmoother

`_partials/chrome-top.html` lines 632–633 open the wrapper; `chrome-bottom.html` closes it.

```html
<div id="smooth-wrapper">
    <div id="smooth-content">
        <!-- header, breadcrumb, page body, footer all live here -->
    </div>
</div>
```

`custom.js:5-11`

```js
let smoother = ScrollSmoother.create({
  wrapper: "#smooth-wrapper",
  content: "#smooth-content",
  smooth: 2,
  smoothTouch: 0.1,
  effects: true,   // must be true to use data-lag
});
```

* `#magic-cursor`, `#scroll-percentage` and `.right-sidebar-menu` sit **outside**
  `#smooth-wrapper` on purpose — they must not be transformed. Anything you add that has to
  stay fixed to the viewport belongs there too; `position: fixed` inside `#smooth-content`
  is broken by the smoother's transform.
* Every ScrollTrigger in `custom.js` is created **without** an explicit `scroller`, relying
  on ScrollSmoother's auto-registration. Do not pass a `scroller` yourself.

### `data-lag` (ScrollSmoother parallax)

`effects: true` is set, so ScrollSmoother reads `data-lag` and `data-speed` off any element
inside `#smooth-content`. **Neither attribute is used anywhere in this project today** —
grep for `data-lag` across `*.html`, `*.css`, `*.js` returns only the comment on
`custom.js:10`. It is available but unproven here.

```html
<!-- element trails the scroll by 0.5s -->
<div class="portfolio-img" data-lag="0.5">
    <img src="images/rnd-lab.webp" alt="" loading="lazy" decoding="async">
</div>
```

* Value is a number (seconds of lag). No default is applied by our code — GSAP's own default
  applies only when the attribute is present.
* **Gotcha:** ScrollSmoother implements the effect by setting a `transform` on the element.
  Do not put `data-lag` on an element that is also a `.fade_anim` target, a ScrollTrigger
  `pin` target (`.portfolioCard`), or an ancestor of either — the transforms fight.
* **Gotcha:** an element with `data-lag` must not be `position: sticky`.

---

## A2. `.fade_anim` — the general-purpose entrance

`custom.js:1052-1086`. This is the hook to reach for 90% of the time.

```js
let tp_fade_offset    = item.getAttribute("data-fade-offset") || 40,
    tp_duration_value = item.getAttribute("data-duration")    || 0.75,
    tp_fade_direction = item.getAttribute("data-fade-from")   || "bottom",
    tp_onscroll_value = item.getAttribute("data-on-scroll")   || 1,
    tp_delay_value    = item.getAttribute("data-delay")       || 0.15,
    tp_ease_value     = item.getAttribute("data-ease")        || "power2.out";
```

It runs `gsap.from(item, { opacity: 0, x, y, ease, duration, delay, scrollTrigger })` with
`scrollTrigger: { trigger: item, start: "top 85%" }`.

| attribute | accepted values | default | notes |
|---|---|---|---|
| `data-fade-from` | `top` \| `bottom` \| `left` \| `right` | `bottom` | anything else = fade with no travel |
| `data-fade-offset` | number, px | `40` | `top`/`left` negate it internally |
| `data-duration` | number, seconds | `0.75` | |
| `data-delay` | number, seconds | `0.15` | homepage uses `.2`–`.6` to stagger a grid |
| `data-ease` | any GSAP ease name | `power2.out` | homepage service cards use `bounce` |
| `data-on-scroll` | `1` \| `0` | `1` | `0` drops the ScrollTrigger — animates immediately on load |

Real usage on the homepage (`_content/index.html:375-380`) — note the class goes on the
**Bootstrap column**, not the card:

```html
<div class="col-lg-4 col-md-6 fade_anim" data-delay=".3" data-duration="2" data-ease="bounce">
    <div class="home3-service-card">
        <h3><a href="#">Fragrance Development</a></h3>
        <p>Custom fragrance accords and formulations …</p>
        <a class="primary-btn2 transparent" href="#">
            <span class="icon"><!-- icon svg --></span>
            <span class="content">View Details</span>
            <span class="icon two"><!-- icon svg --></span>
        </a>
        <div class="vector-icon"><!-- icon svg --></div>
    </div>
</div>
```

and on a list item (`_content/index.html:1375`):

```html
<li class="active fade_anim" data-delay=".2" data-fade-from="top">
    <h2><a href="#">Fine Fragrances</a></h2>
    <div class="our-work-content"><p>…</p></div>
</li>
```

`build.py` emits it automatically on every inner page's breadcrumb:

```html
<ul class="breadcrumb-list fade_anim" data-fade-from="top" data-delay=".15"> … </ul>
<div class="para fade_anim" data-fade-from="bottom" data-delay=".35"> … </div>
```

**Gotchas**

* `.fade_anim` has **zero CSS** in `style.css` or `site-fixes.css`. It is a pure behaviour
  hook — it will not style or lay anything out, and adding it never changes layout.
* Do **not** nest a `.fade_anim` inside another `.fade_anim`. Both write `transform` and
  `opacity` on their own elements; the outer one's `gsap.from` re-parents nothing but the
  compounded opacity makes the inner reveal read as a double fade.
* Never put `.fade_anim` on `.portfolioCard`, on `.porfolio-card-wrapper`, or on any
  ancestor of a pinned element — GSAP's inline transform breaks ScrollTrigger `pin`.
* `data-delay="0"` and `data-fade-offset="0"` both work (the `||` guard sees the non-empty
  string `"0"`, which is truthy). Only a *missing* attribute falls back to the default.
* Because it is `gsap.from`, the element is fully visible if JS fails. Safe for SEO.

---

## A3. `.text-anim` — SplitText character reveal

`custom.js:462-486`.

```js
let staggerAmount = 0.03, translateXValue = 20, defaultDelay = 0.25, easeType = "power2.out";
let animationSplitText = new SplitText(element, { type: "chars, words" });
gsap.from(animationSplitText.chars, {
  duration: 1, delay: delayValue, x: translateXValue, autoAlpha: 0,
  stagger: staggerAmount, ease: easeType,
  scrollTrigger: { trigger: element, start: "top 85%" },
});
```

* **No specific tag is required.** On the homepage it is applied to `<h2>` (6 times) and
  `<p>` (2 times); `build.py` applies it to the breadcrumb `<h1>`. Confirmed occurrences in
  the built `index.html`: lines 782, 828, 829, 987, 1494, 1495, 1857, 2094.
* Only tunable attribute: **`data-delay`** (seconds, `parseFloat`). Default `0.25`.
  `data-duration`, `data-ease`, `data-fade-from` are **ignored** here — they belong to
  `.fade_anim` only.

```html
<div class="section-title home3-section-title three">
    <span>Our Expertise</span>
    <h2 class="text-anim">Expertise That Shapes Every Fragrance</h2>
</div>
```

```html
<div class="section-title home4-section-title three">
    <span>Process</span>
    <div class="left-content">
        <h2 class="text-anim">From Brief to Finished Product</h2>
        <p class="text-anim">Our structured 8-step process ensures every product reaches market with confidence.</p>
    </div>
</div>
```

**Gotchas**

* SplitText **destroys and rebuilds the element's innerHTML** into `<div>` wrappers per word
  and per character. Never put a `.text-anim` on an element containing an `<a>`, a `<br>`,
  a `<span>` you style, or anything with its own event handler — it will be re-wrapped and
  handlers bound before `custom.js` runs are lost. The homepage banner `<h1>` contains a
  `<span>` and correctly does **not** carry `.text-anim`.
* Keep it to headings and one-line intro paragraphs. A long paragraph becomes hundreds of
  DOM nodes and the 0.03s stagger makes the reveal crawl.
* Like `.fade_anim`, `.text-anim` has **no CSS** — pure behaviour hook.
* SplitText is a GSAP Club plugin. `gsap.config({ trialWarn: false })` is only executed
  inside the magic-cursor branch (desktop > 1024px), so on narrow viewports a console
  warning may appear. Harmless.

---

## A4. `.counter` — counterUp (the one the homepage uses)

`custom.js:105-108`

```js
$(".counter").counterUp({ delay: 10, time: 1000 });
```

Powered by `jquery.counterup.min.js` + `waypoints.js`. It reads the element's **own text**
as the target, replaces it with `0`, then steps to the target once (`this.destroy()` after
first fire, `offset: '100%'` — fires as the element's top crosses the bottom of the viewport).

Exact homepage markup (`_content/index.html:1164-1171`):

```html
<div class="col-lg-3 col-md-4 col-sm-6 divider">
    <div class="single-countdown">
        <div class="number">
            <h2 class="counter">20</h2><span>+</span>
        </div>
        <span>Years of Expertise</span>
    </div>
</div>
```

* Per-element overrides read by the plugin: **`data-counterup-time`** (ms) and
  **`data-counterup-delay`** (ms). Both override the global `1000` / `10`.
* The plugin preserves thousands separators (`1,200` counts as `1,200`), decimals
  (`4.8` keeps one decimal place) and `HH:MM:SS` time strings.
* **Gotcha:** the suffix must live in a **sibling** element. `<h2 class="counter">20+</h2>`
  breaks — the text is parsed as a number and the `+` is destroyed. The template's
  `<h2 class="counter">20</h2><span>+</span>` pattern is the correct one.
* `.counter` itself has no styling; `.single-countdown .number h2` supplies it. Always use
  the full `.single-countdown > .number > h2.counter + span` chain.

## A5. `.counter_number` — the GSAP counter (not used on the homepage)

`custom.js:1089-1114`. A second, independent counter implementation.

```js
const rawText = el.textContent.trim();
const finalValue = parseInt(rawText, 10) || 0;
const hasLeadingZero = finalValue >= 10 || (rawText.length > 1 && rawText.startsWith("0"));
gsap.to(counter, {
  value: finalValue, duration: 0.7, ease: "none", snap: { value: 1 },
  scrollTrigger: { trigger: el, start: "top 85%", once: true },
  onUpdate: () => { el.textContent = hasLeadingZero && v < 10 ? "0" + v : v; },
});
```

* Target is read from `textContent` with `parseInt(…, 10)`. No data-attribute controls it.
  There are **no** tunable attributes at all — duration is hard-coded at 0.7s.
* If the final value is `>= 10`, intermediate values below 10 are zero-padded (`07`, `08`)
  so the number does not jitter in width.
* `parseInt` means `"1,200"` becomes **1** and `"2.5"` becomes **2**. Integers only.
* **`.counter_number` has zero CSS anywhere in the project** and zero markup usage. It is a
  behaviour hook only — you must supply your own wrapper styling.
* **Never put `.counter` and `.counter_number` on the same element** — they both rewrite
  `textContent` on a timer and will fight.

**Use `.counter` on new pages.** It is the one proven in this build, and it keeps commas
and decimals.

---

## A6. Swiper — the ten configured sliders

Swiper is initialised unconditionally for all ten selectors; a missing selector is a no-op.
Every one needs the standard Swiper 8+ DOM: a root carrying **both** `swiper` and the config
class, then `.swiper-wrapper` > `.swiper-slide`.

| root class (JS hook) | effect / loop | pagination el | navigation els | slides at ≥1400 |
|---|---|---|---|---|
| `.home1-process-slider` | — | — | `.process-slider-next` / `.process-slider-prev` | 3 |
| `.home1-testimonial-slider` | fade, loop | `.testimonial-pagi` | — | 1 |
| `.home3-banner-slide` | fade, loop | `.banner-pagi` | — | 1 |
| `.team-card-slider` | — | `.team-section-pagi` | — | 4 |
| `.creative-team-card-slider` | — | `.creative-team-pagi` | — | 4 |
| `.home3-testimonial-slide` | — | `.testimonial-section-pagi` | — | 2 |
| `.award-slider` | — | `.testimonial-section-pagi` | — | 6.5 (fractional) |
| `.portfolio-details-slider` | fade, loop | `.banner-pagi` | `.slider-next` / `.slider-prev` | 1 |
| `.home6-testimonial-slider` | — | — | `.testimonial-slider-next` / `.testimonial-slider-prev` | 2 |
| `.home2-testimonial-slider` | fade, loop | `.franctional-pagi` (type `fraction`) | `.testimonial-slider-next` / `.testimonial-slider-prev` | 1 |

All ten autoplay: `delay: 2500` except `.creative-team-card-slider` (`2000`).
`speed: 1500` on all ten. Only `.home6-testimonial-slider` sets `pauseOnMouseEnter: true`.

**The pagination and nav class names are JS selectors with no styling of their own.**
Confirmed: `banner-pagi`, `testimonial-pagi`, `testimonial-section-pagi`, `team-section-pagi`,
`creative-team-pagi`, `process-slider-next/prev`, `testimonial-slider-prev` return **0 hits**
in `style.css`. The visual styling comes from a second class you must add alongside:
`.swiper-pagination1` (13 rules) for dots, `.slider-btn` (35 rules) inside `.slider-btn-grp`
for arrows, `.franctional-pagi` (3 rules) for the fraction counter.

Homepage banner slider, verbatim (`_content/index.html:78-100`):

```html
<div class="banner-img-wrap">
    <div class="swiper home3-banner-slide">
        <div class="swiper-wrapper">
            <div class="swiper-slide">
                <div class="img-area">
                    <img src="images/banner-img-slide.webp" alt="" fetchpriority="high" decoding="async">
                </div>
            </div>
            <div class="swiper-slide">
                <div class="img-area">
                    <img src="images/banner-img-slide2.webp" alt="" loading="lazy" decoding="async">
                </div>
            </div>
        </div>
    </div>
    <div class="swiper-pagination1 banner-pagi"></div>
</div>
```

Note the pattern: `class="swiper-pagination1 banner-pagi"` = **styling class + JS hook class**.
Reproduce that pairing for any slider you add.

**Gotchas**

* Three selector collisions. Never put these pairs on the same page, they will steal each
  other's controls: `.home3-banner-slide` + `.portfolio-details-slider` (both bind
  `.banner-pagi`); `.home3-testimonial-slide` + `.award-slider` (both bind
  `.testimonial-section-pagi`); `.home6-testimonial-slider` + `.home2-testimonial-slider`
  (both bind `.testimonial-slider-next/prev`).
* Also: those selectors are **document-wide**, so two instances of the *same* slider class on
  one page share one pagination element and one Swiper instance's controls.
* `effect: "fade"` sliders need every slide the same height or the container jumps.
* Fancy cursor states for sliders (`.cursor-drag`, `.cursor-drag-mouse-down`,
  `data-simulate-touch="true"` on the slider's **parent**) are wired in `custom.js:667-766`
  but **none of those three class/attribute names exist in `style.css` or in any markup**.
  Treat them as dormant template code, not as an available feature.

---

## A7. The magic cursor family (desktop only, > 1024px)

Gate: `custom.js:488-489`

```js
if ($("body").not(".is-mobile").hasClass("tt-magic-cursor")) {
  if ($(window).width() > 1024) { … }
}
```

`_partials/chrome-top.html:34-37` supplies the required body class and the cursor node:

```html
<body class="tt-magic-cursor">
    <div id="magic-cursor">
        <div id="ball"></div>
    </div>
```

Default ball: 20×20, 2px border, opacity 0.5, follows the pointer at ratio 0.15.
Styling lives on `#magic-cursor` (2 rules) and `#ball` (12 rules) in `style.css`; the
dynamic children `.ball-view` / `.ball-view-inner` (3), `.ball-drag` (5), `.ball-close` (2)
are also styled.

### `.magnetic-item` / `.magnetic-wrap`

```js
$(".magnetic-item").wrap('<div class="magnetic-wrap"></div>');
```

* **Author writes `.magnetic-item` only. `.magnetic-wrap` is created by JS.**
  Writing `.magnetic-wrap` yourself produces a nested double wrapper and the ball scales
  twice on hover.
* Effect: the ball inflates to 70×70 opacity 1 and the item is pulled toward the cursor
  (movement factor 25) with a 0.3s ease; `clearProps: "all"` on leave.
* `a.magnetic-item` automatically also gets `.not-hide-cursor`.
* **Gotcha:** the generated wrapper is a plain `<div>`, i.e. `display: block`. Applying
  `.magnetic-item` to an inline element or to a flex/grid child inserts a block box into
  that layout and will shift it. Only apply to elements whose parent tolerates a block
  wrapper.
* **Neither `.magnetic-item` nor `.magnetic-wrap` has any CSS.** Pure behaviour.
* Not used anywhere in the current site (0 hits in the built `index.html`).

```html
<a class="primary-btn2 magnetic-item" href="contact.html">
    <span class="icon"><!-- icon svg --></span>
    <span class="content">Let’s Connect</span>
    <span class="icon two"><!-- icon svg --></span>
</a>
```

### `data-cursor`

`custom.js:628-664`. On hover the ball becomes a rounded label containing the attribute's
value; the element also gets `.not-hide-cursor` added automatically.

```html
<a class="portfolio-img" href="manufacturing.html" data-cursor="View Facility">
    <img src="images/facility-jebel-ali.webp" alt="" loading="lazy" decoding="async">
</a>
```

* The value is **appended as HTML** into `.ball-view-inner` (`$(".ball-view-inner").append(...)`),
  so keep it to plain text.
* Desktop only. Unused in the current site (0 hits).

### Other cursor classes that exist in JS

| class | what it does | CSS? |
|---|---|---|
| `.cursor-alter` | ball → 90×90, grey, opacity 0.2, no border | none |
| `.hide-cursor` | ball scales to 0 on hover (also applied to every `a, button`) | none |
| `.not-hide-cursor` | opts an element **out** of the hide-on-hover rule | none |
| `.cursor-close` | ball → 80×80 with a "Close" label | none (`.ball-close` is styled) |
| `.cursor-drag`, `.cursor-drag-mouse-down` | slider drag ball; requires `data-simulate-touch="true"` on the slider's parent | none |

None of these appear in the site's markup. `.cursor-alter` and `.hide-cursor`/`.not-hide-cursor`
are safe to reuse; the drag ones are effectively dead code.

### ⚠ The anchor-jump side effect

`custom.js:813-831`

```js
$('a[href^="#"]').not('[href$="#"]').not('[href$="#0"]').on("click", function () {
  …
  return false;
});
```

On desktop with the magic cursor active, **every in-page anchor link is neutered** —
`return false` cancels the jump and nothing scrolls in its place. The homepage's
`<a href="#footer" class="view-more-btn style-2">Let’s Work Together</a>` does nothing on
desktop. **Use `data-target` (A15) for in-page scrolling, not `href="#id"`.**

---

## A8. `.progress-bar` with `data-progress`

`custom.js:1040-1049`

```js
window.onload = () => {
  document.querySelectorAll(".progress-bar").forEach((bar) => {
    bar.style.width = bar.getAttribute("data-progress");
  });
};
```

* `data-progress` must be a **complete CSS length including the unit** — it is assigned
  straight to `style.width`. `data-progress="85%"` works; `data-progress="85"` does not.
* The transition comes entirely from CSS, and that CSS is scoped to exactly one deep chain
  (`style.css:17265-17277`) — the bar is invisible outside it:

```html
<div class="team-details-page">
    <div class="team-details-content">
        <div class="skills-expertise-list">
            <div class="skills-container">
                <h4>Skills &amp; Expertise</h4>
                <div class="skill-item">
                    <div class="skill-info">
                        <span>Fragrance Formulation</span>
                        <span>92%</span>
                    </div>
                    <div class="progress-track">
                        <div class="progress-bar" data-progress="92%"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

* **Gotcha:** the effect is `window.onload = …`, an assignment, not `addEventListener`. It
  will clobber any other `window.onload` handler added before `custom.js`, and vice versa.
* **Gotcha:** it fires on load, not on scroll. A skills block far down the page will have
  already animated by the time the reader arrives.
* Only usable on a page that carries the `.team-details-page` wrapper class.

---

## A9. Fancybox — `data-fancybox` and `.video-player`

`custom.js:94-103`

```js
$('[data-fancybox="gallery-01"]').fancybox({ buttons: ["close"], loop: false, protect: true });
$(".video-player").fancybox({ buttons: ["close"], loop: false, protect: true });
```

* **The gallery name is hard-coded.** Only `data-fancybox="gallery-01"` is initialised.
  `data-fancybox="gallery-02"`, `data-fancybox` with no value, etc. do nothing.
* Standard fancybox extras (`data-caption`, `data-src`) still apply because they are read by
  fancybox itself, not by our code.

```html
<a href="images/facility-jebel-ali.webp" data-fancybox="gallery-01" data-caption="Jebel Ali facility">
    <img src="images/facility-jebel-ali.webp" alt="" loading="lazy" decoding="async">
</a>
```

`.video-player` is the lightbox trigger for a video URL:

```html
<a class="video-player" href="https://www.youtube.com/watch?v=XXXXXXXX">
    <i class="bi bi-play-fill"></i>
</a>
```

* **Gotcha:** `.video-player` is *styled* only inside two testimonial cards —
  `.testimonial-card3 .author-area .author-img .video-player` and
  `.testimonial-card4 .testimonial-img .video-player` (`style.css:11220, 19934`). Used
  anywhere else it is an unstyled inline anchor; you must supply the button styling.
* `.video-player` is explicitly excluded from the "hide cursor on click" list, so the magic
  cursor stays visible on it.
* Neither hook is used in the current site.

---

## A10. `.shape-hover-item` / `.shape-hover-img` — WebGL displacement hover

`custom.js:1173-1209`, powered by `three.js` + `hover-effect.umd.js`. **This is used on the
homepage blog cards.**

```html
<div class="blog-image-wrap">
    <a class="blog-img shape-hover-item" href="#">
        <div class="shape-hover-img"
             data-displacement="images/start-up/hover-img-shape2.webp"
             data-intensity="0.6"
             data-speedin="1"
             data-speedout="1">
            <img src="images/blog-img.webp" alt="" loading="lazy" decoding="async">
        </div>
    </a>
    <div class="icon">
        <a href="#"><!-- icon svg --></a>
    </div>
</div>
```

Two classes, two jobs:

* `.shape-hover-img` — the element the WebGL canvas is built **into**. Carries all the
  data-attributes and contains the `<img>`.
* `.shape-hover-item` — the **hover target**, found via `.closest(".shape-hover-item")`.
  Must be `.shape-hover-img`'s ancestor (or itself). This is what makes the anchor's whole
  hit area trigger the ripple.

The guard is `if ($(".shape-hover-item").length)`, so **both classes are required** — a
`.shape-hover-img` with no `.shape-hover-item` ancestor never initialises anything.

| attribute (on `.shape-hover-img`) | maps to | notes |
|---|---|---|
| `data-displacement` | `displacementImage` | **required**, a greyscale map. The only one in the repo is `images/start-up/hover-img-shape2.webp` (512×512) |
| `data-intensity` | `intensity` | homepage uses `0.6` |
| `data-speedin` | `speedIn` | homepage uses `1` |
| `data-speedout` | `speedOut` | homepage uses `1` |
| `data-easing` | `easing` | unused on the homepage |
| `data-hover` | ~~`hover`~~ | **dead** — the config object sets `hover: !1` *after* reading it, so the later key always wins |

**Gotchas**

* `image1` and `image2` are **both** set to `n.eq(0).attr("src")` — the same, first `<img>`.
  This is a displacement ripple on one image, *not* a crossfade between two. Adding a second
  `<img>` inside `.shape-hover-img` does nothing.
* `imagesRatio: n[0].height / n[0].width` reads the **rendered** box of the `<img>`. The code
  guards with `i[0].complete` / `.on("load")`, so `loading="lazy"` is fine, but the `<img>`
  must have a resolved layout width when it fires. Do not put it inside a `display: none`
  parent that is revealed later — the canvas will be sized wrong.
* The library injects a `<canvas>` next to the `<img>`. Only two selectors in `style.css`
  give that canvas a border-radius: `.blog-card.style-2 .blog-image-wrap .blog-img canvas`
  (5297 — this is the homepage's) and `.blog-card.home4-blog-card … canvas` (5439). Use one
  of those two card shells, or the canvas will have square corners inside a rounded card.
* Costs a WebGL context per instance. Three on the homepage is already the practical ceiling.

---

## A11. `.portfolioCard` — the scroll-stacking cards

`custom.js:971-1003`. **This is the homepage "Manufacturing Capabilities" section.**

```js
$(function () {
  if ($(window).width() > 991) {
    let cards = gsap.utils.toArray(".portfolioCard");
    let lastCardST = ScrollTrigger.create({ trigger: cards[cards.length - 1], start: "top 100px" });
    cards.forEach((card, index) => {
      var scale = 1 - (cards.length - index) * 0.025;
      …
      ScrollTrigger.create({ trigger: card, start: "top 100px", end: () => lastCardST.start + 0,
                             pin: true, pinSpacing: false, animation: scaleDown, … });
    });
  }
});
```

Each card pins at `top 100px` and scales down as later cards ride over it. Desktop only
(> 991px). Structure — `.two` … `.seven` are the background-colour modifiers
(`style.css:13383-13400`), so **seven cards is the styled maximum**:

```html
<div class="porfolio-card-wrapper">
    <div class="portfolioCard">
        <div class="row">
            <div class="col-lg-6">
                <div class="portfolio-content">
                    <div class="portfolio-content-top">
                        <h3><a href="#">Our Manufacturing Facility</a></h3>
                        <p>Located in Jebel Ali Industrial First, Dubai …</p>
                    </div>
                    <div class="portfolio-content-btm">
                        <a href="#" class="view-details-btn">View Details
                            <svg class="arrow" width="20" height="20" viewBox="0 0 20 20"><!-- icon svg --></svg>
                        </a>
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="portfolio-img">
                    <img src="images/facility-jebel-ali.webp" alt="First Perfumes Jebel Ali Facility" loading="lazy" decoding="async">
                </div>
            </div>
        </div>
    </div>
    <div class="portfolioCard two"> … </div>
    <div class="portfolioCard three"> … </div>
</div>
```

Note the folder-level typo in the wrapper: **`porfolio-card-wrapper`** (missing the second
`t`). It is spelled that way in `style.css` (33 rules) and in `site-fixes.css`. Copy it
exactly.

**Gotchas**

* `gsap.utils.toArray(".portfolioCard")` is **document-wide and unscoped**. Two separate
  stacks on one page merge into one stack, and `lastCardST` anchors to the very last card in
  the DOM. **One `.portfolioCard` group per page, maximum.**
* Because every card pins to the same offset, **a card taller than the one covering it bleeds
  out of the stack**. `site-fixes.css:341-353` fixes this by forcing
  `height: clamp(420px, 30vw, 480px)` on `.home4-portfolio-section … .portfolioCard` at
  ≥992px and centring `.portfolio-content`. **If you reuse this section on another page you
  must keep the copy inside that height budget** (measured comfortable at ~380px of text at
  992px and 1280px), or extend the `site-fixes.css` rule to the new section.
* `site-fixes.css:325-339` also sets `overflow: hidden` on the card and `--bs-gutter-x: 0`
  on its inner `.row`, and `object-fit: cover` on `.portfolio-img img` — without those the
  photo hangs 12px past the rounded border.
* Do not put `.fade_anim`, `data-lag` or any other transform hook on the card or an ancestor.
* Below 992px the JS does not run and the cards simply flow — this is intentional, not a bug.

---

## A12. `.marquee` — CSS-only, and a red herring

`js/jquery.marquee.min.js` is loaded but **`custom.js` never calls `.marquee()`**. Do not
try to use the plugin's `data-duration` / `data-direction` / `data-duplicated` attributes;
nothing reads them.

What *does* exist is a pure-CSS marquee (`style.css:6454-6549`), scoped entirely to
`.partner-section .partner-wrap`:

```html
<div class="partner-section">
    <div class="partner-title">
        <h3>Trusted by <span>global brands</span></h3>
    </div>
    <div class="partner-wrap">
        <div class="marquee">
            <div class="marquee__group">
                <a href="#"><img src="images/fda.webp" alt="" loading="lazy" decoding="async"></a>
                <a href="#"><img src="images/iso.webp" alt="" loading="lazy" decoding="async"></a>
            </div>
            <div class="marquee__group" aria-hidden="true">
                <a href="#"><img src="images/fda.webp" alt="" loading="lazy" decoding="async"></a>
                <a href="#"><img src="images/iso.webp" alt="" loading="lazy" decoding="async"></a>
            </div>
        </div>
    </div>
</div>
```

* `.marquee` — `display: flex; overflow: hidden; gap: 60px` (40 at ≤1199, 30 at ≤576).
* `.marquee__group` — `flex-shrink: 0; min-width: 100%;
  animation: scroll-x-reverse 30s linear infinite`. The keyframe runs `translateX(-100%)` →
  `translateX(0)`, which is why you need **two identical groups** for a seamless loop.
* `.marquee__group a img` — width 145px (155 ≤1199, 120 ≤991, 140 ≤576).
* `.partner-wrap::before/::after` are 30px white gradient fades on each edge. **They are
  hard-coded `#ffffff`**, so the marquee only looks right on a white background.
* `@keyframes scroll-x` is defined (`style.css:6531`) but no rule uses it. Available if you
  want the opposite direction — you would add your own rule; there is no class for it.

---

## A13. `.lazy-bg-video` — the homepage background video

`custom.js:1511-1545`. IntersectionObserver with `rootMargin: "400px 0px"`; loads and plays
on approach, pauses when out of view, falls back to immediate load if IO is unavailable.

```html
<div class="video-area">
    <video loop="loop" muted="muted" playsinline="playsinline" preload="none"
           poster="media/video-poster.webp"
           class="lazy-bg-video"
           data-src="media/first-perfumes-web.mp4">
        <source data-src="media/first-perfumes-web.mp4" type="video/mp4" />
    </video>
</div>
```

* `data-src` is required **on both** the `<video>` and each `<source>` — the code copies the
  `<source>` `data-src` values first, then sets `lazyVideo.src`, then `.load()`.
* `preload="none"`, `muted`, `playsinline` are all required for autoplay to be allowed.
* **Gotcha:** the selector is `document.querySelector(".lazy-bg-video")` — **singular**.
  Only the *first* one on a page is wired. One background video per page.
* `.lazy-bg-video` itself has **no CSS**. Sizing comes from
  `.video-and-counter-section .video-area` (height 711 / 500 / 400 / 300px by breakpoint)
  and `.video-and-counter-section video` (`object-fit: cover`, `border-radius: 20px 20px 0 0`).
  Reuse that section wrapper or supply your own height.

---

## A14. WOW.js + animate.css

`custom.js:431-442`, on `window load`. Two WOW instances are created (`new WOW().init()`
then `window.wow = new WOW({...}); window.wow.init()`), the second with
`boxClass: "wow", animateClass: "animated", mobile: true, live: true, offset: 80`.

Homepage usage (`_content/index.html:216-217`) — the four process cards:

```html
<div class="single-process mt-30">
    <div class="process-card wow animate fadeInLeft" data-wow-delay="200ms" data-wow-duration="1500ms">
        <div class="step-no"><span>STEP : 01</span></div>
        <h3>Briefing</h3>
        <p>We understand your client vision, market goals …</p>
        <svg class="vector" width="75" height="75" viewBox="0 0 75 75"><!-- icon svg --></svg>
    </div>
</div>
```

* Animation names come from `css/animate.css`, which is **animate.css v3** — classic,
  unprefixed names: `.animated`, `.fadeInLeft`, `.fadeInRight`, `.fadeInUp`. It is **not**
  the `animate__` v4 build.
* Attributes: `data-wow-delay`, `data-wow-duration` (CSS time strings — `"200ms"`,
  `"1500ms"`), plus WOW's `data-wow-offset` and `data-wow-iteration`.
* **`animate` in `class="wow animate fadeInLeft"` is a no-op.** There is no `.animate`
  selector in `animate.css` or `style.css`. Harmless, but do not assume it does anything.
* Two WOW instances means the reveal callback runs twice per element. Cosmetically fine.
* Prefer `.fade_anim` for new work — it is GSAP-based, consistent with the rest of the
  system, and has real tunables. `.wow` is here only because the process section shipped
  with it.

### The SVG connector animation in that same section

The process connectors are pure SVG `<animateMotion>` + `<mpath>` — no JS at all:

```html
<svg class="animated-vector" width="65" height="100" viewBox="0 0 181 124" fill="none">
    <path opacity="0.2" id="theMotionPath11" d="…" stroke="black" />
    <path d="M0 0 L13 0" stroke="url(#paint0_linear_354_7441)" stroke-linecap="round" stroke-width="20">
        <animateMotion dur="4s" begin="0s" repeatCount="indefinite" rotate="auto">
            <mpath href="#theMotionPath11"></mpath>
        </animateMotion>
    </path>
    <defs>
        <linearGradient id="paint0_linear_354_7441" x1="10" y1="0" x2="0" y2="0" gradientUnits="userSpaceOnUse">
            <stop stop-color="#CB0000" offset="0" />
            <stop offset="1" stop-color="white" stop-opacity="0" />
        </linearGradient>
    </defs>
</svg>
```

* **The ids must be unique per page.** The homepage uses `theMotionPath11/12/13` and
  `paint0_linear_354_7441/7442/7443`. If you copy this section onto another page that
  already has one, renumber every id and every `href`/`url()` reference or the paths merge.
* `keyPoints="1;0" keyTimes="0;1"` on the second connector is what reverses its direction.
* `site-fixes.css:274-276` hides `.animated-vector` below 1200px, where the section goes
  two-up then one-up.

---

## A15. `data-target` — in-page smooth scroll

`custom.js:1212-1247`. **This is the correct way to link to a section on the same page**
(see the A7 anchor gotcha).

```js
const scrollTriggers = document.querySelectorAll("[data-target]");
const scrollOffset = 120;
// preventDefault, then smoother.scrollTo(targetTop + window.scrollY - 120, true)
```

```html
<a href="#" data-target="#footer" class="view-more-btn style-2">
    <svg class="border" width="88" height="1" viewBox="0 0 88 1"><rect width="88" height="1"></rect></svg>
    Let’s Work Together</a>
```

* Value is a **CSS selector string**, passed to `document.querySelector`. `#footer` exists
  (`_partials/chrome-bottom.html:2` — `<footer id="footer" class="footer-section home3-footer-section">`).
* Fixed 120px top offset, not configurable.
* Works on all viewports; not gated behind the magic cursor.
* Currently 0 uses in the site. Safe and recommended.
* **Gotcha:** Bootstrap 4 used `data-target` for collapse/modal. This project ships
  Bootstrap 5 (which uses `data-bs-target`), so there is no collision today — but never add
  a bare `data-target` to a Bootstrap component.

---

## A16. Index-paired hover lists

Two near-identical handlers that sync a text list with an image list **by DOM index**.

### `.our-work-list` ↔ `.our-work-img` — used on the homepage

`custom.js:1150-1170`. Hovering `.our-work-list ul li` at index *n* adds `.active` to that
`li` and to `ul li:eq(n)` inside **every** `.our-work-img` on the page.

```html
<div class="our-work-wrapper">
    <div class="row justify-content-between align-items-center">
        <div class="col-lg-4 col-md-5 d-md-block d-none">
            <div class="our-work-img">
                <ul>
                    <li class="active">
                        <div class="single-img">
                            <img src="images/our-work-img.webp" alt="" loading="lazy" decoding="async">
                        </div>
                        <div class="counter-wrap">
                            <div class="counter-content">
                                <div class="number"><h3>98</h3><span>%</span></div>
                                <span>Success Rate</span>
                            </div>
                            <svg class="arrow" width="15" height="15" viewBox="0 0 15 15"><!-- icon svg --></svg>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        <div class="col-lg-7 col-md-6">
            <div class="row justify-content-between align-items-center">
                <div class="col-xxl-8 col-lg-7">
                    <div class="our-work-list">
                        <ul>
                            <li class="active fade_anim" data-delay=".2" data-fade-from="top">
                                <h2><a href="#">Fine Fragrances</a></h2>
                                <div class="our-work-content"><p>…</p></div>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-4 d-lg-block d-none">
                    <div class="our-work-img two">
                        <ul>
                            <li class="active">
                                <div class="single-img">
                                    <img src="images/our-work-right-img1.webp" alt="" loading="lazy" decoding="async">
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

* **The two image lists must have at least as many `<li>` as the text list**, in the same
  order. The homepage has 4 text items and 6 images in each column, so items 5 and 6 are
  never reachable — harmless, but the first four must line up.
* `.our-work-img.two` is the narrow right-hand variant (no counter block).
* The `h3`/`span` inside `.counter-wrap` here are **plain numbers, not `.counter`** — they
  do not animate. Do not add `.counter` to them; it would fire once and then be stuck.
* Mouseenter only — there is no touch/keyboard path. Hence the `d-md-block d-none` /
  `d-lg-block d-none` guards that hide the images on small screens.
* **Gotcha:** selectors are document-wide. Two `.our-work-list` blocks on one page will
  cross-talk (`$(this).index()` is the index within its own `ul`, but `.active` is stripped
  from *all* `.our-work-list ul li`).

### `.award-list` ↔ `.award-img` — same pattern, not used here

`custom.js:1331-1351`. Identical logic. CSS exists (`.award-list` 14 rules, `.award-img`
11 rules) but no markup in the site. Reusable if you build an awards section, with the same
index-pairing rules.

---

## A17. Section-scoped hooks that are **NOT** on the homepage

These fire only when their owning section class is present. They exist in `custom.js`;
knowing them prevents accidental activation.

| JS hook | required root | CSS present? | status |
|---|---|---|---|
| `.home1-process-section .process-wrapper` + `.process-list .single-process` + `.process-count > span` | `.home1-process-section` | yes (64 rules) | Pins every step and a `n/total` counter, ≥992px. Complex; needs the exact 3-level DOM. |
| `.home3-process-section .process-list .single-process` | `.home3-process-section` | yes (46 rules) | Cumulative `.active` on scroll (0..i down, i+1..end up). |
| `.home4-banner-video video` + `.home4-banner-video-full` | `.home4-banner-video` | yes (7 rules) | Scrubbed video expand to 100vw/100vh, ≥991px. **Also drives the global `stickyLock` flag that suppresses `header.sticky`.** |
| `.home2-footer-top-section` + `.footer-top-wrapper` | `.home2-footer-top-section` | yes (44 / 41) | Toggles `.active` on the footer-top wrap, ≥768px. |
| `.team-img-area` | `.team-img-area` | yes (92 rules) | Toggles `.active` on itself, ≥768px. |
| `.single-portfolio2` | — | yes (45 rules) | Hover moves `.active` between cards. Document-wide. |
| `.portfolio-wrap .single-portfolio` | `.portfolio-wrap` | yes (46 / 41) | Cursor-following image; requires the hovered item's **second child** (`children[1]`) to be the floating image. |
| `.industries-wrap .single-industries` | — | **NO CSS AT ALL** | Dead. The markup does not exist in this template build. Do not use. |

**The `.home4-banner-video` one is the most dangerous.** It sets a module-level
`stickyLock` that the global scroll listener (`custom.js:79-91`) reads to decide whether
`header.sticky` may be applied. Adding `.home4-banner-video` to a page changes header
behaviour for that whole page.

---

## A18. Chrome behaviours (already in the partials — do not re-implement)

All bound in `custom.js`, all markup already in `chrome-top.html` / `chrome-bottom.html`:

* `.sidebar-button` → toggles `.active` on itself and `.show-menu` on `.main-menu`;
  `.menu-close-btn` removes it.
* `.right-sidebar-button` / `.right-sidebar-close-btn` → `.show-right-menu` on
  `.right-sidebar-menu`.
* `.dropdown-icon` → slideToggle on the next `ul, .mega-menu, .mega-menu2` and closes siblings.
* `.dropdown-icon2` → slideToggle on the next `.submenu-list`.
* `.portfolio-drop-down` → slideToggle on the sibling `.sub-menu` (delegated, so it works on
  injected markup).
* `.language-btn` → toggles `.active` on `.language-list`; closes on outside click.
* `header.header-area, header.home4-sticky` → `.sticky` toggled at `scrollY > 0`.
  **`site-fixes.css` styles `header.home3-header` — the FP header carries both
  `header-area` and `home3-header`.**
* `#scroll-percentage` / `#scroll-percentage-value` → conic-gradient progress ring, `.active`
  past 50px, `.is-complete` at 100%, click scrolls to top. Uses `var(--primary-color1)` and
  `var(--progress-bg)`.
* `$("select").niceSelect()` — any `<select>` you add is auto-upgraded. If you need a native
  select, you cannot have one.

## A19. Throwable physics box (homepage About card)

`js/matter.min.js` + `js/Throwable.min.js` (+ `throwable-helper.js`, which only exports
`window.egensDebounce`). Driven by two attributes read by `Throwable.min.js`, **not** by
`custom.js`:

```html
<div class="throwable-box-wrap">
    <div class="throwable-item-wrap" data-eg-throwable-scene="true">
        <p data-eg-throwable-el><span class="throwable-item">End-to-End Expertise</span></p>
        <p data-eg-throwable-el><span class="terracotta throwable-item">Premium Quality</span></p>
        <p data-eg-throwable-el><span class="periwinkle throwable-item">Customised Solutions</span></p>
        <p data-eg-throwable-el><span class="muted-green throwable-item">Innovation &amp; Creativity</span></p>
        <p data-eg-throwable-el><span class="aqua-green throwable-item">Manufacturing Excellence</span></p>
        <p data-eg-throwable-el><span class="green throwable-item">Global Partnership</span></p>
    </div>
</div>
```

* `data-eg-throwable-scene="true"` on the container, `data-eg-throwable-el` on each `<p>`.
  Those are the only two attribute names in the minified file.
* Colour variants confirmed in `style.css` (`.throwable-item`, 10 rules):
  `terracotta`, `periwinkle`, `muted-green`, `aqua-green`, `green` — plus the default (no
  modifier). **These five are the complete set; do not invent another.**
* The scene needs a sized container. On the homepage that is
  `.home4-about-us-section .about-us-left-area .feature-wrap`, which `site-fixes.css:160-178`
  forces to full width with the background image absolutely positioned behind it.

---

## A20. Safe vs. do-not-copy — the short list

### ✅ Safe to reuse on any new page

| hook | why |
|---|---|
| `.fade_anim` + its 6 data-attributes | fully generic, no CSS, no DOM requirements |
| `.text-anim` | generic; keep to headings / one-line paragraphs with no inner markup |
| `.counter` (+ `data-counterup-time`, `data-counterup-delay`) | generic; use inside `.single-countdown > .number` |
| `data-target="#id"` | the only reliable in-page scroll |
| `.wow` + animate.css v3 names + `data-wow-delay` / `data-wow-duration` | generic (but prefer `.fade_anim`) |
| Swiper roots — **one per page**, with the styling class paired on the pagination/nav | see the A6 collision table first |
| `.shape-hover-item` / `.shape-hover-img` | inside a `.blog-card.style-2` or `.blog-card.home4-blog-card` shell only |
| `.marquee` / `.marquee__group` | inside `.partner-section .partner-wrap` only, on a white background |
| `data-fancybox="gallery-01"` | that exact value only |
| `.magnetic-item`, `data-cursor`, `.cursor-alter`, `.hide-cursor`, `.not-hide-cursor` | desktop-only enhancement; never load-bearing |
| `.our-work-list` / `.our-work-img`, `.award-list` / `.award-img` | one pair per page, image list ≥ text list |
| `.lazy-bg-video` | one per page |
| `.throwable-item-wrap` scene | needs a sized container |
| SVG `<animateMotion>` connectors | renumber every id |

### ⛔ Wired to one homepage section — do NOT copy blindly

| hook | why |
|---|---|
| **`.portfolioCard` / `.porfolio-card-wrapper`** | `gsap.utils.toArray(".portfolioCard")` is document-wide; **one stack per page**, and the height fix in `site-fixes.css:341-353` is scoped to `.home4-portfolio-section`. Copying the markup without extending that rule makes cards bleed out of the stack. |
| **`.home4-banner-video` / `.home4-banner-video-full`** | mutates the global `stickyLock`, changing header behaviour for the whole page. |
| **`.home1-process-section` / `.home3-process-section`** | pin-and-count machinery that requires an exact `.process-wrapper > .process-list > .single-process` + `.process-count > span` tree; a partial copy silently does nothing or pins the wrong element. |
| **`.home2-footer-top-section` + `.footer-top-wrapper`**, **`.team-img-area`** | `querySelector` singular + hard-coded `.active` toggling; only meaningful with the template's exact section. |
| **`.industries-wrap` / `.single-industries`** | JS handler exists, **no CSS at all**. Dead. |
| **`.cursor-drag` / `.cursor-drag-mouse-down` / `data-simulate-touch`** | JS exists, no CSS, no markup anywhere. Dead. |
| **`.counter_number`** | no CSS, no usage, integers only, no tunables. Use `.counter`. |
| **`href="#anchor"`** | cancelled by the magic-cursor handler on desktop. Use `data-target`. |

---

## A21. Known defects in `custom.js` (leave alone unless briefed, but know they exist)

1. **`followImageCursor` is declared twice** (lines 1009 and 1026) in the same IIFE scope.
   The second declaration wins for *both* loops, so `.portfolio-wrap .single-portfolio`
   items rotate `5deg` (the industries value) rather than the intended `-19deg`.
2. **`setInterval(followImageCursor(event, item), 100)`** (lines 1018, 1034) calls the
   function immediately and passes its `undefined` return to `setInterval`, registering a
   dead 100ms timer **on every mousemove event**. This leaks timers on any page using
   `.portfolio-wrap .single-portfolio`. (Not the homepage.)
3. **`window.onload = () => {…}`** for `.progress-bar` (line 1040) is an assignment, not
   `addEventListener` — it clobbers/gets clobbered by other load handlers.
4. **Two WOW instances** are initialised (lines 432 and 441); reveal callbacks run twice.
5. The `offset` key is set twice in the WOW config (`0` then `80`); `80` wins.
6. `$('a[href^="#"]').on("click", … return false)` disables all in-page anchors on desktop
   with no replacement scroll. See A7/A15.
7. Every `new Swiper(...)` is assigned to the same `var swiper`; only the last instance is
   reachable from that variable. Harmless — nothing reads it.
8. Several source comments are in Bengali (left from the template author). Ignore them.

---
---

# PART B — ASSETS

Dimensions measured with Pillow 12.3.0. Sizes are on-disk.

## B1. First Perfumes brand & identity

| file | px | size | notes |
|---|---|---|---|
| `images/header-logo.svg` | vector | 24.9 KB | crimson script "F" monogram over `FIRST / PERFUMES IND LLC`. Used in the header. |
| `images/header-logo.webp` | 200×152 | 4.3 KB | RGBA raster of the same mark. Used in `.right-sidebar-menu` for both `.logo-dark` and `.logo-light`. |
| `images/footer-logo.svg` | vector | 5.6 KB | footer lockup |
| `images/white-logo.svg` | vector | 5.5 KB | **unreferenced.** Reversed lockup — use on any dark panel. |
| `images/fav-icon.webp` | 20×20 | 0.3 KB | favicon in use |
| `images/fav-icon.svg` | vector | 0.6 KB | **unreferenced** — better favicon source than the 20px raster |
| `images/fav-icon.jpg` | 20×20 | 1.3 KB | **unreferenced**, redundant |

## B2. Certification badges — RGBA, 300×300, transparent

`fda.webp` (USA FDA Approved Facility), `iso.webp` (ISO 22716:2007), `cpnp.webp` (EU Cosmetic
Product Notification Portal), `cgmp.webp` (Current Good Manufacturing Practice Certified),
`scpn.webp` (UK Cosmetic Product Notification). 10.7–14.9 KB each.

All five are in the homepage hero under `ul.author-img-grp`. Transparent background, so they
sit on any panel colour. **Reuse:** about, manufacturing, faq, contact, and every expertise
sub-page — these are the site's strongest trust signal.

## B3. Facility & manufacturing photography (FP-specific, in use)

Every one is a 678×544 crop except where noted — that is the `.portfolioCard .portfolio-img`
slot on the homepage.

| file | px | size | depicts | best pages |
|---|---|---|---|---|
| `facility-jebel-ali.webp` | 678×544 | 122 KB | the Jebel Ali building exterior, FIRST PERFUMES signage in English + Arabic | manufacturing, about, contact (all three already preload it) |
| `rnd-lab.webp` | 678×544 | 189 KB | gloved hand pipetting into a flask beside a microscope | fragrance-development, manufacturing |
| `perfume-compounding.webp` | 678×544 | 232 KB | operator hand at a machine control panel, amber bottle on the line | perfume-manufacturing, manufacturing |
| `cosmetics-care.webp` | 1240×953 | 39 KB | two lab technicians titrating green liquid into a cylinder | cosmetics-personal-care |
| `quality-lab.webp` | 678×544 | 208 KB | graduated cylinders of green/yellow liquid, gloved hands with a dropper | manufacturing, faq |
| `bottle-decor.webp` | 678×544 | 282 KB | gloved hand spray-lacquering a pink bottle behind a spray-booth curtain | bottle-decoration |
| `packaging-unit.webp` | 678×544 | 150 KB | empty conveyor / packaging line, shallow depth of field | packaging-filling |
| `production-lines.webp` | 678×544 | 244 KB | gloved hands loading bottles onto the filling line | expertise (already its preload) |
| `about.webp` | 640×460 | 126 KB | monochrome row of bottles on a lit production line | about (already its preload); currently the `.feature-wrap` background on the homepage |
| `legacy-perfumer.webp` | 1224×1763 | 150 KB | **unreferenced.** Overhead flat-lay of ~8 coloured FP bottles with gold caps on marble. Portrait. The single best "product family" hero in the library. | about, products, fine-fragrances, oriental-fragrances |
| `sustainability-env.webp` | 1024×972 | 55 KB | **unreferenced.** Hand holding a bottle, sustainability icons in hexagons over a green bokeh background | about, packaging-filling, an ESG block |
| `compliance-global.webp` | 892×832 | 25 KB | **unreferenced.** Pink/magenta bottle-shaped globe with world map and location pins | manufacturing, faq, a "global markets" block |
| `sketchup.webp` | 1917×1917 | 31 KB | **unreferenced.** White line-art technical drawing of a bottle on a faint grid | any "development / design" block. **Note:** the comment at `site-fixes.css:166` ("The sketch is white line art on white") describes *this* file, but the About card currently renders `about.webp`. One of the two is stale — worth a decision. |
| `media/video-poster.webp` | 1280×720 | 24 KB | FP-branded poster frame: technician holding a yellow flask, FIRST PERFUMES logo overlay | poster for `.lazy-bg-video` (in use) |
| `media/video-poster.jpg` | 1280×720 | 50 KB | same frame, JPEG. Redundant fallback. |

## B4. Template stock — abstract 3D renders (✅ REPLACED)

These filenames used to hold the purchased template's placeholder art: neon cubes, rainbow
gradients, a black cauldron, a marble sculpture, a tote bag reading "Place your design here".
None of them related to fragrance manufacturing and all of them were on the live homepage.

**They have been replaced in place** by real First Perfumes photography centre-cropped to the
*exact* pixel dimensions of the file each one replaces — so no CSS or markup changed. The
replacement is already baked into `images/`; the template originals and the full-resolution
PDF source library they were cut from have both been deleted from the repo. Recover them from
the vendor template or the company profile PDF if a re-crop is ever needed.

| files | px | now shows |
|---|---|---|
| `our-work-img.webp` … `our-work-img6.webp` | 424×515 | FP bottle flat-lay, filled bottles on the line, gift boxes, personal-care tray, gold-capped bottle, capping machine |
| `our-work-right-img1.webp` … `-img6.webp` | 285×264 | the same six subjects at the smaller crop |
| `blog-img.webp`, `blog-img2.webp`, `blog-img3.webp` | 424×367 | sustainability hexagons, the bottle-globe, the bottle range |
| `home4-portfolio-img.webp` … `-img4.webp` | 678×544 | gift boxes, compounding tanks, bottle loading, dosing head |

`project-img*.webp` (1096×1308) were **not** remapped — every source photograph is smaller
than that, so a replacement would be an upscale. No page references them and the unreferenced
ones have been deleted; treat whatever remains as dead.

**Rule for new pages:** `alt` text must describe the photograph that is there now, not the
template render the filename was originally named for.

## B5. Template stock — people & awards (unreferenced)

| files | px | depicts |
|---|---|---|
| `team-img.webp` … `team-img8.webp` | 648×725 | eight neon-lit studio portraits of models, heavy magenta/cyan gels. Editorial, not corporate. |
| `mega-menu-people-img1..8.webp` | 51×51 – 63×63 | tiny circular avatars — **in use**, in the header mega menu |
| `award-img.webp` … `award-img5.webp` | 349×564 | **replaced.** Were five "person holding a trophy" stock shots; now lab and line photography (cylinders, conveyor, control panel, microscope, assembly team). Used by `bottle-decoration` and `oriental-fragrances`. |

The unreferenced members of this family — `counter-people-img1..3.webp`,
`testimonial-author-img*.webp` and `about-us-img.webp` — have been deleted.

`pages.json` preloads `team-img.webp` for **our-team**. That page will need real portraits —
the template's neon-gel models will not read as perfumers and chemists.

## B6. Template stock — portfolio/project renders (partly replaced)

`home4-portfolio-img.webp` … `-img4.webp` (678×544) held abstract product renders; they now
hold real facility photography (see B4) and are safe to use in any feature slot.

The surviving `project-img*.webp` files (1096×1308) are still the template's originals — a
marble sculpture, a soda can, a tote-bag mockup, a VR headset. **Do not reference them.** No
page does. They were left in place rather than upscaled from a smaller source.

## B7. Backgrounds, textures and vectors (mostly CSS `url()`, not markup)

| file | px | size | used by |
|---|---|---|---|
| `banner-bg_1.webp` | 1860×793 | 31 KB | `.home3-banner-section .banner-wrapper` — **the homepage hero background** |
| `banner-bg.webp` | 7680×4492 | **5.0 MB** | `.home1-banner-section` only. ⚠ Not used by this site. If anyone ever adds `.home1-banner-section`, that page ships a 5 MB background. Do not use that section. |
| `banner-bg_3.webp` | 1920×1090 | 193 KB | `.home5-banner-section .banner-content-wrapper` |
| `banner-bg-dark.webp` / `-dark_1.webp` | 1920×1123 / 1920×1090 | 5.9 / 13.8 KB | `body.dark` variants |
| `banner-card-bg.webp` / `-dark.webp` | 1008×288 | 1.8 / 1.0 KB | `.banner-card-section .banner-card` |
| `service-inner-banner-card-bg.webp` | 1008×288 | 10.7 KB | inner service banner card |
| `banner-image-mask.webp` | 1520×580 | 2.3 KB | RGBA mask |
| `footer-bg.webp` / `-bg_1.webp` / `-bg-dark.webp` | 1920×647 | 11 / 15 / 20 KB | footer panel |
| `footer-top-bg.webp` | 1920×703 | 7.4 KB | `.footer-top-*` |
| `counter-area-bg.webp` / `-bg2.webp` | 204×194 / 204×188 | 0.3 KB | counter band texture |
| `team-area-bg.webp` | 1860×863 | 3.3 KB | team section bg. **Preloaded by the careers page.** |
| `project-area-bg.webp` | 1860×1127 | 41.5 KB | project section bg |
| `innerpage-our-work-bg.webp` | 1920×942 | 4.3 KB | inner our-work bg |
| `portfolio-details-banner-card.webp` | 509×304 | 1.0 KB | portfolio details |
| `customer-satisfaction.webp` | 178×217 | 4.4 KB | flat green texture, RGBA |
| `project-completed.webp` | 178×188 | 0.2 KB | flat texture |
| `process-area-vector.png` | 510×705 | 4.0 KB | decorative |
| `video-area-vector.png` | 875×480 | 3.3 KB | decorative |
| `check-icon.svg` / `check-icon-white.svg` | vector | 0.2 KB | list bullets, via CSS |
| `footer-vector.svg` / `-vector1.svg` / `-vector2.svg` | vector | 0.6–0.8 KB | footer flourishes |
| `boxicons.svg` | vector | **1.2 MB** | referenced by `css/boxicons.min.css`. Font files are in `fonts/`. |
| `start-up/hover-img-shape2.webp` | 512×512 | 4.0 KB | **the displacement map for `.shape-hover-img`.** In use. |

Deleted as unreferenced: `process-img-dark.webp`, `hover-line.svg` / `hover-line-white.svg`,
`start-up/hover-img-shape2.png` (a redundant PNG copy of the displacement map), and the
third-party review-platform logos `clutchco-logo.svg`, `clutchco-logo-dark.svg`,
`google-logo.svg` — those last three should not go back on the site unless First Perfumes
actually holds those profiles.

## B8. `media/` — video and the company profile PDF

`media/` now holds exactly four files, all of them live:

| file | size | notes |
|---|---|---|
| `first-perfumes-web.mp4` | 8.8 MB | the homepage `.lazy-bg-video` |
| `video-poster.webp` | 24 KB | poster frame for that video |
| `video-poster.jpg` | 50 KB | JPEG fallback of the same frame |
| `First Perfumes Ind.pdf` | 5.0 MB | the company profile, linked from the footer. **ASCII-safe filename — keep it that way.** |

Removed in the cleanup: two intermediate video encodes and the 31.9 MB original master
(`first-perfumes-optimized.mp4`, `First Perfumes LLC - Best Manufacturing Company.mp4`), the
template stock `home3-video.mp4`, two byte-identical copies of the PDF whose filenames carried
an en-dash and a mojibake version of it, and `media/extracted_pdf_images/` +
`media/pdf_content.json` — the scratch library the page copy and photography were cut from.
Everything they fed has already been baked into `images/`; the company profile PDF is still in
the repo if any of it needs to be re-extracted.

### The former `media/extracted_pdf_images/` library (historical)

These 28 full-resolution originals were lifted from the company profile PDF and are **no
longer in the repo**. The table is kept as a map of what page of the PDF each subject came
from, so a future re-extraction can find the same frame without re-deriving it. Dimensions are
in each filename.

| file | depicts | suggested use |
|---|---|---|
| `page_1_img_1_853x696.jpeg` | FIRST PERFUMES logo lockup | reference only (use the SVG) |
| `page_17_img_1_655x464.jpeg` | the same logo, smaller | reference only |
| `page_2_img_1_1224x1763.jpeg` | flat-lay of coloured FP bottles on marble | **products / fine-fragrances hero.** Already downsized to `images/legacy-perfumer.webp` |
| `page_3_img_1_2490x917.jpeg` | Jebel Ali facility exterior, wide | **manufacturing page banner** — the widest FP asset in the repo |
| `page_4_img_1_661x778.jpeg` | filling line, gloved hands, yellow-capped bottles | perfume-manufacturing |
| `page_4_img_2_811x775.jpeg` | stainless dosing head over a red vessel | perfume-manufacturing, fragrance-development |
| `page_4_img_3_661x769.jpeg` | graduated cylinders, green and yellow liquid | fragrance-development, quality/faq |
| `page_5_img_1_652x778.jpeg` | empty conveyor, packaging line | packaging-filling |
| `page_5_img_2_811x778.jpeg` | capping / labelling machine, operator's gloved hand | packaging-filling |
| `page_5_img_3_661x778.jpeg` | row of stainless compounding tanks | manufacturing, perfume-manufacturing |
| `page_6_img_1_2189x463.png` | all five certification badges as one strip | compliance strip on any page |
| `page_7_img_1_1058x962.jpeg` | operator loading bottles into the filler | perfume-manufacturing |
| `page_7_img_2_1050x962.jpeg` | filled bottles queued on the line | products, manufacturing |
| `page_8_img_1_799x1047.jpeg` | machine control panel with an amber bottle | manufacturing |
| `page_8_img_2_567x501.jpeg` | capping head descending onto bottles | packaging-filling |
| `page_8_img_3_567x501.jpeg` | gloved hand adjusting a gold-capped bottle | packaging-filling, bottle-decoration |
| `page_9_img_1_1240x953.jpeg` | technician titrating green liquid | cosmetics-personal-care (already `images/cosmetics-care.webp`) |
| `page_10_img_1_1124x962.jpeg` | luxury rigid gift boxes, navy/red/black, flat-lay | **packaging-filling hero, and the best replacement for the abstract `our-work-*` art** |
| `page_11_img_1_760x560.jpeg` | filling line, two bottles mid-fill | perfume-manufacturing |
| `page_11_img_2_768x560.jpeg` | line of workers assembling product on a green conveyor | about, careers, manufacturing |
| `page_11_img_3_768x560.jpeg` | spray-lacquering a pink bottle | bottle-decoration (already `images/bottle-decor.webp`) |
| `page_12_img_1_540x525.jpeg` | gloved hands with a white cream jar | cosmetics-personal-care |
| `page_12_img_2_540x531.jpeg` | cosmetics bench, pink bottle and botanicals | cosmetics-personal-care |
| `page_12_img_3_541x525.jpeg` | microscope, flasks of coloured liquid | fragrance-development, R&D (already `images/rnd-lab.webp`) |
| `page_13_img_1_1273x710.jpeg` | red tray of white cosmetic tubes and jars | cosmetics-personal-care, private-label |
| `page_14_img_1_1024x972.jpeg` | hand holding a bottle, sustainability icon hexagons | sustainability block (already `images/sustainability-env.webp`) |
| `page_15_img_1_892x832.jpeg` | pink bottle-globe with world map and pins | global markets block (already `images/compliance-global.webp`) |
| `page_16_img_1_1560x2247.jpeg` | hand spraying perfume against a pale sky, portrait | **insights / article-details hero, or a lifestyle banner.** Tallest asset in the library. |

`media/pdf_content.json` held the extracted text from the same PDF — copy source, not an
asset. It has been deleted too.

## B9. Missing files

**Nothing referenced by `index.html` is missing.** All 47 HTML-side references resolve.

Four `url()` references in `css/style.css` point at files that are **not on disk**:

| reference | selector | risk |
|---|---|---|
| `../images/banner-bg_2.png` | `.home4-banner-section` (`style.css:12433`) | **do not use `.home4-banner-section`** — its background will 404 |
| `../images/home2-testimonial-bg.png` | home2 testimonial section | avoid that section, or add the file |
| `../images/home2-testimonial-bg-dark.png` | dark variant of the same | as above |
| `../images/mega-menu-support-area-bg.png` | mega-menu support panel | the FP mega menu does not use that panel — currently harmless |

These are pre-existing template gaps, not regressions. They only bite if a page author adopts
one of those four sections.

## B10. Weight to watch

* `images/banner-bg.webp` — **5.0 MB, 7680×4492.** Still on disk because `css/style.css`
  references it from `.home1-banner-section`; no page on this site uses that section, so it
  never ships. Downsizing it (or dropping the rule and the file together) is the single
  biggest win left.
* `js/three.js` — **1.8 MB, unminified**, loaded on every page for one effect: the WebGL
  displacement hover on the three homepage blog cards (see A10). Swapping in a minified build,
  or loading it only on `index.html`, would cut more weight than every image change combined.
* `images/boxicons.svg` — 1.2 MB, pulled by `css/boxicons.min.css`. The site uses `bi-*`
  (Bootstrap Icons) classes in the chrome; if no `bx-*` class survives, both the boxicons CSS
  and this sprite can go.
* The homepage's own manufacturing photos are 120–282 KB each at only 678×544 — heavier than
  they need to be for that crop. Re-encoding at quality ~80 would roughly halve them.

## B11. Page-to-asset map (from `pages.json` preloads)

| slug | preloaded hero | status |
|---|---|---|
| index | `banner-img-slide.webp` | ✅ FP product photography |
| about | `about.webp` | ✅ FP |
| expertise | `production-lines.webp` | ✅ FP |
| fragrance-development | `rnd-lab.webp` | ✅ FP |
| perfume-manufacturing | `perfume-compounding.webp` | ✅ FP |
| private-label-solutions | `home4-portfolio-img.webp` | ⚠ template stock (VR headset) — replace |
| cosmetics-personal-care | `cosmetics-care.webp` | ✅ FP |
| packaging-filling | `packaging-unit.webp` | ✅ FP |
| bottle-decoration | `bottle-decor.webp` | ✅ FP |
| manufacturing | `facility-jebel-ali.webp` | ✅ FP |
| products | `our-work-img.webp` | ⚠ abstract render — replace |
| fine-fragrances | `our-work-img.webp` | ⚠ abstract render — replace |
| oriental-fragrances | `our-work-img2.webp` | ⚠ abstract render — replace |
| home-lifestyle | `our-work-img3.webp` | ⚠ abstract render — replace |
| private-label | `our-work-img4.webp` | ⚠ abstract render — replace |
| insights | `blog-img.webp` | ⚠ abstract render — replace |
| article-details | `blog-img.webp` | ⚠ abstract render — replace |
| our-team | `team-img.webp` | ⚠ neon-gel stock portraits — replace |
| careers | `team-area-bg.webp` | texture, acceptable |
| contact | `facility-jebel-ali.webp` | ✅ FP |
| faq, privacy-policy, terms-conditions, support-policy, 404 | none | fine |

The three homepage banner slides (`banner-img-slide.webp`, `-slide2.webp`, `-slide3.webp`,
all 860×793) are FP-appropriate perfumery photography: amber liquid in laboratory glassware,
a copper distillation column, and a white flat-lay of clear bottles. Reuse them freely for
inner-page heroes at that aspect ratio.
