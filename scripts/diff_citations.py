#!/usr/bin/env python3
"""
Diff a fresh Google Scholar citation export against the last one that was
worked through, so only new or changed entries need a look before updating
research.qmd. Classifying an entry (Academic / Working Paper / Policy) and
writing its summary is still a manual step -- this only narrows down which
rows need that attention.

Usage:
    python scripts/diff_citations.py path/to/new_export.csv
    python scripts/diff_citations.py path/to/new_export.csv --update-baseline

The second form is for after research.qmd has been updated: it copies the
new export over scripts/citations-baseline.csv so next time's diff starts
from here. Without that flag, the baseline is left untouched.
"""
import csv
import shutil
import sys
from pathlib import Path

BASELINE = Path(__file__).parent / "citations-baseline.csv"
FIELDS = ["Authors", "Title", "Publication", "Volume", "Number", "Pages", "Year", "Publisher"]


def normalize_title(title):
    return " ".join(title.lower().split())


def load_csv(path):
    rows = {}
    if not path.exists():
        return rows
    with path.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            title = (row.get("Title") or "").strip()
            if title:
                rows[normalize_title(title)] = row
    return rows


def format_row(row):
    meta = " | ".join(f"{k}: {row[k]}" for k in ("Authors", "Publication", "Year") if row.get(k))
    return f"{row['Title']}\n  {meta}" if meta else row["Title"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python diff_citations.py <new_export.csv> [--update-baseline]")
        sys.exit(1)

    new_path = Path(sys.argv[1])
    update_baseline = "--update-baseline" in sys.argv

    old_rows = load_csv(BASELINE)
    new_rows = load_csv(new_path)

    new_titles = sorted(set(new_rows) - set(old_rows))
    removed_titles = sorted(set(old_rows) - set(new_rows))
    common_titles = set(new_rows) & set(old_rows)

    changed = []
    for key in common_titles:
        old, new = old_rows[key], new_rows[key]
        diffs = [
            (f, old.get(f, "").strip(), new.get(f, "").strip())
            for f in FIELDS
            if old.get(f, "").strip() != new.get(f, "").strip()
        ]
        if diffs:
            changed.append((new, diffs))

    if new_titles:
        print(f"=== NEW ({len(new_titles)}) ===\n")
        for key in new_titles:
            print(format_row(new_rows[key]))
            print()

    if changed:
        print(f"=== CHANGED ({len(changed)}) ===\n")
        for row, diffs in changed:
            print(row["Title"])
            for field, old_val, new_val in diffs:
                print(f"  {field}: {old_val!r} -> {new_val!r}")
            print()

    if removed_titles:
        print(f"=== IN BASELINE BUT NOT IN NEW EXPORT ({len(removed_titles)}) ===\n")
        for key in removed_titles:
            print(old_rows[key]["Title"])
        print()

    if not (new_titles or changed or removed_titles):
        print("No differences from the last processed export.")

    if update_baseline:
        shutil.copy(new_path, BASELINE)
        print(f"Baseline updated -> {BASELINE}")
    else:
        print("(Baseline not updated -- rerun with --update-baseline once these are incorporated into research.qmd.)")


if __name__ == "__main__":
    main()
