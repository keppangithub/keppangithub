# 10: Adversarial investment-committee review of the top 10

Reference date: 29 Oct 2026. Reviewed 30 Oct 2026. Reviewer: independent skeptical analyst (red team).
Inputs: `model/opportunities.py` (scores), `model/models_top20.py` (financial assumptions), research files W01–W09. I used 15 web searches and 3 fetches.

**Conventions.** `[W07 Area 2]` points to a section of a research file. URLs are given for facts I checked on the web. **[inference]** marks my own judgement. Scores are on the 0–10 scale of `opportunities.py`, and the weights come from `CRITERIA`.

---

## 0. Findings that cut across several opportunities (read first)

1. **The direct-award limit (direktupphandlingsgräns) is SEK 700,000 in 2026**, the same as last year. It counts the **whole contract value over its duration**, and the buyer must add up purchases of the same kind ([Konkurrensverket, Analys i korthet 2026:1](https://www.konkurrensverket.se/globalassets/dokument/informationsmaterial/rapporter-och-broschyrer/analys-i-korthet/analys-i-korthet_2026-1.pdf); [Mercell, Jan 2026](https://info.mercell.com/en/blog/new-procurement-thresholds-take-effect-on-1-january-2026/)). This caps the retainers the financial model assumes:
   - id 4 at SEK 25k/month plus a 60k set-up fee: a 2-year deal is SEK 660k, just under the limit. A 3-year deal is not.
   - id 21 at SEK 40k/month: SEK 960k over 2 years, **over the limit**, so the buyer must run a tender or use a framework.
   - id 1 at SEK 18k/month plus a 90k set-up fee: SEK 522k over 2 years, which fits.
   - Every direct-awarded contract ends after about 2 years and has to be re-bought. That makes the model's churn of 1.0–1.2%/month (about 13%/yr) **too optimistic for public customers** [inference].
2. **New entrants cannot join Adda's "Säkerhetslösningar konsulter 2025" during its term.** It is a ranked framework agreement, not a dynamic purchasing system (DIS). It runs from 16 Feb 2026 to 15 Feb 2030 with no extension. Area 7 (crisis preparedness and total defence) has up to 10 suppliers. Call-offs **up to SEK 150k go to the supplier ranked #1**, and larger ones go to a renewed competition (FKU) among the framework suppliers. The award was decided "till största del av kvalitet d v s erfarenhet" (mostly on quality, meaning experience), judged from **reference assignments** ([Adda avropsvägledning](https://www.adda.se/globalassets/2.-upphandling-ramavtal/2.-fastighetsforvaltning/fastighetsnara-tjanster/sakerhetslosningar-konsulter-2025/avropsvagledning---sakerhetlosningar-konsulter-2025.pdf), pp. 2–4). I could not find the supplier list. Even so, the Adda route that id 4's model basis relies on is **closed to a new company until 2030**. Even for a framework supplier, the ≤150k ranked route only helps whoever is ranked #1. The basis line in `models_top20.py` ("Retainer below Adda area-7 direct call-off ceiling of SEK 150k") is wrong twice over. The retainer is SEK 300k/yr, not under 150k, and the company would not be on the framework at all.
3. **The NIS2 entity count is closer to the low end.** MCF's own impact assessment for MCFFS 2026:1 cites the government estimate of **about 1,500 companies (about 500,000 employees) plus 310 municipalities and regions** ([MCF konsekvensutredning, Jan 2026](https://www.mcf.se/contentassets/9f0c38cd40b7485f9f006047555533bc/konsekvensutredning-mcffs-2026-1.pdf), p. ~6). The "5,000–8,000" figure in W02 §2.1 comes from law-firm and MSB secondary estimates [S]. The same document says public bodies' costs are to be **"finansieras inom befintlig ram"** (funded within existing budgets), and that drinking-water operators are in scope only from **20,000 persons served**. Many small municipal water companies therefore fall outside unless they are part of the municipality itself. MCF has published no registration count (search, Oct 2026).
4. **The "säkerhetsskydd notification duty from 1 Jan 2027" is a one-off catch-up obligation, not a recurring driver.** 4 kap. 1 a § requires operators to notify certain *förfaranden* (outsourcing and similar procedures that do not require a security-protection agreement) that started before the activity became security-sensitive. It must be met "utan dröjsmål från den 1 januari 2027" (without delay from 1 Jan 2027) ([Transportstyrelsen](https://www.transportstyrelsen.se/sv/om-oss/det-har-ar-transportstyrelsen/krisberedskap-och-sakerhet/sakerhetsskydd/aktuellt-inom-sakerhetsskydd/en-ny-anmalningsplikt-i-sakerhetsskyddslagen/); [PTS form](https://www.pts.se/contentassets/ecec80078d424b688900bcb12e286f43/anmalan-av-forfaranden-som-inte-omfattas-av-krav-pa-sakerhetsskyddsavtal.pdf)). The window closes about **9 weeks** after the reference date, before a new company could be selling.
5. **Security-protection work brings its own access controls.** If a supplier can get access to security-classified information or security-sensitive activity, the operator must sign a **säkerhetsskyddsavtal** (security-protection agreement) with it. For the relevant levels this means security vetting of the supplier's management and staff and notifying Säpo or the supervisory authority. Säpo can stop a procurement that does not meet the rules (säkerhetsskyddslag 4 kap. 1 §; [Säpo vägledning](https://www.securityservice.se/download/18.3222e1b7187a064b070e6/1683815514604/Skyldighet%20vid%20exponering%20av%20sa%CC%88kerhetska%CC%88nslig%20verksamhet_anpassad.pdf); [Ellevio SUA process](https://kundnyheter.ellevio.se/globalassets/content/sakerhetsskydd/overgripande-processbeskrivning-sua_.pdf)). A säkerhetsskyddsanalys by nature exposes the client's most sensitive assets. Each new client therefore means **weeks to months of vetting and agreement work before any billable hours** [inference]. Neither id 4's speed score of 6 nor its 4-month sales cycle reflects this.
6. **Several financial-model parameters contradict the repo's own evidence.**
   - id 13 assumes ARPA of SEK 1,800/firm/month. Fortnox's whole Byråpartner suite costs **SEK 499/month** and includes case management, KYC, engagement letters and unlimited clients [W09 §1].
   - id 15 ramps to 1.2 deals/month at a SEK 200k fee. Bolagsplatsen had only **13 accounting-firm listings in total** [W09 §2].
   - id 22 charges SEK 15–40k per bid, while Tendium's AI bid studio starts at €125/month [W07 Area 5].
   - id 2 ramps to 50 paying suppliers/month at CAC SEK 4k with no buyer network.

---

## 1. Per-opportunity review

### id 4: Säkerhetsskydd and civil-defence retainer (current 76.0, so #1)
1. **Why not at scale already?** The supply side is the bottleneck: cleared, experienced advisers are scarce [W02 §2.19; W05 M3]. Buyers also route spend through frameworks that established firms have won: Adda area 7 [§0.2] and Uppsala's 100 MSEK framework [W07 Area 2]. Supply is fragmented among Combitech, Vesper (SEK 244m), SRI, 4C Strategies and micro firms [W07 Area 2], so the gap is not empty.
2. **Signs customers won't pay:** The headline money is mostly earmarked for **physical capex**: SEK 400m for supply-preparedness materiel, SEK 490m for command centres and "trygghetspunkter", and SEK 1.2bn for shelters [W02 §2.19]. The SEK 649m general grant averages about SEK 2.2m per municipality [inference: 649/290]. That largely funds in-house beredskapssamordnare (preparedness coordinators). A SEK 300k/yr retainer competes with that salary line. TED shows only 27 "säkerhetsskydd" and 14 "krisberedskap" notices in 12 months [W05 2b].
3. **Incumbents that could eliminate it:** Adda area-7 framework suppliers (ranked call-offs), Combitech, 4C Strategies (Försvarsmakten frameworks of SEK 150m and 48–100m [W07 Area 2]), and Securitas. Securitas has partnered with AlertMedia on crisis management ([securityworldmarket](https://www.securityworldmarket.com/se/Nyheter/Foretagsnyheter/securitas-och-alertmedia-i-partnerskap-for-krishantering)).
4. **Market smaller than estimated?** Yes. The model's "600–1,000 organisations" counts every public body. Larger municipalities buy through frameworks or tenders, which a new company can't win without references. That leaves small municipalities and municipal companies buying by direct award, perhaps **150–300 reachable buyers** [inference].
5. **Painful enough?** Yes, the pain is real and politically salient. But it is met by hiring staff and by framework call-offs, not by unmet demand for a new vendor.
6. **Much better than the workaround?** Only modestly. A retainer with a "light planning tool" is roughly what framework consultants already deliver by the hour [inference].
7. **Switching costs too high?** Incumbent framework call-offs and existing security-protection agreements with known advisers create stickiness. Each new adviser triggers new vetting [§0.5].
8. **Hidden regulatory barrier?** **Yes, the largest in the top 10.**
   - LOU: the SEK 700k limit allows only about 2-year retainers [§0.1].
   - The Adda framework is closed [§0.2].
   - Security-protection agreements and vetting are needed per client [§0.5].
   - Tenders are evaluated on reference assignments, which a new company does not have.
9. **Unrealistically cheap CAC?** Yes. The model assumes CAC SEK 40k with a 4-month cycle. Public buying plus per-client vetting suggests SEK 80–120k and 6–9 months [inference].
10. **Could AI tools commoditize it?** Partly. Templates, exercise scenarios and plan drafting are easy for an LLM. The parts that can't be automated (clearance, trust, on-site exercises) are exactly the parts that are hard to scale.
11. **Still attractive in 3 years?** Spend keeps rising, with the civil-defence frame at about SEK 15bn/yr from 2028 [W02 §2.19]. But the 1 Jan 2027 one-off deadline passes, and frameworks lock in until 2030.
12. **Abandon immediately if:** within 30 days, fewer than 3 of 20 small municipalities or municipal companies will accept a direct-award retainer from an unreferenced supplier; or the founders cannot pass security vetting or name a cleared senior adviser willing to join.
- **Verdict: DOWNGRADE.** Viable only as a founder-fit play (ex-Försvarsmakten, MSB/MCF or Säpo people with clearances and references), or as a subcontractor to a framework holder.
- **Score adjustments:**
  - demand 9→7: spend is real but largely capex, in-house salaries or captured by frameworks.
  - wtp 9→7: per-municipality grants are small, and retainers compete with coordinator salaries.
  - timing 9→8: the 2027 notification is a one-off with a 9-week window.
  - gap 6→4: the Adda framework is closed to 2030, and the Uppsala framework plus established firms take the volume.
  - unit 7→6: scarce cleared seniors push up delivery cost.
  - speed 6→4: vetting and references come before the first invoice.
  - scale 5→4: people-bound, and every client needs its own vetting.
  - feas 5→3: säkerhetsskydd, LOU and framework barriers stack.
- **Most dangerous assumption:** that a new, unreferenced company can get into municipal security-protection work at SEK 300k/yr. Both procurement law and the security-protection rules are built to keep it out.

### id 1: NIS2 compliance-as-a-service (74.5, so #2)
1. **Why not at scale already?** The law has only been in force since 15 Jan 2026, and supervision starts now. Transportstyrelsen plans inspections of security measures **from Nov 2026** ([Transportstyrelsen](https://www.transportstyrelsen.se/sv/om-oss/det-har-ar-transportstyrelsen/krisberedskap-och-sakerhet/cybersakerhet-nis2/tillsyn-av-cybersakerhet/)). Fixed-price offers already exist, though. Opsio publishes gap analyses at SEK 45–90k and SEK 10–30k/month [W07 Area 1].
2. **Signs customers won't pay:** Public NIS2 costs are to be met **within existing budgets** [§0.3]. The extra NIS2 money is SEK 0.25bn/yr across 310 bodies, about SEK 0.8m each [W01 §2.4, inference]. KLASSA is free or cheap, used by **410 organisations**, and its requirements catalogue is **mapped to NIS2** [W07 Area 1]. Municipal companies are hiring in-house security roles: Nybro Energi advertised a säkerhetsansvarig ([framtid.se](https://www.framtid.se/yrke/sakerhetsarkitekt/lediga-jobb/nybro-energi-ab/sakerhetsansvarig)).
3. **Incumbents that could eliminate it:** Atea, Advania and Tietoevry bundle NIS2 into existing MSP contracts. Stratsys extends its municipal governance base. SKR/Adda could add services around KLASSA [inference].
4. **Market smaller than estimated?** Yes, by 2–4x on the private side: about 1,500 companies, not 5–8k [§0.3]. Small water companies under 20,000 persons are out of scope. Still enough: 1,800 entities × 5% share = 90 customers ≈ SEK 20m ARR [inference].
5. **Painful enough?** Yes. There are fines, a management ban, mandatory management training and 24h/72h reporting [W02 §2.1].
6. **Much better than the workaround?** For a 50–500 FTE municipal company, a fixed price with a Swedish named vCISO beats hourly Big-4 work and beats a bare tool. The difference over Opsio-type packages is small.
7. **Switching costs too high?** Low to enter, since many buyers have no incumbent. They are moderate once the ISMS is embedded, which helps retention.
8. **Hidden regulatory barrier?** A mild one. Retainers fit under the SEK 700k limit [§0.1], but municipalities must add up all IT-security consulting of the same kind. Some energy and water companies buy under LUF, not LOU (different limits; not verified here).
9. **Unrealistically cheap CAC?** Somewhat. SEK 35k for a public-sector advisory sale from an unknown brand is low. SEK 50–70k is more realistic [inference]. Annual value is about SEK 300k, so it still pays back.
10. **Could AI tools commoditize it?** Yes for policy and ISMS documents: Isodora is an AI agent from SEK 500/month [W07 Area 1]. Value moves to the named human, incident runbooks, board training and evidence collection. Price pressure on the "implementation" fee is likely.
11. **Still attractive in 3 years?** It stays attractive. The remediation wave peaks 2026–27, then recurring audits, training and supply-chain reviews follow. Margins will compress.
12. **Abandon immediately if:** the 30-company test in `validation` yields 0 paid SEK 60k gap analyses; or more than half of prospects say "our IT partner (Atea/Advania) or KLASSA covers it".
- **Verdict: KEEP (#1).** It is the cleanest of the ten: law in force, buyers fit the direct-award limit, low capital needed.
- **Score adjustments:**
  - demand 8→7: the entity count is about 1,800, not 5–8k.
  - wtp 8→7: public funding is "within existing budgets", and Opsio anchors prices at SEK 10–30k/month.
  - gap 5→4: KLASSA (410 organisations, NIS2-mapped), Opsio fixed-price packages and Isodora at SEK 500/month.
  - speed 8→7: public buying cycle and LUF/LOU checks.
- **Most dangerous assumption:** that buyers will pay a new brand for what their existing IT partner or KLASSA bundles in "well enough".

### id 6: Defence-SME supplier onboarding (66.0, so #3)
1. **Why not at scale already?** Demand only crystallises when a prime or FMV initiates a security-protection agreement. FMV's routine says the agreement is **initiated by the customer, not the supplier** [W07 Area 3]. Nobody can sell "säkerhetsskydd setup" ahead of a contract in a form that counts.
2. **Signs customers won't pay:** SOFF calls säkerhetsskydd "betungande administrativt och kostsamt" (administratively burdensome and costly) [W07 Area 3]. That is a complaint about cost, not a sign of budget. The model's programme fee of SEK 150–500k is "assumption, no Swedish benchmark found" (`models_top20.py`). Almi grants are capped at about SEK 15k ([Realtid](https://www.realtid.se/bors-finans/smaforetag-drar-nitlott/)).
3. **Incumbents that could eliminate it:** Primes' own supplier development, and Combitech (though Saab ownership creates a conflict). Free or subsidised alternatives: Business Sweden (SEK 300m over 2026–30 [W07 Area 3]), Vinnova civil-military accelerators ([Vinnova](https://www.vinnova.se/en/calls-for-proposals/civil-military-synergies/acceleration-of-civil-military-innovations-2027)), SOFF courses.
4. **Market smaller than estimated?** Yes. "300–800 relevant" firms, of which only those with a near-term contract will pay. That might be **30–80 per year** [inference]. SOFF has 400–500 members [W07 Area 3].
5. **Painful enough?** Only at the moment of a contract. Before that it is "nice to have".
6. **Much better than the workaround?** Productising ISM, AQAP and export-control basics is useful. The workaround (prime hand-holding plus an ISO consultant) works.
7. **Switching costs too high?** No. But engagements are one-off: the model's ARPA is only SEK 8k/month.
8. **Hidden regulatory barrier?** Export-control advice drifts into legal practice. A firm advising on ISM gets security-sensitive information and may itself need security-protection agreements [§0.5].
9. **Unrealistically cheap CAC?** The model's CAC of SEK 45k against a few hundred buyers is plausible only through a SOFF or cluster channel.
10. **Could AI tools commoditize it?** Gap assessments and document packs can be largely automated. A JOSCAR-style registry needs primes, not AI.
11. **Still attractive in 3 years?** Defence spend keeps growing (FMV order frame SEK 92bn→244bn [W06 #2]). The service would remain niche.
12. **Abandon immediately if:** Saab, BAE Hägglunds or FMV supplier managers say they onboard SMEs themselves at no charge; or fewer than 3 of 15 SOFF SMEs would pay SEK 100k+ without a contract in hand.
- **Verdict: DOWNGRADE** to a product line inside id 1 or id 4, not a standalone venture.
- **Score adjustments:**
  - demand 6→4: demand appears only when a contract does.
  - wtp 6→4: no price benchmark, SOFF complaints about cost, subsidised substitutes.
  - gap 8→6: "no JOSCAR in Sweden" signals thin demand as much as a gap.
  - unit 6→5: one-off fees, small retainer.
  - speed 6→5: slow, channel-dependent sales.
  - scale 5→4: 30–80 buyers/yr.
- **Most dangerous assumption:** that SMEs invest SEK 150–500k ahead of an order.

### id 7: CRA PSIRT-as-a-service (63.5, so #4)
1. **Why not at scale already?** Full obligations start **11 Dec 2027**. Article 14 reporting (live Sep 2026) only covers actively exploited vulnerabilities and severe incidents [W02 §2.2], so volume is tiny today. No CRA notified body had been designated as of the latest checks ([cyberresilienceact.eu, 26 Jun 2026](https://www.cyberresilienceact.eu/news/cra-notified-bodies-rules-apply-11-june-2026.html); [W07 Area 4]).
2. **Signs customers won't pay:** Buyers are anchored by tool prices: Verimu €49–149/month and sbomify $159/month [W07 Area 4]. The file itself says "many will wait until 2027".
3. **Incumbents that could eliminate it:** Intertek Semko (SEK 462m) and RISE bundling testing with PSIRT. SBOM vendors adding PSIRT workflows. EU-wide PSIRT services such as ONEKEY [W07 Area 4].
4. **Market smaller than estimated?** Probably not in units: "hundreds to low thousands" of Swedish product makers [W03 §4]. Most products are in the default class and can self-assess (CRA Annex III/IV structure, background knowledge), so the conformity-assessment upsell is smaller than implied.
5. **Painful enough?** Yes from H2 2027. Support periods of at least 5 years mean recurring obligations.
6. **Much better than the workaround?** For SMEs without security staff, an outsourced PSIRT with 24h coverage is meaningfully better than tool-only.
7. **Switching costs too high?** Moderate and helpful: once a company is the registered PSIRT contact, it rarely switches.
8. **Hidden regulatory barrier?** None material. Swedish market surveillance (PTS) and notification (Swedac) are still being set up [W07 Area 4].
9. **Unrealistically cheap CAC?** CAC SEK 50k with a 5-month cycle is fair for industrial sales.
10. **Could AI tools commoditize it?** Triage and SBOM diffing can largely be automated. That helps margins (65% GM) but also lowers prices.
11. **Still attractive in 3 years?** Yes, and it is the most durable demand driver here. Interest will peak in 2027–28.
12. **Abandon immediately if:** 15 Swedish machine or IoT makers interviewed say their SBOM tool or test house already covers PSIRT; or the CRA is reopened by an omnibus that delays Dec 2027.
- **Verdict: KEEP.** Its timing is better than its demand score suggests. Plan to start selling Q2 2027.
- **Score adjustments:**
  - wtp 7→6: SBOM tools anchor prices low.
  - speed 5→4: buyers wait for 2027, so first revenue is slow.
  - Everything else unchanged.
- **Most dangerous assumption:** that SMEs outsource PSIRT rather than tick the box with a €49/month tool.

### id 13: Practice OS for small accounting firms (63.5)
1. **Why not at scale already?** The ledger vendors already ship it. Fortnox Byråpartner at **SEK 499/month** includes case management, KYC/PEP, engagement letters and unlimited clients. Spiris Smarta Byrån costs SEK 379/consultant. Wolters Kluwer launched Capego Practice Management in Sep 2025 [W09 §1].
2. **Signs customers won't pay:** The "backlash" in the file is anger at **paying more**, not a wish to buy another tool [W09 §1; W03 S8-S10]. Byråer say their own clients are holding back automation [W09 §1]. Sector EBITDA is 7.3% [W09 §1].
3. **Incumbents that could eliminate it:** Fortnox (EQT-owned, more than 10,000 firms) can bundle features or restrict API access. My search found no published partner terms, so the risk is unquantified.
4. **Market smaller than estimated?** Yes. The SAM assumes 3 seats × SEK 4.8k/yr across 8,126 firms. At the realistic price (below Fortnox's 499/month suite) the SAM is about SEK 20–40m [inference]. Most firms are single-ledger, so the "platform-neutral" pitch fits a minority [inference].
5. **Painful enough?** It is a moderate, daily pain, and incumbents partly solve it.
6. **Much better than the workaround?** Not substantially for single-ledger firms.
7. **Switching costs too high?** Yes for the workflow layer. Deadline, client and KYC data already sit inside Fortnox Byrå.
8. **Hidden regulatory barrier?** None. GDPR and AML data processing are manageable.
9. **Unrealistically cheap CAC?** CAC SEK 9k against SEK 1,800/month ARPA looks fine, but the ARPA is 3.6x the incumbent suite. At SEK 500/month, payback is 18+ months [inference].
10. **Could AI tools commoditize it?** Yes. AI document chasing is appearing inside Fortnox's marketplace (MoreAI MCP) and from Briox Lerry [W09 §1].
11. **Still attractive in 3 years?** Unlikely. Bundling deepens after EQT's take-private [inference].
12. **Abandon immediately if:** Fortnox's integration-partner terms bar competing byrå workflow or charge per-client API fees; or fewer than 10 of 50 multi-ledger byråer commit to SEK 1,000+/month.
- **Verdict: REJECT** as scored. A platform-neutral AI layer sold to multi-ledger firms of 10–50 staff is a niche of only about 114 firms with 20+ staff [W03 §9].
- **Score adjustments:**
  - demand 7→5: the pain is mostly about price, and largely bundled away.
  - wtp 3: down from 5; the incumbent suite costs SEK 499/month.
  - gap 6→3: Fortnox Byrå, Smarta Byrån and Capego PM already cover it.
  - unit 7→5: realistic ARPA is a third of the model's.
  - scale 7→5: API and platform dependence.
  - feas 6→5: Fortnox API terms are unknown.
- **Most dangerous assumption:** that byråer pay SEK 1,800/month on top of a SEK 499/month suite that already does most of it.

### id 15: Accounting-firm succession marketplace (63.5)
1. **Why not at scale already?** Deals are rare, local and relationship-driven. Clients "follow the person", and small books are absorbed by colleagues [W09 §2; file `wrong`].
2. **Signs customers won't pay:** Bolagsplatsen has only **13 listings** in Ekonomi & Redovisning, and prices are mostly undisclosed [W09 §2]. Buyers (Cedra, Azets, Aspia, Accru, Freedom Group, Wint) **source directly**. Wint pays upfront plus kick-back for client books [W09 §2], which removes the need for an intermediary.
3. **Incumbents that could eliminate it:** Bolagsplatsen, Svensk FöretagsFörmedling, the consolidators' corporate-development teams, and Srf/FAR networks.
4. **Market smaller than estimated?** Yes. "300–800 deals/yr" is an assumption. About 16k of the 23,921 firms have no employees [W03 §9], so their "deals" are client-book transfers worth well under SEK 1m. At 6%, that fee is below SEK 60k, not the SEK 200k in `models_top20.py` [inference].
5. **Painful enough?** For retiring owners, once. It is not a recurring problem.
6. **Much better than the workaround?** A valuation report adds some value. Matching does not, when buyers phone sellers directly.
7. **Switching costs too high?** Not applicable (transactional), so there is no lock-in either.
8. **Hidden regulatory barrier?** None. Client consent and GDPR apply to transferring client books [inference].
9. **Unrealistically cheap CAC?** CAC SEK 40k per deal is plausible. Volume is the problem.
10. **Could AI tools commoditize it?** Valuation and teasers, yes. Trust, no.
11. **Still attractive in 3 years?** It weakens. PE has already taken the Big-4 SME arms [W09 §2], and the best targets are being bought now.
12. **Abandon immediately if:** fewer than 10 owners sign mandates within 60 days of outreach to 200 owners over 60.
- **Verdict: DOWNGRADE.** Better run as a lead source for id 16 (roll-up) than as a standalone business.
- **Score adjustments:**
  - demand 6→5: deal volume is unproven.
  - wtp 6→4: buyers pay sellers directly, and micro-deal fees are below SEK 60k.
  - timing 7→6: PE consolidation is already advanced.
  - gap 6→4: buyers' own sourcing and Wint client-book buying.
  - unit 6→4: SEK 200k average fee is unrealistic.
- **Most dangerous assumption:** a SEK 200k fee per deal at about 1 deal/month.

### id 21: Procurement-support-as-a-service (63.5)
1. **Why not at scale already?** Municipalities solve it **without the market**. Examples: inter-municipal joint procurement units such as Dalarna's GNU/Upphandlingscenter ([Hedemora riktlinje](https://hedemora.se/wp-content/uploads/2024/09/riktlinje-for-inkop-upphandling-avtalsforvaltning-2024-04-03.pdf)); a shared unit for 6 Kalmar-region municipalities ([Västervik](https://vastervik.se/globalassets/naringsliv-arbete/upphandling/dokument/policy-riktlinjer-uppforandekod-etc/instruktioner-for-upphandling-och-inkop---vastervik-290-kb.pdf)); Inköp Gävleborg; Timrå buying from Sundsvall [W07 Area 5]; staffing firms (Bemannia).
2. **Signs customers won't pay:** The price benchmark is SEK 675/h (2019) [W07 Area 5]. Both "spend" data points come from **Konkurrensverket supervision cases** (Timrå tillsynsbeslut; KKO 19-020) [W07 ledger #61–62]. That suggests these deals attract regulator scrutiny [inference].
3. **Incumbents that could eliminate it:** Inter-municipal procurement units, Bemannia-type staffing frameworks, e-Avrop's consultant marketplace.
4. **Market smaller than estimated?** "~1,000+ small contracting bodies" overstates it, because many already belong to joint units [inference]. Business-services tenders draw 6.2 bids on average [W05 2b], so the venture's own sales tenders will be competitive.
5. **Painful enough?** Yes. Upphandlare are in shortage [W05 M3].
6. **Much better than the workaround?** Not clearly. The "AI-assisted" part is the only difference from hourly consultants and joint units.
7. **Switching costs too high?** No.
8. **Hidden regulatory barrier?** **Yes.** At SEK 40k/month the contract exceeds the SEK 700k limit within 2 years [§0.1], so it must be tendered. Konkurrensverket fines unlawful direct awards [W07 Area 5]. Municipality-to-municipality cooperation can often avoid procurement altogether (in-house and cooperation exemptions; background), which a private supplier cannot.
9. **Unrealistically cheap CAC?** Yes. CAC SEK 30k assumes direct sales, but in reality the venture must win tenders judged on references.
10. **Could AI tools commoditize it?** Specification drafting and eForms work are prime LLM targets. Buyers' own e-tendering platforms (Mercell/TendSign, e-Avrop) will add them [inference].
11. **Still attractive in 3 years?** It erodes as AI and Statskontoret's national procurement data function arrive [W05 2a].
12. **Abandon immediately if:** 10 small municipalities confirm they belong to or plan joint units; or the first 3 tender attempts are lost to staffing frameworks on price.
- **Verdict: DOWNGRADE.**
- **Score adjustments:**
  - demand 7→6: joint units absorb much of the need.
  - wtp 6→5: anchored at hourly rates.
  - gap 5→3: joint units, staffing frameworks and consultancies.
  - unit 6→4: 45% GM, and the model's ARPA forces tenders.
  - speed 7→5: the venture has to tender to sell.
  - scale 4→3: labour-linear.
  - feas 7→5: LOU limit and Konkurrensverket enforcement.
- **Most dangerous assumption:** that municipalities can buy a SEK 480k/yr retainer by direct award.

### id 22: Done-for-you bid writing for SMEs (60.0)
1. **Why not at scale already?** Every Swedish bid-writing firm found is a micro firm under SEK 10m revenue [W07 Area 5]. That is structural evidence the model doesn't scale.
2. **Signs customers won't pay:** Tendium starts at **€125/month** with an AI bid studio and "Win Bid Specialists" [W07 Area 5]. Upphandlingsmyndigheten and Företagarna offer free guides. Low-competition categories are low-competition **because of proprietary equipment and incumbents** (lab instruments 52% single-bid, "Proprietary equipment"; IT single bids are "licenspartner"/named-vendor support) [W05 2b], not because SMEs lack writers.
3. **Incumbents that could eliminate it:** Tendium and Mercell productising AI plus experts.
4. **Market smaller than estimated?** Yes. Among about 13,000 bidders, few will pay SEK 15–40k per bid on small tenders [inference].
5. **Painful enough?** Episodic.
6. **Much better than the workaround?** No. AI drafting now gets close to it.
7. **Switching costs too high?** None, so no retention either.
8. **Hidden regulatory barrier?** None material.
9. **Unrealistically cheap CAC?** CAC SEK 6k per bid customer is optimistic [inference].
10. **Could AI tools commoditize it?** **Yes, most directly of all ten.**
11. **Still attractive in 3 years?** No.
12. **Abandon immediately if:** Tendium's Bid Studio produces a compliant draft for a sample tender in under 2 hours (likely already the case [inference]).
- **Verdict: REJECT.**
- **Score adjustments:**
  - demand 6→4: low competition comes from lock-in, not missing writers.
  - wtp 5→4: anchored to Tendium's €125/month.
  - gap 4→2: Tendium/Mercell plus free guides.
  - unit 5→4: price pressure.
  - scale 4→2: micro-firm ceiling.
- **Most dangerous assumption:** that better bids unlock single-bid categories.

### id 38: Grid-connection consultancy (59.0)
1. **Why not at scale already?** Sweco, Rejlers and AFRY do it hourly and are "capacity-constrained" with "no productised offer found" [W08 §6]. Credentialed power-systems engineers are scarce.
2. **Signs customers won't pay:** Grid pain is concentrated in large loads; "~0% of SMEs" name grid as their top obstacle [W01 row 2]. Consultants cannot create capacity; the DSO decides.
3. **Incumbents that could eliminate it:** The big engineering firms, BESS developers' in-house teams, and DSO portals if they become digital (the German epilot model) [W08 §6].
4. **Market smaller than estimated?** "Growing" is unquantified. The SvK queue of over 175 GW is low-reliability [W08 §6], and much of it is offshore wind (125 GW) that consultants of this type won't serve.
5. **Painful enough?** Yes for depots and BESS: delays are expensive.
6. **Much better than the workaround?** Possibly. SvK's proposed **"ready-first"** allocation replacing first-come-first-served ([SvK report, Apr 2026](https://www.svk.se/499267/siteassets/om-oss/rapporter/2026/rapport_-regeringsuppdrag-om-att-se-over-anslutningsprocessen-till-elsystemet-och-tilltradet-till-elmarknaden-.pdf)) rewards well-prepared applications. That favours specialists.
7. **Switching costs too high?** Not applicable (project work).
8. **Hidden regulatory barrier?** None formal. Credibility requires grid-engineering credentials, and the opportunity is founder-gated.
9. **Unrealistically cheap CAC?** CAC SEK 20k per project is plausible through developer networks.
10. **Could AI tools commoditize it?** Low risk. Load-flow, flexibility design and negotiation are expert work.
11. **Still attractive in 3 years?** Yes. Electrification, ready-first queues and Ei fee reforms keep complexity high.
12. **Abandon immediately if:** the founding team has no power-systems engineer, or 5 BESS or depot developers say Sweco or in-house teams suffice.
- **Verdict: KEEP (conditional on founder fit).** It is under-rated relative to the ids above that face procurement barriers. Private B2B buyers face no LOU.
- **Score adjustments:**
  - wtp 6→7: private buyers, high cost of delay, and SvK's SEK 100k investigation fee shows they pay for process [W08 §6].
  - feas 5→4: hard dependence on credentials.
- **Most dangerous assumption:** that the founders have credible power-systems competence.

### id 2: NIS2 supplier security attestation (58.0)
1. **Why not at scale already?** It needs buyers to accept a common standard. The UK precedents had government backing (Cyber Essentials) or backing from primes (JOSCAR: 30+ buyers, 6,000+ suppliers) [W07 Area 3].
2. **Signs customers won't pay:** Only 40% of 10–49 FTE firms have security policies [W03 §6]. These are low-priority buyers who answer questionnaires for free today.
3. **Incumbents that could eliminate it:** MCF publishing a free baseline, SKR/Adda extending **KLASSA's NIS2-mapped requirements catalogue** to suppliers (410 organisations already use it) [W07 Area 1], Vanta trust centres, ISO bodies.
4. **Market smaller than estimated?** In paid units, yes, until a buyer network exists.
5. **Painful enough?** Not yet. Questionnaires are only starting to arrive.
6. **Much better than the workaround?** Only if accepted. Without acceptance it is worse than nothing.
7. **Switching costs too high?** Not applicable yet.
8. **Hidden regulatory barrier?** None, and also no mandate.
9. **Unrealistically cheap CAC?** **Yes.** CAC SEK 4k and 10–50 new suppliers/month with no network.
10. **Could AI tools commoditize it?** AI questionnaire answering (trust-centre AI) removes the supplier-side pain.
11. **Still attractive in 3 years?** Only if a public body endorses it.
12. **Abandon immediately if:** the 2 municipal companies in `validation` decline to accept the baseline.
- **Verdict: REJECT** as a standalone business. Keep it as a free lead-gen feature of id 1.
- **Score adjustments:**
  - demand 5→3: no pull until buyers mandate it.
  - wtp 4→3: suppliers answer questionnaires for free.
  - gap 7→4: KLASSA and MCF could fill it for free.
  - speed 5→3: chicken-and-egg.
  - scale 8→6: network value is unrealised.
- **Most dangerous assumption:** that buyers accept a private, non-statutory standard.

---

## 2. Revised top 10

The table recomputes the weights with my adjustments. Non-top-10 ids keep their original scores; I did not attack them, so they are **probably also inflated**.

| New rank | id | Opportunity | Old score | New score | Change / reason |
|---|---|---|---|---|---|
| 1 | 1 | NIS2 compliance-as-a-service | 74.5 | **69.0** | Moves up to #1. Fits the direct-award limit, law in force, private and municipal buyers |
| 2 | 7 | CRA PSIRT-as-a-service | 63.5 | **61.0** | Most durable driver. Sell from Q2 2027 |
| 3 | 4 | Säkerhetsskydd retainer | 76.0 | **61.0** | Falls behind id 1 on tie-break: closed framework, per-client vetting, LOU limit. Founder-gated |
| 4 | 38 | Grid-connection consultancy | 59.0 | **60.0** | No LOU, high cost of delay, SvK ready-first. Founder-gated |
| 5 | 30 | Stambyte procurement adviser for BRFs | 58.0 | 58.0 | **Promoted.** Private buyers, high stakes (SEK 250–500k/flat) [W03 §2], hard for AI to replace. Not stress-tested |
| 6 | 17 | Vertical bookkeeping for construction trades | 58.0 | 58.0 | **Promoted.** Not stress-tested; linear service scaling |
| 7 | 5 | Civil-preparedness planning software | 58.0 | 58.0 | **Promoted with caveats.** Same procurement and classification barriers as id 4 (feas 4 already) |
| 8 | 27 | BRF compliance copilot | 57.5 | 57.5 | **Promoted with caveats.** Boappa/Nabo overlap [W08 §1] |
| 9 | 16 | Micro accounting roll-up | 57.0 | 57.0 | **Promoted.** Absorbs id 15 as its sourcing engine. Capital-heavy |
| 10 | 20 | Packaging EPR for small producers | 57.0 | 57.0 | **Promoted.** Low ARPA, PRO portals as substitutes |
| — | 6 | Defence-SME onboarding | 66.0 | 54.0 | Out. Fold into id 1/4 |
| — | 21 | Procurement support | 63.5 | 53.5 | Out. LOU limit, joint municipal units |
| — | 15 | Succession marketplace | 63.5 | 52.5 | Out. Fold into id 16 |
| — | 13 | Practice OS | 63.5 | 51.5 | Out. Fortnox bundle at SEK 499/month |
| — | 2 | Supplier attestation | 58.0 | 48.0 | Out. Free feature of id 1 |
| — | 22 | Bid writing | 60.0 | 47.5 | Out. AI and Tendium commoditize it |

**The big changes, in one paragraph.** The original ranking rewarded *public money exists* without discounting *how that money is allowed to be spent*. Once you apply the SEK 700k direct-award limit, the closed Adda area-7 framework (to 2030), reference-based award criteria and per-client security vetting, the public-sector service plays (ids 4, 21, 6) lose 5–15 points. Ideas whose proposed price is a multiple of an incumbent's bundle (ids 13, 22) collapse. Private-buyer, expert-heavy services (ids 38, 30) rise by default. **The gap between #2 and #10 is now only 4 points.** The study's real conclusion is "one clear winner (id 1), then a pack that is founder-dependent". It is not "ten strong opportunities".

Note: the promoted ids 30, 17, 5, 27, 16 and 20 have **not** had this adversarial pass. Their 57–58 scores should be treated as upper bounds until they do.

---

## 3. Machine-readable adjustments

```
ADJ id=4 demand=7 wtp=7 timing=8 gap=4 unit=6 speed=4 scale=4 feas=3
ADJ id=1 demand=7 wtp=7 gap=4 speed=7
ADJ id=6 demand=4 wtp=4 gap=6 unit=5 speed=5 scale=4
ADJ id=7 wtp=6 speed=4
ADJ id=13 demand=5 wtp=3 gap=3 unit=5 scale=5 feas=5
ADJ id=15 demand=5 wtp=4 timing=6 gap=4 unit=4
ADJ id=21 demand=6 wtp=5 gap=3 unit=4 speed=5 scale=3 feas=5
ADJ id=22 demand=4 wtp=4 gap=2 unit=4 scale=2
ADJ id=38 wtp=7 feas=4
ADJ id=2 demand=3 wtp=3 gap=4 speed=3 scale=6
```

Model-parameter fixes recommended for `models_top20.py`, all [inference]:
- **id 4:** basis text is wrong (§0.2). Set cac 90k, sales_cycle 7, churn_month 0.025 to reflect re-buying after the 2-year direct award.
- **id 1:** cac 55k, churn_month 0.018.
- **id 13:** arpa_month 600.
- **id 15:** setup_fee 80k, ramp (0.2, 0.4, 0.6).
- **id 21:** arpa_month 28k (to stay under the direct-award limit over 2 years) or model tender win rates.
- **id 22:** setup_fee 15k.
- **id 2:** ramp (2, 6, 12).

## 4. Sources checked on the web this session
- Konkurrensverket, *Analys i korthet 2026:1* (direct-award limit SEK 700,000): https://www.konkurrensverket.se/globalassets/dokument/informationsmaterial/rapporter-och-broschyrer/analys-i-korthet/analys-i-korthet_2026-1.pdf
- Mercell, thresholds from 1 Jan 2026: https://info.mercell.com/en/blog/new-procurement-thresholds-take-effect-on-1-january-2026/
- Adda, avropsvägledning Säkerhetslösningar konsulter 2025: https://www.adda.se/globalassets/2.-upphandling-ramavtal/2.-fastighetsforvaltning/fastighetsnara-tjanster/sakerhetslosningar-konsulter-2025/avropsvagledning---sakerhetlosningar-konsulter-2025.pdf
- MCF, konsekvensutredning MCFFS 2026:1: https://www.mcf.se/contentassets/9f0c38cd40b7485f9f006047555533bc/konsekvensutredning-mcffs-2026-1.pdf
- Transportstyrelsen, ny anmälningsplikt i säkerhetsskyddslagen: https://www.transportstyrelsen.se/sv/om-oss/det-har-ar-transportstyrelsen/krisberedskap-och-sakerhet/sakerhetsskydd/aktuellt-inom-sakerhetsskydd/en-ny-anmalningsplikt-i-sakerhetsskyddslagen/
- PTS, anmälan av förfaranden: https://www.pts.se/contentassets/ecec80078d424b688900bcb12e286f43/anmalan-av-forfaranden-som-inte-omfattas-av-krav-pa-sakerhetsskyddsavtal.pdf
- Transportstyrelsen, tillsyn av cybersäkerhet: https://www.transportstyrelsen.se/sv/om-oss/det-har-ar-transportstyrelsen/krisberedskap-och-sakerhet/cybersakerhet-nis2/tillsyn-av-cybersakerhet/
- Säpo, vägledning exponering av säkerhetskänslig verksamhet: https://www.securityservice.se/download/18.3222e1b7187a064b070e6/1683815514604/Skyldighet%20vid%20exponering%20av%20sa%CC%88kerhetska%CC%88nslig%20verksamhet_anpassad.pdf
- Ellevio, process for security-protection agreements (SUA): https://kundnyheter.ellevio.se/globalassets/content/sakerhetsskydd/overgripande-processbeskrivning-sua_.pdf
- cyberresilienceact.eu, notified bodies: https://www.cyberresilienceact.eu/news/cra-notified-bodies-rules-apply-11-june-2026.html
- Svenska kraftnät, report on the connection process (Apr 2026): https://www.svk.se/499267/siteassets/om-oss/rapporter/2026/rapport_-regeringsuppdrag-om-att-se-over-anslutningsprocessen-till-elsystemet-och-tilltradet-till-elmarknaden-.pdf
- Joint municipal procurement units: Hedemora https://hedemora.se/wp-content/uploads/2024/09/riktlinje-for-inkop-upphandling-avtalsforvaltning-2024-04-03.pdf ; Västervik https://vastervik.se/globalassets/naringsliv-arbete/upphandling/dokument/policy-riktlinjer-uppforandekod-etc/instruktioner-for-upphandling-och-inkop---vastervik-290-kb.pdf
- Vinnova civil-military acceleration 2027: https://www.vinnova.se/en/calls-for-proposals/civil-military-synergies/acceleration-of-civil-military-innovations-2027
- Nybro Energi security-role job ad: https://www.framtid.se/yrke/sakerhetsarkitekt/lediga-jobb/nybro-energi-ab/sakerhetsansvarig

**Not verified (gaps):** the Adda area-7 supplier list; Fortnox integration-partner terms (no public page found); MCF's NIS2 registration count; whether municipal energy and water companies buy under LUF with a different direct-award limit; the 2026 KLASSA price under Adda.
