#!/usr/bin/env python3
"""Update homepage news from scholarly metadata sources.

The script keeps manually pinned items in _data/news.yml and appends recent
publication updates discovered from OpenAlex. It uses only the Python standard
library so it can run on GitHub Actions without extra dependencies.
"""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NEWS_FILE = ROOT / "_data" / "news.yml"
AUTHOR_NAME = "Longbo Han"
SEARCH_TERMS = [
    "Longbo Han generative AI security",
    "Longbo Han privacy protection",
    "Longbo Han lattice cryptography",
    "Longbo Han zero knowledge proofs",
]
MAX_AUTO_ITEMS = 8


def yml_escape(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def strip_tags(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value)


def read_existing_items() -> list[dict[str, str | bool]]:
    if not NEWS_FILE.exists():
        return []

    items: list[dict[str, str | bool]] = []
    current: dict[str, str | bool] | None = None
    for raw_line in NEWS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("- "):
            if current:
                items.append(current)
            current = {}
            line = line[2:]
        elif current is None:
            continue
        else:
            line = line.strip()

        if ":" not in line or current is None:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.lower() in {"true", "false"}:
            current[key] = value.lower() == "true"
        else:
            current[key] = value.strip('"')

    if current:
        items.append(current)
    return items


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "LoongDoctor-homepage-news-updater/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.loads(response.read().decode("utf-8"))


def openalex_items() -> list[dict[str, str | bool]]:
    found: dict[str, dict[str, str | bool]] = {}
    for term in SEARCH_TERMS:
        query = urllib.parse.urlencode(
            {
                "search": term,
                "filter": "from_publication_date:2020-01-01",
                "per-page": "10",
                "sort": "publication_date:desc",
            }
        )
        payload = fetch_json(f"https://api.openalex.org/works?{query}")
        for work in payload.get("results", []):
            authors = [
                author.get("author", {}).get("display_name", "")
                for author in work.get("authorships", [])
            ]
            if AUTHOR_NAME not in authors:
                continue

            title = work.get("title") or "Untitled work"
            title_key = re.sub(r"\W+", "", title).lower()
            if title_key in found:
                continue

            date = work.get("publication_date") or str(work.get("publication_year", ""))
            year_month = date[:7].replace("-", ".") if len(date) >= 7 else str(work.get("publication_year", ""))
            venue = (
                work.get("primary_location", {})
                .get("source", {})
                .get("display_name")
                or work.get("host_venue", {})
                .get("display_name")
                or "a scholarly venue"
            )
            url = work.get("doi") or work.get("id") or ""

            safe_title = html.escape(title)
            safe_venue = html.escape(venue)
            text = f"<strong>{safe_title}</strong> published in <em>{safe_venue}</em>."
            if url:
                text = f'<a href="{html.escape(url)}">{text}</a>'

            found[title_key] = {
                "date": year_month,
                "text": text,
                "source": "auto",
                "pinned": False,
            }
    return sorted(found.values(), key=lambda item: str(item["date"]), reverse=True)


def write_items(items: list[dict[str, str | bool]]) -> None:
    lines: list[str] = []
    for item in items:
        lines.append(f"- date: {yml_escape(str(item['date']))}")
        lines.append(f"  text: {yml_escape(str(item['text']))}")
        lines.append(f"  source: {yml_escape(str(item.get('source', 'auto')))}")
        lines.append(f"  pinned: {str(bool(item.get('pinned', False))).lower()}")
        lines.append("")
    NEWS_FILE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    existing = read_existing_items()
    manual_items = [item for item in existing if item.get("source") != "auto"]
    existing_titles = {strip_tags(str(item.get("text", ""))).lower() for item in manual_items}

    auto_items = []
    for item in openalex_items():
        title = strip_tags(str(item["text"])).lower()
        if title in existing_titles:
            continue
        auto_items.append(item)

    combined = sorted(manual_items, key=lambda item: str(item["date"]), reverse=True)
    combined.extend(auto_items[:MAX_AUTO_ITEMS])
    write_items(combined)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"news update failed: {exc}", file=sys.stderr)
        raise
