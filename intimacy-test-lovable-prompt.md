# Lovable Build Prompt — The Future CEO Intimacy Test

Copy everything below into Lovable as your initial project prompt.

---

Build a public web app called **"The Future CEO Intimacy Test"** — a customer trust scoring platform for Australian businesses, similar in spirit to a public review leaderboard but using a structured 5-question diagnostic instead of free-text reviews.

## Tech & Backend
- Use Supabase as the backend (Postgres + Edge Functions). No authentication / login system — fully public, anonymous submissions.
- Create two tables:

**businesses**
- place_id (text, primary key — Google Place ID)
- name (text)
- category (text)
- suburb (text)
- city (text)
- state (text)
- country (text, default 'Australia')
- lat (float)
- lng (float)
- avg_score (float)
- submission_count (integer, default 0)
- tier (text)
- created_at (timestamp, default now())
- updated_at (timestamp, default now())

**submissions**
- id (uuid, primary key, default gen_random_uuid())
- place_id (text, references businesses.place_id)
- q1_score, q2_score, q3_score, q4_score, q5_score (integer, 1-10)
- total_score (integer, computed as sum of the five scores)
- tier (text)
- submitted_at (timestamp, default now())
- ip_hash (text)
- share_token (text, unique)

## Business Search (Google Places)
- On the "Score a Business" page, integrate Google Places Autocomplete for business search.
- Customer types a business name, sees live autocomplete suggestions, and selects one.
- After selection, show the resolved name, suburb, and category for confirmation.
- Do NOT allow free-text business entry — every submission must resolve to a Google Place ID.
- If the selected place_id doesn't exist yet in `businesses`, create it automatically from the Place Details data.

## The Five Questions
Every submission asks these five questions, one per screen, each answered with a 1–10 slider with anchor text shown for both ends:

1. "Did they use what they know about you to help you — or to sell to you?"
   - 1: "Pure extraction. They used my data against me."
   - 10: "They used what they knew to genuinely serve me."
2. "Did they show up when you needed them — or when they needed something?"
   - 1: "They only contacted me when they wanted money."
   - 10: "They were there exactly when I needed them."
3. "When they got it wrong, did they own it?"
   - 1: "Deflected, explained, blamed. Never admitted it."
   - 10: "Owned it immediately. No spin. Made it right."
4. "Did you choose this relationship — or did it just happen to you?"
   - 1: "I feel trapped. Switching is too hard or too expensive."
   - 10: "I actively chose them and would choose them again."
5. "After every interaction, do you feel like a person or a transaction?"
   - 1: "A number. A data point. A revenue line."
   - 10: "A person they actually know and value."

Total possible score: 50.

## Scoring Tiers
Map total_score to a tier label and colour:

| Score | Tier Label | Colour |
|---|---|---|
| 45–50 | The Closed Door | Gold (#F2C14E) |
| 35–44 | Knocking First | Cream (#F5EEDC) |
| 25–34 | Ajar | Mid grey (#444444) |
| 15–24 | Walking In Uninvited | Coral (#C0392B), muted |
| 0–14 | Door Kicked Open | Coral (#C0392B), bold |

When a business's avg_score is recalculated, store the matching tier label on the business record too.

## Pages & Routes

### `/` — Homepage / Leaderboard
- Hero section with a strong headline and a prominent "Score a Business" CTA.
- Below the hero, show the live leaderboard (default sorted lowest score first — worst trust scores at the top).
- Each row: business name, suburb, category, avg score /50, tier label, submission count, and a "Score this business" button.

### `/score` — Score a Business
- Step 1: Google Places Autocomplete search → confirm business name, suburb, category.
- Steps 2–6: One question per screen (the five questions above), each with a 1–10 slider showing both anchor texts.
- Step 7: Summary screen showing all five scores, total /50, and the tier label.
- Step 8: Shareable card preview (see below) with options to share to LinkedIn, share to X/Twitter, or copy link.
- Optional email capture: "Want a copy of your score card? Enter your email" — store this only for sending an email, do not persist it in Supabase.
- On submit, redirect to the business profile page.

### `/result/:share_token` — Your Score Card
- Displays the individual submission's shareable card at a permanent URL.
- Card content: "THE FUTURE CEO INTIMACY TEST" masthead (top left, coral, monospace), business name (large, dark), suburb/city, "Intimacy Score: X / 50" (large, coral), tier label (bold, tier colour), the five scores as a minimal dot/bar row, a subtle "ajar door" icon bottom right, and the URL "thefutureceo.com.au/test" small at the bottom.
- Card must be high-contrast, legible at small sizes (LinkedIn/Twitter thumbnail), and exportable/screenshot-friendly as roughly a 1200x630 image.

### `/business/:place_id` — Business Profile
- Business name, suburb, category, and a small Google Maps pin/embed.
- Large, prominent current avg_score and tier label.
- Score breakdown: average for each of the five questions shown as horizontal bars.
- Total submission count.
- Chronological list of past individual submissions (scores only, no identifying info).
- Share button for the business profile.

### `/leaderboard` — Full Leaderboard
- Full sortable/filterable table: filter by city, suburb, category, and tier.
- Search by business name.
- Default sort: lowest avg_score first.
- "Score this business" button on every row.

### `/about` — About the Test
- Plain explanation of what the tool is, how scoring works, the five questions, and the tier system. No marketing fluff, no onboarding tone.

## Rate Limiting & Integrity (via Supabase Edge Function)
- Hash the submitter's IP (never store raw IP).
- Before inserting a submission, check: has this ip_hash already submitted for this place_id in the last 24 hours? If yes, reject with the message: "You have already scored this business today. Come back tomorrow."
- No CAPTCHA.
- Flag submissions where all five scores equal 1 AND the time between question 1 and question 5 is under 2 seconds — hold these in a review queue (separate flag/column) and exclude from avg_score calculations until reviewed.
- After each accepted submission, recalculate the business's avg_score, submission_count, and tier.

## Design Direction
This must look like a serious diagnostic instrument, not a gamified app — think Roy Morgan trust data meets premium editorial design.

- Background: deep near-black `#0A0A0E`
- Primary text: warm cream `#F5EEDC`
- Accent / coral: `#C0392B` — used for scores, tier labels, CTAs
- Gold: `#F2C14E` — tier highlights, shareable card accents
- Mid grey: `#444444` — secondary text
- Dividers: `#E8E0D8`
- Headings font: Bricolage Grotesque (Bold) — load from Google Fonts
- Body font: Crimson Pro (Regular / Italic) — load from Google Fonts
- Labels/data/monospace: IBM Plex Mono (Regular) — load from Google Fonts
- No rounded corners on key UI elements (buttons, cards, inputs) — sharp, editorial.
- No emoji anywhere in the UI.
- No confetti, no celebratory animations on submission — this is a serious tool with a cheeky premise; the seriousness wins.
- Tone: direct, no "Hey! Welcome!" onboarding copy. Present the five questions in full, no truncation or tooltips needed.

## Seed Data
On first setup, seed the `businesses` table with these Australian businesses (resolve real Place IDs via Google Places where possible, or placeholder rows if not): Woolworths, Coles, Optus, Telstra, Commonwealth Bank, ANZ, Qantas, JB Hi-Fi, Harvey Norman, Kmart, Bunnings, Aldi, McDonald's Australia, Uber Australia, Temu — so the leaderboard isn't empty at launch.

## Out of scope for this build
- No business login or business-side editing/dashboard.
- No free-text reviews or comments.
- No CAPTCHA.
- Brevo email integration can be stubbed as a simple "enter your email" form that posts to a placeholder Edge Function for now.
