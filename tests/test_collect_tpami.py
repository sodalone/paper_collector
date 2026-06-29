import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "collect-ai-arxiv"
    / "scripts"
    / "collect_tpami.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("collect_tpami", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CollectTpamiTests(unittest.TestCase):
    def test_normalize_doi_strips_url_and_lowercases(self):
        mod = load_module()

        self.assertEqual(
            mod.normalize_doi("https://doi.org/10.1109/TPAMI.2025.3528723"),
            "10.1109/tpami.2025.3528723",
        )
        self.assertEqual(mod.normalize_doi(" 10.1109/TPAMI.2026.3656763 "), "10.1109/tpami.2026.3656763")
        self.assertEqual(mod.normalize_doi(None), "")

    def test_normalize_csdl_article_produces_report_paper_shape(self):
        mod = load_module()
        article = {
            "id": "23vhkaFU1Ne",
            "doi": "10.1109/TPAMI.2025.3528723",
            "title": "A Survey of Behavior Foundation Model",
            "abstract": "Humanoid robots need reusable whole-body control priors.",
            "authors": [{"fullName": "Ada Lovelace"}, {"fullName": "Grace Hopper"}],
            "year": "2026",
            "issueNum": "04",
            "pages": "4909-4927",
            "pubDate": "2026-04-01",
            "fno": "11319214",
            "idPrefix": "tp",
        }
        issue = {"year": "2026", "issueNum": "04", "volume": "48", "label": "Apr. 2026"}

        paper = mod.normalize_csdl_article(article, issue)

        self.assertEqual(paper["id"], "10.1109/tpami.2025.3528723")
        self.assertEqual(paper["base_id"], "10.1109/tpami.2025.3528723")
        self.assertEqual(paper["title"], "A Survey of Behavior Foundation Model")
        self.assertEqual(paper["summary"], "Humanoid robots need reusable whole-body control priors.")
        self.assertEqual(paper["authors"], ["Ada Lovelace", "Grace Hopper"])
        self.assertEqual(paper["published"], "2026-04-01")
        self.assertEqual(paper["abs_url"], "https://www.computer.org/csdl/journal/tp/2026/04/11319214/23vhkaFU1Ne")
        self.assertEqual(paper["pdf_url"], "https://doi.org/10.1109/tpami.2025.3528723")
        self.assertEqual(paper["source_category"], "TPAMI2026")
        self.assertEqual(paper["source_categories"], ["TPAMI2026", "TPAMI2026-04"])
        self.assertIn("IEEE Transactions on Pattern Analysis and Machine Intelligence", paper["categories"])
        self.assertEqual(paper["venue"], "IEEE Transactions on Pattern Analysis and Machine Intelligence")
        self.assertEqual(paper["page"], "4909-4927")
        self.assertEqual(paper["issue"], "2026-04")
        self.assertEqual(paper["volume"], "48")

    def test_official_issue_list_stops_at_current_year_limit(self):
        mod = load_module()

        self.assertEqual(mod.issue_numbers_for_year(2025, current_year=2026, current_month=6), ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
        self.assertEqual(mod.issue_numbers_for_year(2026, current_year=2026, current_month=6), ["01", "02", "03", "04", "05", "06"])
        self.assertEqual(mod.issue_numbers_for_year(2027, current_year=2026, current_month=6), [])


if __name__ == "__main__":
    unittest.main()
