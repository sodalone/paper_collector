import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "collect-ai-arxiv"
    / "scripts"
    / "collect_tro.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("collect_tro", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CollectTroTests(unittest.TestCase):
    def test_abstract_from_inverted_index_restores_word_order(self):
        mod = load_module()
        inverted = {
            "Robots": [0],
            "navigate": [2],
            "can": [1],
            "safely.": [3],
        }

        abstract = mod.abstract_from_inverted_index(inverted)

        self.assertEqual(abstract, "Robots can navigate safely.")

    def test_normalize_openalex_work_produces_report_paper_shape(self):
        mod = load_module()
        work = {
            "id": "https://openalex.org/W123",
            "doi": "https://doi.org/10.1109/TRO.2025.1234567",
            "title": "Safe Robot Navigation in Crowded Spaces",
            "publication_year": 2025,
            "publication_date": "2025-06-01",
            "updated_date": "2025-06-02T00:00:00",
            "abstract_inverted_index": {"Mobile": [0], "robots": [1], "avoid": [2], "collisions.": [3]},
            "authorships": [
                {"author": {"display_name": "Ada Lovelace"}},
                {"author": {"display_name": "Grace Hopper"}},
            ],
            "primary_location": {
                "landing_page_url": "https://ieeexplore.ieee.org/document/1234567",
                "pdf_url": "https://example.com/paper.pdf",
            },
            "biblio": {"first_page": "10", "last_page": "20"},
        }

        paper = mod.normalize_openalex_work(work, "TRO2025")

        self.assertEqual(paper["id"], "10.1109/tro.2025.1234567")
        self.assertEqual(paper["base_id"], "10.1109/tro.2025.1234567")
        self.assertEqual(paper["title"], "Safe Robot Navigation in Crowded Spaces")
        self.assertEqual(paper["summary"], "Mobile robots avoid collisions.")
        self.assertEqual(paper["authors"], ["Ada Lovelace", "Grace Hopper"])
        self.assertEqual(paper["published"], "2025-06-01")
        self.assertEqual(paper["abs_url"], "https://doi.org/10.1109/tro.2025.1234567")
        self.assertEqual(paper["pdf_url"], "https://example.com/paper.pdf")
        self.assertEqual(paper["source_category"], "TRO2025")
        self.assertEqual(paper["source_categories"], ["TRO2025"])
        self.assertIn("IEEE Transactions on Robotics", paper["categories"])
        self.assertEqual(paper["venue"], "IEEE Transactions on Robotics")
        self.assertEqual(paper["page"], "10-20")

    def test_is_research_article_excludes_corrections_and_editorials(self):
        mod = load_module()

        self.assertFalse(mod.is_research_article({"title": "Corrections to “A Robot Paper”"}))
        self.assertFalse(mod.is_research_article({"title": "Guest Editorial Special Collection on Tactile Robotics"}))
        self.assertTrue(mod.is_research_article({"title": "Tactile Planning for Dexterous Robot Hands"}))


if __name__ == "__main__":
    unittest.main()
