"""Scrape the public contribution calendar (no token needed) into data/contributions.json.

GitHub serves the calendar as an HTML fragment at
https://github.com/users/<username>/contributions — the same one the profile page uses.

Usage: python scripts/fetch_contributions.py [username]
"""
import json
import os
import re
import sys
from collections import OrderedDict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "contributions.json"
USERNAME = "keppangithub"

COUNT_RE = re.compile(r"^\s*([\d,]+|No)\s+contributions?\b", re.I)
TOTAL_RE = re.compile(r"([\d,]+)\s+contributions?\s+in the last year", re.I)


def fetch_html(username: str) -> str:
    resp = requests.get(
        f"https://github.com/users/{username}/contributions",
        headers={"User-Agent": "profile-readme-heatmap", "Accept": "text/html"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.text


def parse(html: str) -> tuple[list[dict], int | None]:
    soup = BeautifulSoup(html, "html.parser")
    tooltips = {t.get("for"): t.get_text(" ", strip=True) for t in soup.find_all("tool-tip")}
    days = []
    for cell in soup.select("td.ContributionCalendar-day[data-date]"):
        level = int(cell.get("data-level", 0))
        tip = tooltips.get(cell.get("id"), "") or cell.get_text(" ", strip=True)
        m = COUNT_RE.match(tip)
        if m:
            count = 0 if m.group(1).lower() == "no" else int(m.group(1).replace(",", ""))
        else:
            count = int(cell.get("data-count", 0) or 0)
        days.append({"date": cell["data-date"], "count": count, "level": level})
    days.sort(key=lambda d: d["date"])

    total = None
    heading = soup.find(id="js-contribution-activity-description") or soup.find("h2")
    if heading:
        m = TOTAL_RE.search(heading.get_text(" ", strip=True))
        if m:
            total = int(m.group(1).replace(",", ""))
    return days, total


def streaks(days: list[dict], today: date) -> tuple[int, int]:
    longest = run = 0
    for d in days:
        run = run + 1 if d["count"] > 0 else 0
        longest = max(longest, run)
    # Current streak may end today or yesterday (today isn't over yet).
    past = [d for d in days if date.fromisoformat(d["date"]) <= today]
    if past and past[-1]["count"] == 0:
        past = past[:-1]
    current = 0
    for d in reversed(past):
        if d["count"] == 0:
            break
        current += 1
    return current, longest


def main() -> None:
    username = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GH_USERNAME", USERNAME)
    days, total = parse(fetch_html(username))
    if not days:
        sys.exit("no contribution cells found; GitHub's markup may have changed")

    today = datetime.now(timezone.utc).date()
    current, longest = streaks(days, today)
    best = max(days, key=lambda d: d["count"])
    monthly: OrderedDict[str, int] = OrderedDict()
    for d in days:
        monthly[d["date"][:7]] = monthly.get(d["date"][:7], 0) + d["count"]

    data = {
        "username": username,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total": total if total is not None else sum(d["count"] for d in days),
        "current_streak": current,
        "longest_streak": longest,
        "best_day": {"date": best["date"], "count": best["count"]},
        "monthly": monthly,
        "days": days,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1) + "\n")
    print(f"wrote data/{OUT.name}: {len(days)} days, {data['total']} contributions")


if __name__ == "__main__":
    main()
