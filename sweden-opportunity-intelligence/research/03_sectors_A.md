# 03 – Sector Screen A: Swedish B2B/B2G sectors for a small founding team

Reference date: 29 October 2026 (launch window 2026–2028). Researcher: sector-screen agent A.

## How to read this file (method and limits)

- **Hard numbers come mainly from three kinds of sources.**
  - SCB's open statistics API, pulled live on 2026-10-29:
    - Företagsdatabasen (FDB): firm counts by SNI 2007 and size class, register year 2025, table updated 2025-12-02.
    - Företagens ekonomi: turnover, employees and value added for 2022–2024.
    - Branschnyckeltal: operating-margin quartiles for 2024.
    - IT-användning i företag: AI, security and robots.
  - Riksdagen's open-data documents (budget and legislative propositions).
  - Industry and trade-press pages fetched directly.
- **Reliability tags in the Source Ledger:**
  - **H**: primary source fetched and read.
  - **M**: secondary source fetched and read.
  - **L**: seen only as a search-engine snippet; not opened and not independently verified. Treat L figures as leads only.
- **Limitation:** the shared web-search budget for this run ran out partway through. That left these sectors thinner than the others: 3 Logistics, 6 Cybersecurity, 8 Fintech, 10 Legal, 20 IT infra / data centres, 25 Robotics. For them, the evidence is mostly SCB structural data plus primary legislation. Open gaps are marked **[GAP]**. Do not fill them with guesses.
- **Estimates and derived numbers** are marked **(est.)** or **(derived)**, with the arithmetic shown.
- **SCB caveats:**
  - "Firms" counts every registered enterprise, including those with 0 employees (many are dormant shells or sole traders). "Firms w/ employees" is the better proxy for real buyers.
  - Turnover from Företagens ekonomi covers the business sector, including municipally owned companies. It excludes public administration, so publicly run healthcare, eldercare and VA are under-represented.
  - Median operating margins are firm-level medians across all sizes. Small owner-managed firms distort them, because the owner's pay is taken as salary or as profit. Use them as indicative only.

---

## 1. Sector matrix (summary)

| # | Sector | Swedish market-size anchor (source) | Prospective buyers (count) | Fragmentation | Median op. margin 2024 (SCB) | Regulation driver 2026–28 | Score (1–10) |
|---|---|---|---|---|---|---|---|
| 1 | Healthcare & eldercare | Municipal eldercare cost **166 bn SEK (2024)**. Hemtjänst ≈35% of that. Private eldercare purchases ≈23 bn, of which hemtjänst ≈8 bn [Vårdföretagarna]. Private health firms (SNI 86) had 113.5 bn turnover in 2024 [SCB] | 290 municipalities and 21 regions. 435 hemtjänst firms for the elderly with employees, 341 of them 20+ staff. 827 disability-service/assistance firms with employees [SCB FDB 2025] | High on the provider side; concentrated on the buyer side (municipalities) | Hemtjänst (88.101) 5.6%; residential care (87) 8.8%; staffing (78.20) 6.1% | New Social Services Act (2025:400); fast omsorgskontakt; language requirement from 1 Jul 2026 [L]; IVO's expanded reporting duty | **6** |
| 2 | Construction & property mgmt (incl. BRF) | Construction investment ≈690 bn SEK in 2027 [Byggföretagen]. Commissioned property management (68.32) had 54.2 bn turnover in 2024 [SCB] | ~29–30k BRFs [L]. 121,575 property firms (68), 13,829 with employees. 1,105 commissioned property managers with employees [SCB] | Very high | 68.32 10.6%; VVS 5.5%; el 6.2% | EPBD implementation (new energy classes, building renovation plan due to the EU 31 Dec 2026). OVK/SBA are ongoing obligations | **7** |
| 3 | Logistics & transport | ≈1,500 bn SEK sector turnover; ≈56k firms; ≈325k employees [Transportföretagen, undated] | 7,488 haulage firms with employees (49.41), 751 of them 20+ staff [SCB] | Very high in haulage | Haulage 6.5%; warehousing 4.7% | [GAP] (e.g. EU Mobility Package, tachograph rules not verified) | **4** |
| 4 | Manufacturing & industrial automation | Machinery industry (28) 420.7 bn turnover in 2024; metal products (25) 196 bn [SCB] | 19,264 manufacturers with employees; 3,557 with 20+ [SCB FDB 2025] | Medium | Machinery 6.9%; metal goods 5.8%; repair/installation (33) 8.3% | EU Machinery Regulation; CBAM; NIS2 for some | **5** |
| 5 | Energy & grid | Grid needs ≈945 bn SEK of investment to 2045 [L, Energiföretagen/Ellevio]. Electricity distribution (35.13) 69.2 bn turnover in 2024 [SCB] | 168 grid companies (147 local) [Regelrådet]. 5,717 electrical installers with employees [SCB]. ~314,600 grid-connected PV plants [pv magazine/Energimyndigheten] | Grid concentrated (top 3 = 52% of customers). Installers fragmented | Distribution 16.6%; electrical installers 6.2% | Mandatory effektavgift repealed (Mar 2026). Ei must propose a new model by 12 Apr 2027. Svk is reforming connections (an allocation system from 2027) | **7** |
| 6 | Cybersecurity | [GAP]: no verified Swedish market size this pass | Cybersäkerhetslagen in force 15 Jan 2026; government estimate "drygt 1 500 företag / ~500 000 employees" affected (≥50 staff). Only 40% of 10–49-employee firms have IT-security policy documents (2024) [SCB] | High (many MSSPs/consultants) | n/a | NIS2 (cybersäkerhetslagen), CER law proposed for 1 Jan 2027, DORA (finance) | **6** |
| 7 | Defence & civil preparedness | Budget area 6 (UO6): 128.2 bn SEK (2024 outturn), 225.0 bn proposed for 2026, 234.0 bn for 2027 (incl. Ukraine support). Target 3.5% of GDP by 2030 [Prop. 2025/26:1] | FMV/Försvarsmakten plus ~290 municipalities, 21 regions and businesses with preparedness duties. Weapons industry (25.4) only 12 firms with employees [SCB] | Prime-contractor dominated | Weapons (25.4) 13.8 bn turnover, up 52% 2022→24 [SCB] | Civil defence: up to 50 of 300 bn SEK loan-financed top-ups for infrastructure and stockpiles | **6** |
| 8 | Financial services & fintech | 66 (financial auxiliaries) 2,000 firms with employees; 64 (banks/credit) 2,766 with employees [SCB] | as left | Oligopoly in banking | n/a | DORA; FI 2026 priorities: operational resilience, AML/fraud, consumer credit | **3** |
| 9 | Accounting, bookkeeping & tax | ≈61 bn SEK (accounting 25, audit 18, tax/advisory 13) plus ~5 bn software (est.) [Spiris 2025]. SNI 69.20 turnover 64.8 bn in 2024, up 16.6% from 2022 [SCB] | 23,921 accounting/bookkeeping firms (69.201), 8,126 with employees, only **114** with 20+ staff [SCB FDB 2025]. ~25,000 providers [Spiris] | **Extreme** (62% of accounting done by ABs with <10 staff) | 69.201 16.7% | AML registration; Fortnox price and licence changes (autumn 2025 to Apr 2026) | **8** |
| 10 | Legal & regulatory compliance | Legal firms (69.10): 38.9 bn SEK turnover 2024, up 17% from 2022; 13,446 employees [SCB] | 3,120 law firms with employees, only 105 with 20+ [SCB] | High | 21.7% | NIS2/CER/DORA/AI Act/CSRD create compliance demand among *other* sectors | **6** |
| 20 | IT infra / cloud / data centres | Data processing and hosting (63.11): 145.1 bn turnover 2024 vs 100.6 bn 2022 (+44%) [SCB] | 910 firms with employees in 63.1 [SCB] | Hyperscaler-dominated | 63.11 5.5% (wide spread) | EED data-centre reporting ≥500 kW [Prop. 2024/25:131] | **4** |
| 25 | Robotics & specialised hardware | [GAP] on market size. Only ~29% of manufacturers with 10+ staff used robots in 2022 [SCB, derived] | 19,264 manufacturers with employees | Global OEM-dominated (ABB etc.) | n/a | EU Machinery Regulation (2027) | **3** |
| VA | Water & sewer | Need **590 bn SEK to 2040 (≈37 bn/yr)** vs ~31.5 bn invested in 2025. Average 2026 VA-taxa +7.5% (single-family houses) [Svenskt Vatten 2026-10-01] | 290 municipalities / VA principals (huvudmän). SNI 36: 62 firms with employees; SNI 37: 172 [SCB] | Concentrated, municipal | 36: 3.2%; 37: 6.3% | CER/NIS2 cover water utilities; EU urban waste water directive [GAP on details] | **5** |

The scores are preliminary and weigh five things for a 2–4 person team: buyer count and reachability, pain intensity, regulatory forcing, recurring revenue, and barriers to entry. See the rationale in each sector section below.

---

## 2. Per-sector detail

### Sector 1 – Healthcare & eldercare (hemtjänst, LSS, private providers, staffing)

**Market size**
- Total municipal eldercare cost: **166 bn SEK in 2024**, up more than 50 bn over 10 years, mostly from cost increases [S12].
  - Special housing (särskilt boende) is 57% of that.
  - Hemtjänst is 35%, which gives ≈58 bn SEK (derived: 0.35 × 166).
- Purchases from private providers:
  - Municipal purchases of eldercare from private providers: just over **23 bn SEK (2024)**. Of this, 15.2 bn was special housing and **almost 8 bn hemtjänst** [S12].
  - In 2025, municipalities bought **15.3%** of their care operations from private firms, or 19.4% including other public providers [S13].
  - Regions bought **12.3%** of healthcare from private firms in 2025 [S14].
- Private healthcare firms (SNI 86): 113.5 bn SEK turnover in 2024, against 103.5 bn in 2022 [S2].

**Buyers and providers**
- Buyers: 290 municipalities and 21 regions. Around 180 municipalities ran LOV (free choice) in hemtjänst over 2022–2025, described as "knappt hälften" of all municipalities and declining. Only **28** ran LOV in special housing [S12].
- Private providers, from SCB FDB 2025 [S1]:
  - Hemtjänst for the elderly (88.101): 708 firms, 435 with employees, **341 with 20+ staff** (214 with 100+).
  - Disability services including personal assistance (88.102): 1,246 firms, 827 with employees.
  - Residential care (87): 1,930 firms, 1,126 with employees.
  - Staffing firms (78.200): 5,758 firms (2,739 with employees, up from 2,176 in 2020). This covers all staffing, not only care staffing.
- Hemtjänst firms are few but large: at least 20 staff in 341 of 435 cases. They are a reachable list of B2B buyers, as are the 290 municipal care administrations.

**Growth**
- Hemtjänst recipients grew by only "knappt 10 000" over ten years [S12].
- Workload per carer rose: 9.16 recipients per carer on weekdays in 2024, 10.06 in 2025 [L, S17]. Productivity pressure is rising.
- Regional costs for hired staff fell 2.6% (−62 MSEK) in H1 2026 versus H1 2025. The decline is slowing, and hired-doctor costs rose [S15]. That implies roughly 2.3–2.4 bn SEK for the half-year (derived: 62/0.026 ≈ 2.38 bn for H1 2025; est.).

**Margins**
- Median operating margins in 2024 [S3]:
  - Hemtjänst (88.101): **5.6%**. Interquartile range 0.4–12.1%, so it is thin.
  - Residential care (87): 8.8%.
  - Staffing (78.20): 6.1%.
  - Health units (86): 20.3%. This is skewed by small practitioner companies.

**Failures and exits**
- No SNI-specific bankruptcy count was verified [GAP].
- Uppsala terminated its hemtjänst LOV contracts as of 31 Aug 2025 [L, S52]. That is an example of municipal policy risk for providers.

**Procurement**
- Two routes: LOV (accreditation, price fixed by the municipality, usually an hourly rate adjusted by the OPI index), or LOU tenders.
- Software is bought by municipalities through framework or LOU procurement, which takes 6–18 months (est., typical; not verified here).
- Private providers buy software directly. That is a faster SaaS sales cycle.

**Regulation**
- New Social Services Act (2025:400). It brings new documentation requirements for services given without individual needs assessment [L, S18].
- An SFS amendment from May 2026 requires that hemtjänst recipients be offered a **fast omsorgskontakt** (a permanent named care contact) [L].
- Language requirement in eldercare (Prop. 2025/26:93), in force 1 Jul 2026 [L].
- IVO expects more reports under the municipalities' expanded reporting duty [L, S51].

**Painful manual workflows and dissatisfaction**
- Minute scheduling:
  - Socialstyrelsen's autumn-2025 survey found about one in four municipalities uses **minutstyrning** (minute-based scheduling) in hemtjänst.
  - Kommunal demanded negotiations in **100 municipalities** to remove it. Staff say "Vi stressar till bristningsgränsen" [S16].
  - Staff complaints cover insufficient travel time between visits and no continuity [L].
- Satisfaction with hemtjänst was 85% in 2025, but in 11 municipalities it was 75% or lower [S12].
- Tension: continuity rules (fast omsorgskontakt), trust-based models replacing minute rules, and language and competence requirements together create a hard rostering-and-compliance problem. Incumbent tools (Timecare, IntraPhone, municipal journal systems) handle it only partly [L, S17].

**Tech adoption**
- No sector-specific SCB AI data for care [GAP].
- Incumbent scheduling vendors are named in municipal documents (Timecare/RLDatix, IntraPhone) [L].

**Barriers**
- Municipal procurement, integration with journal systems, and GDPR/patient-data rules (the patient data act).
- Selling to *private* providers lowers these barriers.

**Recurring revenue:** high, per caregiver per month.

**Candidate opportunities**
1. **Continuity-aware hemtjänst planning for private LOV providers and small municipalities.** It would optimise routes, protect travel time, track continuity (fast omsorgskontakt) and log language-requirement compliance. Evidence: S16, the 2026 continuity amendment, and the 341 private hemtjänst firms with 20+ staff.
2. **"Trust-based model" transition kit.** Analytics that let a municipality drop minute-based scheduling while keeping budget control (time banks, outcome logging). Evidence: Kommunal's negotiations in 100 municipalities [S16] and Norrköping's 2026 proposal [L].
3. **IVO/SoL documentation and deviation-reporting assistant for small care providers.** Covers documentation under SoL 2025:400 and the expanded IVO reporting duty [L, S18, S51].

**Score: 6/10.**
- For: clear pain, a reachable private-provider list, and recurring revenue.
- Against: thin provider margins (5.6% median), a municipal sales cycle, entrenched journal/HR vendors, and political LOV risk.

---

### Sector 2 – Construction & property management (incl. BRF, renovations, stambyten, inspections)

**Market size**
- Byggföretagen (Oct 2026) [S22]:
  - Construction investment rises **6% over 2026–2027** to ≈**690 bn SEK in 2027**, back to the 2023 level.
  - Housing starts: 29,500 in 2025 and 31,700 forecast for 2027.
  - Sector employment +10,600, to ≈377,600.
- SCB turnover 2024 [S2]:
  - Specialised contractors (43): 570 bn SEK.
  - Building contractors (41): 367.6 bn, down from 419.1 bn in 2022.
  - VVS (43.22): 111.2 bn, up 18% from 2022.
  - Commissioned property management (68.32): 54.2 bn, up 9.5% from 2022.

**Buyers**
- BRFs: "cirka 29 000 bostadsrättsföreningar som äger sina hus", plus a few thousand not yet owning their buildings [L, S24]. "~30 000" is also commonly cited [L].
- Large BRF administrators:
  - SBC: 4,600 customers, 640 MSEK turnover in 2024 [L, S27].
  - Nabo: ~2,700 BRFs [L, S28].
  - Riksbyggen: 4,384 BRFs at end-2019 [L].
  - HSB's barometer covers 4,274 BRFs [L, S25].
- Property firms (SNI 68): 121,575, of which **13,829 with employees**. Commissioned property managers (68.32): 1,105 with employees [S1].
- Installers with employees: electrical (43.21) 5,717; VVS (43.22) 5,105; other building installation (43.29, which includes lifts and ventilation) 1,026 [S1].
- Technical testing and inspection (71.20): 1,357 firms, 521 with employees; 2024 turnover 16.1 bn, **+31% vs 2022** [S1, S2].

**Fragmentation:** very high. 91,033 specialised contracting firms, only 2,191 with 20+ staff [S1].

**Failures and exits**
- 1,933 construction bankruptcies in 2025 (−5% y/y); 9 in 10 had fewer than 10 employees; Stockholm accounts for 41% [S19].
- UC (July 2026) lists construction and real estate among the most bankruptcy-hit industries [L, S21 context].

**Margins (median 2024)** [S3]
- 68.32 property management: 10.6%.
- Testing/inspection (71.20): 13.6%.
- Technical consultants (71.12): 16.9%.
- VVS: 5.5%.

**Regulation**
- EPBD: Boverket's proposal (Feb 2026) adds no general retroactive requirements for residential buildings, but energy classes are re-based. The weight is expected to shift towards class D, and in some cases C, when a new energy declaration is made [S23].
- The national building renovation plan is due to the EU by 31 Dec 2026 [L].
- ~31,000 non-residential buildings need measures by 2033 [L]. Not confirmed by S23.
- OVK (mandatory ventilation inspection) and SBA (systematic fire-safety work, required by law 2003:778 [L]) are ongoing statutory obligations. The 3/6-year OVK intervals are training knowledge, not re-verified.
- Boverket's 2023 pre-study on digitalising OVK points to missing national OVK data [L].

**Stambyten**
- 250–500k SEK per apartment; relining 75–150k [L, S29].
- BRF maintenance plans must cover 50 years [L].

**BRF finances and dissatisfaction**
- 31% of BRF owners are worried about their association's finances, up 15 points since 2022. 50% are worried about fee increases [S26].
- Nabo: 26% of its BRFs raised fees, by 6.7% on average [L].
- Boards are volunteer and rotating. Low financial literacy is reported: "Trots miljoninvesteringar är kunskapen om bostadsrättsföreningens ekonomi liten" (SBAB, Apr 2025) [L].

**Tech adoption:** construction is the lowest AI adopter. Only **15%** of construction firms with 10+ employees used AI in 2025 (3% in 2023). Real estate was 56% [S4].

**Acquisition channels**
- BRF boards: through administrators (SBC, Nabo, HSB, Riksbyggen), the members' association (Bostadsrätterna, ~7,500 member BRFs [L]), and local SEO.
- Commercial owners: through Fastighetsägarna.

**Recurring revenue:** high for administration and compliance SaaS; project-based for renovation.

**Candidate opportunities**
1. **BRF compliance and maintenance-plan copilot.** One calendar for OVK, SBA, energy declaration (re-classing under EPBD), lift inspection, stambyte planning and 50-year plan updates. Sold via administrators or directly to ~29–30k boards. Evidence: S23, S24, S26.
2. **Stambyte/renovation procurement adviser for BRFs.** A fixed-fee service plus software: condition survey → tender documents → contractor comparison → member communication. Evidence: S29 cost levels and S26 owner anxiety about fees.
3. **OVK/SBA inspection field app with structured reports.** Sold to the 521 inspection firms with employees (71.20) and to municipalities that enforce OVK supervision. The market is growing fast (+31% turnover 2022–24 [S2]).
4. **EPBD energy-class impact screening.** Bulk analysis of energy declarations for property owners ahead of re-classing [S23].

**Score: 7/10.**
- For: huge, fragmented buyer base; statutory recurring obligations; weak digitalisation; volunteer boards with a real pain.
- Against: administrators (SBC/HSB/Riksbyggen) may bundle similar features, and BRF willingness to pay is low per unit.

---

### Sector 3 – Logistics & transportation

**Market size:** ~56,000 firms, ~325,000 employees, "drygt 1 500 miljarder" turnover a year [S43]. The figure is undated; reliability M.

**Buyers** [S1]
- Haulage (49.41): 14,943 firms, **7,488 with employees**, 751 with 20+.
- Warehousing and transport services (52): 1,772 with employees.
- Post and courier (53): 187 with employees.

**Turnover** [S2]
- Haulage: 144.0 bn SEK in 2024, down from 150.1 bn in 2022 (−4%).
- Warehousing: 222.3 bn (flat).

**Failures:** haulage firms had the **largest increase in bankruptcies in 2025, +18%** [S20].

**Margins (median 2024)** [S3]: haulage 6.5% (IQR 0.4–15.1%); warehousing 4.7%.

**Tech adoption:** only **12%** of transport firms with 10+ employees used AI in 2025 (5% in 2023). That is the lowest of the measured sectors after construction [S4].

**Regulation:** [GAP]. Not verified this pass: EU Mobility Package enforcement, smart tachograph v2, and the driver competence (YKB) rules.

**Pain points:** [GAP] for documented dissatisfaction. Transportföretagen lists "Tillgång till kompetens" as a priority issue [S43].

**Candidate opportunities (lower evidence)**
1. **Back-office copilot for small hauliers.** Covers invoicing, fuel/toll reconciliation and driver-hours compliance. It targets 7,488 firms with employees, where distress is rising (+18% bankruptcies) [S20].
2. **Defence/preparedness logistics readiness.** Helps private transport firms take on preparedness obligations (see Sector 7) [GAP].

**Score: 4/10.**
- For: many buyers.
- Against: falling turnover, rising distress, low willingness to pay, crowded TMS/fleet-telematics vendors, and thin evidence this pass.

---

### Sector 4 – Manufacturing & industrial automation

**Market size (2024 turnover)** [S2]
- Machinery n.e.c. (28): 420.7 bn SEK.
- Motor vehicles (29): 722.2 bn.
- Metal products (25): 196.1 bn.
- Electrical equipment (27): 126.9 bn, up 47% from 2022.
- Repair and installation of machinery (33): 45.6 bn, up 22% from 2022.
- Lifting and handling equipment (28.22): 60.0 bn.

**Buyers:** 55,623 manufacturing firms, **19,264 with employees**, 3,557 with 20+, 792 with 100+ [S1]. Installation of industrial machinery (33.2) grew from 782 to 1,824 firms between 2020 and 2025, though only 325 have employees [S1].

**Margins (median 2024)** [S3]: machinery 6.9%; metal products 5.8%; repair/installation 8.3%.

**Tech adoption**
- AI: 33% of manufacturers with 10+ employees used AI in 2025, up from 7% in 2023 [S4].
- Robots: about **29%** of manufacturers with 10+ employees used at least one robot in 2022 (derived: 18% <5 robots + 6% 5–10 + 5% >10) [S6].
- IT-security policy documents: 52% of manufacturers with 10+ employees in 2024 [S5].

**Regulation:** EU Machinery Regulation 2023/1230 (applies from Jan 2027; training knowledge) and NIS2 for manufacturers in covered categories ≥50 staff [S39].

**Barriers:** domain expertise, integration with PLC/ERP, long sales cycles.

**Candidate opportunities**
1. **Machinery Regulation / CE technical-file automation for SME machine builders and integrators.** Targets the ~1,500 machinery-industry firms with employees, the 2,686 repair/installation firms (33) with employees, and the integrators in 33.2 [S1].
2. **NIS2 "manufacturing edition" compliance kit** for ≥50-employee manufacturers (see Sector 6).

**Score: 5/10.** A solid buyer base and strong AI-adoption momentum, but industrial sales are slow and incumbents (Siemens, ABB, the ERP vendors) are strong. The regulatory hook (Machinery Regulation) is promising but not verified in depth.

---

### Sector 5 – Energy & grid infrastructure (grid connection, solar/battery, heat pumps, effekttariffer)

**Grid structure**
- **168 grid companies**: 147 local-grid, 25 regional, 2 transmission or interconnector only [S31].
- The top three (E.ON, Ellevio, Vattenfall) have ~52% of customers.
- About 70 others have more than 10,000 customers each, together 32% of customers.
- The rest have fewer than 10,000 customers, together 6% of customers.
- Mean ≈38,500 and median ≈11,200 metering points per company [S31].
- Electricity distribution (35.13) turnover: 69.2 bn SEK in 2024; median operating margin 16.6% [S2, S3].

**Investment need**
- ≈945 bn SEK of grid investment needed to 2045 [L, S46].
- Svenska kraftnät's investment frame is 14.6 bn, rising to 25 bn a year by 2029 [L, riksdag interpellation].

**Connection queues**
- In Sept 2025 the government tasked Svk with reviewing the connection process; final report due 30 Apr 2026 [L, S37].
- Svk's queue reportedly exceeded **175 GW** of requested feed-in [L, S35]. The source is a third-party wiki citing Svk's grid development plan 2026–2035, so verify before use.
- Battery storage:
  - Capacity grew from ~80 MW to 610 MW in 2024.
  - Some grid companies have long queues and have refused battery connections.
  - Grid companies use flexibility tools only to a very limited extent [S34].
  - County boards approved 130 large battery parks (>5 GW) in 2021–2025 [L, S36].
- Kraftlyftet support: 200 MSEK in 2026, 400 MSEK a year from 2027 [L, S47].

**Effekttariffer (capacity tariffs)**
- Ei's 2022 rule that all grid companies introduce capacity charges by 1 Jan 2027 was **stopped on 13 Mar 2026**. Ei must repeal it by 30 Jun 2026 and propose a new model by 12 Apr 2027. Meanwhile the charges are voluntary [S30].
- About 13% of households had a capacity charge in spring 2025 [L].
- Most grid companies had not introduced one [S31].

**Solar**
- 652 MW installed in 2025, against 848 MW in 2024 [S32].
- 21,600 new grid-connected plants in 2025; ~314,600 in total; ~5.5 GW [S32].
- **196 solar-installer bankruptcies in 2025 (+33%)** [L, S33]. Drivers: tax-reduction changes, and the green-tech deduction cut from 20% to 15% in Jul 2025 [L].

**Installers:** 12,376 electrical installation firms (5,717 with employees, 440 with 20+); median operating margin 6.2% [S1, S3].

**Heat pumps:** [GAP]. Not verified this pass (SKVP sales statistics).

**Tech adoption:** 44% of energy and recycling firms with 10+ employees used AI in 2025 [S4].

**Painful manual workflows (evidence-based)**
- Connection applications, capacity assessments and queue management at 147 local-grid companies, many of them small (median ~11k customers) [S31, S34].
- Tariff redesign: companies that "lagt ned" (invested) work in capacity tariffs must now pause, adjust or continue during policy limbo [S31].

**Candidate opportunities**
1. **Grid-connection case management and capacity pre-check for small and medium DSOs.** Software, or software plus consulting. Buyers: ~140 sub-scale grid companies [S31]. Pain: queue backlogs and the battery/flex connection debate [S34, S37].
2. **Independent grid-connection consultancy for C&I customers, BESS developers and housing.** Prepares complete applications, flexible-connection options and tariff optimisation. Hook: Svk's queue reform and allocation system from 2027 [L, S35].
3. **Tariff-design simulation tool for DSOs** ahead of Ei's new-model proposal (due 12 Apr 2027) [S30].
4. **Distressed solar-installer roll-up or aftercare platform.** Service contracts for orphaned PV and battery owners whose installer went bankrupt (196 bankruptcies in 2025) [L, S33]. ~314,600 plants [S32].

**Score: 7/10.**
- For: concrete regulatory churn with deadlines, a niche B2B buyer set (168 DSOs) that a small team can map completely, and high recurring potential.
- Against: DSO sales cycles and incumbent utility-IT vendors (not verified), plus policy volatility, since the capacity-tariff mandate was reversed.

---

### Sector 6 – Cybersecurity

**Regulation (primary)**
- **Cybersäkerhetslagen** (NIS2) entered into force on **15 January 2026** [S39].
- The government estimates "drygt 1 500 företag i Sverige med sammanlagt runt 500 000 sysselsatta" could be affected. The estimate counts firms with ≥50 employees. Some actors are covered regardless of size [S39].
- Size threshold for private entities: ≥50 employees or >10 M EUR turnover [S39].
- Sanctions for essential entities: up to the higher of 2% of global turnover or 10 M EUR [S39].
- **CER-based law** for critical entities' resilience was proposed on 14 Jul 2026 for **1 Jan 2027** [S40].
- DORA applies to financial firms. FI's 2026 priority is operational IT resilience, including against cyberattacks [S45].

**Readiness gap (SCB)** [S5]
- Firms with written IT-security policy documents (2024): 10–49 employees **40%**; 50–249: 69%; 250+: 91%; 0–9: **9%**.
- By sector (10+ employees): construction 40%, transport 42%, manufacturing 52%, real estate 65%, energy 79%.

**Market size and suppliers:** [GAP] (no verified Swedish cybersecurity market figure this pass).

**Barriers:** trust and credentials, plus a crowded MSSP and consulting field. Security clearance is needed for some public work.

**Candidate opportunities**
1. **NIS2/CER compliance-as-a-service for mid-sized covered entities (50–249 employees).** Covers the policy pack, supplier-risk register, incident-reporting runbooks and board training. Evidence: 69% versus 91% policy coverage by size [S5]; the CER law from 2027 [S40].
2. **Supply-chain security attestation for SMEs that sell to NIS2 entities.** Covered entities must manage supplier risk, which pushes requirements down to the 10–49-employee tier, where only 40% have policies [S5].

**Score: 6/10.**
- For: a strong regulatory tailwind in force now, with a second law in 2027.
- Against: a crowded field, a fuzzy market size, and buyers who may default to large consultancies. The best fit is a vertical focus (e.g. water, energy, municipalities).

---

### Sector 7 – Defence & civil preparedness

**Budget (Prop. 2025/26:1, Utgiftsområde 6, 22 Sep 2025)** [S38]
- UO6 total, MSEK: 2024 outturn 128,177; 2025 budget 168,818; 2026 proposed **225,022**; 2027 estimated 234,025; 2028 estimated 207,201.
  - Column reading follows the standard budget-table layout (derived).
  - The totals include military support to Ukraine of ≈40 bn SEK a year for 2025–2027.
- Target: defence spending **3.5% of GDP by 2030** (NATO accounting). Reaching it requires a further ~30 bn SEK in 2030.
- Loan-financed top-ups are capped at 300 bn SEK. Of this, at most **50 bn may go to physical infrastructure and stockpiles of food, medicines and fuel** (civil defence).
- Materiel and facility procurement: ~52.1 bn SEK in 2024. Försvarsmakten was authorised to order materiel for 128 bn SEK in 2024.
- Civil defence: up to **15 bn SEK a year from 2028** was announced in the 2025 budget.
- Delivery delays are largely attributed to "utmaningar inom försvarsindustrin" (challenges in the defence industry) [S38].

**Supplier base**
- Weapons and ammunition (25.4): 53 firms, only 12 with employees; turnover 13.8 bn SEK in 2024, up 52% from 2022; 3,603 employees, up from 2,733 [S1, S2].
- Military vehicles (30.4): 1–2 firms [S1].
- Security and guarding (80): 1,121 firms, 535 with employees, 139 with 20+ (91 in 2020); turnover 32.2 bn in 2024 [S1, S2].
- Säkerhetsföretagen: ~200 member companies and ~30,000 employees. It is calling for state funding for training and staffing in total defence, and a civil-duty (civilplikt) model for guarding is under analysis by the Police [S44].

**SME access:** [GAP] (no verified FMV SME-share figure; FMV pages returned 403).

**Procurement:** FMV handles most military procurement. It is security-classified, with long cycles and framework agreements. Civil preparedness buying is spread across municipalities, regions and businesses.

**Candidate opportunities**
1. **Civil-preparedness (civilt försvar) planning software for municipalities and essential private firms.** Covers continuity planning, stockpile tracking, staff war-placement (krigsplacering) and exercise logs. Evidence: 50 bn SEK for infrastructure and stockpiles, 15 bn a year from 2028 [S38], and the call for joint planning [S44].
2. **Defence-supplier onboarding and compliance service for SME subcontractors.** Covers security-protection agreements, export-control classification and quality certification, for firms entering a supply chain growing ~50% in two years [S2, S38].
3. **Training and exercise management for private security firms** under a civilplikt model [S44].

**Score: 6/10.** The fastest-growing public budget in Sweden, with explicit money for civil preparedness. Security clearance, FMV cycles and the founders' credibility are real barriers. Civil preparedness (municipal and private) is the more accessible entry point.

---

### Sector 8 – Financial services & fintech

**Buyers** [S1]
- Banks and credit institutions (64): 24,662 firms (many holding entities), 2,766 with employees.
- Financial auxiliaries (66): 5,386 firms, 2,000 with employees.

**Regulator priorities 2026 (FI)** [S45]: (1) stability and operational IT resilience, including against cyberattacks; (2) AML and fraud; (3) suitable consumer products, credit assessment and debt collection. FI supports becoming the AI Act market-surveillance authority for finance (SOU 2025:101).

**Market size, growth, failures:** [GAP] this pass.

**Assessment:** a crowded, capital-intensive and licensed space with strong Nordic incumbents (Klarna, Tink, Trustly and the banks; training knowledge). The niche angle is compliance tooling, such as DORA register-of-information or AML for small institutions, which overlaps with Sectors 6 and 10.

**Score: 3/10.** High barriers (licensing, capital, trust), crowded, and the evidence this pass is thin.

---

### Sector 9 – Accounting, bookkeeping & tax  (top-ranked sector)

**Market size**
- Spiris (Visma) Branschrapport 2025 [S7], all estimates:
  - Total ≈ **61 bn SEK**: accounting 25 bn, audit 18 bn, tax/advisory/other 13 bn, plus software ≈5 bn.
  - ≈**25,000 firms** and ≈**62,000 people**.
  - Scenario: the market grows from 53 bn (2023) to 69 bn (2030), with 15–20% price increases.
- SCB [S2]: SNI 69.20 (accounting, audit, tax) turnover **64.8 bn SEK in 2024**, against 55.6 bn in 2022 (+16.6%); 37,356 employees.

**Number of firms and fragmentation**
- SCB FDB 2025 [S1], SNI 69.201 (accounting and bookkeeping firms):
  - **23,921 firms** (21,707 in 2020).
  - **8,126 with employees**.
  - Only **114 with 20+ employees**, and 13 with 100+.
  - Audit firms (69.202): 1,483 firms, 672 with employees. Tax-advisory firms (69.203): 444.
- Spiris breakdown [S7]:
  - Limited-company accounting firms with fewer than 10 employees: **14,217 firms, 15.7 bn SEK**.
  - Those with 10 or more employees: 234 firms, 9.4 bn.
  - Sole traders and partnerships: 8,916.
  - "Cirka 62% av all redovisning utförs av byråer (AB) med färre än 10 anställda."
- Authorisation [S7]:
  - About 4,200 authorised accounting consultants working at 1,900 firms; 1,300 of those firms have exactly one.
  - About 25,000 actors offer accounting with no authorisation requirement.
  - 12,888 accounting businesses were registered in Bolagsverket's AML register in 2024.
- Srf's annual report: authorised accounting consultants (ARK) rose 2,663 → 2,716 and authorised payroll consultants (ALK) 776 → 806 [L, S11].

**Succession and demographics**
- "Stora pensionsavgångar de kommande 5–10 åren, speciellt bland små byråer" (large retirements over the next 5–10 years, especially at small firms).
- Average founder age of one-person firms started since 2020 is **64** [S7].

**Consolidation and PE**
- PE-owned Cedra bought 26 EY offices (≈400 staff, ≈500 MSEK), reaching ≈1.5 bn SEK of Swedish turnover.
- Azets took over parts of KPMG's SME practice (270 staff, 14 partners), reaching ≈1 bn SEK.
- EQT bought Fortnox for 55 bn SEK; the deal closed June 2025 [S7].
- Acquired firms typically have lower prices than their acquirers, so acquirers raise prices after purchase [S7].

**Margins and economics**
- SCB median operating margin (69.201) in 2024: **16.7%** (IQR 2.8–37.5%) [S3].
- Salaries rose 10–12% over 2021–2024, roughly in line with prices, so gross margins held but did not improve [S7].
- Utilisation is about 82–83% for authorised consultants, 76–79% for assistants. Spiris suggests that with hourly billing "taket [kan] vara nått" (the ceiling may have been reached) [S7].
- "Vissa bedömare anser att det finns utrymme för en prisökning på 20–30%" (some estimate room for a 20–30% price increase) on the ~16 bn small-firm market [S7].

**Fortnox pricing changes (documented dissatisfaction)**
- Autumn 2025: the byrålicens (firm licence) went up **+200 SEK per consultant per month**, bundling Bokslut and Skatt, and firms cannot opt out of modules. Many firms are considering switching supplier [S8, 2026-04-10].
- Apr 2026: the new mandatory **"Access"** service costs end clients **9–199 SEK per month** by voucher volume. Firms reacted with "hård kritik" (sharp criticism). Fortnox acknowledged a risk of customer loss [S10].
- Firms object to partner fees and say they are becoming "en betydelselös mellanhand" (an insignificant middleman), as Fortnox serves their clients directly. Switching is seen as hard for lack of competition [S9].
- Fortnox was delisted in July 2025 after EQT's acquisition [S10].
- Vendor concentration: Fortnox targeted 12,000+ accounting-firm customers in 2025 [L].

**Tech adoption**
- EDI is only ~20–30% of Swedish B2B invoices, against 70–90% elsewhere in the Nordics [S7].
- Some firms still run 1990s locally installed software [S7].

**Regulation:** AML registration and county-board supervision [S7]. The accounting title is unprotected, and state authorisation is debated [S7].

**Acquisition channels**
- Srf konsulterna and FAR events, Balans/FAR Online, Fortnox and Visma partner ecosystems, LinkedIn, and local networks.
- Firm owners are reachable, and SCB/Bolagsverket lists allow full enumeration.

**Recurring revenue:** very high, priced per seat or per client company per month.

**Barriers:** low. Integration with Fortnox, Visma/Spiris and BL is needed, and Fortnox may restrict access (the partner/Access changes). That is a platform risk.

**Candidate opportunities**
1. **Succession marketplace and valuation service for small accounting firms.** Matches retiring owners (founder average age 64) with acquirers. Offers valuation, client-portfolio transfer and engagement-letter migration. Monetised by success fees. Buyers: ~14,200 small limited-company firms plus ~8,900 sole traders and partnerships, and PE-backed acquirers (Cedra, Azets) that need deal flow [S7, S1].
2. **Platform-neutral "practice OS" for small firms.** Workflow, deadlines, client portal, AML know-your-customer and price-list management on top of Fortnox, Spiris or other ledgers. Evidence: Fortnox licence and Access backlash and a desire to switch [S8, S9, S10]; utilisation ceilings and the case for fixed-price packaging [S7].
3. **AI "digital junior" for categorisation, reconciliation and year-end prep, sold per client file.** Addresses the staff shortage and wage inflation (salaries +10–12%) [S7].
4. **AML/KYC compliance kit for small accounting firms.** 12,888 registered businesses face county-board supervision [S7].

**Score: 8/10.**
- For: the largest number of reachable, identifiable small B2B buyers in this screen (8,126 employer firms). Documented, current, specific anger at the dominant supplier. A demographic succession wave. PE consolidators as a second customer type. Low capital needs and high recurring revenue.
- Against: platform dependence on Fortnox/Spiris APIs and low per-firm budgets.

---

### Sector 10 – Legal & regulatory compliance

**Market size:** legal firms (69.10) had **38.9 bn SEK** turnover in 2024, against 33.3 bn in 2022 (+17%); 13,446 employees; 6,965 enterprises [S2].

**Buyers and fragmentation:** 7,397 law-firm enterprises in 2025, 3,120 with employees, **only 105 with 20+** and 18 with 100+ [S1].

**Margins:** median operating margin **21.7%** in 2024, the highest in this screen [S3].

**Advokatsamfundet statistics:** [GAP]. The site returned HTTP 503 on two attempts.

**Compliance demand created by other sectors:** NIS2 from 15 Jan 2026 [S39], CER law from 1 Jan 2027 (proposed) [S40], DORA and FI priorities [S45], the AI Act (FI as surveillance authority) [S45], SoL 2025:400 in care [L], and EPBD in property [S23].

**Candidate opportunities**
1. **Regulatory-change monitoring and obligations register for mid-sized organisations.** Maps NIS2, CER, AI Act and sector rules to tasks. It overlaps with Sector 6, sold through law firms as a white-label offering.
2. **Practice-management and AI drafting for the 3,000 small law firms**, which have high margins and therefore budget [S1, S3]. Competition from Nordic legal-tech vendors is not verified [GAP].

**Score: 6/10.** Small firms with high margins and reachable buyers, but trust barriers and an unverified competitive landscape this pass.

---

### Sector 20 – IT infrastructure / cloud / data centres

**Market size:** data processing and hosting (63.11) had 2024 turnover of **145.1 bn SEK**, against 100.6 bn in 2022 (+44%), but only 6,476 employees [S2]. This points to capital-intensive hyperscaler and colocation activity (interpretation).

**Buyers:** 3,311 firms in 63.1, of which 910 have employees and 97 have 20+ [S1]. Software and IT consultancies (62): 48,616 firms, 18,805 with employees [S1].

**Margins:** 63.11 median 5.5%, with a wide spread (IQR −14.1% to 28.8%). Software and IT consultancies (62): 18.1% [S3].

**Regulation:** under the EED, data centres with ≥500 kW of installed IT power must publish energy information annually. Those ≥1 MW are encouraged to follow the EU Code of Conduct [S41].

**Tech adoption:** the ICT sector has the highest AI adoption, at **88%** of firms with 10+ employees in 2025 [S4].

**Gaps:** data-centre pipeline in MW, grid constraints for data centres, and power-price data [GAP].

**Candidate opportunity:** EED energy-reporting and PUE/heat-reuse compliance tooling for mid-size Swedish data centres and server rooms ≥500 kW [S41]. A small, niche buyer base.

**Score: 4/10.** Large and growing, but dominated by capital-intensive hyperscalers. The mid-market niche is narrow.

---

### Sector 25 – Robotics & specialised hardware

**Adoption**
- About 29% of manufacturers with 10+ employees used robots in 2022 (derived) [S6].
- Across all sectors, firms with 10+ employees: 4% use fewer than 5 robots, 1% use 5–10, and 1% use more than 10 [S6].
- Robot use is concentrated in large firms: 31% of firms with 250+ employees (derived: 10+9+12) [S6].

**Suppliers:** lifting and handling equipment (28.22) had 60.0 bn turnover in 2024 (+29% vs 2022) [S2]. Global OEMs dominate (training knowledge).

**Gaps:** robot density, market size and integrator count [GAP].

**Candidate opportunity:** robot-as-a-service or retrofit cells for SME metal-products firms (25: 8,467 firms with turnover data, 196 bn SEK) [S2], where adoption is low. This is hardware-capital intensive.

**Score: 3/10.** Capital needs, long cycles and global competition make it a poor fit for a 2–4 person team without hardware pedigree.

---

### Water & sewer (VA) infrastructure

**Investment need**
- **590 bn SEK to 2040 (≈37 bn a year)**. Investment rose from ~15 bn (2019) to ~31.5 bn (2025) [S42].
- ~70% of the need is renewal and replacement of existing infrastructure. The rest is driven by climate adaptation, environmental rules, security/preparedness and growth [S42].
- Average VA-taxa increase in 2026: **+7.5% (single-family houses)** and +7.2% (multi-family) [S42].
- Svenskt Vatten asks for a state financing inquiry [S42].

**Buyers:** 290 municipalities and municipal VA companies. SNI 36 (water works): 396 enterprises, 62 with employees. SNI 37 (sewage): 337, 172 with employees [S1].

**Turnover (2024)** [S2]: water supply 12.65 bn SEK (8.25 bn in 2022); sewage 12.15 bn (9.0 bn in 2022). This covers only the corporatised part of the sector.

**Margins:** water supply 3.2% median; sewage 6.3% [S3]. These are municipal cost-recovery entities.

**Regulation:** CER law (critical entities, water included) proposed for 1 Jan 2027, with consultation input from Sydvatten [S40]. NIS2 covers water [S39]. The recast EU Urban Waste Water Treatment Directive is not verified [GAP].

**Painful workflows (inferred, not documented):** asset-condition data, renewal-plan prioritisation and taxa justification to councils [GAP for direct evidence].

**Candidate opportunities**
1. **Renewal-planning and taxa-justification analytics for small and mid-size municipal VA organisations.** Links pipe-condition data to the 37 bn a year need and to council taxa decisions [S42].
2. **CER/NIS2 resilience compliance pack specialised for VA.** Covers background checks, risk assessment and incident reporting [S39, S40].

**Score: 5/10.** A large, regulation-forced and non-cyclical need, but municipal procurement is slow, buyers are few (~290), and engineering consultancies (Sweco, WSP, Tyréns; training knowledge) are strong.

---

## 3. Candidate opportunities: consolidated list (ranked by preliminary fit for a 2–4 person team)

| Rank | Opportunity | Sector | Buyer count (evidence) | Why now (evidence) | Revenue model | Key risk |
|---|---|---|---|---|---|---|
| 1 | Platform-neutral practice OS and AI "digital junior" for small accounting firms | 9 | 8,126 accounting firms with employees; 14,217 small ABs [S1, S7] | Fortnox +200 SEK/consultant/month and mandatory Access fee (9–199 SEK) caused backlash, Apr 2026 [S8–S10]; wages +10–12% [S7] | SaaS per seat or per client | Fortnox API and partner terms |
| 2 | Accounting-firm succession and M&A marketplace and valuation | 9 | ~23k firms; founder average age 64 among recent solo firms [S1, S7] | PE roll-ups (Cedra, Azets) [S7] | Success fees plus subscription | Deal-flow cyclicality; brokers |
| 3 | BRF compliance and maintenance-plan copilot (OVK, SBA, energy declaration/EPBD, lift, stambyte) | 2 | ~29–30k BRFs [L, S24]; 1,105 managers [S1] | EPBD re-classing [S23]; owner anxiety 31% [S26] | SaaS per BRF; via administrators | Administrators bundling; low willingness to pay |
| 4 | Grid-connection case management for small DSOs, plus a connection consultancy for C&I and BESS | 5 | 168 DSOs, ~140 sub-scale [S31] | Queue reform and allocation system (2027) [L, S35, S37]; battery connection denials [S34] | SaaS per DSO plus consulting | Utility-IT incumbents; policy shifts |
| 5 | Continuity-aware hemtjänst scheduling for private LOV providers | 1 | 341 hemtjänst firms with 20+ staff [S1]; ~180 LOV municipalities [S12] | Fast omsorgskontakt [L]; minute-scheduling conflict in 100 municipalities [S16] | SaaS per caregiver | Thin provider margins; LOV policy risk |
| 6 | NIS2/CER compliance-as-a-service for 50–249-employee entities (vertical: water, energy, municipal companies) | 6/10/VA | ~1,500+ firms ≥50 staff [S39] | In force 15 Jan 2026; CER 1 Jan 2027 [S39, S40]; 69% policy coverage [S5] | Subscription plus onboarding | Crowded consultancies |
| 7 | Civil-preparedness planning software (municipalities and essential firms) | 7 | 290 municipalities, 21 regions, essential firms | 50 bn civil-defence top-up; 15 bn a year from 2028 [S38] | SaaS per organisation | Public procurement speed |
| 8 | Stambyte/renovation procurement adviser for BRFs | 2 | ~29–30k BRFs [L] | 250–500k SEK per apartment [L, S29] | Fixed fee plus software | Project lumpiness |
| 9 | Orphaned-PV/battery aftercare network (post-bankruptcy service) | 5 | ~314,600 PV plants [S32] | 196 installer bankruptcies in 2025 [L, S33] | Service contracts | Field-service ops intensity |
| 10 | OVK/SBA inspection field app for inspection firms | 2 | 521 testing/inspection firms with employees [S1] | 71.20 turnover +31% 2022–24 [S2] | SaaS per inspector | Niche size |
| 11 | Machinery Regulation / CE technical-file automation | 4 | ~1,500 machinery firms with employees; integrators [S1] | Regulation applies from 2027 (training knowledge) | SaaS per project | Unverified demand |
| 12 | VA renewal and taxa-justification analytics | VA | 290 municipalities [S42] | 590 bn need; +7.5% taxa [S42] | SaaS per municipality | Slow procurement |

---

## 4. Cross-cutting observations

- **AI-adoption gap as a wedge.** Share of firms with 10+ employees using AI in 2025 [S4]:
  - construction 15%, transport 12%, manufacturing 33%, energy 44%, real estate 56%, ICT 88%;
  - all firms with 10+ employees 35%; firms with 0–9 employees 17%.
  - The lowest adopters (construction, transport) also have the thinnest margins. The best mix of low adoption and ability to pay is in the professional services (69.201 at 16.7% and 69.10 at 21.7% median margin) and in property management.
- **Regulation-forced demand with dated deadlines (2026–2028):**
  - NIS2: 15 Jan 2026.
  - Language requirement in eldercare: 1 Jul 2026 [L].
  - Ei's tariff rules repealed by 30 Jun 2026; new model due 12 Apr 2027.
  - EPBD renovation plan to the EU by 31 Dec 2026 [L].
  - CER law: 1 Jan 2027 (proposed).
  - Svk allocation system: 2027 [L].
  - Defence spending at 3.5% of GDP by 2030.
- **Distress signals:**
  - Aktiebolag bankruptcies: 10,158 in 2025, flat against the 2024 record [S20].
  - Jan–Sep 2026: 6,910, down 6%; but September 2026 was the highest September since 1994 [S21].
  - Haulage +18% (2025) [S20]; solar installers +33% [L]; construction 1,933 (−5%) [S19].
  - Distressed sectors are poor SaaS buyers but good roll-up or aftercare targets.

## 5. Open gaps to close in a follow-up pass

- Heat-pump market (SKVP sales statistics).
- Ei's connection-time statistics.
- Svk queue figures from the primary source.
- Swedish cybersecurity market size.
- Advokatsamfundet member and firm statistics.
- FMV SME share and supplier count.
- Data-centre MW pipeline.
- Robot density (IFR).
- Logistics regulation (Mobility Package, tachographs).
- Lift-inspection rules and market; OVK non-compliance rates.
- Official count of bostadsrättsföreningar (Bolagsverket).
- SNI-level bankruptcy data (Tillväxtanalys or SCB).
- Socialstyrelsen's primary report on minute-based scheduling.
- Fortnox churn data.

---

## 6. Source Ledger

Retrieval date for all sources: **2026-10-29**. Reliability: H = primary fetched; M = secondary fetched; L = search snippet only (unverified lead).

| ID | URL | Publisher | Title | Pub date | Retrieval | Finding | Reliability |
|---|---|---|---|---|---|---|---|
| S1 | https://api.scb.se/OV0104/v1/doris/sv/ssd/NV/NV0101/FDBR07N | SCB | Företag (FDB) efter näringsgren SNI2007 och storleksklass, 2008–2025 | 2025-12-02 (table update) | 2026-10-29 | Firm counts by SNI and size class (e.g. 69.201: 23,921 firms, 8,126 with employees, 114 with 20+; 88.101: 435 with employees; 49.41: 7,488 with employees) | H |
| S2 | https://api.scb.se/OV0104/v1/doris/sv/ssd/NV/NV0109/NV0109P/NSEBasfaktaFEngs07 | SCB | Företagens ekonomi: basfakta efter SNI 2007, 2022–2024 | 2022–2024 data (published 2025/26) | 2026-10-29 | Turnover, employees and value added by SNI (e.g. 69.20 64.8 bn; 63.11 145.1 bn; 25.4 13.8 bn) | H |
| S3 | https://api.scb.se/OV0104/v1/doris/sv/ssd/NV/NV0109/NV0109O/BNTT01 | SCB | Branschnyckeltal efter SNI 2007, storleksklass och kvartil, 2008–2024 | 2024 data | 2026-10-29 | Operating-margin quartiles 2024 (e.g. 69.201 median 16.7%; 88.101 5.6%; 69.10 21.7%) | H |
| S4 | https://api.scb.se/OV0104/v1/doris/sv/ssd/NV/NV0116/NV0116M/AiTeknikerTypN | SCB | Användning av AI-tekniker efter typ, andel företag, 2021–2025 | 2025 data | 2026-10-29 | AI use, firms with 10+ employees: 35% overall; construction 15%; transport 12%; ICT 88% | H |
| S5 | https://api.scb.se/OV0104/v1/doris/sv/ssd/NV/NV0116/NV0116S/StyrdokumentSakerhN | SCB | Har styrande dokument för informationssäkerhet, andel företag, 2019–2024 | 2024 data | 2026-10-29 | IT-security policy documents: 0–9 employees 9%; 10–49 40%; 50–249 69%; 250+ 91% | H |
| S6 | https://api.scb.se/OV0104/v1/doris/sv/ssd/NV/NV0116/NV0116J/ForetagRobotAnv | SCB | Användning av robotar i företag, 2022 | 2022 data | 2026-10-29 | Manufacturing (10+ employees) robot use ≈29% (derived sum) | H |
| S7 | https://www.spiris.se/globalassets/pressrum/dokument/spiris_branschrapport-2025.v1.1.pdf | Spiris (Visma) | Branschrapport 2025 – Tillväxt, teknikskifte och nya marknadsstrukturer | ~Dec 2025 (file metadata) | 2026-10-29 | ~61 bn SEK market; 25k firms; 62% done by <10-employee ABs; founder average age 64; Cedra/Azets deals; price headroom 20–30%; 12,888 in AML register | M (vendor report; vested interest) |
| S8 | https://www.faronline.se/dokument/balans/2026/april/balans_2026041001/ | Balans (FAR) | Interview with Fortnox's Håkan Rosén on licence changes | 2026-04-10 | 2026-10-29 | Byrålicens +200 SEK per consultant per month (autumn 2025); bundling criticised; firms considering switching | M |
| S9 | https://www.faronline.se/dokument/balans/2026/april/balans_2026041402/ | Balans (FAR) | Accounting firms' criticism of Fortnox | 2026-04-14 | 2026-10-29 | Partner fees; "betydelselös mellanhand"; lack of competition makes switching hard | M (social-media quotes) |
| S10 | https://borsvarlden.com/finwire/FWM00D3792 | Finwire/Börsvärlden (citing Dagens Industri) | Fortnox möter kritik efter ny obligatorisk tjänst | 2026-04-13 | 2026-10-29 | Mandatory "Access" 9–199 SEK per month; firms critical; Fortnox acknowledges churn risk; delisted Jul 2025 | M |
| S11 | https://www.srfkonsult.se/globalassets/dokument/aret-i-korthet/2026/srf-konsulterna_rapport_final_260702_2.pdf | Srf konsulterna | Annual report (Året i korthet) | 2026 (est.) | 2026-10-29 (404 on fetch) | ARK 2,663→2,716; ALK 776→806 | L |
| S12 | https://www.vardforetagarna.se/app/uploads/sites/3/2026/06/Aldreomsorgsbarometern-20260611.pdf | Vårdföretagarna (Almega) | Äldreomsorgsbarometern | 2026-06-11 | 2026-10-29 | Eldercare cost 166 bn (2024); hemtjänst 35%; private purchases 23 bn (hemtjänst ~8 bn); ~180 LOV municipalities in hemtjänst; 28 in special housing; satisfaction 85% | M (industry association; data from Socialstyrelsen/SKR) |
| S13 | https://www.ekonomifakta.se/sakomraden/foretagande/valfardsforetag/omsorgen-i-privat-regi_1213087.html | Ekonomifakta (Svenskt Näringsliv) | Omsorgen i privat regi | updated 2026-09-21 | 2026-10-29 | Municipalities bought 15.3% of care from private firms in 2025 (19.4% incl. other public) | M |
| S14 | https://www.ekonomifakta.se/sakomraden/foretagande/valfardsforetag/varden-i-privat-regi_1213086.html | Ekonomifakta | Vården i privat regi | updated 2026-07-01 | 2026-10-29 | Regions bought 12.3% of healthcare from private firms in 2025 | M |
| S15 | https://lakartidningen.se/nyheter/notiser/hyrkostnaderna-sjunker-men-inte-for-lakare/ | Läkartidningen (citing SKR) | Hyrkostnaderna sjunker men inte för läkare | 2026-09-23 | 2026-10-29 | Regions' hired-staff costs −2.6% (−62 MSEK) in H1 2026; hired-doctor costs rising | M |
| S16 | https://www.svt.se/nyheter/lokalt/helsingborg/facket-tar-strid-mot-minutstyrning-i-bland-annat-helsingborg-vi-stressar-till-bristningsgransen | SVT | Facket tar strid mot minutstyrning | 2026-06-01 (updated 2026-09-15) | 2026-10-29 | ~1 in 4 municipalities use minute scheduling (Socialstyrelsen, autumn 2025); Kommunal negotiating in 100 municipalities | M |
| S17 | https://www.socialstyrelsen.se/contentassets/bd46266fbc174da1a472373a3e2671de/2026-4-10218.pdf | Socialstyrelsen | Report on hemtjänst (snippet) | 2026 | 2026-10-29 | 9.16 (2024) → 10.06 (2025) hemtjänst recipients per carer on weekdays; Timecare/IntraPhone mentioned in municipal documents | L |
| S18 | https://data.riksdagen.se/dokument/HD0393.html | Riksdagen | Prop. 2025/26:93 Ett språkkrav inom äldreomsorgen; plus SoL 2025:400 municipal documents | 2025/26 | 2026-10-29 | Language requirement in force 1 Jul 2026; new documentation requirements under SoL 2025:400 | L |
| S19 | https://fastighetstidningen.se/?p=141485 | Fastighetstidningen | Construction bankruptcies 2025 | 2026-01-19 | 2026-10-29 | 1,933 construction bankruptcies (−5%); 9 in 10 had <10 employees; Stockholm 41% | M |
| S20 | https://www.tv4.se/artikel/tt-260102-konkurser1-19bf3b74/antalet-konkurser-pa-fortsatt-hog-niva | TT/TV4 (Creditsafe data) | Antalet konkurser på fortsatt hög nivå | 2026-01-02 | 2026-10-29 | 10,158 AB bankruptcies in 2025; haulage +18%, retail +16% | M |
| S21 | https://www.foretagarna.se/nyheter/riks/2026/oktober/fler-konkurser-i-september/ | Företagarna (UC/Creditsafe data) | Fler konkurser i september | 2026-10-01 | 2026-10-29 | Sept 2026: 798 AB bankruptcies (highest September since 1994); Jan–Sep 6,910 (−6%); wholesale +56% | M |
| S22 | https://www.placera.se/telegram/byggforetagen-bygginvesteringarna-okar-aterhamtningen-fortsatt-bracklig-20261020 | Finwire/Placera (Byggföretagen forecast) | Bygginvesteringarna ökar – återhämtningen fortsatt bräcklig | 2026-10-20 | 2026-10-29 | +6% construction investment 2026–27, ~690 bn in 2027; housing starts 29,500 (2025) → 31,700 (2027) | M |
| S23 | https://fastighetstidningen.se/?p=142050 | Fastighetstidningen | Boverket's EPBD proposal | 2026-02-10 | 2026-10-29 | No retroactive residential requirements; energy classes shift towards D/C on new declarations | M |
| S24 | https://www.bostadsratterna.se/media/oswefzu0/att-bo-i-bostadsrätt-2023.pdf | Bostadsrätterna | Att bo i bostadsrätt 2023 | 2023 | 2026-10-29 | "cirka 29 000 bostadsrättsföreningar som äger sina hus"; ~7,500 member BRFs | L |
| S25 | https://via.tt.se/files/3237251/4441121/359329/sv | HSB | Bostadsrättsbarometern 2026 | 2026 | 2026-10-29 | Covers 4,274 BRFs in 207 municipalities | L |
| S26 | https://sbc.se/media/kiqnpfi5/sveriges-bostadsrattsrapport-2025.pdf | SBC | Sveriges Bostadsrättsrapport 2025 | ~Mar 2025 | 2026-10-29 | 31% of owners worried about BRF finances (+15 points since 2022); 50% worried about fee hikes | M |
| S27 | https://mb.cision.com/Main/15291/4363985/4152886.pdf | SBC (Cision) | SBC press material | 2026 | 2026-10-29 | SBC: 4,600 customers, 450 staff, 640 MSEK turnover in 2024 | L |
| S28 | https://www.affarsvarlden.se/artikel/4-av-10-bostadsrattsforeningar-hojer-avgiften-med-10 | Affärsvärlden / Nabo | BRF fee increases | n/a | 2026-10-29 | Nabo manages ~2,700 BRFs; 26% raised fees by 6.7% on average | L |
| S29 | https://offerta.se/guider/bygg-och-renovering/vad-kostar-ett-stambyte | Offerta | Vad kostar ett stambyte | ~Mar 2025 | 2026-10-29 | Stambyte 250–500k SEK per apartment; relining 75–150k | L |
| S30 | https://regeringen.se/pressmeddelanden/2026/03/krav-pa-inforande-av-effektavgifter-stoppas/ | Regeringskansliet | Krav på införande av effektavgifter stoppas | 2026-03-13 | 2026-10-29 | 2027 capacity-charge mandate stopped; Ei repeals by 30 Jun 2026; new model by 12 Apr 2027 | H |
| S31 | https://www.regelradet.se/download/18.73837f1119e639446eb367c/1779887263700/RR%202026-115%20Regelr%C3%A5et.pdf | Regelrådet | RR 2026-115 opinion on repealing Ei's tariff rules | 2026-05-27 | 2026-10-29 | 168 grid companies (147 local, 25 regional); top 3 ≈52% of customers; median ~11,200 customers | H |
| S32 | https://www.pv-magazine.com/2026/04/10/sweden-connects-21600-solar-plants-in-2025/ | pv magazine (Energimyndigheten / Svensk Solenergi data) | Sweden connects 21,600 solar plants in 2025 | 2026-04-10 | 2026-10-29 | 652 MW in 2025 (848 MW in 2024); ~314,600 plants; ~5.5 GW | M |
| S33 | https://www.affarsvarlden.se/kronika/sa-mycket-okade-solkonkurserna-2025 | Affärsvärlden (column; Laddtorsk data) | Så mycket ökade solkonkurserna 2025 | 2026 | 2026-10-29 (paywall) | 196 solar-installer bankruptcies in 2025 (+33%) | L |
| S34 | https://www.ess-news.com/?p=4647 | ESS News (pv magazine) | Swedish grid operators reluctant to integrate batteries | 2025-03-26 | 2026-10-29 | Battery capacity 80→610 MW (2024); connection refusals and queues; little use of flexibility | M |
| S35 | https://flex-wiki.pages.dev/wiki/anvisningssystem | flex-wiki (third party, citing Svk) | Anvisningssystem / Svk NUP 2026–2035 | 2026 | 2026-10-29 | Svk queue >175 GW requested feed-in; allocation system from 2027 | L (verify with Svk) |
| S36 | https://balticwind.eu/sweden-approved-over-5-gw-of-battery-parks-in-five-years-green-power-sweden-reports/ | Baltic Wind (Green Power Sweden) | Sweden approved >5 GW of battery parks | 2026 | 2026-10-29 | 130 battery parks, >5 GW approved 2021–25 | L |
| S37 | https://regeringen.se/regeringsuppdrag/2025/09/uppdrag-till-affarsverket-svenska-kraftnat-om-att-se-over-anslutningsprocessen-till-elsystemet-och-tilltradet-till-elmarknaden-for-ett-starkare-och-mer-konkurrenskraftigt-sverige/ | Regeringskansliet | Uppdrag till Svk om anslutningsprocessen | 2025-09 | 2026-10-29 | Svk to review the connection process; final report 30 Apr 2026 | L |
| S38 | https://data.riksdagen.se/dokument/HD031d8.html | Riksdagen / Regeringen | Prop. 2025/26:1 Utgiftsområde 6 Försvar och samhällets krisberedskap | 2025-09-22 | 2026-10-29 | UO6 225.0 bn (2026 proposed); 3.5% of GDP by 2030; 300 bn loan cap (50 bn civil); materiel 52.1 bn (2024); civil defence up to 15 bn a year from 2028 | H |
| S39 | https://data.riksdagen.se/dokument/HD0328.html | Riksdagen / Regeringen | Prop. 2025/26:28 Ett starkt skydd för nätverks- och informationssystem – en ny cybersäkerhetslag | 2025-10-14 | 2026-10-29 | In force 15 Jan 2026; "drygt 1 500 företag… runt 500 000 sysselsatta"; ≥50 staff / >10 M EUR threshold; fines up to 2% / 10 M EUR | H |
| S40 | https://data.riksdagen.se/dokument/HD03303.html | Riksdagen / Regeringen | Prop. 2025/26:303 En ny lag för ökad motståndskraft hos kritiska verksamhetsutövare | 2026-07-14 | 2026-10-29 | CER law proposed in force 1 Jan 2027 | H |
| S41 | https://data.riksdagen.se/dokument/HC03131.html | Riksdagen / Regeringen | Prop. 2024/25:131 Nya regler för datacenter och hållbara bränslen | 2025-03-18 | 2026-10-29 | Data centres ≥500 kW must publish energy information annually (EED) | H |
| S42 | https://www.svensktvatten.se/om-oss/nyheter-och-press/nyheter/ny-rapport-590-miljarder-behover-investeras-i-vatten-och-avlopp/ | Svenskt Vatten | Ny rapport: 590 miljarder behöver investeras i vatten och avlopp (Investeringsrapporten 2026) | 2026-10-01 | 2026-10-29 | 590 bn to 2040 (~37 bn a year); 2025 investment ~31.5 bn; ~70% renewal; taxa +7.5% / +7.2% in 2026 | H |
| S43 | https://www.transportforetagen.se/prioriterade-fragor/transportfakta/ | Transportföretagen | Transportfakta | undated | 2026-10-29 | ~56,000 firms, ~325,000 employees, >1,500 bn SEK turnover | M (undated) |
| S44 | https://www.sakerhetsforetagen.se/2026/10/23/bevakningsforetagens-roll-i-totalforsvaret/ | Säkerhetsföretagen | Bevakningsföretagens roll i totalförsvaret (plus homepage facts) | 2026-10-23 | 2026-10-29 | ~200 members, ~30,000 employees; calls for state funding; Police analysing civilplikt for guarding | M |
| S45 | https://www.fi.se/sv/om-fi/vara-prioriteringar-i-tillsynen/ | Finansinspektionen | Våra prioriteringar i tillsynen 2026 | reviewed 2026-02-05 | 2026-10-29 | Priorities: operational/IT resilience, AML/fraud, consumer products; FI as AI Act surveillance authority (SOU 2025:101) | H |
| S46 | https://ellevio.se/link/3cd6588a61894a7388f1d368b4aaf358.aspx | Ellevio / Energiföretagen | Grid investment need | n/a | 2026-10-29 | ~890–945 bn SEK grid investment needed 2021–2045 | L |
| S47 | https://www.pveurope.eu/solar-storage/swedish-government-presents-kraftlyftet-proposal-grid-capacity | pv Europe | Swedish government presents Kraftlyftet proposal | 2026 | 2026-10-29 (redirect loop) | 200 MSEK in 2026, 400 MSEK a year from 2027 | L |
| S48 | https://www.dnb.com/sv-se/nyheter/stora-konkurser-slar-hart-fler-jobb-hotas-trots-mattlig-okning.html | Dun & Bradstreet | Stora konkurser slår hårt | 2026 | 2026-10-29 | Construction bankruptcies −6% (2025); bankruptcies of ≥100 MSEK-turnover firms +12.1% | L |
| S49 | https://www.affarsvarlden.se/premium/fortnox-skruvar-at-provisionerna-ogillas-av-redovisningsbyraerna | Affärsvärlden | Fortnox skruvar åt provisionerna – ogillas av redovisningsbyråerna | n/a | 2026-10-29 | Headline only: Fortnox tightened partner commissions | L |
| S50 | https://borsvarlden.com/artiklar/fortnox-ska-ha-over-12-000-redovisningsbyraer-som-kunder-2025 | Börsvärlden | Fortnox ska ha över 12 000 redovisningsbyråer som kunder 2025 | n/a | 2026-10-29 | Fortnox target of 12,000+ accounting-firm customers | L |
| S51 | https://www.ivo.se/globalassets/dokument/publikationer/rapporter/rapporter-2026/forberedelser-infor-utokad-kommunal-anmalningsplikt.pdf | IVO | Förberedelser inför utökad kommunal anmälningsplikt | 2026-03 | 2026-10-29 | Expanded municipal reporting duty to IVO; more reports expected | L |
| S52 | https://www.uppsala.se/contentassets/38a79edbd1a64176a91934643fbb0831/8-aln-uppsagning-av-avtal-gallande-hemtjanst-och-hemsjukvard.pdf | Uppsala kommun | Uppsägning av avtal gällande hemtjänst och hemsjukvård | 2025-06 | 2026-10-29 | Uppsala ends hemtjänst LOV, contracts terminated by 31 Aug 2025 | L |

*Note on rejected evidence:* one search-engine summary claimed a June 2026 Realtid article on falling new-BRF formations. Fetching it showed the article is from **28 Jan 2009** (895 new BRFs in 2008). It was excluded. This is why L-rated items must be verified before use.
