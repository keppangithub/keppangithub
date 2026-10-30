# Sweden Opportunity Intelligence, 2026–2030

This study set out to find businesses a new founder could launch in Sweden in 2026–2028 with evidence of demand, good timing, sound economics and a path to becoming a substantial company by 2030.

**Reference date:** 29 October 2026. **Research cutoff:** 30 October 2026.

## Headline

- **Recommended business:** a fixed-price **NIS2 compliance operations partner** (Swedish named vCISO + ISMS + incident runbooks + board training) for municipal utilities and mid-size entities under Cybersäkerhetslagen. It adds **CRA product-security services in 2027**.
- **Score and capital:** weighted score 69.0 (next best 61.0). Evidence confidence is high. Peak funding need is ~SEK 0.8–1.6m (modelled).
- **Status:** not proven. It must pass the 45-day validation gate in the roadmap before more money is committed.

## Deliverables

| # | Deliverable | File |
|---|---|---|
| 1 | Executive intelligence brief | [01_executive_intelligence_brief.md](01_executive_intelligence_brief.md) |
| 2 | Sweden opportunity landscape: macro, structural opportunity map, 28-sector matrix, spend evidence | [02_sweden_opportunity_landscape.md](02_sweden_opportunity_landscape.md) |
| 3 | 50-opportunity database (52 opportunities, scores, rankings) | [03_opportunity_database.md](03_opportunity_database.md), [Excel](output/sweden_opportunity_database.xlsx), [CSV](output/opportunity_database.csv) |
| 4 | Competitive intelligence dossiers | [04_competitive_intelligence_dossiers.md](04_competitive_intelligence_dossiers.md) |
| 5 | Top 10 investment shortlist, including adversarial re-ranking | [05_top10_investment_shortlist.md](05_top10_investment_shortlist.md) |
| 6 | Top five deep dives | [06_top5_deep_dives.md](06_top5_deep_dives.md) |
| 7 | Recommended business | [07_recommended_business.md](07_recommended_business.md) |
| 8 | 90-day founder roadmap | [08_90_day_roadmap.md](08_90_day_roadmap.md) |
| 9 | Sources, methodology and uncertainty register | [09_sources_methodology_uncertainty.md](09_sources_methodology_uncertainty.md), [source index (634 URLs)](output/source_index.csv) |

## Research workstreams (evidence base)

| Code | Workstream |
|---|---|
| W01 | [Macro and megatrends](research/01_macro.md) |
| W02 | [Regulation](research/02_regulation.md) |
| W03 | [Sector screen A](research/03_sectors_A.md) |
| W04 | [Sector screen B](research/04_sectors_B.md) |
| W05 | [Demand signals: complaints, TED procurement analysis, hiring, spending leakage](research/05_demand_signals.md) |
| W06 | [Foreign models](research/06_foreign_models.md) |
| W07 | [Competitors: cyber and public sector](research/07_competitors_cyber_public.md) |
| W08 | [Competitors: property and energy](research/08_competitors_property_energy.md) |
| W09 | [Competitors: SME services, waste, automotive and care](research/09_competitors_sme_waste_auto_care.md) |
| W10 | [Adversarial investment-committee review](research/10_adversarial_review.md) |

## Reproducing the numbers

```bash
cd model
pip install openpyxl
python3 build.py         # rebuilds output/*.xlsx, *.csv, tables.md and 03_opportunity_database.md
python3 source_index.py  # rebuilds output/source_index.csv
```

The model files:

| File | Contents |
|---|---|
| `opportunities.py` | The 52 opportunities, their fields, criteria, weights and pre-review scores |
| `adversarial.py` | Post-review adjustments, with a rationale for each |
| `rank.py` | The seven ranking views |
| `sizing.py` | TAM/SAM/SOM for the top 20 |
| `finance.py` and `models_top20.py` | 36-month models and sensitivities |

## Integrity notes

- All scores, market sizes and projections are **analyst estimates or model outputs**, labelled as such. They are not observed data.
- No customer interviews were held and no organisations were contacted. No leads are claimed.
- Several items could not be verified; all of them are listed in the uncertainty register (Deliverable 9 §4). The main ones:
  - the web-search budget ran out during the early workstreams;
  - Reddit, Flashback and app-store evidence was not collected;
  - procurement analysis covers TED only.
