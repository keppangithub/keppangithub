# 07 — Competitor intelligence: cyber / public-sector / compliance opportunity areas (Sweden)

Reference date: 29 Oct 2026. Retrieval: 2026-10-29/30. Author: competitive-intelligence sub-agent.

**How to read the numbers**
- Swedish financials come from allabolag.se search-result pages. Revenue is shown there without a unit. Allabolag's standard is **kSEK**, so "689 530" means about 689.5 MSEK. The year is the latest filing year shown. Profit ("resultat") was **not shown** on search pages and is reported as "not found" unless stated otherwise.
- "not found" means I searched and the information was not public or not retrievable. Nothing is estimated unless it is labelled **[analyst inference]**.
- Some vendor domains did not resolve from this sandbox: wfisms.se, kycon.se, cocrisis.com, and the parked fidureon.se and exportkontroll.se. Facts for those vendors are taken from third-party pages or alternative domains.
- Coverage limit: web search worked poorly for Swedish SME vendor names. Several candidates named in the brief could not be profiled (Noru, Kertos, DataGuard pricing, Lexly, Pej, Kycon, Svensk Säkerhetsrådgivning, Krisberedskapsbyrån, Lumell, Kommers, Inköpsrådet). They are listed as "not found" rather than guessed.

---

## Executive summary of market structure

| # | Area | Classification | Key reason |
|---|---|---|---|
| 1 | NIS2 / Cybersäkerhetslagen compliance-as-a-service for municipalities, municipal companies and 50–500 FTE entities | **Fragmented, with consolidating channels.** Crowded at the top (Truesec, Knowit, Advania, Atea, Combitech, Omegapoint). There is a cheap-tool layer: KLASSA (free or low cost via SKR/Adda, 410 organisations, now NIS2-mapped), WF ISMS (from 2,995–3,990 SEK/month) and Isodora (from 500 SEK/month). A **fixed-price "software + Swedish vCISO" bundle for small municipalities and municipal energy/water/housing companies is underserved.** | No vendor found publishing a fixed monthly vCISO + ISMS price aimed at municipalities. Kammarkollegiet's state IT-security consultant framework (ITK area 3) expired on 2026-03-09. |
| 2 | Säkerhetsskydd + civil-defence/continuity subscription for municipalities | **Emerging, with fast-growing spend; fragmented supply.** Adda's new national framework (area 7 "krisberedskap och totalförsvar", up to 10 suppliers, 2026-02-16 to 2030-02-15) will concentrate call-offs among framework winners. | Uppsala kommun alone advertised a **100 MSEK** framework (2+1+1 years) for krisberedskap, civilt försvar and säkerhetsskydd (TED 307120-2026). State grants to municipalities were 649 MSEK in 2024 and 739 MSEK in 2025. |
| 3 | Defence-SME supplier onboarding and compliance | **Underserved / emerging-unproven as a productised service.** Supply is split between Combitech, security consultancies (Vesper, SRI), law firms and associations (SOFF, Exportkontrollföreningen). There is no Swedish JOSCAR-style shared supplier-assurance utility. | SOFF has 400–500 members, mostly SMEs. FMV requires companies to implement ISM before signing a säkerhetsskyddsavtal, and the CEO and security-protection officer must be different people. SOU 2026:16 proposes a 300 MSEK defence-export initiative to 2030. |
| 4 | EU CRA + Machinery Regulation readiness for SME manufacturers | **Emerging-unproven, likely to be bottlenecked.** Test/certification incumbents (Intertek Semko 462 MSEK, RISE) sit beside cheap SaaS (sbomify US$159/month, Verimu €49–149/month). No Swedish "PSIRT-as-a-service" offer for SMEs was found. | No CRA notified body had been designated EU-wide as of 8 Sep 2026. Reporting obligations started on 11 Sep 2026; full application is 11 Dec 2027. |
| 5a | Procurement support for small municipalities and public companies | **Fragmented and structurally constrained.** Buyers lean on staffing firms (Bemannia), inter-municipal sharing (for example Timrå buying from Sundsvall for 1.372 MSEK/year) and platform-attached consulting (e-Avrop). | The procurement rules themselves constrain this market: buyers must tender for consultants, and Konkurrensverket fines unlawful direct awards. |
| 5b | Done-for-you bid writing for SMEs | **Fragmented (micro-firms), with software substitution under way.** Tendium (AI bid studio, from €125/month), Mercell (owns TendSign and Opic since 2020) and e-Avrop's "anbudskonsulter". | Every allabolag "upphandlingskonsult/anbud" firm found has under 10 MSEK revenue and 1–5 employees. |
| 6 | AML/KYC for small obliged entities | **Saturated / dominated by bundled incumbents at the low end.** Fortnox Byråpartner (KYC included, 499 SEK/month), Spiris/Visma Advisor KYC (199 SEK per client per year), Björn Lundén Lundify (16,650 SEK/year for 1 user, more than 11,000 users), plus Trapets, Blikk, Roaring and Creditsafe. | Low prices, embedded in practice-management software, and high switching friction. There is a possible opening in a **"done-for-you AML function"** (policy, risk assessment, file review, training, supervisory-inspection support) for estate agents, dealers and small accounting firms before AMLR applies on 10 July 2027 **[analyst inference]**. |

---

## Area 1 — NIS2 / Cybersäkerhetslagen compliance-as-a-service

### Competitor table

| Competitor | Website | Country / market | Segment | Positioning | Pricing & contract (public?) | Financials (allabolag, kSEK) | Distribution / channels | Key capabilities | Weaknesses / notes | Switching costs | Partnerships / certs / launches |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Truesec** | truesec.com | SE / Nordics | Enterprise, public sector, mid-market | Premium IR/SOC + advisory brand | not found | Truesec Group AB (556690-8074): rev 689,530, 32 empl (2025). Truesec Detect AB: rev 321,947, 148 empl (2025). Truesec FS AB merger in progress (2026-09-24) [allabolag] | Direct; frameworks | IR, MDR/SOC, advisory | Premium price point; not a SMB/municipal fixed-price play **[inference]** | High (MDR integration) | not found |
| **Secify** | secify.com | SE | Large and smaller organisations; healthcare, finance, industry, supply chain | Broad cyber + compliance consultancy (CISO-as-a-Service, DPO, NIS2, ISO 27001, GAP analyses, CRA, PDL, SOC/SIEM, pentest) | No prices published [secify.com] | Secify by Sweden AB (559316-2513): rev 33,474, 21 empl (2025) | Direct | vCISO, DPO, NIS2, CRA, SOC | No municipal references on the homepage; logos are private sector (If, Coop MedMera, Kronans Apotek, Aleris…) | Medium | not found |
| **Webbfabriken – WF ISMS** | webbfabriken.com (wf-isms) | SE (also .us site) | SMEs, public sector (claims Swedish data residency as a "hard requirement" for public sector, finance, healthcare) | Swedish-hosted multi-framework ISMS: ISO 27001:2022, NIS2, GDPR, SOC 2, DORA, PCI DSS, **MSB frameworks, Säkerhetsskyddslagen** | "from 3,990 SEK/month (up to 5 users)". Another vendor page says Starter 2,995 SEK/month, so the vendor's own figures are inconsistent [search-result extract of webbfabriken.com compare page] | Webbfabriken AB (559274-4816): rev 5,606, 5 empl (2025) | Direct web | Risk register, controls, incidents, supplier and audit tracking | Very small company; no municipal reference customer found | Medium (data migration) | not found |
| **Isodora** | isodora.se | SE (Stockholm) | Growing companies, SMEs (finance, industry, crafts, energy) | AI-agent compliance platform (ISO 27001, GDPR, NIS2, DORA, SOC 2, ISO 9001, CSRD, AI Act) with MCP integration | **From 500 SEK/month platform fee + framework add-ons**; 7-day trial; "no enterprise minimum". Benchmarks traditional consulting at **450k–1.7 MSEK and 3–9 months** [isodora.se] | Isodora AB (559565-0424): no filing yet [allabolag] | Self-serve | Automated control checks, evidence, free NIS2 applicability test | New; anonymised cases only; no public-sector focus | Low–medium | SIS licensee; partner Hellström Advokatbyrå [isodora.se] |
| **KLASSA (SKR / Adda)** | klassa.skr.se | SE | Municipalities, regions, municipal companies, agencies | Sector-owned information-classification and security-requirements tool; **KLASSA 5.0 requirements catalogue mapped to NIS2 implementing regulation 2024/2690**, GDPR, OSL, ISO 27001 | Older SKR material says it is free of charge. SaaS and on-prem versions are now run by Adda; current price not found | n/a (SKR/Adda) | SKR network; **used by 410 organisations** | Classification, risk, requirements, follow-up | Tool only; no vCISO or people | High (sector standard, embedded in municipal policies, e.g. Eksjö) | Owned by SKR/Adda/Inera [klassa.skr.se] |
| **Knowit Cybersecurity & Law** | knowit.se | SE/Nordic | Public + private | Cyber + legal advisory | not found | Knowit Cybersecurity & Law AB (556866-3248): rev 191,734, 122 empl (2025) | Frameworks (Kammarkollegiet ITK area 3 supplier with Precio Fishbone) | Advisory, legal | Hourly-rate model (IT-säkerhetsanalytiker about 1,565 SEK/h on ITK 2020, see benchmarks) | Medium | — |
| **Combitech (Saab)** | combitech.com | SE | Defence, public sector, industry | Security + technology consultancy | Hourly on frameworks (about 1,270 SEK/h for IT-säkerhetsanalytiker on ITK 2020) | Combitech AB (556218-6790): rev 4,754,858, 2,203 empl (2025) | Frameworks, direct | Cyber, säkerhetsskydd, crisis, defence | Large-firm overhead **[inference]** | Medium | Saab group |
| **Omegapoint** | omegapoint.se | SE | Enterprise, public | Security/dev consultancy | not found | Omegapoint Stockholm AB rev 506,042 (307 empl); Göteborg 178,736 (128); Malmö 125,300 (85) (2025) | Direct | AppSec, pentest, advisory | Not SMB/municipal-packaged | Medium | — |
| **Advania** | advania.se | Nordic | Enterprise/public IT | IT services incl. security | not found | Advania Sverige AB (556214-9996): rev 9,498,469, 1,578 empl (2025) | Frameworks | MSP + security | Generalist | High (MSP) | — |
| **Secure State Cyber** | securestate.se | SE | Public/enterprise | GRC/cyber consultancy | ITK 2020 IT-säkerhetsanalytiker about 1,668 SEK/h | Secure State Cyber AB (556689-2294): rev 38,356, 11 empl (2026 filing) | Kammarkollegiet framework | GRC | Small | Medium | — |
| **Visma Draftit** | draftit.se | SE | Compliance/legal-requirement registers | Legal-requirement tracking SaaS | not found | Visma Draftit AB (556578-3957): rev 92,477, 54 empl (2025) | Visma channel | Regulatory registers | Not security-specific | Medium | Visma group |
| **Stratsys** | stratsys.com | SE | Municipalities, regions, enterprise | Strategy/governance platform with risk/internal-control modules (incumbent in municipal management systems) | not found | Stratsys AB (556586-9848): rev 299,009, 150 empl (2025) | Direct; strong municipal base **[inference from its known positioning; not verified this session]** | Governance, risk | ISMS depth not verified | High | — |
| **Integrity360** | integrity360.com | IE/UK, selling in SE | Public sector IR | Incident response | DIS call-off | n/a (foreign) | **Adda "IT-säkerhet – Incidenthantering (IRT) DIS"** supplier (announced 5 Nov 2025) | IR | — | — | Adda DIS |
| **Opsio** | opsiocloud.com | SE | SMEs | MSP publishing NIS2 fixed-price packages | **Workshop/initial analysis 20,000 SEK; in-depth gap analysis 45,000–90,000 SEK; ongoing 10,000–30,000 SEK/month or 15,000–80,000 SEK/quarter; senior advisor 1,800–3,000 SEK/h** (vendor blog) | not retrieved | Content marketing | — | Vendor-marketing figures | — | — |
| **Vanta** | vanta.com | US, sells into SE | SaaS scale-ups | Automated compliance | Plans Essentials/Plus/Professional/Enterprise. **No public prices**; NIS2 not visible on pricing page [vanta.com/pricing] | n/a | Direct | SOC 2/ISO automation | US-centric; no Swedish public-sector fit | Medium | — |
| **Fidureon** | fidureon-website.pages.dev | unknown | NIS2 Art. 21 supply-chain mapping | NIS2 software | not found | not found (fidureon.se parked at Loopia) | — | Supplier-to-process mapping | Unverifiable vendor | — | — |
| **Legiscope** | legiscope.com | LT | Privacy teams | GDPR system marketing in Swedish | Says NIS2 platforms typically cost **30,000–200,000 SEK/year** (vendor blog) | n/a | — | — | — | — | — |
| Kertos, DataGuard, Noru, Formpipe | — | DE/SE | — | — | **not found** (pages 404 or not retrieved) | not found | — | — | — | — | — |

### Spend evidence (Area 1)
- **Adda "IT-säkerhet – incidenthantering (IRT) DIS"** and **"Säker digital kommunikation DIS"** are existing dynamic purchasing systems open to municipalities (Adda Upphandlingsplan 2026). Integrity360 is an appointed IRT supplier.
- **Kammarkollegiet ITK area 3 "Säkerhet i IT och IT-projekt"** covered IT security, information security and security technology. It ran 2022-03-10 to **2026-03-09 and has expired**. The ITK info seminar of 2025-11-06 lists it as "Utgår 2026-03-10". Successor not confirmed. This gap matters for state buyers and for municipalities eligible to call off.
- **Adda "It-infrastruktur 2026"** (start Oct 2027) includes "säkerhetslösningar". **"Programvaror och molntjänster 2027"** starts Nov 2028.
- KLASSA's move to NIS2 mapping, and use by 410 organisations, shows municipalities already working the problem. Much of that work runs through low-cost sector tools.

---

## Area 2 — Säkerhetsskydd + civil defence / continuity planning subscription

### Competitor table

| Competitor | Website | Country | Segment | Positioning | Pricing & contract | Financials (kSEK) | Distribution | Capabilities | Weaknesses | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| **Combitech** | combitech.com | SE | Defence, public sector | Security, säkerhetsskydd, crisis management | Hourly / framework | rev 4,754,858; 2,203 empl (2025) | Frameworks, direct | Broad | Large-firm rates | Appears in allabolag "krisberedskap" match |
| **Vesper Group** | vespergroup.com | SE | Enterprise, public | Security risk management, säkerhetsskydd | not found | Vesper Group AB (556665-9354): rev 244,236, 155 empl (2025) | Direct | Säkerhetsskydd, risk, travel security | Corporate focus **[inference]** | Top allabolag match for "säkerhetsskydd" |
| **SRI (S R Intelligence)** | — | SE | Public/enterprise | Security/intelligence consultancy | not found | S R Intelligence AB (559088-9381): rev 62,013, 35 empl (2025) | Direct | Säkerhetsskydd | — | allabolag "säkerhetsskydd" hit |
| **Attiva AB** | — | SE | — | Security consultancy | not found | 559305-2433: rev 13,581, 5 empl (2025) | — | — | — | — |
| **Micro firms** (Arentoft Säkerhetsskydd, Svenska Säkerhetsskyddsbyrån, Krisberedskap Sverige AB) | — | SE | Municipalities, SMEs | Säkerhetsskydd/krisberedskap niche | not found | 2,705 / 291 / 684 kSEK revenue; 1–2 empl each (2025) | Direct | — | Sub-scale | Evidence of fragmentation |
| **4C Strategies** | 4cstrategies.com | SE | Defence, government, enterprise | Exercise/readiness software (Exonaut) + consulting | Framework with Försvarsmakten: 150 MSEK over 5+2 years; another 2-year framework 48 MSEK (up to 100 MSEK) [MFN press releases] | 4C Strategies AB (556598-6436): rev 92,327, 28 empl (2025) | Direct, frameworks | Exercises, readiness management | Defence/enterprise-priced | Likely a credible area-7 bidder **[inference]** |
| **Cosafe Technology** | cosafe.com | SE | Municipalities, schools, enterprises | Digital incident/crisis/alarm communication platform | not found | Cosafe Technology AB (556987-4539): rev 50,251, 18 empl (2025) | Direct to municipalities (Sigtuna, Höganäs contracts) | Crisis comms, alarm | Comms tool, not a planning service | — |
| **Grannkompaniet – Cocrisis** | cocrisis.com (no DNS) | SE | Municipalities | Crisis-management platform | not found | not found | Eslöv kommun contract (2018) | Crisis log/coordination | Old evidence | — |
| **SOS Alarm** | sosalarm.se | SE (state/SKR-owned) | Municipalities, regions | Alerting municipal TiB under agreements; krisjour | not found | not retrieved | Agreements with municipalities and regions | 24/7 alerting | Not planning/säkerhetsskydd advisory | Incumbent in TiB alerting |
| Sweco, AFRY, WSP, Securitas consulting, Prevent, Everbridge, Crises Control, DSAM, Safeplan, Svensk Säkerhetsrådgivning | — | — | — | — | **not found** this session (search returned no usable vendor data) | not found | — | — | — | — |


### Spend evidence (Area 2)
- **Adda "Säkerhetslösningar konsulter 2025"** (ref. 10658) runs **2026-02-16 to 2030-02-15**, with no extension. It has 7 areas, and **area 7 = "Konsulter för krisberedskap och totalförsvar"** (beredskapsplanering, utbildning, övningar, krishantering, stöd vid krishantering, övergripande planering). Up to **10 ranked suppliers** in area 7 and up to 5 in areas 1–6. Call-offs **≤150 kSEK go by ranking** to the #1 supplier; **>150 kSEK go by FKU** (renewed competition). National coverage is required. The supplier list was not found publicly.
- **Uppsala kommun, TED 307120-2026** (OJ S 86/2026, 05/05/2026): "Ramavtal Tjänster inom krisberedskap, civilt försvar och säkerhetsskydd", CPV 79417000. **Estimated value 100,000,000 SEK** excl. VAT. Runs 16/09/2026–15/09/2028 with 2×12-month extensions. Open procedure via TendSign.
- **State funding to municipalities** (MSB/SKR agreement 2024–2026): **649 MSEK in 2024** (+130 MSEK) and **739 MSEK in 2025**, per search-result extracts of government press releases and budget documents. The 2026 figure is not verified.
- Adda "Säker förvaring 2027" (crisis storage, start June 2028) and "Livsmedel krisberedskap 2026" show a broader shift of municipal purchasing towards preparedness.

---

## Area 3 — Defence-SME supplier onboarding & compliance service

| Competitor / actor | Website | Country | Segment | Positioning | Pricing | Financials (kSEK) | Notes |
|---|---|---|---|---|---|---|---|
| **SOFF (Säkerhets- och försvarsföretagen)** | soff.se | SE | 400–500 member companies; SMF group | Industry association: member groups incl. **säkerhetsskydd** and cyber defence; anti-corruption course; Försvarsentreprenörsdagen'26 with FMV, Saab, BAE Systems Bofors & Hägglunds on "Att leverera till systemleverantörer" | Membership fee not found | n/a | Membership page says "500 medlemsföretag"; the FED'26 folder says "över 400". An older remiss response says >100 members, >80 SMEs. SOFF calls säkerhetsskydd "betungande administrativt och kostsamt" |
| **Business Sweden / Team Sweden Defence & Security** | business-sweden.com | SE (state) | Exporters | Export promotion | Current 15,000 SEK export-support application fee is proposed to be abolished | n/a | SOU 2026:16: **300 MSEK** over 2026–2030 (≈15 pavilions, 25 market days, ~10 delegations). Business Sweden says the target group is much larger than current reach |
| **Combitech** | combitech.com | SE | Defence suppliers | Security/säkerhetsskydd, ISM | Hourly | 4,754,858 rev (2025) | Saab-owned, so conflict-of-interest perception among Saab suppliers **[inference]** |
| **Vesper Group / SRI** | — | SE | Enterprise | Säkerhetsskydd consulting | not found | 244,236 / 62,013 | — |
| **Law firms** (Mannheimer Swartling, Setterwalls…) | — | SE | Larger exporters | Export control / sanctions legal | not found (an older realtid.se headline references a Mannheimer rate of 1,906 SEK/h to SL; context not verified) | — | Premium |
| **Sveriges Exportkontrollförening** | (exportkontroll.se parked) | SE | Export-control practitioners | Association | not found | 802462-7575 | Only allabolag hit for "exportkontroll". **No commercial export-control consultancy found by name**, which suggests a thin market |
| **Hellios – JOSCAR** (UK model) | hellios.com | UK | Defence/aerospace supply chains | Shared supplier-assurance registry | Supplier fee not shown | n/a | **30+ buyers, 6,000+ suppliers** (BAE Systems, Boeing, Leonardo UK, Lockheed Martin, MBDA, Thales, QinetiQ, MoD). Saab not mentioned. No Swedish equivalent found |
| Almi, ISO certification consultancies, AQAP specialists | — | — | — | — | **not found** | — | — |

**Structural evidence of need (Area 3):**
- FMV's routines say a säkerhetsskyddsavtal is initiated by the customer (FMV, a foreign authority or a contracted company), not by the supplier. The company must **implement ISM (Industrisäkerhetsskyddsmanualen) as early as possible**. "Det är företagets ansvar att driva processen." FMV does not negotiate the wording. **The CEO and the security-protection officer may not be the same person** (except in one-person companies).
- Under Kammarkollegiet frameworks, subcontractors must also have security-protection agreements, which creates a cascade down to SMEs.
- Saab supplier-requirements page: **not retrieved** (404).

---

## Area 4 — EU Cyber Resilience Act + Machinery Regulation readiness for SME manufacturers

| Competitor | Website | Country | Segment | Positioning | Pricing | Financials (kSEK) | Notes |
|---|---|---|---|---|---|---|---|
| **Intertek Semko** | intertek.se | SE (Intertek UK) | Product manufacturers | Testing/certification; CRA webinar; "end-to-end cybersecurity testing and certification… to support CRA"; reporting-readiness checklist; EN 18031 (RED) gap assessments | not found | Intertek Semko AB (556024-0599): rev 462,142, 277 empl (2025) | Incumbent conformity channel |
| **RISE** | ri.se | SE (state) | Industry | Notified body for **RED cybersecurity** (radio equipment); Cyber Range; CRA press release 2026-09-09 | not found | n/a | **Not a CRA notified body as of Sep 2026** (none designated EU-wide) |
| **Secify** | secify.com | SE | Mid-market | Lists Cyber Resilience Act among compliance services | not found | 33,474 rev | Consultancy, not PSIRT tooling |
| **Omegapoint / Knowit / Combitech / Truesec** | — | SE | Enterprise | AppSec/product security | not found | see Area 1 | No CRA-specific pages surfaced in search |
| **sbomify** | sbomify.com | UK (sbomify ltd) | Product teams | SBOM management, CRA Compliance Wizard, Dependency-Track integration, trust centre | **Community $0; Business $159/month billed annually (5 products, 200 components); Enterprise custom** | n/a | Open source / self-hostable |
| **Verimu** | verimu.com | EU | SMEs | SBOM + CVE monitoring with 24h→72h→14d CRA notification workflow | **€49/month Starter; €149/month Professional.** Claims enterprise tools cost €2,000–5,000+/month | n/a | Vendor claim |
| **ONEKEY** | onekey.com | DE | Device makers | Firmware analysis, SBOM, PSIRT webinars ("start small but start") | Pricing page 404, so not found | n/a | — |
| Cybellum, Finite State, Kiwa, Pilz, Sick, TÜV, Debricked/OpenText, Sentor, Assured | — | — | — | — | **not found** this session | — | — |

**Regulatory timing (for demand modelling):**
- CRA notified-body rules apply from **11 Jun 2026**. Article 14 reporting (24h early warning, 72h notification) applies from **11 Sep 2026**, with the ENISA Single Reporting Platform open. Member states should have enough notified bodies by **11 Dec 2026**. Full application is **11 Dec 2027**.
- **No CRA notified body was designated in NANDO as of 8 Sep 2026.** Designation "takes months per body" (cyberresilienceact.eu, updated 11 Sep 2026).
- Sweden: SOU 2025:115 proposes Swedac as notifying authority and PTS as market surveillance authority. Riksdagen bill HCB1119 adds supplementary provisions.
- Machinery Regulation (EU) 2023/1230 applies from 20 Jan 2027 (from the regulation text, background knowledge; not re-fetched this session).

---

## Area 5 — Procurement support (buyers) & done-for-you bid writing (SMEs)

| Competitor | Website | Country | Segment | Positioning | Pricing | Financials (kSEK) | Notes |
|---|---|---|---|---|---|---|---|
| **Mercell (incl. TendSign, Opic)** | mercell.com | NO/SE | Buyers (e-tendering) + suppliers (alerts) | Europe-wide e-tender + alerts; bought Visma's Opic and TendSign (announced 25 Nov 2020) | No public list price. One user review reports 12,000 (2022) → 22,000 (2023), currency/scope unclear | Mercell Sverige AB (556533-8745): rev 369,381, 117 empl (2025) | At acquisition: ~1,000 pre-award buyers, 250 post-award, ~16,000 suppliers. Free supplier registration on TendSign |
| **Tendium** | tendium.com | SE | Suppliers (B2G sales) | AI B2G platform: Find, Pre-sell, Bid Studio, Louie AI, Office 365, competitor intelligence | **Light from €125/month**; Core and Scale "scale with bids/year"; unlimited users | Tendium AB (559169-6843): rev 36,182, 55 empl (2024) | "Trusted by thousands of companies"; has "Win Bid Specialists" and a partner network, i.e. productising bid help |
| **e-Avrop** | e-avrop.com | SE | Buyers and suppliers | Procurement tool, spend analysis, e-commerce, **"Konsulttjänster – Upphandling & Inköp"**, **"Anbudskonsulter"**, Pabliq alerts | Supplier ad database free; training 2,950 SEK/course; other prices not found | e-Avrop AB not found on allabolag | "1,500 buyers" |
| **Bemannia** | bemannia.se | SE | Municipalities | Staffing incl. procurement consultants | not found | not retrieved | Won procurement-consultant framework with Laholms kommun; Gävle framework covering ~20 competence areas |
| **Upphandlingsbyrån i Hälsingland** | — | SE | Local public/SME | Procurement consultancy | not found | 559174-9733: rev 7,405, 4 empl (2025) | — |
| **Micro procurement consultants** | — | SE | — | — | not found | Upphandlingskonsult Wilen AB 1,606 (1 empl); Proactive Upphandlingskonsult i Kalmar 1,404 (2); Upphandlingskonsulten TBO 347 (1) | Fragmentation evidence |
| **Micro bid writers** | — | SE | SMEs | — | not found | Anbud Direkt JSLB AB 5,774 (5 empl); M-Anbud Konsult 809 (2); Tender as a Service Sweden AB 602 (2) | Fragmentation evidence |
| **Upphandlingsmyndigheten / Företagarna** | — | SE | SMEs | Free guidance and bid guides | free | n/a | Free substitutes |
| Lumell, Kommers, Inköpsrådet, Anbudsbyrån, Upphandlingsexperten | — | — | — | — | **not found** (no allabolag match under those names) | — | — |

**Spend evidence (Area 5):**
- Timrå kommun buys procurement services from Sundsvall: **1,372,000 SEK/year**, equivalent to two employees' salaries (Konkurrensverket tillsynsbeslut, Timrå). Arvidsjaur's procurement-consultant contract: **37,968.75 SEK/month**, 1.8225 MSEK over 48 months (KKO 19-020). KKO 19-020 also references a procurement-consultant contract at **675 SEK/h** (2019).
- Adda has **no current dedicated procurement-consultant framework** found. "Gransknings- och rådgivningstjänster 2026" (start Oct 2027) covers contract compliance, sustainable value chains, environment, welfare crime and work-life crime.

---

## Area 6 — AML/KYC for small obliged entities

| Competitor | Website | Country | Segment | Positioning | Pricing (public) | Financials (kSEK) | Notes |
|---|---|---|---|---|---|---|---|
| **Fortnox – Kundkännedom** | fortnox.se | SE | Accounting firms | KYC built into practice software (BankID ID, PEP/sanctions, UBO, monitoring, unlimited clients) | **Included in Byråpartner, 499 SEK/month**; no per-check fees | not retrieved | Strong bundling incumbent |
| **Spiris (Visma) – Visma Advisor KYC** | spiris.se | SE | Accounting firms | Add-on to Byråstöd (Smarta Byrån) | **199 SEK per client per year** | not retrieved | Bundled |
| **Björn Lundén – Lundify Compliance** | bjornlunden.com | SE | Accountants, auditors, lawyers, **estate agents**, financial advisers, company brokers, funeral homes | KYC + templates (risk assessment, policy, routines) + AML training with certificate; Monitor and Conflict add-ons | **1 user 16,650 SEK/yr; 3 users 20,430; 5 users 30,190; 10 users 54,590** (Premium 23,840–126,490) | not retrieved | **More than 11,000 users** |
| **Trapets** | trapets.com | SE | Banks, investment firms, insurers, PSPs; Trapets KYC for accounting/audit firms | InstantWatch AML/market surveillance; AMLR readiness content | Demo only | Trapets AB (556586-4773): rev 142,443, 73 empl (2025) | Customers: DNB Carnegie, Coop Bank, Max Matthiessen. Integration with Björn Lundén |
| **Blikk KYC & AML** | blikk.se | SE | Accounting firms | KYC/AML workflow | not found | Blikk Sverige AB (559093-8345): rev 68,817, 24 empl (2025; whole company) | — |
| **Roaring.io** | roaring.io | SE | Banking, finance, insurance, public sector | Data/KYC APIs, monitoring, adverse media | **Sandbox 0; from 1,495 SEK/month + transaction pricing; monthly rolling** | Roaring Group AB (559067-2613): rev 55,987, 30 empl (2025) | Developer-oriented |
| **Wolters Kluwer – Capego KYC** | wolterskluwer.com | NL/SE | Accounting firms | KYC in Capego suite | not found | n/a | — |
| Creditsafe, Nordkyc, Pingwire, CM1, Signicat, ZignSec, Addo Sign | — | — | — | Listed on BusinessWith KYC comparison | not found | — | — |
| Kycon, Pej, "Penningtvätt.se", Srf tools, Lexly, Enento/UC | — | — | — | — | **not found** (no DNS / empty page / not searched) | — | — |

**Spend and enforcement evidence (Area 6):**
- In 2025, länsstyrelserna reviewed **33 accounting firms**; **31 got sanction fees**, totalling **4.6 MSEK** (FAR Balans, Mar 2026). By June 2024, 191 firms had been reviewed in Stockholm, Västra Götaland and Skåne, and just over 40% were sanctioned (FAR, Sep 2024).
- AMLR (EU 2024/1624) applies from **10 July 2027** (regulation text; background).

---

## Pricing benchmarks for financial modelling

| Item | Benchmark | Source / reliability |
|---|---|---|
| IT-security analyst hourly rate (state framework ITK 2020, area 3, price appendix 2024-02-29) | **1,006–1,696 SEK/h**: Tietoevry 1,006; Combitech 1,270; B3 1,272; Knowit & Precio 1,565; Secure State Cyber 1,668; HiQ 1,687; Softronic 1,696. Fixed under dynamic ranking, ceiling under FKU | avropa.se prisbilaga (via search extract; file since removed, column alignment unverified). **M** |
| Senior cybersecurity advisor | 1,800–3,000 SEK/h (cites "Radar Ecosystem 2024") | Opsio blog. **L–M** |
| NIS2 initial workshop / analysis (fixed) | 20,000 SEK | Opsio. **L–M** |
| NIS2 in-depth gap analysis (fixed) | 45,000–90,000 SEK | Opsio. **L–M** |
| Ongoing NIS2 advisory | 10,000–30,000 SEK/month, or 15,000–80,000 SEK/quarter | Opsio. **L–M** |
| Traditional ISO 27001/NIS2 consulting project | 450k–1.7 MSEK, 3–9 months | Isodora (competitor claim). **L** |
| NIS2 compliance platforms | 30,000–200,000 SEK/year typical | Legiscope blog. **L** |
| ISMS SaaS entry price (SE) | WF ISMS 2,995–3,990 SEK/month; Isodora from 500 SEK/month + add-ons | Vendor pages. **M** |
| vCISO international | UK £497–997/month basic retainer; US $3k–12k/month; AU $5k–15k/month (10–40 h) | pyralink, sidechannel, techbrain. **L–M**. *No Swedish public vCISO monthly price found* |
| Managed SOC (SE) | 25,000–80,000 SEK/month | Opsio. **L** |
| Procurement consultant | 675 SEK/h (2019 contract); about 38 kSEK/month retainer (Arvidsjaur); 1.372 MSEK/year for shared procurement function (Timrå) | Konkurrensverket. **H** (dated) |
| Construction consultant ladder (reference) | 350 / 780 / 880 SEK/h | Konkurrensverket 17-0643. **H** (different service) |
| Bid-writing software | Tendium from €125/month | tendium.com. **H** |
| SBOM / CRA tooling | sbomify $159/month; Verimu €49–149/month; "enterprise €2–5k+/month" (claim) | Vendor pages. **M** |
| KYC tools | Fortnox 499 SEK/month bundle; Spiris 199 SEK/client/year; Lundify 16,650–54,590 SEK/year; Roaring from 1,495 SEK/month | Vendor pages. **H** |
| Crisis/säkerhetsskydd framework call-off threshold | Adda area 7: ≤150 kSEK by ranking (direct to #1), above that FKU | Adda avropsvägledning. **H** |

---

## Implications for venture design [analyst inference]
1. **Area 2 has the strongest current spend signal.** Examples: a 100 MSEK single-municipality framework, the Adda area-7 national framework, and growing state grants. A subscription priced under **150 kSEK/year per customer** fits Adda's ranking-based direct call-off if the venture is an Adda area-7 supplier. Without a framework place, municipalities must tender, so getting onto frameworks (Adda, regional) is the gating go-to-market step.
2. **Area 1 should not compete with KLASSA or cheap SaaS on software.** It should bundle a Swedish vCISO + incident/reporting duty + board reporting at a fixed monthly fee, aimed at municipal companies (energy, water, housing) that are "important/essential entities" in their own right.
3. **Area 3 is thin but real.** A "JOSCAR-light" readiness passport (ISM/säkerhetsskydd, ISO 9001/27001, export-control basics) sold via SOFF or regional defence clusters could ride SOU 2026:16 funding.
4. **Area 6 is the least attractive as software.** It is attractive only as a service layer for under-served obliged entities (estate agents, dealers in goods, small accounting firms) that face sanction risk.
5. **Area 4 timing is uncertain.** The notified-body bottleneck and the 2027 deadline favour advisory + PSIRT retainer over certification.

---

## Source Ledger

| # | URL | Publisher | Title | Pub date | Retrieved | Finding | Rel. |
|---|---|---|---|---|---|---|---|
| 1 | https://www.allabolag.se/what/truesec | Allabolag | Search "truesec" | 2025 filings | 2026-10-29 | Truesec Group AB rev 689,530 kSEK/32 empl; Detect 321,947/148 | H |
| 2 | https://www.allabolag.se/what/secify | Allabolag | Search "secify" | 2025 | 2026-10-29 | Secify by Sweden AB rev 33,474/21 | H |
| 3 | https://www.allabolag.se/what/stratsys | Allabolag | Search | 2025 | 2026-10-29 | Stratsys AB rev 299,009/150 | H |
| 4 | https://www.allabolag.se/what/tendium | Allabolag | Search | 2024 | 2026-10-29 | Tendium AB rev 36,182/55 | H |
| 5 | https://www.allabolag.se/what/trapets | Allabolag | Search | 2025 | 2026-10-29 | Trapets AB rev 142,443/73 | H |
| 6 | https://www.allabolag.se/what/roaring | Allabolag | Search | 2025 | 2026-10-29 | Roaring Group AB rev 55,987/30 | H |
| 7 | https://www.allabolag.se/what/combitech | Allabolag | Search | 2025 | 2026-10-29 | Combitech AB rev 4,754,858/2,203 | H |
| 8 | https://www.allabolag.se/what/mercell | Allabolag | Search | 2025 | 2026-10-29 | Mercell Sverige AB rev 369,381/117 | H |
| 9 | https://www.allabolag.se/what/säkerhetsskydd | Allabolag | Search | 2025 | 2026-10-29 | Vesper 244,236/155; SRI 62,013/35; micro firms | H |
| 10 | https://www.allabolag.se/what/krisberedskap | Allabolag | Search | 2025 | 2026-10-29 | Krisberedskap Sverige AB 684/1 | H |
| 11 | https://www.allabolag.se/what/4c%20strategies | Allabolag | Search | 2025 | 2026-10-29 | 4C Strategies AB 92,327/28 | H |
| 12 | https://www.allabolag.se/what/cosafe | Allabolag | Search | 2025 | 2026-10-30 | Cosafe Technology AB 50,251/18 | H |
| 13 | https://www.allabolag.se/what/omegapoint | Allabolag | Search | 2025 | 2026-10-29 | Omegapoint entities | H |
| 14 | https://www.allabolag.se/what/intertek%20semko | Allabolag | Search | 2025 | 2026-10-29 | Intertek Semko AB 462,142/277 | H |
| 15 | https://www.allabolag.se/what/knowit%20cybersecurity | Allabolag | Search | 2025 | 2026-10-29 | Knowit Cybersecurity & Law 191,734/122 | H |
| 16 | https://www.allabolag.se/what/advania%20sverige | Allabolag | Search | 2025 | 2026-10-29 | Advania Sverige 9,498,469/1,578 | H |
| 17 | https://www.allabolag.se/what/webbfabriken | Allabolag | Search | 2025 | 2026-10-29 | Webbfabriken AB 5,606/5 | H |
| 18 | https://www.allabolag.se/what/isodora | Allabolag | Search | — | 2026-10-29 | Isodora AB 559565-0424, no filing | H |
| 19 | https://www.allabolag.se/what/secure%20state%20cyber | Allabolag | Search | 2026 filing | 2026-10-30 | Secure State Cyber 38,356/11 | H |
| 20 | https://www.allabolag.se/what/draftit | Allabolag | Search | 2025 | 2026-10-30 | Visma Draftit 92,477/54 | H |
| 21 | https://www.allabolag.se/what/blikk | Allabolag | Search | 2025 | 2026-10-30 | Blikk Sverige 68,817/24 | H |
| 22 | https://www.allabolag.se/what/upphandlingskonsult | Allabolag | Search | 2025 | 2026-10-29 | Micro procurement consultancies | H |
| 23 | https://www.allabolag.se/what/anbud | Allabolag | Search | 2025 | 2026-10-30 | Micro bid-writing firms | H |
| 24 | https://www.allabolag.se/what/upphandlingsbyrån | Allabolag | Search | 2025 | 2026-10-30 | Upphandlingsbyrån i Hälsingland 7,405/4 | H |
| 25 | https://www.allabolag.se/what/exportkontroll | Allabolag | Search | — | 2026-10-29 | Only Sveriges Exportkontrollförening | H |
| 26 | https://isodora.se/ | Isodora AB | Homepage | 2026 | 2026-10-29 | From 500 SEK/month; consulting 450k–1.7 MSEK claim; SIS licensee | M |
| 27 | https://secify.com/ | Secify | Homepage | 2026 | 2026-10-29 | Services incl. CISOaaS, NIS2, CRA; no prices | M |
| 28 | https://webbfabriken.com/en/cybersecurity/wf-isms (+ /compare via search extract) | Webbfabriken | WF ISMS | 2026 | 2026-10-29 | Frameworks incl. MSB, Säkerhetsskyddslagen; 2,995–3,990 SEK/month | M |
| 29 | https://webbfabriken.us/cybersecurity/wf-isms | Webbfabriken | WF ISMS (US) | 2026 | 2026-10-29 | No prices; ISO 27001/NIS2/GDPR | M |
| 30 | https://fidureon-website.pages.dev/nis2 | Fidureon | NIS2 page (search) | 2025 | 2026-10-29 | NIS2 supply-chain mapping SW | L |
| 31 | https://klassa.skr.se/ (user-forum and guidance files via search) | SKR | KLASSA | 2026-04-15 | 2026-10-29 | 410 organisations; KLASSA 5.0 NIS2-mapped; Adda takeover | M–H |
| 32 | https://www.adda.se/globalassets/3.-larande-verksamhetsstod/2.-digitalisering/klassa/klassa-produktblad--saas.pdf | Adda | KLASSA SaaS sheet | 2026 | 2026-10-29 | SaaS/on-prem; no price | H |
| 33 | https://www.adda.se/globalassets/2.-upphandling-ramavtal/8.-upphandlingsplan-2026/adda_upphandlingsplan_2026_a4_webb_ny.pdf | Adda | Upphandlingsplan 2026 | 2026 | 2026-10-29 | IRT DIS; Säker digital kommunikation DIS; Gransknings- och rådgivningstjänster (Oct 2027); It-infrastruktur 2026 | H |
| 34 | https://www.adda.se/globalassets/2.-upphandling-ramavtal/2.-fastighetsforvaltning/fastighetsnara-tjanster/sakerhetslosningar-konsulter-2025/avropsvagledning---sakerhetlosningar-konsulter-2025.pdf | Adda | Avropsvägledning Säkerhetslösningar konsulter 2025 | 2026 | 2026-10-29 | Area 7 krisberedskap & totalförsvar; 10 suppliers; 150 kSEK ranking threshold | H |
| 35 | https://www.adda.se/globalassets/2.-upphandling-ramavtal/2.-fastighetsforvaltning/fastighetsnara-tjanster/sakerhetslosningar-konsulter-2025/1.administrativa-foreskrifter-enligt-ama-konsult-10-1.pdf | Adda | AF (via search extract) | 2026-01-23 | 2026-10-29 | Term 2026-02-16 to 2030-02-15; ref 10658 | M–H |
| 36 | https://ted.europa.eu/en/notice/307120-2026/pdf | EU TED / Uppsala kommun | Ramavtal Tjänster inom krisberedskap, civilt försvar och säkerhetsskydd | 2026-05-05 | 2026-10-29 | Est. 100 MSEK; 2026-09-16 to 2028-09-15 +2×12 months | H |
| 37 | https://insights.integrity360.com/integrity360-appointed-trusted-supplier-for-incident-response-by-adda | Integrity360 | Appointed IRT supplier by Adda | 2025-11-05 | 2026-10-29 | Adda IRT DIS supplier | M |
| 38 | https://www.avropa.se/globalassets/presentationer/allra-senaste-version-informationsseminarium-itk20251106-002.pdf | Kammarkollegiet | ITK info seminar | 2025-11-06 | 2026-10-29 | ITK area 3 IT-säkerhet 2022-03-10 to 2026-03-09 ("Utgår 2026-03-10") | H |
| 39 | https://www.avropa.se/globalassets/bilagor/1.-aktuella-rao/itk-2020/3.-sakerhet-i-it-och-it-projekt/1.-avropsstod-ao3/prisbilaga---sammanstallning-delomrade-3---sakerhet-it_240229.pdf | Kammarkollegiet | Prisbilaga area 3 | 2024-02-29 | 2026-10-30 (search extract; direct fetch 404) | IT-säkerhetsanalytiker 1,006–1,696 SEK/h | M |
| 40 | https://opsiocloud.com/sv/blogs/vad-kostar-nis2-efterlevnad-en-prisguide-for-svenska-foretag/ | Opsio | NIS2 price guide | 2025–26 | 2026-10-29 | Gap 20k / 45–90k SEK; 10–30k/month; 1,800–3,000 SEK/h | L–M |
| 41 | https://www.legiscope.com/blog/nis2-programvara-sverige.html | Legiscope UAB | NIS2 programvara | 2026 | 2026-10-30 | Platforms 30k–200k SEK/yr | L |
| 42 | https://www.vanta.com/pricing | Vanta | Pricing | 2026 | 2026-10-29 | No public prices | H |
| 43 | https://pyralink.co.uk/insights/vciso-pricing/ ; https://sidechannel.com/blog/the-ultimate-guide-to-vciso-pricing-everything-you-need-to-know | Pyralink; SideChannel | vCISO pricing | 2026 | 2026-10-30 | £497–997/month; $3k–12k/month | L–M |
| 44 | https://soff.se/ ; https://soff.se/om-soff/medlemskap/ | SOFF | Home / Membership | 2026 | 2026-10-29 | Member groups incl. säkerhetsskydd; "500 medlemsföretag" | H |
| 45 | https://soff.se/app/uploads/2025/10/FED-Folder-2026-1.pdf | SOFF | Försvarsentreprenörsdagen'26 | 2025-10 | 2026-10-29 | SMF event; Saab/BAE on supplying primes; "över 400 medlemsföretag" | H |
| 46 | https://www.regeringen.se/contentassets/60fe4c4aa4434d6aa09e628e43248f84/sakerhets--och-forsvarsforetagen.pdf | Regeringen / SOFF | Remissvar (via search) | older | 2026-10-29 | Säkerhetsskydd "betungande… kostsamt"; >100 members, >80 SMEs (dated) | M |
| 47 | https://nordicdefencesector.com/en/article/sweden-proposes-new-defense-export-initiative | Nordic Defence Sector | Sweden proposes new defense export initiative | 2026-03-16 (upd. 03-27) | 2026-10-29 | SOU 2026:16; 300 MSEK to 2030; abolish 15k fee | M–H |
| 48 | https://www.hellios.com/joscar/ | Hellios | JOSCAR | 2026 | 2026-10-29 | 30+ buyers; 6,000+ suppliers | H |
| 49 | https://www.fmv.se/globalassets/dokument/om-fmv/sakerhetsskydd/faq-sua.pdf ; …rutin-vid-upprattande-av-sakerhetsskyddsavtal-i-niva-1.pdf | FMV | FAQ SUA; Rutin nivå 1 (via search) | n/d | 2026-10-29 | ISM implementation; CEO ≠ security officer; company drives process | H |
| 50 | https://www.cyberresilienceact.eu/news/cra-notified-bodies-rules-apply-11-june-2026.html | Independent CRA guide | CRA notified-body rules apply | upd. 2026-09-11 | 2026-10-29 | No notified bodies designated as of 2026-09-08; key dates | M |
| 51 | https://ri.se/en/mnb/news/sweden-has-a-new-notified-body ; https://www.ri.se/en/expertise-areas/expertises/cyber-resilience-act | RISE | Notified body news; CRA page | 2026 | 2026-10-29 | RED cyber notified body; CRA press release 2026-09-09 | M |
| 52 | https://www.intertek.com/resources/webinars/2026/cybersecurity-cyber-resilience-act/ | Intertek | CRA webinar | 2026 | 2026-10-29 | End-to-end testing/certification for CRA | M |
| 53 | https://sbomify.com/pricing/ | sbomify ltd | Pricing | 2026 | 2026-10-29 | $0 / $159/month / Enterprise | H |
| 54 | https://verimu.com/pricing | Verimu | Pricing (via search) | 2026 | 2026-10-29 | €49 / €149 per month | M |
| 55 | https://www.riksdagen.se/sv/dokument-och-lagar/dokument/_HCB1119 | Riksdagen | Kompletterande bestämmelser till EU:s cyberresiliensförordning | 2026 | 2026-10-30 | Swedish CRA implementing bill | H |
| 56 | https://tendium.com/ ; https://tendium.com/pricing | Tendium | Home; Pricing | 2026-10-29 | 2026-10-29 | Products; Light from €125/month | H |
| 57 | https://www.mynewsdesk.com/visma/pressreleases/visma-to-divest-two-of-its-product-areas-within-procurement-software-3122211 | Visma | Divest Opic and TendSign to Mercell | 2020-11-25 | 2026-10-30 | Mercell ~1,000 buyers, ~16,000 suppliers | H |
| 58 | https://www.reco.se/mercell-svenska-ab | Reco | User reviews (via search) | n/d | 2026-10-29 | 12,000 → 22,000 price anecdote | L |
| 59 | http://info.e-avrop.com/ | e-Avrop AB | Homepage | 2021© | 2026-10-30 | Buyer consulting + supplier "anbudskonsulter"; 1,500 buyers | M |
| 60 | https://www.mynewsdesk.com/se/bemannia/subjects/konsultverksamhet | Bemannia | Laholm procurement-consultant framework (via search) | n/d | 2026-10-29 | Staffing firms win procurement-consultant frameworks | M |
| 61 | https://lawinsider.com/sv/contracts/1yUCxYNlRb1 | Konkurrensverket (via LawInsider) | KKO 19-020 | 2019 | 2026-10-29 | 675 SEK/h; 37,968.75 SEK/month | H (dated) |
| 62 | https://www.konkurrensverket.se/contentassets/af16fb7fef854c4ea99a00ba10dee930/tillsynsbeslut-timra_15-0269_15-0273_15-0274_15-0275_16-0587.pdf | Konkurrensverket | Tillsynsbeslut Timrå (via search) | 2016-17 | 2026-10-29 | 1.372 MSEK/year procurement services | H (dated) |
| 63 | https://www.konkurrensverket.se/contentassets/ae57a78af81040978bcaa84427e091bc/17-0643_ansokan-upphandlingsskadeavg-stockholms-kommun.pdf | Konkurrensverket | 17-0643 (via search) | 2017 | 2026-10-29 | 350/780/880 SEK/h ladder | H (dated) |
| 64 | https://www.fortnox.se/produkt/kundkannedom | Fortnox | Kundkännedom | 2026 | 2026-10-29 | Included in Byråpartner 499 SEK/month | H |
| 65 | https://www.spiris.se/redovisningsbyra/byrastod/kyc | Spiris (Visma) | Visma Advisor KYC | 2026 | 2026-10-29 | 199 SEK/client/year | H |
| 66 | https://bjornlunden.com/se/juridik-kunskap/compliance-kyc-aml/ | Björn Lundén | Lundify Compliance | 2026 | 2026-10-29 | 16,650–54,590 SEK/yr; more than 11,000 users; estate agents in segment | H |
| 67 | https://www.trapets.com/ | Trapets | Homepage | 2026 | 2026-10-29 | Segments, customers, AMLR content | M |
| 68 | https://businesswith.se/kyc-system/ | BusinessWith | Jämför KYC-system | 2026 | 2026-10-29 | 18 KYC vendors listed | M |
| 69 | https://www.roaring.io/pricing | Roaring | Pricing | 2026 | 2026-10-30 | From 1,495 SEK/month | H |
| 70 | https://www.faronline.se/dokument/balans/2026/mars/balans_2026030901/ | FAR Balans | Länsstyrelsernas tillsyn 2025 (via search) | 2026-03 | 2026-10-30 | 33 reviewed, 31 sanctioned, 4.6 MSEK | M–H |
| 71 | https://www.faronline.se/dokument/balans/2024/september/balans_2024090301/ | FAR Balans | (via search) | 2024-09 | 2026-10-30 | 191 firms reviewed; >40% sanctioned | M–H |
| 72 | https://regeringen.se/pressmeddelanden/2023/09/okade-bidrag-till-kommunernas-och-regionernas-arbete-med-krisberedskap-och-civilt-forsvar/ | Regeringen | Ökade bidrag… (via search) | 2023-09 | 2026-10-30 | Municipal grants 649 MSEK 2024; 739 MSEK 2025 (budget docs) | M |
| 73 | https://storage.mfn.se/8f119d48-e775-49c7-8f20-dad384315a91/... ; https://storage.mfn.se/3fa67026-.../4c-strategies-tilldelas-tvaarigt-ramavtal... | 4C Strategies via MFN | Framework press releases (via search) | n/d | 2026-10-29 | 150 MSEK FM framework; 48 MSEK (to 100 MSEK) framework | M |
| 74 | https://www.securityworldmarket.com/se/Nyhetsarkiv/sigtuna-kommun-tecknar-avtal-med-cosafe-technology ; …/eslovs-kommun-i-avtal-med-grannkompaniet-om-krishanteringssystem1 | Security World Market | Municipal crisis-platform contracts (via search) | 2018–2020 | 2026-10-30 | Cosafe (Sigtuna, Höganäs); Cocrisis (Eslöv) | M |
| 75 | https://www.sosalarm.se/ (alarmeringsavtal; regeringen remissvar via search) | SOS Alarm | TiB alerting | n/d | 2026-10-30 | Alerts municipal TiB under agreements | M |
