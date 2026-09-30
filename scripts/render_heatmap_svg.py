"""Render data/contributions.json as an animated 53-week contribution heatmap SVG.

Boxes slide in diagonally (column + row stagger) once on load and freeze.

Usage: python scripts/render_heatmap_svg.py [data.json] [out.svg]
"""
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent

PALETTE = ["#161b22", "#0e4429", "#006d32",
           "#26a641", "#39d353", "#69f0a0"]
#          none -> brightest (level 5 is a neon top end)

WIDTH = 860
CELL = 12
GAP = 3
PAD = 20
LEFT = 34  # weekday labels
TOP = 46  # title + month labels
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"
BG = "#0d1117"
BORDER = "#30363d"
FG = "#c9d1d9"
MUTED = "#8b949e"
ACCENT = "#39d353"
DIAG_STEP = 0.022  # seconds per diagonal
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def levels(days: list[dict]) -> list[int]:
    """GitHub's 0-4 levels, with the busiest days promoted to a neon level 5."""
    nonzero = sorted(d["count"] for d in days if d["count"] > 0)
    top = nonzero[int(len(nonzero) * 0.95)] if len(nonzero) >= 20 else None
    out = []
    for d in days:
        lvl = d.get("level", 0)
        if top is not None and lvl >= 4 and d["count"] >= top:
            lvl = 5
        out.append(lvl)
    return out


def fmt_date(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{MONTHS[d.month - 1]} {d.day}, {d.year}"


def build_svg(data: dict, static: bool) -> str:
    days = data["days"]
    first = date.fromisoformat(days[0]["date"])
    start = first - timedelta(days=(first.weekday() + 1) % 7)  # back up to Sunday
    lvls = levels(days)

    cols = ((date.fromisoformat(days[-1]["date"]) - start).days // 7) + 1
    grid_w = cols * (CELL + GAP) - GAP
    grid_h = 7 * (CELL + GAP) - GAP
    x0 = LEFT + PAD + max(0, (WIDTH - 2 * PAD - LEFT - grid_w) // 2)
    y0 = TOP + PAD - 4
    height = y0 + grid_h + 64

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" role="img" '
        f'aria-label="{data["total"]:,} contributions in the last year">',
    ]
    if not static:
        out.append(
            "<style>"
            ".c{opacity:0;animation:drop .5s cubic-bezier(.2,.8,.3,1) forwards}"
            "@keyframes drop{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:translateY(0)}}"
            ".f{opacity:0;animation:fade .6s ease-out forwards}"
            "@keyframes fade{to{opacity:1}}"
            "</style>"
        )
    out += [
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>',
        f'<g font-family="{FONT}" font-size="11" fill="{MUTED}">',
        f'<text x="{PAD}" y="{PAD + 8}" font-size="13" fill="{FG}">'
        f'<tspan fill="{ACCENT}">$</tspan> contributions --user {escape(data["username"])} --last 365d</text>',
    ]

    # Month labels at the first column containing the 1st..7th of a month.
    last_month = None
    for c in range(cols):
        d = start + timedelta(days=7 * c)
        if d.month != last_month and d.day <= 7:
            if c < cols - 2:
                out.append(f'<text x="{x0 + c * (CELL + GAP)}" y="{y0 - 7}">{MONTHS[d.month - 1]}</text>')
            last_month = d.month
    for r, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        out.append(f'<text x="{x0 - 30}" y="{y0 + r * (CELL + GAP) + CELL - 2}">{label}</text>')
    out.append("</g>")

    out.append("<g>")
    for d, lvl in zip(days, lvls):
        dt = date.fromisoformat(d["date"])
        offset = (dt - start).days
        c, r = offset // 7, offset % 7
        x, y = x0 + c * (CELL + GAP), y0 + r * (CELL + GAP)
        count = d["count"]
        title = f'{count or "No"} contribution{"" if count == 1 else "s"} on {fmt_date(d["date"])}'
        anim = "" if static else f' class="c" style="animation-delay:{(c + r) * DIAG_STEP:.3f}s"'
        out.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" '
            f'fill="{PALETTE[lvl]}"{anim}><title>{title}</title></rect>'
        )
    out.append("</g>")

    reveal = (cols + 7) * DIAG_STEP
    footer_y = y0 + grid_h + 30
    fclass = "" if static else f' class="f" style="animation-delay:{reveal:.2f}s"'
    best = data["best_day"]
    stats = (
        f'<tspan fill="{FG}" font-weight="700">{data["total"]:,}</tspan> contributions in the last year'
        f'  <tspan fill="{BORDER}">|</tspan>  streak <tspan fill="{ACCENT}">{data["current_streak"]}d</tspan>'
        f'  <tspan fill="{BORDER}">|</tspan>  longest <tspan fill="{ACCENT}">{data["longest_streak"]}d</tspan>'
    )
    if best["count"]:
        stats += (
            f'  <tspan fill="{BORDER}">|</tspan>  best day <tspan fill="{ACCENT}">{best["count"]}</tspan>'
            f' ({fmt_date(best["date"])})'
        )
    label_w = 30  # "Less" / "More" at 11px monospace, plus a gap
    legend_x = WIDTH - PAD - 2 * label_w - len(PALETTE) * (CELL + 3)
    legend = "".join(
        f'<rect x="{legend_x + label_w + i * (CELL + 3)}" y="{footer_y - 10}" width="{CELL}" height="{CELL}" rx="2.5" fill="{c}"/>'
        for i, c in enumerate(PALETTE)
    )
    out.append(
        f'<g font-family="{FONT}" font-size="11" fill="{MUTED}"{fclass}>'
        f'<text x="{x0 - 30}" y="{footer_y}">{stats}</text>'
        f'<text x="{legend_x}" y="{footer_y}">Less</text>{legend}'
        f'<text x="{legend_x + label_w + 2 + len(PALETTE) * (CELL + 3)}" y="{footer_y}">More</text>'
        f"</g>"
    )
    out.append("</svg>")
    return "\n".join(out)


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "contributions.json"
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "contrib-heatmap.svg"
    data = json.loads(src.read_text())
    dst.write_text(build_svg(data, static=os.environ.get("STATIC") == "1") + "\n")
    print(f"wrote {dst.name}")


if __name__ == "__main__":
    main()
