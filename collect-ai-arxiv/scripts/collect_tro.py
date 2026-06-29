#!/usr/bin/env python3
"""Collect and classify IEEE Transactions on Robotics papers from OpenAlex."""

import argparse
import importlib.util
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


OPENALEX_WORKS_URL = "https://api.openalex.org/works"
OPENALEX_SOURCE_URL = "https://openalex.org/S4210186415"
TRO_ISSN = "1552-3098"
VENUE_NAME = "IEEE Transactions on Robotics"
DEFAULT_YEARS = (2025, 2026)
DEFAULT_USER_AGENT = "paper-collector-tro/0.1 (mailto:paper_collector@example.com)"
DEFAULT_PER_PAGE = 200
EXCLUDED_TITLE_PREFIXES = (
    "correction",
    "corrections",
    "correction to",
    "corrections to",
    "guest editorial",
    "editorial",
)


def load_collect_arxiv_module():
    script_path = Path(__file__).with_name("collect_arxiv.py")
    spec = importlib.util.spec_from_file_location("collect_arxiv", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load collect_arxiv.py from {script_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def abstract_from_inverted_index(inverted_index: object) -> str:
    if not isinstance(inverted_index, dict):
        return ""
    positioned_words: List[Tuple[int, str]] = []
    for word, positions in inverted_index.items():
        if not isinstance(word, str) or not isinstance(positions, list):
            continue
        for position in positions:
            if isinstance(position, int):
                positioned_words.append((position, word))
    return " ".join(word for _position, word in sorted(positioned_words)).strip()


def normalize_doi(value: object) -> str:
    if not isinstance(value, str):
        return ""
    doi = value.strip()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi.lower()


def doi_url(doi: str) -> str:
    return f"https://doi.org/{doi}" if doi else ""


def clean_title(title: object) -> str:
    if not isinstance(title, str):
        return ""
    return re.sub(r"\s+", " ", title).strip()


def is_research_article(work: Dict) -> bool:
    title = clean_title(work.get("title"))
    lowered = title.lower()
    compact = re.sub(r"\s+", "", lowered)
    if not title:
        return False
    if any(lowered.startswith(prefix) for prefix in EXCLUDED_TITLE_PREFIXES):
        return False
    return not compact.startswith("guesteditorial")


def page_range(work: Dict) -> str:
    biblio = work.get("biblio")
    if not isinstance(biblio, dict):
        return ""
    first = biblio.get("first_page") or ""
    last = biblio.get("last_page") or ""
    if first and last:
        return f"{first}-{last}"
    return str(first or last)


def author_names(work: Dict) -> List[str]:
    names: List[str] = []
    for authorship in work.get("authorships") or []:
        if not isinstance(authorship, dict):
            continue
        author = authorship.get("author")
        if not isinstance(author, dict):
            continue
        name = author.get("display_name")
        if isinstance(name, str) and name.strip():
            names.append(name.strip())
    return names


def normalize_openalex_work(work: Dict, source_label: str) -> Dict:
    doi = normalize_doi(work.get("doi"))
    openalex_id = work.get("id") if isinstance(work.get("id"), str) else ""
    paper_id = doi or openalex_id.rsplit("/", 1)[-1].lower()
    location = work.get("primary_location")
    if not isinstance(location, dict):
        location = {}
    landing_page = location.get("landing_page_url") if isinstance(location.get("landing_page_url"), str) else ""
    pdf_url = location.get("pdf_url") if isinstance(location.get("pdf_url"), str) else ""
    published = work.get("publication_date") if isinstance(work.get("publication_date"), str) else ""
    updated = work.get("updated_date") if isinstance(work.get("updated_date"), str) else ""
    if "T" in updated:
        updated = updated.split("T", 1)[0]
    abs_url = doi_url(doi) or landing_page or openalex_id
    return {
        "id": paper_id,
        "base_id": paper_id,
        "title": clean_title(work.get("title")),
        "summary": abstract_from_inverted_index(work.get("abstract_inverted_index")),
        "authors": author_names(work),
        "published": published,
        "updated": updated or published,
        "abs_url": abs_url,
        "pdf_url": pdf_url or abs_url,
        "categories": [source_label, VENUE_NAME],
        "source_category": source_label,
        "source_categories": [source_label],
        "fetch_method": "openalex",
        "venue": VENUE_NAME,
        "conference": f"TRO {source_label.removeprefix('TRO')}",
        "track": "journal",
        "publication_year": work.get("publication_year"),
        "doi": doi,
        "openalex_id": openalex_id,
        "page": page_range(work),
    }


def cache_key(parts: Iterable[object]) -> str:
    raw = "__".join(str(part) for part in parts)
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", raw).strip("_")


def build_openalex_url(year: int, cursor: str) -> str:
    params = urllib.parse.urlencode(
        {
            "filter": (
                f"primary_location.source.issn:{TRO_ISSN},"
                f"from_publication_date:{year}-01-01,"
                f"to_publication_date:{year}-12-31,"
                "type:article"
            ),
            "per-page": str(DEFAULT_PER_PAGE),
            "cursor": cursor,
            "sort": "publication_date:asc",
            "mailto": "paper_collector@example.com",
        }
    )
    return f"{OPENALEX_WORKS_URL}?{params}"


def read_url_json(url: str, cache_path: Path, no_cache: bool, timeout: int, user_agent: str) -> Tuple[Dict, bool]:
    if cache_path.exists() and not no_cache:
        return json.loads(cache_path.read_text(encoding="utf-8")), True
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    cache_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload, False


def fetch_openalex_year(
    year: int,
    raw_dir: Path,
    no_cache: bool,
    timeout: int,
    user_agent: str,
) -> Tuple[List[Dict], Dict]:
    papers: List[Dict] = []
    raw_count = 0
    cached_pages = 0
    pages = 0
    cursor = "*"
    first_url = build_openalex_url(year, cursor)
    while cursor:
        url = build_openalex_url(year, cursor)
        cache_path = raw_dir / f"{cache_key(['openalex', year, pages])}.json"
        payload, cached = read_url_json(url, cache_path, no_cache, timeout, user_agent)
        pages += 1
        if cached:
            cached_pages += 1
        results = payload.get("results")
        if not isinstance(results, list) or not results:
            break
        raw_count += len(results)
        source_label = f"TRO{year}"
        for work in results:
            if isinstance(work, dict) and is_research_article(work):
                papers.append(normalize_openalex_work(work, source_label))
        next_cursor = payload.get("meta", {}).get("next_cursor")
        if not isinstance(next_cursor, str) or next_cursor == cursor:
            break
        cursor = next_cursor
        if not cached:
            time.sleep(0.2)
    return papers, {
        "source": f"TRO{year}",
        "method": "openalex-cache" if pages and cached_pages == pages else "openalex",
        "status": "ok",
        "count": len(papers),
        "raw_count": raw_count,
        "excluded": raw_count - len(papers),
        "pages": pages,
        "url": first_url,
    }


def parse_years(value: str) -> List[int]:
    years = [int(part.strip()) for part in value.split(",") if part.strip()]
    if not years:
        raise ValueError("--years must contain at least one year")
    return sorted(dict.fromkeys(years))


def venue_slug(years: Sequence[int]) -> str:
    if len(years) == 1:
        return f"tro{years[0]}"
    return f"tro{years[0]}-{years[-1]}"


def venue_display(years: Sequence[int]) -> str:
    if len(years) == 1:
        return f"TRO {years[0]}"
    return f"TRO {years[0]}-{years[-1]}"


def all_papers_filename(years: Sequence[int]) -> str:
    if len(years) == 1:
        return f"TRO{years[0]}_all_papers.json"
    return f"TRO{years[0]}_{years[-1]}_all_papers.json"


def profile_title(profile: str, years: Sequence[int]) -> str:
    prefix = "自动驾驶" if profile == "autonomous-driving" else "具身智能"
    return f"{prefix} {venue_display(years)} 全量论文分类报告"


def report_paths(out_dir: Path, profile: str, years: Sequence[int]) -> Tuple[Path, Path]:
    base_dir = out_dir / profile / venue_slug(years)
    title = profile_title(profile, years)
    return base_dir / f"{title}.md", base_dir / "papers.json"


def format_counts(counts: Dict[str, int]) -> str:
    return ", ".join(f"{key} {value}" for key, value in counts.items()) or "无"


def render_venue_markdown(
    collect_mod,
    profile: str,
    years: Sequence[int],
    selected: Sequence[Dict],
    rejected: Sequence[Dict],
    total_count: int,
    statuses: Sequence[Dict],
    classifier_status: Dict,
) -> str:
    title = profile_title(profile, years)
    lines = [
        f"# {title}",
        "",
        f"- 来源: [OpenAlex: {VENUE_NAME}]({OPENALEX_SOURCE_URL}) / ISSN `{TRO_ISSN}`",
        f"- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- 年份范围: {', '.join(str(year) for year in years)}",
        f"- 全量论文数: {total_count}",
        f"- 二次分类输入: {classifier_status.get('total', len(selected))}",
        f"- 候选论文数: {len(selected)}",
        f"- 拒绝论文数: {len(rejected)}",
        f"- 高相关: {sum(1 for paper in selected if paper.get('relevance') == 'high')}",
        f"- 中相关: {sum(1 for paper in selected if paper.get('relevance') == 'medium')}",
        f"- 低相关: {sum(1 for paper in selected if paper.get('relevance') == 'low')}",
    ]
    if profile == "autonomous-driving":
        stack_counts = collect_mod.count_by(selected, "driving_stack_category")
        lines.append(f"- 技术栈分布: {format_counts(stack_counts)}")
    else:
        contribution_counts = collect_mod.count_by(selected, "primary_contribution")
        task_counts = collect_mod.count_many(selected, "embodied_tasks")
        lines.append(f"- 主贡献分布: {format_counts(contribution_counts)}")
        lines.append(f"- 任务分布: {format_counts(task_counts)}")
    lines.append("")
    if profile == "autonomous-driving":
        lines.extend(["## Driving Stack 索引", ""])
        for category in collect_mod.DRIVING_STACK_CATEGORIES:
            lines.append(f"### {collect_mod.DRIVING_STACK_LABELS[category]}")
            group = [paper for paper in selected if paper.get("driving_stack_category") == category]
            if not group:
                lines.extend(["暂无", ""])
                continue
            for index, paper in enumerate(collect_mod.sort_by_relevance(group), 1):
                lines.extend([collect_mod.format_driving_paper(paper, index), ""])
            lines.append("")
    else:
        lines.extend(["## Embodied Task 索引", ""])
        for task in collect_mod.EMBODIED_TASKS:
            group = [paper for paper in selected if task in collect_mod.paper_tasks(paper)]
            if not group:
                continue
            lines.append(f"### {task}")
            for index, paper in enumerate(collect_mod.sort_by_relevance(group), 1):
                lines.extend([collect_mod.format_embodied_paper(paper, index), ""])
            lines.append("")
    lines.extend(["## 抓取状态", ""])
    lines.append(
        f"- `classifier`: {classifier_status.get('status')} / {classifier_status.get('classifier')} / "
        f"selected {classifier_status.get('selected', len(selected))} / rejected {classifier_status.get('rejected', len(rejected))}"
    )
    if classifier_status.get("errors"):
        lines.append("  - 说明: LLM 分类失败或部分失败，已使用规则草稿兜底。")
        for error in classifier_status.get("errors", [])[:3]:
            lines.append(f"  - 错误: {collect_mod.truncate(str(error), 220)}")
    for status in statuses:
        lines.append(
            f"- `{status.get('source')}`: {status.get('status')} / {status.get('method')} / "
            f"{status.get('count')} 篇"
        )
        lines.append(f"  - OpenAlex 原始记录: {status.get('raw_count')}；剔除非论文记录: {status.get('excluded')}")
    lines.append("")
    return "\n".join(lines)


def classification_cache_path(out_dir: Path, classifier: str, years: Sequence[int]) -> Path:
    if classifier == "rules":
        return out_dir / ".cache" / f"{venue_slug(years)}-rules-classifications.json"
    return out_dir / ".cache" / f"{venue_slug(years)}-{classifier}-classifications.json"


def ensure_traecli_path() -> None:
    fixed = Path("/Users/bytedance/.local/bin/traecli")
    if fixed.exists() and os.access(fixed, os.X_OK):
        os.environ["PATH"] = f"{fixed.parent}{os.pathsep}{os.environ.get('PATH', '')}"


def collect(args: argparse.Namespace) -> Dict:
    years = parse_years(args.years)
    profiles = [part.strip() for part in args.profiles.split(",") if part.strip()]
    collect_mod = load_collect_arxiv_module()
    for profile in profiles:
        collect_mod.validate_profile(profile)
    if args.classifier == "traecli":
        ensure_traecli_path()
    out_dir = Path(args.out)
    dataset_dir = out_dir / venue_slug(years)
    raw_dir = dataset_dir / "raw"
    all_papers: List[Dict] = []
    statuses: List[Dict] = []
    for year in years:
        year_papers, status = fetch_openalex_year(
            year=year,
            raw_dir=raw_dir,
            no_cache=args.no_cache,
            timeout=args.timeout,
            user_agent=args.user_agent,
        )
        all_papers.extend(year_papers)
        statuses.append(status)
    deduped = collect_mod.dedupe_papers(all_papers)
    all_json_path = dataset_dir / all_papers_filename(years)
    all_json_path.parent.mkdir(parents=True, exist_ok=True)
    all_json_path.write_text(json.dumps(deduped, ensure_ascii=False, indent=2), encoding="utf-8")
    outputs = {"all_papers_json": str(all_json_path), "reports": []}
    for profile in profiles:
        selected, rejected, classifier_status = collect_mod.classify_and_partition(
            deduped,
            classifier=args.classifier,
            llm_cache_path=classification_cache_path(out_dir, args.classifier, years),
            profile=profile,
            llm_batch_size=args.llm_batch_size,
            classifier_timeout=args.classifier_timeout,
            codex_model=args.codex_model,
            trae_model=args.trae_model,
            trae_thinking_effort=args.trae_thinking_effort,
            trae_verbosity=args.trae_verbosity,
            use_llm_cache=not args.no_llm_cache,
        )
        markdown = render_venue_markdown(
            collect_mod=collect_mod,
            profile=profile,
            years=years,
            selected=selected,
            rejected=rejected,
            total_count=len(deduped),
            statuses=statuses,
            classifier_status=classifier_status,
        )
        report_path, papers_json_path = report_paths(out_dir, profile, years)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        papers_json_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(markdown, encoding="utf-8")
        payload = {
            "profile": profile,
            "source": venue_display(years),
            "source_url": OPENALEX_SOURCE_URL,
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "years": years,
            "total_fetched": len(deduped),
            "candidate_input": classifier_status.get("total", len(selected)),
            "total_selected": len(selected),
            "total_rejected": len(rejected),
            "statuses": statuses,
            "classifier_status": classifier_status,
            "papers": selected,
            "rejected_papers": rejected,
        }
        papers_json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs["reports"].append({"profile": profile, "report_path": str(report_path), "json_path": str(papers_json_path)})
    return outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Collect and classify IEEE TRO papers from OpenAlex.")
    parser.add_argument("--years", default=",".join(str(year) for year in DEFAULT_YEARS), help="Comma-separated years")
    parser.add_argument("--profiles", default="embodied,autonomous-driving", help="Comma-separated report profiles")
    parser.add_argument("--out", default="./reports", help="Output directory")
    parser.add_argument("--no-cache", action="store_true", help="Ignore cached OpenAlex responses")
    parser.add_argument("--classifier", choices=("codex", "traecli", "rules"), default="traecli", help="Paper classifier backend")
    parser.add_argument("--codex-model", help="Optional model name for codex exec")
    parser.add_argument("--trae-model", default=collect_default("DEFAULT_TRAE_MODEL", "GPT-5.5"), help="TraeCLI model name")
    parser.add_argument("--trae-thinking-effort", choices=("low", "medium", "high"), default="high", help="TraeCLI thinking effort")
    parser.add_argument("--trae-verbosity", choices=("low", "medium", "high"), default="high", help="TraeCLI verbosity")
    parser.add_argument("--llm-batch-size", type=int, default=60, help="Papers per LLM classification batch")
    parser.add_argument("--classifier-timeout", type=int, default=600, help="LLM classifier timeout in seconds")
    parser.add_argument("--no-llm-cache", action="store_true", help="Ignore cached LLM classification results")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout in seconds")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT, help="HTTP User-Agent")
    return parser


def collect_default(_name: str, fallback: str) -> str:
    return fallback


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = collect(args)
    except Exception as exc:
        print(f"collect_tro.py: error: {exc}", file=sys.stderr)
        return 1
    print(f"All papers JSON: {result['all_papers_json']}")
    for report in result["reports"]:
        print(f"Report ({report['profile']}): {report['report_path']}")
        print(f"JSON ({report['profile']}): {report['json_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
