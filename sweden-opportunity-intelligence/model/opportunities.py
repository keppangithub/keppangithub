"""Opportunity universe for the Sweden Opportunity Intelligence study (reference date 2026-10-29).

Every opportunity is derived from the research workstreams stored in ../research/.
Evidence references use workstream codes:
  W01 macro & megatrends          W02 regulation            W03 sector screen A
  W04 sector screen B             W05 demand signals        W06 foreign models
  W07 competitors cyber/public    W08 competitors property  W09 competitors SME/waste/auto/care
followed by a section or source id inside that file (e.g. "W04 S23", "W02 §2.6").

Scores are analyst judgements (0-10) informed by that evidence; they are NOT measured data.
"""

CRITERIA = [
    ("demand", "Verified customer pain and demand", 0.20),
    ("wtp", "Willingness to pay and budget availability", 0.15),
    ("timing", "Market timing and growth", 0.10),
    ("gap", "Competitive gap and differentiation", 0.10),
    ("unit", "Unit economics and profit potential", 0.15),
    ("speed", "Speed to launch and first revenue", 0.10),
    ("capeff", "Capital efficiency", 0.10),
    ("scale", "Scalability and defensibility", 0.05),
    ("feas", "Regulatory and execution feasibility", 0.05),
]

TAG_KEYS = [
    "Bootstrappable", "Capital intensive", "Software", "Physical operations", "Hybrid",
    "Marketplace", "Regulated", "Recurring revenue", "Public-sector dependent",
    "High international expansion potential",
]

OPPS = []


def O(**kw):
    kw.setdefault("intl", False)
    OPPS.append(kw)


# ---------------------------------------------------------------------------
# A. Cybersecurity, compliance, defence & preparedness
# ---------------------------------------------------------------------------
O(id=1, name="NIS2 compliance-as-a-service (fixed-price ISMS + Swedish vCISO)",
  sector="Cybersecurity / compliance",
  customer="Municipal companies (energy, water, housing, waste), mid-size 'important entities' 50-500 FTE, smaller municipalities",
  problem="Cybersäkerhetslag (2025:1506) in force 15 Jan 2026 obliges registration, risk management, management training and 24h/72h incident reporting; most mid-size entities lack an ISMS and staff (only 69% of 50-249 FTE firms have IT-security policies).",
  alternatives="Big consultancies (Truesec, Combitech, Knowit, Big4) on hourly billing; small ISMS tools (Stratsys, WF ISMS, Isodora, Fidureon, Noru); global tools in English (Vanta, Drata, DataGuard).",
  evidence="Law in force with fines up to 2%/EUR10m (W02 §2.1); 5,000-8,000 entities est. vs ~1,500 firms >=50 FTE per govt (W02 vs W03 S39 - contradictory counts); IT-security specialists in shortage (W05 Method 3); 'informationssäkerhet' in 46 TED notices (W05 2b); Vanta >$300M ARR shows model (W06 #1); SEK 0.25bn/yr NIS2 funding to municipalities/regions (W01 §2.4).",
  concept="Swedish-language ISMS templates mapped to MCF guidance + 90-day fixed-price implementation + monthly vCISO retainer + board training certificates + incident runbooks; software is a thin evidence/workflow layer.",
  why_now="Law in force since Jan 2026, supervisors staffing up; CER law proposed 1 Jan 2027; supply-chain pass-through to suppliers.",
  revenue="Fixed implementation fee (SEK 150-400k) + recurring retainer SEK 15-40k/month.",
  decision_maker="CEO/CFO of municipal company; IT manager; municipal säkerhetschef",
  competitors="Truesec, Secify, Stratsys, WF ISMS, Isodora, Advania, Atea, Knowit, DataGuard, Vanta",
  capital=400_000, tech="ISMS document automation, evidence collection integrations (M365/Entra), reporting runbooks", reg="Cybersäkerhetslagen, MCFFS 2026:1; LOU for public buyers (direct-award threshold)",
  market="Bottom-up: ~1,500-5,000 in-scope private entities + 290 municipalities x ~3 municipal companies; see sizing model",
  uncertainty="Whether mid-size entities buy fixed-price packages from a new brand vs established consultancies",
  validation="Contact 30 municipal energy/water companies with a fixed-price NIS2 gap analysis offer (SEK 60k); target 3 paid within 30 days",
  origin="Foreign model transfer (Vanta/DataGuard) adapted to Swedish service culture",
  tags=["Bootstrappable", "Hybrid", "Regulated", "Recurring revenue"],
  scores=dict(demand=8, wtp=8, timing=9, gap=5, unit=7, speed=8, capeff=8, scale=5, feas=7),
  confidence="High", n_sources=7,
  assumption="That a new entrant can win against Truesec/Big4 on trust; and the true number of in-scope entities (estimates range 1,500 to 8,000)",
  wrong="Crowding: dozens of consultancies launched NIS2 offers in 2025-26; price competition may compress retainers.")

O(id=2, name="NIS2 supplier security attestation for SMEs selling to regulated entities",
  sector="Cybersecurity", customer="10-49 FTE suppliers (IT, facilities, logistics) to NIS2 entities",
  problem="NIS2 entities must manage supply-chain risk and push security questionnaires to suppliers; only 40% of 10-49 FTE firms have security policies.",
  alternatives="Ad-hoc questionnaire answering; ISO 27001 certification (expensive); Cyber Essentials does not exist in Sweden.",
  evidence="SCB: 40% of 10-49 FTE firms have IT-security policy (W03 §6); UK JOSCAR/Cyber Essentials precedent (W06 #2); NIS2 supply-chain duty (W02 §2.1).",
  concept="Standardised 'Swedish Cyber Baseline' self-assessment + light audit + shareable trust profile, sold to suppliers, sponsored by buyers.",
  why_now="First buyer questionnaires in 2026; no national baseline scheme.",
  revenue="SEK 9-25k per supplier per year; buyer-sponsored programmes.",
  decision_maker="SME CEO; buyer's procurement/security lead", competitors="Vanta trust center, Secify, ISO certification bodies, Whistic",
  capital=300_000, tech="Questionnaire engine, evidence storage, trust profile pages", reg="None mandated; depends on buyers' contract terms",
  market="Tens of thousands of suppliers; adoption uncertain", uncertainty="Needs network effect (buyers must accept the standard)",
  validation="Get 2 municipal companies to agree to accept the baseline from their suppliers",
  origin="Foreign model (UK Cyber Essentials/JOSCAR)", tags=["Software", "Recurring revenue", "Marketplace"],
  scores=dict(demand=5, wtp=4, timing=7, gap=7, unit=6, speed=5, capeff=7, scale=8, feas=6),
  confidence="Low", n_sources=3, assumption="Buyers will accept a non-statutory standard", wrong="Chicken-and-egg; a public body (MCF) may publish its own baseline for free.", intl=True)

O(id=3, name="Swedish MSP-enablement SOC (managed detection via local IT partners)",
  sector="Cybersecurity", customer="Small Swedish IT-partner MSPs serving SMEs and municipalities",
  problem="NIS2 pushes MSP customers to demand 24/7 monitoring; small MSPs cannot staff a SOC.",
  alternatives="Huntress, Arctic Wolf, Truesec MDR, Sectra; building in-house",
  evidence="Huntress $250M ARR via MSPs (W06 #3); IT-security specialists in shortage (W05)",
  concept="White-label Swedish-language SOC and NIS2 incident reporting sold through MSPs.",
  why_now="NIS2 incident reporting duties 24h/72h", revenue="Per endpoint per month via MSP margin",
  decision_maker="MSP owner", competitors="Huntress, Truesec, Sectra, Arctic Wolf, Basalt", capital=6_000_000,
  tech="SIEM/EDR stack, 24/7 staffing", reg="NIS2; possibly own NIS2 scope as MSP",
  market="Hundreds of MSPs", uncertainty="Global vendors already sell via MSPs at low price",
  validation="Survey 20 MSPs on willingness to switch from Huntress-type tools", origin="Foreign model (Huntress)",
  tags=["Capital intensive", "Hybrid", "Recurring revenue"],
  scores=dict(demand=6, wtp=6, timing=7, gap=3, unit=5, speed=3, capeff=2, scale=6, feas=5),
  confidence="Medium", n_sources=3, assumption="Local language SOC is a differentiator", wrong="24/7 staffing cost destroys margin at small scale.")

O(id=4, name="Säkerhetsskydd & civil-defence planning retainer for municipalities and municipal companies",
  sector="Defence & civil preparedness", customer="290 municipalities, 21 regions, municipal companies (energy, water, ports), private firms in säkerhetskänslig verksamhet",
  problem="New säkerhetsskydd notification duty from 1 Jan 2027, CER law proposed 1 Jan 2027, and state civil-defence money (SEK >1.5bn to municipalities in 2026) require security-protection analyses, continuity plans, exercises and supplier vetting that small organisations cannot staff.",
  alternatives="Combitech, Sweco, AFRY, WSP, Svensk Säkerhetsrådgivning; in-house beredskapssamordnare (often a single person).",
  evidence="SFS 2026:764 in force, notification duty 2027 (W02 §2.19); civil-defence package ~SEK 12bn 2026-28 incl. ~4.6bn to municipalities/regions (W01 §2.4); säkerhetsrådgivare in shortage (W05 M3); 'säkerhetsskydd' 27 and 'krisberedskap' 14 TED notices (W05 2b); Adda frameworks for preparedness (W05 2c).",
  concept="Subscription: annual säkerhetsskyddsanalys, continuity/krisledning plans, 2 exercises/yr, supplier säkerhetsskyddsavtal support, tracked in a light planning tool.",
  why_now="Funding flows 2026-2028 and rises to ~SEK 15bn/yr civil-defence frame from 2028; new duties from 2027.",
  revenue="SEK 20-60k/month retainer per organisation + exercise fees",
  decision_maker="Kommundirektör, säkerhetschef, VD of municipal company", competitors="Combitech, Sweco, AFRY, Svensk Säkerhetsrådgivning, Prevent, Securitas",
  capital=500_000, tech="Planning and exercise tool (light); cleared staff", reg="Säkerhetsskyddslagen; staff need security clearance for some work; LOU",
  market="~600-1,000 public/municipal organisations + private säkerhetskänslig operators", uncertainty="Founders' credibility and clearance; buyers prefer known consultancies",
  validation="Pitch 15 small municipalities a fixed-price 'civilt försvar 2027-pack' funded from MCF grant; target 2 signed orders",
  origin="Original finding", tags=["Bootstrappable", "Hybrid", "Regulated", "Recurring revenue", "Public-sector dependent"],
  scores=dict(demand=9, wtp=9, timing=9, gap=6, unit=7, speed=6, capeff=8, scale=5, feas=5),
  confidence="Medium", n_sources=6, assumption="New entrant without security-sector track record can be trusted", wrong="Expertise is scarce for everyone; the bottleneck may be hiring cleared people, not demand.")

O(id=5, name="Civil-preparedness planning software (continuity, stockpiles, krigsplacering, exercises)",
  sector="Defence & civil preparedness", customer="Municipalities, regions, essential private firms",
  problem="Preparedness planning lives in Word/Excel; crisis-management systems focus on incident response, not planning and stock tracking.",
  alternatives="DSAM, Coordcom, Crises Control, Everbridge, Excel; consultancies",
  evidence="Civil-defence money (W01, W02 §2.19); Säkerhetsföretagen call for joint planning (W03 S44)",
  concept="SaaS for continuity plans, war-placement registers, stockpile inventory and exercise logs.",
  why_now="2026-28 funding; MCF guidance", revenue="SaaS SEK 50-200k/yr per municipality",
  decision_maker="Säkerhetschef/beredskapssamordnare", competitors="DSAM, Coordcom, Crises Control, Everbridge",
  capital=1_500_000, tech="SaaS with classified-data constraints (on-prem option)", reg="Säkerhetsskydd constraints on hosting; LOU",
  market="311 public bodies x SEK 100k = ~SEK 31m/yr SAM", uncertainty="Procurement cycles; security classification limits SaaS",
  validation="Demo to 10 beredskapssamordnare; count willingness to buy via direct award", origin="Original finding",
  tags=["Software", "Recurring revenue", "Public-sector dependent"],
  scores=dict(demand=6, wtp=6, timing=8, gap=5, unit=6, speed=4, capeff=6, scale=6, feas=4),
  confidence="Low", n_sources=3, assumption="Buyers want software rather than consultants", wrong="Small SAM; classified info pushes buyers to on-prem incumbents.")

O(id=6, name="Defence-SME supplier onboarding & compliance service",
  sector="Defence", customer="Swedish manufacturing SMEs wanting to enter FMV/Saab/BAE supply chains",
  problem="Entry path for new defence suppliers 'still difficult' (SOFF 2026): säkerhetsskyddsavtal, AQAP/ISO, export control, cyber requirements.",
  alternatives="Large consultancies, law firms (export control), SOFF/Almi general advice",
  evidence="FMV order frame SEK 92bn->244bn; 170 contract partners, 80% of Swedish ones SMEs (W06 #2); SOFF evaluation (W06 S12); weapons-industry turnover +52% 2022-24 (W03 §7).",
  concept="Readiness programme: gap assessment, säkerhetsskydd setup, AQAP 2110 quality, export-control classification, cyber baseline, prime supplier packs.",
  why_now="Budget ramp 2024-2030; primes need more suppliers", revenue="Programme fee SEK 150-500k + retainer",
  decision_maker="CEO of 20-200 FTE manufacturer", competitors="Combitech, Business Sweden, law firms, ISO consultants",
  capital=500_000, tech="Low; compliance evidence platform optional", reg="Export control (ISP), säkerhetsskyddslagen",
  market="~3,557 manufacturers with 20+ staff; maybe 300-800 relevant", uncertainty="Whether SMEs pay before having a contract",
  validation="Run a paid workshop with SOFF/regional industry group; 5 paying SMEs", origin="Foreign model (UK JOSCAR/Hellios)",
  tags=["Bootstrappable", "Hybrid", "Regulated"],
  scores=dict(demand=6, wtp=6, timing=9, gap=8, unit=6, speed=6, capeff=8, scale=5, feas=5),
  confidence="Medium", n_sources=5, assumption="SMEs will invest ahead of orders", wrong="Primes may fund onboarding internally; demand concentrated in few firms.")

O(id=7, name="CRA PSIRT-as-a-service + SBOM for SME product makers",
  sector="Manufacturing / cybersecurity", customer="Swedish makers of connected products and embedded software (machinery, IoT, medtech-adjacent)",
  problem="CRA vulnerability reporting live 11 Sep 2026; full obligations (secure development, SBOM, 5-year vuln handling, CE) 11 Dec 2027; SMEs lack PSIRT capability.",
  alternatives="RISE, Intertek Semko, TÜV, Cybellum, Finite State, OneKey; internal teams",
  evidence="CRA status and dates (W02 §2.2); ~1,500 machinery firms with employees (W03 §4); 52% manufacturer IT-security policy coverage (W03 §4)",
  concept="Outsourced PSIRT (intake, triage, ENISA reporting), SBOM generation and monitoring, CRA technical file support.",
  why_now="Hard deadline Dec 2027; reporting already live", revenue="SEK 10-30k/month per product line + readiness project",
  decision_maker="CTO/Head of R&D", competitors="Cybellum, Finite State, OneKey, RISE, Omegapoint",
  capital=800_000, tech="SBOM tooling (open-source based), vuln monitoring, reporting workflows", reg="CRA, Machinery Reg.",
  market="Hundreds to low thousands of Swedish product makers", uncertainty="Buyer awareness; many will wait until 2027",
  validation="Offer CRA readiness assessments to 20 machine builders; 3 paid", origin="Original finding (regulation-driven)",
  tags=["Hybrid", "Regulated", "Recurring revenue", "High international expansion potential"],
  scores=dict(demand=5, wtp=7, timing=8, gap=6, unit=7, speed=5, capeff=7, scale=7, feas=6),
  confidence="Medium", n_sources=4, assumption="SMEs outsource PSIRT rather than ignore", wrong="Tool vendors and certification bodies bundle it; enforcement may be slow.", intl=True)

O(id=8, name="Machinery Regulation CE technical-file automation",
  sector="Manufacturing", customer="SME machine builders and integrators",
  problem="Regulation (EU) 2023/1230 applies 20 Jan 2027; new risk assessments, cyber for safety functions, digital instructions.",
  alternatives="CE consultants (Pilz, Sick, RISE, Kiwa), Word templates, CE software (e.g., CE-Expert, Safexpert)",
  evidence="Regulation applies 20 Jan 2027 (W02 §2.18); 19,264 manufacturers with employees (W03 §4)",
  concept="SaaS to build/maintain technical files and risk assessments with regulation-mapped templates.",
  why_now="Jan 2027 deadline", revenue="SaaS per seat/project",
  decision_maker="Design/engineering manager", competitors="Safexpert (IBF), CE-Expert, Pilz, RISE",
  capital=1_200_000, tech="Document/risk engine", reg="Machinery Regulation", market="~1,500-3,000 builders/integrators",
  uncertainty="Existing CE software incumbents", validation="Interview 15 integrators about tooling gaps", origin="Original finding",
  tags=["Software", "Regulated", "Recurring revenue", "High international expansion potential"],
  scores=dict(demand=5, wtp=5, timing=8, gap=4, unit=6, speed=4, capeff=5, scale=6, feas=6),
  confidence="Low", n_sources=2, assumption="Existing tools are inadequate", wrong="Established European CE software already covers this.", intl=True)

O(id=9, name="AML/KYC compliance kit for small obliged entities (pre-AMLR 2027)",
  sector="Legal/compliance", customer="Accounting firms, estate agents, dealers (12,888 accounting businesses AML-registered)",
  problem="AMLR applies 10 Jul 2027; small obliged entities must run risk assessments, CDD and screening; county-board supervision.",
  alternatives="Trapets, Roaring, Creditsafe, Kycon, Fortnox/Visma modules, Excel",
  evidence="AMLR date (W02 §2.13); 12,888 accounting firms in AML register (W03 §9)",
  concept="Fixed-price AML policy pack + KYC workflow + screening integration for micro firms.",
  why_now="Regulatory reform 2027", revenue="SEK 300-1,000/month per firm",
  decision_maker="Firm owner", competitors="Trapets, Roaring, Kycon, Creditsafe, Fortnox add-ons",
  capital=600_000, tech="BankID + PEP/sanctions API integration", reg="AMLR, penningtvättslagen",
  market="~15-20k small obliged entities x SEK 6k = ~SEK 100m/yr", uncertainty="Crowded with existing vendors",
  validation="Landing page to Srf members; 50 sign-ups", origin="Original finding",
  tags=["Software", "Bootstrappable", "Regulated", "Recurring revenue"],
  scores=dict(demand=5, wtp=4, timing=7, gap=2, unit=6, speed=7, capeff=7, scale=5, feas=7),
  confidence="Medium", n_sources=3, assumption="Gap in micro-firm tooling", wrong="Existing vendors and Fortnox modules already serve this cheaply.")

O(id=10, name="AI Act governance & inventory for municipalities and HR-tech users",
  sector="Legal/compliance", customer="Municipalities and regions using AI; employers using AI in recruitment",
  problem="Annex III high-risk obligations from 2 Dec 2027; transparency from Aug 2026",
  alternatives="Law firms, Big4, generic GRC tools",
  evidence="Omnibus 2026/1744 timeline (W02 §2.3); AI-literacy duty softened (W02 §2.3)",
  concept="AI system inventory, risk classification and documentation service", why_now="Dec 2027 deadline",
  revenue="Project + subscription", decision_maker="CIO / DPO", competitors="Law firms, Big4, OneTrust",
  capital=400_000, tech="Inventory/GRC", reg="AI Act; Swedish authorities not yet designated", market="Uncertain",
  uncertainty="Hard spend arrives late 2027-28; literacy mandate softened", validation="Ask 10 municipal DPOs about 2027 budgets",
  origin="Original finding", tags=["Hybrid", "Regulated", "Public-sector dependent"],
  scores=dict(demand=3, wtp=4, timing=5, gap=4, unit=5, speed=6, capeff=7, scale=5, feas=5),
  confidence="Low", n_sources=2, assumption="Enforcement will be real", wrong="Hype zone; further delays possible.")

O(id=11, name="EAA accessibility audit + remediation retainer for mid-size e-commerce",
  sector="Retail / compliance", customer="Mid-size e-tailers and service providers in EAA scope",
  problem="Lag 2023:254 in force 28 Jun 2025; PTS supervision stepwise", alternatives="Funka, Axess Lab, Siteimprove, agencies",
  evidence="EAA status (W02 §2.4)", concept="Annual audit + dev retainer", why_now="Supervision starting",
  revenue="SEK 50-200k/yr", decision_maker="E-commerce manager", competitors="Funka, Axess Lab, Siteimprove, Monsido",
  capital=200_000, tech="Audit tooling", reg="EAA", market="Few thousand firms", uncertainty="Light enforcement",
  validation="Outbound to 30 e-tailers", origin="Original finding", tags=["Bootstrappable", "Hybrid", "Recurring revenue"],
  scores=dict(demand=4, wtp=4, timing=5, gap=3, unit=6, speed=8, capeff=8, scale=4, feas=8),
  confidence="Medium", n_sources=2, assumption="Enforcement creates urgency", wrong="No sanctions yet; mature competitors.")

O(id=12, name="EUDR geolocation & due-diligence data service for forest-owner associations and sawmills",
  sector="Agriculture/forestry", customer="Sawmills, pulp/paper, furniture makers, forest-owner associations, importers",
  problem="EUDR applies 30 Dec 2026 (large/medium) with no further delay; needs plot geolocation and DDS per shipment.",
  alternatives="In-house IT at Södra/SCA/Holmen, global EUDR SaaS, consultants",
  evidence="COM(2026)191 ruled out delay (W02 §2.12)", concept="Plot geodata + DDS submission service", why_now="Hard date Dec 2026",
  revenue="Per shipment/per supplier subscription", decision_maker="Sustainability/sourcing manager",
  competitors="Big forest companies in-house; global EUDR SaaS vendors", capital=1_000_000, tech="GIS + EU TRACES integration",
  reg="EUDR", market="Concentrated; large players in-house", uncertainty="Large firms solved in-house; simplifications reduce burden",
  validation="Interview 10 small sawmills", origin="Original finding", tags=["Software", "Regulated", "Recurring revenue"],
  scores=dict(demand=5, wtp=5, timing=7, gap=4, unit=5, speed=4, capeff=5, scale=5, feas=5),
  confidence="Low", n_sources=1, assumption="Small/medium players lack solutions", wrong="Simplified guidance (-75% costs) shrinks the need.")

# ---------------------------------------------------------------------------
# B. Accounting & SME professional services
# ---------------------------------------------------------------------------
O(id=13, name="Platform-neutral practice OS for small accounting firms",
  sector="Accounting", customer="8,126 accounting firms with employees (mostly <10 staff)",
  problem="Firms juggle deadlines, client documents, KYC and price lists across Fortnox/Spiris/BL; Fortnox raised byrå licence +200 SEK/consultant/month (autumn 2025) and added a mandatory client 'Access' fee (Apr 2026), triggering backlash and switching intent.",
  alternatives="Fortnox Byrå, Spiris/Visma byrå tools, Wolters Kluwer, Kleer, Briljant, Excel",
  evidence="SCB FDB: 23,921 firms, 8,126 with employees, 114 with 20+ (W03 §9); Fortnox pricing backlash (W03 S8-S10); Trustpilot price complaints (W05 C6); margins EBITA 10.6%->9.2% (W04 §22).",
  concept="Practice management (deadlines, client portal, document chasing, AML/KYC, pricing) across ledgers, with AI document chasing.",
  why_now="Fortnox price changes 2025-26; staff shortage; succession wave", revenue="SaaS per seat SEK 300-600/month",
  decision_maker="Firm owner", competitors="Fortnox Byrå, Spiris Byrå, Wolters Kluwer, Kleer, Briljant, Pinch",
  capital=1_500_000, tech="Integrations to Fortnox/Spiris/BL APIs; SIE files", reg="GDPR; AML", market="8,126 firms x ~3 seats x SEK 4.8k/yr = SEK ~117m/yr SAM (derived)",
  uncertainty="Fortnox API/partner terms can cut off access; low per-firm budgets",
  validation="Interview 25 firm owners; pre-sell 10 annual licences", origin="Original finding",
  tags=["Software", "Recurring revenue"],
  scores=dict(demand=7, wtp=5, timing=8, gap=6, unit=7, speed=5, capeff=6, scale=7, feas=6),
  confidence="Medium", n_sources=5, assumption="Firms will pay for another tool on top of Fortnox", wrong="Platform risk; Fortnox/EQT can bundle or block.")

O(id=14, name="AI 'digital junior' for bookkeeping and year-end prep, sold per client file to accounting firms",
  sector="Accounting", customer="Small and mid accounting firms",
  problem="Salaries +10-12% 2021-24; utilisation at ceiling 82-83%; routine categorisation/reconciliation consumes staff time.",
  alternatives="Fortnox AI features, Spiris automation, Wint (as competitor service), manual work",
  evidence="Spiris branschrapport (W03 §9); Basis $1.15B valuation shows category (W06 #4); payroll/admin roles in surplus nationally (W05 M3 counter-signal)",
  concept="Agent that pre-books, reconciles and drafts year-end packages; firm reviews.", why_now="LLM capability 2025-26",
  revenue="Per client file per month", decision_maker="Firm owner", competitors="Fortnox, Spiris, Wint, Bokio, global AI accounting tools",
  capital=2_000_000, tech="Ledger APIs, LLM pipelines, accuracy controls", reg="Bokföringslagen; GDPR",
  market="~330k SME clients served by bureaus", uncertainty="Ledger vendors will build this natively",
  validation="Pilot on 50 client files at 3 firms; measure minutes saved", origin="Foreign model (Basis)",
  tags=["Software", "Recurring revenue", "High international expansion potential"],
  scores=dict(demand=6, wtp=5, timing=8, gap=3, unit=6, speed=5, capeff=5, scale=6, feas=6),
  confidence="Medium", n_sources=4, assumption="Ledger incumbents leave room", wrong="Commoditised by Fortnox/Spiris AI within 18 months.", intl=True)

O(id=15, name="Accounting-firm succession marketplace & valuation service",
  sector="Accounting", customer="Retiring owners of ~14,200 small AB accounting firms + acquirers (Cedra, Azets, Wint, local firms)",
  problem="Large retirements expected in 5-10 years; founder average age 64 among recent solo firms; no structured marketplace.",
  alternatives="Bolagsplatsen, business brokers, personal networks, PE consolidators' own sourcing",
  evidence="Spiris succession commentary (W03 §9); PE roll-ups Cedra/Azets (W03 §9); Wint buying client books (W06 #4)",
  concept="Valuation, client-portfolio transfer, buyer matching; success fee", why_now="Demographics + PE appetite",
  revenue="Success fee 5-8% of deal + valuation fee", decision_maker="Retiring owner", competitors="Bolagsplatsen, brokers, Cedra/Azets",
  capital=300_000, tech="Light", reg="None", market="Deals: perhaps 300-800/yr (assumption)", uncertainty="Deal volume and fee capture",
  validation="Contact 50 owners aged 60+; count mandates", origin="Original finding",
  tags=["Bootstrappable", "Marketplace"],
  scores=dict(demand=6, wtp=6, timing=7, gap=6, unit=6, speed=6, capeff=8, scale=5, feas=8),
  confidence="Low", n_sources=3, assumption="Owners sell via an intermediary rather than to colleagues", wrong="Many small books are simply absorbed by local colleagues without fees.")

O(id=16, name="Acquire-and-automate micro accounting roll-up",
  sector="Accounting", customer="SME clients of acquired firms",
  problem="Retiring owners; small firms under-priced vs acquirers; automation can lift margins",
  alternatives="Cedra, Azets, Aspia, Wint", evidence="Consolidation & pricing gap (W03 §9); Xeinadin UK sale collapse (W06 #5)",
  concept="Buy 3-5 small firms (SEK 2-6m revenue each), centralise and automate", why_now="Succession wave",
  revenue="Accounting fees", decision_maker="n/a", competitors="Cedra, Azets, Wint, Ludvig", capital=8_000_000,
  tech="Automation stack", reg="AML supervision", market="SEK ~16bn small-firm accounting market", uncertainty="Valuations and staff retention",
  validation="Get LOIs from 2 sellers", origin="Foreign model (UK roll-ups) / Swedish (Wint)",
  tags=["Capital intensive", "Recurring revenue", "Hybrid"],
  scores=dict(demand=7, wtp=7, timing=7, gap=4, unit=6, speed=5, capeff=2, scale=5, feas=6),
  confidence="Medium", n_sources=4, assumption="Buy at ~0.8-1.2x revenue", wrong="PE competition bids up multiples.")

O(id=17, name="Vertical AI-native bookkeeping service for construction trades",
  sector="Accounting", customer="Small construction/trade firms (ROT, personalliggare, project accounting)",
  problem="Trades need ROT claims, project costing, personalliggare and reverse VAT; generic bureaus underserve",
  alternatives="Local bureaus, Wint, Fortnox+Bygglet", evidence="Construction lowest AI adopter 15% (W03 §2); 91k specialised contractors (W03 §2)",
  concept="Fixed-price bookkeeping+payroll specialised for trades", why_now="Personalliggare/ROT control bill 2027 (W02 §2.17)",
  revenue="SEK 2-6k/month per client", decision_maker="Owner", competitors="Wint, local bureaus", capital=1_000_000,
  tech="Automation", reg="Bokföringslag", market="Tens of thousands of trade firms", uncertainty="CAC in a crowded service market",
  validation="Pre-sell 10 clients via trade associations", origin="Original finding", tags=["Hybrid", "Recurring revenue"],
  scores=dict(demand=6, wtp=6, timing=6, gap=5, unit=6, speed=6, capeff=5, scale=5, feas=7),
  confidence="Low", n_sources=2, assumption="Vertical specialisation lowers CAC", wrong="Service businesses scale linearly with staff.")

O(id=18, name="Personalliggare/kassaregister 2027 compliance SaaS for restaurants and salons",
  sector="Hospitality / SME services", customer="Restaurants, hair & beauty, car washes",
  problem="Prop. 2025/26:282 proposes digital personalliggare from 1 Jan 2027; new kassaregister requirements mandatory 1 Jan 2027",
  alternatives="Caspeco, Personalkollen, Quinyx, POS vendors", evidence="W02 §2.17", concept="Digital staff ledger + compliance checks",
  why_now="Jan 2027", revenue="SEK 199-499/month", decision_maker="Owner", competitors="Caspeco, Personalkollen, POS vendors",
  capital=400_000, tech="App", reg="Bill not yet adopted", market="Tens of thousands of venues", uncertainty="Bill may slip after election",
  validation="Track Riksdag vote; survey 30 salons", origin="Original finding", tags=["Software", "Bootstrappable", "Recurring revenue"],
  scores=dict(demand=4, wtp=3, timing=6, gap=2, unit=5, speed=7, capeff=7, scale=4, feas=4),
  confidence="Low", n_sources=1, assumption="Bill passes on time", wrong="Incumbent POS/scheduling vendors add the feature for free.")

O(id=19, name="VSME supplier-response service for SMEs",
  sector="Sustainability", customer="SMEs receiving ESG data requests from large customers/banks",
  problem="Large customers ask for ESG data; Omnibus caps requests at VSME for <1,000 FTE", alternatives="Position Green, Normative, Worldfavor, consultants",
  evidence="CSRD scope cut (W02 §2.5; W04 §24)", concept="Fill VSME once, share many", why_now="Value-chain cap delegated act",
  revenue="SEK 5-15k/yr", decision_maker="CFO", competitors="Worldfavor, Normative, Position Green", capital=500_000,
  tech="Data collection", reg="VSME voluntary", market="Shrinking", uncertainty="Demand collapsed post-omnibus",
  validation="Survey 30 suppliers", origin="Original finding", tags=["Software", "Recurring revenue"],
  scores=dict(demand=3, wtp=2, timing=3, gap=3, unit=4, speed=6, capeff=6, scale=5, feas=7),
  confidence="Medium", n_sources=3, assumption="Banks keep asking", wrong="Already the main hype zone; avoid.")

O(id=20, name="Packaging EPR registration & reporting for small producers/e-tailers",
  sector="Waste / retail compliance", customer="Small importers and e-tailers newly defined as producers (PPWR from 12 Aug 2026)",
  problem="Register with Naturvårdsverket, join PRO, annual report by 31 March; many micro-producers newly in scope",
  alternatives="NPA, TMR (PROs), Lizenzero (DE), consultants",
  evidence="PPWR status and Swedish producer definition (W02 §2.8)", concept="Done-for-you registration + annual reporting from webshop data",
  why_now="First reports due 31 Mar 2027", revenue="SEK 1-5k/yr per producer", decision_maker="E-com owner",
  competitors="NPA, TMR, Lizenzero", capital=500_000, tech="Shopify/WooCommerce integrations", reg="PPWR",
  market="Tens of thousands of producers (unverified)", uncertainty="PROs may offer simple portals free",
  validation="Landing page + 100 e-tailer signups before Mar 2027", origin="Foreign model (Lizenzero DE)",
  tags=["Software", "Bootstrappable", "Regulated", "Recurring revenue", "High international expansion potential"],
  scores=dict(demand=5, wtp=4, timing=8, gap=5, unit=5, speed=7, capeff=7, scale=6, feas=7),
  confidence="Low", n_sources=2, assumption="Micro-producers face real burden", wrong="Low WTP; PRO portals suffice.", intl=True)

# ---------------------------------------------------------------------------
# C. Public procurement & govtech
# ---------------------------------------------------------------------------
O(id=21, name="Procurement-support-as-a-service for small municipalities and public companies",
  sector="Public procurement", customer="Municipalities and municipal companies running 1-5 tenders/yr",
  problem="Upphandlare in national shortage; bids per tender fell 5.9->4.6; ~20% single-bid; only 64% of awards post-announced; eForms complexity.",
  alternatives="Upphandlingskonsulter (hourly), Adda frameworks, in-house generalists",
  evidence="UHM Rapport 2026:1 (W05 2a); AF Yrkesbarometer shortage (W05 M3); >half of contracting organisations run 1-5 tenders/yr (W04 §15)",
  concept="Fractional procurement office: spec drafting, eForms, supplier outreach to raise bid counts, contract follow-up; AI-assisted.",
  why_now="Persistent shortage + falling competition; Statskontoret national procurement database", revenue="Retainer SEK 25-80k/month or per-tender fee",
  decision_maker="Ekonomichef / kommundirektör", competitors="Upphandlingsbyrån-type consultancies, Inköpsrådet, Lumell, Kommers",
  capital=300_000, tech="Templates, AI spec drafting, supplier database", reg="LOU; must itself be procured (direct award < threshold)",
  market="~1,000+ small contracting bodies", uncertainty="Consultancy market already exists; hourly rates set ceiling",
  validation="Offer 5 small municipalities a fixed-price tender (SEK 75k); 2 paid in 45 days", origin="Original finding",
  tags=["Bootstrappable", "Hybrid", "Recurring revenue", "Public-sector dependent"],
  scores=dict(demand=7, wtp=6, timing=6, gap=5, unit=6, speed=7, capeff=8, scale=4, feas=7),
  confidence="Medium", n_sources=4, assumption="Buyers prefer retainer over hourly consultants", wrong="Linear service scaling; consultants compete on price.")

O(id=22, name="Done-for-you bid writing for SMEs in low-competition categories",
  sector="Public procurement", customer="SME suppliers (<50 FTE) in IT, maintenance, lab, food, transport categories",
  problem="Only ~13,000 firms bid nationally; 22% single-tender lots on TED; SMEs lack bid capacity",
  alternatives="Tendium (1,400+ customers), Mercell, Visma Opic, freelance bid writers",
  evidence="TED analysis (W05 2b); Tendium traction (W06 #8)", concept="AI-assisted bid writing service, success-linked",
  why_now="Defence/preparedness and public spend growth", revenue="Per bid SEK 15-40k + win bonus", decision_maker="SME CEO",
  competitors="Tendium, Mercell, bid consultants", capital=200_000, tech="AI drafting", reg="LOU",
  market="~13k bidding firms + non-bidders", uncertainty="Win-rate dependence", validation="Write 5 bids for paying SMEs",
  origin="Foreign model (UK bid-writing) ", tags=["Bootstrappable", "Hybrid"],
  scores=dict(demand=6, wtp=5, timing=6, gap=4, unit=5, speed=8, capeff=9, scale=4, feas=8),
  confidence="Medium", n_sources=3, assumption="SMEs pay per bid", wrong="Commoditised by Tendium AI features.")

O(id=23, name="Public-sector legacy-system exit & migration service",
  sector="Govtech", customer="Municipalities locked into ekonomi/löne/dokument/verksamhetssystem",
  problem="31-33% of IT/software award lots on TED receive one tender - lock-in",
  alternatives="Incumbent vendors, large IT consultancies", evidence="Own TED analysis (W05 2b); SKR on case-system lock-in (W04 §15); Adda Ekonomisystem 2027 (W05 2c)",
  concept="Independent requirements, data migration and procurement support to switch systems", why_now="Framework windows 2027-28",
  revenue="Project fees", decision_maker="IT chief / ekonomichef", competitors="Sweco, Knowit, Tieto, Netlight",
  capital=500_000, tech="Data migration skills", reg="LOU", market="290 municipalities", uncertainty="Long cycles, project lumpiness",
  validation="Pitch 10 municipalities facing renewals", origin="Original finding", tags=["Hybrid", "Public-sector dependent"],
  scores=dict(demand=5, wtp=6, timing=6, gap=5, unit=5, speed=4, capeff=7, scale=4, feas=6),
  confidence="Medium", n_sources=3, assumption="Municipalities want to switch", wrong="Switching costs are the reason single bids exist.")

O(id=24, name="LOV/hemtjänst spend follow-up analytics",
  sector="Govtech / eldercare", customer="Municipalities with LOV choice systems (437 systems)",
  problem=">SEK 52bn paid via LOV in 2024 with weak follow-up data", alternatives="Adda 'Uppföljandekontroll inom socialtjänsten' consultants, Excel",
  evidence="W05 2a & Method 6; prop. 2025/26:164 better control of private providers (W02 §2.20)", concept="Analytics on visit data vs payments + audit service",
  why_now="New control requirements", revenue="SEK 100-300k/yr per municipality", decision_maker="Socialchef",
  competitors="Adda framework consultants, system vendors", capital=1_000_000, tech="Data integration with TES/Lifecare", reg="Socialtjänstlag, GDPR (sensitive data)",
  market="~180 LOV municipalities", uncertainty="Data access via incumbents", validation="Pilot with 1 municipality", origin="Original finding",
  tags=["Software", "Public-sector dependent", "Recurring revenue"],
  scores=dict(demand=5, wtp=5, timing=6, gap=7, unit=6, speed=4, capeff=5, scale=5, feas=4),
  confidence="Low", n_sources=3, assumption="Data accessible", wrong="Sensitive data and incumbents block access.")

O(id=25, name="Bid-competition insight product for public buyers (single-bid early warning)",
  sector="Govtech", customer="Contracting bodies, UHM, Statskontoret",
  problem="~20% single-bid tenders; buyers lack market analysis", alternatives="Tendium, Mercell data, consultants",
  evidence="W05 2b own TED analysis", concept="Market analysis per CPV/region from TED + national data", why_now="Statskontoret national database mandate",
  revenue="Subscriptions", decision_maker="Upphandlingschef", competitors="Tendium, Mercell, Opic", capital=600_000, tech="Data pipelines",
  reg="Open data", market="Small", uncertainty="WTP of buyers for analytics", validation="Sell 3 reports", origin="Original finding",
  tags=["Software", "Public-sector dependent"],
  scores=dict(demand=4, wtp=3, timing=5, gap=5, unit=4, speed=6, capeff=7, scale=5, feas=7),
  confidence="Low", n_sources=2, assumption="Buyers pay for analytics", wrong="State may provide this free.")

O(id=26, name="Municipal packaging-compensation reporting & kerbside-rollout operations software",
  sector="Waste", customer="290 municipalities / municipal waste companies",
  problem="Kerbside (fastighetsnära) packaging collection mandatory by 1 Jan 2027; compensation claims via Naturvårdsverket/Kammarkollegiet; cost coverage disputed; fees rising.",
  alternatives="EDP Future and other waste-admin systems, Excel, consultants",
  evidence="SFS 2025:825 deadline (W02 §2.8; W04 §16); Nacka/Göteborg cost-coverage issues (W04 S14b-c); textile volume +60% (W04 S12)",
  concept="Module that turns bin registry/weights into compensation reporting; deviation handling and resident comms.",
  why_now="Jan 2027 deadline, annual compensation cycle", revenue="SaaS SEK 100-400k/yr per organisation",
  decision_maker="Avfallschef", competitors="EDP Future, waste-system vendors", capital=1_500_000, tech="Integration with waste admin systems, weighing data",
  reg="Förpackningsförordningen; LOU", market="~150-290 buyers x SEK 200k = SEK 30-60m/yr",
  uncertainty="Incumbent waste systems add modules; procurement cycles", validation="Interview 10 waste companies; 2 paid pilots",
  origin="Original finding", tags=["Software", "Recurring revenue", "Public-sector dependent"],
  scores=dict(demand=6, wtp=6, timing=8, gap=3, unit=6, speed=3, capeff=5, scale=4, feas=5),
  confidence="Medium", n_sources=4, assumption="Incumbent systems don't cover compensation reporting", wrong="Small SAM and incumbent EDP integrates feature.")

# ---------------------------------------------------------------------------
# D. Property, BRF, buildings & energy
# ---------------------------------------------------------------------------
O(id=27, name="BRF compliance & maintenance-plan copilot (self-managed boards)",
  sector="Real estate / BRF", customer="~30,000 BRF boards, esp. self-managed and small",
  problem="Volunteer boards must track OVK, SBA, energy declaration (EPBD re-classing), lift inspection, radon, 50-year maintenance plan; 31% of owners worried about finances.",
  alternatives="Administrators (SBC, HSB, Riksbyggen, Nabo), Boappa, Planima/underhållsplan tools, Excel",
  evidence="BRF count & finances (W03 §2; W04 §23); EPBD in force 1 Jul 2026 (W02 §2.6); manager complaints (W05 C5)",
  concept="Compliance calendar + document vault + maintenance plan + fee scenarios + vendor quotes.",
  why_now="EPBD changes, fee stress", revenue="SEK 200-600/month per BRF", decision_maker="Board chair/treasurer",
  competitors="Nabo, Boappa, SBC, HSB, Riksbyggen, Planima", capital=800_000, tech="SaaS", reg="PBL, energideklaration law",
  market="30k BRFs x 10% adoption x SEK 4.8k = SEK 14m/yr (low ARPU)", uncertainty="Low WTP; managers bundle",
  validation="Facebook/BRF forum ads; 100 paying boards in 90 days", origin="Original finding",
  tags=["Software", "Bootstrappable", "Recurring revenue"],
  scores=dict(demand=6, wtp=4, timing=6, gap=5, unit=5, speed=7, capeff=7, scale=6, feas=8),
  confidence="Medium", n_sources=5, assumption="Boards pay for software separately", wrong="Boappa/Nabo already cover most of it.")

O(id=28, name="Bundled building-compliance inspection subscription (OVK + energy declaration + EPBD HVAC inspection + radon)",
  sector="Real estate / energy services", customer="BRFs, small landlords, municipal property portfolios, public buildings",
  problem="EPBD law in force 1 Jul 2026 adds energy declarations for all public buildings, renovation triggers and 3/5-year heating/ventilation/AC inspections, on top of OVK; owners juggle multiple certified vendors.",
  alternatives="Separate local OVK firms and energy experts; Sweco/WSP for large owners",
  evidence="Prop. 2025/26:159 (W02 §2.6); testing & inspection (71.20) turnover +31% 2022-24 (W03 §2); energy-efficiency consulting tenders highly competitive 11.5 bids (W05 2b - counter-signal)",
  concept="One subscription per building: schedule, perform (certified staff/partners), document, remind; digital reports.",
  why_now="New EPBD triggers", revenue="Annualised per building SEK 3-15k", decision_maker="BRF board / property manager",
  competitors="Local OVK/energy firms, Bengt Dahlgren, Sweco, inspection firms", capital=1_000_000,
  tech="Scheduling, field app; certified inspectors", reg="Certification required (Boverket, accredited bodies)",
  market="Large but commoditised; see W08", uncertainty="Price competition; certification capacity",
  validation="Offer bundle to 50 BRFs in one city", origin="Original finding",
  tags=["Hybrid", "Physical operations", "Regulated", "Recurring revenue"],
  scores=dict(demand=5, wtp=6, timing=5, gap=5, unit=5, speed=6, capeff=5, scale=5, feas=6),
  confidence="Medium", n_sources=4, assumption="Bundling wins vs cheapest local inspector", wrong="Commodity service with highly competitive pricing.")

O(id=29, name="OVK/SBA inspection field app for inspection firms",
  sector="Construction / inspection", customer="521 testing/inspection firms with employees",
  problem="Inspection reporting manual; missing national OVK data", alternatives="Generic forms apps, legacy tools",
  evidence="W03 §2 (71.20 growth; Boverket OVK digitalisation pre-study)", concept="Field app + structured reports",
  why_now="Growth of inspection market", revenue="SaaS per inspector", decision_maker="Firm owner", competitors="Generic field apps",
  capital=600_000, tech="Mobile app", reg="None", market="~1-2k inspectors", uncertainty="Niche size",
  validation="Interview 10 OVK firms", origin="Original finding", tags=["Software", "Recurring revenue"],
  scores=dict(demand=4, wtp=4, timing=5, gap=5, unit=5, speed=6, capeff=6, scale=4, feas=8),
  confidence="Low", n_sources=1, assumption="Pain exists", wrong="Tiny SAM.")

O(id=30, name="Stambyte/renovation procurement adviser for BRFs",
  sector="Real estate / construction", customer="BRFs facing pipe replacement and major renovations",
  problem="Stambyte costs SEK 250-500k per apartment; boards lack expertise to specify, tender and control contractors",
  alternatives="Byggkonsulter, administrators, contractors' own proposals", evidence="W03 §2 (costs, owner anxiety)",
  concept="Fixed-fee condition survey -> tender docs -> contractor comparison -> member communication",
  why_now="Ageing stock; fee stress", revenue="Fixed fee SEK 100-400k per project", decision_maker="BRF board",
  competitors="Local byggkonsulter, Sweco, WSP", capital=300_000, tech="Light", reg="None", market="Thousands of projects/decade",
  uncertainty="Project lumpiness; trust", validation="Win 2 projects via BRF networks", origin="Original finding",
  tags=["Bootstrappable", "Hybrid"],
  scores=dict(demand=6, wtp=6, timing=5, gap=5, unit=6, speed=5, capeff=8, scale=3, feas=7),
  confidence="Low", n_sources=2, assumption="Boards pay for independent advice", wrong="Local consultants already serve this.")

O(id=31, name="BRF arrears & collections workflow for self-managed associations",
  sector="Real estate / BRF", customer="Self-managed BRFs", problem="~14% of SBC BRFs handle collection cases monthly; fee hikes",
  alternatives="Administrators, inkasso firms", evidence="W04 §23 (SBC data)", concept="Reminders, payment plans, inkasso hand-off",
  why_now="Fee increases", revenue="Per case / subscription", decision_maker="Treasurer", competitors="Inkasso firms, administrators",
  capital=300_000, tech="Payments", reg="Inkassolagen", market="Small", uncertainty="Feature, not company",
  validation="Survey boards", origin="Original finding", tags=["Software", "Bootstrappable"],
  scores=dict(demand=4, wtp=3, timing=5, gap=4, unit=4, speed=7, capeff=7, scale=3, feas=7),
  confidence="Low", n_sources=1, assumption="Self-managed BRFs lack tools", wrong="Feature of any BRF platform.")

O(id=32, name="BRF EV-charging 'decision-to-install' service",
  sector="Energy / real estate", customer="~18,600 BRFs with parking lacking charging",
  problem="Board decision paralysis; grant paperwork; load management; installs fell from 2,061 BRFs (2022) to 742 (2024).",
  alternatives="Chargenode, Zaptec partners, Vattenfall InCharge, Eways, local electricians",
  evidence="Vendor analysis of Naturvårdsverket register (W04 S23); 50% grant (W04 S23b)",
  concept="Board decision pack, member survey, procurement, grant, install via partners, billing", why_now="EV share ~36% of new cars",
  revenue="Project margin + charging-as-a-service", decision_maker="BRF board", competitors="Chargenode, Eways, Vattenfall, Mer, Bee",
  capital=800_000, tech="Billing/load management via partners", reg="Grant rules (status 2026 to verify)",
  market="Thousands of BRFs", uncertainty="Crowded with charging vendors; grant availability", validation="Run 5 board decision packs",
  origin="Original finding", tags=["Hybrid", "Physical operations", "Recurring revenue"],
  scores=dict(demand=5, wtp=5, timing=5, gap=3, unit=5, speed=6, capeff=6, scale=4, feas=6),
  confidence="Medium", n_sources=3, assumption="Decision paralysis is solvable by a service", wrong="Market saturated by vendors offering free decision support.")

O(id=33, name="BRF fault-report SLA & transparency layer over property managers",
  sector="Real estate", customer="BRF boards using HSB/Riksbyggen/SBC", problem="Unanswered fault reports (82-95% 1-star reviews)",
  alternatives="Switch manager", evidence="Trustpilot samples (W05 C5)", concept="Tracking & escalation app", why_now="Dissatisfaction",
  revenue="Per BRF", decision_maker="Board", competitors="Boappa, Nabo", capital=300_000, tech="App", reg="None",
  market="Small", uncertainty="Managers won't integrate", validation="Pilot with 5 boards", origin="Original finding",
  tags=["Software", "Bootstrappable"],
  scores=dict(demand=4, wtp=2, timing=4, gap=4, unit=3, speed=7, capeff=7, scale=3, feas=6),
  confidence="Low", n_sources=1, assumption="Boards pay to monitor managers", wrong="Switching manager is the real solution.")

O(id=34, name="Water-damage prevention retrofit (leak sensors / auto shut-off) distributed via insurers and BRFs",
  sector="Insurance / property", customer="BRFs, villa owners, insurers",
  problem="Water damage is a major claims cost; no national insurer-distributed sensor programme",
  alternatives="Local plumbers; vattenfelsbrytare products; regional LF subsidies", evidence="LeakBot UK model (W06 #6); regional subsidies (W06 S18)",
  concept="Install + monitoring subscription, insurer co-funded", why_now="Claims inflation", revenue="Install fee + SEK 49-99/month",
  decision_maker="Homeowner/board; insurer", competitors="Waterguard, LeakBot, local installers", capital=2_000_000, tech="IoT hardware (sourced)",
  reg="Installer certification (Säker Vatten)", market="Millions of homes", uncertainty="Insurer partnership is critical",
  validation="Pilot with one regional insurer", origin="Foreign model (HomeServe LeakBot)",
  tags=["Hybrid", "Physical operations", "Recurring revenue"],
  scores=dict(demand=5, wtp=4, timing=5, gap=6, unit=5, speed=4, capeff=4, scale=6, feas=6),
  confidence="Low", n_sources=3, assumption="Insurers co-fund", wrong="Homeowners don't buy prevention; insurers move slowly.")

O(id=35, name="Backflow-protection retrofit programme with insurer-ready certificate",
  sector="Climate adaptation", customer="Villa owners, BRFs in flood-prone municipalities",
  problem=">60% of flood claims are sewer backflow, largely preventable; some insurers refuse cover",
  alternatives="Local plumbers; municipal subsidies", evidence="Svensk Försäkring on SOU 2025:51 (W04 S46)",
  concept="Survey + valve install + certificate", why_now="Cloudburst events", revenue="Project SEK 15-40k",
  decision_maker="Homeowner", competitors="Plumbers", capital=600_000, tech="Low; VVS certified installers", reg="VVS certification",
  market="Hundreds of thousands of basements", uncertainty="Reactive demand", validation="Campaign in one municipality post-event",
  origin="Original finding", tags=["Physical operations", "Bootstrappable"],
  scores=dict(demand=5, wtp=5, timing=5, gap=5, unit=5, speed=6, capeff=6, scale=3, feas=6),
  confidence="Low", n_sources=2, assumption="Demand without recent flood", wrong="Plumber shortage (W05 M3) limits delivery.")

O(id=36, name="Orphaned solar/battery aftercare network (post-installer-bankruptcy O&M)",
  sector="Energy services", customer="Owners of ~314,600 grid-connected PV plants, esp. customers of bankrupt installers",
  problem="196 solar-installer bankruptcies in 2025 (+33%) leave warranties and service orphaned; solar is the lowest-rated craftsman category on Reco.",
  alternatives="Original installer (if alive), local electricians, Otovo Care",
  evidence="W03 §5 (installed base, bankruptcies [L]); W05 C3; Otovo bought 24,000 Soly NL customers for ~EUR0.75M (W06 #7)",
  concept="Buy customer books from bankruptcy estates; offer inspection, inverter replacement, monitoring subscription; battery retrofit upsell.",
  why_now="Wave of bankruptcies 2024-26; inverters reaching mid-life", revenue="Service subscription SEK 79-149/month + repairs + battery upsell",
  decision_maker="Homeowner", competitors="Otovo, Svea Solar service, local electricians", capital=1_500_000,
  tech="Monitoring integrations (inverter APIs), field-service ops", reg="Electrical installation authorisation (Elsäkerhetsverket)",
  market="~314k plants; addressable orphaned subset unknown", uncertainty="Size of orphaned base and conversion rate",
  validation="Buy one small estate's customer list; measure conversion", origin="Foreign model (Otovo) + original",
  tags=["Hybrid", "Physical operations", "Recurring revenue"],
  scores=dict(demand=5, wtp=5, timing=7, gap=4, unit=5, speed=5, capeff=5, scale=5, feas=5),
  confidence="Low", n_sources=4, assumption="Orphaned owners convert at >10%", wrong="Electrician shortage; homeowners only pay on failure.")

O(id=37, name="Grid-connection case management for small DSOs",
  sector="Energy & grid", customer="~140 sub-scale local DSOs (median ~11k customers)",
  problem="Connection applications, capacity checks and queues handled manually; battery/flex connection debates; Svk allocation reform 2027",
  alternatives="Volue, Hansen, Trimble modules; Excel; consultants (Rejlers, Sweco)",
  evidence="W03 §5 (168 DSOs; queue; Ei rule changes)", concept="SaaS workflow + capacity pre-check", why_now="Queue reform 2027; Ei new tariff model Apr 2027",
  revenue="SaaS SEK 100-300k/yr per DSO", decision_maker="Nätchef", competitors="Volue, Hansen, Trimble, Rejlers",
  capital=1_500_000, tech="Grid data integration (NIS/GIS)", reg="Ellagen; NIS2 for DSOs", market="~140 x SEK 200k = SEK 28m/yr",
  uncertainty="Small SAM; incumbent utility IT", validation="Interview 15 DSOs", origin="Original finding",
  tags=["Software", "Recurring revenue", "High international expansion potential"],
  scores=dict(demand=5, wtp=6, timing=7, gap=4, unit=6, speed=4, capeff=5, scale=6, feas=5),
  confidence="Low", n_sources=3, assumption="DSO pain is unsolved", wrong="Tiny SAM; utility-IT incumbents.", intl=True)

O(id=38, name="Independent grid-connection consultancy for C&I, depots and BESS",
  sector="Energy & grid", customer="Logistics depots, industrial sites, BESS developers, housing developers",
  problem="Long queues, capacity refusals, complex applications", alternatives="Sweco, Rejlers, AFRY, ÅF",
  evidence="W03 §5; SvK queue >175 GW [L]", concept="Application prep, flexible-connection design, tariff optimisation",
  why_now="Electrification", revenue="Project fees", decision_maker="Project/energy manager", competitors="Sweco, Rejlers, AFRY",
  capital=200_000, tech="Power-system expertise", reg="Ellagen", market="Growing", uncertainty="Requires grid-engineering credentials",
  validation="Win 3 paid applications", origin="Original finding", tags=["Bootstrappable", "Hybrid"],
  scores=dict(demand=6, wtp=6, timing=7, gap=4, unit=6, speed=6, capeff=8, scale=3, feas=5),
  confidence="Low", n_sources=2, assumption="Founder has power-systems competence", wrong="Big engineering firms dominate.")

O(id=39, name="Craftsman quote -> binding contract -> change-order -> ROT-check tool",
  sector="Construction / consumer", customer="Small trade firms (and their consumer clients)",
  problem="Boende 17% of complaints, half craftsman-related; ARN Bostad 3,057 cases; ROT rejections; price raised mid-job",
  alternatives="Bygglet, Next, Fieldly, Hantverkarformuläret 17, Offerta/Reco", evidence="W05 C2; W04 ARN table",
  concept="Digital quote/contract/change-order with BankID and ROT pre-check", why_now="ROT control bill 2027 (W02 §2.17)",
  revenue="SaaS SEK 200-500/month", decision_maker="Trade firm owner", competitors="Bygglet, Next One, Fieldly, Struqtur",
  capital=800_000, tech="BankID signing, Skatteverket ROT rules", reg="Konsumenttjänstlagen", market="Tens of thousands of firms",
  uncertainty="Crowded PE-owned field-service SaaS", validation="Interview 20 trades", origin="Original finding",
  tags=["Software", "Recurring revenue"],
  scores=dict(demand=5, wtp=4, timing=5, gap=3, unit=5, speed=5, capeff=6, scale=5, feas=7),
  confidence="Medium", n_sources=3, assumption="Trades value dispute prevention", wrong="Existing field-service SaaS adds this.")

O(id=40, name="Textile take-back service for property owners and housing companies",
  sector="Waste / circular", customer="Housing companies and BRFs in municipalities without kerbside textile collection",
  problem="Textile collection mandatory since 2025; 4 in 10 municipalities only collect at recycling centres", alternatives="Charities, Human Bridge, municipal ÅVC",
  evidence="W04 §16 (S12, S15b, S15c)", concept="Bins + collection + sorting partner", why_now="+60% textile volumes",
  revenue="Per bin per month", decision_maker="Property manager", competitors="Charities, Human Bridge, Sysav", capital=1_500_000,
  tech="Logistics", reg="Waste permits", market="Moderate", uncertainty="Low margins", validation="Pilot with 1 housing company",
  origin="Original finding", tags=["Physical operations", "Recurring revenue"],
  scores=dict(demand=4, wtp=3, timing=6, gap=4, unit=3, speed=5, capeff=4, scale=4, feas=5),
  confidence="Low", n_sources=3, assumption="Owners pay for take-back", wrong="Charities collect for free.")

# ---------------------------------------------------------------------------
# E. Automotive
# ---------------------------------------------------------------------------
O(id=41, name="EV battery-health (SoH) certificate workflow for small used-car dealers",
  sector="Automotive", customer="Independent used-car dealers",
  problem="Since 1 Nov 2025 goods declaration can show battery SoH 1-100; ARN motor complaints +20% with small dealers least compliant",
  alternatives="Dekra tests (Bilia chose Dekra Jan 2026), Aviloo, OEM tools", evidence="W04 §17 (S21, S21c); W05 C1",
  concept="Mobile SoH test + certificate attached to listing", why_now="Rising used-EV volumes", revenue="Per test SEK 300-900",
  decision_maker="Dealer", competitors="Dekra, Aviloo, Bilprovningen/Opus", capital=700_000, tech="OBD/test hardware partnerships",
  reg="Goods declaration rules", market="Used EV transactions (to verify)", uncertainty="Dekra/Aviloo capture",
  validation="Sell 100 tests to 10 dealers", origin="Original finding", tags=["Hybrid", "Physical operations"],
  scores=dict(demand=5, wtp=4, timing=7, gap=2, unit=5, speed=6, capeff=6, scale=4, feas=7),
  confidence="Medium", n_sources=4, assumption="Small dealers will pay per test", wrong="Incumbents already have it; commodity pricing.")

O(id=42, name="Used-car dealer warranty & dispute-compliance layer",
  sector="Automotive", customer="Small used-car dealers and their buyers",
  problem="Motor ARN cases 6,664 (+20%); 74% compliance; disputes over used cars", alternatives="Fragus, Garantibolaget, Blocket, MRF",
  evidence="ARN 2025 (W05 C1)", concept="Inspection + warranty + dispute handling bundle", why_now="Complaints rising",
  revenue="Per car warranty premium share", decision_maker="Dealer", competitors="Fragus, Garantibolaget, Bilgaranti, Kvdbil",
  capital=2_000_000, tech="Claims platform; insurance partner", reg="Insurance distribution (IDD)", market="Hundreds of thousands of used-car sales",
  uncertainty="Insurance partner needed; dealers with poor compliance are poor customers", validation="Pilot with 5 dealers",
  origin="Original finding", tags=["Hybrid", "Regulated"],
  scores=dict(demand=6, wtp=3, timing=5, gap=3, unit=4, speed=4, capeff=4, scale=4, feas=4),
  confidence="Medium", n_sources=2, assumption="Bad dealers want compliance", wrong="Adverse selection: non-compliant dealers won't buy.")

O(id=43, name="Workshop capacity & booking SaaS for small car workshops",
  sector="Automotive", customer="Independent workshops", problem="Mechanic shortage; capacity bottlenecks",
  alternatives="Autobutler, Wehlo, dealer systems", evidence="AF shortage (W05 M3)", concept="Booking & capacity optimisation",
  why_now="Shortage", revenue="SaaS", decision_maker="Owner", competitors="Autobutler, Wehlo, Mekonomen systems",
  capital=800_000, tech="SaaS", reg="None", market="Thousands", uncertainty="Crowded", validation="Interview 15 workshops",
  origin="Original finding", tags=["Software", "Recurring revenue"],
  scores=dict(demand=4, wtp=4, timing=4, gap=2, unit=5, speed=5, capeff=6, scale=4, feas=8),
  confidence="Low", n_sources=1, assumption="Gap exists", wrong="Chains own the tools.")

# ---------------------------------------------------------------------------
# F. Care, consumer & other
# ---------------------------------------------------------------------------
O(id=44, name="Continuity-aware hemtjänst scheduling for private LOV providers",
  sector="Eldercare", customer="341 hemtjänst firms with 20+ staff; municipal providers",
  problem="Continuity requirements (fast omsorgskontakt), minute-scheduling conflicts in ~100 municipalities; incumbent systems",
  alternatives="Tieto Laps Care, Phoniro/TES, Alfa eCare, Carefox", evidence="W03 §1; W05 C9",
  concept="Scheduling optimisation for continuity and travel", why_now="New SoL 2025:400", revenue="Per caregiver per month",
  decision_maker="Provider CEO", competitors="Laps Care, Alfa eCare, Carefox, Phoniro", capital=1_500_000, tech="Optimisation + integrations",
  reg="SoL; GDPR sensitive data", market="Hundreds of providers", uncertainty="Thin provider margins (5.6%)", validation="Pilot with 2 providers",
  origin="Original finding", tags=["Software", "Recurring revenue"],
  scores=dict(demand=5, wtp=3, timing=6, gap=4, unit=4, speed=4, capeff=5, scale=5, feas=5),
  confidence="Low", n_sources=3, assumption="Providers will pay", wrong="Margins too thin; municipal systems mandated.")

O(id=45, name="Senior household-help RUT bundle operator",
  sector="Consumer services", customer="Seniors 65+ (41% of RUT buyers) and adult children",
  problem="Fragmented services (cleaning, garden, IT, snow); trust", alternatives="Hemfrid, local firms, Hemtjänst",
  evidence="RUT SEK 8.9bn 2025 (W04 §21)", concept="Subscription bundle with vetted staff", why_now="Ageing (85+ +59% by 2035, W01)",
  revenue="Subscription after RUT", decision_maker="Senior / adult child", competitors="Hemfrid, Freska, local firms",
  capital=1_500_000, tech="Scheduling", reg="RUT rules; F-skatt", market="SEK 8.9bn RUT pool", uncertainty="Labour-intensive, low margin",
  validation="Pilot in one suburb", origin="Original finding", tags=["Physical operations", "Recurring revenue"],
  scores=dict(demand=6, wtp=6, timing=6, gap=4, unit=4, speed=6, capeff=5, scale=4, feas=7),
  confidence="Medium", n_sources=3, assumption="Bundle beats single-service firms", wrong="Staff cost and churn.")

O(id=46, name="Dödsbo / estate administration service",
  sector="Funeral / legal", customer="~92,200 bereaved households per year", problem="Estate inventory, account closures; rogue operators",
  alternatives="Fonus/Familjens Jurist (SEK 444m revenue), Fenix, Lexly, banks", evidence="W04 Funeral section",
  concept="Fixed-price digital dödsbo service", why_now="Trust gap", revenue="SEK 5-15k per estate", decision_maker="Next of kin",
  competitors="Familjens Jurist, Fenix, Lexly", capital=1_000_000, tech="Workflow + bank integrations", reg="Ärvdabalken",
  market="92k estates/yr", uncertainty="Channel via funeral bureaus dominated by Fonus", validation="Partner with 3 independent bureaus",
  origin="Foreign model (UK Farewill) / Swedish Fenix exists", tags=["Hybrid"],
  scores=dict(demand=5, wtp=5, timing=4, gap=3, unit=5, speed=5, capeff=5, scale=4, feas=6),
  confidence="Medium", n_sources=3, assumption="Channel access", wrong="Fenix and Fonus already cover it.")

O(id=47, name="Rural primary-care permanent-doctor pool (anti-hyrläkare)",
  sector="Healthcare", customer="Rural regions (Värmland, Västernorrland, etc.)",
  problem="Regions spent ~SEK 7.9bn on hired staff (2022); Västernorrland 18.3% of staff costs", alternatives="Staffing agencies; telemedicine (Kry, Min Doktor)",
  evidence="W05 Method 6", concept="Employed rotating doctor pool + telemedicine", why_now="Regions' hyrpersonal exit targets",
  revenue="Contracts with regions", decision_maker="Region HR/primary-care director", competitors="Staffing agencies, Kry, Capio",
  capital=10_000_000, tech="Telemedicine", reg="IVO registration; healthcare regulation", market="SEK bn", uncertainty="Regulation and recruitment",
  validation="Discuss with 2 regions", origin="Original finding", tags=["Capital intensive", "Regulated", "Public-sector dependent"],
  scores=dict(demand=7, wtp=7, timing=6, gap=4, unit=4, speed=2, capeff=2, scale=5, feas=3),
  confidence="Medium", n_sources=3, assumption="Doctors join", wrong="Founder-fit very low; regulated.")

O(id=48, name="Driving-test readiness scoring for driving schools",
  sector="Education", customer="Driving schools (STR ~75%)", problem="376,000 failed tests in 2025; government mandate to reduce",
  alternatives="Theory apps (STR, Körkortonline)", evidence="W04 §11", concept="Lesson logging + readiness score", why_now="Govt mandate",
  revenue="Per student", decision_maker="School owner", competitors="STR apps, Körkortonline, Trafiko", capital=500_000,
  tech="App", reg="Transportstyrelsen", market="~100k new licences/yr", uncertainty="WTP of schools", validation="Pilot with 5 schools",
  origin="Original finding", tags=["Software", "Recurring revenue"],
  scores=dict(demand=5, wtp=4, timing=5, gap=5, unit=5, speed=6, capeff=7, scale=4, feas=7),
  confidence="Low", n_sources=2, assumption="Schools value fewer failed tests", wrong="Failed tests earn schools revenue (more lessons).")

O(id=49, name="Restaurant distress early-warning via accountants",
  sector="Hospitality", customer="Independent restaurants via accounting firms", problem="Most bankruptcy-prone sector (2.8%)",
  alternatives="Accountants, Caspeco analytics", evidence="W04 §14", concept="Cash-flow cockpit", why_now="VAT cliff 2027 (W01 A3)",
  revenue="SaaS via bureaus", decision_maker="Owner", competitors="Caspeco, Fortnox", capital=500_000, tech="Ledger integration",
  reg="None", market="Tens of thousands", uncertainty="Distressed buyers don't pay", validation="Pilot via 2 bureaus", origin="Original finding",
  tags=["Software"],
  scores=dict(demand=4, wtp=2, timing=5, gap=4, unit=3, speed=6, capeff=6, scale=4, feas=7),
  confidence="Low", n_sources=2, assumption="Willingness to pay", wrong="Distressed customers churn.")

O(id=50, name="Inspection-ready digital farm binder (livestock)",
  sector="Agriculture", customer="~14,000 cattle holdings", problem="~2.7 h/week admin; subsidy admin ~SEK 34k/firm",
  alternatives="Jordbruksverket e-services, Växa, Swedbank tools", evidence="W04 §12", concept="Record keeping for inspections",
  why_now="Admin burden", revenue="Subscription via advisers", decision_maker="Farmer", competitors="Växa, Jordbruksverket, Dataväxt",
  capital=800_000, tech="App", reg="CAP", market="Shrinking", uncertainty="Low ARPU", validation="Interview 20 farmers",
  origin="Original finding", tags=["Software", "Recurring revenue"],
  scores=dict(demand=4, wtp=3, timing=4, gap=4, unit=4, speed=4, capeff=5, scale=4, feas=6),
  confidence="Low", n_sources=2, assumption="Gap vs Växa", wrong="Shrinking buyer base.")

O(id=51, name="Household/SME telecom bill audit (success fee)",
  sector="Consumer services", customer="Households and SMEs", problem="Billing errors, binding contracts (Telia 87% 1-star)",
  alternatives="Price comparison sites", evidence="W05 C4", concept="Audit + switch + claim", why_now="Complaints",
  revenue="Success fee", decision_maker="Household", competitors="Comparison sites", capital=300_000, tech="Bill parsing",
  reg="None", market="Large", uncertainty="Low WTP", validation="100 audits", origin="Original finding", tags=["Software", "Bootstrappable"],
  scores=dict(demand=4, wtp=2, timing=3, gap=4, unit=3, speed=7, capeff=7, scale=4, feas=7),
  confidence="Low", n_sources=1, assumption="Savings large enough", wrong="Small savings per customer.")

O(id=52, name="VA (water & sewer) renewal and tariff-justification analytics",
  sector="Water infrastructure", customer="290 VA principals", problem="SEK 590bn need to 2040; tariffs +7.5% in 2026",
  alternatives="Sweco, WSP, VA-asset systems", evidence="W01 megatrend 9; W03 VA", concept="Asset-renewal planning + taxa model",
  why_now="Tariff pressure", revenue="SaaS", decision_maker="VA chief", competitors="Sweco, WSP, DHI, VA SYD tools", capital=1_500_000,
  tech="Asset data", reg="Vattentjänstlagen", market="290 x SEK 150k", uncertainty="Slow procurement", validation="Interview 10 VA orgs",
  origin="Original finding", tags=["Software", "Public-sector dependent", "Recurring revenue"],
  scores=dict(demand=5, wtp=5, timing=6, gap=4, unit=5, speed=3, capeff=5, scale=5, feas=5),
  confidence="Low", n_sources=2, assumption="Analytics gap", wrong="Consultancies own the relationship.")
