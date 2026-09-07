# _archive

Not part of the site. Nothing here is built, linked or deployed.

## pre-merge-pages/

Five root-level `.html` files left over from the pre-merge version of the site,
moved out of the deploy root on 2026-09-07.

| file | superseded by |
|---|---|
| `our-expertise.html` | `expertise.html` |
| `our-manufacturing-facility.html` | `manufacturing.html` |
| `products-&-solutions.html` | `products.html` |
| `cosmetics.html` | `cosmetics-personal-care.html` |
| `packaging.html` | `packaging-filling.html` |

They were unreachable from the built site (they only linked to each other),
absent from `sitemap.xml`, and did not load `css/site-fixes.css`, so they
rendered with the un-corrected theme layout. `products-&-solutions.html` also
carried an `&` in its filename, which needs escaping in every URL that names it.

Kept as a reference for content that may not have made it into `_content/`.
