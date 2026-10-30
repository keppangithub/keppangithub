"""Builds all quantitative outputs: Excel workbook, CSVs and markdown tables.

Usage:  cd model && python3 build.py
Outputs go to ../output/.
"""
import csv
import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from adversarial import ADJ, RATIONALE
from finance import sensitivities, simulate, EMPLOYER_FEE
from models_top20 import M
from opportunities import CRITERIA, OPPS, TAG_KEYS
from rank import views, weighted
from sizing import size

OUT = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUT, exist_ok=True)

FX = {"EUR/SEK": 11.0416, "USD/SEK": 9.9074, "GBP/SEK": 13.1996}  # closing 2026-10-29, poundsterlinglive.com history pages

# --- scores before and after adversarial review -----------------------------------------
for o in OPPS:
    o["score_pre"] = weighted(o)
    adj = ADJ.get(o["id"], {})
    o["scores_post"] = {**o["scores"], **adj}
    o["score"] = weighted(o, o["scores_post"])
pre_rank = {o["id"]: i for i, o in enumerate(sorted(OPPS, key=lambda o: o["score_pre"], reverse=True), 1)}
V = views(OPPS)
post_rank = {o["id"]: i for i, o in enumerate(V["Best overall"], 1)}
for o in OPPS:
    o["rank_pre"], o["rank"] = pre_rank[o["id"]], post_rank[o["id"]]

BY_ID = {o["id"]: o for o in OPPS}
SHORTLIST = [m.oid for m in M]
FIN = {m.oid: (m, simulate(m), sensitivities(m)) for m in M}


def k(x):
    return f"{x / 1e3:,.0f}k" if x is not None else "n/a"


def m_(x):
    return f"{x / 1e6:,.1f}m"


# --- Excel ---------------------------------------------------------------------------------
wb = Workbook()
HDR = Font(bold=True, color="FFFFFF")
FILL = PatternFill("solid", fgColor="1F3A5F")


def sheet(title, header, rows, widths=None):
    ws = wb.create_sheet(title)
    ws.append(header)
    for c in ws[1]:
        c.font, c.fill = HDR, FILL
        c.alignment = Alignment(wrap_text=True, vertical="top")
    for r in rows:
        ws.append(r)
    ws.freeze_panes = "B2"
    for i, _ in enumerate(header, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(i, 18)
    return ws


wb.remove(wb.active)
readme = wb.create_sheet("README")
for line in [
    "Sweden Opportunity Intelligence — 52-opportunity database (reference date 2026-10-29)",
    "Scores 0-10 are analyst judgements anchored on cited evidence (workstream codes W01-W10 -> research/ folder). They are not measured data.",
    "Weighted score = SUM(score x weight) x 10, normalised to 0-100. 'Post' scores include adjustments from the adversarial review (W10).",
    "All market sizes and financial projections are MODELLED estimates; see Assumptions sheet and model/*.py for formulas.",
    f"FX (closing 2026-10-29): " + ", ".join(f"{a} {b}" for a, b in FX.items()) + " (source: poundsterlinglive.com history pages).",
    f"Swedish employer contributions {EMPLOYER_FEE:.2%} applied to salaries.",
]:
    readme.append([line])
readme.column_dimensions["A"].width = 160

crit_keys = [c[0] for c in CRITERIA]
header = (["Rank (post)", "Rank (pre)", "ID", "Opportunity", "Sector", "Target customer", "Problem", "Current alternatives",
           "Evidence (refs)", "Product/service concept", "Why now", "Revenue model", "Decision-maker", "Competitors",
           "Startup capital (SEK)", "Technical requirements", "Legal/regulatory dependencies", "Market size note",
           "Main uncertainty", "Fastest validation experiment", "Origin"]
          + [f"{c[1]} ({int(c[2] * 100)}%) pre" for c in CRITERIA]
          + [f"{c[0]} post" for c in CRITERIA]
          + ["Weighted score pre", "Weighted score post", "Evidence confidence", "# independent sources",
             "Largest unverified assumption", "Why ranking could be wrong", "Intl expansion"] + TAG_KEYS)
rows = []
for o in sorted(OPPS, key=lambda o: o["rank"]):
    rows.append([o["rank"], o["rank_pre"], o["id"], o["name"], o["sector"], o["customer"], o["problem"], o["alternatives"],
                 o["evidence"], o["concept"], o["why_now"], o["revenue"], o["decision_maker"], o["competitors"], o["capital"],
                 o["tech"], o["reg"], o["market"], o["uncertainty"], o["validation"], o["origin"]]
                + [o["scores"][c] for c in crit_keys] + [o["scores_post"][c] for c in crit_keys]
                + [o["score_pre"], o["score"], o["confidence"], o["n_sources"], o["assumption"], o["wrong"], o["intl"]]
                + ["x" if t in o["tags"] or (t.startswith("High international") and o["intl"]) else "" for t in TAG_KEYS])
ws = sheet("Opportunities", header, rows, {4: 48, 6: 36, 7: 60, 9: 60, 10: 50})
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")

with open(os.path.join(OUT, "opportunity_database.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)

# rankings
rr = []
for view, lst in V.items():
    for i, o in enumerate(lst[:10], 1):
        rr.append([view, i, o["id"], o["name"], o["score"], o["confidence"], o["capital"]])
sheet("Rankings", ["View", "Position", "ID", "Opportunity", "Weighted score (post)", "Confidence", "Startup capital SEK"], rr, {1: 44, 4: 70})

# adversarial changes
ar = []
for o in sorted(OPPS, key=lambda o: o["rank"]):
    if o["id"] in ADJ or o["rank_pre"] <= 10:
        ar.append([o["id"], o["name"], o["score_pre"], o["score"], o["rank_pre"], o["rank"],
                   ", ".join(f"{c}: {o['scores'][c]}->{v}" for c, v in ADJ.get(o["id"], {}).items()), RATIONALE.get(o["id"], "")])
sheet("Adversarial changes", ["ID", "Opportunity", "Score pre", "Score post", "Rank pre", "Rank post", "Criterion changes", "Rationale"], ar, {2: 60, 7: 50, 8: 90})

# sizing
sz = []
for oid in SHORTLIST:
    s = size(oid)
    sz.append([oid, BY_ID[oid]["name"], s["buyers"][0], s["buyers"][1], s["buyers"][2], s["buyer_basis"], s["spend"][0], s["spend"][1], s["spend"][2],
               s["spend_basis"], s["tam_low"], s["tam_base"], s["tam_high"], s["sam_share"], s["sam_basis"], s["sam_base"], s["som_customers"],
               s["som_arpa"], s["som"], round(100 * s["som_share_of_sam"], 1)])
sheet("Market sizing (modelled)", ["ID", "Opportunity", "Buyers low", "Buyers base", "Buyers high", "Buyer basis", "Spend/buyer low", "Spend/buyer base",
                                    "Spend/buyer high", "Spend basis", "TAM low SEK", "TAM base SEK", "TAM high SEK", "SAM share", "SAM basis",
                                    "SAM base SEK", "SOM customers (3-5y)", "SOM revenue/customer", "SOM SEK/yr", "SOM % of SAM"], sz, {2: 50, 6: 50, 10: 50, 15: 40})

# financials
fr, sr = [], []
for oid in SHORTLIST:
    m, r, sens = FIN[oid]
    fr.append([oid, m.label, m.arpa_month, m.setup_fee, m.gross_margin, m.cac, m.sales_cycle, str(m.ramp), m.churn_month,
               str(tuple(round(x) for x in m.fixed_month)), m.startup_cost, round(r["rev_y1"]), round(r["rev_y2"]), round(r["rev_y3"]),
               round(r["arr_m36"]), round(r["customers_m36"], 1), round(r["ebit_y3"]), r["breakeven_month"] or "not within 36m",
               round(r["working_capital_need"]), round(r["ltv"]) if m.churn_month else "n/a (project)",
               round(r["ltv_cac"], 1) if m.churn_month and m.cac else "n/a", round(r["payback_months"], 1) if r["payback_months"] else "n/a", m.basis])
    for case, rs in sens.items():
        sr.append([oid, m.label, case, round(rs["rev_y3"]), round(rs["ebit_y3"]), rs["breakeven_month"] or "not within 36m",
                   round(rs["working_capital_need"]), round(rs["cash_m36"])])
sheet("Financial models (modelled)", ["ID", "Model", "ARPA/month", "Setup fee", "Gross margin", "CAC", "Sales cycle (m)", "New customers/month Y1-3",
                                       "Monthly churn", "Fixed opex/month Y1-3", "Startup cost", "Revenue Y1", "Revenue Y2", "Revenue Y3", "ARR m36",
                                       "Customers m36", "EBIT Y3", "Break-even month", "Peak funding need", "LTV", "LTV/CAC", "CAC payback (m)",
                                       "Assumption basis"], fr, {2: 36, 23: 90})
sheet("Sensitivity (modelled)", ["ID", "Model", "Case", "Revenue Y3", "EBIT Y3", "Break-even month", "Peak funding need", "Cash m36"], sr, {2: 36, 3: 32})

# monthly detail for top 5
for oid in [o["id"] for o in V["Best overall"][:5] if o["id"] in FIN]:
    m, r, _ = FIN[oid]
    sheet(f"Monthly #{oid}", ["Month", "New customers", "Active customers", "Revenue", "Gross profit", "Contribution", "EBIT", "Cumulative cash"],
          [[x["month"], round(x["new"], 2), round(x["active"], 1), round(x["revenue"]), round(x["gross_profit"]), round(x["contribution"]),
            round(x["ebit"]), round(x["cash"])] for x in r["rows"]])

wb.save(os.path.join(OUT, "sweden_opportunity_database.xlsx"))

# --- markdown tables for the report --------------------------------------------------------
md = []
md.append("## Full ranking (post adversarial review)\n")
md.append("| Rank | Pre | ID | Opportunity | Sector | Score | Pre-score | Confidence | Sources | Capital (SEK) |")
md.append("|---|---|---|---|---|---|---|---|---|---|")
for o in V["Best overall"]:
    md.append(f"| {o['rank']} | {o['rank_pre']} | {o['id']} | {o['name']} | {o['sector']} | {o['score']} | {o['score_pre']} | {o['confidence']} | {o['n_sources']} | {o['capital']:,} |")
md.append("\n## Ranking views (top 10 each)\n")
for view, lst in V.items():
    md.append(f"### {view}\n")
    md.append("| # | ID | Opportunity | Score | Confidence |")
    md.append("|---|---|---|---|---|")
    for i, o in enumerate(lst[:10], 1):
        md.append(f"| {i} | {o['id']} | {o['name']} | {o['score']} | {o['confidence']} |")
    md.append("")
md.append("## Market sizing, top 20 (modelled, SEK per year)\n")
md.append("| ID | Opportunity | TAM low | TAM base | TAM high | SAM base | SOM (3-5 y) | SOM % SAM |")
md.append("|---|---|---|---|---|---|---|---|")
for oid in SHORTLIST:
    s = size(oid)
    md.append(f"| {oid} | {BY_ID[oid]['name']} | {m_(s['tam_low'])} | {m_(s['tam_base'])} | {m_(s['tam_high'])} | {m_(s['sam_base'])} | {m_(s['som'])} | {100 * s['som_share_of_sam']:.0f}% |")
md.append("\n## Financial models, top 20 (modelled, SEK)\n")
md.append("| ID | Model | Rev Y1 | Rev Y2 | Rev Y3 | EBIT Y3 | Break-even month | Peak funding need | LTV/CAC | Downside Y3 EBIT* |")
md.append("|---|---|---|---|---|---|---|---|---|---|")
for oid in SHORTLIST:
    m, r, sens = FIN[oid]
    ltv = f"{r['ltv_cac']:.1f}" if m.churn_month and m.cac else "n/a"
    md.append(f"| {oid} | {m.label} | {k(r['rev_y1'])} | {k(r['rev_y2'])} | {k(r['rev_y3'])} | {k(r['ebit_y3'])} | {r['breakeven_month'] or '>36'} | {k(r['working_capital_need'])} | {ltv} | {k(sens['Combined downside']['ebit_y3'])} |")
md.append("\n*Combined downside = CAC +50%, price -20%, sales cycle +50% with ramp /1.5.\n")
md.append("## Sensitivity detail, top 20\n")
md.append("| ID | Case | Rev Y3 | EBIT Y3 | Break-even | Peak funding |")
md.append("|---|---|---|---|---|---|")
for oid in SHORTLIST:
    for case, rs in FIN[oid][2].items():
        md.append(f"| {oid} | {case} | {k(rs['rev_y3'])} | {k(rs['ebit_y3'])} | {rs['breakeven_month'] or '>36'} | {k(rs['working_capital_need'])} |")
open(os.path.join(OUT, "tables.md"), "w").write("\n".join(md) + "\n")
print("built:", os.listdir(OUT))
for o in V["Best overall"][:12]:
    print(o["rank"], o["rank_pre"], o["id"], o["score_pre"], "->", o["score"], o["name"][:60])

# --- Deliverable 3 document (generated) ------------------------------------------------------
intro = f"""# Deliverable 3: 50-opportunity database

**Reference date:** 29 October 2026. This file is generated by `model/build.py`; do not edit it by hand.

**Exportable files:**
- [`output/sweden_opportunity_database.xlsx`](output/sweden_opportunity_database.xlsx), with these sheets:
  - Opportunities (all 52, with the 17 required fields, nine criterion scores before and after review, confidence, source counts, largest unverified assumption, why the ranking could be wrong, and tags)
  - Rankings
  - Adversarial changes
  - Market sizing
  - Financial models
  - Sensitivity
  - Monthly detail for the top 5
- [`output/opportunity_database.csv`](output/opportunity_database.csv): the same data as a flat file.
- [`output/source_index.csv`](output/source_index.csv): all 619 sources.

**How to read the scores:**
- Scores (0–10) are analyst judgements anchored on cited evidence. Workstream codes W01–W10 point to the files in [`research/`](research/).
- Weighted score = SUM(score x weight) x 10, normalised to 0–100. The weights are in [`model/opportunities.py`](model/opportunities.py).
- "Pre" is the score before the adversarial review (W10); the main score is after it.
- **Confidence is reported separately from the score and should be read with it.** A precise number does not mean a precise estimate.

**Totals:**
- {len(OPPS)} opportunities (at least 50 required).
- Origin: {sum(1 for o in OPPS if o['origin'].lower().startswith('original'))} original findings; {sum(1 for o in OPPS if 'foreign' in o['origin'].lower())} based on foreign models (labelled in the Origin column).

**Tags:** Bootstrappable, Capital intensive, Software, Physical operations, Hybrid, Marketplace, Regulated, Recurring revenue, Public-sector dependent, High international expansion potential. They are shown as columns in the spreadsheet.

## Per-opportunity summary

| ID | Opportunity | Target customer | Revenue model | Capital (SEK) | Main uncertainty | Fastest validation | Tags |
|---|---|---|---|---|---|---|---|
"""
lines = [intro]
for o in sorted(OPPS, key=lambda o: o["rank"]):
    tags = ", ".join(o["tags"] + (["Intl"] if o["intl"] else []))
    cell = lambda t: str(t).replace("|", "/")
    lines.append(f"| {o['id']} | {cell(o['name'])} | {cell(o['customer'])} | {cell(o['revenue'])} | {o['capital']:,} | {cell(o['uncertainty'])} | {cell(o['validation'])} | {tags} |")
lines.append("\n" + open(os.path.join(OUT, "tables.md")).read().split("## Market sizing")[0])
open(os.path.join(OUT, "..", "03_opportunity_database.md"), "w").write("\n".join(lines))
