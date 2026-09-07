#!/usr/bin/env python3
"""
Car Wash x suburb landing-page generator for TJM Detailing.

Why this exists rather than an extension of suburb_render.py: that generator lifts a
`tailwind.config` <script> out of interior-detail.html, and the Tailwind precompile
(commit 3821891) removed it, so suburb_render.py now aborts on every run. Until it is
repaired, a new page has to take its chrome from a page that is actually live. This
follows the Radiant Rides precedent (gen_car_detailing_suburbs.py): clone the chrome
from a committed page, inject hand-written copy.

Cloning a LIVE page also keeps the pages precompile-safe. styles.css only contains the
utility classes Tailwind could see when it was compiled, so a class this generator
invents would silently do nothing. Every class used here is already on the reference
page.

"Car wash" is the search term; the product is TJM's Exterior Detail - a two-bucket
hand wash, wheels and tyres dressed, windows and door jambs cleaned, dried by hand,
from $70. The copy says so plainly and links to the service page rather than implying
a separate cheaper offering that does not exist.

Run:  python3 .build/gen_car_wash_suburbs.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
REF = os.path.join(ROOT, "exterior-detailing-werribee.html")
DOMAIN = "https://tjmdetailing.com.au"
PHONE_TEL = "0447418866"
PHONE = "0447 418 866"
GA4 = "G-GCCC696KEN"
LOGO = f"{DOMAIN}/Assets/TJM%20detailing%20logo%20FA.png"
HERO_IMG = "Assets/Auto Detailing/Exterior Detail 2.jpg"

# ── Chrome, lifted verbatim from a live page ──────────────────────────────────
_ref = open(REF, encoding="utf-8").read()


def _grab(pat, name):
    m = re.search(pat, _ref, re.S)
    if not m:
        raise SystemExit(f"Could not extract {name} from {os.path.basename(REF)}")
    return m.group(1)


STYLE_BLOCK = _grab(r"(<style>[\s\S]*?</style>)", "style block")
NAV = _grab(r'(<header><nav id="navbar"[\s\S]*?</nav></header>)', "nav")
FOOTER = _grab(r"(<footer[\s\S]*?</footer>)", "footer")
SCRIPTS = _grab(r"</footer>([\s\S]*?)</body>", "trailing scripts")

# GA4 base tag plus the sitewide lead-events block. The suburb pages were generated
# before that block existed, so they are the 34 pages on this site still missing it -
# new pages ship with it so click_to_call actually fires on their tel: buttons.
HEAD_TRACKING = f"""  <!-- Google tag (gtag.js) - GA4 {GA4} -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA4}');
  </script>

  <!-- Sutera lead events (GA4) -->
  <script>/* SUTERA_LEAD_EVENTS */
  (function(){{
    function ev(n, p){{ if (typeof window.gtag === 'function') {{ window.gtag('event', n, Object.assign({{transport_type:'beacon'}}, p||{{}})); }} }}
    document.addEventListener('click', function(e){{
      var a = e.target.closest ? e.target.closest('a[href^="tel:"]') : null;
      if (a) ev('click_to_call', {{ link_url: a.getAttribute('href') }});
    }}, true);
    document.addEventListener('submit', function(e){{
      var f = e.target;
      if (!f || f.tagName !== 'FORM' || f.hasAttribute('data-no-lead')) return;
      var action = f.getAttribute('action') || '';
      var isLead = /formspree/i.test(action) || f.querySelector('input[type="email"], input[type="tel"], textarea');
      if (isLead) ev('generate_lead', {{ form_id: f.id || f.getAttribute('name') || 'contact' }});
    }}, true);
  }})();
  </script>"""

# Prices are facts, shared: straight off exterior-detail.html and the site CLAUDE.md.
PRICES = [("Hatch / Sedan", "$70"), ("SUV / 4WD", "$80"), ("7 Seater", "$90")]

# Everything else is per page. Two adjacent suburbs sharing one block of service prose
# is how a doorway-page footprint gets built, and the validation gate fails it on sight.
# Each page therefore answers different questions and leads on a different angle.

PAGES = [
    {
        "slug": "car-wash-werribee",
        "suburb": "Werribee",
        "hero_sub": "A proper hand car wash that comes to your driveway in Werribee. No queue, no brushes, no drive-through.",
        "intro_h2": "A hand car wash that comes to you in Werribee",
        "intro": [
            "The problem with getting the car washed is rarely the washing. It is the queue at the servo, the drive there and back, and the swirl marks the spinning brushes leave in your clear coat for the privilege.",
            "TJM is based in Werribee, so this is our own street. The van arrives at your house or your workplace carrying its own water and power, the car is washed by hand in your driveway, and you get your Saturday morning back.",
            "The service behind the search term is our Exterior Detail. Same wash, same price, listed under the name people actually type into Google. It starts at $70 and takes about an hour.",
        ],
        "included_h2": "What the wash covers",
        "included": [
            ("Foam pre wash", "The car gets a foam pre wash before anything touches it, so the grit that would otherwise be dragged across your paint is lifted off first."),
            ("Two buckets, not one", "Soap in one, clean water in the other, and the mitt rinsed between every panel. It is the single biggest difference between a wash that protects paint and one that slowly ruins it."),
            ("Wheels, barrels and tyres", "Brake dust cleaned off the faces and inside the barrels, then the tyres dressed so the car looks finished rather than merely wet."),
            ("Glass and door jambs", "Exterior glass cleaned and the jambs wiped out. The jambs are the tell: it is the part a drive-through cannot physically reach, so it is the part that gives a cheap wash away."),
            ("Dried by hand", "Towelled off panel by panel, because leaving a car to air dry is what puts the water spots back on within a day."),
        ],
        "why_h2": "Why Werribee books TJM",
        "why_cards": [
            ("This is the home base", "The van is already in Werribee, so this is the suburb with the earliest slots and the best chance of fitting you in at short notice."),
            ("Home or workplace", "Plenty of Werribee washes happen in a work car park during the day rather than at home on the weekend. Either suits, as long as we can park beside the car."),
            ("Rated 5.0 on Google", "100% 5-star reviews from drivers across Melbourne's west."),
            ("Fully insured", "Professional, insured and reliable, so your car is in safe hands while you get on with something else."),
        ],
        "faq_h2": "Car washing in Werribee, answered",
        "faq": [
            ("How much is a car wash in Werribee?",
             "It is $70 for a hatch or sedan, $80 for an SUV or 4WD and $90 for a 7 seater. That covers the full hand wash including wheels, tyres, glass and door jambs. Prices may vary on inspection."),
            ("Can you wash the car at my work instead of home?",
             "Yes, and in Werribee that is a common booking. As long as there is space to park beside the vehicle and we are allowed on site, the car park works as well as the driveway."),
            ("Do you need my tap or my power point?",
             "No. The van carries its own water and power, so nothing is run off your place unless you would prefer we used your tap."),
            ("Can I book a regular wash rather than a one-off?",
             "Yes. A lot of Werribee customers settle into a fortnightly or monthly wash, which is the point at which the car stops ever really getting dirty. Just say so when you book and we will keep the slot."),
            ("How far ahead do I need to book?",
             "Usually a few days. Werribee is where we are based so short-notice jobs are easiest here, but weekends fill first, so a Saturday needs more warning than a Wednesday."),
        ],
        "related": [
            ("Exterior Detailing Werribee", "The same wash listed under its detailing name, with the full process broken down.", "/exterior-detailing-werribee"),
            ("Car Detailing Werribee", "Inside and out in one visit, for when the cabin needs the attention too.", "/car-detailing-werribee"),
        ],
    },
    {
        "slug": "car-wash-hoppers-crossing",
        "suburb": "Hoppers Crossing",
        "hero_sub": "A proper hand car wash at your place in Hoppers Crossing. We bring the water, the power and the buckets.",
        "intro_h2": "A hand car wash that comes to you in Hoppers Crossing",
        "intro": [
            "Most cars around Hoppers Crossing get cleaned one of two ways. Badly, at an automatic bay on the way home from somewhere else, or not at all, because nobody has a spare hour to sit and watch it happen.",
            "Booking a mobile wash removes the errand entirely. We are ten minutes up the road in Werribee, the van turns up self-contained, and the car is washed by hand where it is already parked.",
            "What arrives is our Exterior Detail under the name people search for: a two-bucket hand wash with the wheels, tyres, glass and jambs done properly, from $70.",
        ],
        "included_h2": "What you get for the money",
        "included": [
            ("Nothing touches dry paint", "A foam pre wash goes on first and does the loosening, so the wash mitt is never the thing dragging road grit across your panels."),
            ("The two-bucket method", "The mitt is rinsed in clean water before it goes back into the soap, every panel. Skip that step and you are effectively sanding the car every time you wash it."),
            ("Wheels done properly", "Faces and barrels cleared of brake dust, tyres dressed afterwards. Clean paint above dirty wheels never looks right."),
            ("The bits machines miss", "Exterior glass and the door jambs, which no drive-through can reach, and which are the first thing anyone notices when they open the door."),
            ("Hand dried", "The car is towelled dry rather than left to spot in the sun, which is the difference between clean on the day and clean by Tuesday."),
        ],
        "why_h2": "Why Hoppers Crossing books TJM",
        "why_cards": [
            ("Ten minutes away", "Hoppers Crossing sits right next to the Werribee base, so it is one of the suburbs the van is in most weeks and slots are rarely hard to find."),
            ("Driveways, units and car parks", "The setup is self-contained, so a townhouse driveway or a unit car park works the same as a big suburban block."),
            ("Rated 5.0 on Google", "Every review the business has ever received is a five star one, left by drivers right across the west."),
            ("Fully insured", "Professional, insured and reliable, with the same care taken on a work ute as on a weekend car."),
        ],
        "faq_h2": "Common questions from Hoppers Crossing",
        "faq": [
            ("What does a car wash cost in Hoppers Crossing?",
             "$70 for a hatch or sedan, $80 for an SUV or 4WD, $90 for a 7 seater, with wheels, tyres, glass and door jambs included. Prices may vary on inspection."),
            ("What happens if it rains on the day?",
             "We will call and move it. Washing a car in the rain wastes your money, so it gets rescheduled to the next slot that suits rather than pushed through."),
            ("I live in a unit with a shared car park. Is that a problem?",
             "Not usually. The van brings its own water and power, so all that is needed is room to work around the car and permission to be there."),
            ("Can you do more than one car in the same visit?",
             "Yes, and it is worth doing. Two cars at the same address in one visit saves the second trip, so it is easier to book and quicker on the day."),
            ("Is this the same thing as your exterior detail?",
             "It is the same service. Exterior Detail is what it is called on the price list, car wash is what people search for, and both land on the same hand wash from $70."),
        ],
        "related": [
            ("Exterior Detailing Hoppers Crossing", "This wash written up as a detail, step by step, if you want the longer version.", "/exterior-detailing-hoppers-crossing"),
            ("Car Detailing Hoppers Crossing", "Add the interior and have the whole car done in a single visit.", "/car-detailing-hoppers-crossing"),
        ],
    },
]


def build_head(p):
    suburb = p["suburb"]
    title = f"Car Wash {suburb} - Mobile Hand Wash | TJM Detailing"
    desc = (f"Mobile hand car wash in {suburb} from $70. We come to you Wed-Sun with our own "
            f"water and power. Fully insured, rated 5.0 on Google. Call {PHONE}.")
    url = f"{DOMAIN}/{p['slug']}"

    service = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f"Car Wash - {suburb}",
        "serviceType": "Car Wash",
        "description": (f"Mobile hand car wash in {suburb}, Victoria by TJM Detailing. Two-bucket hand "
                        f"wash, wheels and tyres, glass and door jambs, dried by hand. We come to your "
                        f"home or workplace. Fully insured, open Wednesday to Sunday."),
        "provider": {
            "@type": "LocalBusiness",
            "name": "TJM Detailing",
            "telephone": "+61447418866",
            "image": LOGO,
            "url": f"{DOMAIN}/",
            "areaServed": {"@type": "Place", "name": f"{suburb}, Victoria, Australia"},
            "priceRange": "$$",
        },
        "areaServed": {"@type": "Place", "name": f"{suburb}, Victoria, Australia"},
        "offers": [
            {"@type": "Offer", "name": f"Car Wash - {label}", "price": price.lstrip("$"),
             "priceCurrency": "AUD"}
            for label, price in PRICES
        ],
    }
    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
            {"@type": "ListItem", "position": 2, "name": "Auto Detailing", "item": f"{DOMAIN}/auto-detailing"},
            {"@type": "ListItem", "position": 3, "name": f"Car Wash {suburb}", "item": url},
        ],
    }
    faqs = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faq"]
        ],
    }

    return f"""{HEAD_TRACKING}
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" sizes="32x32" href="Assets/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="Assets/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="Assets/apple-touch-icon.png">
    <link rel="shortcut icon" href="Assets/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{LOGO}">
    <meta property="og:locale" content="en_AU">
    <meta property="og:site_name" content="TJM Detailing">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{LOGO}">
    <meta name="geo.region" content="AU-VIC">
    <meta name="geo.placename" content="{suburb}, Victoria">
<link rel="stylesheet" href="styles.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Teko:wght@400;500;600;700&display=swap" rel="stylesheet">
{STYLE_BLOCK}
    <script type="application/ld+json">
{json.dumps(service, indent=4)}
    </script>
    <script type="application/ld+json">
{json.dumps(crumbs, indent=4)}
    </script>
    <script type="application/ld+json">
{json.dumps(faqs, indent=4)}
    </script>"""


def build_body(p):
    suburb = p["suburb"]

    intro_html = "\n                ".join(f'<p class="text-g mb-4">{t}</p>' for t in p["intro"])

    included_html = "\n".join(
        f"""                <div class="border-t border-black/10 pt-4">
                    <h3 class="font-display text-2xl font-bold text-gray-900 mb-2">{name}</h3>
                    <p class="text-g">{body}</p>
                </div>"""
        for name, body in p["included"]
    )

    price_html = "\n".join(
        f"""                <div class="bg-white border border-black/10 rounded-2xl p-6 text-center">
                    <div class="text-g text-sm font-semibold tracking-wide uppercase mb-2">{label}</div>
                    <div class="font-display text-5xl font-bold text-gray-900">{price}</div>
                    <div class="text-g text-sm mt-2">Hand wash, wheels, tyres, glass</div>
                </div>"""
        for label, price in PRICES
    )

    why_html = "\n".join(
        f"""                <div class="bg-white border border-black/10 rounded-2xl p-6">
                    <h3 class="font-display text-2xl font-bold text-gray-900 mb-2">{name}</h3>
                    <p class="text-g">{body}</p>
                </div>"""
        for name, body in p["why_cards"]
    )

    faq_html = "\n".join(
        f"""                <details class="bg-white border border-black/10 rounded-2xl p-6">
                    <summary class="flex items-start justify-between cursor-pointer">
                        <h3 class="font-display text-xl md:text-2xl font-semibold text-gray-900 pr-6">{q}</h3>
                    </summary>
                    <p class="text-g mt-4">{a}</p>
                </details>"""
        for q, a in p["faq"]
    )

    related_html = "\n".join(
        f"""                <a href="{href}" class="group block bg-white border border-black/10 rounded-2xl p-6">
                    <h3 class="font-display text-2xl font-bold text-gray-900 group-hover:text-r" style="transition: color 0.3s ease;">{name}</h3>
                    <p class="text-g mt-2">{body}</p>
                </a>"""
        for name, body, href in p["related"]
    )

    return f"""

    <main id="main">

    <!-- BREADCRUMB -->
    <nav aria-label="Breadcrumb" class="max-w-7xl mx-auto px-5 sm:px-8 pt-24 md:pt-28 pb-2 text-sm text-g">
        <a href="/" class="hover:text-r" style="transition:color .3s">Home</a>
        <span class="mx-2 text-g/40">/</span>
        <a href="/auto-detailing" class="hover:text-r" style="transition:color .3s">Auto Detailing</a>
        <span class="mx-2 text-g/40">/</span>
        <span class="text-gray-900">Car Wash {suburb}</span>
    </nav>

    <!-- HERO -->
    <section class="relative grain overflow-hidden bg-black">
        <div class="absolute inset-0"><img src="{HERO_IMG}" alt="Mobile hand car wash in {suburb} by TJM Detailing" class="w-full h-full object-cover opacity-40"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/70 to-black/40"></div>
        <div class="relative max-w-7xl mx-auto px-5 sm:px-8 py-20 md:py-28">
            <div class="inline-flex items-center gap-2 bg-r/15 border border-r/30 rounded-full px-3 py-1 mb-5 reveal">
                <span class="w-1.5 h-1.5 rounded-full bg-r"></span>
                <span class="text-white/90 text-[11px] font-bold tracking-[0.2em] uppercase">Mobile &bull; {suburb}</span>
            </div>
            <h1 class="font-display text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-bold leading-[0.9] text-white mb-5 reveal reveal-delay-1">Car Wash in<br>{suburb}</h1>
            <p class="text-white/70 text-lg md:text-xl max-w-2xl mb-8 reveal reveal-delay-2">{p['hero_sub']}</p>
            <div class="flex flex-wrap gap-4 reveal reveal-delay-3">
                <a href="tel:{PHONE_TEL}" class="btn-red text-base">Call {PHONE}</a>
                <a href="/contact" class="btn-outline text-base" style="color:#fff;border-color:rgba(255,255,255,0.25)">Book Online</a>
            </div>
        </div>
    </section>

    <!-- INTRO + INCLUDES -->
    <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-24">
        <div class="grid lg:grid-cols-2 gap-12 lg:gap-16 items-start">
            <div class="reveal">
                <h2 class="font-display text-4xl md:text-5xl font-bold text-gray-900 mb-5">{p['intro_h2']}</h2>
                {intro_html}
            </div>
            <div class="reveal reveal-delay-1 grid gap-5">
{included_html}
            </div>
        </div>
    </section>

    <!-- PRICING -->
    <section class="bg-d-900 border-y border-black/8">
        <div class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-24">
            <h2 class="font-display text-4xl md:text-5xl font-bold text-gray-900">Car wash prices in {suburb}</h2>
            <p class="text-g mt-3 mb-8 max-w-2xl">Priced by vehicle size, quoted before we start. Prices may vary upon inspection of the vehicle. Bookings essential.</p>
            <div class="grid sm:grid-cols-3 gap-5">
{price_html}
            </div>
        </div>
    </section>

    <!-- WHY -->
    <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-24">
        <h2 class="font-display text-4xl md:text-5xl font-bold text-gray-900 max-w-2xl mb-8">{p['why_h2']}</h2>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
{why_html}
        </div>
    </section>

    <!-- FAQ -->
    <section class="bg-d-900 border-y border-black/8">
        <div class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-24">
            <h2 class="font-display text-4xl md:text-5xl font-bold text-gray-900 mb-8">{p['faq_h2']}</h2>
            <div class="grid gap-4 max-w-4xl">
{faq_html}
            </div>
        </div>
    </section>

    <!-- RELATED -->
    <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-20">
        <h2 class="font-display text-3xl md:text-4xl font-bold text-gray-900 mb-6 reveal">More in {suburb}</h2>
        <div class="grid sm:grid-cols-2 gap-5">
{related_html}
        </div>
    </section>

    <!-- CTA -->
    <section class="bg-black">
        <div class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-24 text-center">
            <h2 class="font-display text-4xl md:text-6xl font-bold text-white mb-4 reveal">Book a wash in {suburb}</h2>
            <p class="text-white/70 text-lg max-w-2xl mx-auto mb-8 reveal reveal-delay-1">Wednesday to Sunday, 8am to 5pm. Call and we will find you a slot, or book online and we will confirm it.</p>
            <div class="flex flex-wrap gap-4 justify-center reveal reveal-delay-2">
                <a href="tel:{PHONE_TEL}" class="btn-red text-lg px-8 py-4">Call {PHONE}</a>
                <a href="/contact" class="btn-outline text-lg px-8 py-4" style="color:#fff;border-color:rgba(255,255,255,0.25)">Book Online</a>
            </div>
        </div>
    </section>

    </main>

"""


def build_page(p):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{build_head(p)}
</head>

<body class="antialiased overflow-x-hidden">
<a href="#main" class="skip-to-content">Skip to content</a>
{NAV}
{build_body(p)}
{FOOTER}
{SCRIPTS}</body>
</html>
"""


def update_sitemap(slugs):
    path = os.path.join(ROOT, "sitemap.xml")
    xml = open(path, encoding="utf-8").read()
    added = []
    for slug in slugs:
        loc = f"{DOMAIN}/{slug}"
        if loc in xml:
            continue
        entry = (f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>2026-09-07</lastmod>\n"
                 f"    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n")
        xml = xml.replace("</urlset>", entry + "</urlset>")
        added.append(slug)
    if added:
        open(path, "w", encoding="utf-8").write(xml)
    return added


def main():
    only = set(sys.argv[1:])
    written = []
    for p in PAGES:
        if only and p["slug"] not in only:
            continue
        out = os.path.join(ROOT, f"{p['slug']}.html")
        html = build_page(p)
        open(out, "w", encoding="utf-8").write(html)
        written.append(p["slug"])
        print(f"Wrote {p['slug']}.html ({html.count(chr(10)) + 1} lines, {len(html)} chars)")
    added = update_sitemap(written)
    print(f"sitemap.xml: {len(added)} new url(s)" if added else "sitemap.xml: unchanged")


if __name__ == "__main__":
    main()
