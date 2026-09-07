#!/usr/bin/env python3
"""Report files in images/ and media/ that nothing on the built site references.

Reads every reference out of the built .html pages, the stylesheets' url() calls
and any path literals in js/, then lists what is left over. Reports only — it
deletes nothing, because the leftovers include client source material
(the company profile PDF, the extracted image library) that is worth keeping in
the repository even though it should not be uploaded to the web root.

    python _content/_lib/unused.py
"""

import glob
import os
import re
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEP = os.sep


def referenced():
    used = set()

    def add(u):
        u = urllib.parse.unquote(u.strip().strip("'\"").split("#")[0].split("?")[0])
        used.add(u.replace("../", "").replace("\\", "/").lstrip("./"))

    for p in glob.glob(os.path.join(ROOT, "*.html")):
        s = open(p, encoding="utf-8").read()
        for m in re.findall(r'(?:href|src|poster|data-bg-src)="([^"]+)"', s):
            add(m)
        for m in re.findall(r"url\(([^)]+)\)", s):
            add(m)

    for p in glob.glob(os.path.join(ROOT, "css", "*.css")):
        s = open(p, encoding="utf-8", errors="ignore").read()
        for m in re.findall(r"url\(([^)]+)\)", s):
            add(m)

    for p in glob.glob(os.path.join(ROOT, "js", "*.js")):
        s = open(p, encoding="utf-8", errors="ignore").read()
        for m in re.findall(r"""['"]((?:\.\./)?(?:images|media)/[^'"]+)['"]""", s):
            add(m)

    return used


def main():
    used = referenced()
    rows, total = [], 0
    for d in ("images", "media"):
        for base, _, files in os.walk(os.path.join(ROOT, d)):
            for f in files:
                full = os.path.join(base, f)
                rel = os.path.relpath(full, ROOT).replace(SEP, "/")
                if rel in used:
                    continue
                size = os.path.getsize(full)
                total += size
                rows.append((size, rel))

    rows.sort(reverse=True)
    print("unreferenced: %d file(s), %.1f MB\n" % (len(rows), total / 1048576))
    for size, rel in rows:
        if size < 200 * 1024:
            break
        print("  %8.2f MB  %s" % (size / 1048576, rel))
    small = [r for r in rows if r[0] < 200 * 1024]
    if small:
        print("  + %d file(s) under 200 KB, %.1f MB combined"
              % (len(small), sum(s for s, _ in small) / 1048576))


if __name__ == "__main__":
    main()
