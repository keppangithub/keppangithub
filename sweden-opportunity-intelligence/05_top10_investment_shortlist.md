# Deliverable 5: Top 10 investment shortlist

**Reference date:** 29 October 2026. The ranking below is **after** the adversarial review. The full review, which answers all twelve skeptic questions for each of the original top 10, is in [research/10_adversarial_review.md](research/10_adversarial_review.md) (W10). Score changes and their rationale are in [model/adversarial.py](model/adversarial.py) and the spreadsheet sheet "Adversarial changes".

**Read this first:**
- There is **one clear leader (#1, NIS2 compliance-as-a-service, 69.0)**.
- After it, the field is tight: ranks 2–10 lie within 7 points.
- Several of them depend on who the founders are (security clearance, power-systems engineering).
- Use the evidence-confidence column alongside the score.

---

## 1. Comparative ranking

| Rank | Pre-review rank | ID | Opportunity | Score (pre) | Confidence | Indep. sources | Rev Y3 (model) | EBIT Y3 (model) | Break-even | Peak funding | Largest unverified assumption | Why the ranking could be wrong |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 1 | NIS2 compliance-as-a-service (fixed-price ISMS + Swedish vCISO) | **69.0** (74.5) | High | 7 | SEK 11.5m | SEK 1.9m | Month 19 | SEK 1.6m | That buyers pay a new brand for what their IT partner or KLASSA covers "well enough" | Atea, Advania and Tietoevry bundle NIS2 into MSP contracts; price compression from AI-generated ISMS documents |
| 2 | 1 | 4 | Säkerhetsskydd & civil-defence retainer | 61.0 (76.0) | Medium | 6 | SEK 9.6m | SEK 0.1m | Month 31 | SEK 3.5m | That an unreferenced company can enter municipal säkerhetsskydd work | Adda area 7 closed until 2030; per-client vetting; SEK 700k direct-award limit |
| 3 | 4 | 7 | CRA PSIRT-as-a-service + SBOM | 61.0 (63.5) | Medium | 4 | SEK 8.5m | SEK 0.8m | Month 23 | SEK 2.3m | That SMEs outsource PSIRT rather than buy a EUR 49/month tool | An omnibus delay of Dec 2027; test houses bundling |
| 4 | 9 | 38 | Grid-connection consultancy (C&I, depots, BESS) | 60.0 (59.0) | Low | 2 | SEK 4.3m | SEK 0.3m | Month 25 | SEK 1.0m | That the founders hold power-systems credentials | Weak evidence on volume; Sweco and Rejlers dominate |
| 5 | 13 | 30 | Stambyte/renovation procurement adviser for BRFs | 57.0 (58.0) | Low | 2 | SEK 3.1m | **−SEK 0.4m** | Not within 36 m | SEK 2.3m | That boards pay for independent advice | Local byggkonsulter already serve this; project lumpiness |
| 6 | 14 | 27 | BRF compliance & maintenance-plan copilot | 56.5 (57.5) | Medium | 5 | SEK 4.2m | SEK 0.7m | Month 27 | SEK 3.0m | That boards pay separately from their manager or app | Boappa can add the feature cheaply |
| 7 | 15 | 16 | Acquire-and-automate micro accounting roll-up | 55.5 (57.0) | Medium | 4 | SEK 17.9m | SEK 4.8m | Month 16 (operating) | SEK 8.0m incl. acquisitions | Buying at about 1.0–1.3x revenue and retaining clients | PE acquirers bid up prices; the model treats acquisitions crudely |
| 8 | 12 | 17 | Vertical AI-native bookkeeping for construction trades | 55.5 (58.0) | Low | 2 | SEK 5.9m | SEK 0.3m | Month 28 | SEK 2.5m | That vertical focus lowers acquisition cost (CAC) | Crowded bureau market; staff-heavy margins |
| 9 | 3 | 6 | Defence-SME supplier onboarding | 54.0 (66.0) | Medium | 5 | SEK 5.5m | −SEK 0.1m | Month 32 | SEK 2.5m | That SMEs invest before they have an order | Demand appears only when a contract does (FMV: the customer initiates the security agreement) |
| 10 | 18 | 9 | AML/KYC compliance kit, as a done-for-you AML function | 54.0 (54.0) | Medium | 3 | SEK 2.7m | SEK 0.1m | Month 30 | SEK 2.8m | That a service layer beats bundled tools | Saturated software market (Fortnox, Lundify with 11,000+ users) |

All revenue, EBIT and funding figures are **modelled** (see [output/tables.md](output/tables.md)), not observed.

---

## 2. Significant ranking changes after the adversarial review

| Opportunity | Move | Why |
|---|---|---|
| #4 Säkerhetsskydd retainer | 1 → 2 (−15 pts) | The headline money is real but largely **capex and in-house salaries**. The national Adda framework is **closed to new suppliers until Feb 2030**. Direct awards are capped at **SEK 700k total contract value**, so only ~2-year retainers fit. Each client requires its own security-protection agreement and vetting. The 1 Jan 2027 notification duty is a one-off. |
| #1 NIS2 compliance | 2 → 1 (−5.5 pts) | MCF's own impact assessment gives **~1,500 companies + 310 municipalities/regions**, not 5–8k. KLASSA (410 organisations, NIS2-mapped) and fixed-price packages like Opsio's narrow the gap. It still has the law in force, contracts that fit the direct-award limit, and low capital, so it remains the leader. |
| #6 Defence-SME onboarding | 3 → 9 (−12 pts) | FMV says the security-protection agreement is **initiated by the customer**, so SMEs pay only when a contract exists. Subsidised substitutes exist (Business Sweden SEK 300m, Vinnova). |
| #13 Practice OS | 5 → out (−14.5 pts) | Fortnox's whole Byråpartner suite is **SEK 499/month** with case management and KYC. The backlash is about price, not a wish for another tool. |
| #15 Succession marketplace | 6 → out (−11 pts) | Bolagsplatsen has only 13 listings for accounting firms, and most transfers are client books worth under SEK 1m. Folded into #16 as its sourcing engine. |
| #21 Procurement support | 7 → out (−12 pts) | A SEK 40k/month retainer breaches the SEK 700k limit within 2 years. Neighbouring municipalities share staff instead (Timrå). |
| #22 Bid writing | 8 → out (−10 pts) | Tendium's AI bid studio, from EUR 125/month, commoditises the work. |
| #2 Supplier attestation | 10 → out (−11.5 pts) | No buyer mandate. KLASSA or MCF could publish a free baseline. Kept as a free lead-generation feature of #1. |
| #38 Grid connection | 9 → 4 (+1 pt) | Private buyers face no public-procurement (LOU) rules, delay is expensive, and Svenska kraftnät's "ready-first" queue reform rewards prepared applications. |
| #30, #27, #16, #17, #9 | Promoted | They rose by default, after the same skeptic lens was applied by the lead analyst (see the note in model/adversarial.py). They are not as well evidenced as ranks 1–3. |

**The lesson:** the original ranking rewarded "public money exists" without discounting **how that money may be spent**. Procurement law, closed frameworks and security-protection vetting are the binding constraints in Swedish B2G markets.

---

## 3. Short profiles

### 1. NIS2 compliance-as-a-service: KEEP (leader)
- **Evidence:**
  - Cybersäkerhetslag (2025:1506) has been in force since 15 Jan 2026, with fines up to 2% of turnover or EUR 10m and mandatory management training (W02 §2.1).
  - About 1,500 companies plus 310 public bodies are in scope (W10 §0.3).
  - IT-security specialists are in shortage (W05).
  - Kammarkollegiet's state IT-security framework expired 9 Mar 2026 (W07).
  - Transportstyrelsen supervision starts Nov 2026 (W10).
- **Economics (modelled):**
  - Gap analysis about SEK 90k, then a retainer of SEK 18k/month at 62% gross margin.
  - Break-even month 19; peak funding SEK 1.6m.
  - In the combined downside, Y3 EBIT is −SEK 1.5m. The model is sensitive to sales-cycle length.
- **Limitations:**
  - Pricing benchmarks come from one vendor (Opsio, low reliability).
  - No customer interviews.
- **Downside risks:** MSP bundling; AI commoditisation of ISMS documents; municipal budgets "within existing frames".

### 2. Säkerhetsskydd & civil-defence retainer: DOWNGRADE (founder-gated)
- **Evidence:** SEK 739m in state grants to municipalities (2025); Uppsala's SEK 100m framework; säkerhetsrådgivare in shortage (W07, W05).
- **Economics:**
  - Break-even month 31; peak funding SEK 3.5m.
  - Y3 EBIT is only about SEK 0.07m in the base case and **negative in Y3 under every sensitivity** ([output/tables.md](output/tables.md)).
- **When it works:** only with founders who already hold clearances and references, or as a subcontractor to framework holders. Otherwise it is best run as a later product line of #1.

### 3. CRA PSIRT-as-a-service: KEEP (timing play)
- **Evidence:**
  - CRA reporting has been live since 11 Sep 2026; full application is 11 Dec 2027.
  - No notified body exists EU-wide.
  - About 1,500 machinery firms with employees (W02, W07, W03).
- **Economics:** break-even month 23; LTV/CAC is high because product-security contacts rarely switch.
- **Key risk:** demand starts late. Sell from Q2 2027. Best positioned as the **second product line of #1** for manufacturing clients.

### 4. Grid-connection consultancy: KEEP (if the founders have the credentials)
- No procurement law applies, delays are expensive, and queue reform helps.
- Evidence of volume is thin (the queue figure is [L]).
- The project model is lumpy: break-even month 25.

### 5. Stambyte procurement adviser: WEAK UNIT ECONOMICS
- **No break-even within 36 months** in the base case.
- The pain is high (SEK 250–500k per apartment), but the business is project-based, has no recurring revenue and competes with local consultants.
- Keep it on the list only as an evidence-gathering bet.

### 6. BRF compliance copilot
- It is a real gap: there is no cross-domain compliance calendar.
- But willingness to pay per BRF is about SEK 4–14k/year, and Boappa (churn under 1.5%) can copy the feature.
- Best as a partnership or acquisition target, not a venture.

### 7. Micro accounting roll-up
- It has the highest modelled Y3 revenue, but it needs about **SEK 6–8m of acquisition capital**.
- It competes with PE buyers.
- The modelling of acquisitions is crude; a proper deal model is needed before relying on it.

### 8. Vertical bookkeeping for trades
- A solid service business. It is labour-linear and its unit economics are only modest.

### 9. Defence-SME onboarding
- The need is thin but real, and arises only at the moment of a contract.
- Fold it into #1 or #4 as a "supplier readiness" package.

### 10. Done-for-you AML function
- Supervisory fines are real: 31 of the 33 accounting firms inspected in 2025 were sanctioned (W07).
- AMLR applies from 10 Jul 2027.
- The software is saturated, so only a service wrapper is viable.

---

## 4. Opportunities to avoid, and why

| Avoid | Evidence |
|---|---|
| CSRD/ESG reporting for SMEs (#19) | Omnibus I cut scope by about 70–90%; the Swedish bill raises the threshold to about SEK 5bn turnover (W02 §2.5, W04 §24) |
| Platform staffing / gig labour | Coople exited the UK (1 Jan 2026), Gigstr went bankrupt, Jobandtalent posted about −€120m net (W06) |
| Capital-heavy B2C energy installers | Aira: SEK 1.38bn loss on SEK 1.35bn sales, going-concern doubt (W06); 196 solar-installer bankruptcies [L] (W03) |
| EV battery-health certificates (#41) | Dekra captured MRF and Bilia (W09 §5) |
| Municipal waste-system software (#26) | EDP dominance; 10-year LOU contracts (W09 §3) |
| AML/KYC *software* (#9 as SaaS) | Bundled at SEK 199/client/yr (Spiris) and inside the SEK 499/month Fortnox suite (W07 Area 6) |
| Accounting practice-management software (#13) | Fortnox Byråpartner at SEK 499/month includes it (W09 §1) |
| Digital product passports (ESPR) | No product delegated act adopted; obligations from about 2028–29 at the earliest (W02 §2.11) |
| Restaurant/hospitality SaaS (#49, #18) | Most bankruptcy-prone sector (2.8%); distressed buyers (W04 §14) |
