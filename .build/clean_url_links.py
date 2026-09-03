#!/usr/bin/env python3
"""
clean_url_links.py - point every internal reference at the URL the host actually
serves, instead of the one that 308-redirects to it.

WHY. As of 2026-09-03 Google Search Console reported 16 TJM pages as "URL is
unknown to Google" - among them /about, /auto-detailing and eight car-detailing
suburb pages, the oldest live for 31 days. It was not robots.txt (Allow: /), not
the sitemap (all 49 clean URLs are in it) and not the canonicals (69df153 already
fixed those). It was discovery: every internal link, every og:url and every
BreadcrumbList item still named the `.html` form, and the host 308s `.html` to the
extension-less URL. So the only path Google had into a page was a redirect, and
the clean URL - the one the canonical and the sitemap both nominate - was never
linked from anywhere on the site. Google knew the redirecting alias and had never
been handed the destination.

WHAT IT REWRITES, and nothing else:

    href="page.html"     -> href="/page"        (index.html -> "/")
    <meta og:url ...>    -> the clean URL
    JSON-LD "url"/"item" -> the clean URL

Every `.html` reference on this site is internal, flat and free of anchors and
query strings (checked before writing this), so the rewrite is a strip, not a
resolve. Anything with a scheme other than the site's own domain is left alone.

Idempotent - a second run finds nothing to do. Dry run by default, --apply writes.
"""

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://tjmdetailing.com.au"

# href="slug.html" or href="/slug.html" -> href="/slug"; index.html -> "/"
HREF = re.compile(r'(href\s*=\s*")(?:\./)?/?([A-Za-z0-9._-]+)\.html(")')
# Absolute self-referencing URLs inside content="" and JSON-LD "url"/"item".
ABS = re.compile(r'(' + re.escape(DOMAIN) + r'/)([A-Za-z0-9._-]+)\.html\b')


def clean_href(m):
    slug = m.group(2)
    return m.group(1) + ("/" if slug == "index" else "/" + slug) + m.group(3)


def clean_abs(m):
    slug = m.group(2)
    return m.group(1) + ("" if slug == "index" else slug)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    total = 0
    touched = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        txt = open(path, encoding="utf-8").read()
        new, n1 = HREF.subn(clean_href, txt)
        new, n2 = ABS.subn(clean_abs, new)
        n = n1 + n2
        if not n:
            continue
        touched += 1
        total += n
        print("  %-46s %4d  (%d href, %d absolute)"
              % (os.path.basename(path), n, n1, n2))
        if args.apply:
            open(path, "w", encoding="utf-8").write(new)

    print("\n%d reference(s) across %d file(s)%s"
          % (total, touched, "" if args.apply else "  [dry run - use --apply]"))

    if args.apply:
        # Nothing may name a .html URL afterwards. A leftover means a form this
        # script does not understand, and a silent partial sweep is worse than none.
        left = []
        for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
            txt = open(path, encoding="utf-8").read()
            for m in re.finditer(r'(?:href\s*=\s*"[^"]*|' + re.escape(DOMAIN)
                                 + r'/[^"\s]*)\.html\b', txt):
                left.append("%s: %s" % (os.path.basename(path), m.group(0)[:70]))
        if left:
            print("\nFAIL - %d reference(s) survived the sweep:" % len(left))
            for line in left[:20]:
                print("  " + line)
            return 1
        print("verified: no internal reference names a .html URL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
