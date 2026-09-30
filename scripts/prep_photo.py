"""Prep a photo for ASCII conversion.

1. Remove the background with rembg so only the subject remains.
2. Boost local contrast with OpenCV CLAHE so a flat face gets real highlights/shadows.
3. Composite onto pure white so the background maps to the blank end of the ramp.

Usage: python scripts/prep_photo.py source-photo.jpg [out.png]
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from rembg import remove

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: prep_photo.py <photo> [out.png]")
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "source-prepped.png"

    cutout = remove(Image.open(src).convert("RGB")).convert("RGBA")
    rgba = np.array(cutout)
    alpha = rgba[:, :, 3].astype(np.float32) / 255.0

    gray = cv2.cvtColor(rgba[:, :, :3], cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray).astype(np.float32)

    composited = gray * alpha + 255.0 * (1.0 - alpha)
    Image.fromarray(composited.clip(0, 255).astype(np.uint8), "L").save(out)
    print(f"wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")


if __name__ == "__main__":
    main()
