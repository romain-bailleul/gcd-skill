#!/usr/bin/env python3
"""Write the daily release note: what changed in the scraped docs since the previous run.

The scheduled job merges each scrape without a person reading it, so this note is the
record of what changed, one file per day under docs-changes/. For each region it compares
the previous copy of the scraped directory with the new one, through each side's
_manifest.json:

- pages added and removed;
- pages whose text changed, with line counts and the sections the changes fall under;
- pages only re-dated: the "Last updated:" header line moved but the text did not;
- SecNumCloud 3.2 qualification moves, when the region has _secnumcloud_status.json.

Everything taken from a scraped page (titles, headings, paths, service names, statuses) is
rendered inside a code span, with invisible format characters removed, so the note and the
pull request body that quotes it cannot mention people, link issues or carry markup.

Usage:
    python3 scripts/docs-release-note.py --date 2026-11-12 \\
        --region S3NS PREVIOUS/docs-raw-s3ns docs-raw-s3ns \\
        --region Berlin PREVIOUS/docs-raw docs-raw \\
        [--failed Berlin] [--notes-dir docs-changes] [--pr-body BODY.md]

It prints ``note=<path>`` for the file it wrote, for $GITHUB_OUTPUT.
"""

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

MANIFEST = "_manifest.json"
SECNUMCLOUD = "_secnumcloud_status.json"
NOTES_DIRNAME = "docs-changes"
MAX_TEXT = 120          # characters kept from one scraped title, heading or name
MAX_SECTIONS = 5        # sections named per changed page
HEADER_LINES = 4        # "# title", blank, "Source:", "Last updated:" (scrape-gcd-docs.py)
PR_BODY_LIMIT = 60000   # GitHub caps a pull request body at 65536 characters

DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
LABEL_RE = re.compile(r"[A-Za-z0-9 ._-]{1,40}\Z")
FILENAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\.md\Z")
SAFE_URL_RE = re.compile(r"https://[A-Za-z0-9.-]+/[A-Za-z0-9/._~%-]*\Z")
HEADING_RE = re.compile(r"#{2,6}\s+(.+?)\s*#*\s*\Z")
LAST_UPDATED_HEADER = "Last updated:"


class NoteError(ValueError):
    """A scraped directory cannot be compared: its manifest or status file is malformed."""


@dataclass
class Page:
    path: str
    title: str
    url: str
    added: int = 0
    removed: int = 0
    sections: list = field(default_factory=list)


@dataclass
class RegionChanges:
    added: list = field(default_factory=list)
    removed: list = field(default_factory=list)
    changed: list = field(default_factory=list)
    redated: int = 0
    qualification: list = field(default_factory=list)

    @property
    def has_content_changes(self) -> bool:
        return bool(self.added or self.removed or self.changed or self.qualification)


def inert(text) -> str:
    """Render scraped text as one capped code span, without invisible characters."""
    text = "".join(c for c in str(text or "") if unicodedata.category(c) != "Cf")
    text = " ".join(text.replace("`", "").split())
    if len(text) > MAX_TEXT:
        text = text[:MAX_TEXT - 1] + "…"
    return f"`{text or '(untitled)'}`"


def read_json(path: Path, expected: type):
    """Returns the parsed file, None when it does not exist. Raises NoteError."""
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise NoteError(f"{path}: {e}") from e
    if not isinstance(data, expected):
        raise NoteError(f"{path}: expected a JSON {expected.__name__}")
    return data


def read_manifest(directory: Path) -> dict:
    """Returns {path: entry} with a validated plain filename per entry. Raises NoteError."""
    manifest = read_json(directory / MANIFEST, dict) or {}
    for path, entry in manifest.items():
        name = entry.get("filename") if isinstance(entry, dict) else None
        if not isinstance(name, str) or not FILENAME_RE.match(name):
            raise NoteError(f"{directory / MANIFEST}: {path!r} has no plain .md filename")
    return manifest


def read_qualification(directory: Path) -> dict:
    """Returns {service name: status} from the SecNumCloud file, {} without one."""
    data = read_json(directory / SECNUMCLOUD, dict)
    if data is None:
        return {}
    services = data.get("services")
    if not isinstance(services, list) or not all(isinstance(s, dict) for s in services):
        raise NoteError(f"{directory / SECNUMCLOUD}: expected a 'services' list of objects")
    return {str(s.get("name")): str(s.get("status")) for s in services}


def read_page(directory: Path, entry: dict) -> list:
    path = directory / entry["filename"]
    return path.read_text(encoding="utf-8").splitlines() if path.is_file() else []


def without_date_header(lines: list) -> list:
    """Drops the scraper's own "Last updated:" header line, never a body line."""
    return [line for i, line in enumerate(lines)
            if not (i < HEADER_LINES and line.startswith(LAST_UPDATED_HEADER))]


def unmatched(lines: list, other: list) -> list:
    """Indexes of the lines with no counterpart in other, counting duplicates."""
    spare = Counter(other)
    indexes = []
    for index, line in enumerate(lines):
        if spare[line]:
            spare[line] -= 1
        else:
            indexes.append(index)
    return indexes


def sections_of(lines: list, indexes: list) -> list:
    """The heading each indexed line falls under, in page order, without repeats."""
    wanted, sections, current = set(indexes), [], None
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            current = match.group(1)
        if index in wanted and current and current not in sections:
            sections.append(current)
    return sections


def changed_page(page: Page, old: list, new: list) -> Page:
    """Fills the line counts and the sections the changes fall under.

    Lines are matched as multisets, not aligned: a release note needs how much changed
    and where, and an alignment (difflib) takes minutes on the largest scraped pages.
    A moved line therefore counts as unchanged.
    """
    added, removed = unmatched(new, old), unmatched(old, new)
    page.added, page.removed = len(added), len(removed)
    sections = sections_of(new, added)
    sections += [s for s in sections_of(old, removed) if s not in sections]
    page.sections = sections[:MAX_SECTIONS]
    return page


def make_page(path: str, entry: dict) -> Page:
    return Page(path=path, title=str(entry.get("title") or ""), url=str(entry.get("url") or ""))


def compare_pages(old_dir: Path, new_dir: Path, changes: RegionChanges) -> None:
    old_manifest, new_manifest = read_manifest(old_dir), read_manifest(new_dir)
    for path in sorted(new_manifest.keys() - old_manifest.keys()):
        changes.added.append(make_page(path, new_manifest[path]))
    for path in sorted(old_manifest.keys() - new_manifest.keys()):
        changes.removed.append(make_page(path, old_manifest[path]))
    for path in sorted(old_manifest.keys() & new_manifest.keys()):
        old_lines = read_page(old_dir, old_manifest[path])
        new_lines = read_page(new_dir, new_manifest[path])
        if old_lines == new_lines:
            continue
        old_text, new_text = without_date_header(old_lines), without_date_header(new_lines)
        if old_text == new_text:
            changes.redated += 1
        else:
            changes.changed.append(changed_page(make_page(path, new_manifest[path]), old_text, new_text))


def compare_region(old_dir: Path, new_dir: Path) -> RegionChanges:
    """Compares two scraped copies of one region. Raises NoteError."""
    changes = RegionChanges()
    compare_pages(Path(old_dir), Path(new_dir), changes)
    old_status, new_status = read_qualification(Path(old_dir)), read_qualification(Path(new_dir))
    for name in sorted(old_status.keys() | new_status.keys()):
        before, after = old_status.get(name), new_status.get(name)
        if before != after:
            changes.qualification.append((name, before, after))
    return changes


def plural(count: int, word: str) -> str:
    return f"{count} {word}{'' if count == 1 else 's'}"


def page_link(page: Page) -> str:
    title = inert(page.title or page.path)
    return f"[{title}]({page.url})" if SAFE_URL_RE.match(page.url) else title


def render_pages(heading: str, pages: list, detail) -> list:
    if not pages:
        return []
    return [f"### {heading}", "", *(f"- {page_link(p)} {detail(p)}".rstrip() for p in pages), ""]


def changed_detail(page: Page) -> str:
    sections = ", ".join(inert(s) for s in page.sections)
    return f"+{page.added} −{page.removed}" + (f", in {sections}" if sections else "")


def qualification_line(name: str, before, after) -> str:
    if before is None:
        return f"- {inert(name)}: added as {inert(after)}"
    if after is None:
        return f"- {inert(name)}: removed (was {inert(before)})"
    return f"- {inert(name)}: {inert(before)} → {inert(after)}"


def render_region(label: str, changes: RegionChanges) -> list:
    lines = [f"## {label}", ""]
    counts = [plural(len(changes.added), "page") + " added", f"{len(changes.removed)} removed",
              f"{len(changes.changed)} changed"]
    lines.append(", ".join(counts) + ".")
    if changes.redated:
        lines.append(plural(changes.redated, "page") + " re-dated with no content change.")
    lines.append("")
    lines += render_pages("Added", changes.added, lambda p: f"({inert(p.path)})")
    lines += render_pages("Removed", changes.removed, lambda p: f"({inert(p.path)})")
    lines += render_pages("Changed", changes.changed, changed_detail)
    if changes.qualification:
        lines += ["### SecNumCloud 3.2 qualification", "",
                  *(qualification_line(*move) for move in changes.qualification), ""]
    return lines


def render(date: str, regions: list, failed: list) -> str:
    """Returns the note for [(label, RegionChanges)] and the labels whose scrape failed."""
    lines = [f"# Documentation changes, {date}", ""]
    if failed:
        names = ", ".join(failed)
        lines += [f"> **Warning:** the {names} scrape failed. Its pages are the previous copy, "
                  "so this note cannot show what changed there.", ""]
    for label, changes in regions:
        lines += render_region(label, changes)
    return "\n".join(lines).rstrip() + "\n"


def truncate_on_lines(text: str, limit: int, pointer: str) -> str:
    """Cuts text to whole lines within limit, so no code span is split, then adds pointer."""
    if len(text) <= limit:
        return text
    kept, size = [], 0
    for line in text.splitlines(keepends=True):
        if size + len(line) > limit:
            break
        kept.append(line)
        size += len(line)
    return "".join(kept) + f"\n{pointer}\n"


def note_path(notes_dir: Path, date: str) -> Path:
    """docs-changes/DATE.md, or DATE-2.md and up when a run already wrote one that day."""
    path, number = notes_dir / f"{date}.md", 2
    while path.exists():
        path, number = notes_dir / f"{date}-{number}.md", number + 1
    return path


def iso_date(value: str) -> str:
    if not DATE_RE.match(value):
        raise argparse.ArgumentTypeError(f"{value!r} is not YYYY-MM-DD")
    return value


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Write the daily docs release note.")
    parser.add_argument("--date", required=True, type=iso_date)
    parser.add_argument("--region", required=True, nargs=3, action="append",
                        metavar=("LABEL", "PREVIOUS_DIR", "NEW_DIR"))
    parser.add_argument("--failed", action="append", default=[], metavar="LABEL",
                        help="a region whose scrape failed")
    parser.add_argument("--notes-dir", type=Path, default=Path(NOTES_DIRNAME))
    parser.add_argument("--pr-body", type=Path, help="also write a pull request body here")
    parser.add_argument("--pr-body-limit", type=int, default=PR_BODY_LIMIT)
    args = parser.parse_args(argv)
    for label in [r[0] for r in args.region] + args.failed:
        if not LABEL_RE.match(label):
            parser.error(f"invalid region label {label!r}")
    return args


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        regions = [(label, compare_region(Path(old), Path(new))) for label, old, new in args.region]
    except NoteError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    text = render(args.date, regions, args.failed)
    path = note_path(args.notes_dir, args.date)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if args.pr_body:
        pointer = f"The full note is `{NOTES_DIRNAME}/{path.name}`."
        body = truncate_on_lines(text, args.pr_body_limit, f"(Truncated.) {pointer}")
        args.pr_body.write_text(f"{pointer}\n\n{body}", encoding="utf-8")
    print(f"note={NOTES_DIRNAME}/{path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
