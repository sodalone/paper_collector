import importlib.util
import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "collect-ai-arxiv"
    / "scripts"
    / "collect_arxiv.py"
)
GITIGNORE_PATH = Path(__file__).resolve().parents[1] / ".gitignore"


def load_module():
    spec = importlib.util.spec_from_file_location("collect_arxiv", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CollectArxivTests(unittest.TestCase):
    def test_daily_window_defaults_to_previous_shanghai_day_in_utc(self):
        mod = load_module()
        now = datetime.fromisoformat("2026-06-24T10:30:00+08:00")

        window = mod.resolve_window("daily", date_arg=None, week_arg=None, now=now)

        self.assertEqual(window.label, "2026-06-23")
        self.assertEqual(window.start_utc.strftime("%Y%m%d%H%M"), "202606221600")
        self.assertEqual(window.end_utc.strftime("%Y%m%d%H%M"), "202606231600")

    def test_weekly_window_defaults_to_previous_full_iso_week(self):
        mod = load_module()
        now = datetime.fromisoformat("2026-06-24T10:30:00+08:00")

        window = mod.resolve_window("weekly", date_arg=None, week_arg=None, now=now)

        self.assertEqual(window.label, "2026-W25")
        self.assertEqual(window.start_utc.strftime("%Y%m%d%H%M"), "202606141600")
        self.assertEqual(window.end_utc.strftime("%Y%m%d%H%M"), "202606211600")

    def test_dedupe_merges_sources_and_categories_by_base_arxiv_id(self):
        mod = load_module()
        papers = [
            {
                "id": "2606.12345v1",
                "title": "A Robot Paper",
                "source_category": "cs.RO",
                "categories": ["cs.RO"],
            },
            {
                "id": "2606.12345v2",
                "title": "A Robot Paper",
                "source_category": "cs.CV",
                "categories": ["cs.CV"],
            },
        ]

        deduped = mod.dedupe_papers(papers)

        self.assertEqual(len(deduped), 1)
        self.assertEqual(deduped[0]["base_id"], "2606.12345")
        self.assertEqual(deduped[0]["id"], "2606.12345v2")
        self.assertEqual(deduped[0]["source_categories"], ["cs.CV", "cs.RO"])
        self.assertEqual(deduped[0]["categories"], ["cs.CV", "cs.RO"])

    def test_rule_classifier_high_recall_embodied_vla_manipulation(self):
        mod = load_module()
        paper = {
            "title": "Vision-Language-Action Policies for Contact-Rich Robot Manipulation",
            "summary": "We train a VLA robot policy for dexterous manipulation with tactile feedback.",
            "categories": ["cs.RO"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "high")
        self.assertEqual(classified["primary_contribution"], "Foundation/VLA Model")
        self.assertIn("Manipulation", classified["embodied_tasks"])
        self.assertIn("vla", classified["technique_tags"])
        self.assertIn("tactile", classified["technique_tags"])
        self.assertNotIn("primary_class", classified)
        self.assertNotIn("tags", classified)
        self.assertEqual(classified["uncertainty"], "")

    def test_rule_classifier_promotes_tactile_robot_exploration_to_manipulation(self):
        mod = load_module()
        paper = {
            "title": "Tactile-Driven Exploration for Object Localization",
            "summary": "A multi-fingered robot autonomously explores confined workspaces by touch.",
            "categories": ["cs.RO"],
            "source_categories": ["cs.RO"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "high")
        self.assertEqual(classified["primary_contribution"], "Policy/Control/Planning")
        self.assertIn("Manipulation", classified["embodied_tasks"])
        self.assertIn("tactile", classified["technique_tags"])

    def test_rule_classifier_excludes_medical_3d_cv_without_robot_action(self):
        mod = load_module()
        paper = {
            "title": "Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning",
            "summary": "Medical images span organs and radiology reports in clinical practice, with benchmark datasets and spatial regions for 3D CT models.",
            "categories": ["cs.CV"],
            "source_categories": ["cs.CV"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "none")

    def test_rule_classifier_excludes_image_text_manipulation_without_robot_context(self):
        mod = load_module()
        paper = {
            "title": "A Severity-Aware Benchmark for Contextual Image-Text Manipulation",
            "summary": "We evaluate image-text manipulation and document tampering localization for visual forensics.",
            "categories": ["cs.CV"],
            "source_categories": ["cs.CV"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "none")

    def test_rule_classifier_does_not_default_general_robotics_to_manipulation(self):
        mod = load_module()
        paper = {
            "title": "Temporal logics and formal synthesis for robot planning and control",
            "summary": "We study temporal logic specifications and controller synthesis for robotic systems.",
            "categories": ["cs.RO"],
            "source_categories": ["cs.RO"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "none")
        self.assertEqual(classified["primary_contribution"], "")

    def test_rule_classifier_excludes_autonomous_driving_without_embodied_ai_signal(self):
        mod = load_module()
        paper = {
            "title": "Autonomous Driving with Priority-Ordered STL Specifications Under Multimodal Uncertainty",
            "summary": "Autonomous vehicles plan trajectories that satisfy traffic rules with model predictive path integral control.",
            "categories": ["cs.RO"],
            "source_categories": ["cs.RO"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "none")

    def test_rule_classifier_excludes_transportation_agv_planning_without_embodied_ai_signal(self):
        mod = load_module()
        paper = {
            "title": "Optimization-based Safe Trajectory Planning for Autonomous Ground Vehicle in Multi-Floor Scenarios",
            "summary": (
                "Trajectory planning strategies for autonomous ground vehicles represent a research "
                "interest in intelligent transportation systems. The framework contains a task "
                "planning module and a trajectory planning module."
            ),
            "categories": ["cs.RO"],
            "source_categories": ["cs.RO"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "none")
        self.assertEqual(classified["primary_contribution"], "")

    def test_rule_classifier_excludes_ocr_long_horizon_without_embodiment(self):
        mod = load_module()
        paper = {
            "title": "Unlimited OCR Works",
            "summary": (
                "An end-to-end OCR model uses an LLM decoder for long-horizon copying tasks "
                "and working memory during document parsing."
            ),
            "categories": ["cs.CV"],
            "source_categories": ["cs.CV"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "none")
        self.assertEqual(classified["primary_contribution"], "")

    def test_rule_classifier_keeps_real_robot_manipulation(self):
        mod = load_module()
        paper = {
            "title": "Pose-Agnostic Robotic Functional Grasping via Observation-Action Canonicalization",
            "summary": "A robot arm learns functional grasping policies for real-world manipulation tasks.",
            "categories": ["cs.RO"],
            "source_categories": ["cs.RO"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "high")
        self.assertEqual(classified["primary_contribution"], "Policy/Control/Planning")
        self.assertIn("Manipulation", classified["embodied_tasks"])

    def test_qwen_robot_suite_multiaxis_classification_is_stable(self):
        mod = load_module()
        cases = [
            (
                "Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation",
                "A language-conditioned video world model for embodied intelligence predicts future visual trajectories across robotic manipulation and navigation.",
                "World Model/Representation",
                ["Manipulation", "Navigation"],
                ["world-model"],
            ),
            (
                "Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models",
                "Qwen-RobotManip is a generalizable Vision-Language-Action foundation model for robotic manipulation.",
                "Foundation/VLA Model",
                ["Manipulation"],
                ["vla", "robot-foundation-model"],
            ),
            (
                "Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System",
                "Qwen-RobotNav is a scalable navigation model for instruction following, object search, target tracking, and autonomous driving.",
                "Policy/Control/Planning",
                ["Navigation"],
                ["planning"],
            ),
        ]

        for title, summary, expected_contribution, expected_tasks, expected_tags in cases:
            with self.subTest(title=title):
                classified = mod.classify_paper(
                    {
                        "title": title,
                        "summary": summary,
                        "categories": ["cs.RO", "cs.CV"],
                        "source_categories": ["cs.RO", "cs.CV"],
                    }
                )
                self.assertEqual(classified["relevance"], "high")
                self.assertEqual(classified["primary_contribution"], expected_contribution)
                for task in expected_tasks:
                    self.assertIn(task, classified["embodied_tasks"])
                for tag in expected_tags:
                    self.assertIn(tag, classified["technique_tags"])

    def test_holoagent_framework_prefers_embodied_agent_over_task_mentions(self):
        mod = load_module()
        paper = {
            "title": "HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory",
            "summary": (
                "Embodied AgentOS converts language instructions into executable skill graphs, "
                "schedules robot resources, monitors execution, and triggers clarification or "
                "re-planning from runtime feedback. HoloAgent-0 organizes heterogeneous robot "
                "models and controllers through three coupled layers: Embodied AgentOS for "
                "closed-loop execution, 3D spatial memory for physical world grounding, and "
                "embodied skills for robot action. We evaluate long-horizon navigation, "
                "cross-robot coordination, and mobile manipulation."
            ),
            "categories": ["cs.CV", "cs.RO"],
            "source_categories": ["cs.CV", "cs.RO"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "high")
        self.assertEqual(classified["primary_contribution"], "Agent/System")
        self.assertIn("Navigation", classified["embodied_tasks"])
        self.assertIn("Manipulation", classified["embodied_tasks"])
        self.assertIn("planning", classified["technique_tags"])
        self.assertIn("spatial-memory", classified["technique_tags"])

    def test_simulated_physics_data_pipeline_prefers_simulation_over_long_horizon_agent(self):
        mod = load_module()
        paper = {
            "title": "Policy-as-Data: Learning Generalizable HOI Diffusion Models from Simulated Physics",
            "summary": (
                "Synthesizing realistic human-object interactions is critical for embodied avatars. "
                "The framework leverages policies trained with reinforcement learning in a physics "
                "simulator for task execution and data collection. The generated data supports "
                "human-object interaction diffusion models over long-horizon tasks."
            ),
            "categories": ["cs.CV"],
            "source_categories": ["cs.CV"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "high")
        self.assertEqual(classified["primary_contribution"], "Data/Benchmark/Simulation")

    def test_rule_classifier_assigns_general_cross_task_when_no_specific_task_matches(self):
        mod = load_module()
        paper = {
            "title": "Causal Reward World Models for Embodied Skill Generation",
            "summary": (
                "A robot world model supports automated skill generation across embodied tasks "
                "without focusing on any single robot application scenario."
            ),
            "categories": ["cs.RO"],
            "source_categories": ["cs.RO"],
        }

        classified = mod.classify_paper(paper)

        self.assertEqual(classified["relevance"], "high")
        self.assertEqual(classified["primary_contribution"], "World Model/Representation")
        self.assertEqual(classified["embodied_tasks"], ["General/Cross-task"])

    def test_classify_and_partition_keeps_rejected_papers_for_audit(self):
        mod = load_module()
        papers = [
            {
                "id": "2606.00001v1",
                "base_id": "2606.00001",
                "title": "Unlimited OCR Works",
                "summary": "An OCR model uses long-horizon copying and document parsing.",
                "categories": ["cs.CV"],
                "source_categories": ["cs.CV"],
            },
            {
                "id": "2606.00002v1",
                "base_id": "2606.00002",
                "title": "Robot Manipulation Policy",
                "summary": "A robot arm learns manipulation policies.",
                "categories": ["cs.RO"],
                "source_categories": ["cs.RO"],
            },
        ]

        selected, rejected, status = mod.classify_and_partition(
            papers,
            classifier="rules",
            llm_cache_path=Path("/tmp/unused.json"),
        )

        self.assertEqual([paper["base_id"] for paper in selected], ["2606.00002"])
        self.assertEqual([paper["base_id"] for paper in rejected], ["2606.00001"])
        self.assertEqual(rejected[0]["relevance"], "none")
        self.assertEqual(status["classifier"], "rules")
        self.assertEqual(status["selected"], 1)
        self.assertEqual(status["rejected"], 1)

    def test_autonomous_driving_rule_classifier_assigns_full_stack_categories(self):
        mod = load_module()
        cases = [
            (
                "VLM-Driven End-to-End Autonomous Driving Agents",
                "A vision-language driving foundation model predicts ego actions from camera observations for closed-loop autonomous driving.",
                "End-to-End Driving",
                ["foundation-driving-model", "vlm-driving"],
            ),
            (
                "BEV Occupancy Prediction for Autonomous Driving",
                "We propose a camera-based BEV occupancy perception model on nuScenes for 3D object detection and tracking.",
                "Perception",
                ["bev", "occupancy", "tracking"],
            ),
            (
                "Safe MPC Trajectory Planning for Autonomous Vehicles",
                "Autonomous vehicles use model predictive control and trajectory optimization for safe planning in urban driving.",
                "Planning/Control",
                ["planning", "control", "safety"],
            ),
            (
                "A Closed-Loop Benchmark and Simulator for Autonomous Driving",
                "We introduce a dataset, simulator, and benchmark for evaluating autonomous driving policies.",
                "Data/Simulation",
                ["dataset", "benchmark", "simulation"],
            ),
        ]

        for title, summary, expected_category, expected_tags in cases:
            with self.subTest(title=title):
                classified = mod.classify_paper(
                    {
                        "title": title,
                        "summary": summary,
                        "categories": ["cs.CV"],
                        "source_categories": ["cs.CV"],
                    },
                    profile="autonomous-driving",
                )

                self.assertEqual(classified["relevance"], "high")
                self.assertEqual(classified["driving_stack_category"], expected_category)
                self.assertNotIn("primary_contribution", classified)
                self.assertNotIn("embodied_tasks", classified)
                for tag in expected_tags:
                    self.assertIn(tag, classified["technique_tags"])

    def test_autonomous_driving_rule_classifier_rejects_noise(self):
        mod = load_module()
        for paper in [
            {
                "title": "Temporal logics and formal synthesis for robot planning and control",
                "summary": "We study controller synthesis for robotic systems.",
                "categories": ["cs.RO"],
                "source_categories": ["cs.RO"],
            },
            {
                "title": "Generic Object Detection with Vision Transformers",
                "summary": "A detector for natural images on common object recognition benchmarks.",
                "categories": ["cs.CV"],
                "source_categories": ["cs.CV"],
            },
            {
                "title": "Traffic Flow Forecasting for Urban Infrastructure",
                "summary": "A graph model forecasts traffic speed for intelligent transportation systems.",
                "categories": ["cs.CV"],
                "source_categories": ["cs.CV"],
            },
        ]:
            with self.subTest(title=paper["title"]):
                classified = mod.classify_paper(paper, profile="autonomous-driving")
                self.assertEqual(classified["relevance"], "none")

    def test_codex_classifier_maps_schema_and_writes_content_cache(self):
        mod = load_module()
        paper = {
            "id": "2606.23565v1",
            "base_id": "2606.23565",
            "title": "HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory",
            "summary": "A unified embodied agent framework with spatial memory for navigation and mobile manipulation.",
            "categories": ["cs.CV", "cs.RO"],
            "source_categories": ["cs.CV", "cs.RO"],
            "abs_url": "https://arxiv.org/abs/2606.23565v1",
        }
        calls = []

        def fake_run(cmd, input, text, capture_output, timeout):
            calls.append({"cmd": cmd, "input": input})
            out_path = Path(cmd[cmd.index("--output-last-message") + 1])
            out_path.write_text(
                json.dumps(
                    {
                        "papers": [
                            {
                                "id": "2606.23565v1",
                                "relevance": "high",
                                "primary_contribution": "Agent/System",
                                "embodied_tasks": ["Navigation", "Manipulation"],
                                "technique_tags": ["spatial-memory", "planning"],
                                "one_line_contribution": "提出统一具身 Agent 框架，用 3D 空间记忆支撑闭环执行。",
                                "problem_statement": "真实机器人长程任务执行缺少统一的空间记忆和闭环调度框架。",
                                "method_summary": "构建 Embodied AgentOS、3D spatial memory 和 embodied skills 三层框架。",
                                "classification_reason": "核心贡献是 AgentOS 与技能图闭环执行。",
                                "uncertainty": "",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            class Result:
                returncode = 0
                stderr = "codex noise"

            return Result()

        original_run = mod.subprocess.run
        mod.subprocess.run = fake_run
        try:
            with tempfile.TemporaryDirectory() as tmp:
                cache_path = Path(tmp) / "codex-classifications.json"
                classified, status = mod.classify_with_codex(
                    [paper],
                    llm_cache_path=cache_path,
                    profile="embodied",
                    batch_size=60,
                    timeout=30,
                    codex_model=None,
                    use_cache=True,
                )
                classified_again, status_again = mod.classify_with_codex(
                    [paper],
                    llm_cache_path=cache_path,
                    profile="embodied",
                    batch_size=60,
                    timeout=30,
                    codex_model=None,
                    use_cache=True,
                )
        finally:
            mod.subprocess.run = original_run

        self.assertEqual(len(calls), 1)
        self.assertEqual(classified[0]["primary_contribution"], "Agent/System")
        self.assertEqual(classified[0]["embodied_tasks"], ["Navigation", "Manipulation"])
        self.assertEqual(classified[0]["technique_tags"], ["spatial-memory", "planning"])
        self.assertEqual(classified[0]["problem_statement"], "真实机器人长程任务执行缺少统一的空间记忆和闭环调度框架。")
        self.assertEqual(classified[0]["method_summary"], "构建 Embodied AgentOS、3D spatial memory 和 embodied skills 三层框架。")
        self.assertEqual(status["status"], "ok")
        self.assertEqual(status_again["cache_hits"], 1)
        self.assertEqual(classified_again[0]["classifier"], "codex-cache")

    def test_autonomous_driving_codex_classifier_maps_schema(self):
        mod = load_module()
        paper = {
            "id": "2606.30000v1",
            "base_id": "2606.30000",
            "title": "VLM-Driven End-to-End Autonomous Driving Agents",
            "summary": "A VLM driving agent predicts ego actions for closed-loop autonomous driving.",
            "categories": ["cs.CV"],
            "source_categories": ["cs.CV"],
            "abs_url": "https://arxiv.org/abs/2606.30000v1",
        }

        def fake_run(cmd, input, text, capture_output, timeout):
            self.assertIn("Driving Stack", input)
            out_path = Path(cmd[cmd.index("--output-last-message") + 1])
            out_path.write_text(
                json.dumps(
                    {
                        "papers": [
                            {
                                "id": "2606.30000v1",
                                "relevance": "high",
                                "driving_stack_category": "End-to-End Driving",
                                "technique_tags": ["vlm-driving", "foundation-driving-model"],
                                "problem_statement": "端到端自动驾驶需要统一视觉语言推理和闭环动作输出。",
                                "method_summary": "用 VLM driving agent 从相机观测预测 ego actions。",
                                "classification_reason": "核心贡献是端到端 driving agent。",
                                "uncertainty": "",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            class Result:
                returncode = 0
                stderr = ""

            return Result()

        original_run = mod.subprocess.run
        mod.subprocess.run = fake_run
        try:
            with tempfile.TemporaryDirectory() as tmp:
                classified, status = mod.classify_with_codex(
                    [paper],
                    llm_cache_path=Path(tmp) / "codex-classifications.json",
                    profile="autonomous-driving",
                    batch_size=60,
                    timeout=30,
                    codex_model=None,
                    use_cache=True,
                )
        finally:
            mod.subprocess.run = original_run

        self.assertEqual(status["status"], "ok")
        self.assertEqual(classified[0]["driving_stack_category"], "End-to-End Driving")
        self.assertEqual(classified[0]["technique_tags"], ["vlm-driving", "foundation-driving-model"])

    def test_llm_cache_preserves_entries_across_profiles(self):
        mod = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            cache_path = Path(tmp) / "codex-classifications.json"
            embodied_entries = {"embodied-key": {"id": "2606.1v1"}}
            driving_entries = {"driving-key": {"id": "2606.2v1"}}

            mod.write_llm_cache(cache_path, embodied_entries, profile="embodied")
            mod.write_llm_cache(cache_path, driving_entries, profile="autonomous-driving")

            self.assertEqual(mod.load_llm_cache(cache_path, profile="embodied"), embodied_entries)
            self.assertEqual(mod.load_llm_cache(cache_path, profile="autonomous-driving"), driving_entries)

    def test_codex_classifier_failure_falls_back_to_rule_drafts(self):
        mod = load_module()
        paper = {
            "id": "2606.11111v1",
            "base_id": "2606.11111",
            "title": "Vision-Language-Action Policies for Robot Manipulation",
            "summary": "A VLA robot policy for manipulation.",
            "categories": ["cs.RO"],
            "source_categories": ["cs.RO"],
        }

        def fake_run(*_args, **_kwargs):
            raise TimeoutError("slow codex")

        original_run = mod.subprocess.run
        mod.subprocess.run = fake_run
        try:
            with tempfile.TemporaryDirectory() as tmp:
                classified, status = mod.classify_with_codex(
                    [paper],
                    llm_cache_path=Path(tmp) / "codex-classifications.json",
                    profile="embodied",
                    batch_size=60,
                    timeout=1,
                    codex_model=None,
                    use_cache=False,
                )
        finally:
            mod.subprocess.run = original_run

        self.assertEqual(status["status"], "fallback_rules")
        self.assertEqual(classified[0]["classifier"], "rules-fallback")
        self.assertEqual(classified[0]["primary_contribution"], "Foundation/VLA Model")
        self.assertTrue(classified[0]["problem_statement"])
        self.assertTrue(classified[0]["method_summary"])

    def test_render_markdown_uses_task_index_as_only_paper_body(self):
        mod = load_module()
        paper = {
            "id": "2606.12345v1",
            "base_id": "2606.12345",
            "title": "Embodied Navigation for Household Robots",
            "authors": ["Ada Lovelace", "Alan Turing"],
            "summary": "A robot navigation benchmark for household embodied agents.",
            "published": "2026-06-23T01:00:00Z",
            "updated": "2026-06-23T01:00:00Z",
            "abs_url": "https://arxiv.org/abs/2606.12345v1",
            "pdf_url": "https://arxiv.org/pdf/2606.12345v1",
            "categories": ["cs.RO"],
            "source_categories": ["cs.RO"],
        }
        classified = mod.classify_paper(paper)
        classified["problem_statement"] = "家庭机器人需要可评测的具身导航能力。"
        classified["method_summary"] = "构建 household navigation benchmark 并评估机器人导航模型。"
        report = mod.render_markdown(
            mode="daily",
            window=mod.resolve_window(
                "daily",
                date_arg="2026-06-23",
                week_arg=None,
                now=datetime.fromisoformat("2026-06-24T10:30:00+08:00"),
            ),
            papers=[classified],
            statuses=[{"source": "cs.RO", "method": "api", "status": "ok", "count": 1}],
        )

        self.assertIn("# 具身智能 arXiv 2026-06-23 日报", report)
        self.assertIn("## 统计概览", report)
        self.assertNotIn("## 高相关", report)
        self.assertNotIn("## 中相关", report)
        self.assertNotIn("## 低相关", report)
        self.assertNotIn("## 分类目录", report)
        self.assertIn("## Embodied Task 索引", report)
        self.assertIn("## 抓取状态", report)
        self.assertIn("主贡献分布", report)
        self.assertIn("任务分布", report)
        self.assertIn("六类分类:", report)
        self.assertIn("相关度:", report)
        self.assertIn("技术标签:", report)
        self.assertIn("解决问题: 家庭机器人需要可评测的具身导航能力。", report)
        self.assertIn("具体方法: 构建 household navigation benchmark 并评估机器人导航模型。", report)
        self.assertIn("分类理由:", report)
        self.assertNotIn("作者:", report)
        self.assertNotIn("arXiv category:", report)
        self.assertNotIn("摘要:", report)
        self.assertNotIn("分类器:", report)
        self.assertNotIn("不确定性:", report)
        self.assertNotIn("一句话贡献:", report)
        self.assertNotIn("主类:", report)
        self.assertNotIn("副标签:", report)
        self.assertIn("2606.12345", report)

    def test_render_markdown_repeats_multitask_papers_under_each_task_sorted_by_relevance(self):
        mod = load_module()
        window = mod.resolve_window(
            "daily",
            date_arg="2026-06-23",
            week_arg=None,
            now=datetime.fromisoformat("2026-06-24T10:30:00+08:00"),
        )
        multitask = {
            "id": "2606.23565v1",
            "base_id": "2606.23565",
            "title": "HoloAgent-0",
            "abs_url": "https://arxiv.org/abs/2606.23565v1",
            "primary_contribution": "Agent/System",
            "embodied_tasks": ["Manipulation", "Navigation"],
            "technique_tags": ["spatial-memory", "planning"],
            "relevance": "high",
            "problem_statement": "机器人长程执行缺少统一记忆。",
            "method_summary": "构建 AgentOS 与空间记忆。",
            "classification_reason": "核心贡献是系统框架。",
        }
        medium_nav = {
            "id": "2606.00003v1",
            "base_id": "2606.00003",
            "title": "Medium Navigation Paper",
            "abs_url": "https://arxiv.org/abs/2606.00003v1",
            "primary_contribution": "Policy/Control/Planning",
            "embodied_tasks": ["Navigation"],
            "technique_tags": ["navigation"],
            "relevance": "medium",
            "problem_statement": "导航策略泛化不足。",
            "method_summary": "提出规划改进。",
            "classification_reason": "核心贡献是规划。",
        }

        report = mod.render_markdown(
            mode="daily",
            window=window,
            papers=[medium_nav, multitask],
            statuses=[],
        )

        self.assertEqual(report.count("[HoloAgent-0]"), 2)
        self.assertLess(report.index("### Navigation"), report.index("### Manipulation"))
        navigation_section = report.split("### Navigation", 1)[1].split("### Manipulation", 1)[0]
        manipulation_section = report.split("### Manipulation", 1)[1].split("## 抓取状态", 1)[0]
        self.assertIn("[HoloAgent-0]", manipulation_section)
        self.assertIn("[HoloAgent-0]", navigation_section)
        self.assertLess(navigation_section.index("[HoloAgent-0]"), navigation_section.index("[Medium Navigation Paper]"))

    def test_render_markdown_weekly_title_includes_week_label_and_shanghai_dates(self):
        mod = load_module()
        window = mod.resolve_window(
            "weekly",
            date_arg=None,
            week_arg="2026-W25",
            now=datetime.fromisoformat("2026-06-25T10:30:00+08:00"),
        )

        report = mod.render_markdown(mode="weekly", window=window, papers=[], statuses=[])

        self.assertIn("# 具身智能 arXiv 2026-W25-0615-0621 周报", report)

    def test_autonomous_driving_render_markdown_uses_stack_index_once(self):
        mod = load_module()
        window = mod.resolve_window(
            "daily",
            date_arg="2026-06-24",
            week_arg=None,
            now=datetime.fromisoformat("2026-06-25T10:30:00+08:00"),
        )
        e2e = {
            "id": "2606.30000v1",
            "base_id": "2606.30000",
            "title": "VLM-Driven End-to-End Autonomous Driving Agents",
            "abs_url": "https://arxiv.org/abs/2606.30000v1",
            "driving_stack_category": "End-to-End Driving",
            "technique_tags": ["vlm-driving"],
            "relevance": "high",
            "problem_statement": "自动驾驶需要闭环端到端推理。",
            "method_summary": "训练 VLM driving agent 输出 ego actions。",
            "classification_reason": "核心贡献是端到端驾驶 agent。",
        }
        perception = {
            "id": "2606.30001v1",
            "base_id": "2606.30001",
            "title": "BEV Occupancy Prediction for Autonomous Driving",
            "abs_url": "https://arxiv.org/abs/2606.30001v1",
            "driving_stack_category": "Perception",
            "technique_tags": ["bev", "occupancy"],
            "relevance": "medium",
            "problem_statement": "自动驾驶需要稳定 3D 场景理解。",
            "method_summary": "预测 BEV occupancy 表示。",
            "classification_reason": "核心贡献是感知表示。",
        }

        report = mod.render_markdown(
            mode="daily",
            window=window,
            papers=[perception, e2e],
            statuses=[],
            profile="autonomous-driving",
        )

        self.assertIn("# 自动驾驶 arXiv 2026-06-24 日报", report)
        self.assertIn("## Driving Stack 索引", report)
        self.assertIn("### 端到端", report)
        self.assertIn("### 感知", report)
        self.assertIn("### 规控", report)
        self.assertIn("### 数据&仿真", report)
        self.assertEqual(report.count("[VLM-Driven End-to-End Autonomous Driving Agents]"), 1)
        self.assertEqual(report.count("[BEV Occupancy Prediction for Autonomous Driving]"), 1)
        self.assertIn("四类分类: `End-to-End Driving`", report)
        self.assertIn("解决问题: 自动驾驶需要闭环端到端推理。", report)
        self.assertNotIn("Embodied Task 索引", report)

    def test_fetch_source_uses_html_fallback_when_api_fails(self):
        mod = load_module()
        calls = []
        html = """
        <dt><a href="/abs/2606.11111v1">arXiv:2606.11111</a></dt>
        <dd>
          <div class="list-title mathjax"><span class="descriptor">Title:</span>
            Robot Navigation Benchmark
          </div>
          <div class="list-authors">Authors:
            <a>Ada Lovelace</a>, <a>Alan Turing</a>
          </div>
        </dd>
        """

        def fake_read_url(url, cache_path, no_cache, timeout, user_agent):
            calls.append(url)
            if len(calls) == 1:
                raise mod.FetchError("api down")
            return html, False

        original_read_url = mod.read_url
        original_page_size = mod.API_PAGE_SIZE
        original_sleep = mod.time.sleep
        mod.read_url = fake_read_url
        mod.API_PAGE_SIZE = 1
        mod.time.sleep = lambda _seconds: None
        try:
            with tempfile.TemporaryDirectory() as tmp:
                papers, status = mod.fetch_source(
                    source="cs.RO",
                    window=mod.resolve_window("daily", "2026-06-23", None),
                    raw_dir=Path(tmp),
                    max_results=10,
                    no_cache=False,
                    timeout=1,
                    user_agent="test",
                )
        finally:
            mod.read_url = original_read_url
            mod.API_PAGE_SIZE = original_page_size
            mod.time.sleep = original_sleep

        self.assertEqual(status["status"], "api_failed_fallback_ok")
        self.assertEqual(status["method"], "html-fallback")
        self.assertEqual(status["count"], 1)
        self.assertEqual(papers[0]["id"], "2606.11111v1")
        self.assertEqual(papers[0]["title"], "Robot Navigation Benchmark")

    def test_html_fallback_parses_real_arxiv_markup_and_filters_window_date(self):
        mod = load_module()
        calls = []
        html = """
        <dl id='articles'>
          <h3>Thu, 25 Jun 2026 (showing 1 of 1 entries )</h3>
          <dt>
            <a name='item1'>[1]</a>
            <a href ="/abs/2606.25000" title="Abstract" id="2606.25000">
              arXiv:2606.25000
            </a>
          </dt>
          <dd>
            <div class='meta'>
              <div class='list-title mathjax'><span class='descriptor'>Title:</span>
                Wrong Day Robot Paper
              </div>
              <div class='list-authors'><a>Ada Lovelace</a></div>
            </div>
          </dd>
          <h3>Wed, 24 Jun 2026 (showing 1 of 1 entries )</h3>
          <dt>
            <a name='item2'>[2]</a>
            <a href ="/abs/2606.24000" title="Abstract" id="2606.24000">
              arXiv:2606.24000
            </a>
          </dt>
          <dd>
            <div class='meta'>
              <div class='list-title mathjax'><span class='descriptor'>Title:</span>
                Right Day Robot Paper
              </div>
              <div class='list-authors'><a>Alan Turing</a>, <a>Grace Hopper</a></div>
            </div>
          </dd>
        </dl>
        """

        def fake_read_url(url, cache_path, no_cache, timeout, user_agent):
            calls.append(url)
            if len(calls) == 1:
                raise mod.FetchError("api down")
            return html, False

        original_read_url = mod.read_url
        original_page_size = mod.API_PAGE_SIZE
        original_sleep = mod.time.sleep
        mod.read_url = fake_read_url
        mod.API_PAGE_SIZE = 1
        mod.time.sleep = lambda _seconds: None
        try:
            with tempfile.TemporaryDirectory() as tmp:
                papers, status = mod.fetch_source(
                    source="cs.RO",
                    window=mod.resolve_window("daily", "2026-06-24", None),
                    raw_dir=Path(tmp),
                    max_results=10,
                    no_cache=False,
                    timeout=1,
                    user_agent="test",
                )
        finally:
            mod.read_url = original_read_url
            mod.API_PAGE_SIZE = original_page_size
            mod.time.sleep = original_sleep

        self.assertEqual(status["status"], "api_failed_fallback_ok")
        self.assertEqual(status["count"], 1)
        self.assertEqual([paper["id"] for paper in papers], ["2606.24000"])
        self.assertEqual(papers[0]["title"], "Right Day Robot Paper")
        self.assertEqual(papers[0]["authors"], ["Alan Turing", "Grace Hopper"])

    def test_fetch_source_pages_api_until_requested_limit(self):
        mod = load_module()
        calls = []

        def feed(arxiv_id, title):
            return f"""<?xml version="1.0" encoding="UTF-8"?>
            <feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
              <entry>
                <id>http://arxiv.org/abs/{arxiv_id}</id>
                <updated>2026-06-16T00:00:00Z</updated>
                <published>2026-06-16T00:00:00Z</published>
                <title>{title}</title>
                <summary>Robot manipulation policy.</summary>
                <author><name>Ada Lovelace</name></author>
                <arxiv:primary_category term="cs.RO" />
                <category term="cs.RO" />
                <link href="http://arxiv.org/abs/{arxiv_id}" rel="alternate" type="text/html" />
                <link title="pdf" href="http://arxiv.org/pdf/{arxiv_id}" rel="related" type="application/pdf" />
              </entry>
            </feed>"""

        def fake_read_url(url, cache_path, no_cache, timeout, user_agent):
            calls.append(url)
            if "start=0" in url:
                return feed("2606.11111v1", "First Robot Paper"), False
            if "start=1" in url:
                return feed("2606.22222v1", "Second Robot Paper"), False
            raise AssertionError(f"unexpected url: {url}")

        original_read_url = mod.read_url
        original_page_size = mod.API_PAGE_SIZE
        original_sleep = mod.time.sleep
        mod.read_url = fake_read_url
        mod.API_PAGE_SIZE = 1
        mod.time.sleep = lambda _seconds: None
        try:
            with tempfile.TemporaryDirectory() as tmp:
                papers, status = mod.fetch_source(
                    source="cs.RO",
                    window=mod.resolve_window("daily", "2026-06-16", None),
                    raw_dir=Path(tmp),
                    max_results=2,
                    no_cache=False,
                    timeout=1,
                    user_agent="test",
                )
        finally:
            mod.read_url = original_read_url
            mod.API_PAGE_SIZE = original_page_size
            mod.time.sleep = original_sleep

        self.assertEqual([paper["id"] for paper in papers], ["2606.11111v1", "2606.22222v1"])
        self.assertEqual(status["count"], 2)
        self.assertEqual(status["pages"], 2)
        self.assertTrue(any("start=1" in call for call in calls))

    def test_parser_uses_larger_default_limit_for_weekly_reports(self):
        mod = load_module()
        parser = mod.build_parser()

        daily = parser.parse_args(["daily"])
        weekly = parser.parse_args(["weekly", "--profile", "autonomous-driving"])

        self.assertEqual(daily.max_results, 100)
        self.assertEqual(daily.profile, "embodied")
        self.assertEqual(weekly.max_results, 1000)
        self.assertEqual(weekly.profile, "autonomous-driving")
        self.assertEqual(weekly.classifier, "codex")
        self.assertEqual(weekly.llm_batch_size, 60)
        self.assertEqual(weekly.classifier_timeout, 600)

    def test_parser_accepts_traecli_classifier_with_gpt55_high_defaults(self):
        mod = load_module()
        parser = mod.build_parser()

        weekly = parser.parse_args(["weekly", "--classifier", "traecli"])

        self.assertEqual(weekly.classifier, "traecli")
        self.assertEqual(weekly.trae_model, "GPT-5.5")
        self.assertEqual(weekly.trae_thinking_effort, "high")
        self.assertEqual(weekly.trae_verbosity, "high")

    def test_traecli_cache_path_is_separate_from_codex_cache(self):
        mod = load_module()

        self.assertEqual(
            mod.classification_cache_path(Path("/tmp/reports"), "traecli"),
            Path("/tmp/reports/.cache/traecli-classifications.json"),
        )
        self.assertEqual(
            mod.classification_cache_path(Path("/tmp/reports"), "codex"),
            Path("/tmp/reports/.cache/codex-classifications.json"),
        )

    def test_parse_traecli_json_response_reads_assistant_content_as_json(self):
        mod = load_module()
        payload = json.dumps(
            {
                "message": {
                    "role": "assistant",
                    "content": json.dumps(
                        {
                            "papers": [
                                {
                                    "id": "2606.00001v1",
                                    "relevance": "none",
                                    "primary_contribution": "",
                                    "embodied_tasks": [],
                                    "technique_tags": [],
                                    "one_line_contribution": "",
                                    "problem_statement": "不属于具身智能候选。",
                                    "method_summary": "未提出具身智能方法。",
                                    "classification_reason": "缺少机器人任务语境。",
                                    "uncertainty": "",
                                }
                            ]
                        },
                        ensure_ascii=False,
                    ),
                }
            },
            ensure_ascii=False,
        )

        parsed = mod.parse_traecli_json_response(payload)

        self.assertEqual(parsed["papers"][0]["id"], "2606.00001v1")
        self.assertEqual(parsed["papers"][0]["problem_statement"], "不属于具身智能候选。")

    def test_embodied_llm_prompt_requires_chinese_problem_and_method_fields(self):
        mod = load_module()
        prompt = mod.build_codex_prompt(
            [
                {
                    "id": "2606.00002v1",
                    "base_id": "2606.00002",
                    "title": "Robot Manipulation with World Models",
                    "summary": "We solve long-horizon robot manipulation with a learned world model.",
                    "categories": ["cs.RO"],
                    "source_categories": ["cs.RO"],
                }
            ],
            profile="embodied",
        )

        self.assertIn("必须使用中文", prompt)
        self.assertIn("不要直接复制英文摘要", prompt)
        self.assertIn("problem_statement", prompt)
        self.assertIn("method_summary", prompt)

    def test_output_paths_are_profile_scoped(self):
        mod = load_module()
        window = mod.resolve_window("weekly", date_arg=None, week_arg="2026-W25")
        report_path, json_path, raw_dir = mod.output_paths(
            Path("/tmp/reports"),
            mode="weekly",
            window=window,
            profile="autonomous-driving",
        )

        self.assertEqual(
            report_path,
            Path("/tmp/reports/autonomous-driving/weekly/自动驾驶 arXiv 2026-W25-0615-0621 周报.md"),
        )
        self.assertEqual(json_path, Path("/tmp/reports/autonomous-driving/weekly/2026-W25/papers.json"))
        self.assertEqual(raw_dir, Path("/tmp/reports/autonomous-driving/weekly/2026-W25/raw"))

    def test_report_filename_matches_report_title(self):
        mod = load_module()
        daily_window = mod.resolve_window("daily", date_arg="2026-06-24", week_arg=None)
        weekly_window = mod.resolve_window("weekly", date_arg=None, week_arg="2026-W25")

        self.assertEqual(
            mod.report_filename("daily", daily_window, profile="embodied"),
            "具身智能 arXiv 2026-06-24 日报.md",
        )
        self.assertEqual(
            mod.report_filename("weekly", weekly_window, profile="embodied"),
            "具身智能 arXiv 2026-W25-0615-0621 周报.md",
        )
        self.assertEqual(
            mod.report_filename("weekly", weekly_window, profile="autonomous-driving"),
            "自动驾驶 arXiv 2026-W25-0615-0621 周报.md",
        )

    def test_rename_existing_markdown_reports_uses_h1_and_is_idempotent(self):
        mod = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            report_root = Path(tmp) / "reports"
            daily_dir = report_root / "embodied" / "daily"
            daily_dir.mkdir(parents=True)
            old_path = daily_dir / "2026-06-24.md"
            old_path.write_text("# 具身智能 arXiv 2026-06-24 日报\n\n内容\n", encoding="utf-8")

            first_result = mod.rename_existing_markdown_reports(report_root)
            second_result = mod.rename_existing_markdown_reports(report_root)

            new_path = daily_dir / "具身智能 arXiv 2026-06-24 日报.md"
            self.assertEqual(first_result, [(old_path, new_path)])
            self.assertEqual(second_result, [])
            self.assertFalse(old_path.exists())
            self.assertEqual(new_path.read_text(encoding="utf-8"), "# 具身智能 arXiv 2026-06-24 日报\n\n内容\n")

    def test_copy_legacy_embodied_reports_does_not_overwrite_title_named_reports(self):
        mod = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            report_root = Path(tmp) / "reports"
            legacy_dir = report_root / "daily"
            profile_dir = report_root / "embodied" / "daily"
            legacy_dir.mkdir(parents=True)
            profile_dir.mkdir(parents=True)
            legacy_path = legacy_dir / "2026-06-24.md"
            target_path = profile_dir / "具身智能 arXiv 2026-06-24 日报.md"
            legacy_path.write_text("# 具身智能 arXiv 2026-06-24 日报\n\n旧内容\n", encoding="utf-8")
            target_path.write_text("# 具身智能 arXiv 2026-06-24 日报\n\n新内容\n", encoding="utf-8")

            mod.copy_legacy_embodied_reports(report_root)

            self.assertFalse((profile_dir / "2026-06-24.md").exists())
            self.assertEqual(target_path.read_text(encoding="utf-8"), "# 具身智能 arXiv 2026-06-24 日报\n\n新内容\n")

    def test_gitignore_keeps_report_markdown_and_ignores_regenerable_bundles(self):
        patterns = GITIGNORE_PATH.read_text(encoding="utf-8").splitlines()

        self.assertIn("reports/.cache/", patterns)
        self.assertIn("reports/**/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/", patterns)
        self.assertIn("reports/**/[0-9][0-9][0-9][0-9]-W[0-9][0-9]/", patterns)
        self.assertIn("reports/**/raw/", patterns)
        self.assertIn("reports/daily/", patterns)
        self.assertIn("reports/weekly/", patterns)
        self.assertIn(".DS_Store", patterns)
        self.assertNotIn("reports/**/*.md", patterns)


if __name__ == "__main__":
    unittest.main()
