"""Convert source-prepped.png into a self-typing monochrome ASCII portrait SVG.

Each row is revealed by a left-to-right clip wipe with a block cursor riding the
edge, staggered top to bottom. It prints once and freezes (SMIL, fill="freeze").

Usage: python scripts/make_ascii_svg.py [prepped.png] [out.svg]
"""
import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent

RAMP = " .`:-=+*cs#%@"  # sparse -> dense
#       ^ leading space clears the background to nothing
# Glyphs are drawn light-on-dark, so bright skin/highlights get the dense end of
# the ramp and the white (removed) background maps to spaces.

COLS = 100
GAMMA = 1.25  # >1 deepens shadows so features stand out
FONT_SIZE = 11
CHAR_W = FONT_SIZE * 0.6  # monospace advance
LINE_H = 12
PAD = 18
NBSP = "\u00a0"  # renderers collapse plain leading spaces
FG = "#c9d1d9"
BG = "#0d1117"
BORDER = "#30363d"
ROW_DURATION = 0.35  # seconds for one row to wipe across
ROW_STAGGER = 0.06  # seconds between row starts
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"


def to_rows(img: Image.Image) -> list[str]:
    arr = np.array(img.convert("L"))
    # Crop to the subject (anything noticeably darker than white).
    ys, xs = np.where(arr < 245)
    if len(xs):
        arr = arr[ys.min() : ys.max() + 1, xs.min() : xs.max() + 1]
    h, w = arr.shape
    rows = max(1, round(h / w * COLS * CHAR_W / LINE_H))
    small = np.array(Image.fromarray(arr).resize((COLS, rows), Image.LANCZOS), dtype=np.float32)
    subject = small < 225
    # Erode the mask by one cell: the cutout's soft edge is light gray and would
    # otherwise draw a dense outline around the silhouette.
    padded = np.pad(subject, 1, constant_values=False)
    subject &= padded[:-2, 1:-1] & padded[2:, 1:-1] & padded[1:-1, :-2] & padded[1:-1, 2:]
    lo, hi = np.percentile(small[subject], [2, 98]) if subject.any() else (0.0, 255.0)
    norm = ((small - lo) / max(hi - lo, 1.0)).clip(0.0, 1.0) ** GAMMA
    idx = (1 + norm * (len(RAMP) - 2)).round().astype(int)
    idx[~subject] = 0
    lines = ["".join(RAMP[i] for i in row).rstrip() for row in idx]
    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.pop(0)
    return lines


def build_svg(lines: list[str], static: bool) -> str:
    width = round(COLS * CHAR_W + PAD * 2)
    height = round(len(lines) * LINE_H + PAD * 2)
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="ASCII portrait">',
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" '
        f'fill="{BG}" stroke="{BORDER}"/>',
    ]
    if not static:
        out.append("<defs>")
        for i, line in enumerate(lines):
            y = PAD + i * LINE_H
            begin = i * ROW_STAGGER
            row_w = len(line) * CHAR_W
            out.append(
                f'<clipPath id="r{i}"><rect x="{PAD}" y="{y}" width="0" height="{LINE_H}">'
                f'<animate attributeName="width" from="0" to="{row_w:.1f}" begin="{begin:.2f}s" '
                f'dur="{ROW_DURATION}s" fill="freeze"/></rect></clipPath>'
            )
        out.append("</defs>")
    out.append(
        f'<g font-family="{FONT}" font-size="{FONT_SIZE}" fill="{FG}">'
    )
    for i, line in enumerate(lines):
        if not line:
            continue
        y = PAD + i * LINE_H
        text_len = len(line) * CHAR_W
        clip = "" if static else f' clip-path="url(#r{i})"'
        out.append(
            f'<text x="{PAD}" y="{y + LINE_H - 3}" textLength="{text_len:.1f}" '
            f'lengthAdjust="spacing"{clip}>{escape(line).replace(" ", NBSP)}</text>'
        )
        if not static:
            begin = i * ROW_STAGGER
            out.append(
                f'<rect x="{PAD}" y="{y + 1}" width="{CHAR_W:.1f}" height="{LINE_H - 2}" '
                f'fill="{FG}" opacity="0">'
                f'<set attributeName="opacity" to="0.85" begin="{begin:.2f}s"/>'
                f'<animate attributeName="x" from="{PAD}" to="{PAD + text_len:.1f}" '
                f'begin="{begin:.2f}s" dur="{ROW_DURATION}s" fill="freeze"/>'
                f'<set attributeName="opacity" to="0" begin="{begin + ROW_DURATION:.2f}s"/>'
                f"</rect>"
            )
    out.append("</g></svg>")
    return "\n".join(out)


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "source-prepped.png"
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "ascii-portrait.svg"
    lines = to_rows(Image.open(src))
    dst.write_text(build_svg(lines, static=os.environ.get("STATIC") == "1") + "\n")
    print(f"wrote {dst.name} ({len(lines)} rows x {COLS} cols)")


if __name__ == "__main__":
    main()
