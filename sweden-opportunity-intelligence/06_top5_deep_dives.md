# Deliverable 6: Top five deep-dive reports

**Reference date:** 29 October 2026.

**How to read the numbers:**
- All financial figures are **modelled**. The parameters and formulas are in [`model/models_top20.py`](model/models_top20.py) and [`model/finance.py`](model/finance.py).
- Each model has three scenarios:
  - **Low:** CAC +50%, price −20%, sales cycle +50% with the customer ramp divided by 1.5.
  - **Base**
  - **High:** customer ramp ×1.3.
- Salaries include Swedish employer contributions of 31.42%.
- **No prospects have been contacted.** The "first 20 customers" sections give selection criteria and sourcing methods, not names of interested parties.

**The five:**

| # | Opportunity | Score | Confidence |
|---|---|---|---|
| 1 | NIS2 compliance-as-a-service | 69.0 | High |
| 2 | Säkerhetsskydd & civil-defence retainer | 61.0 | Medium |
| 3 | CRA PSIRT-as-a-service | 61.0 | Medium |
| 4 | Grid-connection consultancy | 60.0 | Low |
| 5 | Stambyte procurement adviser for BRFs | 57.0 | Low |

Opportunities 1, 2 and 3 share buyers, skills and delivery infrastructure, so section 6 treats them as one company with three product lines.

---

## Deep dive 1: NIS2 compliance-as-a-service ("Swedish NIS2 operations partner")

### A. Investment thesis
- **The business:** a fixed-price service with a software backbone that makes a mid-sized regulated organisation compliant with the Swedish Cybersecurity Act and keeps it compliant.
- **The law:** Cybersäkerhetslag (2025:1506) has been in force since 15 January 2026. It requires covered entities to:
  - register with MCF;
  - run documented risk management, supplier-security and incident-handling processes;
  - train management;
  - report incidents within 24 hours (early warning), 72 hours (notification) and one month (final report).
- **Sanctions:** essential entities face fines up to the higher of 2% of global turnover or EUR 10m, and managers can be banned from management roles (W02 §2.1).
- **Who is covered:** about **1,500 companies with 50+ employees plus 310 municipalities and regions** (MCF impact assessment, W10 §0.3).
- **Why now:**
  - Supervision is starting; Transportstyrelsen plans inspections from November 2026 (W10).
  - Kammarkollegiet's state IT-security consultant framework expired 9 March 2026 (W07).
  - IT-security specialists are a national shortage occupation (W05).
  - The proposed CER law (1 Jan 2027) adds resilience duties for the same kinds of entities (W02 §2.19).
- **The gap:** premium consultancies sell by the hour at SEK 1,000–1,700/h on the expired state framework (W07). Software tools (KLASSA, WF ISMS, Isodora) come without the people. Nobody publishes a fixed monthly "named Swedish vCISO + ISMS + incident runbooks + board training" package for municipal energy, water and waste companies or private mid-size entities (W07 Area 1).

### B. Ideal customer profile

| Dimension | Profile |
|---|---|
| Industry | Municipal energy/district heating, municipal water (≥20,000 persons served), waste, ports; private NIS2 entities with 50–500 staff in manufacturing of critical products, digital providers/MSPs and transport |
| Organisation size | 50–500 employees; IT team of 1–10; no CISO |
| Geography | Sweden; start in one region (e.g. Mälardalen or Västsverige) for on-site work |
| Current workflow | IT manager plus an outsourced MSP; Excel or KLASSA for classification; policies outdated; no tested incident runbook; board unaware of personal liability |
| Decision-maker | IT manager or säkerhetschef |
| Economic buyer | CEO/CFO (municipal company); kommundirektör or IT director (municipality) |
| Buying trigger | MCF registration; supervisory letter or inspection notice; board training duty; an incident at a peer; customer or supplier questionnaires |
| Approximate budget | Gap analysis SEK 45–90k; ongoing SEK 10–30k/month (Opsio public prices, W07 [L–M]); traditional projects SEK 450k–1.7m (Isodora claim, W07 [L]) |
| Typical objections | "Our MSP handles it"; "KLASSA covers it"; "no budget, it must fit within existing frames"; "you have no references"; "procurement rules" |

### C. Business model
- **Product and service:**
  1. NIS2 gap analysis: fixed price, 3–4 weeks.
  2. 90-day implementation: ISMS documents, risk register, supplier-security process, incident runbooks with reporting templates for MCF/CSIRT, and a management-training certificate.
  3. Monthly retainer: a named vCISO about 10–12 h/month, an annual internal audit, a tabletop exercise, supplier reviews and board reporting.
- **Revenue streams:**
  - one-off implementation, SEK 60–150k;
  - recurring retainer, SEK 12–25k/month;
  - add-ons: incident-response readiness, supplier assessments, CER risk assessment from 2027, CRA PSIRT (Deep dive 3).
- **Pricing hypothesis:** gap analysis SEK 60k; implementation SEK 90k; retainer SEK 18k/month. A two-year deal is about SEK 0.52m, **under the SEK 700k direct-award limit** (W10 §0.1).
- **Delivery model:** a senior consultant pool supported by a thin platform for evidence collection, templates and reporting workflows. Delivery is remote-first with on-site workshops.
- **Gross-margin drivers:** template reuse; AI drafting of policies (reviewed by humans); utilisation of the vCISO pool; standardised scope.
- **Expansion:** CER compliance (2027); CRA product security; säkerhetsskydd (with a cleared hire); a supplier baseline offered free as lead generation (#2); ISO 27001 certification readiness.

### D. Minimum viable product
- **Essential:**
  - a Swedish NIS2 control library mapped to SFS 2025:1506, the förordning, MCFFS 2026:1 and Implementing Regulation 2024/2690;
  - a gap-analysis questionnaire and scoring report;
  - a policy and runbook template pack;
  - incident-reporting checklists with timers;
  - the management-training deck, quiz and certificate;
  - a risk register in a shared workspace;
  - a monthly status report.
- **Not needed yet:** an automated cloud-evidence platform, SOC/MDR, multi-framework mapping, self-serve SaaS.
- **Minimum architecture:**
  - a document repository (M365/SharePoint or a hosted wiki);
  - a structured database for controls, risks and suppliers (Postgres plus a simple web UI);
  - a templating engine;
  - read-only Microsoft Graph and Entra integration (MFA status, admin accounts) as the first automated evidence;
  - EU/Swedish hosting; client data segregated.
- **Security safeguards:** ISO 27001-aligned internal controls from day one; NDA and data-processing agreements; no client secrets stored; MFA everywhere; liability insurance (konsultansvar plus cyber).

### E. Go-to-market
- **First 20 prospects, selection criteria:**
  1. In scope under Cybersäkerhetslagen (sector plus size), confirmed from public sector lists and annual reports.
  2. No named CISO or information-security manager on LinkedIn or the company website.
  3. Within 2 hours' travel.
  4. 50–500 employees.
  5. Signs of activity, such as a security job ad (indicating budget but no hire yet) or a board minute mentioning NIS2.
- **Sourcing:**
  - SCB/Bolagsverket lists of municipal companies in SNI 35 (energy), 36–37 (water) and 38 (waste);
  - MCF sector guidance;
  - municipal annual reports;
  - Svenskt Vatten and Energiföretagen member lists.
- **Outreach:**
  - founder-led email and phone to the IT manager and CEO, offering a free 45-minute "NIS2 board briefing";
  - webinars through regional industry associations;
  - content in Swedish: a public guide to MCFFS 2026:1 and a liability guide for managers.
- **Messaging:** "Fixed price. Named Swedish vCISO. Board-ready in 90 days. Fits under the direct-award limit."
- **Demonstration:** a live run-through of the gap-analysis report on an anonymised example, plus the incident-reporting runbook.
- **Pilot pricing:** first 3 clients get the gap analysis at SEK 40k (discounted from SEK 60k) in exchange for a reference.
- **Sales cycle:** municipal companies 2–4 months; municipalities 4–6 months; private companies 1–3 months.
- **Conversion assumptions (to be measured):**

| Stage | Assumed conversion |
|---|---|
| Outreach → briefing | 15% |
| Briefing → paid gap analysis | 30% |
| Gap analysis → implementation | 60% |
| Implementation → retainer | 80% |

### F. Financial model (modelled)

| Scenario | Revenue Y1 | Revenue Y2 | Revenue Y3 | Retainer clients at M36 | Break-even month | Peak funding need |
|---|---|---|---|---|---|---|
| Low | SEK 0.6m | SEK 3.2m | SEK 6.0m | 33 | Not within 36 m | SEK 5.2m |
| Base | SEK 1.6m | SEK 6.4m | SEK 11.5m | 50 | 19 | SEK 1.6m |
| High | SEK 2.1m | SEK 8.3m | SEK 14.9m | 65 | 16 | SEK 1.3m |

- **Base assumptions:**
  - ARPA SEK 18k/month plus SEK 90k setup;
  - gross margin 62%;
  - CAC SEK 55k (post-review);
  - sales cycle 3 months;
  - 1.0 / 2.0 / 2.5 new clients per month in years 1 / 2 / 3;
  - churn 1.8%/month;
  - fixed costs: 2 founders in Y1, plus one specialist in Y2 and another in Y3.
- **Break-even condition:** Y2 fixed costs are about SEK 0.215m/month. At SEK 18k/month and 62% gross margin, each retainer client contributes about SEK 11.2k/month, so about **20 retainer clients** break even. That assumes acquisition costs are roughly offset by the gross profit on setup fees, which holds at 2 new clients/month (2 × 55k CAC vs 2 × 90k × 62%) [derived].
- **Sensitivity:** the model is most sensitive to sales-cycle length; +50% pushes break-even to month 31. A 20% price cut delays break-even to month 23.

### G. Risks

| Type | Risk | Mitigation |
|---|---|---|
| Commercial | MSPs (Atea, Advania, Tietoevry) bundle NIS2 | Partner with smaller MSPs, which lack the compliance capability |
| Commercial | Public buyers fund NIS2 "within existing budgets" | Target municipal companies with their own P&L first |
| Regulatory | Aggregation of same-kind purchases breaches the SEK 700k limit | Keep 2-year contracts under the limit; pursue regional frameworks |
| Technical | Liability for poor advice during an incident | Professional indemnity insurance; scope letters; no operational control of client systems |
| Operational | Hiring senior security people (shortage) | Founder delivery in Y1; a pool of independent consultants; certification of juniors |
| Competitive | AI-generated ISMS commoditises documents | Sell outcomes and accountability (named vCISO, supervisory-inspection support), not documents |

### H. Differentiation
1. A fixed, published price that fits procurement rules.
2. A Swedish-native control library mapped to MCF regulations.
3. A named, accountable vCISO.
4. Incident-reporting runbooks rehearsed in tabletop exercises.
5. A clear upgrade path to CER, CRA and säkerhetsskydd. Hourly consultancies and software-only tools can't offer this combination at this price.

### I. Validation experiment
- **Hypothesis:** in-scope municipal companies and mid-size NIS2 entities will pay a new provider SEK 40–60k for a fixed-price NIS2 gap analysis within 45 days of first contact.
- **Success threshold:** ≥3 signed paid orders out of ≥40 qualified prospects contacted (about 7.5%), and ≥10 briefings held.
- **Cost:** about SEK 60k (founder time valued at cost, plus travel and a webinar).
- **Evidence:** signed orders or purchase orders, written refusals with reasons, and logged objections.
- **Duration:** 45 days.
- **Go:** ≥3 paid orders. **Pivot:** 1–2 paid orders with a consistent objection (for example "our MSP covers it"); try MSP partnering. **No-go:** 0 orders, or more than half of prospects say an existing provider covers it.

---

## Deep dive 2: Säkerhetsskydd & civil-defence retainer (founder-gated)

### A. Investment thesis
- **The demand:**
  - Sweden is rebuilding total defence. Municipalities received SEK 649m (2024) and 739m (2025) in state preparedness grants (W07).
  - A civil-defence package of about SEK 12bn runs over 2026–28 (W01).
  - Säkerhetsskyddslag changes (SFS 2026:764) expand supervision (W02 §2.19).
  - Uppsala alone advertised a SEK 100m framework (W07).
- **The obstacle, after the adversarial review:** the opening is **narrower than the money suggests**.
  - The national Adda framework is closed until Feb 2030.
  - Direct awards cap contracts at SEK 700k total.
  - Each client requires a security-protection agreement and staff vetting.
  - The 2027 notification duty is a one-off (W10 §0.2–0.5).
- **Where it works:** as a business for **founders who already have clearances and municipal or defence references**, or as a cleared product line added to Deep dive 1 in year 2.

### B. Ideal customer profile
- **Who:** small and mid municipalities (10–60k inhabitants) without a full-time säkerhetsskyddschef; municipal energy, water and port companies classed as säkerhetskänslig verksamhet; regional public transport.
- **Buyers:** the decision-maker is the säkerhetschef or beredskapssamordnare; the economic buyer is the kommundirektör or company CEO.
- **Trigger:** the MCF grant cycle, the new supervision powers, staff turnover in the single preparedness role, and exercise requirements.
- **Budget:** part of the SEK ~2.2m average grant per municipality, which is largely spent on salaries and capex (W10).
- **Objections:** "we buy from Adda framework suppliers"; "you lack references"; "we hire our own coordinator".

### C. Business model
- **Offer:** a retainer of SEK 15–25k/month (annual säkerhetsskyddsanalys, continuity and crisis-management plans, two exercises, supplier security-agreement support) plus exercise fees.
- **Contract shape:** 2-year contracts under the direct-award limit.
- **Gross margin:** limited by scarce cleared seniors.
- **Expansion:** subcontracting to framework holders; private säkerhetskänsliga companies (outside LOU); defence-SME supplier readiness (#6).

### D. Minimum viable product
- **Essential:** a cleared senior adviser; templates (säkerhetsskyddsanalys, krisledningsplan); an exercise playbook; secure document handling, which **cannot be ordinary SaaS** for classified material.
- **Not needed:** planning software (#5).

### E. Go-to-market
- **First-20 criteria:** municipalities of 10–60k inhabitants that are **not** party to a large-city framework, plus municipal utilities; checked for existing preparedness staffing in municipal organisation charts.
- **Channels:**
  - subcontracting offers to Adda area-7 holders (the supplier list still has to be obtained);
  - county administrative board (länsstyrelse) preparedness networks.
- **Pilot:** a fixed-price "exercise + plan review" for SEK 80k.
- **Sales cycle:** 6–9 months, plus vetting.

### F. Financial model (modelled, post-review parameters)

| Scenario | Revenue Y1 | Revenue Y2 | Revenue Y3 | Clients at M36 | Break-even month | Peak funding |
|---|---|---|---|---|---|---|
| Low | SEK 0.03m | SEK 2.1m | SEK 4.9m | 22 | Not within 36 m | SEK 7.5m |
| Base | SEK 0.5m | SEK 4.6m | SEK 9.6m | 34 | 31 | SEK 3.5m |
| High | SEK 0.6m | SEK 6.0m | SEK 12.5m | 45 | 23 | SEK 3.0m |

**Weak unit economics, stated plainly:**
- Y3 EBIT is about SEK 0.07m in the base case and negative under every sensitivity.
- Underlying parameters: CAC SEK 90k, sales cycle 7 months, churn 2.5%/month (re-buying after 2-year direct awards).

### G. Risks
- **Regulatory:** vetting delays and Säpo/supervisory objections.
- **Commercial:** framework capture until 2030.
- **Operational:** key-person dependency on cleared staff.
- **Competitive:** Combitech, Vesper, 4C Strategies and Securitas.

### H. Differentiation
A small-municipality focus, fixed price and exercise-led delivery. All of this is credible **only** with references.

### I. Validation experiment
- **Hypothesis:** ≥3 of 20 small municipalities or municipal companies will accept a direct-award offer for an SEK 80k exercise-plus-plan-review from the team.
- **Threshold:** 3 written acceptances within 60 days.
- **Cost:** about SEK 40k.
- **No-go:** fewer than 3 acceptances, **or** no cleared senior adviser can be recruited.

---

## Deep dive 3: CRA PSIRT-as-a-service (product security for SME manufacturers)

### A. Investment thesis
- **The law:** the EU Cyber Resilience Act applies in full from **11 December 2027**. Every manufacturer selling hardware or software with digital elements in the EU must:
  - follow secure development practices;
  - maintain SBOMs;
  - handle vulnerabilities for the support period (at least 5 years);
  - report actively exploited vulnerabilities to ENISA within 24 hours. This duty has been live since 11 September 2026.
- **The market gap:**
  - No CRA notified body had been designated EU-wide as of September 2026 (W07 Area 4).
  - Swedish SME machine builders and IoT makers lack product-security teams; only 52% of manufacturers even have IT-security policies (W03 §4).
  - Tooling exists (SBOM tools at EUR 49–149/month), but outsourced **people-run PSIRT** does not exist in Sweden (W07).

### B. Ideal customer profile
- **Who:** Swedish manufacturers with 20–500 employees whose products contain firmware, software or network connectivity: machinery, building automation, medtech-adjacent, energy equipment, consumer IoT.
- **Buyers:** the decision-maker is the CTO or R&D manager; the economic buyer is the CEO.
- **Triggers:** CE-marking planning for 2027; requests from distributors and large customers; the first vulnerability report.
- **Budget:** unknown. Validate whether it is SEK 100–300k/year.
- **Objections:** "we'll handle it in 2027"; "our SBOM tool covers it"; "the test house does it".

### C. Business model
- **Offer:** a readiness assessment (SEK 80–150k) plus a PSIRT retainer (SEK 10–30k/month per product line).
- **The retainer covers:** vulnerability intake, triage, ENISA reporting, SBOM monitoring, security advisories and annual secure-development training.
- **Gross margin:** the margin driver is automated SBOM diffing and triage.
- **Contract shape:** long contracts, because the support period is at least 5 years.
- **Expansion:** the Machinery Regulation (Jan 2027); RED cyber; other EU markets, since the CRA is EU-wide (international potential).

### D. Minimum viable product
- **Essential:** a CRA gap-assessment framework; an SBOM pipeline built on open source (Syft, Dependency-Track); a vulnerability intake and triage workflow; ENISA reporting templates; a CVD policy template.
- **Architecture:** a hosted Dependency-Track instance per client (isolated), a ticketing system and a customer portal.
- **Not needed:** firmware binary analysis or a certification lab.

### E. Go-to-market
- **First-20 criteria:** Swedish product makers with connected products, 20–500 employees, no product-security role on LinkedIn, exporting to the EU.
- **Sourcing:**
  - Teknikföretagen member lists;
  - SCB SNI 26–28 firms with employees;
  - trade-fair exhibitor lists (public).
- **Channels:** cross-selling to manufacturing clients of Deep dive 1; partnerships with test houses that lack PSIRT services.
- **Timing:** sell from Q2 2027.

### F. Financial model (modelled)

| Scenario | Revenue Y1 | Revenue Y2 | Revenue Y3 | Clients at M36 | Break-even month | Peak funding |
|---|---|---|---|---|---|---|
| Low | SEK 0.2m | SEK 2.2m | SEK 4.4m | 26 | Not within 36 m | SEK 5.8m |
| Base | SEK 0.6m | SEK 4.4m | SEK 8.5m | 40 | 23 | SEK 2.3m |
| High | SEK 0.8m | SEK 5.8m | SEK 11.1m | 53 | 19 | SEK 1.9m |

### G. Risks
- **Regulatory:** an omnibus delay of the CRA.
- **Commercial:** tool-only box-ticking.
- **Competitive:** test houses (Intertek Semko, RISE) bundling PSIRT; ONEKEY.
- **Technical:** liability for missed 24-hour reports. Mitigate with clear RACI and insurance.

### H. Differentiation
A Swedish-speaking human PSIRT with an SLA, plus the evidence pack customers need for conformity. As a product line of the NIS2 business it shares security staff and brand.

### I. Validation experiment
- **Hypothesis:** ≥3 of 25 qualified Swedish product makers will pay SEK 50k+ for a CRA readiness assessment before June 2027.
- **Duration and cost:** 60 days; about SEK 50k.
- **No-go:** fewer than 2 paid, or more than half say their tool or test house covers PSIRT.

---

## Deep dive 4: Grid-connection consultancy (founder-gated)

### A. Investment thesis
- **The problem:** electrification of logistics depots, industrial sites and battery parks runs into connection queues and capacity refusals (W03 §5).
- **Why now:** Svenska kraftnät proposes moving from first-come-first-served to a **"ready-first"** allocation (SvK report, Apr 2026, W10), which rewards complete, well-engineered applications.
- **Buyers:** private, so no public-procurement law applies, and delays cost them a lot.
- **Incumbents:** Sweco, Rejlers and AFRY work hourly.
- **Constraint:** credible only with power-systems engineers on the team.

### B. Ideal customer profile
Logistics/depot owners, BESS developers, industrial expansions and housing developers with large loads. The buyer is a project or energy manager or the developer's CEO. The trigger is a connection request or a refusal. Budgets run to SEK 100–300k per study (assumption; Svenska kraftnät's SEK 100k investigation fee is an anchor, W08 §6).

### C. Business model
- **Offer:** application preparation, a flexible-connection design (curtailment, storage), tariff optimisation and negotiation support.
- **Pricing:** project fees of SEK 80–200k (assumption); a success fee on accelerated connection.
- **Expansion:** a capacity pre-check tool for DSOs (#37).

### D. Minimum viable product
A power-systems engineer, load-flow tools (e.g. PowerFactory or open-source pandapower), an application template library and DSO process maps.

### E. Go-to-market
- **First-20 criteria:** BESS projects with county board approval (130 approved in 2021–25, W03 §5 [L]); depot electrification projects announced publicly; developers active in grid-constrained regions.
- **Channels:** Power Circle network, BESS developer associations, logistics property owners.

### F. Financial model (modelled, project business)

| Scenario | Revenue Y1 | Revenue Y2 | Revenue Y3 | Break-even month | Peak funding |
|---|---|---|---|---|---|
| Low | SEK 0.7m | SEK 1.9m | SEK 2.3m | Not within 36 m | SEK 3.5m |
| Base | SEK 1.6m | SEK 3.6m | SEK 4.3m | 25 | SEK 1.0m |
| High | SEK 2.1m | SEK 4.7m | SEK 5.6m | 13 | SEK 0.8m |

This is a modest consultancy, not a venture-scale business.

### G. Risks
DSOs decide capacity, and consultants cannot create it. Volume evidence is weak (the queue figure is [L]). The business depends on key persons.

### H. Differentiation
A productised, fixed-scope application package tuned to ready-first criteria.

### I. Validation experiment
- **Hypothesis:** ≥2 of 15 BESS or depot developers will commission a paid application study within 60 days.
- **No-go:** fewer than 2, **or** no power-systems engineer on the team.

---

## Deep dive 5: Stambyte/renovation procurement adviser for BRFs (weak economics)

### A. Investment thesis
- **The problem:**
  - BRFs face pipe replacements (stambyten) costing **SEK 250–500k per apartment** (W03 §2, [L]).
  - Owners are anxious about association finances: 31% worried, up 15 points since 2022 (W03 §2).
  - Volunteer boards lack the expertise to specify, tender and control contractors.
- **The offer:** an independent fixed-fee adviser covering condition survey, tender documents, contractor comparison and member communication, which could save members far more than it costs.
- **The problem with the business:** the evidence is thin and the model is project-based.

### B. Ideal customer profile
BRFs with 30–150 apartments, buildings from 1950–1975, and a stambyte in their maintenance plan within 3 years. The decision-maker is the board, and the economic buyer is the members' meeting (stämma). The trigger is the maintenance plan or a water-damage event. The budget is about 1–2% of project cost.

### C. Business model
- **Pricing:** a fixed fee of SEK 100–400k per project; optional construction-phase control.
- **Repeat revenue:** low.

### D. Minimum viable product
A building engineer, a condition-survey protocol, tender templates (AB/ABT 06), a contractor database and member-communication templates.

### E. Go-to-market
- **Criteria:** BRFs whose public annual reports mention stambyte; boards in Bostadsrätterna networks.
- **Channels:** BRF forums, Bostadsrätterna, property managers that lack the expertise.

### F. Financial model (modelled)

| Scenario | Revenue Y1 | Revenue Y2 | Revenue Y3 | Break-even | Peak funding |
|---|---|---|---|---|---|
| Low | SEK 0.3m | SEK 1.3m | SEK 1.7m | No | SEK 4.1m |
| Base | SEK 0.8m | SEK 2.4m | SEK 3.1m | **No (within 36 m)** | SEK 2.3m |
| High | SEK 1.0m | SEK 3.1m | SEK 4.1m | Month 25 | SEK 1.6m |

**Weak unit economics:** a CAC of SEK 40k per project on top of lumpy, non-recurring fees does not cover two salaries until volume exceeds about 1.3 projects per month.

### G. Risks
Local byggkonsulter already serve this market. Trust and liability. Lumpy project flow.

### H. Differentiation
Fixed fee, member communication and benchmarking data across projects.

### I. Validation experiment
- **Hypothesis:** ≥2 of 30 BRFs planning a stambyte will sign a paid condition-survey-plus-tender package within 90 days.
- **No-go:** fewer than 2.

---

## 6. How the top three fit together

Opportunities 1, 2 and 3 can form one company: a **regulated-resilience services firm** with a single brand, one pool of senior security people and one control-library platform.

| Year | Product line | Customers |
|---|---|---|
| Y1 | NIS2 operations partner | Municipal companies and mid-size private entities |
| Y2 | CRA PSIRT | Manufacturing clients and new product makers, ahead of Dec 2027 |
| Y2–3 | CER resilience assessments | The same customer base |
| Y2–3 | Säkerhetsskydd services | Only once a cleared senior adviser is hired |

Deliverable 7 recommends this sequencing.
