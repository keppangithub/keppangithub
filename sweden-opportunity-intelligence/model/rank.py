"""Weighted scoring and the seven ranking views (Phase 7)."""
from opportunities import CRITERIA, OPPS

WEIGHTS = {k: w for k, _, w in CRITERIA}
assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9


def weighted(o, scores=None):
    s = scores or o["scores"]
    # sum(score x weight) is on a 0-10 scale; x10 normalises to 0-100
    return round(10 * sum(s[k] * w for k, w in WEIGHTS.items()), 1)


def is_software_only(o):
    return "Software" in o["tags"] and "Hybrid" not in o["tags"] and "Physical operations" not in o["tags"]


def views(opps, key="score"):
    by = lambda f, sk=lambda o: o[key]: sorted([o for o in opps if f(o)], key=sk, reverse=True)
    return {
        "Best overall": by(lambda o: True),
        "Best bootstrap businesses (<= SEK 1m capital)": by(lambda o: o["capital"] <= 1_000_000 and "Capital intensive" not in o["tags"]),
        "Fastest path to first revenue": by(lambda o: True, lambda o: (o["scores"]["speed"], o[key])),
        "Best technical-founder opportunities": by(lambda o: "Software" in o["tags"] or "Hybrid" in o["tags"],
                                                   lambda o: o[key] + 2 * (o["scores"]["scale"] - 5) * ("Software" in o["tags"])),
        "Highest defensibility": by(lambda o: True, lambda o: (o["scores"]["scale"] + o["scores"]["gap"], o[key])),
        "Best international scaling potential": by(lambda o: o["intl"]),
        "Best non-software opportunities": by(lambda o: not is_software_only(o) and ("Physical operations" in o["tags"] or "Hybrid" in o["tags"] or "Marketplace" in o["tags"])),
    }


for o in OPPS:
    o["score"] = weighted(o)
