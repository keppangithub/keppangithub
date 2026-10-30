"""Bottom-up market sizing for the top 20 (Phase 6). MODELLED ESTIMATES, NOT MEASURED DATA.

TAM = relevant buyers x annual spend per buyer on the problem (low / base / high).
SAM = TAM x share realistically addressable by a new Swedish entrant (segment fit, channel reach).
SOM = plausible customers won in 3-5 years x annual revenue per customer.
"""

SIZING = {
    # id: dict(buyers=(lo, base, hi), buyer_basis, spend=(lo, base, hi), spend_basis, sam_share, sam_basis, som_customers, som_arpa)
    4: dict(buyers=(500, 711, 1000), buyer_basis="290 municipalities + 21 regions + ~400 municipal companies/ports/utilities (assumption on companies); private säkerhetskänsliga operators in high case",
            spend=(150_000, 300_000, 600_000), spend_basis="External preparedness/säkerhetsskydd advice per org/yr; Uppsala advertised SEK 100m over up to 4 years (W07 Area 2) is a large-city outlier; state grants SEK 739m to municipalities in 2025 (W07)",
            sam_share=0.5, sam_basis="Small/mid organisations outside large-city frameworks", som_customers=40, som_arpa=330_000),
    1: dict(buyers=(1_500, 4_000, 8_000), buyer_basis="Government estimate 'drygt 1,500 företag' >=50 FTE (W03 S39) vs secondary 5,000-8,000 entities incl. public (W02 §2.1) - contradictory",
            spend=(150_000, 250_000, 400_000), spend_basis="Ongoing NIS2 advisory SEK 10-30k/month (W07 benchmarks, L-M) + tooling 30-200k/yr (W07, L)",
            sam_share=0.3, sam_basis="Municipal companies and 50-500 FTE entities willing to buy fixed-price bundles", som_customers=60, som_arpa=250_000),
    6: dict(buyers=(400, 800, 1_500), buyer_basis="SOFF 400-500 members (W07 Area 3) + non-member aspirants (assumption)",
            spend=(50_000, 100_000, 200_000), spend_basis="Programme fee SEK 150-500k amortised over 3 yrs + retainer (assumption)",
            sam_share=0.5, sam_basis="SMEs without in-house security function", som_customers=30, som_arpa=200_000),
    7: dict(buyers=(1_000, 2_000, 3_500), buyer_basis="Swedish makers of products with digital elements; ~1,500 machinery firms with employees (W03 §4) + electronics/IoT/software (assumption)",
            spend=(100_000, 200_000, 400_000), spend_basis="PSIRT/SBOM retainer + readiness work (assumption; tooling EUR 49-149/month W07)",
            sam_share=0.4, sam_basis="SMEs without product-security teams", som_customers=45, som_arpa=250_000),
    13: dict(buyers=(6_000, 8_126, 9_000), buyer_basis="Accounting firms with employees (SCB FDB 2025, W03 §9)",
             spend=(12_000, 21_600, 36_000), spend_basis="~3 seats x SEK 400-1,000/month (byrå seat prices 199-499, W09 §1)",
             sam_share=0.5, sam_basis="Firms using >1 ledger or dissatisfied with Fortnox fees", som_customers=400, som_arpa=21_600),
    15: dict(buyers=(400, 700, 1_000), buyer_basis="Firm/book transfers per year; ~14,200 small AB firms + 8,900 sole traders (W03 §9); 3-7% transfer rate (assumption)",
             spend=(100_000, 150_000, 250_000), spend_basis="Broker/valuation fee per deal (assumption)",
             sam_share=0.3, sam_basis="Deals using an intermediary", som_customers=15, som_arpa=200_000),
    21: dict(buyers=(600, 1_000, 1_500), buyer_basis=">half of contracting organisations run 1-5 tenders/yr (W04 §15)",
             spend=(200_000, 400_000, 800_000), spend_basis="Arvidsjaur ~SEK 456k/yr retainer; Timrå SEK 1.372m/yr (W07 Area 5)",
             sam_share=0.25, sam_basis="Bodies willing to outsource (rest staff in-house or share with neighbours)", som_customers=20, som_arpa=480_000),
    22: dict(buyers=(8_000, 13_000, 20_000), buyer_basis="~13,000 firms bid in 2024 (W05 2a) + non-bidders",
             spend=(20_000, 50_000, 100_000), spend_basis="Outsourced bid support per firm/yr (assumption)",
             sam_share=0.1, sam_basis="Firms that outsource bid writing", som_customers=110, som_arpa=30_000),
    38: dict(buyers=(500, 1_000, 2_000), buyer_basis="C&I/BESS/depot connection cases per year (assumption; SvK queue >175 GW, W03 §5 [L])",
             spend=(80_000, 150_000, 300_000), spend_basis="Application/design study fee (assumption; SvK investigation fee SEK 100k, W08 §6)",
             sam_share=0.4, sam_basis="Cases outsourced to independent advisers", som_customers=36, som_arpa=120_000),
    2: dict(buyers=(10_000, 20_000, 40_000), buyer_basis="Suppliers to NIS2 entities (assumption)",
            spend=(5_000, 15_000, 30_000), spend_basis="Attestation fee (assumption)",
            sam_share=0.2, sam_basis="Suppliers in buyer-sponsored programmes", som_customers=900, som_arpa=15_000),
    5: dict(buyers=(311, 600, 900), buyer_basis="290 municipalities + 21 regions + essential private firms",
            spend=(50_000, 100_000, 200_000), spend_basis="SaaS per org/yr (assumption)",
            sam_share=0.5, sam_basis="Orgs not locked into incumbents", som_customers=40, som_arpa=100_000),
    17: dict(buyers=(12_000, 20_000, 30_000), buyer_basis="Installers & contractors with employees (5,717 el + 5,105 VVS + ... W03 §2)",
             spend=(24_000, 42_000, 72_000), spend_basis="Bookkeeping fees SEK 2-6k/month (assumption)",
             sam_share=0.1, sam_basis="Firms switching bureau within 3-5 yrs", som_customers=150, som_arpa=42_000),
    30: dict(buyers=(500, 1_000, 1_500), buyer_basis="BRF stambyte/major renovation projects per year (assumption)",
             spend=(100_000, 200_000, 400_000), spend_basis="Independent adviser fee per project (assumption)",
             sam_share=0.3, sam_basis="Boards buying independent advice", som_customers=15, som_arpa=200_000),
    27: dict(buyers=(30_000, 33_865, 34_000), buyer_basis="Active BRFs (SCB via ChargeNode, W08 §0)",
             spend=(3_900, 6_600, 13_900), spend_basis="Boappa price ladder SEK 3,900-13,900/yr (W08 §1)",
             sam_share=0.45, sam_basis="Self-managed share estimate 40-55% (W08 §0, L)", som_customers=800, som_arpa=6_600),
    16: dict(buyers=(14_217, 14_217, 14_217), buyer_basis="Small AB accounting firms (Spiris via W03 §9)",
             spend=(1_000_000, 1_100_000, 1_200_000), spend_basis="SEK 15.7bn / 14,217 firms (W03 §9)",
             sam_share=0.2, sam_basis="Micro firms with retiring owners open to sale", som_customers=5, som_arpa=4_000_000),
    20: dict(buyers=(10_000, 20_000, 40_000), buyer_basis="Small packaging producers/e-tailers (unverified; W02 §2.8)",
             spend=(1_500, 3_000, 6_000), spend_basis="UK service GBP 535/yr (W09 §4)",
             sam_share=0.5, sam_basis="Micro-producers without in-house compliance", som_customers=1_500, som_arpa=3_500),
    14: dict(buyers=(6_000, 8_126, 9_000), buyer_basis="Accounting firms with employees (W03 §9)",
             spend=(15_000, 30_000, 60_000), spend_basis="Per-client AI fee x client files (W09 §1 per-client prices)",
             sam_share=0.4, sam_basis="Firms adopting third-party AI", som_customers=300, som_arpa=30_000),
    9: dict(buyers=(10_000, 15_000, 20_000), buyer_basis="Small obliged entities; 12,888 accounting firms AML-registered (W03 §9)",
            spend=(2_400, 8_000, 16_650), spend_basis="Spiris 199/client/yr to Lundify SEK 16,650/yr (W07 Area 6)",
            sam_share=0.2, sam_basis="Entities not served by bundled tools", som_customers=400, som_arpa=8_400),
    8: dict(buyers=(1_500, 2_500, 3_500), buyer_basis="Machine builders/integrators (W03 §4)",
            spend=(20_000, 40_000, 80_000), spend_basis="CE software/consulting per firm/yr (assumption)",
            sam_share=0.4, sam_basis="SMEs without CE engineers", som_customers=150, som_arpa=40_000),
    23: dict(buyers=(20, 40, 60), buyer_basis="Municipal core-system switches per year (assumption)",
             spend=(250_000, 400_000, 800_000), spend_basis="Migration/requirements project (assumption)",
             sam_share=0.5, sam_basis="Projects buying independent support", som_customers=3, som_arpa=400_000),
}


def size(oid):
    d = SIZING[oid]
    tam = tuple(b * s for b, s in zip(d["buyers"], d["spend"]))
    sam = tuple(t * d["sam_share"] for t in tam)
    som = d["som_customers"] * d["som_arpa"]
    return dict(tam_low=tam[0], tam_base=tam[1], tam_high=tam[2], sam_low=sam[0], sam_base=sam[1], sam_high=sam[2], som=som,
                som_share_of_sam=som / sam[1] if sam[1] else None, **d)
