"""Hand-author a neofetch-style info card SVG that prints line by line.

Edit CARD below to change what the card says. STATIC=1 emits a frozen frame
(useful for local previews that don't run animations).

Usage: python scripts/make_info_card.py [out.svg]
"""
import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent

USER = "kevin"
HOST = "github"
CARD = [
    ("Name", "Kevin Nordkvist"),
    ("Role", "Full-stack developer"),
    ("Now", "Building for the web and beyond"),
    ("Web", "Terminal-style portfolio in Next.js + TS"),
    ("AI", "AI-powered apps with Python + Flask"),
    ("Plugins", "Minecraft plugins in Java"),
    ("Stack", "TypeScript, JavaScript, Python, Java, C++"),
    ("Frontend", "React, Next.js, Tailwind CSS, HTML5"),
    ("Backend", "Node.js, Flask, PostgreSQL"),
    ("Tools", "Git, Docker, Linux, Vercel, Figma, Postman"),
    ("Off-hours", "Gaming, self-improvement, tinkering with Linux"),
    ("Portfolio", "kevinnordkvist.dev"),
]

WIDTH = 490
PAD_X = 22
TITLE_H = 30
LINE_H = 22
FONT_SIZE = 13
KEY_COL = 96
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"
BG = "#0d1117"
BAR = "#161b22"
BORDER = "#30363d"
FG = "#c9d1d9"
MUTED = "#8b949e"
KEY_COLORS = ["#58a6ff", "#3fb950", "#d2a8ff", "#ffa657", "#79c0ff", "#ff7b72"]
BLOCKS = ["#161b22", "#ff7b72", "#3fb950", "#d29922", "#58a6ff", "#bc8cff", "#39c5cf", "#c9d1d9"]
STEP = 0.18  # seconds between lines
START = 0.3


def build_svg(static: bool) -> str:
    header = f"{USER}@{HOST}"
    body_top = TITLE_H + 26
    # header + rule + card rows + gap + color blocks
    height = body_top + (2 + len(CARD)) * LINE_H + 40 + 18

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" role="img" aria-label="{escape(header)} info card">',
    ]
    if not static:
        out.append(
            "<style>"
            ".ln{opacity:0;animation:in .45s ease-out forwards}"
            "@keyframes in{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:translateX(0)}}"
            "</style>"
        )
    out += [
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>',
        f'<path d="M0.5 {TITLE_H} V10.5 A10 10 0 0 1 10.5 0.5 H{WIDTH - 10.5} A10 10 0 0 1 {WIDTH - 0.5} 10.5 V{TITLE_H} Z" fill="{BAR}" stroke="{BORDER}"/>',
        '<circle cx="18" cy="15.5" r="5.5" fill="#ff5f57"/>',
        '<circle cx="36" cy="15.5" r="5.5" fill="#febc2e"/>',
        '<circle cx="54" cy="15.5" r="5.5" fill="#28c840"/>',
        f'<text x="{WIDTH / 2}" y="20" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{MUTED}">{escape(header)}: ~ / neofetch</text>',
        f'<g font-family="{FONT}" font-size="{FONT_SIZE}">',
    ]

    # Line wrappers use a nested <g> so the CSS transform on .ln doesn't fight
    # the positioning transform.
    def row(i: int, content: str) -> str:
        y = body_top + i * LINE_H
        if static:
            return f'<g transform="translate(0 {y})">{content}</g>'
        delay = START + i * STEP
        return (
            f'<g transform="translate(0 {y})"><g class="ln" style="animation-delay:{delay:.2f}s">'
            f"{content}</g></g>"
        )

    out.append(
        row(
            0,
            f'<text x="{PAD_X}" y="0"><tspan fill="#3fb950" font-weight="700">{USER}</tspan>'
            f'<tspan fill="{FG}">@</tspan><tspan fill="#58a6ff" font-weight="700">{HOST}</tspan></text>',
        )
    )
    out.append(row(1, f'<text x="{PAD_X}" y="0" fill="{MUTED}">{"-" * len(header)}</text>'))
    for n, (key, value) in enumerate(CARD):
        color = KEY_COLORS[n % len(KEY_COLORS)]
        out.append(
            row(
                n + 2,
                f'<text x="{PAD_X}" y="0" fill="{color}" font-weight="700">{escape(key)}</text>'
                f'<text x="{PAD_X + KEY_COL}" y="0" fill="{FG}">{escape(value)}</text>',
            )
        )
    blocks = "".join(
        f'<rect x="{PAD_X + i * 26}" y="-4" width="22" height="16" rx="3" fill="{c}"/>'
        for i, c in enumerate(BLOCKS)
    )
    out.append(row(len(CARD) + 3, blocks))
    out.append("</g></svg>")
    return "\n".join(out)


def main() -> None:
    dst = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "info-card.svg"
    dst.write_text(build_svg(static=os.environ.get("STATIC") == "1") + "\n")
    print(f"wrote {dst.name}")


if __name__ == "__main__":
    main()
