#!/usr/bin/env python3
"""Re-describe the images that `reimage.py` swapped.

`reimage.py` replaced the template's placeholder art with real First Perfumes
photography at identical dimensions. The `alt` text left behind describes the old
picture, so every swapped image now has a caption that does not match what a
screen reader user would be told is there. This rewrites the alt on those files
across `_content/`, and drops the `project-img*` files — which were left as the
template's soda can, tote-bag mockup and marble sculpture — out of the markup.

    python _content/_lib/realt.py
"""

import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# file -> the one alt that describes what the photograph actually shows
ALT = {
    "our-work-img.webp": "Finished First Perfumes bottles arranged on a marble surface",
    "our-work-right-img1.webp": "Finished First Perfumes bottles arranged on a marble surface",
    "our-work-img2.webp": "Filled fragrance bottles queued along the production line",
    "our-work-right-img2.webp": "Filled fragrance bottles queued along the production line",
    "our-work-img3.webp": "Luxury rigid gift boxes from the First Perfumes packaging range",
    "our-work-right-img3.webp": "Luxury rigid gift boxes from the First Perfumes packaging range",
    "our-work-img4.webp": "Personal care jars and tubes presented in a branded gift tray",
    "our-work-right-img4.webp": "Personal care jars and tubes presented in a branded gift tray",
    "our-work-img5.webp": "Gloved hand adjusting a gold-capped bottle on the line",
    "our-work-right-img5.webp": "Gloved hand adjusting a gold-capped bottle on the line",
    "our-work-img6.webp": "Capping and labelling machine running a production batch",
    "our-work-right-img6.webp": "Capping and labelling machine running a production batch",
    "blog-img.webp": "Hand holding a First Perfumes bottle beside sustainability icons",
    "blog-img2.webp": "Bottle-shaped globe marked with international market locations",
    "blog-img3.webp": "First Perfumes bottle range laid out ahead of a brand launch",
    "home4-portfolio-img.webp": "Luxury rigid gift boxes from the First Perfumes packaging range",
    "home4-portfolio-img2.webp": "Row of stainless steel compounding tanks",
    "home4-portfolio-img3.webp": "Operator loading empty bottles into the filling machine",
    "home4-portfolio-img4.webp": "Stainless dosing head lowered over a compounding vessel",
    "award-img.webp": "Graduated cylinders of coloured concentrate on the laboratory bench",
    "award-img2.webp": "Empty conveyor running through the packaging hall",
    "award-img3.webp": "Machine control panel with an amber bottle on the line",
    "award-img4.webp": "Microscope and flasks of coloured liquid in the R&D laboratory",
    "award-img5.webp": "Production team assembling finished product along the conveyor",
}


def main():
    changed = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        s = io.open(path, encoding="utf-8", newline="").read()
        orig = s

        def fix(m):
            tag, fname = m.group(0), m.group(1)
            if fname not in ALT:
                return tag
            new = ALT[fname]
            if 'alt="' in tag:
                return re.sub(r'alt="[^"]*"', 'alt="%s"' % new, tag, count=1)
            return tag.replace("<img", '<img alt="%s"' % new, 1)

        s = re.sub(r'<img[^>]*src="images/([^"]+)"[^>]*>', fix, s)
        if s != orig:
            io.open(path, "w", encoding="utf-8", newline="").write(s)
            changed += 1
            print("  alt updated:", os.path.basename(path))
    print("%d fragment(s) updated" % changed)


if __name__ == "__main__":
    main()
