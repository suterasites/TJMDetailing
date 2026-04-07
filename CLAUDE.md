# TJM Detailing - Business Reference

## Brand Overview

- **Business Name:** TJM Detailing
- **Tagline:** Professional Detailing/Maintenance
- **Service Area:** Melbourne's West
- **Reputation:** 100% 5-Star Reviews
- **Insurance:** Fully Insured
- **NDIS:** Registered NDIS Provider (Garden Maintenance services only)
- **Phone:** 0447 418 866
- **Booking Policy:** Bookings Essential
- **Logo:** `Assets/TJM detailing logo FA.png` (grey "T", red "JM", dark grey "DETAILING" - used for both branches)

## Business Branches

TJM Detailing has **two main service branches**:

1. **Auto Detailing** - vehicle detailing and maintenance services
2. **Gardening & Yard Maintenance** - lawn and garden care services (NDIS Provider)

---

## Operating Hours

| Day       | Hours            |
|-----------|------------------|
| Monday    | Closed           |
| Tuesday   | Closed           |
| Wednesday | 8:00 AM - 5:00 PM |
| Thursday  | 8:00 AM - 5:00 PM |
| Friday    | 8:00 AM - 5:00 PM |
| Saturday  | 8:00 AM - 5:00 PM |
| Sunday    | 8:00 AM - 5:00 PM |

---

## Services & Pricing

> **Note:** All prices are in AUD. Prices may vary upon inspection of the vehicle.

### Headlight Restoration - A$100 | 45 mins

- Removes oxidation and cloudiness
- Restores clarity & improves night visibility
- Keeps headlights cleaner for longer
- Provides up to 6–12 months protection with proper care

---

### Interior Detail

| Vehicle Type   | Price | Duration |
|----------------|-------|----------|
| Hatch/Sedan    | A$70  | 1 hr     |
| SUV/4WD        | A$80  | 1 hr     |
| 7 Seater       | A$90  | 1 hr     |

**Includes:**

- Vacuum of seats, under seats, carpet, boot, floor mats & compartments
- Wipe down of dashboard, centre console & trims
- Windows cleaned (inside only)

---

### Exterior Detail

| Vehicle Type   | Price | Duration |
|----------------|-------|----------|
| Hatch/Sedan    | A$70  | 1 hr     |
| SUV/4WD        | A$80  | 1 hr     |
| 7 Seater       | A$90  | 1 hr     |

**Includes:**

- Pre wash
- Two bucket exterior hand wash
- Wheel & tyre dressing
- Windows cleaned (exterior)
- Door jambs cleaned
- Drying of vehicle

---

### Maintenance Detail

| Vehicle Type   | Price  | Duration    |
|----------------|--------|-------------|
| Hatch/Sedan    | A$110  | 1 hr 30 min |
| SUV/4WD        | A$140  | 1 hr 45 min |
| 7 Seater       | A$150  | 2 hrs       |
| Small Truck    | A$190  | 2 hrs       |

**Includes:**

- Pre wash
- Two bucket exterior hand wash
- Wheel & tyre shine
- Windows cleaned
- Door jambs cleaned
- Drying of vehicle
- Vacuum of seats, under seats, carpet, floor mats & compartments
- Dashboard, centre console & trim wipe down

---

### Full Detail

| Vehicle Type   | Price  | Duration       |
|----------------|--------|----------------|
| Hatch/Sedan    | A$265  | 2 hrs 30 min   |
| SUV/4WD        | A$285  | 2 hrs 45 min   |
| 7 Seater       | A$300  | 3 hrs          |

**Includes:**

- Everything in the Maintenance Detail, plus:
- Steam clean of trim, dash, air vents, floor mats & seats
- Stain removal (if necessary)
- UV protectant applied to dash, console & door trims

---

---

## Gardening & Yard Maintenance Services

> **Note:** TJM Detailing is a registered NDIS provider for garden maintenance services. NDIS participants can access these services through their plan.

- Lawn Mowing
- Edging and Whipper Snipping
- Hedge Trimming
- Weeding Garden Beds
- Removal of green waste
- General Yard Tidy

---

## Key Selling Points (for website copy)

- **Wednesday to Sunday availability** - convenient for customers who work early in the week
- **100% 5-star reviews** - strong social proof
- **Fully insured** - professional and trustworthy
- **Mobile/local service** - servicing Melbourne's West
- **Tiered pricing** - options for every budget, from a quick interior clean to a full detail
- **Vehicle-size pricing** - fair pricing based on hatch/sedan, SUV/4WD, or small truck
- **NDIS Provider** - registered NDIS provider for garden maintenance services, enabling NDIS participants to access yard care through their plan

---

## Website Development Notes

- The business operates **Wednesday to Sunday** (8 AM - 5 PM). This should be prominent so customers know when to book.
- A **booking/contact CTA** should be highly visible on every page since bookings are essential.
- Service pages should clearly distinguish between **vehicle size tiers** (Hatch/Sedan vs SUV/4WD vs Small Truck) for easy price comparison.
- Consider a **before/after gallery** section to showcase detailing results.
- A **reviews/testimonials** section would reinforce the 100% 5-star rating.
- The **"Prices may vary upon inspection"** disclaimer should appear near pricing.

# CLAUDE.md - Frontend Website Rules

## Always Do First
- **Invoke the `frontend-design` skill** before writing any frontend code, every session, no exceptions.

## Reference Images
- If a reference image is provided: match layout, spacing, typography, and color exactly. Swap in placeholder content (images via `https://placehold.co/`, generic copy). Do not improve or add to the design.
- If no reference image: design from scratch with high craft (see guardrails below).
- Screenshot your output, compare against reference, fix mismatches, re-screenshot. Do at least 2 comparison rounds. Stop only when no visible differences remain or user says so.

## Local Server
- **Always serve on localhost** - never screenshot a `file:///` URL.
- Start the dev server: `node serve.mjs` (serves the project root at `http://localhost:3000`)
- `serve.mjs` lives in the project root. Start it in the background before taking any screenshots.
- If the server is already running, do not start a second instance.

## Screenshot Workflow
- Puppeteer is installed at `C:/Users/nateh/AppData/Local/Temp/puppeteer-test/`. Chrome cache is at `C:/Users/nateh/.cache/puppeteer/`.
- **Always screenshot from localhost:** `node screenshot.mjs http://localhost:3000`
- Screenshots are saved automatically to `./temporary screenshots/screenshot-N.png` (auto-incremented, never overwritten).
- Optional label suffix: `node screenshot.mjs http://localhost:3000 label` → saves as `screenshot-N-label.png`
- `screenshot.mjs` lives in the project root. Use it as-is.
- After screenshotting, read the PNG from `temporary screenshots/` with the Read tool - Claude can see and analyze the image directly.
- When comparing, be specific: "heading is 32px but reference shows ~24px", "card gap is 16px but should be 24px"
- Check: spacing/padding, font size/weight/line-height, colors (exact hex), alignment, border-radius, shadows, image sizing

## Output Defaults
- Single `index.html` file, all styles inline, unless user says otherwise
- Tailwind CSS via CDN: `<script src="https://cdn.tailwindcss.com"></script>`
- Placeholder images: `https://placehold.co/WIDTHxHEIGHT`
- Mobile-first responsive

## Brand Assets
- **Logo:** `Assets/TJM detailing logo FA.png` - the current logo for both branches (Auto Detailing and Gardening & Yard Maintenance). Brand colors from logo: grey (#808080), red (#CC0000), dark grey (#4A4A4A).
- Always check the `Assets/` and `brand_assets/` folders before designing. They may contain logos, color guides, style guides, or images.
- If assets exist there, use them. Do not use placeholders where real assets are available.
- If a logo is present, use it. If a color palette is defined, use those exact values - do not invent brand colors.

## Anti-Generic Guardrails
- **Colors:** Never use default Tailwind palette (indigo-500, blue-600, etc.). Pick a custom brand color and derive from it.
- **Shadows:** Never use flat `shadow-md`. Use layered, color-tinted shadows with low opacity.
- **Typography:** Never use the same font for headings and body. Pair a display/serif with a clean sans. Apply tight tracking (`-0.03em`) on large headings, generous line-height (`1.7`) on body.
- **Gradients:** Layer multiple radial gradients. Add grain/texture via SVG noise filter for depth.
- **Animations:** Only animate `transform` and `opacity`. Never `transition-all`. Use spring-style easing.
- **Interactive states:** Every clickable element needs hover, focus-visible, and active states. No exceptions.
- **Images:** Add a gradient overlay (`bg-gradient-to-t from-black/60`) and a color treatment layer with `mix-blend-multiply`.
- **Spacing:** Use intentional, consistent spacing tokens - not random Tailwind steps.
- **Depth:** Surfaces should have a layering system (base → elevated → floating), not all sit at the same z-plane.

## Deployment
- **Always commit and push after making changes.** After every set of changes, commit to `main` and `git push origin main`. Vercel auto-deploys from the `main` branch on GitHub (`suterasites/TJMDetailing`).
- Do not wait for the user to ask - push is part of completing a task.

## Hard Rules
- Do not add sections, features, or content not in the reference
- Do not "improve" a reference design - match it
- Do not stop after one screenshot pass
- Do not use `transition-all`
- Do not use default Tailwind blue/indigo as primary color
- Do not use em dashes or en dashes anywhere - no Unicode characters, no `&mdash;`, no `&ndash;`, no `&#8212;`, no `&#8211;`. Use regular hyphens (-) instead.

## Multi-Page Consistency
- **Navbar:** The navbar must be identical across all pages. If the navbar is modified on any page, apply the same change to every other page immediately.
- **Footer:** The footer must be identical across all pages. If the footer is modified on any page, apply the same change to every other page immediately.
- **Internal links:** All text links that reference a page on the site must link to the correct page URL. When a new page is created, scan all existing pages and update any mentions of that topic to link to the new page.

# Site Checklist

Use this checklist for every page on the site. Each page must have the following metadata and content requirements configured before launch.

---

## Per-Page Checklist

### Page: _______________

**Meta & SEO**
- [ ] **Title Tag** - Under 60 characters, includes primary keyword, brand name at end
- [ ] **Meta Description** - Under 160 characters, includes a clear CTA and primary keyword
- [ ] **Page Canonical URL** - Self-referencing canonical set, uses preferred URL format (trailing slash consistency, www vs non-www)
- [ ] **Open Graph Title** - Optimised for social sharing, can differ from title tag if needed
- [ ] **Open Graph Description** - Written for social click-through, under 200 characters
- [ ] **Search Title** - Google Business / search appearance title confirmed
- [ ] **Search Description** - Google Business / search appearance description confirmed

**Schema & Structured Data**
- [ ] **JSON-LD Schema** - Appropriate schema type applied (LocalBusiness, Service, FAQPage, etc.)
- [ ] **Schema.org Structured Data** - Validated via Google Rich Results Test, no errors or warnings
- [ ] **Identity Schema** - Organization or LocalBusiness identity schema present on key pages (name, logo, URL, contact info, social profiles, sameAs links)

**Sitemaps & Indexing**
- [ ] **XML Sitemap** - Page is included in the XML sitemap with correct URL, lastmod date, and priority value

**Content & AI Readability**
- [ ] **Minimum 500 Words** - Page contains at least 500 words of unique, relevant body content (excluding nav, footer, boilerplate)
- [ ] **Rendered Content LLM Readability** - Page content is fully rendered in the HTML source (not hidden behind JS-only rendering), uses semantic HTML (h1-h6, p, ul/ol, section, article), has a clear content hierarchy that AI crawlers and LLMs can parse and summarise accurately

---

## Page-by-Page Tracker

### Home (index.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | TJM Detailing - Auto Detailing & Garden Maintenance | Melbourne's West |
| Meta Description | ✅ | Professional auto detailing and garden maintenance in Melbourne's West. Rated 5.0 on Google. Fully insured. Open Wednesday to Sunday. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/ |
| Open Graph Title | ✅ | TJM Detailing - Auto Detailing & Garden Maintenance | Melbourne's West |
| Open Graph Description | ✅ | Professional auto detailing and garden maintenance in Melbourne's West. 5-star rated, fully insured. Open Wednesday to Sunday. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | LocalBusiness with AggregateRating, OpeningHours |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness - name, logo, URL, phone, email, address, areaServed, sameAs |
| XML Sitemap Included | ✅ | Priority: 1.0 |
| Min 500 Words | ✅ | ~2000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 25 headings, 11 semantic elements |

### About (about.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | About Us - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Learn about TJM Detailing - professional auto detailing and garden maintenance in Melbourne's West. Built on reliability, craftsmanship, and genuine care. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/about.html |
| Open Graph Title | ✅ | About Us - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Learn about TJM Detailing - professional auto detailing and garden maintenance in Melbourne's West. Built on reliability and genuine care. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | LocalBusiness |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness - name, logo, URL, phone, email, address, areaServed |
| XML Sitemap Included | ✅ | Priority: 0.8 |
| Min 500 Words | ✅ | ~1500+ words body content |
| LLM Readability | ✅ | Semantic HTML, 17 headings, 8 semantic elements |

### Contact (contact.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Contact Us - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Get in touch with TJM Detailing for auto detailing and garden maintenance in Melbourne's West. Call 0447 418 866 or send us a message. Open Wednesday to Sunday. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/contact.html |
| Open Graph Title | ✅ | Contact Us - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Contact TJM Detailing for auto detailing and garden maintenance in Melbourne's West. Call 0447 418 866. Open Wednesday to Sunday. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | LocalBusiness |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness - name, logo, URL, phone, email, address, areaServed |
| XML Sitemap Included | ✅ | Priority: 0.8 |
| Min 500 Words | ✅ | ~800+ words body content |
| LLM Readability | ✅ | Semantic HTML, 6 headings, 5 semantic elements |

### Auto Detailing (auto-detailing.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Auto Detailing Packages - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional auto detailing in Melbourne's West. Interior, exterior, maintenance & full detail packages. Rated 5.0 on Google. Fully insured. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/auto-detailing.html |
| Open Graph Title | ✅ | Auto Detailing Packages - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional auto detailing in Melbourne's West. Interior, exterior, maintenance and full detail packages. 5-star rated, fully insured. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service (Auto Detailing) with LocalBusiness provider |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.9 |
| Min 500 Words | ✅ | ~3000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 20 headings, 11 semantic elements |

### Gardening & Yard Maintenance (gardening-yard-maintenance.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Garden Maintenance - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional garden maintenance in Melbourne's West. Lawn mowing, hedge trimming, weeding, green waste removal and more. Fully insured, 100% 5-star reviews. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/gardening-yard-maintenance.html |
| Open Graph Title | ✅ | Garden Maintenance - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional garden maintenance in Melbourne's West. Lawn mowing, hedge trimming, weeding, green waste removal. Fully insured, NDIS registered. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service (Garden Maintenance) with LocalBusiness provider |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.9 |
| Min 500 Words | ✅ | ~2000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 18 headings, 8 semantic elements |

### Maintenance Detail (maintenance-detail.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Maintenance Detail - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional maintenance detail from $110. Full interior + exterior clean in one session. Hatch/Sedan, SUV/4WD & 7 Seater pricing. Rated 5.0 on Google. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/maintenance-detail.html |
| Open Graph Title | ✅ | Maintenance Detail - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional maintenance detail from $110. Full interior and exterior clean in one session. 5-star rated, fully insured. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service with Offers ($110/$140/$150/$190) |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.8 |
| Min 500 Words | ✅ | ~1500+ words body content |
| LLM Readability | ✅ | Semantic HTML, 15 headings, 9 semantic elements |

### Exterior Detail (exterior-detail.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Exterior Detail - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional exterior detailing from $70. Two-bucket hand wash, wheel & tyre dressing, windows cleaned. Hatch/Sedan & SUV/4WD pricing. Rated 5.0 on Google. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/exterior-detail.html |
| Open Graph Title | ✅ | Exterior Detail - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional exterior detailing from $70. Two-bucket hand wash, wheel and tyre dressing, windows cleaned. 5-star rated. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service with Offers ($70/$80/$90) |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.8 |
| Min 500 Words | ✅ | ~1500+ words body content |
| LLM Readability | ✅ | Semantic HTML, 14 headings, 9 semantic elements |

### Interior Detail (interior-detail.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Interior Detail - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional interior detailing from $70. Vacuum, wipe down, windows cleaned. Hatch/Sedan & SUV/4WD pricing. Rated 5.0 on Google. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/interior-detail.html |
| Open Graph Title | ✅ | Interior Detail - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional interior detailing from $70. Vacuum, wipe down, windows cleaned. 5-star rated, fully insured. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service with Offers ($70/$80/$90) |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.8 |
| Min 500 Words | ✅ | ~1500+ words body content |
| LLM Readability | ✅ | Semantic HTML, 14 headings, 9 semantic elements |

### Full Detail (full-detail.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Full Detail - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Premium full detail from $265. Everything in the Maintenance Detail plus steam cleaning, stain removal & UV protection. Hatch/Sedan & SUV/4WD pricing. Rated 5.0 on Google. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/full-detail.html |
| Open Graph Title | ✅ | Full Detail - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Premium full detail from $265. Steam cleaning, stain removal and UV protection included. 5-star rated, fully insured. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service with Offers ($265/$285/$300) |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.8 |
| Min 500 Words | ✅ | ~1500+ words body content |
| LLM Readability | ✅ | Semantic HTML, 14 headings, 9 semantic elements |

### Headlight Restoration (headlight-restoration.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Headlight Restoration - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional headlight restoration for $100. Remove oxidation, restore clarity, improve night visibility. 6-12 months protection. Rated 5.0 on Google. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/headlight-restoration.html |
| Open Graph Title | ✅ | Headlight Restoration - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional headlight restoration for $100. Remove oxidation, restore clarity, improve night visibility. 6-12 months protection. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service with Offer ($100) |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.8 |
| Min 500 Words | ✅ | ~1200+ words body content |
| LLM Readability | ✅ | Semantic HTML, 15 headings, 10 semantic elements |

### Lawn Mowing (lawn-mowing.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Lawn Mowing - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional lawn mowing in Melbourne's West. Clean, even cuts for a well-maintained yard. Fully insured, 100% 5-star reviews. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/lawn-mowing.html |
| Open Graph Title | ✅ | Lawn Mowing - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional lawn mowing in Melbourne's West. Clean, even cuts for a well-maintained yard. Fully insured, 5-star reviews. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service (Lawn Mowing) with LocalBusiness provider |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.7 |
| Min 500 Words | ✅ | ~1000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 15 headings, 8 semantic elements |

### Edging & Whipper Snipping (edging-whipper-snipping.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Edging & Whipper Snipping - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional edging and whipper snipping in Melbourne's West. Crisp, defined edges along driveways, paths, and garden beds. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/edging-whipper-snipping.html |
| Open Graph Title | ✅ | Edging & Whipper Snipping - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional edging and whipper snipping in Melbourne's West. Crisp, defined edges along driveways, paths and garden beds. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service (Edging and Whipper Snipping) with LocalBusiness provider |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.7 |
| Min 500 Words | ✅ | ~1000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 15 headings, 8 semantic elements |

### Hedge Trimming (hedge-trimming.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Hedge Trimming - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional hedge trimming in Melbourne's West. Neat, shaped hedges for a clean, well-kept property. Fully insured. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/hedge-trimming.html |
| Open Graph Title | ✅ | Hedge Trimming - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional hedge trimming in Melbourne's West. Neat, shaped hedges for a clean, well-kept property. Fully insured. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service (Hedge Trimming) with LocalBusiness provider |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.7 |
| Min 500 Words | ✅ | ~1000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 15 headings, 8 semantic elements |

### Weeding Garden Beds (weeding-garden-beds.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Weeding Garden Beds - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional garden bed weeding in Melbourne's West. Thorough weeding to keep your beds clean and healthy. Fully insured. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/weeding-garden-beds.html |
| Open Graph Title | ✅ | Weeding Garden Beds - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional garden bed weeding in Melbourne's West. Thorough weeding to keep your beds clean and healthy. Fully insured. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service (Weeding Garden Beds) with LocalBusiness provider |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.7 |
| Min 500 Words | ✅ | ~1000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 15 headings, 8 semantic elements |

### Green Waste Removal (green-waste-removal.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | Green Waste Removal - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional green waste removal in Melbourne's West. Collection and disposal of branches, clippings, and garden debris. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/green-waste-removal.html |
| Open Graph Title | ✅ | Green Waste Removal - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional green waste removal in Melbourne's West. Collection and disposal of branches, clippings and garden debris. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service (Green Waste Removal) with LocalBusiness provider |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.7 |
| Min 500 Words | ✅ | ~1000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 15 headings, 8 semantic elements |

### General Yard Tidy (general-yard-tidy.html)

| Item | Status | Value / Notes |
|---|---|---|
| Title Tag | ✅ | General Yard Tidy - TJM Detailing | Melbourne's West |
| Meta Description | ✅ | Professional general yard tidy-up in Melbourne's West. Complete yard clean-up covering lawns, garden beds, and paths. Fully insured. Call 0447 418 866. |
| Page Canonical URL | ✅ | https://tjmdetailing.com.au/general-yard-tidy.html |
| Open Graph Title | ✅ | General Yard Tidy - TJM Detailing | Melbourne's West |
| Open Graph Description | ✅ | Professional general yard tidy-up in Melbourne's West. Complete yard clean-up covering lawns, garden beds and paths. Fully insured. Call 0447 418 866. |
| Search Title | ⬜ | |
| Search Description | ⬜ | |
| JSON-LD Schema | ✅ | Service (General Yard Tidy) with LocalBusiness provider |
| Schema.org Structured Data | ⬜ | Needs validation via Google Rich Results Test |
| Identity Schema | ✅ | LocalBusiness provider within Service schema |
| XML Sitemap Included | ✅ | Priority: 0.7 |
| Min 500 Words | ✅ | ~1000+ words body content |
| LLM Readability | ✅ | Semantic HTML, 15 headings, 8 semantic elements |

---

## Site-Wide Checks

These items apply once across the entire site, not per page.

- [x] **XML Sitemap generated** - sitemap.xml created with all 16 pages, correct URLs, lastmod dates, and priority values
- [ ] **XML Sitemap submitted** - Needs submission to Google Search Console
- [ ] **XML Sitemap auto-updates** - Static site, manual updates required when pages are added/removed
- [x] **Robots.txt** - robots.txt created, references sitemap URL, allows all crawlers
- [x] **Identity Schema on Home** - LocalBusiness schema with name, logo, URL, phone, email, address, areaServed, openingHours, aggregateRating, sameAs
- [ ] **Schema validation clean** - Needs validation via Google Rich Results Test

---

## Quick Reference - Character Limits

| Element | Max Length |
|---|---|
| Title Tag | 60 characters |
| Meta Description | 160 characters |
| OG Title | 60 characters |
| OG Description | 200 characters |
| Search Title | 60 characters |
| Search Description | 160 characters |

---

## JSON-LD Schema Types - Common for Service Businesses

- **LocalBusiness** - Home page, About page
- **Service** - Individual service pages
- **FAQPage** - FAQ sections or pages
- **BreadcrumbList** - All inner pages
- **WebSite** - Home page (with SearchAction if applicable)
- **Review / AggregateRating** - Testimonials or review pages
- **Organization** - Identity schema (name, logo, sameAs social links)

---

## LLM Readability - What to Check

When verifying rendered content is LLM-readable, confirm the following:

1. **Server-side or pre-rendered HTML** - Content is in the HTML source, not loaded entirely via client-side JavaScript after page load
2. **Semantic heading hierarchy** - Single H1 per page, logical H2-H6 nesting, no skipped levels
3. **Paragraph and list structure** - Body content uses `<p>`, `<ul>`, `<ol>` tags rather than divs with styled text
4. **Section and article tags** - Major content blocks wrapped in `<section>` or `<article>` for clear content boundaries
5. **Descriptive alt text on images** - Every image has alt text that describes the content, not just "image1.jpg"
6. **No critical content in images only** - Key information (phone numbers, addresses, service lists) exists as text, not embedded in graphics
7. **Clean readable text** - No keyword stuffing, no hidden text, no excessive boilerplate repeated across pages

---

*Duplicate the page section for each additional page on the site. Replace ⬜ with ✅ once completed and fill in the Value / Notes column with the actual content.*