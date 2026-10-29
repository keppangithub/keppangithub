"""Simple 36-month unit-economics model (Phase 6). ALL OUTPUTS ARE MODELLED, NOT MEASURED.

Cost conventions (Sweden 2026):
  * Employer social contributions (arbetsgivaravgifter) 31.42% on gross salary.
  * Founder salary SEK 45,000/month gross -> ~SEK 59,000/month fully loaded.
  * Senior specialist/consultant SEK 60,000-65,000/month gross -> ~SEK 80-85k loaded.
Delivery labour for service-heavy models is captured in gross margin, not fixed cost.
"""
from dataclasses import dataclass, field, replace

EMPLOYER_FEE = 0.3142
LOADED = lambda gross: gross * (1 + EMPLOYER_FEE)


@dataclass
class Model:
    oid: int
    label: str
    arpa_month: float            # recurring revenue per active customer per month (SEK)
    setup_fee: float             # one-off revenue per new customer (SEK)
    gross_margin: float          # on all revenue
    cac: float                   # SEK per new customer (sales & marketing, incl. founder time valued at cost)
    sales_cycle: int             # months before first customers close
    ramp: tuple                  # new customers per month in year 1, 2, 3
    churn_month: float           # monthly logo churn
    fixed_month: tuple           # fixed opex per month in year 1, 2, 3 (SEK)
    startup_cost: float          # one-off before month 1 (SEK)
    basis: str = ""              # where the price/cost assumptions come from
    notes: list = field(default_factory=list)


def simulate(m: Model, months=36):
    active = 0.0
    cash = -m.startup_cost
    min_cash = cash
    rows = []
    be = None
    for t in range(1, months + 1):
        yr = (t - 1) // 12
        new = 0.0 if t <= m.sales_cycle else m.ramp[yr]
        active = active * (1 - m.churn_month) + new
        rev = active * m.arpa_month + new * m.setup_fee
        gp = rev * m.gross_margin
        contrib = gp - new * m.cac
        ebit = contrib - m.fixed_month[yr]
        cash += ebit
        min_cash = min(min_cash, cash)
        if be is None and ebit >= 0 and t > m.sales_cycle:
            be = t
        rows.append(dict(month=t, new=new, active=active, revenue=rev, gross_profit=gp, contribution=contrib, ebit=ebit, cash=cash))
    yr = lambda y: sum(r["revenue"] for r in rows[12 * (y - 1):12 * y])
    ltv = m.arpa_month * m.gross_margin / max(m.churn_month, 1e-6)
    return dict(
        rows=rows,
        rev_y1=yr(1), rev_y2=yr(2), rev_y3=yr(3),
        arr_m36=rows[-1]["active"] * m.arpa_month * 12,
        customers_m36=rows[-1]["active"],
        ebit_y3=sum(r["ebit"] for r in rows[24:36]),
        breakeven_month=be,
        working_capital_need=-min_cash,
        cash_m36=rows[-1]["cash"],
        ltv=ltv,
        ltv_cac=ltv / m.cac if m.cac else float("inf"),
        payback_months=m.cac / (m.arpa_month * m.gross_margin) if m.arpa_month else None,
    )


def sensitivities(m: Model):
    cases = {
        "Base": m,
        "CAC +50%": replace(m, cac=m.cac * 1.5),
        "Price -20%": replace(m, arpa_month=m.arpa_month * 0.8, setup_fee=m.setup_fee * 0.8),
        "Sales cycle +50% (slower ramp)": replace(m, sales_cycle=round(m.sales_cycle * 1.5 + 0.49),
                                                  ramp=tuple(r / 1.5 for r in m.ramp)),
        "Churn x2": replace(m, churn_month=m.churn_month * 2),
        "Combined downside": replace(m, cac=m.cac * 1.5, arpa_month=m.arpa_month * 0.8, setup_fee=m.setup_fee * 0.8,
                                     sales_cycle=round(m.sales_cycle * 1.5 + 0.49), ramp=tuple(r / 1.5 for r in m.ramp)),
    }
    return {k: simulate(v) for k, v in cases.items()}


F = LOADED(45_000)        # founder fully loaded
S = LOADED(62_000)        # specialist fully loaded
TOOLS = 15_000            # software, insurance, accounting, travel per month (assumption)
