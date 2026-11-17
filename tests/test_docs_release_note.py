import json
import tempfile
import unittest
from pathlib import Path

from tests.helpers import load_script

note = load_script("docs-release-note")

BASE = "https://documentation.s3ns.fr"


def write_region(root: Path, pages: dict, secnumcloud: list | None = None) -> Path:
    """Write a scraped region: {path: (title, body, last_updated)} plus its manifest."""
    root.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for path, (title, body, last_updated) in pages.items():
        filename = path.strip("/").replace("/", "_") + ".md"
        header = f"# {title}\n\nSource: {BASE}{path}\n"
        if last_updated:
            header += f"Last updated: {last_updated}\n"
        (root / filename).write_text(header + "\n" + body, encoding="utf-8")
        manifest[path] = {"title": title, "filename": filename, "url": f"{BASE}{path}",
                          "last_updated": last_updated}
    (root / "_manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    if secnumcloud is not None:
        services = [{"name": n, "status": s} for n, s in secnumcloud]
        (root / "_secnumcloud_status.json").write_text(json.dumps({"services": services}), encoding="utf-8")
    return root


class CompareRegionTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def compare(self, old_pages, new_pages, old_snc=None, new_snc=None):
        old = write_region(self.tmp / "old", old_pages, old_snc)
        new = write_region(self.tmp / "new", new_pages, new_snc)
        return note.compare_region(old, new)

    def test_compareRegion_dateOnlyChange_countsAsRedated(self):
        changes = self.compare({"/run/docs": ("Cloud Run", "Same text.\n", "2026-11-01")},
                               {"/run/docs": ("Cloud Run", "Same text.\n", "2026-11-10")})
        self.assertEqual(changes.redated, 1)
        self.assertEqual(changes.changed, [])
        self.assertTrue(changes.has_content_changes is False)

    def test_compareRegion_bodyChange_listsPageWithLineCountsAndSections(self):
        old_body = "## Limits\n\nA.\n\n## Regions\n\nB.\n"
        new_body = "## Limits\n\nA.\n\n## Regions\n\nB.\nC.\n"
        changes = self.compare({"/run/docs": ("Cloud Run", old_body, "2026-11-01")},
                               {"/run/docs": ("Cloud Run", new_body, "2026-11-10")})
        self.assertEqual(changes.redated, 0)
        [page] = changes.changed
        self.assertEqual((page.path, page.added, page.removed), ("/run/docs", 1, 0))
        self.assertEqual(page.sections, ["Regions"])

    def test_compareRegion_newAndGonePages_areListed(self):
        changes = self.compare({"/old/docs": ("Old", "x\n", "2026-11-01")},
                               {"/new/docs": ("New", "y\n", "2026-11-10")})
        self.assertEqual([p.path for p in changes.added], ["/new/docs"])
        self.assertEqual([p.path for p in changes.removed], ["/old/docs"])

    def test_compareRegion_unchangedPage_reportsNothing(self):
        pages = {"/run/docs": ("Cloud Run", "Same.\n", "2026-11-01")}
        changes = self.compare(pages, pages)
        self.assertFalse(changes.has_content_changes)
        self.assertEqual(changes.redated, 0)

    def test_compareRegion_missingPreviousDir_treatsEveryPageAsAdded(self):
        new = write_region(self.tmp / "new", {"/run/docs": ("Cloud Run", "x\n", "")})
        changes = note.compare_region(self.tmp / "absent", new)
        self.assertEqual([p.path for p in changes.added], ["/run/docs"])

    def test_compareRegion_secnumcloudMoves_areReported(self):
        changes = self.compare({}, {},
                               old_snc=[("Cloud Run", "in_progress"), ("Gone", "upcoming")],
                               new_snc=[("Cloud Run", "qualified"), ("New", "upcoming")])
        self.assertEqual(changes.qualification, [
            ("Cloud Run", "in_progress", "qualified"),
            ("Gone", "upcoming", None),
            ("New", None, "upcoming"),
        ])

    def test_compareRegion_lastUpdatedLineInBody_countsAsChange(self):
        changes = self.compare({"/a/docs": ("A", "Last updated: 2026-01-01\n", "2026-11-01")},
                               {"/a/docs": ("A", "Last updated: 2026-02-02\n", "2026-11-01")})
        self.assertEqual([p.path for p in changes.changed], ["/a/docs"])

    def test_compareRegion_renamedFile_readsEachSideThroughItsManifest(self):
        old = write_region(self.tmp / "old", {"/a/docs": ("A", "x\n", "2026-11-01")})
        new = write_region(self.tmp / "new", {"/a/docs": ("A", "x\n", "2026-11-01")})
        (new / "a_docs.md").rename(new / "docs_a.md")
        manifest = json.loads((new / "_manifest.json").read_text(encoding="utf-8"))
        manifest["/a/docs"]["filename"] = "docs_a.md"
        (new / "_manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        changes = note.compare_region(old, new)
        self.assertFalse(changes.has_content_changes)

    def test_compareRegion_filenameOutsideTheDirectory_raisesNoteError(self):
        old = write_region(self.tmp / "old", {})
        new = write_region(self.tmp / "new", {})
        (new / "_manifest.json").write_text(json.dumps({"/a": {"filename": "../x.md"}}), encoding="utf-8")
        with self.assertRaises(note.NoteError):
            note.compare_region(old, new)

    def test_compareRegion_malformedManifest_raisesNoteError(self):
        old = write_region(self.tmp / "old", {})
        new = self.tmp / "new"
        new.mkdir()
        (new / "_manifest.json").write_text("[]", encoding="utf-8")
        with self.assertRaises(note.NoteError):
            note.compare_region(old, new)


class InertTest(unittest.TestCase):
    def test_inert_mentionAndMarkup_areWrappedInACodeSpan(self):
        self.assertEqual(note.inert("@owner `x` <b>#12</b>\n"), "`@owner x <b>#12</b>`")

    def test_inert_longText_isCapped(self):
        self.assertLessEqual(len(note.inert("a" * 500)), note.MAX_TEXT + 2)

    def test_inert_emptyText_isAPlaceholder(self):
        self.assertEqual(note.inert("  "), "`(untitled)`")

    def test_inert_invisibleFormatCharacters_areRemoved(self):
        self.assertEqual(note.inert("a‮b​c\U000e0041"), "`abc`")


class TruncateTest(unittest.TestCase):
    def test_truncateOnLines_shortText_isUnchanged(self):
        self.assertEqual(note.truncate_on_lines("a\nb\n", 100, "more"), "a\nb\n")

    def test_truncateOnLines_longText_cutsOnALineBoundary(self):
        text = "".join(f"- `line {i}`\n" for i in range(100))
        cut = note.truncate_on_lines(text, 60, "see file")
        self.assertLessEqual(len(cut), 60 + len("\nsee file\n"))
        body = cut.split("\nsee file")[0]
        self.assertTrue(all(line.count("`") == 2 for line in body.splitlines()))
        self.assertTrue(cut.endswith("see file\n"))


class RenderTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def regions(self, old_pages, new_pages):
        old = write_region(self.tmp / "old", old_pages)
        new = write_region(self.tmp / "new", new_pages)
        return [("S3NS", note.compare_region(old, new))]

    def test_render_redatedOnly_saysContentUnchanged(self):
        regions = self.regions({"/a/docs": ("A", "x\n", "2026-11-01")},
                               {"/a/docs": ("A", "x\n", "2026-11-10")})
        text = note.render("2026-11-12", regions, failed=[])
        self.assertIn("# Documentation changes, 2026-11-12", text)
        self.assertIn("1 page re-dated with no content change", text)
        self.assertNotIn("### Changed", text)

    def test_render_changedPage_linksTheSourcePage(self):
        regions = self.regions({"/a/docs": ("A", "x\n", "2026-11-01")},
                               {"/a/docs": ("A", "y\n", "2026-11-10")})
        text = note.render("2026-11-12", regions, failed=[])
        self.assertIn(f"[`A`]({BASE}/a/docs)", text)
        self.assertIn("+1 −1", text)

    def test_render_failedRegion_warnsFirst(self):
        text = note.render("2026-11-12", self.regions({}, {}), failed=["Berlin"])
        self.assertLess(text.index("Warning"), text.index("## S3NS"))
        self.assertIn("Berlin", text)

    def test_render_unsafeSourceUrl_isNotLinked(self):
        regions = self.regions({}, {"/a/docs": ("A", "x\n", "")})
        page = regions[0][1].added[0]
        page.url = "javascript:alert(1)"
        text = note.render("2026-11-12", regions, failed=[])
        self.assertNotIn("javascript:", text)


class MainTest(unittest.TestCase):
    def test_main_writesTheNoteFile(self):
        tmp = Path(tempfile.mkdtemp())
        old = write_region(tmp / "old", {"/a/docs": ("A", "x\n", "2026-11-01")})
        new = write_region(tmp / "new", {"/a/docs": ("A", "y\n", "2026-11-10")})
        notes = tmp / "docs-changes"
        code = note.main(["--date", "2026-11-12", "--region", "S3NS", str(old), str(new),
                          "--notes-dir", str(notes)])
        self.assertEqual(code, 0)
        out = notes / "2026-11-12.md"
        self.assertIn("## S3NS", out.read_text(encoding="utf-8"))

    def test_main_secondRunSameDay_keepsTheFirstNote(self):
        tmp = Path(tempfile.mkdtemp())
        old = write_region(tmp / "old", {"/a/docs": ("A", "x\n", "")})
        new = write_region(tmp / "new", {"/a/docs": ("A", "y\n", "")})
        notes = tmp / "docs-changes"
        notes.mkdir()
        (notes / "2026-11-12.md").write_text("first", encoding="utf-8")
        args = ["--date", "2026-11-12", "--region", "S3NS", str(old), str(new), "--notes-dir", str(notes)]
        self.assertEqual(note.main(args), 0)
        self.assertEqual((notes / "2026-11-12.md").read_text(encoding="utf-8"), "first")
        self.assertIn("## S3NS", (notes / "2026-11-12-2.md").read_text(encoding="utf-8"))

    def test_main_prBody_isWrittenTruncated(self):
        tmp = Path(tempfile.mkdtemp())
        pages = {f"/p{i}/docs": (f"P{i}", f"{i}\n", "") for i in range(50)}
        old = write_region(tmp / "old", {})
        new = write_region(tmp / "new", pages)
        body = tmp / "body.md"
        args = ["--date", "2026-11-12", "--region", "S3NS", str(old), str(new),
                "--notes-dir", str(tmp / "notes"), "--pr-body", str(body), "--pr-body-limit", "500"]
        self.assertEqual(note.main(args), 0)
        text = body.read_text(encoding="utf-8")
        self.assertLess(len(text), 800)
        self.assertIn("docs-changes/2026-11-12.md", text)

    def test_main_invalidDate_isRejected(self):
        with self.assertRaises(SystemExit):
            note.main(["--date", "12/11/2026", "--region", "S3NS", "a", "b", "--notes-dir", "x"])


if __name__ == "__main__":
    unittest.main()
