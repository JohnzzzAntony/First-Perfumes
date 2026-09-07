#!/usr/bin/env python3
"""Replace the purchased template's placeholder art with real First Perfumes photography.

The Softro template shipped abstract stock renders — a soda can, a tote bag mockup
reading "Place your design here", a marble sculpture, stock shots of men holding
trophies — and those files are wired into the homepage's "Products & Solutions"
and "Insights" sections plus seven inner pages. They are documented as off-brand
in `_partials/notes-motion-and-assets.md` (sections B4-B6).

`media/extracted_pdf_images/` holds 28 full-resolution photographs lifted from the
company profile PDF: the Jebel Ali line, the compounding hall, the QC bench, the
gift-box range. This script crops those to the **exact pixel dimensions of the file
each one replaces**, so the swap needs no CSS or markup change.

    python _content/_lib/reimage.py           # write the replacements
    python _content/_lib/reimage.py --dry-run # report what would change

Originals are copied to `images/_template-originals/` before being overwritten.
"""

import os
import shutil
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "media", "extracted_pdf_images")
DEST = os.path.join(ROOT, "images")
BACKUP = os.path.join(DEST, "_template-originals")

# target file -> source photograph. The target's own dimensions are read off disk,
# so a replacement can never change a layout.
MAP = {
    # Homepage "Products & Solutions", left column (424x515 portrait)
    "our-work-img.webp": "page_2_img_1_1224x1763.jpeg",      # fine fragrances
    "our-work-img2.webp": "page_7_img_2_1050x962.jpeg",      # oriental
    "our-work-img3.webp": "page_10_img_1_1124x962.jpeg",     # home & lifestyle
    "our-work-img4.webp": "page_13_img_1_1273x710.jpeg",     # body & personal care
    "our-work-img5.webp": "page_8_img_3_567x501.jpeg",       # private label
    "our-work-img6.webp": "page_5_img_2_811x778.jpeg",       # packaging & decoration
    # Same six subjects in the right column (285x264)
    "our-work-right-img1.webp": "page_2_img_1_1224x1763.jpeg",
    "our-work-right-img2.webp": "page_7_img_2_1050x962.jpeg",
    "our-work-right-img3.webp": "page_10_img_1_1124x962.jpeg",
    "our-work-right-img4.webp": "page_13_img_1_1273x710.jpeg",
    "our-work-right-img5.webp": "page_8_img_3_567x501.jpeg",
    "our-work-right-img6.webp": "page_5_img_2_811x778.jpeg",
    # Homepage "Insights & Trends" cards (424x367)
    "blog-img.webp": "page_14_img_1_1024x972.jpeg",          # sustainability
    "blog-img2.webp": "page_15_img_1_892x832.jpeg",          # global compliance
    "blog-img3.webp": "page_2_img_1_1224x1763.jpeg",         # private label launch
    # Stacked case cards (678x544)
    "home4-portfolio-img.webp": "page_10_img_1_1124x962.jpeg",
    "home4-portfolio-img2.webp": "page_5_img_3_661x778.jpeg",
    "home4-portfolio-img3.webp": "page_7_img_1_1058x962.jpeg",
    "home4-portfolio-img4.webp": "page_4_img_2_811x775.jpeg",
    # `project-img1..5.webp` (the soda can, the tote bag mockup reading "Place your
    # design here", the marble sculpture) are deliberately NOT remapped: at
    # 1096x1308 they are larger than every source photograph, so a replacement
    # would be an upscale. They are dropped from the markup instead.
    # "Person holding a trophy" stock, five files
    "award-img.webp": "page_4_img_3_661x769.jpeg",
    "award-img2.webp": "page_5_img_1_652x778.jpeg",
    "award-img3.webp": "page_8_img_1_799x1047.jpeg",
    "award-img4.webp": "page_12_img_3_541x525.jpeg",
    "award-img5.webp": "page_11_img_2_768x560.jpeg",
}


def cover(img, w, h):
    """Scale to fill w x h and centre-crop the overflow — same as CSS object-fit: cover."""
    sw, sh = img.size
    scale = max(w / sw, h / sh)
    nw, nh = max(w, int(round(sw * scale))), max(h, int(round(sh * scale)))
    img = img.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - w) // 2, (nh - h) // 2
    return img.crop((left, top, left + w, top + h))


def main():
    dry = "--dry-run" in sys.argv[1:]
    if not dry:
        os.makedirs(BACKUP, exist_ok=True)

    done = skipped = 0
    for target, source in sorted(MAP.items()):
        tpath = os.path.join(DEST, target)
        spath = os.path.join(SRC, source)
        if not os.path.exists(tpath):
            print("  skip (no target): %s" % target)
            skipped += 1
            continue
        if not os.path.exists(spath):
            print("  skip (no source): %s" % source)
            skipped += 1
            continue

        with Image.open(tpath) as t:
            w, h = t.size
        before = os.path.getsize(tpath)

        if dry:
            print("  %-28s %4dx%-4d  <- %s" % (target, w, h, source))
            done += 1
            continue

        # keep one copy of the template art before it is overwritten
        bak = os.path.join(BACKUP, target)
        if not os.path.exists(bak):
            shutil.copy2(tpath, bak)

        with Image.open(spath) as im:
            im = im.convert("RGB")
            out = cover(im, w, h)
            # quality 82 lands close to the originals' weight at these crops
            out.save(tpath, "WEBP", quality=82, method=6)

        after = os.path.getsize(tpath)
        print("  %-28s %4dx%-4d  %6.1fKB -> %6.1fKB  <- %s"
              % (target, w, h, before / 1024, after / 1024, source))
        done += 1

    print("\n%s %d file(s), skipped %d" % ("would rewrite" if dry else "rewrote", done, skipped))
    if not dry:
        print("template originals kept in images/_template-originals/")


if __name__ == "__main__":
    main()
