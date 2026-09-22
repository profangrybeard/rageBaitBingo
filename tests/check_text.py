"""House rules check for everything that ships.

Usage (from the repo root):
    python tests/check_text.py

Fails if any shipped file contains:
  - an em dash (house writing rule, no exceptions)
  - a specific instructor's name (materials must run for any teacher)
  - course-specific references that tie the game to one class
  - the old misspelling "Bate" (the 1.0 joke nobody got, retired)

Names, schools, and course codes that must never ship live in
tests/private_terms.txt, one regex per line. That file is gitignored so the
public repo never lists the very names it is protecting. The check runs
without it, but only the generic rules apply.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHIPPED = [ROOT / "index.html", *sorted((ROOT / "print").glob("*.html")), ROOT / "README.md"]
DOCS = sorted((ROOT / "docs").glob("*.md")) + [ROOT / "CLAUDE.md"]

PRIVATE = ROOT / "tests" / "private_terms.txt"

RULES = [
    (re.compile("—"), "em dash", SHIPPED + DOCS),
    (re.compile(r"\bProf\.", re.I), "instructor name", SHIPPED),
    (re.compile(r"Session \d", re.I), "course-specific reference", SHIPPED),
    (re.compile(r"\bBate\b"), "old misspelling", SHIPPED),
]
if PRIVATE.exists():
    terms = [t.strip() for t in PRIVATE.read_text(encoding="utf-8").splitlines()
             if t.strip() and not t.startswith("#")]
    if terms:
        RULES.append((re.compile("|".join(terms), re.I), "private term", SHIPPED))
else:
    print("note: tests/private_terms.txt not found, checking generic rules only")

bad = 0
for pattern, label, files in RULES:
    for f in files:
        if not f.exists():
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                bad += 1
                print(f"{f.relative_to(ROOT)}:{n}: {label}: {line.strip()[:100]}")

print("clean" if not bad else f"\n{bad} problem(s)")
sys.exit(1 if bad else 0)
