# TJM Detailing — Business Reference

## Brand Overview

- **Business Name:** TJM Detailing
- **Tagline:** Professional Detailing/Maintenance
- **Service Area:** Melbourne's West
- **Reputation:** 100% 5-Star Reviews
- **Insurance:** Fully Insured
- **Phone:** 0447 418 866
- **Booking Policy:** Bookings Essential

---

## Operating Hours

| Day       | Hours            |
|-----------|------------------|
| Monday    | Closed           |
| Tuesday   | Closed           |
| Wednesday | Closed           |
| Thursday  | Closed           |
| Friday    | Closed           |
| Saturday  | 8:00 AM – 5:00 PM |
| Sunday    | 8:00 AM – 5:00 PM |

---

## Services & Pricing

> **Note:** All prices are in AUD. Prices may vary upon inspection of the vehicle.

### Headlight Restoration — A$100 | 45 mins

- Removes oxidation and cloudiness
- Restores clarity & improves night visibility
- Keeps headlights cleaner for longer
- Provides up to 6–12 months protection with proper care

---

### Interior Detail

| Vehicle Type   | Price | Duration |
|----------------|-------|----------|
| Hatch/Sedan    | A$55  | 1 hr     |
| SUV/4WD        | A$65  | 1 hr     |

**Includes:**

- Vacuum of seats, under seats, carpet, boot, floor mats & compartments
- Wipe down of dashboard, centre console & trims
- Windows cleaned (inside only)

---

### Exterior Detail

| Vehicle Type   | Price | Duration |
|----------------|-------|----------|
| Hatch/Sedan    | A$55  | 1 hr     |
| SUV/4WD        | A$65  | 1 hr     |

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
| Hatch/Sedan    | A$85   | 1 hr 30 min |
| SUV/4WD        | A$110  | 1 hr 45 min |
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

**Includes:**

- Everything in the Maintenance Detail, plus:
- Steam clean of trim, dash, air vents, floor mats & seats
- Stain removal (if necessary)
- UV protectant applied to dash, console & door trims

---

## Key Selling Points (for website copy)

- **Weekend-only availability** — convenient for customers who work weekdays
- **100% 5-star reviews** — strong social proof
- **Fully insured** — professional and trustworthy
- **Mobile/local service** — servicing Melbourne's West
- **Tiered pricing** — options for every budget, from a quick interior clean to a full detail
- **Vehicle-size pricing** — fair pricing based on hatch/sedan, SUV/4WD, or small truck

---

## Website Development Notes

- The business operates **Saturday and Sunday only** (8 AM – 5 PM). This should be prominent so customers don't expect weekday availability.
- A **booking/contact CTA** should be highly visible on every page since bookings are essential.
- Service pages should clearly distinguish between **vehicle size tiers** (Hatch/Sedan vs SUV/4WD vs Small Truck) for easy price comparison.
- Consider a **before/after gallery** section to showcase detailing results.
- A **reviews/testimonials** section would reinforce the 100% 5-star rating.
- The **"Prices may vary upon inspection"** disclaimer should appear near pricing.

# CLAUDE.md — Frontend Website Rules

## Always Do First
- **Invoke the `frontend-design` skill** before writing any frontend code, every session, no exceptions.

## Reference Images
- If a reference image is provided: match layout, spacing, typography, and color exactly. Swap in placeholder content (images via `https://placehold.co/`, generic copy). Do not improve or add to the design.
- If no reference image: design from scratch with high craft (see guardrails below).
- Screenshot your output, compare against reference, fix mismatches, re-screenshot. Do at least 2 comparison rounds. Stop only when no visible differences remain or user says so.

## Local Server
- **Always serve on localhost** — never screenshot a `file:///` URL.
- Start the dev server: `node serve.mjs` (serves the project root at `http://localhost:3000`)
- `serve.mjs` lives in the project root. Start it in the background before taking any screenshots.
- If the server is already running, do not start a second instance.

## Screenshot Workflow
- Puppeteer is installed at `C:/Users/nateh/AppData/Local/Temp/puppeteer-test/`. Chrome cache is at `C:/Users/nateh/.cache/puppeteer/`.
- **Always screenshot from localhost:** `node screenshot.mjs http://localhost:3000`
- Screenshots are saved automatically to `./temporary screenshots/screenshot-N.png` (auto-incremented, never overwritten).
- Optional label suffix: `node screenshot.mjs http://localhost:3000 label` → saves as `screenshot-N-label.png`
- `screenshot.mjs` lives in the project root. Use it as-is.
- After screenshotting, read the PNG from `temporary screenshots/` with the Read tool — Claude can see and analyze the image directly.
- When comparing, be specific: "heading is 32px but reference shows ~24px", "card gap is 16px but should be 24px"
- Check: spacing/padding, font size/weight/line-height, colors (exact hex), alignment, border-radius, shadows, image sizing

## Output Defaults
- Single `index.html` file, all styles inline, unless user says otherwise
- Tailwind CSS via CDN: `<script src="https://cdn.tailwindcss.com"></script>`
- Placeholder images: `https://placehold.co/WIDTHxHEIGHT`
- Mobile-first responsive

## Brand Assets
- Always check the `brand_assets/` folder before designing. It may contain logos, color guides, style guides, or images.
- If assets exist there, use them. Do not use placeholders where real assets are available.
- If a logo is present, use it. If a color palette is defined, use those exact values — do not invent brand colors.

## Anti-Generic Guardrails
- **Colors:** Never use default Tailwind palette (indigo-500, blue-600, etc.). Pick a custom brand color and derive from it.
- **Shadows:** Never use flat `shadow-md`. Use layered, color-tinted shadows with low opacity.
- **Typography:** Never use the same font for headings and body. Pair a display/serif with a clean sans. Apply tight tracking (`-0.03em`) on large headings, generous line-height (`1.7`) on body.
- **Gradients:** Layer multiple radial gradients. Add grain/texture via SVG noise filter for depth.
- **Animations:** Only animate `transform` and `opacity`. Never `transition-all`. Use spring-style easing.
- **Interactive states:** Every clickable element needs hover, focus-visible, and active states. No exceptions.
- **Images:** Add a gradient overlay (`bg-gradient-to-t from-black/60`) and a color treatment layer with `mix-blend-multiply`.
- **Spacing:** Use intentional, consistent spacing tokens — not random Tailwind steps.
- **Depth:** Surfaces should have a layering system (base → elevated → floating), not all sit at the same z-plane.

## Hard Rules
- Do not add sections, features, or content not in the reference
- Do not "improve" a reference design — match it
- Do not stop after one screenshot pass
- Do not use `transition-all`
- Do not use default Tailwind blue/indigo as primary color
