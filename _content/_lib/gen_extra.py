#!/usr/bin/env python3
"""Blog, article and contact components. Extends gen.py."""

from gen import esc, ARROW20, btn1_submit


def blog_grid(posts, cols="col-lg-6 col-md-6"):
    """posts: (img, alt, category, date, headline). All link to article-details."""
    out = []
    for n, (img, alt, cat, date, head) in enumerate(posts):
        out.append("""    <div class="%s fade_anim" data-delay=".%d">
        <div class="blog-card2">
            <div class="blog-image-wrap">
                <a href="article-details.html" class="blog-img">
                    <img src="%s" alt="%s" loading="lazy" decoding="async">
                </a>
                <div class="icon">
                    <a href="article-details.html" aria-label="Read the article">%s</a>
                </div>
            </div>
            <div class="blog-content-wrap">
                <ul class="blog-meta">
                    <li><a href="insights.html">%s</a></li>
                    <li>%s</li>
                </ul>
                <h2><a href="article-details.html">%s</a></h2>
            </div>
        </div>
    </div>""" % (cols, 2 + (n % 3), img, esc(alt), ARROW20,
                 esc(cat), esc(date), esc(head)))
    return '<div class="row gy-4">\n%s\n</div>' % "\n".join(out)


def pagination(pages=3):
    items = "\n".join(
        '            <li class="page-item%s"><a href="insights.html">%d</a></li>'
        % (" active" if i == 1 else "", i) for i in range(1, pages + 1))
    return """<div class="pagination-area fade_anim" data-delay=".2">
    <ul class="paginations">
%s
    </ul>
    <div class="paginations-button">
        <a href="insights.html">Next Page %s</a>
    </div>
</div>""" % (items, ARROW20)


def article_body(author, role, date, thumb, thumb_alt, blocks, quote, tags):
    """Uses .details-contnt-wrap — misspelled in style.css, copied verbatim."""
    body = []
    for tag, heading, paras in blocks:
        body.append("            <%s>%s</%s>" % (tag, esc(heading), tag))
        for p in paras:
            body.append("            <p>%s</p>" % p)
        body.append('            <span class="line-break"></span>')
    quote_html = """            <blockquote>
                <div class="content">
                    <h4>%s</h4>
                    <div class="author-area">
                        <h5>%s</h5>
                        <span>%s</span>
                    </div>
                </div>
            </blockquote>""" % (esc(quote), esc(author), esc(role))
    taglis = "\n".join('                    <li><a href="%s">%s</a></li>' % (h, esc(t))
                       for t, h in tags)
    return """<div class="row">
    <div class="col-lg-10">
        <div class="post-author-meta mb-40 fade_anim" data-delay=".2">
            <div class="author-area">
                <div class="author-content">
                    <span>Written by</span>
                    <h2>%s</h2>
                </div>
            </div>
            <div class="post-date">
                <span>Published</span>
                <h2>%s</h2>
            </div>
            <div class="social-area-wrap">
                <div class="social-area">
                    <h2>Share</h2>
                    <ul class="social-list">
                        <li><a href="https://www.linkedin.com/" aria-label="Share on LinkedIn"><i class="bi bi-linkedin"></i></a></li>
                        <li><a href="https://x.com/" aria-label="Share on X"><i class="bi bi-twitter-x"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="article-details-thumb-img mb-40 fade_anim" data-delay=".3">
            <img src="%s" alt="%s" fetchpriority="high" decoding="async">
        </div>
        <div class="details-contnt-wrap fade_anim" data-delay=".2">
%s
%s
            <div class="tag-navigation-area">
                <ul class="tag-list">
%s
                </ul>
            </div>
        </div>
    </div>
</div>""" % (esc(author), esc(date), thumb, esc(thumb_alt),
             "\n".join(body), quote_html, taglis)


def contact_form(interests):
    checks = "\n".join("""                        <li>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="int%d" name="interest" value="%s">
                                <label class="form-check-label" for="int%d">%s</label>
                            </div>
                        </li>""" % (i + 1, esc(x), i + 1, esc(x))
                       for i, x in enumerate(interests))
    return """<!-- The form has no action attribute, so it posts to itself and does nothing.
     Wire it to your own endpoint (or a service such as Formspree) before launch. -->
<div class="contact-form-wrap inner-contact-from fade_anim" data-delay=".2">
    <form method="post">
        <div class="row gy-4">
            <div class="col-md-6">
                <div class="form-inner">
                    <label for="fullName">Full name</label>
                    <input type="text" id="fullName" name="fullName" placeholder="Your name" required>
                </div>
            </div>
            <div class="col-md-6">
                <div class="form-inner">
                    <label for="company">Company</label>
                    <input type="text" id="company" name="company" placeholder="Your brand or company">
                </div>
            </div>
            <div class="col-md-6">
                <div class="form-inner">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" placeholder="you@company.com" required>
                </div>
            </div>
            <div class="col-md-6">
                <div class="form-inner">
                    <label for="phone">Phone</label>
                    <input type="tel" id="phone" name="phone" placeholder="+971 00 000 0000">
                </div>
            </div>
            <div class="col-lg-12">
                <div class="form-inner">
                    <label for="enquiryType">Enquiry type</label>
                    <select id="enquiryType" name="enquiryType">
                        <option value="private-label">Private label programme</option>
                        <option value="fragrance-development">Fragrance development</option>
                        <option value="manufacturing">Manufacturing capacity</option>
                        <option value="packaging">Packaging and decoration</option>
                        <option value="visit">Facility visit</option>
                        <option value="other">Something else</option>
                    </select>
                </div>
            </div>
            <div class="col-lg-12">
                <div class="form-inner">
                    <label for="message">Tell us about the project</label>
                    <textarea id="message" name="message" placeholder="Volumes, target markets, timeline, and anything already decided" required></textarea>
                </div>
            </div>
            <div class="col-lg-12">
                <div class="form-inner2">
                    <label>I am interested in</label>
                    <ul>
%s
                    </ul>
                </div>
            </div>
            <div class="col-lg-12">
                <div class="form-inner2">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="consent" name="consent" required>
                        <label class="form-check-label" for="consent">I agree to the <a href="privacy-policy.html">Privacy Policy</a> and consent to being contacted about this enquiry.</label>
                    </div>
                </div>
            </div>
            <div class="col-lg-12">
                %s
            </div>
        </div>
    </form>
</div>""" % (checks, btn1_submit("Send Enquiry"))


def contact_details():
    """Address / phone / email columns above the form."""
    def card(title, lines, href, label):
        body = "\n".join("                    <p>%s</p>" % x for x in lines)
        return """    <div class="col-lg-4 col-md-6 fade_anim" data-delay=".2">
        <div class="details-content">
            <h3>%s</h3>
%s
            <a href="%s">%s</a>
        </div>
    </div>""" % (esc(title), body, href, esc(label))
    return """<div class="row gy-4">
%s
%s
%s
</div>""" % (
        card("Visit the facility",
             ["Land Area Industrial First, Plot No 969",
              "Jebel Ali, Dubai, United Arab Emirates"],
             "https://www.google.com/maps", "Open in Google Maps"),
        card("Call us",
             ["Sunday to Thursday, 8:00 to 18:00 Gulf Standard Time",
              "Closed Friday and Saturday"],
             "tel:+97142211787", "+971 4 221 1787"),
        card("Email us",
             ["We reply to every enquiry within one business day.",
              "For press and partnerships, use the same address."],
             "mailto:info@firstperfumes.com", "info@firstperfumes.com"))


def map_embed():
    return """<div class="row">
    <div class="col-lg-12 fade_anim" data-delay=".2">
        <div class="service-details-img">
            <iframe title="First Perfumes Ind LLC location in Jebel Ali, Dubai" src="https://www.google.com/maps?q=Jebel+Ali+Industrial+First+Dubai&amp;output=embed" width="100%" height="450" style="border:0" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
    </div>
</div>"""
