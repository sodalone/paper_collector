#!/usr/bin/env python3
"""Collect AI arXiv digests from cs.RO/cs.CV with profile-specific classifiers."""

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, time as dt_time, timedelta, timezone
from html import unescape
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


API_URL = "https://export.arxiv.org/api/query"
LIST_URL = "https://arxiv.org/list/{source}/recent?skip=0&show={limit}"
DEFAULT_SOURCES = ("cs.RO", "cs.CV")
DEFAULT_USER_AGENT = "collect-ai-arxiv/0.2"
API_PAGE_SIZE = 100
DEFAULT_DAILY_MAX_RESULTS = 100
DEFAULT_WEEKLY_MAX_RESULTS = 1000
DEFAULT_LLM_BATCH_SIZE = 60
DEFAULT_CLASSIFIER_TIMEOUT = 600
DEFAULT_TRAE_MODEL = "GPT-5.5"
DEFAULT_TRAE_THINKING_EFFORT = "high"
DEFAULT_TRAE_VERBOSITY = "high"
EMBODIED_PROFILE = "embodied"
AUTONOMOUS_DRIVING_PROFILE = "autonomous-driving"
DEFAULT_PROFILE = EMBODIED_PROFILE
PROFILES = (EMBODIED_PROFILE, AUTONOMOUS_DRIVING_PROFILE)
TAXONOMY_VERSIONS = {
    EMBODIED_PROFILE: "embodied-task-index-problem-method-2026-06-24",
    AUTONOMOUS_DRIVING_PROFILE: "autonomous-driving-stack-v1-2026-06-25",
}
TAXONOMY_VERSION = TAXONOMY_VERSIONS[EMBODIED_PROFILE]
SHANGHAI = timezone(timedelta(hours=8), "Asia/Shanghai")
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
ARXIV_ID_RE = re.compile(
    r"(?P<base>(?:\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7}))(?P<version>v\d+)?",
    re.I,
)
TAG_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"\s+")

PRIMARY_CONTRIBUTIONS = (
    "Foundation/VLA Model",
    "Agent/System",
    "World Model/Representation",
    "Policy/Control/Planning",
    "Data/Benchmark/Simulation",
    "Safety/Evaluation",
)

EMBODIED_TASKS = (
    "Navigation",
    "Manipulation",
    "Locomotion",
    "Whole-body",
    "HRI",
    "General/Cross-task",
)

RELEVANCE_TIERS = ("high", "medium", "low", "none")

TAXONOMY_ORDER = list(PRIMARY_CONTRIBUTIONS)

DRIVING_STACK_CATEGORIES = (
    "End-to-End Driving",
    "Perception",
    "Planning/Control",
    "Data/Simulation",
)

DRIVING_STACK_LABELS = {
    "End-to-End Driving": "端到端",
    "Perception": "感知",
    "Planning/Control": "规控",
    "Data/Simulation": "数据&仿真",
}

CLASS_KEYWORDS: Sequence[Tuple[str, Sequence[str]]] = (
    (
        "VLA",
        (
            "vla",
            "vision-language-action",
            "vision language action",
            "robot foundation model",
            "embodied foundation model",
            "generalist robot",
            "action token",
            "action chunk",
            "multimodal policy",
            "large behavior model",
        ),
    ),
    (
        "Whole-body",
        (
            "whole-body",
            "whole body",
            "loco-manipulation",
            "locomanipulation",
            "mobile manipulation",
            "humanoid manipulation",
            "multi-contact",
            "box carrying",
            "door opening",
        ),
    ),
    (
        "World Modeling",
        (
            "world model",
            "world modeling",
            "world-action",
            "world action",
            "video world model",
            "3d scene",
            "semantic map",
            "occupancy",
            "scene graph",
            "3d gaussian",
            "nerf",
            "affordance",
            "spatial memory",
            "active perception",
        ),
    ),
    (
        "Manipulation",
        (
            "manipulation",
            "grasp",
            "pick-and-place",
            "pick and place",
            "dexterous",
            "bimanual",
            "tool use",
            "contact-rich",
            "tactile",
            "multi-fingered",
            "touch",
            "insertion",
            "peg-in-hole",
            "articulated object",
        ),
    ),
    (
        "Locomotion",
        (
            "locomotion",
            "legged",
            "quadruped",
            "biped",
            "humanoid locomotion",
            "gait",
            "terrain",
            "fall recovery",
            "motion tracking",
            "balance control",
        ),
    ),
    (
        "Navigation",
        (
            "navigation",
            "embodied navigation",
            "objectnav",
            "object navigation",
            "pointnav",
            "imagenav",
            "vln",
            "visual navigation",
            "semantic navigation",
            "active exploration",
            "frontier exploration",
            "topological map",
        ),
    ),
    (
        "Embodied Agent",
        (
            "embodied agent",
            "long-horizon",
            "long horizon",
            "task planning",
            "hierarchical planning",
            "llm planner",
            "vlm planner",
            "skill chaining",
            "replanning",
            "failure recovery",
            "episodic memory",
        ),
    ),
    (
        "Simulation/Data/Benchmark",
        (
            "simulator",
            "benchmark",
            "dataset",
            "robot data",
            "demonstration dataset",
            "teleoperation",
            "synthetic data",
            "sim-to-real",
            "sim2real",
            "data engine",
            "evaluation suite",
        ),
    ),
    (
        "HRI/Safety",
        (
            "human-robot interaction",
            "hri",
            "social navigation",
            "robot safety",
            "safe robot",
            "safe rl",
            "shared autonomy",
            "human preference",
            "collaborative robot",
            "instruction clarification",
        ),
    ),
)

TITLE_CORE_KEYWORDS: Sequence[Tuple[str, Sequence[str]]] = (
    (
        "VLA",
        (
            "vla",
            "vision-language-action",
            "vision language action",
            "robot foundation model",
            "robotic foundation model",
            "embodied foundation model",
        ),
    ),
    (
        "Simulation/Data/Benchmark",
        (
            "benchmark",
            "dataset",
            "simulator",
            "simulated physics",
            "policy-as-data",
            "evaluation suite",
        ),
    ),
    (
        "Embodied Agent",
        (
            "embodied agent framework",
            "unified embodied agent",
            "embodied agentos",
            "embodied agent",
        ),
    ),
    (
        "World Modeling",
        (
            "world model",
            "world modeling",
            "world-action",
            "world action model",
            "video world model",
        ),
    ),
)

TAG_KEYWORDS: Sequence[Tuple[str, Sequence[str]]] = (
    ("vla", ("vla", "vision-language-action", "vision language action")),
    (
        "robot-foundation-model",
        ("robot foundation model", "robotic foundation model", "robotic manipulation foundation model", "embodied foundation model", "foundation models"),
    ),
    ("action-tokenization", ("action token", "action tokenization")),
    ("diffusion-policy", ("diffusion policy", "diffusion policies")),
    ("manipulation", ("manipulation", "grasp", "pick-and-place", "dexterous")),
    ("tactile", ("tactile", "visuotactile", "force feedback", "haptic")),
    ("locomotion", ("locomotion", "legged", "quadruped", "biped", "gait")),
    ("whole-body", ("whole-body", "whole body", "loco-manipulation")),
    ("navigation", ("navigation", "objectnav", "pointnav", "vln")),
    ("world-model", ("world model", "world modeling", "predictive model")),
    ("spatial-memory", ("spatial memory", "episodic memory")),
    ("planning", ("planning", "planner", "task decomposition", "replanning", "navigation model")),
    ("benchmark", ("benchmark", "evaluation suite")),
    ("dataset", ("dataset", "robot data", "demonstration data")),
    ("sim2real", ("sim-to-real", "sim2real", "domain randomization")),
    ("hri", ("human-robot interaction", "hri", "shared autonomy")),
    ("safety", ("safety", "safe rl", "cbf", "verification")),
    (
        "deployment-system-reliability",
        ("deployment", "runtime", "latency", "calibration", "fleet", "data standard"),
    ),
)

STRONG_EMBODIED_TERMS = (
    "robot",
    "robotic",
    "embodied",
    "humanoid",
    "quadruped",
    "biped",
    "robot policy",
    "robot policies",
    "dexterous",
    "grasp",
    "bimanual",
    "tactile",
    "contact-rich",
    "multi-fingered",
    "locomotion",
    "navigation",
    "teleoperation",
    "sim-to-real",
    "vision-language-action",
    "vla",
)

WEAK_EMBODIED_TERMS = (
    "3d scene",
    "affordance",
    "spatial",
    "world model",
    "scene graph",
    "active perception",
    "long-horizon",
    "task planning",
)

NON_EMBODIED_CV_TERMS = (
    "medical",
    "radiolog",
    "clinical",
    "patient",
    "organ",
    "anatom",
    "mri",
    "ct ",
    " ct",
    "ocr",
    "document parsing",
    "text recognition",
)

PHYSICAL_ROBOT_CONTEXT_TERMS = (
    "robot",
    "robotic",
    "embodied",
    "humanoid",
    "manipulator",
    "gripper",
    "dexterous",
    "grasp",
    "bimanual",
    "tactile",
    "teleoperation",
    "sim-to-real",
    "vision-language-action",
    "vla",
)

NON_EMBODIED_MANIPULATION_TERMS = (
    "image-text manipulation",
    "image text manipulation",
    "image manipulation",
    "video manipulation",
    "text manipulation",
    "document tampering",
    "tampering localization",
    "image forensics",
    "visual forensics",
    "deepfake",
    "face forgery",
    "image editing",
    "text-to-image",
)

AUTONOMOUS_DRIVING_TERMS = (
    "autonomous driving",
    "automated driving",
    "autonomous vehicle",
    "autonomous vehicles",
    "autonomous ground vehicle",
    "autonomous ground vehicles",
    "intelligent transportation systems",
    "self-driving",
    "traffic rules",
    "trajectory prediction",
    "ego trajectory",
)

GENERIC_ROBOTICS_NEGATIVE_TERMS = (
    "temporal logic",
    "formal synthesis",
    "linear temporal logic",
    "signal temporal logic specifications",
)

CONTRIBUTION_KEYWORDS: Dict[str, Sequence[str]] = {
    "Foundation/VLA Model": (
        "vla",
        "vision-language-action",
        "vision language action",
        "robot foundation model",
        "robotic foundation model",
        "embodied foundation model",
        "generalist robot",
        "action token",
        "action chunk",
        "multimodal policy",
        "large behavior model",
        "foundation models",
    ),
    "Agent/System": (
        "embodied agent framework",
        "unified embodied agent",
        "embodied agentos",
        "agentos",
        "skill graph",
        "skill library",
        "skill chaining",
        "closed-loop execution",
        "cross-robot coordination",
        "heterogeneous robot",
        "robot resources",
        "runtime feedback",
        "failure recovery",
    ),
    "World Model/Representation": (
        "world model",
        "world modeling",
        "world-action",
        "world action",
        "video world model",
        "spatial memory",
        "semantic map",
        "occupancy",
        "scene graph",
        "3d gaussian",
        "nerf",
        "affordance",
        "active perception",
        "3d scene",
    ),
    "Policy/Control/Planning": (
        "policy",
        "policies",
        "control",
        "controller",
        "planning",
        "planner",
        "trajectory",
        "motion generation",
        "motion planning",
        "reinforcement learning",
        "imitation learning",
        "diffusion policy",
        "navigation model",
        "manipulation policy",
        "locomotion",
        "whole-body control",
    ),
    "Data/Benchmark/Simulation": (
        "benchmark",
        "dataset",
        "simulator",
        "simulation",
        "simulated physics",
        "policy-as-data",
        "robot data",
        "demonstration dataset",
        "teleoperation",
        "synthetic data",
        "sim-to-real",
        "sim2real",
        "data engine",
        "evaluation suite",
        "data collection",
    ),
    "Safety/Evaluation": (
        "safety",
        "safe robot",
        "safe rl",
        "verification",
        "formal verification",
        "red-teaming",
        "red teaming",
        "risk",
        "robustness",
        "watermark",
        "error detection",
        "failure detection",
        "human preference",
    ),
}

TASK_KEYWORDS: Dict[str, Sequence[str]] = {
    "Manipulation": (
        "manipulation",
        "grasp",
        "pick-and-place",
        "pick and place",
        "dexterous",
        "bimanual",
        "tool use",
        "contact-rich",
        "tactile",
        "multi-fingered",
        "insertion",
        "peg-in-hole",
        "articulated object",
        "mobile manipulation",
    ),
    "Navigation": (
        "navigation",
        "embodied navigation",
        "objectnav",
        "object navigation",
        "pointnav",
        "imagenav",
        "vln",
        "visual navigation",
        "semantic navigation",
        "active exploration",
        "frontier exploration",
        "topological map",
        "object search",
    ),
    "Locomotion": (
        "locomotion",
        "legged",
        "quadruped",
        "biped",
        "humanoid locomotion",
        "gait",
        "terrain",
        "fall recovery",
        "balance control",
    ),
    "Whole-body": (
        "whole-body",
        "whole body",
        "loco-manipulation",
        "locomanipulation",
        "humanoid manipulation",
        "multi-contact",
        "full-body",
    ),
    "HRI": (
        "human-robot interaction",
        "hri",
        "social navigation",
        "shared autonomy",
        "collaborative robot",
        "instruction clarification",
    ),
    "General/Cross-task": (),
}

TECHNIQUE_TAGS = tuple(tag for tag, _keywords in TAG_KEYWORDS)

AUTONOMOUS_DRIVING_CONTEXT_TERMS = (
    "autonomous driving",
    "automated driving",
    "self-driving",
    "driverless",
    "autonomous vehicle",
    "autonomous vehicles",
    "ego vehicle",
    "ego car",
    "driving scene",
    "driving scenes",
    "driving scenario",
    "driving scenarios",
    "urban driving",
    "closed-loop driving",
    "nuScenes".lower(),
    "waymo",
    "kitti",
    "argoverse",
    "lyft level 5",
)

TRAFFIC_ENGINEERING_NEGATIVE_TERMS = (
    "traffic flow",
    "traffic speed",
    "traffic forecasting",
    "traffic signal",
    "road network",
    "urban infrastructure",
    "intelligent transportation systems",
)

AUTONOMOUS_DRIVING_STACK_KEYWORDS: Dict[str, Sequence[str]] = {
    "End-to-End Driving": (
        "end-to-end",
        "end to end",
        "e2e",
        "driving foundation model",
        "foundation driving model",
        "vlm driving",
        "llm driving",
        "driving agent",
        "world model for autonomous driving",
        "ego actions",
        "closed-loop driving",
    ),
    "Perception": (
        "perception",
        "bev",
        "occupancy",
        "object detection",
        "3d detection",
        "lane detection",
        "segmentation",
        "tracking",
        "prediction",
        "trajectory prediction",
        "mapping",
        "localization",
        "odometry",
        "sensor fusion",
        "lidar",
        "radar",
        "camera",
    ),
    "Planning/Control": (
        "planning",
        "planner",
        "control",
        "controller",
        "mpc",
        "model predictive control",
        "trajectory optimization",
        "motion planning",
        "trajectory planning",
        "path planning",
        "policy",
        "reinforcement learning",
    ),
    "Data/Simulation": (
        "dataset",
        "benchmark",
        "simulator",
        "simulation",
        "synthetic data",
        "closed-loop benchmark",
        "safety evaluation",
        "evaluation",
        "scenario generation",
        "digital twin",
    ),
}

AUTONOMOUS_DRIVING_TAG_KEYWORDS: Sequence[Tuple[str, Sequence[str]]] = (
    ("end-to-end", ("end-to-end", "end to end", "e2e")),
    ("foundation-driving-model", ("driving foundation model", "foundation driving model", "foundation model")),
    ("vlm-driving", ("vlm driving", "vision-language", "vision language", "llm driving", "driving agent")),
    ("bev", ("bev", "bird's-eye view", "bird eye view")),
    ("occupancy", ("occupancy", "occupancy prediction")),
    ("3d-detection", ("3d detection", "object detection")),
    ("tracking", ("tracking", "multi-object tracking")),
    ("prediction", ("prediction", "trajectory prediction", "motion prediction")),
    ("mapping", ("mapping", "hd map", "map construction")),
    ("localization", ("localization", "odometry", "pose estimation")),
    ("planning", ("planning", "planner", "path planning", "motion planning", "trajectory planning")),
    ("control", ("control", "controller", "mpc", "model predictive control")),
    ("safety", ("safety", "safe", "collision", "risk", "verification")),
    ("dataset", ("dataset", "data collection")),
    ("benchmark", ("benchmark", "evaluation suite", "closed-loop benchmark")),
    ("simulation", ("simulator", "simulation", "scenario generation", "synthetic data")),
    ("closed-loop", ("closed-loop", "closed loop")),
    ("sensor-fusion", ("sensor fusion", "multimodal fusion", "multi-modal fusion")),
    ("lidar", ("lidar", "point cloud")),
    ("camera", ("camera", "vision-based", "camera-based")),
    ("radar", ("radar",)),
    ("v2x", ("v2x", "vehicle-to-everything", "cooperative driving")),
    (
        "deployment-system-reliability",
        ("deployment", "runtime", "latency", "calibration", "real-time", "real time"),
    ),
)

AUTONOMOUS_DRIVING_TECHNIQUE_TAGS = tuple(tag for tag, _keywords in AUTONOMOUS_DRIVING_TAG_KEYWORDS)


@dataclass
class Window:
    label: str
    start_local: datetime
    end_local: datetime
    start_utc: datetime
    end_utc: datetime

    @property
    def api_range(self) -> str:
        return (
            f"{self.start_utc.strftime('%Y%m%d%H%M')}"
            f"+TO+{self.end_utc.strftime('%Y%m%d%H%M')}"
        )


class FetchError(Exception):
    pass


def validate_profile(profile: str) -> str:
    if profile not in PROFILES:
        raise ValueError(f"Unsupported profile: {profile}")
    return profile


def taxonomy_version(profile: str = DEFAULT_PROFILE) -> str:
    return TAXONOMY_VERSIONS[validate_profile(profile)]


def ensure_aware(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=SHANGHAI)
    return dt.astimezone(SHANGHAI)


def resolve_window(
    mode: str,
    date_arg: Optional[str],
    week_arg: Optional[str],
    now: Optional[datetime] = None,
) -> Window:
    now_local = ensure_aware(now or datetime.now(SHANGHAI))
    if mode == "daily":
        target = date.fromisoformat(date_arg) if date_arg else now_local.date() - timedelta(days=1)
        start_local = datetime.combine(target, dt_time.min, tzinfo=SHANGHAI)
        end_local = start_local + timedelta(days=1)
        label = target.isoformat()
    elif mode == "weekly":
        if week_arg:
            year_str, week_str = week_arg.upper().split("-W", 1)
            start_day = date.fromisocalendar(int(year_str), int(week_str), 1)
        else:
            current_week_monday = now_local.date() - timedelta(days=now_local.weekday())
            start_day = current_week_monday - timedelta(days=7)
        end_day = start_day + timedelta(days=7)
        start_local = datetime.combine(start_day, dt_time.min, tzinfo=SHANGHAI)
        end_local = datetime.combine(end_day, dt_time.min, tzinfo=SHANGHAI)
        iso = start_day.isocalendar()
        label = f"{iso[0]}-W{iso[1]:02d}"
    else:
        raise ValueError(f"Unsupported mode: {mode}")
    return Window(
        label=label,
        start_local=start_local,
        end_local=end_local,
        start_utc=start_local.astimezone(timezone.utc),
        end_utc=end_local.astimezone(timezone.utc),
    )


def strip_tags(value: str) -> str:
    return WHITESPACE_RE.sub(" ", unescape(TAG_RE.sub(" ", value))).strip()


def base_arxiv_id(arxiv_id: str) -> str:
    match = ARXIV_ID_RE.search(arxiv_id)
    if not match:
        return arxiv_id
    return match.group("base")


def version_number(arxiv_id: str) -> int:
    match = re.search(r"v(\d+)$", arxiv_id)
    return int(match.group(1)) if match else 0


def cache_key(parts: Iterable[str]) -> str:
    raw = "__".join(parts)
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", raw).strip("_")


def read_url(
    url: str,
    cache_path: Path,
    no_cache: bool,
    timeout: int,
    user_agent: str,
) -> Tuple[str, bool]:
    if cache_path.exists() and not no_cache:
        return cache_path.read_text(encoding="utf-8"), True
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})
    last_error: Optional[Exception] = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                text = response.read().decode("utf-8", "replace")
            cache_path.write_text(text, encoding="utf-8")
            return text, False
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 429:
                break
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
        if attempt == 0:
            time.sleep(3)
    raise FetchError(str(last_error))


def build_api_url(source: str, window: Window, start: int, max_results: int) -> str:
    query = (
        f"cat:{source} AND "
        f"submittedDate:[{window.start_utc.strftime('%Y%m%d%H%M')} "
        f"TO {window.end_utc.strftime('%Y%m%d%H%M')}]"
    )
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": start,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    return f"{API_URL}?{params}"


def parse_api_feed(xml_text: str, source: str) -> List[Dict]:
    root = ET.fromstring(xml_text)
    papers: List[Dict] = []
    for entry in root.findall(f"{ATOM}entry"):
        abs_id = entry.findtext(f"{ATOM}id", default="")
        arxiv_id = abs_id.rstrip("/").split("/")[-1]
        links = {link.attrib.get("title") or link.attrib.get("rel"): link.attrib for link in entry.findall(f"{ATOM}link")}
        categories = sorted(
            {
                node.attrib.get("term", "")
                for node in entry.findall(f"{ATOM}category")
                if node.attrib.get("term")
            }
        )
        primary = entry.find(f"{ARXIV}primary_category")
        if primary is not None and primary.attrib.get("term"):
            categories = sorted(set(categories + [primary.attrib["term"]]))
        authors = [
            strip_tags(author.findtext(f"{ATOM}name", default=""))
            for author in entry.findall(f"{ATOM}author")
        ]
        paper = {
            "id": arxiv_id,
            "base_id": base_arxiv_id(arxiv_id),
            "title": strip_tags(entry.findtext(f"{ATOM}title", default="")),
            "summary": strip_tags(entry.findtext(f"{ATOM}summary", default="")),
            "authors": [a for a in authors if a],
            "published": entry.findtext(f"{ATOM}published", default=""),
            "updated": entry.findtext(f"{ATOM}updated", default=""),
            "abs_url": links.get("alternate", {}).get("href", f"https://arxiv.org/abs/{arxiv_id}"),
            "pdf_url": links.get("pdf", {}).get("href", f"https://arxiv.org/pdf/{arxiv_id}"),
            "categories": categories or [source],
            "source_category": source,
            "source_categories": [source],
            "fetch_method": "api",
        }
        papers.append(paper)
    return papers


def parse_list_heading_date(heading_html: str) -> Optional[date]:
    text = strip_tags(heading_html)
    match = re.search(r"\b[A-Z][a-z]{2},\s+\d{1,2}\s+[A-Z][a-z]{2}\s+\d{4}\b", text)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(0), "%a, %d %b %Y").date()
    except ValueError:
        return None


def date_in_window(day: Optional[date], window: Optional[Window]) -> bool:
    if day is None or window is None:
        return True
    return window.start_local.date() <= day < window.end_local.date()


def parse_list_html(html: str, source: str, limit: int, window: Optional[Window] = None) -> List[Dict]:
    papers: List[Dict] = []
    seen = set()
    current_date: Optional[date] = None
    item_re = re.compile(r"<h3\b[^>]*>.*?</h3>|<dt\b.*?</dt>\s*<dd\b.*?</dd>", re.I | re.S)
    for match in item_re.finditer(html):
        chunk = match.group(0)
        if re.match(r"<h3\b", chunk, re.I):
            current_date = parse_list_heading_date(chunk)
            continue
        if not date_in_window(current_date, window):
            continue
        id_match = re.search(r"""href\s*=\s*["']/abs/([^"#?']+)["']""", chunk)
        if not id_match:
            continue
        arxiv_id = unescape(id_match.group(1))
        if arxiv_id in seen:
            continue
        seen.add(arxiv_id)
        title_match = re.search(
            r"""class\s*=\s*["'][^"']*\blist-title\b[^"']*["'][^>]*>(.*?)</div>""",
            chunk,
            re.I | re.S,
        )
        authors_match = re.search(
            r"""class\s*=\s*["'][^"']*\blist-authors\b[^"']*["'][^>]*>(.*?)</div>""",
            chunk,
            re.I | re.S,
        )
        authors = []
        if authors_match:
            author_text = strip_tags(authors_match.group(1))
            author_text = re.sub(r"^Authors?:\s*", "", author_text)
            authors = [part.strip() for part in author_text.split(",") if part.strip()]
        title = arxiv_id
        if title_match:
            title = strip_tags(title_match.group(1))
            title = re.sub(r"^Title:\s*", "", title).strip()
        papers.append(
            {
                "id": arxiv_id,
                "base_id": base_arxiv_id(arxiv_id),
                "title": title,
                "summary": "",
                "authors": authors,
                "published": "",
                "updated": "",
                "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "categories": [source],
                "source_category": source,
                "source_categories": [source],
                "fetch_method": "html-fallback",
                "uncertainty": "HTML fallback 未提供精确提交时间和摘要，需要人工复核。",
            }
        )
        if len(papers) >= limit:
            break
    return papers


def fetch_source(
    source: str,
    window: Window,
    raw_dir: Path,
    max_results: int,
    no_cache: bool,
    timeout: int,
    user_agent: str,
) -> Tuple[List[Dict], Dict]:
    first_api_url = build_api_url(source, window, 0, min(API_PAGE_SIZE, max_results))
    try:
        papers: List[Dict] = []
        pages = 0
        cached_pages = 0
        start = 0
        while len(papers) < max_results:
            page_size = min(API_PAGE_SIZE, max_results - len(papers))
            api_url = build_api_url(source, window, start, page_size)
            api_cache = raw_dir / f"{cache_key([window.label, source, 'api', str(start)])}.xml"
            xml_text, cached = read_url(api_url, api_cache, no_cache, timeout, user_agent)
            page = parse_api_feed(xml_text, source)
            pages += 1
            if cached:
                cached_pages += 1
            if not page:
                break
            papers.extend(page)
            if len(papers) >= max_results:
                break
            if len(page) < page_size:
                break
            start += len(page)
            time.sleep(3)
        return papers, {
            "source": source,
            "method": "api-cache" if pages and cached_pages == pages else "api",
            "status": "ok",
            "count": len(papers),
            "pages": pages,
            "url": first_api_url,
        }
    except Exception as exc:
        html_cache = raw_dir / f"{cache_key([window.label, source, 'html-fallback'])}.html"
        html_url = LIST_URL.format(source=source, limit=max_results)
        try:
            html, cached = read_url(html_url, html_cache, no_cache, timeout, user_agent)
            papers = parse_list_html(html, source, max_results, window)
            return papers, {
                "source": source,
                "method": "html-fallback-cache" if cached else "html-fallback",
                "status": "api_failed_fallback_ok",
                "count": len(papers),
                "url": html_url,
                "api_error": str(exc),
                "note": "HTML fallback 使用 recent 列表，时间窗可能不精确。",
            }
        except Exception as fallback_exc:
            return [], {
                "source": source,
                "method": "failed",
                "status": "failed",
                "count": 0,
                "url": first_api_url,
                "api_error": str(exc),
                "fallback_error": str(fallback_exc),
            }


def dedupe_papers(papers: Sequence[Dict]) -> List[Dict]:
    by_base: Dict[str, Dict] = {}
    for paper in papers:
        base_id = paper.get("base_id") or base_arxiv_id(paper.get("id", ""))
        current = dict(paper)
        current["base_id"] = base_id
        current_sources = set(current.get("source_categories") or [])
        if current.get("source_category"):
            current_sources.add(current["source_category"])
        current["source_categories"] = sorted(current_sources)
        current["categories"] = sorted(set(current.get("categories") or []) | current_sources)
        if base_id not in by_base:
            by_base[base_id] = current
            continue
        existing = by_base[base_id]
        merged_sources = sorted(set(existing.get("source_categories", [])) | set(current["source_categories"]))
        merged_categories = sorted(set(existing.get("categories", [])) | set(current["categories"]))
        keep_current = version_number(current.get("id", "")) >= version_number(existing.get("id", ""))
        merged = dict(current if keep_current else existing)
        merged["source_categories"] = merged_sources
        merged["categories"] = merged_categories
        if existing.get("summary") and not merged.get("summary"):
            merged["summary"] = existing["summary"]
        if existing.get("authors") and not merged.get("authors"):
            merged["authors"] = existing["authors"]
        by_base[base_id] = merged
    return sorted(by_base.values(), key=lambda p: (p.get("published") or p.get("updated") or "", p.get("id", "")), reverse=True)


def contains_any(text: str, keywords: Sequence[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def keyword_score(text: str, title: str, keywords: Sequence[str]) -> int:
    score = 0
    for keyword in keywords:
        if keyword in text:
            score += 1
        if keyword in title:
            score += 2
    return score


def find_primary_contribution(text: str, title: str) -> str:
    scores = {
        contribution: keyword_score(text, title, keywords)
        for contribution, keywords in CONTRIBUTION_KEYWORDS.items()
    }
    best = max(scores.items(), key=lambda pair: (pair[1], -PRIMARY_CONTRIBUTIONS.index(pair[0])))
    return best[0] if best[1] > 0 else ""


def find_embodied_tasks(text: str, title: str) -> List[str]:
    tasks = [
        task
        for task in EMBODIED_TASKS
        if keyword_score(text, title, TASK_KEYWORDS[task]) > 0
    ]
    return tasks


def find_technique_tags(text: str) -> List[str]:
    return sorted(tag for tag, keywords in TAG_KEYWORDS if contains_any(text, keywords))


def build_contribution(paper: Dict, primary_contribution: str) -> str:
    summary = paper.get("summary", "")
    first_sentence = re.split(r"(?<=[.!?])\s+", summary, maxsplit=1)[0].strip()
    if first_sentence:
        return first_sentence[:220].rstrip()
    title = paper.get("title", "").strip()
    if primary_contribution:
        return f"围绕 {primary_contribution} 的候选论文：{title}"
    return f"候选论文：{title}"


def summary_sentence(paper: Dict, index: int, fallback: str) -> str:
    summary = paper.get("summary", "")
    sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", summary) if part.strip()]
    if index < len(sentences):
        return sentences[index][:220].rstrip()
    return fallback


def build_problem_statement(paper: Dict) -> str:
    return summary_sentence(paper, 0, f"需要判断 `{paper.get('title', 'Untitled')}` 解决的具身智能问题。")


def build_method_summary(paper: Dict) -> str:
    return summary_sentence(paper, 1, f"方法细节需要结合论文摘要或正文进一步复核。")


def is_autonomous_driving_negative(text: str) -> bool:
    if not contains_any(text, AUTONOMOUS_DRIVING_TERMS):
        return False
    allowed_terms = (
        "robot",
        "robotic",
        "embodied",
        "generalist robot",
        "robot foundation model",
        "world model",
        "world modeling",
    )
    return not contains_any(text, allowed_terms)


def build_classification_reason(
    primary_contribution: str,
    embodied_tasks: Sequence[str],
    technique_tags: Sequence[str],
    relevance: str,
) -> str:
    if relevance == "none":
        return "不属于具身智能候选。"
    parts = []
    if primary_contribution:
        parts.append(f"核心贡献轴命中 {primary_contribution}")
    if embodied_tasks:
        parts.append(f"任务轴命中 {', '.join(embodied_tasks)}")
    if technique_tags:
        parts.append(f"技术标签命中 {', '.join(technique_tags[:6])}")
    return "；".join(parts) or "规则层保留为候选，需要人工复核。"


def classify_embodied_paper(paper: Dict) -> Dict:
    title = paper.get("title", "")
    title_text = title.lower()
    text = f"{title} {paper.get('summary', '')}".lower()
    primary_contribution = find_primary_contribution(text, title_text)
    embodied_tasks = find_embodied_tasks(text, title_text)
    technique_tags = find_technique_tags(text)
    if not primary_contribution and embodied_tasks:
        primary_contribution = "Policy/Control/Planning"
    strong = contains_any(text, STRONG_EMBODIED_TERMS)
    weak = contains_any(text, WEAK_EMBODIED_TERMS)
    physical_robot_context = contains_any(text, PHYSICAL_ROBOT_CONTEXT_TERMS)
    source_categories = set(paper.get("source_categories") or [paper.get("source_category", "")])
    uncertainty = paper.get("uncertainty", "")
    source_is_only_cv = bool(source_categories) and source_categories <= {"cs.CV"}
    if contains_any(text, NON_EMBODIED_MANIPULATION_TERMS) and not physical_robot_context:
        relevance = "none"
        primary_contribution = ""
        embodied_tasks = []
        technique_tags = []
        uncertainty = uncertainty or "命中非机器人 image/text manipulation 或取证语义。"
    elif is_autonomous_driving_negative(text):
        relevance = "none"
        primary_contribution = ""
        embodied_tasks = []
        technique_tags = []
        uncertainty = uncertainty or "命中自动驾驶/交通语义，但缺少通用具身机器人或 world-model 贡献线索。"
    elif source_is_only_cv and not strong and contains_any(text, NON_EMBODIED_CV_TERMS):
        relevance = "none"
        primary_contribution = ""
        embodied_tasks = []
        technique_tags = []
        uncertainty = uncertainty or "命中医学/临床 CV 负例，且缺少 robot/action 线索。"
    elif contains_any(text, GENERIC_ROBOTICS_NEGATIVE_TERMS) and not embodied_tasks and not contains_any(
        text,
        (
            "world model",
            "diffusion policy",
            "manipulation",
            "locomotion",
            "navigation",
            "vla",
            "vision-language-action",
            "foundation model",
            "benchmark",
            "dataset",
        ),
    ):
        relevance = "none"
        primary_contribution = ""
        embodied_tasks = []
        technique_tags = []
        uncertainty = uncertainty or "命中通用形式化/控制语义，但缺少具身任务或模型贡献线索。"
    elif primary_contribution and (strong or embodied_tasks):
        relevance = "high"
    elif primary_contribution and (weak or source_categories & {"cs.RO"}):
        relevance = "medium"
        uncertainty = uncertainty or "具身相关性主要来自表示/规划/数据关键词，需要人工复核。"
    elif primary_contribution and physical_robot_context:
        relevance = "low"
        uncertainty = uncertainty or "仅命中弱机器人线索，分类为规则草稿。"
    elif primary_contribution and weak:
        relevance = "low"
        uncertainty = uncertainty or "可能服务于具身任务，但标题摘要缺少明确 robot/action 线索。"
    else:
        relevance = "none"
        uncertainty = uncertainty or "未命中具身智能筛选关键词。"
    if relevance != "none" and not embodied_tasks:
        embodied_tasks = ["General/Cross-task"]
    result = dict(paper)
    result.update(
        {
            "primary_contribution": primary_contribution,
            "embodied_tasks": embodied_tasks,
            "technique_tags": technique_tags,
            "relevance": relevance,
            "uncertainty": uncertainty,
            "one_line_contribution": build_contribution(paper, primary_contribution),
            "problem_statement": build_problem_statement(paper),
            "method_summary": build_method_summary(paper),
            "classification_reason": build_classification_reason(
                primary_contribution,
                embodied_tasks,
                technique_tags,
                relevance,
            ),
            "classifier": "rules",
        }
    )
    return result


def find_driving_stack_category(text: str, title: str) -> str:
    scores = {
        category: keyword_score(text, title, keywords)
        for category, keywords in AUTONOMOUS_DRIVING_STACK_KEYWORDS.items()
    }
    best = max(scores.items(), key=lambda pair: (pair[1], -DRIVING_STACK_CATEGORIES.index(pair[0])))
    return best[0] if best[1] > 0 else ""


def find_autonomous_driving_tags(text: str) -> List[str]:
    return sorted(tag for tag, keywords in AUTONOMOUS_DRIVING_TAG_KEYWORDS if contains_any(text, keywords))


def build_driving_classification_reason(
    driving_stack_category: str,
    technique_tags: Sequence[str],
    relevance: str,
) -> str:
    if relevance == "none":
        return "不属于自动驾驶候选。"
    parts = []
    if driving_stack_category:
        parts.append(f"Driving Stack 命中 {driving_stack_category}")
    if technique_tags:
        parts.append(f"技术标签命中 {', '.join(technique_tags[:6])}")
    return "；".join(parts) or "规则层保留为自动驾驶候选，需要人工复核。"


def classify_autonomous_driving_paper(paper: Dict) -> Dict:
    title = paper.get("title", "")
    title_text = title.lower()
    text = f"{title} {paper.get('summary', '')}".lower()
    context = contains_any(text, AUTONOMOUS_DRIVING_CONTEXT_TERMS)
    category = find_driving_stack_category(text, title_text)
    technique_tags = find_autonomous_driving_tags(text)
    uncertainty = paper.get("uncertainty", "")
    if contains_any(text, TRAFFIC_ENGINEERING_NEGATIVE_TERMS) and not (
        contains_any(text, ("autonomous driving", "autonomous vehicle", "self-driving", "ego vehicle"))
        or category in {"End-to-End Driving", "Planning/Control", "Data/Simulation"}
    ):
        relevance = "none"
        category = ""
        technique_tags = []
        uncertainty = uncertainty or "命中交通工程/交通流语义，但缺少自动驾驶栈语境。"
    elif not context:
        relevance = "none"
        category = ""
        technique_tags = []
        uncertainty = uncertainty or "未命中自动驾驶场景、数据集或系统栈线索。"
    elif category:
        relevance = "high"
    elif technique_tags:
        category = "Perception"
        relevance = "medium"
        uncertainty = uncertainty or "命中自动驾驶语境和技术标签，但主栈分类需要复核。"
    else:
        category = "Perception"
        relevance = "low"
        uncertainty = uncertainty or "仅命中自动驾驶弱语境，分类为规则草稿。"
    result = dict(paper)
    result.update(
        {
            "driving_stack_category": category,
            "technique_tags": technique_tags,
            "relevance": relevance,
            "uncertainty": uncertainty,
            "problem_statement": build_problem_statement(paper),
            "method_summary": build_method_summary(paper),
            "classification_reason": build_driving_classification_reason(
                category,
                technique_tags,
                relevance,
            ),
            "classifier": "rules",
        }
    )
    return result


def classify_paper(paper: Dict, profile: str = DEFAULT_PROFILE) -> Dict:
    profile = validate_profile(profile)
    if profile == AUTONOMOUS_DRIVING_PROFILE:
        return classify_autonomous_driving_paper(paper)
    return classify_embodied_paper(paper)


def classify_and_filter(papers: Sequence[Dict]) -> List[Dict]:
    selected, _rejected, _status = classify_and_partition(
        papers,
        classifier="rules",
        llm_cache_path=Path("/dev/null"),
    )
    return selected


def classification_cache_key(paper: Dict, profile: str = DEFAULT_PROFILE) -> str:
    payload = {
        "profile": validate_profile(profile),
        "taxonomy_version": taxonomy_version(profile),
        "id": paper.get("id", ""),
        "base_id": paper.get("base_id", ""),
        "title": paper.get("title", ""),
        "summary": paper.get("summary", ""),
    }
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def load_llm_cache(cache_path: Path, profile: str = DEFAULT_PROFILE) -> Dict[str, Dict]:
    profile = validate_profile(profile)
    if not cache_path.exists():
        return {}
    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    profiles = data.get("profiles")
    if isinstance(profiles, dict):
        profile_data = profiles.get(profile, {})
        if not isinstance(profile_data, dict):
            return {}
        if profile_data.get("taxonomy_version") != taxonomy_version(profile):
            return {}
        entries = profile_data.get("entries", {})
        return entries if isinstance(entries, dict) else {}
    if data.get("profile") != profile:
        return {}
    if data.get("taxonomy_version") != taxonomy_version(profile):
        return {}
    entries = data.get("entries", {})
    return entries if isinstance(entries, dict) else {}


def write_llm_cache(cache_path: Path, entries: Dict[str, Dict], profile: str = DEFAULT_PROFILE) -> None:
    profile = validate_profile(profile)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    profiles: Dict[str, Dict] = {}
    if cache_path.exists():
        try:
            existing = json.loads(cache_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            existing = {}
        existing_profiles = existing.get("profiles") if isinstance(existing, dict) else {}
        if isinstance(existing_profiles, dict):
            profiles = dict(existing_profiles)
        elif isinstance(existing, dict) and existing.get("profile") in PROFILES:
            profiles[existing["profile"]] = {
                "taxonomy_version": existing.get("taxonomy_version", ""),
                "entries": existing.get("entries", {}),
            }
    profiles[profile] = {
        "taxonomy_version": taxonomy_version(profile),
        "entries": entries,
    }
    payload = {"profiles": profiles}
    cache_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def classification_cache_path(out_dir: Path, classifier: str) -> Path:
    name = "traecli-classifications.json" if classifier == "traecli" else "codex-classifications.json"
    return out_dir / ".cache" / name


def normalize_list(values: object, allowed: Sequence[str]) -> List[str]:
    if not isinstance(values, list):
        return []
    normalized = []
    allowed_set = set(allowed)
    for value in values:
        if isinstance(value, str) and value in allowed_set and value not in normalized:
            normalized.append(value)
    return normalized


def normalize_tags(values: object, profile: str = DEFAULT_PROFILE) -> List[str]:
    if not isinstance(values, list):
        return []
    allowed = set(AUTONOMOUS_DRIVING_TECHNIQUE_TAGS if profile == AUTONOMOUS_DRIVING_PROFILE else TECHNIQUE_TAGS)
    normalized = []
    for value in values:
        if not isinstance(value, str):
            continue
        tag = value.strip().lower()
        if tag in allowed and tag not in normalized:
            normalized.append(tag)
    return normalized


def normalize_classification(
    paper: Dict,
    candidate: Dict,
    classifier_name: str,
    profile: str = DEFAULT_PROFILE,
) -> Dict:
    profile = validate_profile(profile)
    rule_draft = classify_paper(paper, profile=profile)
    result = dict(paper)
    relevance = candidate.get("relevance") if isinstance(candidate, dict) else ""
    if relevance not in RELEVANCE_TIERS:
        relevance = rule_draft.get("relevance", "low")
    if profile == AUTONOMOUS_DRIVING_PROFILE:
        category = candidate.get("driving_stack_category") if isinstance(candidate, dict) else ""
        if relevance == "none":
            category = ""
        elif category not in DRIVING_STACK_CATEGORIES:
            category = rule_draft.get("driving_stack_category") or "Perception"
        tags = normalize_tags(candidate.get("technique_tags"), profile=profile) if isinstance(candidate, dict) else []
        problem = candidate.get("problem_statement") if isinstance(candidate, dict) else ""
        method = candidate.get("method_summary") if isinstance(candidate, dict) else ""
        reason = candidate.get("classification_reason") if isinstance(candidate, dict) else ""
        uncertainty = candidate.get("uncertainty") if isinstance(candidate, dict) else ""
        result.update(
            {
                "driving_stack_category": category,
                "technique_tags": tags,
                "relevance": relevance,
                "problem_statement": problem or rule_draft.get("problem_statement", ""),
                "method_summary": method or rule_draft.get("method_summary", ""),
                "classification_reason": reason or rule_draft.get("classification_reason", ""),
                "uncertainty": uncertainty or rule_draft.get("uncertainty", ""),
                "classifier": classifier_name,
            }
        )
        return result
    primary = candidate.get("primary_contribution") if isinstance(candidate, dict) else ""
    if relevance == "none":
        primary = ""
    elif primary not in PRIMARY_CONTRIBUTIONS:
        primary = rule_draft.get("primary_contribution") or "Policy/Control/Planning"
    tasks = normalize_list(candidate.get("embodied_tasks"), EMBODIED_TASKS) if isinstance(candidate, dict) else []
    tags = normalize_tags(candidate.get("technique_tags"), profile=profile) if isinstance(candidate, dict) else []
    if relevance != "none" and not tasks:
        tasks = ["General/Cross-task"]
    contribution = candidate.get("one_line_contribution") if isinstance(candidate, dict) else ""
    problem = candidate.get("problem_statement") if isinstance(candidate, dict) else ""
    method = candidate.get("method_summary") if isinstance(candidate, dict) else ""
    reason = candidate.get("classification_reason") if isinstance(candidate, dict) else ""
    uncertainty = candidate.get("uncertainty") if isinstance(candidate, dict) else ""
    result.update(
        {
            "primary_contribution": primary,
            "embodied_tasks": tasks,
            "technique_tags": tags,
            "relevance": relevance,
            "one_line_contribution": contribution or rule_draft.get("one_line_contribution", ""),
            "problem_statement": problem or rule_draft.get("problem_statement", ""),
            "method_summary": method or rule_draft.get("method_summary", ""),
            "classification_reason": reason or rule_draft.get("classification_reason", ""),
            "uncertainty": uncertainty or rule_draft.get("uncertainty", ""),
            "classifier": classifier_name,
        }
    )
    return result


def codex_output_schema(profile: str = DEFAULT_PROFILE) -> Dict:
    profile = validate_profile(profile)
    if profile == AUTONOMOUS_DRIVING_PROFILE:
        return {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "papers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "id": {"type": "string"},
                            "relevance": {"type": "string", "enum": list(RELEVANCE_TIERS)},
                            "driving_stack_category": {
                                "type": "string",
                                "enum": list(DRIVING_STACK_CATEGORIES) + [""],
                            },
                            "technique_tags": {
                                "type": "array",
                                "items": {"type": "string", "enum": list(AUTONOMOUS_DRIVING_TECHNIQUE_TAGS)},
                            },
                            "problem_statement": {"type": "string"},
                            "method_summary": {"type": "string"},
                            "classification_reason": {"type": "string"},
                            "uncertainty": {"type": "string"},
                        },
                        "required": [
                            "id",
                            "relevance",
                            "driving_stack_category",
                            "technique_tags",
                            "problem_statement",
                            "method_summary",
                            "classification_reason",
                            "uncertainty",
                        ],
                    },
                }
            },
            "required": ["papers"],
        }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "papers": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "string"},
                        "relevance": {"type": "string", "enum": list(RELEVANCE_TIERS)},
                        "primary_contribution": {"type": "string", "enum": list(PRIMARY_CONTRIBUTIONS) + [""]},
                        "embodied_tasks": {
                            "type": "array",
                            "items": {"type": "string", "enum": list(EMBODIED_TASKS)},
                        },
                        "technique_tags": {
                            "type": "array",
                            "items": {"type": "string", "enum": list(TECHNIQUE_TAGS)},
                        },
                        "one_line_contribution": {"type": "string"},
                        "problem_statement": {"type": "string"},
                        "method_summary": {"type": "string"},
                        "classification_reason": {"type": "string"},
                        "uncertainty": {"type": "string"},
                    },
                    "required": [
                        "id",
                        "relevance",
                        "primary_contribution",
                        "embodied_tasks",
                        "technique_tags",
                        "one_line_contribution",
                        "problem_statement",
                        "method_summary",
                        "classification_reason",
                        "uncertainty",
                    ],
                },
            }
        },
        "required": ["papers"],
    }


def build_codex_prompt(batch: Sequence[Dict], profile: str = DEFAULT_PROFILE) -> str:
    profile = validate_profile(profile)
    compact_papers = []
    for paper in batch:
        draft = classify_paper(paper, profile=profile)
        rule_draft = {
            "relevance": draft.get("relevance"),
            "technique_tags": draft.get("technique_tags"),
            "uncertainty": draft.get("uncertainty"),
        }
        if profile == AUTONOMOUS_DRIVING_PROFILE:
            rule_draft["driving_stack_category"] = draft.get("driving_stack_category")
        else:
            rule_draft["primary_contribution"] = draft.get("primary_contribution")
            rule_draft["embodied_tasks"] = draft.get("embodied_tasks")
        compact_papers.append(
            {
                "id": paper.get("id"),
                "base_id": paper.get("base_id"),
                "title": paper.get("title"),
                "summary": truncate(paper.get("summary", ""), 1800),
                "categories": paper.get("categories", []),
                "source_categories": paper.get("source_categories", []),
                "rule_draft": rule_draft,
            }
        )
    if profile == AUTONOMOUS_DRIVING_PROFILE:
        taxonomy = {
            "driving_stack_category": list(DRIVING_STACK_CATEGORIES),
            "display_labels": DRIVING_STACK_LABELS,
            "technique_tags": list(AUTONOMOUS_DRIVING_TECHNIQUE_TAGS),
            "rules": [
                "Driving Stack 是自动驾驶报告的唯一正文目录；每篇论文只能选择一个 driving_stack_category。",
                "End-to-End Driving 覆盖端到端驾驶、VLM/LLM driving agent、foundation driving model、闭环 ego action 输出。",
                "Perception 覆盖感知、BEV、occupancy、检测、分割、跟踪、预测、mapping、localization。",
                "Planning/Control 覆盖规划、规控、MPC、trajectory optimization、control policy、安全约束控制。",
                "Data/Simulation 覆盖 dataset、benchmark、simulator、scenario generation、closed-loop benchmark、安全评测。",
                "纯交通工程、普通 CV、普通机器人且没有自动驾驶栈语境时输出 relevance=none。",
                "problem_statement、method_summary、classification_reason 必须使用中文且每个字段必须包含中文汉字，不要直接复制英文摘要。",
                "problem_statement 用中文概括论文解决的具体问题；如果摘要为英文，需要理解后改写为中文。",
                "method_summary 用中文概括论文提出的具体方法或系统做法；如果摘要为英文，需要理解后改写为中文。",
            ],
        }
        return "\n".join(
            [
                "你是自动驾驶 arXiv 日报/周报分类器。只返回符合 JSON Schema 的 JSON。",
                "根据论文标题和摘要裁决唯一 Driving Stack 分类，不要让一篇论文进入多个目录。",
                "所有自然语言字段必须使用中文且包含中文汉字，禁止输出英文整句，不要直接复制英文摘要，不要输出 Markdown 代码块。",
                "",
                "Taxonomy:",
                json.dumps(taxonomy, ensure_ascii=False, indent=2),
                "",
                "Papers:",
                json.dumps(compact_papers, ensure_ascii=False, indent=2),
            ]
        )
    taxonomy = {
        "primary_contribution": list(PRIMARY_CONTRIBUTIONS),
        "embodied_tasks": list(EMBODIED_TASKS),
        "technique_tags": list(TECHNIQUE_TAGS),
        "rules": [
            "Primary Contribution 看论文核心贡献，不看关键词先后顺序。",
            "Embodied Task 是任务/场景轴，可以多选；普通自动驾驶默认 relevance=none。",
            "如果论文属于具身智能但没有明确具体任务，embodied_tasks 必须包含 General/Cross-task。",
            "Technique Tags 是横向技术标签。",
            "不属于具身智能候选时输出 relevance=none，并说明原因。",
            "one_line_contribution、problem_statement、method_summary、classification_reason 必须使用中文且每个字段必须包含中文汉字，不要直接复制英文摘要。",
            "one_line_contribution 必须用中文，说明论文为什么值得进入报告。",
            "problem_statement 用中文概括论文解决的具体问题；如果摘要为英文，需要理解后改写为中文。",
            "method_summary 用中文概括论文提出的具体方法或系统做法；如果摘要为英文，需要理解后改写为中文。",
        ],
    }
    return "\n".join(
        [
            "你是具身智能论文日报/周报分类器。只返回符合 JSON Schema 的 JSON。",
            "根据论文标题和摘要裁决多轴分类，不要按关键词顺序抢主类。",
            "所有自然语言字段必须使用中文且包含中文汉字，禁止输出英文整句，不要直接复制英文摘要，不要输出 Markdown 代码块。",
            "",
            "Taxonomy:",
            json.dumps(taxonomy, ensure_ascii=False, indent=2),
            "",
            "Papers:",
            json.dumps(compact_papers, ensure_ascii=False, indent=2),
        ]
    )


def run_codex_batch(
    batch: Sequence[Dict],
    timeout: int,
    codex_model: Optional[str],
    profile: str = DEFAULT_PROFILE,
) -> Dict:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        schema_path = tmp_dir / "schema.json"
        output_path = tmp_dir / "last-message.json"
        schema_path.write_text(json.dumps(codex_output_schema(profile), ensure_ascii=False), encoding="utf-8")
        cmd = [
            "codex",
            "exec",
            "-c",
            'model_reasoning_effort="low"',
            "--ephemeral",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "-C",
            str(Path.cwd()),
        ]
        if codex_model:
            cmd.extend(["--model", codex_model])
        cmd.append("-")
        completed = subprocess.run(
            cmd,
            input=build_codex_prompt(batch, profile=profile),
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        if completed.returncode != 0:
            raise RuntimeError((completed.stderr or completed.stdout or "codex exec failed").strip())
        try:
            return json.loads(output_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"codex output parse failed: {exc}") from exc


def cache_fields_for_profile(profile: str = DEFAULT_PROFILE) -> Tuple[str, ...]:
    profile = validate_profile(profile)
    if profile == AUTONOMOUS_DRIVING_PROFILE:
        return (
            "id",
            "relevance",
            "driving_stack_category",
            "technique_tags",
            "problem_statement",
            "method_summary",
            "classification_reason",
            "uncertainty",
        )
    return (
        "id",
        "relevance",
        "primary_contribution",
        "embodied_tasks",
        "technique_tags",
        "one_line_contribution",
        "problem_statement",
        "method_summary",
        "classification_reason",
        "uncertainty",
    )


def parse_json_object_text(text: str) -> Dict:
    stripped = text.strip()
    fence_match = re.search(r"```(?:json)?\s*(.*?)\s*```", stripped, re.I | re.S)
    if fence_match:
        stripped = fence_match.group(1).strip()
    try:
        parsed = json.loads(stripped)
    except json.JSONDecodeError:
        decoder = json.JSONDecoder()
        for index, char in enumerate(stripped):
            if char != "{":
                continue
            try:
                parsed, _end = decoder.raw_decode(stripped[index:])
                break
            except json.JSONDecodeError:
                continue
        else:
            raise
    if not isinstance(parsed, dict):
        raise ValueError("expected JSON object")
    return parsed


def parse_traecli_json_response(stdout: str) -> Dict:
    wrapper = parse_json_object_text(stdout)
    message = wrapper.get("message")
    if not isinstance(message, dict):
        raise RuntimeError("traecli JSON missing message object")
    content = message.get("content")
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("traecli JSON missing assistant content")
    try:
        return parse_json_object_text(content)
    except (json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError(f"traecli assistant content parse failed: {exc}") from exc


def run_traecli_batch(
    batch: Sequence[Dict],
    timeout: int,
    trae_model: str,
    trae_thinking_effort: str,
    trae_verbosity: str,
    profile: str = DEFAULT_PROFILE,
) -> Dict:
    executable = shutil.which("traecli") or shutil.which("coco") or "traecli"
    cmd = [
        executable,
        "-p",
        "--json",
        "--query-timeout",
        f"{timeout}s",
        "-c",
        f"model.name={trae_model}",
        "-c",
        f"byted_gpt.thinking.thinking_effort={trae_thinking_effort}",
        "-c",
        f"byted_gpt.thinking.verbosity={trae_verbosity}",
        build_codex_prompt(batch, profile=profile),
    ]
    completed = subprocess.run(
        cmd,
        text=True,
        capture_output=True,
        timeout=timeout + 30,
    )
    if completed.returncode != 0:
        raise RuntimeError((completed.stderr or completed.stdout or "traecli failed").strip())
    return parse_traecli_json_response(completed.stdout)


def classify_with_codex(
    papers: Sequence[Dict],
    llm_cache_path: Path,
    batch_size: int,
    timeout: int,
    codex_model: Optional[str],
    use_cache: bool,
    profile: str = DEFAULT_PROFILE,
) -> Tuple[List[Dict], Dict]:
    profile = validate_profile(profile)
    cache = load_llm_cache(llm_cache_path, profile=profile) if use_cache else {}
    results: List[Dict] = []
    missing: List[Dict] = []
    cache_hits = 0
    for paper in papers:
        key = classification_cache_key(paper, profile=profile)
        if use_cache and key in cache:
            results.append(normalize_classification(paper, cache[key], "codex-cache", profile=profile))
            cache_hits += 1
        else:
            missing.append(paper)
    errors: List[str] = []
    calls = 0
    for start in range(0, len(missing), batch_size):
        batch = missing[start : start + batch_size]
        try:
            raw = run_codex_batch(batch, timeout=timeout, codex_model=codex_model, profile=profile)
            calls += 1
            by_id = {
                item.get("id"): item
                for item in raw.get("papers", [])
                if isinstance(item, dict) and item.get("id")
            }
            for paper in batch:
                candidate = by_id.get(paper.get("id"), {})
                normalized = normalize_classification(paper, candidate, "codex", profile=profile)
                results.append(normalized)
                if use_cache:
                    cache[classification_cache_key(paper, profile=profile)] = {
                        key: normalized[key]
                        for key in cache_fields_for_profile(profile)
                    }
            if use_cache:
                write_llm_cache(llm_cache_path, cache, profile=profile)
        except Exception as exc:
            errors.append(str(exc))
            for paper in batch:
                fallback = classify_paper(paper, profile=profile)
                fallback["classifier"] = "rules-fallback"
                fallback["uncertainty"] = (
                    fallback.get("uncertainty") or "LLM 分类失败，使用规则草稿兜底。"
                )
                results.append(fallback)
    if use_cache:
        write_llm_cache(llm_cache_path, cache, profile=profile)
    status_value = "ok"
    if errors and calls == 0 and missing:
        status_value = "fallback_rules"
    elif errors:
        status_value = "partial_fallback_rules"
    return results, {
        "classifier": "codex",
        "profile": profile,
        "status": status_value,
        "total": len(papers),
        "cache_hits": cache_hits,
        "codex_calls": calls,
        "errors": errors,
    }


def classify_with_traecli(
    papers: Sequence[Dict],
    llm_cache_path: Path,
    batch_size: int,
    timeout: int,
    trae_model: str,
    trae_thinking_effort: str,
    trae_verbosity: str,
    use_cache: bool,
    profile: str = DEFAULT_PROFILE,
) -> Tuple[List[Dict], Dict]:
    profile = validate_profile(profile)
    cache = load_llm_cache(llm_cache_path, profile=profile) if use_cache else {}
    results: List[Dict] = []
    missing: List[Dict] = []
    cache_hits = 0
    for paper in papers:
        key = classification_cache_key(paper, profile=profile)
        if use_cache and key in cache:
            results.append(normalize_classification(paper, cache[key], "traecli-cache", profile=profile))
            cache_hits += 1
        else:
            missing.append(paper)
    errors: List[str] = []
    calls = 0
    for start in range(0, len(missing), batch_size):
        batch = missing[start : start + batch_size]
        try:
            raw = run_traecli_batch(
                batch,
                timeout=timeout,
                trae_model=trae_model,
                trae_thinking_effort=trae_thinking_effort,
                trae_verbosity=trae_verbosity,
                profile=profile,
            )
            calls += 1
            by_id = {
                item.get("id"): item
                for item in raw.get("papers", [])
                if isinstance(item, dict) and item.get("id")
            }
            for paper in batch:
                candidate = by_id.get(paper.get("id"), {})
                normalized = normalize_classification(paper, candidate, "traecli", profile=profile)
                results.append(normalized)
                if use_cache:
                    cache[classification_cache_key(paper, profile=profile)] = {
                        key: normalized[key]
                        for key in cache_fields_for_profile(profile)
                    }
            if use_cache:
                write_llm_cache(llm_cache_path, cache, profile=profile)
        except Exception as exc:
            errors.append(str(exc))
            for paper in batch:
                fallback = classify_paper(paper, profile=profile)
                fallback["classifier"] = "rules-fallback"
                fallback["uncertainty"] = (
                    fallback.get("uncertainty") or "TraeCLI 分类失败，使用规则草稿兜底。"
                )
                results.append(fallback)
    if use_cache:
        write_llm_cache(llm_cache_path, cache, profile=profile)
    status_value = "ok"
    if errors and calls == 0 and missing:
        status_value = "fallback_rules"
    elif errors:
        status_value = "partial_fallback_rules"
    return results, {
        "classifier": "traecli",
        "profile": profile,
        "status": status_value,
        "total": len(papers),
        "cache_hits": cache_hits,
        "traecli_calls": calls,
        "trae_model": trae_model,
        "trae_thinking_effort": trae_thinking_effort,
        "trae_verbosity": trae_verbosity,
        "errors": errors,
    }


def classify_and_partition(
    papers: Sequence[Dict],
    classifier: str,
    llm_cache_path: Path,
    profile: str = DEFAULT_PROFILE,
    llm_batch_size: int = DEFAULT_LLM_BATCH_SIZE,
    classifier_timeout: int = DEFAULT_CLASSIFIER_TIMEOUT,
    codex_model: Optional[str] = None,
    trae_model: str = DEFAULT_TRAE_MODEL,
    trae_thinking_effort: str = DEFAULT_TRAE_THINKING_EFFORT,
    trae_verbosity: str = DEFAULT_TRAE_VERBOSITY,
    use_llm_cache: bool = True,
) -> Tuple[List[Dict], List[Dict], Dict]:
    profile = validate_profile(profile)
    rule_classified = [classify_paper(paper, profile=profile) for paper in papers]
    rule_selected = [paper for paper in rule_classified if paper.get("relevance") != "none"]
    rule_rejected = [paper for paper in rule_classified if paper.get("relevance") == "none"]
    if classifier == "rules":
        return rule_selected, rule_rejected, {
            "classifier": "rules",
            "profile": profile,
            "status": "ok",
            "total": len(papers),
            "selected": len(rule_selected),
            "rejected": len(rule_rejected),
        }
    if classifier == "traecli":
        trae_classified, status = classify_with_traecli(
            rule_selected,
            llm_cache_path=llm_cache_path,
            profile=profile,
            batch_size=llm_batch_size,
            timeout=classifier_timeout,
            trae_model=trae_model,
            trae_thinking_effort=trae_thinking_effort,
            trae_verbosity=trae_verbosity,
            use_cache=use_llm_cache,
        )
        selected = [paper for paper in trae_classified if paper.get("relevance") != "none"]
        rejected = rule_rejected + [paper for paper in trae_classified if paper.get("relevance") == "none"]
        status.update({"selected": len(selected), "rejected": len(rejected), "rule_rejected": len(rule_rejected)})
        return selected, rejected, status
    if classifier != "codex":
        raise ValueError(f"Unsupported classifier: {classifier}")
    codex_classified, status = classify_with_codex(
        rule_selected,
        llm_cache_path=llm_cache_path,
        profile=profile,
        batch_size=llm_batch_size,
        timeout=classifier_timeout,
        codex_model=codex_model,
        use_cache=use_llm_cache,
    )
    selected = [paper for paper in codex_classified if paper.get("relevance") != "none"]
    rejected = rule_rejected + [paper for paper in codex_classified if paper.get("relevance") == "none"]
    status.update({"selected": len(selected), "rejected": len(rejected), "rule_rejected": len(rule_rejected)})
    return selected, rejected, status


def count_by(items: Sequence[Dict], key: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for item in items:
        value = item.get(key) or "未分类"
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])))


def count_many(items: Sequence[Dict], key: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for item in items:
        values = item.get(key) or []
        if not values:
            counts["未标注"] = counts.get("未标注", 0) + 1
            continue
        for value in values:
            counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])))


def truncate(text: str, limit: int = 360) -> str:
    text = WHITESPACE_RE.sub(" ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def format_embodied_paper(paper: Dict, index: int) -> str:
    tags = ", ".join(paper.get("technique_tags", [])) or "无"
    return "\n".join(
        [
            f"{index}. **[{paper.get('title', 'Untitled')}]({paper.get('abs_url', '')})**",
            f"   - 六类分类: `{paper.get('primary_contribution') or '未分类'}`",
            f"   - 相关度: `{paper.get('relevance')}`",
            f"   - 技术标签: {tags}",
            f"   - 解决问题: {paper.get('problem_statement', '')}",
            f"   - 具体方法: {paper.get('method_summary', '')}",
            f"   - 分类理由: {paper.get('classification_reason', '')}",
        ]
    )


def format_driving_paper(paper: Dict, index: int) -> str:
    tags = ", ".join(paper.get("technique_tags", [])) or "无"
    return "\n".join(
        [
            f"{index}. **[{paper.get('title', 'Untitled')}]({paper.get('abs_url', '')})**",
            f"   - 四类分类: `{paper.get('driving_stack_category') or '未分类'}`",
            f"   - 相关度: `{paper.get('relevance')}`",
            f"   - 技术标签: {tags}",
            f"   - 解决问题: {paper.get('problem_statement', '')}",
            f"   - 具体方法: {paper.get('method_summary', '')}",
            f"   - 分类理由: {paper.get('classification_reason', '')}",
        ]
    )


def paper_tasks(paper: Dict) -> List[str]:
    tasks = [task for task in paper.get("embodied_tasks", []) if task in EMBODIED_TASKS]
    return tasks or ["General/Cross-task"]


def sort_by_relevance(papers: Sequence[Dict]) -> List[Dict]:
    order = {"high": 0, "medium": 1, "low": 2}
    return sorted(
        papers,
        key=lambda paper: (
            order.get(paper.get("relevance"), 9),
            paper.get("published") or paper.get("updated") or "",
            paper.get("id", ""),
        ),
        reverse=False,
    )


def report_title(mode: str, window: Window, profile: str = DEFAULT_PROFILE) -> str:
    profile = validate_profile(profile)
    prefix = "自动驾驶" if profile == AUTONOMOUS_DRIVING_PROFILE else "具身智能"
    if mode == "daily":
        return f"{prefix} arXiv {window.label} 日报"
    start_label = window.start_local.strftime("%m%d")
    end_label = (window.end_local - timedelta(days=1)).strftime("%m%d")
    return f"{prefix} arXiv {window.label}-{start_label}-{end_label} 周报"


def report_filename(mode: str, window: Window, profile: str = DEFAULT_PROFILE) -> str:
    return f"{report_title(mode, window, profile=profile)}.md"


def render_markdown(
    mode: str,
    window: Window,
    papers: Sequence[Dict],
    statuses: Sequence[Dict],
    classifier_status: Optional[Dict] = None,
    profile: str = DEFAULT_PROFILE,
) -> str:
    profile = validate_profile(profile)
    title = report_title(mode, window, profile=profile)
    relevance_names = {"high": "高相关", "medium": "中相关", "low": "低相关"}
    lines = [
        f"# {title}",
        "",
        f"- 报告周期: `{window.label}`",
        f"- 本地时间范围: {window.start_local.strftime('%Y-%m-%d %H:%M')} ~ {window.end_local.strftime('%Y-%m-%d %H:%M')} Asia/Shanghai",
        f"- UTC 查询范围: `{window.start_utc.strftime('%Y%m%d%H%M')}` ~ `{window.end_utc.strftime('%Y%m%d%H%M')}`",
        "",
        "## 统计概览",
        "",
        f"- 候选论文数: {len(papers)}",
    ]
    for relevance, name in relevance_names.items():
        lines.append(f"- {name}: {sum(1 for paper in papers if paper.get('relevance') == relevance)}")
    if profile == AUTONOMOUS_DRIVING_PROFILE:
        stack_counts = count_by(papers, "driving_stack_category")
        lines.append(f"- 技术栈分布: {', '.join(f'{k} {v}' for k, v in stack_counts.items()) or '无'}")
    else:
        contribution_counts = count_by(papers, "primary_contribution")
        task_counts = count_many(papers, "embodied_tasks")
        lines.append(f"- 主贡献分布: {', '.join(f'{k} {v}' for k, v in contribution_counts.items()) or '无'}")
        lines.append(f"- 任务分布: {', '.join(f'{k} {v}' for k, v in task_counts.items()) or '无'}")
    lines.append("")
    if profile == AUTONOMOUS_DRIVING_PROFILE:
        lines.extend(["## Driving Stack 索引", ""])
        for category in DRIVING_STACK_CATEGORIES:
            lines.append(f"### {DRIVING_STACK_LABELS[category]}")
            group = [paper for paper in papers if paper.get("driving_stack_category") == category]
            if not group:
                lines.extend(["暂无", ""])
                continue
            for idx, paper in enumerate(sort_by_relevance(group), 1):
                lines.extend([format_driving_paper(paper, idx), ""])
            lines.append("")
    else:
        lines.extend(["## Embodied Task 索引", ""])
        for task in EMBODIED_TASKS:
            group = [paper for paper in papers if task in paper_tasks(paper)]
            if not group:
                continue
            lines.append(f"### {task}")
            for idx, paper in enumerate(sort_by_relevance(group), 1):
                lines.extend([format_embodied_paper(paper, idx), ""])
            lines.append("")
    lines.extend(["## 抓取状态", ""])
    if classifier_status:
        lines.append(
            f"- `classifier`: {classifier_status.get('status')} / {classifier_status.get('classifier')} / "
            f"selected {classifier_status.get('selected', len(papers))} / rejected {classifier_status.get('rejected', 0)}"
        )
        if classifier_status.get("errors"):
            lines.append(f"  - 说明: LLM 分类失败或部分失败，已使用规则草稿兜底。")
            for error in classifier_status.get("errors", [])[:3]:
                lines.append(f"  - 错误: {truncate(str(error), 220)}")
    for status in statuses:
        lines.append(
            f"- `{status.get('source')}`: {status.get('status')} / {status.get('method')} / {status.get('count')} 篇"
        )
        if status.get("note"):
            lines.append(f"  - 说明: {status['note']}")
        if status.get("api_error"):
            lines.append(f"  - API 错误: {status['api_error']}")
        if status.get("fallback_error"):
            lines.append(f"  - fallback 错误: {status['fallback_error']}")
    lines.append("")
    return "\n".join(lines)


def parse_sources(value: str) -> List[str]:
    sources = [source.strip() for source in value.split(",") if source.strip()]
    if not sources:
        raise ValueError("--sources must contain at least one arXiv category")
    return sources


def output_paths(
    out_dir: Path,
    mode: str,
    window: Window,
    profile: str = DEFAULT_PROFILE,
) -> Tuple[Path, Path, Path]:
    mode_dir = out_dir / validate_profile(profile) / mode
    report_path = mode_dir / report_filename(mode, window, profile=profile)
    bundle_dir = mode_dir / window.label
    raw_dir = bundle_dir / "raw"
    return report_path, bundle_dir / "papers.json", raw_dir


def markdown_h1_title(markdown_path: Path) -> Optional[str]:
    try:
        with markdown_path.open("r", encoding="utf-8") as handle:
            first_line = handle.readline().strip()
    except OSError:
        return None
    if not first_line.startswith("# "):
        return None
    title = first_line[2:].strip()
    return title or None


def rename_existing_markdown_reports(out_dir: Path) -> List[Tuple[Path, Path]]:
    renamed: List[Tuple[Path, Path]] = []
    for profile in PROFILES:
        for mode in ("daily", "weekly"):
            mode_dir = out_dir / profile / mode
            if not mode_dir.exists():
                continue
            for markdown_path in sorted(mode_dir.glob("*.md")):
                title = markdown_h1_title(markdown_path)
                if not title:
                    continue
                target_path = markdown_path.with_name(f"{title}.md")
                if target_path == markdown_path:
                    continue
                if target_path.exists():
                    old_content = markdown_path.read_text(encoding="utf-8")
                    target_content = target_path.read_text(encoding="utf-8")
                    if old_content != target_content:
                        raise ValueError(f"refuse to overwrite different report: {target_path}")
                    markdown_path.unlink()
                else:
                    markdown_path.rename(target_path)
                renamed.append((markdown_path, target_path))
    return renamed


def copy_legacy_embodied_reports(out_dir: Path) -> None:
    """Copy old reports/daily and reports/weekly outputs into the embodied profile tree."""
    for mode in ("daily", "weekly"):
        legacy_mode_dir = out_dir / mode
        if not legacy_mode_dir.exists():
            continue
        target_mode_dir = out_dir / EMBODIED_PROFILE / mode
        target_mode_dir.mkdir(parents=True, exist_ok=True)
        for markdown_path in legacy_mode_dir.glob("*.md"):
            title = markdown_h1_title(markdown_path)
            target_name = f"{title}.md" if title else markdown_path.name
            target_path = target_mode_dir / target_name
            if not target_path.exists():
                shutil.copy2(markdown_path, target_path)
        for bundle_dir in [path for path in legacy_mode_dir.iterdir() if path.is_dir()]:
            shutil.copytree(bundle_dir, target_mode_dir / bundle_dir.name, dirs_exist_ok=True)


def collect(args: argparse.Namespace) -> Dict:
    profile = validate_profile(args.profile)
    window = resolve_window(args.mode, args.date, args.week)
    out_dir = Path(args.out)
    if profile == EMBODIED_PROFILE:
        copy_legacy_embodied_reports(out_dir)
    rename_existing_markdown_reports(out_dir)
    report_path, json_path, raw_dir = output_paths(out_dir, args.mode, window, profile=profile)
    papers: List[Dict] = []
    statuses: List[Dict] = []
    sources = parse_sources(args.sources)
    for index, source in enumerate(sources):
        source_papers, status = fetch_source(
            source=source,
            window=window,
            raw_dir=raw_dir,
            max_results=args.max_results,
            no_cache=args.no_cache,
            timeout=args.timeout,
            user_agent=args.user_agent,
        )
        papers.extend(source_papers)
        statuses.append(status)
        if index < len(sources) - 1 and status.get("method") == "api":
            time.sleep(3)
    deduped = dedupe_papers(papers)
    selected, rejected, classifier_status = classify_and_partition(
        deduped,
        classifier=args.classifier,
        llm_cache_path=classification_cache_path(out_dir, args.classifier),
        profile=profile,
        llm_batch_size=args.llm_batch_size,
        classifier_timeout=args.classifier_timeout,
        codex_model=args.codex_model,
        trae_model=args.trae_model,
        trae_thinking_effort=args.trae_thinking_effort,
        trae_verbosity=args.trae_verbosity,
        use_llm_cache=not args.no_llm_cache,
    )
    markdown = render_markdown(
        args.mode,
        window,
        selected,
        statuses,
        classifier_status=classifier_status,
        profile=profile,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(markdown, encoding="utf-8")
    payload = {
        "profile": profile,
        "mode": args.mode,
        "window": {
            "label": window.label,
            "start_local": window.start_local.isoformat(),
            "end_local": window.end_local.isoformat(),
            "start_utc": window.start_utc.isoformat(),
            "end_utc": window.end_utc.isoformat(),
        },
        "sources": sources,
        "statuses": statuses,
        "total_fetched": len(deduped),
        "total_selected": len(selected),
        "total_rejected": len(rejected),
        "classifier_status": classifier_status,
        "papers": selected,
        "rejected_papers": rejected,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"report_path": str(report_path), "json_path": str(json_path), "raw_dir": str(raw_dir)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect AI arXiv digests from cs.RO/cs.CV with profile-specific classifiers."
    )
    subparsers = parser.add_subparsers(dest="mode", required=True)
    for mode in ("daily", "weekly"):
        sub = subparsers.add_parser(mode, help=f"Generate {mode} report")
        sub.add_argument("--out", default="./reports", help="Output directory")
        sub.add_argument("--date", help="Daily date in YYYY-MM-DD; defaults to yesterday")
        sub.add_argument("--week", help="Weekly ISO week in YYYY-Www; defaults to previous full week")
        sub.add_argument("--profile", choices=PROFILES, default=DEFAULT_PROFILE, help="Report profile")
        sub.add_argument("--sources", default=",".join(DEFAULT_SOURCES), help="Comma-separated arXiv categories")
        default_max = DEFAULT_DAILY_MAX_RESULTS if mode == "daily" else DEFAULT_WEEKLY_MAX_RESULTS
        sub.add_argument("--max-results", type=int, default=default_max, help="Maximum results per source")
        sub.add_argument("--no-cache", action="store_true", help="Ignore cached raw responses")
        sub.add_argument("--classifier", choices=("codex", "traecli", "rules"), default="codex", help="Paper classifier backend")
        sub.add_argument("--codex-model", help="Optional model name for codex exec")
        sub.add_argument("--trae-model", default=DEFAULT_TRAE_MODEL, help="TraeCLI model name")
        sub.add_argument(
            "--trae-thinking-effort",
            choices=("low", "medium", "high"),
            default=DEFAULT_TRAE_THINKING_EFFORT,
            help="TraeCLI byted_gpt thinking effort",
        )
        sub.add_argument(
            "--trae-verbosity",
            choices=("low", "medium", "high"),
            default=DEFAULT_TRAE_VERBOSITY,
            help="TraeCLI byted_gpt verbosity",
        )
        sub.add_argument("--llm-batch-size", type=int, default=DEFAULT_LLM_BATCH_SIZE, help="Papers per LLM classification batch")
        sub.add_argument("--classifier-timeout", type=int, default=DEFAULT_CLASSIFIER_TIMEOUT, help="LLM classifier timeout in seconds")
        sub.add_argument("--no-llm-cache", action="store_true", help="Ignore cached LLM classification results")
        sub.add_argument("--timeout", type=int, default=20, help="HTTP timeout in seconds")
        sub.add_argument("--user-agent", default=DEFAULT_USER_AGENT, help="HTTP User-Agent")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = collect(args)
    except Exception as exc:
        print(f"collect_arxiv.py: error: {exc}", file=sys.stderr)
        return 1
    print(f"Report: {result['report_path']}")
    print(f"JSON: {result['json_path']}")
    print(f"Raw: {result['raw_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
