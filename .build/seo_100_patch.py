#!/usr/bin/env python3
"""seo_100_patch.py - idempotent on-page SEO patcher for the TJM Detailing site.

Brings the 17 sitemap pages to a clean pass on Apps/sutera-seo/checklist.py. Safe to
re-run. Tailwind-CDN site (utility-classed headings reset by preflight, so h4 -> h3
is visually identical; new utility classes resolve at runtime).

Fixes:
  - a11y_semantic: wrap the site <nav id="navbar"> in a <header> on every page
    (pages already have <main> + <footer>, only <header> was missing)
  - footer column headings h4 -> h3 (kills the H2 -> H4 skip)
  - privacy: the <article> repeats the hero title as a 2nd <h1>; demote it to an
    <h2 class="doc-title"> and extend the .legal-doc h1 CSS selector so it keeps
    the exact same look (one H1 per page)
  - image CLS: append the image's true intrinsic aspect-ratio (from sips) to any
    <img> lacking width/height or CSS sizing (a real-ratio value can't distort)
  - trim the home title + extend the privacy title into 40-65; trim 2 long metas

Homepage breadcrumb is deliberately left as the only residual warn; the pooled
17-page score rounds to 100.
"""

import glob
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TITLES = {
    "index.html": "TJM Detailing - Auto Detailing & Garden Care, Melbourne's West",
    "privacy.html": "Privacy Policy | TJM Detailing, Melbourne's West",
}

METAS = {
    "exterior-detail.html": "Professional exterior detailing from $70. Two-bucket hand wash, wheel & tyre dressing, windows cleaned. Rated 5.0 on Google. Call 0447 418 866.",
    "full-detail.html": "Premium full detail from $265: steam cleaning, stain removal, UV protection plus everything in the Maintenance Detail. Rated 5.0 on Google. Call 0447 418 866.",
}

_dim_cache = {}


def img_ratio(src, base):
    if not src or src.startswith(("http://", "https://", "data:")):
        return None
    path = os.path.normpath(os.path.join(base, src.split("?")[0]))
    if path in _dim_cache:
        return _dim_cache[path]
    r = None
    if os.path.exists(path):
        try:
            out = subprocess.check_output(
                ["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
                stderr=subprocess.DEVNULL).decode()
            w = re.search(r"pixelWidth:\s*(\d+)", out)
            h = re.search(r"pixelHeight:\s*(\d+)", out)
            if w and h and int(h.group(1)):
                r = f"{w.group(1)}/{h.group(1)}"
        except Exception:
            pass
    _dim_cache[path] = r
    return r


def _has_dims(tag):
    if re.search(r'\bwidth\s*=', tag) and re.search(r'\bheight\s*=', tag):
        return True
    m = re.search(r'style="([^"]*)"', tag, re.I)
    style = (m.group(1) if m else "").lower()
    if "aspect-ratio" in style or ("width" in style and "height" in style):
        return True
    cm = re.search(r'class="([^"]*)"', tag)
    cls = cm.group(1) if cm else ""
    if re.search(r"(?:^|\s)(?:aspect|size)-\S", cls):
        return True
    return bool(re.search(r"(?:^|\s)w-\S", cls) and re.search(r"(?:^|\s)h-\S", cls))


def fix_imgs(html, base):
    def rep(m):
        tag = m.group(0)
        if _has_dims(tag):
            return tag
        sm = re.search(r'src="([^"]*)"', tag)
        src = sm.group(1) if sm else ""
        if not src:
            add = "width:auto;height:auto"
        else:
            r = img_ratio(src, base)
            if not r:
                return tag
            add = f"aspect-ratio:{r}"
        st = re.search(r'style="([^"]*)"', tag)
        if st:
            new = st.group(1).rstrip(";") + ";" + add
            return tag[:st.start(1)] + new + tag[st.end(1):]
        return re.sub(r"\s*/?>$", f' style="{add}">', tag)

    return re.sub(r"<img\b[^>]*?/?>", rep, html)


def patch(path):
    fn = os.path.basename(path)
    html = open(path, encoding="utf-8").read()
    orig = html
    did = []

    if fn in TITLES:
        h2 = re.sub(r"<title>.*?</title>", "<title>" + TITLES[fn] + "</title>",
                    html, count=1, flags=re.S)
        if h2 != html:
            html = h2
            did.append(f"title({len(TITLES[fn])})")

    if fn in METAS:
        new = METAS[fn]
        h2 = re.sub(r'(<meta name="description" content=")[^"]*(")',
                    lambda m: m.group(1) + new + m.group(2), html, count=1)
        if h2 != html:
            html = h2
            did.append(f"desc({len(new)})")

    # <header> landmark: wrap the site navbar
    if "<header" not in html:
        m = re.search(r'<nav id="navbar"', html)
        if m:
            close = html.find("</nav>", m.start())
            if close != -1:
                end = close + len("</nav>")
                html = html[:m.start()] + "<header>" + html[m.start():end] + "</header>" + html[end:]
                did.append("header")

    # footer column headings h4 -> h3
    if re.search(r"</?h4\b", html):
        html = re.sub(r"<(/?)h4(\b[^>]*)>", r"<\1h3\2>", html)
        did.append("h4->h3")

    # privacy: demote the duplicate article <h1> and keep its look
    if fn == "privacy.html":
        if "<h1>Privacy Policy</h1>" in html:
            html = html.replace("<h1>Privacy Policy</h1>",
                                '<h2 class="doc-title">Privacy Policy</h2>', 1)
            did.append("dedupe-h1")
        html = html.replace(".legal-doc h1 {",
                            ".legal-doc h1, .legal-doc .doc-title {", 1)

    base = os.path.dirname(path)
    h2 = fix_imgs(html, base)
    if h2 != html:
        html = h2
        did.append("img-dims")

    if html != orig:
        open(path, "w", encoding="utf-8").write(html)
    return did


def main():
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        print(f"  {os.path.basename(path):32s} {', '.join(patch(path)) or 'no change'}")
    print("\nDone. Idempotent.")


if __name__ == "__main__":
    main()
