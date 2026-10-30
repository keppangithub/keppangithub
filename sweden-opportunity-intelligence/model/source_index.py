"""Extracts every URL cited in the research workstreams into output/source_index.csv (Deliverable 9)."""
import csv, glob, os, re

ROOT = os.path.join(os.path.dirname(__file__), "..")
URL = re.compile(r"https?://[^\s|)\]>\"']+")
rows, seen = [], set()
for path in sorted(glob.glob(os.path.join(ROOT, "research", "*.md"))):
    ws = "W" + os.path.basename(path)[:2]
    for line in open(path, encoding="utf-8"):
        for url in URL.findall(line):
            url = url.rstrip(".,;")
            if (ws, url) in seen:
                continue
            seen.add((ws, url))
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rel = next((c for c in reversed(cells) if c in ("H", "M", "L") or c.split(" ")[0] in ("High", "Medium", "Low", "H", "M", "L")), "")
            context = re.sub(r"\s+", " ", line.strip())[:400]
            rows.append([ws, url.split("/")[2] if "//" in url else "", url, rel, context])
with open(os.path.join(ROOT, "output", "source_index.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Workstream", "Domain", "URL", "Reliability (as tagged in ledger)", "Ledger row / context (publisher, title, dates, finding)"])
    w.writerows(rows)
print(len(rows), "source rows;", len({r[2] for r in rows}), "unique URLs")
