# Warehouse Robot Leasing (RaaS) — Business Plan
**Working name: "RoboCo" (placeholder — register a proper trading name before launch)**
Prepared: 27 July 2026

---

## 0. How to read this plan

No startup is truly "99% guaranteed" — anyone who tells you that is selling something. What *is* achievable is eliminating the specific, well-documented failure modes that kill robot-leasing businesses (idle fleets, underpriced contracts, related-party governance messes, undercapitalised maintenance, single-customer dependency). This plan is built around a **checklist of conditions precedent** (Section 11) that, if genuinely satisfied before you commit capital, remove almost all of the controllable risk. The residual risk is market timing and execution discipline — which is on you, not the plan.

Assumptions locked in from your answers:
- The anchor customer is the distribution centre of a major Australian vitamins/nutraceuticals exporter to China and Asia, where **Kevin is CEO**.
- Kevin's company is privately/family-held; Kevin has final decision authority (no external board to satisfy) — governance section is written accordingly, but still recommends arm's-length discipline.
- You have access to **$1.5m+** in capital (own/family/investor), which sets the fleet size and financing mix modelled below.

---

## 1. Executive Summary

**The business:** A new, separate company ("RoboCo") buys or finances warehouse robots (autonomous mobile robots, goods-to-person tote/case robots, and packing/palletising cobots), trains and integrates them for a specific site's SKUs and workflows, and **leases them back to warehouses as a fully-managed monthly service** (Robotics-as-a-Service, RaaS) — hardware + installation + maintenance + fleet-management software + uptime SLA, priced like labour rather than equipment. RoboCo owns the robots and, critically, owns the software/data layer that sits on top of them.

**Why now:** The Australian warehouse robotics market was ~US$301m in 2024 and is forecast to reach ~US$818m by 2030 (17.1% CAGR by value, 18.3% by unit volume) — outpacing most global markets. [Next Move Strategy Consulting / market reports] Global warehouse robotics is tracking from ~US$9.3bn (2025) toward ~US$24.6bn by 2031 (17.5% CAGR), with Asia-Pacific already the largest regional block (39.5% share) and growing fastest. RaaS specifically exists because most mid-sized operators want OpEx not CapEx, want a tech refresh path, and don't want to build in-house robotics/maintenance teams — Grant Thornton Australia's own analysis frames RaaS as removing exactly this capital barrier for SMEs. [Grant Thornton Australia]

**The unlock:** Kevin, as CEO of a distribution centre for a major vitamins/supplements exporter, gives you something almost no robotics startup gets for free: a **committed, credible, real-world anchor site** with genuine automation pain (seasonal export peaks to China, batch/lot traceability requirements, mixed-SKU pick/pack, labour-constrained fulfilment) to pilot on, prove ROI, and turn into a reference case. That reference case — not the family connection itself — is the actual asset. The family connection only gets you in the door; everything after that has to stand on commercial merit, market-rate pricing, and measurable results, or it will not survive scrutiny (from Kevin's other stakeholders, from future investors, or from the ATO).

**The model in one line:** Buy/finance robots → deploy full-service at Kevin's DC at a market rate → prove utilisation, uptime and ROI with real data → use that proof to sign 3–5 more Australian customers in adjacent verticals (health/nutraceutical/FMCG export, general 3PL) within 18 months → scale fleet against contracted demand only, never speculatively → progressively own more of the software stack as the highest-margin, most defensible layer.

---

## 2. Market Opportunity

### Global and Australian sizing
| Metric | Figure | Source |
|---|---|---|
| Australia warehouse robotics market, 2024 | ~US$301.1m | Market research aggregators (Next Move Strategy Consulting-class reports) |
| Australia warehouse robotics market, 2030 (forecast) | ~US$817.6m (17.1% CAGR value, 18.3% CAGR units) | same |
| Australia unit volume, 2024 → 2030 | ~12,660 → ~36,790 units | same |
| Global warehouse robotics market, 2025 → 2031 | ~US$9.33bn → ~US$24.55bn (17.5% CAGR) | industry market reports |
| Global AMR market, 2026 → 2032 | ~US$2.75bn → ~US$7.07bn (14.4% CAGR) | MarketsandMarkets-class reports |
| Asia-Pacific share of global warehouse robotics, 2025 | ~39.5%, growing ~17.9% CAGR to 2031 | same |

Take these numbers as **directional, not gospel** — market-report CAGR figures vary 15–20 percentage points between vendors and are frequently revised. The consistent signal across every source is: Australia is growing faster than the global average, off a small base, which is exactly the profile of a market still open to a well-executed regional entrant rather than one already locked up by incumbents.

### Why Australia specifically, and why now
- **Structural labour shortage** in logistics/warehousing, pushing up wage costs and turnover — the core RaaS value proposition ("robots priced like labour, but reliable and scalable") lands harder here than in labour-abundant markets.
- **E-commerce and export growth**, particularly China/Asia-facing cross-border trade in health, beauty and nutraceutical categories — a genuine local growth vertical.
- **Capital-shy mid-market**: most Australian 3PLs and mid-sized exporters are not going to write a $2–5m cheque for an AutoStore/Dematic turnkey system, but will sign a monthly service contract that shows up as OpEx.
- **Thin RaaS competition domestically** (see Section 3) relative to the number of large systems integrators — there is a real gap between "enterprise turnkey automation" (Dematic, Swisslog, Element Logic/AutoStore) and "no automation," with almost nobody offering a mid-market, multi-vendor, fully-managed lease model at scale. LYRO Robotics (Brisbane) is the clearest existing proof that Australian RaaS works — but in fresh-produce packing, not warehouse pick/pack/logistics.

---

## 3. Competitive Landscape (Australia)

Three distinct groups matter here — they are not equivalent competitors, and you should think about each differently.

### A. Large enterprise systems integrators (compete for large capex projects, not your initial market)
| Company | Position in Australia | Relevance to you |
|---|---|---|
| **Dematic** (KION Group) | Full turnkey integrator; delivers AutoStore-based systems (e.g. South West Healthcare) and large shuttle/ASRS projects | Not a direct competitor for mid-market RaaS leases — they sell $millions, multi-year capital projects, typically to large retail/healthcare. Could become a channel partner or eventual acquirer. |
| **Swisslog** | AutoStore integrator, strong retail/grocery presence (e.g. IKEA Sylvia Park NZ) | Same category as Dematic — enterprise capex, not mid-market lease. |
| **Element Logic** | AutoStore specialist integrator | Same. |
| **Kardex** | Automated storage (vertical lift modules, shuttle systems) | Adjacent technology, enterprise-sale motion. |
| **AutoStore** | Expanding direct ANZ presence (announced milestone, mid-2026) | Watch this closely — if AutoStore or its integrator network starts offering their own financed/leased mid-market packages, that narrows your gap. Currently still capex/integrator-led. |

**Read:** none of these are set up to sign an 8-robot, 24-month, fully-serviced lease with a mid-sized exporter's DC quickly. Their sales cycles, minimum deal sizes and installation footprints are built for much larger, longer projects. That gap is your opening.

### B. Australian robotics/automation integrators and suppliers (potential competitors *and* potential partners/suppliers)
| Company | What they do | Relevance |
|---|---|---|
| **Robotic Automation** | Australian AMR/mobile robot and warehouse management solutions | Closest existing local competitor for AMR deployments — worth a direct comparison call to understand their commercial model before you launch. |
| **The Robot People** | Collaborative robotics (cobots), 30+ years in Australian process automation | Established, manufacturing-leaning; less warehouse-specific — possible integration/service partner. |
| **M.A.P Services** | Robotics and vision systems for industrial processes | Adjacent, vision/QA focus — potential technology partner for pick accuracy/batch verification (useful for TGA/export traceability). |
| **Quantum Robotics** | Warehouse robots/RoboCarts, Melbourne/Sydney/Brisbane | Direct competitor to watch for AMR cart-style deployments. |
| **The Robot Factory Australia** | Industrial/commercial robot supplier | Hardware supplier, not obviously a RaaS/lease operator — potential procurement channel. |
| **LYRO Robotics** (Brisbane) | Robotic packing-as-a-service for Queensland farmers; founded by the 2017 Amazon Robotics Challenge-winning team; raised ~$3.24m total | **The single most important reference point in Australia.** Proves an Australian RaaS model can raise capital, operate, and get renewal. Different vertical (fresh produce packing vs. warehouse fulfilment) so not a direct competitor today, but a natural acquisition/partnership/talent-pool target as you scale, and a template for investor conversations ("LYRO proved this model works in AU agriculture; we're doing the equivalent in warehouse/export logistics"). |

### C. Global RaaS/robot OEMs (your likely hardware suppliers today, possible direct competitors tomorrow)
Locus Robotics, Geek+, Hai Robotics, Hikrobot, Exotec, MiR/Teradyne (see Section 6 for procurement detail). None currently run a dedicated, localised Australian mid-market leasing operation with local field service — that is the specific gap you are filling. **Risk to track:** several of these vendors already run RaaS commercially overseas; if any opens a direct Australian leasing arm with local service infrastructure, that becomes your most dangerous competitor. Your defensibility against that scenario is local service density, vertical (health/export logistics) depth, and your own software layer — not the hardware, which you don't control.

### Bottom line on competition
You are not entering an empty market, but you are entering a market where the mid-sized, fully-serviced, multi-vendor lease model is not yet being run at scale by anyone with local service infrastructure. The white space is real but narrow — move on it with the anchor pilot before a better-capitalised player (an OEM going direct, or an integrator downmarket) closes it.

---

## 4. The Anchor Customer: Structuring the Kevin Relationship Correctly

This is the single highest-risk section of the plan if handled casually, and the easiest to de-risk if handled properly. Get this wrong and it taints every future fundraise, every future customer reference, and possibly Kevin's own standing at his company.

### 4.1 Keep the entities separate
- **RoboCo should be a new, standalone Pty Ltd, owned by you (and any co-founders/investors) — not by Kevin, and not by Kevin's company.** Kevin's cleanest role is **customer + advisor/door-opener**, not owner or director of RoboCo. If Kevin (or his company) wants equity, treat it as a deliberate, disclosed decision with its own paperwork — not an informal handshake — because it changes the conflict-of-interest analysis below.
- If Kevin has no equity in RoboCo, the relationship is simple: RoboCo is a vendor to his company, exactly like any other supplier. This is the version that survives every future audit, sale process, or minority-shareholder question at his company.

### 4.2 Price at arm's length, in writing, from day one
Even though Kevin's company is privately held and he has final say, do the following anyway — it costs you almost nothing and removes the two risks that actually matter:
1. **Benchmark the lease price** against 2–3 indicative market quotes (even informal ones from Locus/Geek+/local integrators) before setting the rate with Kevin. Document it.
2. **Put it in a written services/lease agreement** — term, monthly fee, SLA (uptime %, response times), what happens at end of term, who owns the operational data. Not a handshake.
3. **Invoice at the documented market rate**, not a "mates rates" discount. Reasons this matters even in a private company with no board:
   - **Tax**: the ATO can and does scrutinise related-party pricing (transfer pricing / market value substantiation) even between privately held entities, and if Kevin or family later takes equity in RoboCo, Division 7A issues can arise from underpriced or non-commercial dealing.
   - **Credibility**: your entire growth strategy (Section 8) depends on using this deployment as a *reference case with real numbers* to sign customers #2–5 and to raise capital. "We gave our uncle's company a discount" is worthless as proof; "we delivered X% pick-rate improvement at market rates with a 95%+ uptime SLA" is a sales asset.
   - **Protects Kevin**: if anyone at his company (a family co-owner, a future buyer doing due diligence, a bank covenant reviewer) ever asks why the DC signed with a company run by the CEO's relative, "market-rate, competitively benchmarked, written contract" is a complete answer. "Family favour, undocumented" is not.
4. **Keep a short decision memo** (even one page) recording why this vendor was chosen, what was benchmarked, and who approved it. Costs nothing, and is the single cheapest insurance policy against a future dispute.

### 4.3 What Kevin is actually good for
- **Access and credibility** to get a real pilot site, real SKU data, and real operational cooperation (staff time, floor access, WMS integration access) that a cold-sales robotics startup would spend 6–12 months and significant sales cost acquiring.
- **Domain intelligence**: export cycles to China/Asia, TGA compliance and batch/lot traceability needs (see 4.4), seasonal peak patterns, mixed-SKU (bottles, blister packs, cartons) handling constraints.
- **A warm introduction path** into the broader Australian nutraceutical/health-export and 3PL community once the pilot has real numbers — this is your Phase 2 customer acquisition channel (Section 8).

### 4.4 Vertical-specific requirements this anchor site brings
Because the anchor is a vitamins/supplements exporter to China/Asia:
- **Batch/lot tracking and traceability** through the pick/pack process — robots and software must capture and pass through batch numbers, not just SKU/quantity. This is a real technical requirement to build into the software MVP (Section 7), and it becomes a **differentiator** you can sell to other nutraceutical/health exporters later (generic AMR vendors don't have this out of the box).
- **China market compliance** context: Australian health/supplement exporters typically rely on **TGA certification plus a Certificate of Free Sale**, and for cross-border e-commerce (CBEC) routes, product/manufacturer registration with China's GACC/SAMR. [general China import-compliance sources] Your robots and software don't need to manage this compliance directly, but your pick/pack accuracy and lot-traceability data feed directly into the exporter's compliance and audit trail — get this right and it's a selling point; get it wrong (mis-picks, lost lot traceability) and it's a serious liability for both companies.
- **Possible temperature/humidity sensitivity** for some supplement formulations — confirm with Kevin's ops team whether any SKUs need climate-controlled zones, which affects robot selection (battery/electronics tolerance) and layout.

---

## 5. Business Model

**RoboCo leases fully-managed robot capacity, priced like labour, not like equipment.**

- **Pricing structure**: flat monthly fee per robot (all-in: hardware, software, maintenance, monitoring, support), benchmarked against market RaaS rates of **~AUD 2,000–5,000 per AMR/tote-robot per month** and **~AUD 8–30/hour** for arm-based cobot tasks (Formic's US industrial model, a useful pricing anchor even though it's a different vertical) [Formic, various RaaS pricing guides, 2026]. Actual rate depends on robot class, task complexity, and contract length/minimums.
- **Contract structure**: minimum term (12–24 months) with a utilisation/minimum-commitment clause, uptime SLA (target 95%+), defined maintenance response times, and a clear end-of-term path (renew, upgrade, or return).
- **What's included, deliberately**: installation and site adaptation, remote fleet monitoring, predictive maintenance and spare parts, software/fleet-orchestration layer, training and change management, and insurance-backed liability cover. This is what makes it defensible — a bare hardware rental is easy to copy; a full-service, SLA-backed, software-layered offering is not.
- **Revenue lines over time**: (1) core robot leases, (2) software/analytics as a standalone SaaS upsell to warehouses that already own robots from other vendors (capital-light, high-margin, and a natural Phase 3 expansion), (3) integration/consulting services for complex sites.

---

## 6. Hardware & Procurement Strategy

**Do not build robots. Buy proven hardware, own the integration/software/service layer.** This is the single most important strategic decision in the plan — it converts a capital-intensive, technology-risk-heavy hardware business into a capital-moderate, service-and-software business.

### Priority vendor conversations
| Vendor | Fit | Why |
|---|---|---|
| **Locus Robotics** | Order pick/pack AMRs | Proven collaborative (human+robot) AMR model, mature RaaS commercial terms, good fit for mixed-SKU vitamins pick/pack. |
| **Geek+** | Goods-to-person, tote/shelf systems | Market leader in goods-to-person, strong APAC footprint and Australian integrator relationships already exist. |
| **Hai Robotics** | Autonomous case-handling robots (ACR) | High-density storage without facility rebuild — already has healthcare-adjacent Australian deployments (via DHL-style life-sciences sites), which is a strong precedent for your vertical. |
| **Hikrobot** | AMR + machine vision | Competitive pricing, vision capability useful for batch/lot verification. |
| **MiR / Teradyne** | Flexible material-transport AMRs | Reliable, well-established Australian partner network (e.g. via KUKA/industrial automation channel). |
| **Exotec** | High-throughput goods-to-person (Skypod) | Premium tier — consider only once fleet and site scale justify it. |

### What to negotiate for, specifically
1. **API/SDK access** for third-party fleet orchestration — non-negotiable. If a vendor won't open their fleet interface to your software layer, deprioritise them; you cannot own the software moat on a closed platform.
2. **Explicit data ownership** — the operational data your fleet generates (pick times, error rates, routes, utilisation) must be contractually yours, not the vendor's, even though it runs on their hardware/firmware.
3. **Volume/reseller and residual-value terms** — since you are financing and re-leasing, negotiate as a channel/fleet partner, not a single-unit retail buyer.
4. **Local support/spares commitment** — a vendor with no Australian service presence pushes all field-service risk onto you; price and staff for that (Section 9), or prefer vendors with existing AU/APAC service infrastructure.
5. **Conformance documentation** — request the vendor's AS 5144-4 / ISO 3691-4 (AMR/AGV safety) and, for cobots, ISO 10218-1/2 + ISO/TS 15066 compliance declarations up front. Do not deploy without them (Section 9).

---

## 7. Software & IP Strategy — the actual moat

Hardware is commoditising fast; the durable margin and defensibility sit in the software and data layer.

### Build sequence (don't over-build early)
1. **Phase 1 (Months 0–6, ~AUD 150k–300k, 4–9 months with a small AU-based robotics/software team):** integrate against vendor APIs/ROS2; build a thin orchestration layer plus a customer-facing analytics dashboard (utilisation, pick-rate, error/traceability reporting, ROI reporting) plus one WMS/ERP connector (Kevin's DC system). Include **batch/lot traceability pass-through** from day one — it's cheap to build now and expensive to retrofit, and it's your vertical differentiator.
2. **Phase 2 (Months 6–18):** generalise the WMS connector library (add 2–3 more common Australian WMS platforms), add multi-site fleet management, and start building the optimisation/learning layer from real fleet data.
3. **Phase 3 (18–36 months):** license the software standalone (SaaS) to warehouses running other vendors' hardware — capital-light, high-margin expansion that doesn't require buying more robots.

### Protecting it
- **IP assignment**: every employee and contractor signs an IP assignment deed before writing a line of code. Do this before Phase 1 starts, not after.
- **Copyright**: automatic in Australia on original code; keep clean version control and authorship records as evidence.
- **Trade secrets**: NDAs and access controls around training data, optimisation parameters, and any customer-specific models (especially Kevin's DC data).
- **Patents**: only if something is genuinely novel (e.g., a specific task-allocation method for mixed-batch/lot-tracked SKUs under export deadline constraints) — engage a patent attorney to file a provisional within the first 12 months if so; don't over-invest in patenting a generic orchestration layer.
- **Vendor contracts**: explicitly reserve your right to interface, collect data, and run third-party software — do not sign a hardware agreement with lock-in clauses that block this.

---

## 8. Go-to-Market Beyond the Anchor

1. **Months 0–6**: paid or discounted pilot at Kevin's DC (priced at benchmarked market rate, per Section 4.2). Instrument everything — utilisation, uptime, pick-rate/accuracy improvement, labour hours saved, ROI. This data is your entire sales collateral for Phase 2.
2. **Months 6–18**: use the documented pilot ROI to approach **3–5 adjacent-vertical targets**: other nutraceutical/supplement/health exporters, FMCG/food export 3PLs (similar batch-traceability needs), and general Australian 3PLs feeling labour-cost pressure. Kevin's network is a warm-intro channel here, but the pitch stands on the data, not the relationship. Target geographic density in one metro corridor first (Sydney or Melbourne/Brisbane, wherever the anchor and easiest early prospects cluster) to keep field-service costs low.
3. **Customer concentration discipline**: cap Kevin's DC at no more than ~50% of total lease revenue by month 24. If you haven't diversified by then, you don't have a business, you have a very elaborate favour.
4. **18–36 months**: expand fleet only against signed/contracted demand (never speculative purchasing), add robot types and verticals once the playbook is proven, and begin the standalone software licensing motion (Section 7, Phase 3).

---

## 9. Regulatory, Safety, Insurance

- **AMR/AGV safety**: Australia applies **AS 5144-4**, aligned with international **ISO 3691-4**, covering hardware design (no trap/crush points, ground clearance, obstacle detection/avoidance, e-stop placement) and required documentation. [Dematic AU insights; AGV Network] Require vendor conformance declarations before any unit ships to a customer site.
- **Collaborative robots (cobots)**: apply **ISO 10218-1/2** and **ISO/TS 15066** (collaborative operation force/speed limits) for any packing/palletising arms.
- **WHS**: as the entity deploying equipment into a customer's workplace, run a documented risk assessment and worker consultation (per the WHS Act's general PCBU duties) before go-live at every site, not just the first one. This is cheap and standard practice, and a serious injury without it is close to an existential risk for a young company.
- **Insurance** (bind *before* the first robot ships): public/product liability, equipment/asset insurance on the leased fleet, cyber insurance (you're running fleet-management software with customer operational data), and consider professional indemnity for integration/consulting advice.

---

## 10. Financial Plan (indicative — get vendor quotes before committing capital)

All figures indicative and in AUD; treat as planning ranges, not quotes.

### Phase 1 — Pilot at Kevin's DC (Months 0–6)
| Item | Indicative cost |
|---|---|
| Fleet: ~8 units (mix of 4 tote/case AMRs + 2 packing cobots + 2 material-transport AMRs) | $900k–$1.2m hardware + integration |
| Software MVP build (Section 7, Phase 1) | $150k–$300k |
| Working capital buffer (spares, contingency, opex before revenue ramps, insurance) | $200k–$300k |
| **Total Phase 1** | **~$1.3m–$1.8m** |

**Financing mix, using your $1.5m+ capital base:**
- ~40% equity/family capital — covers the software build and working capital, which equipment lenders will not finance (no tangible collateral, no proven revenue yet).
- ~60% equipment finance (chattel mortgage) against the hardware — this is standard and well-supported in Australia (chattel mortgages are >60% of SME equipment finance; industrial robots sit on a 10-year effective life under ATO Division 40, giving straightforward depreciation claims and GST credit on the BAS). [Switchboard Finance; ATO Division 40 guidance] Lenders will want the signed lease agreement with Kevin's DC as security for serviceability — another reason it must be a real, written, market-rate contract (Section 4.2), not an informal arrangement.

**Revenue**: 8 units × ~$3,500/month average (blended AMR + cobot rate) ≈ **$28,000/month (~$336k/year)** from the anchor site once fully ramped.

### Unit economics target
- **Cost-to-serve** (maintenance, spares, financing/debt service, remote monitoring labour, software amortisation): target 45–55% of lease revenue.
- **Gross margin at maturity**: 45–55%.
- **Payback per robot**: 18–30 months at realistic utilisation (50–70%+).
- **Utilisation is the single biggest lever** — an idle robot is pure loss; prioritise multi-shift, high-volume, or seasonal-peak deployments (the export cycle to China/Asia is actually a *feature* here — it creates a demand pattern for flexible seasonal scale-up, which is exactly what RaaS is good at).

### Phase 2 (Months 6–18)
Grow to ~40–60 leased units across 3–5 customers, financed increasingly through equipment finance against *contracted* revenue (much easier once you have a signed multi-customer book), topped up with a modest seed raise once utilisation/uptime KPIs are proven — investors want to see recurring revenue and unit economics before this stage, not before.

### Phase 3 (18–36 months)
Scale toward 150–250+ units across one or two metro corridors, plus the standalone software-licensing revenue line.

---

## 11. Conditions Precedent — the "eliminate the known failure modes" checklist

Do not deploy the first robot until every item below is true:
1. **Signed, written, market-rate lease agreement** with Kevin's DC in place — benchmarked pricing, defined SLA, term, and data-ownership clause (Section 4.2).
2. **RoboCo is a separate legal entity**, not owned by Kevin or his company, with a documented decision trail for why this vendor was chosen.
3. **Fleet size matches contracted demand only** — no speculative purchasing beyond the pilot's agreed scope.
4. **Financing structured so debt service is covered at a conservative (~50%) utilisation assumption**, not best-case.
5. **Vendor conformance documentation in hand** (AS 5144-4/ISO 3691-4, and ISO 10218-1/ISO/TS 15066 for cobots) and a completed WHS risk assessment with worker consultation.
6. **Insurance bound** (liability, asset, cyber) before first unit ships.
7. **IP assignment deeds signed** by every contractor/employee before software work starts; data-ownership clause secured in the hardware vendor contract.
8. **Batch/lot traceability built into the MVP** from day one (Section 7) — this is your vertical differentiator and it's cheap now, expensive later.
9. **Local field-service capability** (in-house technician or an exclusive local partner) established before signing customer #2 — do not scale service commitments faster than service capacity.
10. **A hard customer-concentration target**: no single customer above ~50% of revenue by month 24, tracked explicitly, with Phase 2 sales motion starting well before the pilot ends.

---

## 12. Key Risks and Mitigations (summary)

| Risk | Mitigation |
|---|---|
| Idle fleet / low utilisation | Contract minimum-commitment clauses; target multi-shift/seasonal-peak sites; track utilisation weekly from day one |
| Related-party/governance issues with Kevin | Separate entity, arm's-length written contract, benchmarked pricing, documented decision trail (Section 4) |
| Technology obsolescence | Modular vendor platforms, negotiated upgrade paths, shorter initial contract terms |
| Underestimated field-service/maintenance cost | Build local service capacity before scaling customer count; price cost-to-serve conservatively (45–55% of revenue) |
| Customer concentration | Explicit cap and active Phase 2 diversification target |
| Vendor/OEM goes direct-to-market in Australia | Differentiate on local service density, vertical (health/export) depth, and proprietary software — not on hardware |
| Currency exposure (hardware priced in USD/CNY) | Negotiate AUD-denominated contracts where possible or hedge; build FX buffer into pricing |
| Regulatory/safety incident | Vendor conformance docs, WHS risk assessments per site, insurance bound before go-live |
| Software/IP walking out the door | IP assignment deeds from day one; access controls on training data and customer-specific models |

---

## 13. Roadmap Summary

| Phase | Timing | Milestone |
|---|---|---|
| 1 — Pilot | Months 0–6 | Signed contract with Kevin's DC, 8-unit fleet live, software MVP with batch-traceability, ROI data captured |
| 2 — Prove & diversify | Months 6–18 | 3–5 total customers, 40–60 units, cost-to-serve and utilisation KPIs validated, seed raise if needed |
| 3 — Scale | Months 18–36 | 150–250+ units, geographic density in 1–2 metro corridors, standalone software licensing line launched |

---

## Sources
- [Australia Warehouse Robotics Market Size & Analysis](https://www.nextmsc.com/report/australia-warehouse-robotics-market-se3133)
- [Warehouse Robotics Market Size & Share Analysis — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/warehouse-robotics-market)
- [Autonomous Mobile Robots (AMR) Market — MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/autonomous-mobile-robots-market-107280537.html)
- [Grant Thornton Australia — Revolutionising warehouse automation: the impact of RaaS](https://www.grantthornton.com.au/insights/blogs/revolutionising-warehouse-automation-the-impact-of-raas/)
- [AutoStore Expands Global Momentum with Australia and New Zealand Milestone](https://www.prnewswire.com/news-releases/autostore-expands-global-momentum-with-australia-and-new-zealand-milestone-302817035.html)
- [Dematic — AGV & AMR Safety Standards](https://www.dematic.com/en-au/insights/articles/agv-and-amr-safety-standards/)
- [ISO 3691-4 — The Global Standard for Mobile Robot Safety](https://jlcrobotics.com/iso-3691-4/)
- [AGV Network — What is ISO 3691-4](https://www.agvnetwork.com/automated-guided-vehicles-technology/standard-3691-4)
- [Switchboard Finance — Factory Automation Lender File 2026](https://www.switchboardfinance.com.au/insights/lender-file-read-factory-automation-chattel-mortgage-2026what-a-lender-sees-on-a-factory-automation-file-2026)
- [LYRO Robotics raises $1.5m pre-Series A funding](https://lyro.io/lyro-robotics-raises-1-5m-pre-series-a-funding-to-tackle-australian-labour-shortages/)
- [Formic Offers Robotics as a Service and Financing to Manufacturers](https://www.robotics247.com/article/formic_offers_robotics_as_a_service_and_financing_to_manufacturers)
- [Unpacking Locus Robotics' RaaS pricing](https://www.oreateai.com/blog/unpacking-locus-robotics-raas-how-much-does-a-robot-cost-per-month/207cffc5189f57e1da32a81878ed6dbd)
- [Importing Supplements to China 2026 — GACC Order 280](https://www.mymypanda.com/importing-supplements-to-china-2026-gacc-order-280-takes-effect-june-1/)
