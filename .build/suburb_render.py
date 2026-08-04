#!/usr/bin/env python3
"""
Service x suburb landing-page generator for TJM Detailing.

Creates one local landing page per (detailing service x Wyndham suburb) under the
site root as <service-slug>-<suburb-slug>.html, matching the existing site chrome
(nav, footer, styles, scripts extracted verbatim from interior-detail.html) and
injecting localized, service-specific content.

Scope (per James 2026-08-04): the 3 core detailing services - Car Detailing,
Interior Detailing, Exterior Detailing - across all 11 City of Wyndham suburbs = 33 pages.

TJM is a MOBILE detailer (comes to the customer) based in Werribee, servicing
Melbourne's west Wed-Sun. Every page is framed "we come to you in <suburb>".

Run:  python3 .build/suburb_render.py
"""
import os
import re
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
REF = os.path.join(ROOT, "interior-detail.html")
DOMAIN = "https://tjmdetailing.com.au"
PHONE_TEL = "0447418866"
PHONE = "0447 418 866"

# ── Extract chrome verbatim from the reference page ───────────────────────────
_ref = open(REF, encoding="utf-8").read()
def _grab(pat, name):
    m = re.search(pat, _ref, re.S)
    if not m:
        raise SystemExit("Could not extract " + name + " from interior-detail.html")
    return m.group(1)

TAILWIND_CONFIG = _grab(r'(<script>\s*tailwind\.config[\s\S]*?</script>)', "tailwind config")
STYLE_BLOCK = _grab(r'(<style>[\s\S]*?</style>)', "style block")
NAV = _grab(r'(<header><nav id="navbar"[\s\S]*?</nav></header>)', "nav")
FOOTER = _grab(r'(<footer[\s\S]*?</footer>)', "footer")
SCRIPTS = _grab(r'(<!-- ============ SCRIPTS ============ -->[\s\S]*?</script>)', "scripts")

GA4 = '''  <!-- Google tag (gtag.js) - GA4 G-GCCC696KEN -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-GCCC696KEN"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-GCCC696KEN');
  </script>'''

FONTS = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Teko:wght@400;500;600;700&display=swap" rel="stylesheet">'''

# ── Services (3) ──────────────────────────────────────────────────────────────
SERVICES = {
    "car-detailing": {
        "name": "Car Detailing", "term_ok": "car-detailing",
        "hero_img": "Assets/Auto Detailing/Full Detail2.jpg",
        "price_from": "70",
        "hero_sub": "Mobile car detailing that comes to you in {sub}. Interior, exterior and full details, done at your home or workplace.",
        "intro1": "Looking for professional car detailing in {sub}? TJM Detailing brings a complete mobile detailing setup to your driveway. From a quick interior refresh to a full interior and exterior detail, we clean your car properly, at a time and place that suits you.",
        "intro2": "We are a fully insured, 5-star rated local detailer based just up the road in Werribee, looking after {sub} and the wider Wyndham area Wednesday to Sunday. Every detail is done by hand with quality products and genuine attention, never a rushed production line.",
        "inc_title": "What a car detail includes",
        "includes": ["Pre wash and two-bucket exterior hand wash", "Wheels and tyres cleaned and dressed",
                     "Windows cleaned inside and out", "Door jambs wiped down",
                     "Full interior vacuum: seats, carpet, boot and mats", "Dashboard, centre console and trims wiped down",
                     "Vehicle dried by hand"],
        "inc_note": "Packages range from a $70 interior or exterior detail up to a full detail. We tailor the detail to your car and budget.",
        "tiers": [("Interior or Exterior Detail", "from $70"), ("Maintenance Detail", "from $110"), ("Full Detail", "from $265")],
        "related": ["interior-detailing", "exterior-detailing"],
        "faq": [
            ("How much does car detailing cost in {sub}?",
             "Our detailing packages start from $70 for an interior or exterior detail, $110 for a maintenance detail, and $265 for a full detail. Final pricing depends on your vehicle size and condition, confirmed on inspection."),
            ("How long does a car detail take?",
             "A single interior or exterior detail takes around an hour, a maintenance detail around 90 minutes to 2 hours, and a full detail 2.5 to 3 hours. We will give you a clear estimate when you book."),
        ],
    },
    "interior-detailing": {
        "name": "Interior Detailing", "term_ok": "interior-detail",
        "hero_img": "Assets/Auto Detailing/Interior Detail 4.jpg",
        "price_from": "70",
        "hero_sub": "Mobile interior car detailing in {sub}. Vacuumed, wiped down and fresh, done at your place.",
        "intro1": "Want the inside of your car looking and feeling new again? TJM Detailing offers professional interior detailing in {sub}, coming to your home or workplace with everything needed to deep clean your cabin.",
        "intro2": "Based in nearby Werribee and fully insured, we look after {sub} drivers Wednesday to Sunday. Seats, carpets, boot, mats, dash and trims, all cleaned by hand with real care and a 5.0 Google rating behind us.",
        "inc_title": "What an interior detail includes",
        "includes": ["Vacuum of seats, under seats, carpet, boot, floor mats and compartments",
                     "Wipe down of dashboard, centre console and trims", "Windows cleaned (inside)"],
        "inc_note": "Interior detailing is priced by vehicle size. Prices may vary upon inspection.",
        "tiers": [("Hatch / Sedan", "$70"), ("SUV / 4WD", "$80"), ("7 Seater", "$90")],
        "related": ["car-detailing", "exterior-detailing"],
        "faq": [
            ("How much is an interior detail in {sub}?",
             "Interior detailing starts at $70 for a hatch or sedan, $80 for an SUV or 4WD, and $90 for a 7 seater. Prices may vary on inspection if the interior needs extra work."),
            ("How long does an interior detail take?",
             "Most interior details take around an hour. Heavily soiled interiors can take a little longer, and we will let you know before we start."),
        ],
    },
    "exterior-detailing": {
        "name": "Exterior Detailing", "term_ok": "exterior-detail",
        "hero_img": "Assets/Auto Detailing/Exterior Detail.jpg",
        "price_from": "70",
        "hero_sub": "Mobile exterior car detailing in {sub}. Hand washed, wheels and tyres dressed, windows clear.",
        "intro1": "Give your car a proper exterior clean without leaving home. TJM Detailing provides mobile exterior detailing in {sub}, a careful two-bucket hand wash that lifts dirt and protects your paint.",
        "intro2": "We are a local, fully insured detailer based in Werribee, servicing {sub} and across Wyndham Wednesday to Sunday. No automatic brushes or rushed jobs, just a proper hand wash and dress done right.",
        "inc_title": "What an exterior detail includes",
        "includes": ["Pre wash to loosen dirt", "Two-bucket exterior hand wash", "Wheel and tyre dressing",
                     "Windows cleaned (exterior)", "Door jambs cleaned", "Vehicle dried by hand"],
        "inc_note": "Exterior detailing is priced by vehicle size. Prices may vary upon inspection.",
        "tiers": [("Hatch / Sedan", "$70"), ("SUV / 4WD", "$80"), ("7 Seater", "$90")],
        "related": ["car-detailing", "interior-detailing"],
        "faq": [
            ("How much is an exterior detail in {sub}?",
             "Exterior detailing starts at $70 for a hatch or sedan, $80 for an SUV or 4WD, and $90 for a 7 seater. Prices may vary on inspection."),
            ("Do you use an automatic car wash?",
             "No. Every exterior detail is a careful two-bucket hand wash, which is far gentler on your paint than an automatic brush wash."),
        ],
    },
}

# Shared FAQ appended to every page (localized)
def shared_faq(sub):
    return [
        ("Do you come to me in {sub}?".format(sub=sub),
         "Yes. TJM Detailing is a mobile detailer, so we bring everything to your home or workplace in {sub}. You just need a safe, off-street spot for us to work.".format(sub=sub)),
        ("What days are you available?",
         "We operate Wednesday to Sunday, 8am to 5pm. Bookings are essential, so it is best to book ahead to lock in your preferred time."),
        ("Are you insured?",
         "Yes. TJM Detailing is fully insured and rated 5.0 on Google, so your car is in safe, professional hands."),
    ]

# ── Suburbs (11, all of Wyndham) ──────────────────────────────────────────────
SUBURBS = [
    {"name": "Werribee", "slug": "werribee", "pc": "3030",
     "angle": "Werribee is our home base, so {sub} bookings get the fastest turnaround and priority times."},
    {"name": "Werribee South", "slug": "werribee-south", "pc": "3030",
     "angle": "Just south of our Werribee base, {sub} is an easy, quick call-out for our mobile team."},
    {"name": "Hoppers Crossing", "slug": "hoppers-crossing", "pc": "3029",
     "angle": "Hoppers Crossing is only minutes from our Werribee base, so we detail here all the time."},
    {"name": "Point Cook", "slug": "point-cook", "pc": "3030",
     "angle": "We detail across Point Cook's estates and streets every week, coming straight to your driveway."},
    {"name": "Tarneit", "slug": "tarneit", "pc": "3029",
     "angle": "Tarneit is one of Wyndham's fastest-growing suburbs and a regular stop for our mobile setup."},
    {"name": "Truganina", "slug": "truganina", "pc": "3029",
     "angle": "We bring the full detailing setup to homes and workplaces right across Truganina."},
    {"name": "Williams Landing", "slug": "williams-landing", "pc": "3027",
     "angle": "Williams Landing sits close to our Werribee base and the freeway, making it an easy trip for us."},
    {"name": "Wyndham Vale", "slug": "wyndham-vale", "pc": "3024",
     "angle": "We service Wyndham Vale's growing estates right at your home, no need to drive anywhere."},
    {"name": "Manor Lakes", "slug": "manor-lakes", "pc": "3024",
     "angle": "We reach the newer Manor Lakes estates and detail right at your place."},
    {"name": "Mambourin", "slug": "mambourin", "pc": "3024",
     "angle": "Mambourin is one of Wyndham's newest pockets, and yes, we come to you here too."},
    {"name": "Little River", "slug": "little-river", "pc": "3211",
     "angle": "We travel out to Little River, bringing the complete mobile detailing setup with us."},
]
SUB_BY_SLUG = {s["slug"]: s for s in SUBURBS}


def li_list(items):
    return "\n".join(
        '                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-r flex-shrink-0 mt-0.5" '
        'fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" '
        'stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg><span class="text-g">' + it + '</span></li>'
        for it in items)


def tiers_html(tiers):
    rows = []
    for label, price in tiers:
        rows.append(
            '                    <div class="flex items-center justify-between border-b border-black/8 py-3">'
            '<span class="text-gray-900 font-medium">' + label + '</span>'
            '<span class="font-display text-2xl font-bold text-r">' + price + '</span></div>')
    return "\n".join(rows)


def faq_pairs(svc, sub):
    pairs = [(q.format(sub=sub), a.format(sub=sub)) for q, a in svc["faq"]]
    pairs += shared_faq(sub)
    return pairs


def faq_html(pairs):
    out = []
    for q, a in pairs:
        out.append(
            '                <details class="group border-b border-black/8 py-5">\n'
            '                    <summary class="flex items-center justify-between cursor-pointer list-none">'
            '<h3 class="font-display text-xl md:text-2xl font-semibold text-gray-900 pr-6">' + q + '</h3>'
            '<svg class="w-5 h-5 text-r flex-shrink-0 transition-transform group-open:rotate-180" fill="none" '
            'stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" '
            'stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></summary>\n'
            '                    <p class="text-g mt-3 max-w-3xl">' + a + '</p>\n'
            '                </details>')
    return "\n".join(out)


def faq_jsonld(pairs):
    items = [{"@type": "Question", "name": q,
              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]
    return json.dumps(items, ensure_ascii=False, indent=8).rstrip()


def other_services_html(svc_slug, sub_slug, sub_name):
    cards = []
    for rel in SERVICES[svc_slug]["related"]:
        r = SERVICES[rel]
        cards.append(
            '                <a href="' + rel + '-' + sub_slug + '.html" class="service-card block bg-white border '
            'border-black/8 rounded-xl p-6 group">\n'
            '                    <h3 class="font-display text-2xl font-bold text-gray-900 group-hover:text-r" '
            'style="transition: color 0.3s ease;">' + r["name"] + ' in ' + sub_name + '</h3>\n'
            '                    <p class="text-g text-sm mt-2">From $' + r["price_from"] + '. Mobile, we come to you.</p>\n'
            '                </a>')
    return "\n".join(cards)


def other_areas_html(svc_slug, this_slug):
    links = []
    for s in SUBURBS:
        if s["slug"] == this_slug:
            continue
        links.append(
            '                <a href="' + svc_slug + '-' + s["slug"] + '.html" class="text-g hover:text-r '
            'text-sm font-medium" style="transition: color 0.3s ease;">' + s["name"] + '</a>')
    return "\n".join(links)


def render(svc_slug, sub):
    svc = SERVICES[svc_slug]
    sub_name = sub["name"]
    slug = svc_slug + "-" + sub["slug"]
    svc_lower = svc["name"].lower()
    title = svc["name"] + " " + sub_name + " - TJM Detailing"
    if len(title) > 60:
        title = svc["name"] + " " + sub_name + " | TJM"
    meta = ("Mobile {s} in {sub} from ${p}. We come to you, Wed-Sun. Fully insured, "
            "rated 5.0 on Google. Call {ph}.").format(s=svc_lower, sub=sub_name, p=svc["price_from"], ph=PHONE)
    pairs = faq_pairs(svc, sub_name)
    canon = DOMAIN + "/" + slug + ".html"

    service_jsonld = {
        "@context": "https://schema.org", "@type": "Service",
        "name": svc["name"] + " - " + sub_name,
        "serviceType": svc["name"],
        "description": ("Mobile " + svc_lower + " in " + sub_name + ", Victoria by TJM Detailing. "
                        "We come to your home or workplace. Fully insured, open Wednesday to Sunday."),
        "provider": {
            "@type": "LocalBusiness", "name": "TJM Detailing", "telephone": "+61447418866",
            "image": DOMAIN + "/Assets/TJM%20detailing%20logo%20FA.png", "url": DOMAIN + "/",
            "areaServed": {"@type": "Place", "name": sub_name + ", Victoria, Australia"},
            "priceRange": "$$",
        },
        "areaServed": {"@type": "Place", "name": sub_name + ", Victoria, Australia",
                       "address": {"@type": "PostalAddress", "addressLocality": sub_name,
                                   "addressRegion": "VIC", "postalCode": sub["pc"], "addressCountry": "AU"}},
        "url": canon,
        "offers": [{"@type": "Offer", "name": t[0], "priceCurrency": "AUD",
                    "price": re.sub(r"[^0-9]", "", t[1])} for t in svc["tiers"]],
    }
    breadcrumb_jsonld = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Auto Detailing", "item": DOMAIN + "/auto-detailing.html"},
            {"@type": "ListItem", "position": 3, "name": svc["name"] + " " + sub_name, "item": canon},
        ],
    }
    faqpage_jsonld = '{\n    "@context": "https://schema.org",\n    "@type": "FAQPage",\n    "mainEntity": ' + faq_jsonld(pairs) + '\n    }'

    head = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
''' + GA4 + '''
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" sizes="32x32" href="Assets/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="Assets/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="Assets/apple-touch-icon.png">
    <link rel="shortcut icon" href="Assets/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@@TITLE@@</title>
    <meta name="description" content="@@META@@">
    <link rel="canonical" href="@@CANON@@">
    <meta property="og:type" content="website">
    <meta property="og:url" content="@@CANON@@">
    <meta property="og:title" content="@@TITLE@@">
    <meta property="og:description" content="@@META@@">
    <meta property="og:image" content="''' + DOMAIN + '''/Assets/TJM%20detailing%20logo%20FA.png">
    <meta property="og:locale" content="en_AU">
    <meta property="og:site_name" content="TJM Detailing">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="@@TITLE@@">
    <meta name="twitter:description" content="@@META@@">
    <meta name="twitter:image" content="''' + DOMAIN + '''/Assets/TJM%20detailing%20logo%20FA.png">
    <meta name="geo.region" content="AU-VIC">
    <meta name="geo.placename" content="@@SUB@@, Victoria">

    <script src="https://cdn.tailwindcss.com"></script>
''' + TAILWIND_CONFIG + '''

''' + FONTS + '''

''' + STYLE_BLOCK + '''
    <script type="application/ld+json">
''' + json.dumps(service_jsonld, ensure_ascii=False, indent=4) + '''
    </script>
    <script type="application/ld+json">
''' + json.dumps(breadcrumb_jsonld, ensure_ascii=False, indent=4) + '''
    </script>
    <script type="application/ld+json">
    ''' + faqpage_jsonld + '''
    </script>
</head>

<body class="antialiased overflow-x-hidden">

    <a href="#main" class="skip-to-content">Skip to content</a>

''' + NAV + '''

    <main id="main">

    <!-- BREADCRUMB -->
    <nav aria-label="Breadcrumb" class="max-w-7xl mx-auto px-5 sm:px-8 pt-24 md:pt-28 pb-2 text-sm text-g">
        <a href="index.html" class="hover:text-r" style="transition:color .3s">Home</a>
        <span class="mx-2 text-g/40">/</span>
        <a href="auto-detailing.html" class="hover:text-r" style="transition:color .3s">Auto Detailing</a>
        <span class="mx-2 text-g/40">/</span>
        <span class="text-gray-900">@@SVC@@ @@SUB@@</span>
    </nav>

    <!-- HERO -->
    <section class="relative grain overflow-hidden bg-black">
        <div class="absolute inset-0"><img src="@@HERO_IMG@@" alt="@@SVC@@ in @@SUB@@ by TJM Detailing" class="w-full h-full object-cover opacity-40"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/70 to-black/40"></div>
        <div class="relative max-w-7xl mx-auto px-5 sm:px-8 py-20 md:py-28">
            <div class="inline-flex items-center gap-2 bg-r/15 border border-r/30 rounded-full px-3 py-1 mb-5 reveal">
                <span class="w-1.5 h-1.5 rounded-full bg-r"></span>
                <span class="text-white/90 text-[11px] font-bold tracking-[0.2em] uppercase">Mobile &bull; @@SUB@@</span>
            </div>
            <h1 class="font-display text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-bold leading-[0.9] text-white mb-5 reveal reveal-delay-1">@@SVC@@ in<br>@@SUB@@</h1>
            <p class="text-white/70 text-lg md:text-xl max-w-2xl mb-8 reveal reveal-delay-2">@@HERO_SUB@@</p>
            <div class="flex flex-wrap gap-4 reveal reveal-delay-3">
                <a href="tel:@@TEL@@" class="btn-red text-base">Call @@PHONE@@</a>
                <a href="contact.html" class="btn-outline text-base" style="color:#fff;border-color:rgba(255,255,255,0.25)">Book Online</a>
            </div>
        </div>
    </section>

    <!-- INTRO + INCLUDES -->
    <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-24">
        <div class="grid lg:grid-cols-2 gap-12 lg:gap-16 items-start">
            <div class="reveal">
                <h2 class="font-display text-4xl md:text-5xl font-bold text-gray-900 mb-5">@@SVC@@, done at your door in @@SUB@@</h2>
                <p class="text-g mb-4">@@INTRO1@@</p>
                <p class="text-g">@@INTRO2@@</p>
            </div>
            <div class="reveal reveal-delay-1 bg-d-900 border border-black/8 rounded-2xl p-7 md:p-9">
                <h2 class="font-display text-2xl font-bold text-gray-900 mb-5">@@INC_TITLE@@</h2>
                <ul class="space-y-3">
@@INCLUDES@@
                </ul>
                <p class="text-g/80 text-sm mt-5">@@INC_NOTE@@</p>
            </div>
        </div>
    </section>

    <!-- PRICING -->
    <section class="bg-d-900 border-y border-black/8">
        <div class="max-w-3xl mx-auto px-5 sm:px-8 py-16 md:py-20">
            <div class="text-center mb-8 reveal">
                <p class="text-r text-xs font-bold tracking-[0.2em] uppercase mb-2">Pricing</p>
                <h2 class="font-display text-4xl md:text-5xl font-bold text-gray-900">@@SVC@@ prices</h2>
            </div>
            <div class="bg-white border border-black/8 rounded-2xl p-7 md:p-9 reveal reveal-delay-1">
@@TIERS@@
                <p class="text-g/70 text-sm mt-5 text-center">Prices may vary upon inspection of the vehicle. Bookings essential.</p>
            </div>
        </div>
    </section>

    <!-- WHY US -->
    <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-24">
        <div class="mb-10 reveal">
            <p class="text-r text-xs font-bold tracking-[0.2em] uppercase mb-2">Why @@SUB@@ chooses TJM</p>
            <h2 class="font-display text-4xl md:text-5xl font-bold text-gray-900 max-w-2xl">Local, mobile, and 5-star</h2>
            <p class="text-g mt-4 max-w-2xl">@@ANGLE@@</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
            <div class="service-card bg-white border border-black/8 rounded-xl p-6 reveal"><h3 class="font-display text-2xl font-bold text-gray-900 mb-2">We come to you</h3><p class="text-g text-sm">A fully mobile detail at your home or workplace in @@SUB@@. No drop-off, no waiting room.</p></div>
            <div class="service-card bg-white border border-black/8 rounded-xl p-6 reveal reveal-delay-1"><h3 class="font-display text-2xl font-bold text-gray-900 mb-2">Rated 5.0</h3><p class="text-g text-sm">100% 5-star reviews on Google from drivers across Melbourne's west.</p></div>
            <div class="service-card bg-white border border-black/8 rounded-xl p-6 reveal reveal-delay-2"><h3 class="font-display text-2xl font-bold text-gray-900 mb-2">Fully insured</h3><p class="text-g text-sm">Professional, insured and reliable, so your car is in safe hands.</p></div>
            <div class="service-card bg-white border border-black/8 rounded-xl p-6 reveal reveal-delay-3"><h3 class="font-display text-2xl font-bold text-gray-900 mb-2">Open Wed to Sun</h3><p class="text-g text-sm">Available Wednesday to Sunday, 8am to 5pm. Bookings essential.</p></div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="bg-d-900 border-y border-black/8">
        <div class="max-w-4xl mx-auto px-5 sm:px-8 py-16 md:py-24">
            <div class="mb-8 reveal">
                <p class="text-r text-xs font-bold tracking-[0.2em] uppercase mb-2">FAQ</p>
                <h2 class="font-display text-4xl md:text-5xl font-bold text-gray-900">@@SVC@@ in @@SUB@@, answered</h2>
            </div>
            <div class="reveal reveal-delay-1">
@@FAQ_HTML@@
            </div>
        </div>
    </section>

    <!-- OTHER SERVICES + AREAS -->
    <section class="max-w-7xl mx-auto px-5 sm:px-8 py-16 md:py-20">
        <h2 class="font-display text-3xl md:text-4xl font-bold text-gray-900 mb-6 reveal">More detailing in @@SUB@@</h2>
        <div class="grid sm:grid-cols-2 gap-5 mb-14 reveal reveal-delay-1">
@@OTHER_SERVICES@@
        </div>
        <h2 class="font-display text-3xl md:text-4xl font-bold text-gray-900 mb-6 reveal">@@SVC@@ across Wyndham</h2>
        <div class="flex flex-wrap gap-x-6 gap-y-3 reveal reveal-delay-1">
@@OTHER_AREAS@@
        </div>
    </section>

    <!-- CTA -->
    <section class="bg-black">
        <div class="max-w-4xl mx-auto px-5 sm:px-8 py-16 md:py-24 text-center">
            <h2 class="font-display text-4xl md:text-6xl font-bold text-white mb-4 reveal">Book @@SVC_LOWER@@ in @@SUB@@</h2>
            <p class="text-white/60 text-lg mb-8 max-w-xl mx-auto reveal reveal-delay-1">Bookings are essential and fill up fast. Call or message us to lock in a time that suits you.</p>
            <div class="flex flex-wrap gap-4 justify-center reveal reveal-delay-2">
                <a href="tel:@@TEL@@" class="btn-red text-lg px-8 py-4">Call @@PHONE@@</a>
                <a href="contact.html" class="btn-outline text-lg px-8 py-4" style="color:#fff;border-color:rgba(255,255,255,0.25)">Book Online</a>
            </div>
        </div>
    </section>

    <!-- Elfsight Google Reviews | TJM Detailing -->
    <section class="bg-black py-16">
        <div class="max-w-7xl mx-auto px-5 sm:px-8">
            <script src="https://static.elfsight.com/platform/platform.js" async></script>
            <div class="elfsight-app-25d79ac5-9b3c-45de-8a27-148e40f124e1" data-elfsight-app-lazy></div>
        </div>
    </section>

    </main>
''' + FOOTER + '''

''' + SCRIPTS + '''

</body>
</html>'''

    repl = {
        "@@TITLE@@": title,
        "@@META@@": meta,
        "@@CANON@@": canon,
        "@@SVC@@": svc["name"],
        "@@SVC_LOWER@@": svc_lower,
        "@@SUB@@": sub_name,
        "@@TEL@@": PHONE_TEL,
        "@@PHONE@@": PHONE,
        "@@HERO_IMG@@": svc["hero_img"],
        "@@HERO_SUB@@": svc["hero_sub"].format(sub=sub_name),
        "@@INTRO1@@": svc["intro1"].format(sub=sub_name),
        "@@INTRO2@@": svc["intro2"].format(sub=sub_name),
        "@@INC_TITLE@@": svc["inc_title"],
        "@@INCLUDES@@": li_list(svc["includes"]),
        "@@INC_NOTE@@": svc["inc_note"],
        "@@TIERS@@": tiers_html(svc["tiers"]),
        "@@ANGLE@@": sub["angle"].format(sub=sub_name),
        "@@FAQ_HTML@@": faq_html(pairs),
        "@@OTHER_SERVICES@@": other_services_html(svc_slug, sub["slug"], sub_name),
        "@@OTHER_AREAS@@": other_areas_html(svc_slug, sub["slug"]),
    }
    out = head
    for k, v in repl.items():
        out = out.replace(k, v)
    if "@@" in out:
        leftover = set(t.split("@@")[0] for t in out.split("@@")[1::2])
        raise SystemExit("Unfilled tokens in {}: {}".format(slug, leftover))
    return slug, out


def main():
    written = []
    for svc_slug in SERVICES:
        for sub in SUBURBS:
            slug, html = render(svc_slug, sub)
            with open(os.path.join(ROOT, slug + ".html"), "w", encoding="utf-8") as fh:
                fh.write(html)
            written.append(slug)
    print("Wrote {} pages:".format(len(written)))
    for w in written:
        print("  " + w + ".html")


if __name__ == "__main__":
    main()
