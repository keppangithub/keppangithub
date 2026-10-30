"""Score adjustments adopted after the adversarial review (research/10_adversarial_review.md, 'W10').

Ten opportunities were challenged by the independent reviewer (ids 4, 1, 6, 7, 13, 15, 21, 22, 38, 2); all ten
proposed adjustments were adopted because each rests on cited evidence (direct-award limit SEK 700k, closed Adda
area-7 framework to 2030, MCF's ~1,800-entity NIS2 count, incumbent bundle prices).
The reviewer flagged that six promoted ids (30, 17, 5, 27, 16, 20) had not been stress-tested; the lead analyst applied
the same lens to them (marked 'lead-analyst pass') so that no unreviewed score is compared with reviewed ones.
"""
ADJ = {
    4: dict(demand=7, wtp=7, timing=8, gap=4, unit=6, speed=4, scale=4, feas=3),
    1: dict(demand=7, wtp=7, gap=4, speed=7),
    6: dict(demand=4, wtp=4, gap=6, unit=5, speed=5, scale=4),
    7: dict(wtp=6, speed=4),
    13: dict(demand=5, wtp=3, gap=3, unit=5, scale=5, feas=5),
    15: dict(demand=5, wtp=4, timing=6, gap=4, unit=4),
    21: dict(demand=6, wtp=5, gap=3, unit=4, speed=5, scale=3, feas=5),
    22: dict(demand=4, wtp=4, gap=2, unit=4, scale=2),
    38: dict(wtp=7, feas=4),
    2: dict(demand=3, wtp=3, gap=4, speed=3, scale=6),
    # lead-analyst pass on promoted ids
    5: dict(demand=5, wtp=5, gap=4, speed=3),
    30: dict(gap=4),
    17: dict(gap=4, unit=5),
    20: dict(demand=4, gap=4),
    14: dict(demand=5),
    27: dict(gap=4),
    16: dict(unit=5),
}

RATIONALE = {
    4: "W10: Adda area-7 framework closed to new suppliers until Feb 2030; direct awards capped at SEK 700k total contract value (~2-year retainers); per-client säkerhetsskyddsavtal and vetting; spend largely capex/in-house salaries; 1 Jan 2027 notification duty is one-off. Viable only with cleared, referenced founders or as subcontractor.",
    1: "W10: MCF cites ~1,500 companies + 310 municipalities/regions (not 5-8k); public costs 'within existing budgets'; KLASSA (410 orgs, NIS2-mapped) and Opsio fixed-price packages narrow the gap. Still law-in-force, fits the direct-award limit, low capital -> stays #1.",
    6: "W10: FMV säkerhetsskyddsavtal is initiated by the customer, so SMEs pay only when a contract exists; subsidised substitutes (Business Sweden SEK 300m, Vinnova). Fold into #1/#4 as a product line.",
    7: "W10: SBOM tools at EUR 49-149/month anchor prices; buyers wait for Dec 2027, so first revenue is slow. Most durable driver otherwise.",
    13: "W10: Fortnox Byråpartner suite costs SEK 499/month incl. case management and KYC; the backlash is about price, not a desire for another tool. Reject as scored.",
    15: "W10: only 13 accounting-firm listings on Bolagsplatsen; most transfers are sub-SEK 1m client books, so fees far below SEK 200k. Fold into #16 as sourcing engine.",
    21: "W10: SEK 40k/month exceeds the SEK 700k direct-award limit within 2 years; neighbour municipalities share procurement staff; reference-based tenders.",
    22: "W10: Tendium AI bid studio from EUR 125/month commoditises bid writing; per-bid fees unproven.",
    38: "W10: private buyers face no LOU; SvK 'ready-first' allocation rewards prepared applications; founder-gated on power-systems credentials.",
    2: "W10: no buyer mandate; suppliers answer questionnaires for free; KLASSA/MCF could publish a free baseline. Keep as free lead-gen inside #1.",
    5: "Lead-analyst pass: same procurement (LOU/frameworks) and classification barriers as #4; Cosafe/4C incumbents.",
    30: "Lead-analyst pass: independent byggkonsulter already serve BRF renovations; gap not demonstrated.",
    17: "Lead-analyst pass: crowded bureau market incl. Wint; staff costs ~57% of revenue (Oxceed) cap margins.",
    14: "Lead-analyst pass: payroll/admin roles in national surplus (W05 M3) weaken the labour-saving pitch; Fortnox marketplace AI and Briox Lerry already shipping (W09 §1).",
    27: "Lead-analyst pass: Boappa (SEK 3,900-13,900/yr, >2,000 BRFs, churn <1.5%) can add a compliance calendar cheaply (W08 §1).",
    16: "Lead-analyst pass: PE acquirers (Cedra, Azets, Aspia, Accru, Freedom) compete for targets; clients follow people, raising post-deal churn (W09 §2).",
    20: "Lead-analyst pass: NPA ~85% share and PRO portals; small-producer burden unverified.",
}
