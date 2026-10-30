# 05 – Demand Signals: Complaint Mining, Procurement, Hiring, Spending Leakage (Sweden)

Reference date: 29 October 2026. Retrieval date for all sources: 2026-10-29.
Scope: only publicly accessible pages, no logins, no contact with anyone.

**Evidence-strength labels**
- **A**: official statistics or a full dataset that we analysed ourselves (counts are reproducible).
- **B**: official or industry report figures quoted second-hand, or a vendor-published report.
- **C**: a small visible sample, such as the first page of Trustpilot reviews (about 20–24 reviews). Indicative only.
- **D**: anecdote or single forum thread.

**Method limitations, stated up front**
- Reddit (old.reddit.com) could not be fetched by the tooling. No Reddit evidence is used.
- No Flashback threads were found through search. No Flashback evidence is used.
- App-store reviews were not collected.
- The shared web-search budget ran out partway through Method 6. Spending-leakage evidence therefore relies on a few direct fetches and is thinner than the other methods.
- Trustpilot counts are from the **visible first page only**, not all reviews. Theme counts are our own grouping and are labelled C.
- TED analysis covers notices **on TED only**. These are mainly above-EU-threshold notices plus some voluntary ones. Sweden-wide statistics come from Upphandlingsmyndigheten (UHM).

---

## Method 1 – Complaint mining: cluster table

| # | Segment | Problem cluster | Frequency signal | Severity | Current workaround | Economic impact | WTP evidence | Alternatives | Strength |
|---|---|---|---|---|---|---|---|---|---|
| C1 | Car owners vs small car dealers / workshops | Disputes over used cars and repairs. Small dealers and workshops ignore ARN rulings | ARN Motor department intake rose from 5,556 (2024) to **6,664 (2025)**, about +20%. It is the largest ARN department and grew while total ARN intake fell 4%. Consumers won in 41% of cases tried on the merits. Only **74%** of firms complied with rulings. ARN says non-compliance is mainly "mindre bilhandlare och verkstäder" and that the cases involve large amounts. Vehicles were also the top category (23%) of 2025 complaints to municipal consumer advisers (Sveriges Konsumenter) | High (large ticket, a car is essential) | ARN (150 kr fee since Aug 2024), court, Konsumentverket | Large ticket per case; motor is the biggest consumer-detriment pool by count | Indirect: consumers pay the ARN fee; the warranty/inspection market already exists | Bilprovning-style checks, extended-warranty insurers, dealer-association guarantees | A (ARN) / B (SvKons) |
| C2 | Homeowners / BRF members vs craftsmen (hantverkare) | Overruns versus quote, delays, ROT-deduction confusion and rejections, poor workmanship | Category "Boende" was 17% of 2025 complaints to consumer advisers, and "varannat klagomål" within it concerns craftsman services. ARN Bostad department: 3,057 cases in 2025, 45% upheld when tried on the merits, 77% compliance. Forum threads (Byggahus) on ROT rejection years later and on price raised mid-job (25k to 31k kr) | High (savings at risk, home damage) | Konsumentverket/Byggföretagen standard contracts (Hantverkarformuläret 17), Reco reviews | Typical job 50–500k kr; ROT clawbacks | Platforms (Offerta, Servicefinder, Reco) monetise lead generation | Offerta, Servicefinder, Reco, Byggfakta | A/B/D |
| C3 | Solar/energy customers vs installers | Delivery delays, unclear technical information, sales over-promising, bankrupt installers leaving warranties orphaned | Energi/värme 4% of 2025 consumer-adviser complaints, "el och solceller" the most common within it. Reco 2025: solar installers had the lowest average craftsman rating (4.23/5). Svea Solar Trustpilot 4.3 (4,652 reviews); visible sample: 3/24 mention delays, 3/24 unclear information. Press reports a sharp rise in solar-installer bankruptcies (Dec 2025) | Medium-high | Chasing the installer; warranty lost if the installer goes bankrupt | Orphaned warranties and service on 100–300k kr systems | Owners pay for service and monitoring | Installer-agnostic O&M firms (few) | B/C |
| C4 | Telecom consumers | Billing errors, hard-to-reach support, binding contracts and cancellation | Telia Trustpilot TrustScore about 1.3 on 5,790 reviews, 87% 1-star. In the visible 20: billing 10, support 9, contracts 7. Telekom was 9% of 2025 consumer-adviser complaints (3rd largest) | Medium | Switching operator; ARN | Low per case, high volume | Low: consumers do not pay to fix telco issues | Price-comparison sites | B/C |
| C5 | BRF/tenant members vs property managers (HSB, Riksbyggen, SBC) | No response to fault reports (felanmälan), slow repairs, opaque fees, unhelpful chat-only support | HSB TrustScore 1.5 (132 reviews, 95% 1-star); visible: repairs about 8/21, no response about 8/21. Riksbyggen 2.0 (111 reviews, 82% 1-star); visible: "no response/follow-up" about 10/20, slow repairs about 7/20. SBC 4.0 (126) but 32% 1-star; visible: hard to reach a human 2/20, payment problems 2/20. BRF forum: associations switching economic administrator up to three times | Medium (water damage left 6 weeks in one review) | Board chases the manager; switch manager | Water damage escalates cost; board members' unpaid time | BRFs already pay management fees; switching happens | Nabo, Simpleko, Bostadsrättsservice, Boio, Brfapp | C/D |
| C6 | Micro-business owners vs accounting SaaS (Fortnox, Bokio) | Price increases and add-on module pricing, lock-in/cancellation friction, navigation | Fortnox TrustScore 3.4 (4,250 reviews; 18% 1-star); visible: price 7/23, usability 6/23 ("186 kr ... I år kostar det 435 kr i månaden"). Bokio 3.6 (1,101; 45% 1-star, polarised); visible: support 4/24, price 3/24, cancellation 3/24. Spiris (ex-Visma eEkonomi) 4.4 (995). Fortnox taken over (Spiris branschrapport cites a 55 bn SEK price, about 2 bn SEK revenue) | Medium (cost creep) | Accept increases or switch to Bokio/Spiris/accounting firm | Hundreds of SEK per month per firm across hundreds of thousands of firms | Strong: firms already pay monthly SaaS fees | Fortnox, Spiris, Bokio, Wint, accounting firms | C |
| C7 | Consumers vs foreign/dropship/social-media sellers | Cannot enforce rights; firms ignore ARN | ARN 2025: lower compliance explained by "alltfler anmälningar riktar sig mot utländska företag" and dropshipping. "Diverse" category (including "help" services) grew 19% in 2025 (SvKons) | Medium | Chargeback via card issuer | Small tickets, high volume | Weak | Card chargeback, Klarna disputes | A/B |
| C8 | Payment-fraud victims (authorised push payment) | Victims tricked into transferring money themselves | FI Konsumentskyddsrapport 2025: this fraud type "har ökat mest" | High | Bank reimbursement disputes, ARN Bank (13% upheld) | Large | Banks have strong incentive (regulatory) | Bank fraud teams, BankID controls | B |
| C9 | Home-care (hemtjänst) operations | Heavy dependence on a few systems (Lifecare/Phoniro/TES); outage routines; mandatory per-visit registration | Municipal routines document that when Lifecare/Phoniro is down only offline apps work for ~8 h (Söderköping). Linköping/Borås require TES registration per visit. 437 LOV systems in 2025, the most common for hemtjänst | Medium | Paper fallback routines | Staff time on admin | Paid by municipality/providers | Lifecare, TES (Tunstall/Phoniro), Alfa eCare | D (documents, not complaints) |
| C10 | Cleaning services (RUT) | Uneven quality, substitute staff, continuity | Hemfrid 4.4 (3,003 reviews; 9% 1-star); visible: incomplete cleaning 4/24, continuity 2/24 | Low | Re-clean guarantees | Low | Paid via RUT | Many | C |

Key quantified source for C1, C2, C4 and C7: ARN annual report 2025. Intake by department, 2023 → 2024 → 2025:
- Allmänna: 5,955 → 4,805 → 4,288
- Bank: 2,780 → 1,953 → 1,416
- Bostad: 3,617 → 3,065 → 3,057
- Elektronik: 3,607 → 2,973 → 2,564
- Försäkring: 1,478 → 1,475 → 1,844
- Motor: 5,621 → 5,556 → 6,664
- Möbler: 1,271 → 986 → 998
- Resor: 4,436 → 3,063 → 2,746
- Sko: 1,189 → 552 → 337
- Textil: 2,213 → 1,139 → 581
- Tvätt: 56 → 49 → 54
- **Total: 32,303 → 25,685 → 24,603**

The 150 kr fee introduced on 1 Aug 2024 depresses intake, so the 2025 increases in Motor and Försäkring are notable.

Gap: a Konsumentverket "Konsumentrapporten 2025/2026" was not found by search. Hallå konsument statistics were not found either.

---

## Method 2 – Procurement demand

### 2a. National statistics (UHM, Rapport 2026:1, Feb 2026)

| Metric | Value | Type (tender / award / framework) | Strength |
|---|---|---|---|
| Value of purchases subject to procurement law | **1,009 bn SEK** (latest stats, 2023 data), up 79 bn from 2022 | Spend estimate | A |
| Advertised procurements 2024 | 17,575, estimated value **931 bn SEK** | Tenders | A |
| Advertised procurements 2025 | 18,015, estimated 982 bn SEK (+454 notices) | Tenders. UHM statistic seen in a search snippet, not opened | B |
| Average bids per procurement | 5.9 (2023) → **4.6 (2024)**; mode 2, median 3 | Tenders | A |
| Share with a single bid | "nästan var femte", **about 20%** for several years | Tenders | A |
| Bids/procurement by CPV group, 2024 | IT services (72) **3.7**, down from 15.2 in 2021; Software (48) **2.3**; Finance/insurance (66) 2.1; Transport equipment (34) 2.5; Real-estate services (70) 2.8; Transport (60) 3.3; Repair and maintenance (50) 3.6; Sewage/waste/environment (90) 3.6; Arch/eng (71) 7.3; Business services (79) 5.7; Health and social (85) 9.6 | Tenders | A |
| Firms bidding | about 13,000 firms bid in 2024 | — | A |
| Award notices published (efterannonsering) | Only **64%** of 2024 procurements were post-announced (74% in 2022). eForms made post-announcing "mer komplext" | Awards | A |
| Valfrihetssystem (LOV) | 437 systems in 2025 (451 in 2024). Most common is hemtjänst. **52+ bn SEK** paid out in 2024 in 259 of 451 systems (Konkurrensverket) | Authorisations (not tenders) | A/B |
| Appeals | 3,643 appeal cases in 2025 (−2.5%) | — | A |
| State decision 2026 | Statskontoret tasked with a national procurement database and analysis function (Mar 2026) | Policy | B |

### 2b. Own analysis: TED award notices, Sweden, 1 Oct 2025 – 30 Sep 2026 (n = 9,032 notices; 14,117 lots with a tender count)

Method: TED Search API v3, query `buyer-country=SWE AND notice-type=can-standard`. Tender counts per lot come from the eForms field `received-submissions-type-val` (code `tenders`), grouped by each notice's main CPV. In the same period there were 13,038 contract notices (cn-standard). Strength: **A**, our own computation, reproducible; it covers TED-published notices only.

Overall: mean **4.4** tenders per lot, median 3. **22.4%** of lots had a single tender and 5.2% had zero.

| CPV division / code | Lots | Mean tenders | Median | % single-bid | Comment |
|---|---|---|---|---|---|
| 38 Lab/measuring instruments | 322 | 2.1 | 1 | **52%** | Proprietary equipment |
| 15 Food | 336 | 2.1 | 2 | 39% | |
| 24 Chemicals | 202 | 2.1 | 1 | 39% | |
| 34 Transport equipment | 672 | 2.5 | 2 | 33% | |
| **48 Software** | 243 | 2.1 | 2 | **33%** | Incumbent / lock-in signal |
| **72 IT services** | 829 | 4.8 | 2 | **31%** | Many single-bid "licenspartner", system support and named-vendor support |
| 33 Medical equipment | 1,855 | 3.3 | 2 | 29% | |
| 50 Repair and maintenance | 520 | 2.9 | 2 | 22% | |
| 50110000 Vehicle repair | 60 | 1.8 | 1.5 | 28% | |
| 66 Financial services | 130 | 2.4 | 2 | 24% | |
| 90 Sewage/waste/cleaning/environment | 1,180 | 4.4 | 3 | 18% | |
| 45 Construction | 1,344 | 4.6 | 4 | 10% | |
| 71 Arch/engineering | 2,022 | 7.5 | 5 | 14% | |
| 79 Business services | 937 | 6.2 | 4 | 12% | |
| 85 Health/social | 210 | 7.0 | 3 | 18% | |
| 79540000 Interpretation | 30 | 6.3 | 6 | 3% | Competitive (framework-driven) |
| 79620000 Staffing | 59 | 9.8 | 8 | 8% | Highly competitive |
| 71314300 Energy-efficiency consulting | 76 | 11.5 | 11 | 0% | Highly competitive |
| 79417000 Safety consultancy | 34 | 5.0 | 5 | 12% | |
| 72220000 IT consulting | 92 | 5.6 | 3 | 20% | |

Examples of single-tender IT/software awards (titles from TED; counted as 1 tender in at least one lot):
- Vårgårda kommun "Ekonomisystem"
- Statens servicecenter "Lönesystem med tillhörande tjänster"
- Huddinge kommun "E-tjänsteplattform" and "Learning management system"
- Uppsala kommun "Dokumenthanteringssystem"
- Räddningstjänsten Skåne NV "Verksamhetssystem"
- Region Västernorrland "System för beräkning av ersättning ... privata vårdgivare"
- Norrköping "IT-stöd för kvalitetsledning och hållbarhetsrapportering"
- Malmö "Service- och supportåtagande avseende IT-systemet ..."
- Multiple municipalities "Licenspartner" (Kinda, Sollentuna, Vetenskapsrådet)
- Enköping "Digitalt planeringsverktyg för skolskjuts"
- Lunds kommun "Lösning för algoritmisk tilldelning av elever"

Full-text keyword counts in Swedish TED contract notices for the same 12 months. Strength **B−**: full-text matching semantics are unverified, and "AI" matched almost everything, so this was discarded.
- informationssäkerhet: 46
- hemtjänst: 35
- säkerhetsskydd: 27
- bygglov: 19
- krisberedskap: 14
- tolkförmedling: 9
- upphandlingsstöd: 7
- dataskydd: 6
- penetrationstest: 4
- civilförsvar: 3
- energirådgivning: 1
- tillgänglighetsgranskning: 0
- NIS2: 0

Interpretation: specialist municipal needs (civil defence, accessibility audits, procurement support) are mostly bought **below the EU threshold, via direct awards, or through frameworks**, so they barely appear on TED. Visibility needs national databases (e-Avrop, Mercell/TendSign, Visma Opic), which were not scraped here.

### 2c. Framework agreements (central purchasing bodies)

| Body | Framework | Suppliers (count) | Valid to (earliest – latest) | Signal | Strength |
|---|---|---|---|---|---|
| Statens inköpscentral (avropa.se, list dated 2026-10-29) | IT-konsulttjänster Resurskonsulter | 24 | 2026-11-30 – 2030-03-09 | Some contracts expire 30 Nov 2026 | A |
| " | Kommunikationstjänster tele/datakom | 5 | 2026-12-31 | Expiring now, so re-procurement is due | A |
| " | **Tolkförmedlingstjänster** | 7 | 2027-02-14 – 2027-04-25 | Renewal in 2027 | A |
| " | Städtjänster | 5 | 2027-02-14 | Renewal 2027 | A |
| " | Programvaror och tjänster | 19 | 2027-02-17 – 2027-10-31 | Renewal 2027 | A |
| " | Bevaknings- och larmcentraltjänster | 13 | 2027-03-31 | Renewal 2027 | A |
| " | Översättning och språktjänster | 7 | 2027-06-08 – 2030-08-12 | | A |
| " | Säkerhetsteknik | 10 | 2027-06-19 – 2027-09-10 | Renewal 2027 | A |
| " | Företagshälsa | 8 | 2027-12-31 | | A |
| " | Managementtjänster | 19 | 2028-06-30 – 2029-09-14 | | A |
| " | IT-drift | 11 | 2028-11-13 | | A |
| " | Bemanningstjänster | 18 | 2029-04 | | A |
| " | Flyttjänster | 28 | 2029-11-30 | | A |
| Adda (SKR), current | Includes "IT-säkerhet – Incidenthantering (IRT) DIS", "Säker digital kommunikation DIS", "Säkerhetslösningar konsulter 2025", "Reservkraft 2025", "Livsmedel krisberedskap 2023", "CBRN-utrustning 2025", "Ekonomisystem 2027", "Uppföljandekontroll inom socialtjänsten 2023", "Digital trygghetstjänst" (welfare tech) | — | — | Preparedness and cyber are now framework-ised. **No interpreter framework** in Adda | A |
| Adda upphandlingsplan 2027/2028 | 2027: Programvaror och molntjänster (start 2028-10-01), Inkasso/påminnelse (2028-09), Bevakning/larmcentral (2028-08), Banktjänster, Pension, AV, Sjunet. 2028: **Bemanningstjänster** (start 2030-01-29), Stödboende för äldre | — | — | Upcoming windows to get onto frameworks | A |

Distinctions: UHM figures are **advertised tenders** and their estimated value. TED counts are **awards** (can-standard). Framework rows are **ceilings/agreements**, not spend.

---

## Method 3 – Hiring signals

| Occupation / area | Signal | Source (date) | Productisable or outsourceable? | Strength |
|---|---|---|---|---|
| Total vacancies | **159,500** in Q2 2026 (+8% y/y, within the margin of error). Business sector 122,400; municipalities 19,400; state 7,100; regions 5,400. Jämtland 8.1 per 100 jobs, Gotland 4.9 | SCB, 28 Aug 2026 | — | A |
| **Inköpare och upphandlare** | **Brist**, large job opportunities, demand expected to **increase** in 5 years (national) | AF Yrkesbarometer, June 2026 | Yes: procurement-support-as-a-service, tender-writing tools for buyers, AI spec drafting. Complements UHM data showing eForms complexity and only 64% post-announcement | A |
| **IT-säkerhetsspecialister** | Brist, increasing | AF YB June 2026 | Yes: managed security / NIS2 (Cybersäkerhetslagen) compliance for municipalities and SMEs. Adda has an IRT DIS | A |
| Systemanalytiker/IT-arkitekter, IT-strateger, mjukvaruutvecklare | Brist, increasing | AF YB June 2026 | Partially: system migration services | A |
| **Säkerhetsrådgivare och inspektörer** | Brist, increasing | AF YB June 2026 | Yes: security-protection (säkerhetsskydd) and preparedness advisory as a service. "säkerhetsskydd" appears in 27 TED notices | A |
| **Revisorer** | Brist, increasing | AF YB June 2026 | Partially: audit automation | A |
| Installations-/service-, distributions- and industrial electricians; drifttekniker värme/vatten; VVS-montörer; bil- and lastbilsmekaniker | Brist, increasing | AF YB June 2026 | Field-service software, scheduling, apprentice pipelines; capacity is the bottleneck (links to C1–C3) | A |
| Nurses (several specialties), doctors, tandläkare, etc. | Brist, increasing | AF YB June 2026 | Hyrpersonal market; scheduling and retention tools | A |
| Undersköterskor in hemtjänst/äldreboende | **Paradox** (shortage of suitable candidates despite applicants), increasing | AF YB June 2026 | Training and validation, language support | A |
| Löne- och personaladministratörer | **Överskott**, small opportunities | AF YB June 2026 | Counter-signal: payroll admin is *not* in shortage, so a "labour-shortage" pitch for payroll tools is weak. Efficiency or quality pitches only | A |
| Ekonomiassistenter; administrativa assistenter; systemadministratörer | Överskott | AF YB June 2026 | Same: automation competes with abundant labour | A |
| Redovisningsekonomer | Balance, increasing | AF YB June 2026 | Moderate | A |
| Socialsekreterare, lantmätare, planeringsarkitekter, miljö- och hälsoskyddsinspektörer, jurister, planerare/utredare | **Balans** (not shortage) in June 2026 | AF YB June 2026 | Counter-signal against "municipalities can't hire bygglov/planning staff" at national level (regional shortages may exist; not checked) | A |
| Labour-shortage indicator | KI Konjunkturbarometern diagram appendix Aug 2026 shows shortage series by sector (values not extracted). Media (Realtid, Jul 2026) report a rising experienced labour shortage | KI / Realtid | — | B |

Caveat: job-ad or shortage status does not equal software buying. Shortages in electricians, VVS and mechanics mean **capacity-constrained suppliers**. This explains slow service and complaints (C1–C3) more than it signals SaaS demand.

---

## Method 6 – Spending leakage

| Area | Documented cost | Year | Source | Note | Strength |
|---|---|---|---|---|---|
| Regions: hired healthcare staff (hyrpersonal) | **≈7.9 bn SEK** (2022, +25% y/y; 6.3 bn 2021; 3.9 bn 2015). Doctors 54%, nurses 45%. Average about 4.8% of own personnel costs | 2022 | Läkartidningen citing SKR (7 Mar 2023) | Newer national totals not retrieved (search budget) | B |
| Region-level hyrpersonal | Västernorrland **18.3%** of own personnel costs (2023, record). Gävleborg hired nurses 13.8% (end 2023) → 9.1% (Q2 2024), target ≤2% by end 2025. Västmanland −98 m SEK Jan–Aug 2024 | 2023–24 | Läkartidningen (20 Sep 2024) | Shows the reduction trend; rural regions are worst | B |
| Region Värmland | 50,000 SEK/month salary supplement to break hyrläkare dependence at 6 rural health centres | Apr 2026 | Läkartidningen (10 Apr 2026) | Persistent rural primary-care dependence | B |
| LOV (choice systems) payouts | **>52 bn SEK** (2024, 259 of 451 systems) | 2024 | Konkurrensverket via UHM report | Large spend with weak follow-up data ("ingen tillgänglig statistik om hur stora värden") | A/B |
| Accounting services market | about **53 bn SEK** (2025), projected 69 bn. About 8,900 sole-trader/partnership "low-price" bureaus. Big 4 about 18 bn | 2025 | Spiris Branschrapport 2025 (vendor) | SME spend on bookkeeping outsourcing | B |
| Procurement process costs | Only 64% of awards post-announced; about 20% single-bid; 4.6 bids average (falling). Leakage = weak competition | 2024 | UHM | Each extra bidder typically lowers price (not quantified here) | A |
| Legacy/lock-in software | 31–33% of TED IT/software award lots received **one** tender. Examples include municipal ekonomisystem, lönesystem, dokumenthantering and verksamhetssystem | Oct 2025 – Sep 2026 | Own TED analysis | Indicates switching cost / incumbent advantage | A |
| Municipal consultant costs ("konsultkostnader kommuner") | **Not retrieved.** The search budget was exhausted before finding a reliable national figure | — | — | Gap: follow up with SKR, Kommuninvest or SCB Räkenskapssammandrag | — |

---

## Opportunity hypotheses (evidence-backed; each must be validated with interviews)

1. **ARN-compliance and dispute-resolution layer for used-car and workshop transactions** (C1). Escrow, warranty-backed "verified dealer" status and automated claim packs. Evidence: Motor intake +20% to 6,664; only 74% compliance, driven by small dealers. Buyer: consumers via marketplaces (Blocket), insurers. Strength A.
2. **Workshop operations/booking SaaS that tackles capacity** for small car workshops (mechanics in shortage; vehicle-repair public tenders draw a median of 1.5 bids). Strength A/C.
3. **Craftsman-contract and ROT "change-order" tool**. Digital quote → binding agreement → documented change orders → ROT submission check. Evidence: Boende 17% of complaints, half of it craftsman; ARN Bostad 3,057; ROT rejection threads. Buyer: craftsman firms, or platforms (Offerta/Reco) as an upsell. Strength B.
4. **Installer-agnostic solar/battery service and warranty-rescue provider** (orphaned systems after installer bankruptcies). Evidence: lowest Reco rating among craftsmen, solar the most common energy complaint, bankruptcy reports. Strength B/C.
5. **BRF fault-report (felanmälan) transparency and SLA layer** on top of incumbent managers (HSB/Riksbyggen/SBC). Evidence: 82–95% 1-star shares; "no response" and "slow repairs" dominate the visible samples. Buyer: BRF boards (already paying fees). Strength C.
6. **BRF economic-administration switching service / benchmark** (fees, interest on accounts, service levels). Evidence: SBC interest-transparency complaints; forum reports of serial switching. Strength C/D.
7. **SME accounting-cost optimiser / transparent flat-price bookkeeping** to counter Fortnox add-on price creep (435 vs 186 kr/month example). 53 bn SEK accounting-services market. Buyer: micro-firms. Strength C (WTP proven by existing spend).
8. **Procurement-support-as-a-service for small municipalities and public companies.** Spec drafting, eForms post-announcement compliance, supplier outreach to raise bid counts. Evidence: upphandlare in shortage (AF), only 64% post-announced, about 20% single-bid, falling bids (4.6). Strength A.
9. **Supplier-side "bid-readiness" service for SMEs** in low-competition categories (software, IT, repair, lab instruments, food). Evidence: 22% single-tender lots on TED; only about 13,000 firms bid nationally. Strength A.
10. **Public-sector legacy-system exit / migration service** (ekonomi-, löne-, dokumenthantering- and verksamhetssystem), sold to break single-bidder lock-in. Evidence: 31–33% single-tender lots in CPV 48/72. Adda "Ekonomisystem 2027" and "Programvaror och molntjänster 2027" (start Oct 2028) are the next windows. Strength A.
11. **Managed cybersecurity / NIS2 compliance for municipalities and municipal companies.** Evidence: IT-säkerhetsspecialister in shortage; "informationssäkerhet" in 46 TED notices; Adda IRT DIS exists (route to market). Strength A/B.
12. **Säkerhetsskydd and civil-preparedness advisory as a subscription.** Evidence: säkerhetsrådgivare in shortage; "säkerhetsskydd" in 27 and "krisberedskap" in 14 TED notices; UHM highlights preparedness. Adda frameworks for reservkraft, CBRN and livsmedel krisberedskap. Strength B (TED counts low, so much is bought below threshold).
13. **Rural primary-care staffing alternative.** Telemedicine plus rotating permanent-doctor pools to cut hyrläkare dependence. Evidence: Värmland 50k/month supplement; Västernorrland 18.3% hyr-share; about 7.9 bn SEK national (2022). Buyer: regions. Strength B.
14. **Follow-up and analytics for LOV (hemtjänst) spend.** Evidence: >52 bn SEK paid via LOV in 2024 with no national value statistics; 437 systems; Adda framework "Uppföljandekontroll inom socialtjänsten". Strength A/B.
15. **Hemtjänst operational resilience tooling** (offline-first visit registration, outage fallbacks across Lifecare/TES/Phoniro). Evidence: municipal outage routines; per-visit registration rules. Strength D, needs validation.
16. **Telecom bill-audit and cancellation assistant for households and SMEs.** Evidence: Telia 87% 1-star; billing errors 10/20 visible; Telekom 9% of complaints. WTP weak, so this probably needs a success-fee model. Strength C.
17. **Cross-border/dropshipping purchase-protection tool** (chargeback automation). Evidence: ARN cites foreign and dropship firms lowering compliance; "Diverse" +19%. Strength B.
18. **Bid-competition insight product for buyers** (single-bid early warning by CPV and region), built on TED and national data. Statskontoret's national-database mandate creates timing and partnering potential. Strength A/B.
19. **Field-service capacity marketplace for electricians and VVS** (subcontract matching, apprentice/certificate tracking). Evidence: all electrician categories and VVS in shortage (AF). Construction lots still draw a median of 4 bids. Strength A (shortage); demand-side WTP unverified.

Counter-signals to respect:
- Payroll and admin roles are in **surplus**, so "replace a scarce admin" pitches are weak.
- Interpretation, staffing and energy-efficiency consulting tenders are **highly competitive** (6–11 bids), so they are poor entry points.
- Social secretaries and planning roles are in national **balance**.

---

## Source Ledger

| URL | Publisher | Title | Pub date | Retrieved | Finding | Reliability |
|---|---|---|---|---|---|---|
| https://arn.se/globalassets/extern/arsredovisningar/allmanna-reklamationsnamndens-arsredovisning-2025.pdf | ARN | Årsredovisning 2025 | 2026 (Feb) | 2026-10-29 | Intake by department; Motor 6,664 (+20%); compliance 76% (Motor 74%); small dealers/workshops non-compliant; foreign/dropship firms | High (official) |
| https://www.upphandlingsmyndigheten.se/globalassets/dokument/publikationer/rapport-om-utvecklingen-pa-upphandlingsomradet-2025.pdf | Upphandlingsmyndigheten | Rapport om utvecklingen på upphandlingsområdet 2025 (Rapport 2026:1) | Feb 2026 | 2026-10-29 | 1,009 bn SEK; 17,575 notices / 931 bn (2024); 4.6 bids; about 20% single-bid; CPV table; 64% post-announced; LOV 52 bn | High (official) |
| https://www.upphandlingsmyndigheten.se/statistik/upphandlingsstatistik/ (via search snippet) | Upphandlingsmyndigheten | Annonserade upphandlingar 2025 | 2026 | 2026-10-29 | 18,015 notices, 982 bn SEK in 2025 | Medium (snippet, not opened) |
| https://api.ted.europa.eu/v3/notices/search | EU Publications Office (TED) | TED Search API: SWE can-standard / cn-standard, 2025-10-01 – 2026-09-30 | live | 2026-10-29 | 9,032 awards / 14,117 lots; 22.4% single-tender; CPV 48/72 at 31–33%; 13,038 contract notices | High (own analysis of official data; TED-only scope) |
| https://www.avropa.se/giltigaramavtal/excel | Statens inköpscentral (Kammarkollegiet) | Giltiga ramavtal 2026-10-29 | 2026-10-29 | 2026-10-29 | Framework areas, supplier counts, expiry dates | High |
| https://www.avropa.se/ramavtal/ramavtalsomraden/ | Statens inköpscentral | Ramavtalsområden | n/a | 2026-10-29 | 16 framework areas | High |
| https://adda.se/upphandling-och-ramavtal/ramavtal-och-avtalskategorier/ | Adda (SKR) | Ramavtal och avtalskategorier | n/a | 2026-10-29 | IRT DIS, säkerhetslösningar, krisberedskap, Ekonomisystem 2027 | High |
| https://adda.se/upphandling-och-ramavtal/planerade-och-pagaende-upphandlingar/upphandlingsplan2027/ | Adda | Upphandlingsplan 2027 | Oct 2026 | 2026-10-29 | 2027/2028 planned procurements incl. Programvaror och molntjänster, Bemanningstjänster 2028 | High |
| https://arbetsformedlingen.se/download/18.28feed2519e47aff4a527f2/1781072408824/arbetsformedlingens-yrkesbarometer-2026-juni.xlsx | Arbetsförmedlingen | Yrkesbarometer juni 2026 | Jun 2026 | 2026-10-29 | 57 national brist occupations incl. upphandlare, IT-säkerhet, säkerhetsrådgivare, electricians; payroll admin in surplus | High (official) |
| https://www.scb.se/hitta-statistik/statistik-efter-amne/arbetsmarknad/efterfragan-pa-arbetskraft/lediga-jobb-och-rekryteringsbehov/pong/statistiknyhet/lediga-jobb-och-rekryteringsbehov-2a-kvartalet-2026/ | SCB | Lediga jobb och rekryteringsbehov, Q2 2026 | 28 Aug 2026 | 2026-10-29 | 159,500 vacancies; sector and county split | High |
| https://www.konj.se/media/toqcyhd3/diagrambilaga-augusti-2026.pdf | Konjunkturinstitutet | Diagrambilaga Konjunkturbarometern aug 2026 | Aug 2026 | 2026-10-29 | Labour-shortage series exist (values not extracted) | High (unused values) |
| https://www.tv4.se/artikel/tt-260113-konsumtion1-f187f769/svenskarnas-samsta-kop-2025 | TV4/TT citing Sveriges Konsumenter | Svenskarnas sämsta köp 2025 | 13 Jan 2026 | 2026-10-29 | Complaint shares: Fordon 23%, Boende 17%, Telekom 9%, Energi 4% (el/solceller) | Medium (media citing NGO stats) |
| https://www.reco.se/foretag/blog/reco-rapporten-hantverkare-2025-var-tionde-hantverkare-far-underkant-men-vissa-branscher-imponerar-stort | Reco | Reco-rapporten Hantverkare 2025 | 2025 | 2026-10-29 | Solar installers lowest avg rating 4.23 (22,000+ reviews, 1,137 firms); via search snippet | Medium (vendor) |
| https://brusselssignal.eu/2025/12/sharp-rise-in-bankruptcies-burns-swedish-solar-installation-sector | Brussels Signal | Sharp rise in bankruptcies burns Swedish solar installation sector | Dec 2025 | 2026-10-29 | Solar installer bankruptcies (headline only) | Low-Medium |
| https://www.fi.se/contentassets/5f29050213f543ff9fc1b289de95c21d/konsumentskyddsrapporten-2025.pdf | Finansinspektionen | Konsumentskyddsrapport 2025 | Apr 2025 | 2026-10-29 | APP fraud increased most (snippet) | High |
| https://se.trustpilot.com/review/www.fortnox.se | Trustpilot | Fortnox reviews | live | 2026-10-29 | 3.4 / 4,250; visible: price 7/23, usability 6/23 | Low-Medium (sample C) |
| https://se.trustpilot.com/review/bokio.se | Trustpilot | Bokio reviews | live | 2026-10-29 | 3.6 / 1,101; 45% 1-star; support, price, cancellation | Low-Medium (C) |
| https://se.trustpilot.com/review/www.spiris.se | Trustpilot | Spiris reviews | live | 2026-10-29 | 4.4 / 995; wait times | Low-Medium (C) |
| https://se.trustpilot.com/review/sbc.se | Trustpilot | SBC reviews | live | 2026-10-29 | 4.0 / 126; 32% 1-star; reachability, payments | Low-Medium (C) |
| https://se.trustpilot.com/review/www.hsb.se | Trustpilot | HSB reviews | live | 2026-10-29 | 1.5 / 132; 95% 1-star; repairs, no response | Low-Medium (C) |
| https://se.trustpilot.com/review/riksbyggen.se | Trustpilot | Riksbyggen reviews | live | 2026-10-29 | 2.0 / 111; no follow-up on felanmälan | Low-Medium (C) |
| https://se.trustpilot.com/review/sveasolar.se | Trustpilot | Svea Solar reviews | live | 2026-10-29 | 4.3 / 4,652; delays, unclear info | Low-Medium (C) |
| https://se.trustpilot.com/review/www.hemfrid.se | Trustpilot | Hemfrid reviews | live | 2026-10-29 | 4.4 / 3,003; uneven cleaning, continuity | Low-Medium (C) |
| https://se.trustpilot.com/review/www.telia.se | Trustpilot | Telia reviews | live | 2026-10-29 | about 1.3 / 5,790; billing 10/20, support 9/20 | Low-Medium (C) |
| https://www.reco.se/fastighetsagarna-service?lang=en | Reco | Fastighetsägarna Service reviews | live | 2026-10-29 | BRF switched economic administrator 3 times (snippet) | Low (D) |
| https://www.byggahus.se/forum/threads/avslag-pa-rotavdrag.325261/ | Byggahus forum | Avslag på ROT-avdrag | n/a | 2026-10-29 | ROT rejection disputes (snippet) | Low (D) |
| https://soderkoping.se/globalassets/documents/04-stod-o-omsorg/13-utforarwebb/04-it-och-system/rutin-vid-avbrott-i-verksamhetssystemen-lifecare_phoniro.pdf | Söderköpings kommun | Rutin vid avbrott i verksamhetssystemen Lifecare/Phoniro | n/a | 2026-10-29 | Offline apps ~8 h during outages | Medium (D for demand) |
| https://lakartidningen.se/nyheter/kostnader-for-hyrpersonal-okar/ | Läkartidningen (citing SKR) | Kostnader för hyrpersonal ökar | 7 Mar 2023 | 2026-10-29 | 7.9 bn SEK hyrpersonal 2022 | Medium-High |
| https://lakartidningen.se/nyheter/hyrkostnaderna-sjunker-pa-flera-hall-nu-aterrekryteras-sjukskoterskor/ | Läkartidningen | Hyrkostnaderna sjunker på flera håll | 20 Sep 2024 | 2026-10-29 | Västernorrland 18.3%; Gävleborg 13.8→9.1% | Medium-High |
| https://lakartidningen.se/nyheter/notiser/50-000-kronor-i-lonepaslag-ska-bryta-hyrlakarberoende/ | Läkartidningen | 50 000 kronor i lönepåslag ska bryta hyrläkarberoende | 10 Apr 2026 | 2026-10-29 | Värmland supplement, 6 health centres | Medium-High |
| (Spiris PDF, retrieved by a parallel fetch in this session; original URL on spiris.se) | Spiris | Branschrapport 2025: Tillväxt, teknikskifte och nya marknadsstrukturer | 2025 | 2026-10-29 | Accounting market about 53 bn SEK → 69 bn; Fortnox deal 55 bn | Medium (vendor) |
| https://upphandling24.se/wp-content/uploads/2026/03/260305-Beslut-Uppdrag-till-Statskontoret-om-en-nationell-upphandlingsdatabas-och-en-analysfunktion-for-inkops-och-upphandlingsdata.pdf | Regeringen (via Upphandling24) | Uppdrag till Statskontoret om nationell upphandlingsdatabas | 5 Mar 2026 | 2026-10-29 | National procurement database mandate (title only) | Medium |
