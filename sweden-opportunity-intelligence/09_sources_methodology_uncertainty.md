# Deliverable 9: Sources, methodology and uncertainty appendix

**Reference date:** 29 October 2026. **Research cutoff:** 30 October 2026, the last retrieval. Information published after that date is not included.

---

## 1. Bibliography and source ledger

All 619 cited sources are in **[`output/source_index.csv`](output/source_index.csv)**: one row per URL per workstream, with publisher, title, publication date, data period, finding and reliability, as recorded in each workstream's ledger. The full ledgers, with retrieval dates, are at the end of each research file:

| Code | Workstream | File | Ledger size |
|---|---|---|---|
| W01 | Macro conditions and structural megatrends | [research/01_macro.md](research/01_macro.md) | 45 rows |
| W02 | Regulatory demand (Swedish and EU) | [research/02_regulation.md](research/02_regulation.md) | ~80 rows |
| W03 | Sector screen A (13 sectors, live SCB API pulls) | [research/03_sectors_A.md](research/03_sectors_A.md) | 52 rows |
| W04 | Sector screen B (15 sectors) | [research/04_sectors_B.md](research/04_sectors_B.md) | ~75 rows |
| W05 | Demand signals: complaints, procurement (own TED analysis), hiring, spending leakage | [research/05_demand_signals.md](research/05_demand_signals.md) | 30 rows |
| W06 | Foreign business-model transfer (26 models) | [research/06_foreign_models.md](research/06_foreign_models.md) | 57 rows |
| W07 | Competitors: cyber, defence, public procurement, AML | [research/07_competitors_cyber_public.md](research/07_competitors_cyber_public.md) | 75 rows |
| W08 | Competitors: property, BRF, energy, construction | [research/08_competitors_property_energy.md](research/08_competitors_property_energy.md) | 81 rows |
| W09 | Competitors: accounting, waste/EPR, automotive, care, estates | [research/09_competitors_sme_waste_auto_care.md](research/09_competitors_sme_waste_auto_care.md) | 73 rows |
| W10 | Adversarial investment-committee review | [research/10_adversarial_review.md](research/10_adversarial_review.md) | — |

**Reliability scale used across the ledgers:**
- **H**: primary or official source, read in full.
- **M**: reputable secondary source, read.
- **L**: search-engine snippet or vendor marketing. Treat as a lead only.

**Most-used primary sources:**
- SCB: national accounts, the business register (FDB), company finances, IT use in companies, and population.
- Konjunkturinstitutet: Konjunkturläget, Sep 2026.
- Riksbanken: Monetary Policy Report, Sep 2026.
- Tillväxtanalys: bankruptcy and new-business statistics.
- Arbetsförmedlingen: Yrkesbarometer, Jun 2026.
- Upphandlingsmyndigheten: Rapport 2026:1.
- TED: Search API v3, own analysis of 9,032 Swedish award notices.
- ARN: annual report 2025.
- riksdagen.se and regeringen.se: budget bill 2025/26:1, props. 2025/26:159, 2025/26:282 and 2025/26:303, SFS 2025:1506 and SFS 2026:764.
- Naturvårdsverket, Boverket, Migrationsverket, MCF.
- Public filing summaries on allabolag.se.

---

## 2. Methodology

### 2.1 Research process (what was actually done)
1. **Six parallel research workstreams:** macro (W01), regulation (W02), sector screens A and B covering 28 sectors (W03, W04), demand signals (W05) and foreign models (W06). They ran independently, in Swedish and English, prioritising primary sources.
2. **Opportunity universe:** **52 distinct opportunities** were derived only from findings in W01–W06; none were brainstormed without evidence. Each has the 17 required fields plus tags. Near-duplicates were merged (for example, "NIS2 for municipalities" and "NIS2 for mid-size firms" became #1).
3. **Competitive intelligence:** competitors were profiled for 21 opportunity areas, which cover the top 20 (W07–W09). About 150 competitors are profiled, using public financial filings and public price pages.
4. **Market sizing and financial models:** built for the top 20 in Python. The code is in [`model/`](model/) and every output is reproducible with `python3 model/build.py`.
5. **Weighted ranking:** all 52 opportunities were ranked on the prescribed nine criteria and weights, with seven ranking views.
6. **Adversarial review (W10):** an independent analyst instance, which had not done the scoring, challenged the top 10 on twelve questions. It proposed score changes, and I adopted or rejected each with a stated reason ([`model/adversarial.py`](model/adversarial.py)).
7. **Deep dives** on the top five after the review, then the recommendation and the 90-day roadmap.

### 2.2 Scoring model

**Weighted score** = Σ (criterion score 0–10 × weight) × 10, which gives a 0–100 scale.

| Criterion | Weight |
|---|---|
| Verified customer pain and demand | 20% |
| Willingness to pay and budget availability | 15% |
| Market timing and growth | 10% |
| Competitive gap and differentiation | 10% |
| Unit economics and profit potential | 15% |
| Speed to launch and first revenue | 10% |
| Capital efficiency | 10% |
| Scalability and defensibility | 5% |
| Regulatory and execution feasibility | 5% |

**Calibration rules:**
- **Demand** scores of 8 or more need evidence of a legal obligation in force with money attached, or documented transactions.
- Forecasts and search interest alone cap demand at 5.
- **Gap** is lowered when a dominant incumbent or a free sector tool exists.
- **Confidence** (High / Medium / Low) is reported next to every score and is not blended into it. A precise score does not hide weak confidence.

### 2.3 Market sizing method

Sizing is bottom-up:
- **TAM** = number of relevant buyers × annual spend per buyer, with low, base and high cases.
- **SAM** = TAM × the share a new Swedish entrant can realistically address.
- **SOM** = plausible customers won in 3–5 years × revenue per customer.

Buyer counts are anchored on SCB, ARN, Upphandlingsmyndigheten and industry data where possible. Spend per buyer is anchored on observed competitor prices. Every input carries a basis note in the spreadsheet, under "Market sizing (modelled)".

### 2.4 Financial model method

A monthly 36-month cohort model ([`model/finance.py`](model/finance.py)) has these inputs:
- recurring revenue per customer (ARPA) and setup fees;
- gross margin;
- customer acquisition cost (CAC) and sales-cycle delay;
- new-customer ramp by year;
- monthly churn;
- fixed opex by year;
- startup cost.

**Cost conventions:**
- Swedish employer contributions of **31.42%** are applied.
- Founders are costed at SEK 45,000/month gross, about SEK 59k fully loaded.
- Specialists are costed at SEK 62,000/month gross, about SEK 81k fully loaded.
- Delivery labour in service businesses sits in gross margin.

**Sensitivities:**
- CAC +50%
- Price −20%
- Sales cycle +50% (with the ramp divided by 1.5)
- Churn doubled
- Combined downside

### 2.5 Currency

All figures are in SEK. Foreign figures were converted at closing rates on **29 October 2026**: EUR/SEK **11.0416**, USD/SEK **9.9074**, GBP/SEK **13.1996** (poundsterlinglive.com history pages, retrieved 2026-10-29). For comparison, the Riksbank's own published rate on 29 May 2026 was EUR/SEK 10.772 and USD/SEK 9.251, which reflects the krona's weakening since February 2026. Foreign figures in the research files are left in their original currency, and converted only where used in a model.

---

## 3. Limitations (read before relying on any number)

1. **The web-search budget ran out** during W01–W05 (a shared cap of about 200 searches per turn across agents). The affected items are tagged in each file. The main gaps:
   - Advokatsamfundet statistics.
   - Municipal consultant spend (the national figure).
   - Heat-pump market data.
   - Svenska kraftnät's grid-queue figures from the primary source.
   - DORA, PSD3 and the 2024 bokföringslag changes (taken from background knowledge, tagged [U]).
2. **Trustpilot evidence comes from the first visible page only** (about 20–24 reviews per vendor) and is graded C (indicative).
3. **No Reddit, Flashback or app-store evidence was collected.** Reddit could not be fetched, and no relevant Flashback threads were found.
4. **Procurement analysis covers TED only** (mostly notices above the EU threshold). National below-threshold platforms (e-Avrop, Mercell/TendSign, Opic) were not scraped, so specialist municipal purchases are under-represented.
5. **No customer interviews were conducted.** No organisations were contacted, which the brief prohibits without authorisation. Willingness to pay is inferred from observed prices and spend, not from stated intent.
6. **Financial figures for private Swedish companies** come from allabolag search pages. These show revenue (in kSEK) but usually not profit.
7. **Political uncertainty.** No government had formed and the 2027 budget had not been tabled by the cutoff. Bills awaiting a Riksdag decision (CER law, personalliggare) may slip.
8. **Survivorship and selection bias.** Foreign "success" models were cross-checked for failures: Aira's going-concern doubt, Coople's UK exit, Gigstr's bankruptcy, the collapsed Xeinadin sale and Eways' bankruptcy. Competitor lists are biased toward firms visible online.

---

## 4. Uncertainty register

| # | Uncertainty / contradiction | Affects | Evidence on each side | Status | How to resolve |
|---|---|---|---|---|---|
| U1 | **Number of NIS2-covered entities in Sweden** | #1, #2 sizing | The government says "drygt 1,500 företag" with 50+ employees (W03 S39). Secondary sources cite MSB at 5,000–8,000 entities including public bodies (W02 §2.1); a consultant cites MSB at 5,000 (search, 2026-10-29). | **Contradictory** | Ask MCF for registration statistics; count municipal companies by SNI code |
| U2 | **Whether new EPBD HVAC-inspection duties apply to BRFs** | #28 | W02 marks the HVAC inspection cycles in prop. 2025/26:159 as [V]. W08 could not confirm a specific duty for BRFs; Boverket guidance updated 1 Oct 2026 gives no thresholds. | Unresolved | Read the Boverket regulations (BFS) on heating and air-conditioning inspection |
| U3 | **Access to Adda area-7 framework** | #4 go-to-market | Awarded 2026-02-16 to 2030-02-15, no extension (W07). The supplier list was not found. | Confirmed barrier | Find the supplier list; explore subcontracting |
| U4 | **Direktupphandling threshold 2026** | #4, #21 | Background knowledge puts it at roughly SEK 0.7–0.8m. Not verified in this study. | Unverified | Check upphandlingsmyndigheten.se, "Direktupphandlingsgräns 2026" |
| U5 | **Share of self-managed BRFs** | #27 sizing | Analyst triangulation of 40–55% (W08 §0, L) | Low reliability | Parse Bolagsverket annual reports or run a survey |
| U6 | **Solar-installer bankruptcies (196 in 2025)** | #36 | Search snippet only (W03 S33 [L]); Sesol's bankruptcy confirmed (W08 §4) | Partly verified | Pull Tillväxtanalys bankruptcies by SNI code |
| U7 | **Svenska kraftnät connection queue above 175 GW** | #37, #38 | Third-party wiki citing Svenska kraftnät (W03 S35 [L]) | Unverified | Read the Svenska kraftnät grid development plan 2026–2035 |
| U8 | **Fortnox API and partner terms for third-party overlays** | #13, #14 | Fortnox has 500+ integrations and an MCP connector exists (W09 §1). The risk of restrictions is not quantified. | Unknown | Read the Fortnox developer terms; ask in a partner programme |
| U9 | **Valuation multiples for small accounting firms** | #15, #16 | A single listing at about 1.3x revenue (W09 §2) | n=1 | Broker interviews; Bolagsplatsen history |
| U10 | **CRA notified-body capacity and enforcement timing** | #7 | None designated EU-wide as of 8 Sep 2026 (W07 Area 4) | Moving | Monitor NANDO and Swedac |
| U11 | **2027 budget and civil-defence funding continuity** | #4, #5, #6 | Budget bill 2025/26:1 multi-year figures; no government in place (W01) | Political | Watch the 12 Nov 2026 budget deadline |
| U12 | **AI Act Art. 4 (AI literacy) final wording after the omnibus** | #10 | Commission proposal softened it; final OJ text not verified (W02 §2.3) | Unverified | Read Regulation (EU) 2026/1744 in the OJ |
| U13 | **Personalliggare bill (prop. 2025/26:282) adoption** | #18 | Tabled 4 Jun 2026; Riksdag vote pending (W02) | Pending | Riksdag voting record |
| U14 | **GDP 2024 revision (0.8% → 2.0%)** | Macro narrative | KI Sep 2025 vs Sep 2026 vintages (W01) | Resolved (use the newer vintage) | — |
| U15 | **CSRD scope in Sweden** | #19 | The EU directive threshold is >1,000 employees and >EUR 450m. The Swedish Lagrådsremiss (Oct 2026) reportedly uses ~SEK 5bn turnover (W04 S62). | Partly reconciled | Read the Lagrådsremiss |
| U16 | **Number of Swedish BRFs** | #27 | 33,865 active (SCB via ChargeNode, W08); "~29,000 owning their buildings" (W03 [L]) | Definitions differ | Use 33,865 for registered and ~29–30k for building-owning |

---

## 5. Market-sizing calculations

The full TAM/SAM/SOM inputs and outputs for the top 20 are in the spreadsheet ([`output/sweden_opportunity_database.xlsx`](output/sweden_opportunity_database.xlsx), sheet "Market sizing (modelled)") and in [`output/tables.md`](output/tables.md). The formulas are in [`model/sizing.py`](model/sizing.py).

**Worked example: Opportunity 4 (base case):**
- **Buyers:** 711 = 290 municipalities + 21 regions + ~400 municipal companies and utilities (the company count is an assumption).
- **Spend per buyer:** SEK 300k/year in external preparedness and säkerhetsskydd services. This is an assumption anchored on SEK 739m in state grants to municipalities (2025) and Uppsala's SEK 100m framework over up to 4 years, which is a large-city outlier.
- **TAM** = 711 × 300k = **SEK 213m/year**. The range is SEK 75m–600m.
- **SAM** = 50% (small and mid-size organisations outside large-city frameworks) = **SEK 107m**.
- **SOM** = 40 customers × SEK 330k = **SEK 13.2m/year**, which is 12% of SAM in 3–5 years.

Because 12% of SAM is ambitious for a new entrant, the 36-month financial model assumes fewer customers (about 37 active by month 36 in the base case).
