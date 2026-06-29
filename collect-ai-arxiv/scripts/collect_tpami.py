#!/usr/bin/env python3
"""Collect and classify TPAMI official-issue papers from IEEE CSDL."""

import argparse
import importlib.util
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime
from html import unescape
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


CSDL_GRAPHQL_URL = "https://www.computer.org/csdl/api/v1/graphql"
CSDL_SOURCE_URL = "https://www.computer.org/csdl/journal/tp"
VENUE_NAME = "IEEE Transactions on Pattern Analysis and Machine Intelligence"
DEFAULT_YEARS = (2025, 2026)
DEFAULT_USER_AGENT = "paper-collector-tpami/0.1"
DEFAULT_TRAE_MODEL = "GPT-5.5"
DEFAULT_TRAE_THINKING_EFFORT = "high"
DEFAULT_TRAE_VERBOSITY = "high"
TAG_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"\s+")
EXCLUDED_TITLE_PREFIXES = (
    "correction",
    "corrections",
    "correction to",
    "corrections to",
    "editorial",
    "guest editorial",
)

ISSUE_ARTICLES_QUERY = """
query ($idPrefix: String!, $year: String!, $issueNum: String!) {
  issue: periodicalIssue(idPrefix: $idPrefix, year: $year, issueNum: $issueNum) {
    id
    title
    year
    issueNum
    idPrefix
    pubType
    volume
    label
  }
  articles: articles(idPrefix: $idPrefix, year: $year, issueNum: $issueNum) {
    id
    doi
    title
    abstract
    normalizedAbstract
    fno
    authors {
      fullName
      givenName
      surname
      affiliation
    }
    idPrefix
    isOpenAccess
    hasPdf
    pubDate
    pubType
    pages
    year
    issn
    isbn
    volume
    issueNum
  }
}
"""


def load_collect_arxiv_module():
    script_path = Path(__file__).with_name("collect_arxiv.py")
    spec = importlib.util.spec_from_file_location("collect_arxiv", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load collect_arxiv.py from {script_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def clean_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    text = TAG_RE.sub(" ", unescape(value))
    return WHITESPACE_RE.sub(" ", text).strip()


def clean_title(value: object) -> str:
    return clean_text(value)


def normalize_doi(value: object) -> str:
    if not isinstance(value, str):
        return ""
    doi = value.strip()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi.lower()


def doi_url(doi: str) -> str:
    return f"https://doi.org/{doi}" if doi else ""


def cache_key(parts: Iterable[object]) -> str:
    raw = "__".join(str(part) for part in parts)
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", raw).strip("_")


def issue_numbers_for_year(year: int, current_year: Optional[int] = None, current_month: Optional[int] = None) -> List[str]:
    today = date.today()
    current_year = current_year if current_year is not None else today.year
    current_month = current_month if current_month is not None else today.month
    if year < current_year:
        max_month = 12
    elif year == current_year:
        max_month = max(0, min(12, current_month))
    else:
        max_month = 0
    return [f"{month:02d}" for month in range(1, max_month + 1)]


def parse_years(value: str) -> List[int]:
    years = [int(part.strip()) for part in value.split(",") if part.strip()]
    if not years:
        raise ValueError("--years must contain at least one year")
    return sorted(dict.fromkeys(years))


def venue_slug(years: Sequence[int]) -> str:
    if len(years) == 1:
        return f"tpami{years[0]}"
    return f"tpami{years[0]}-{years[-1]}"


def venue_display(years: Sequence[int]) -> str:
    if len(years) == 1:
        return f"TPAMI {years[0]}"
    return f"TPAMI {years[0]}-{years[-1]}"


def all_papers_filename(years: Sequence[int]) -> str:
    if len(years) == 1:
        return f"TPAMI{years[0]}_all_papers.json"
    return f"TPAMI{years[0]}_{years[-1]}_all_papers.json"


def profile_title(profile: str, years: Sequence[int]) -> str:
    prefix = "自动驾驶" if profile == "autonomous-driving" else "具身智能"
    return f"{prefix} {venue_display(years)} 全量论文分类报告"


def report_paths(out_dir: Path, profile: str, years: Sequence[int]) -> Tuple[Path, Path]:
    base_dir = out_dir / profile / venue_slug(years)
    title = profile_title(profile, years)
    return base_dir / f"{title}.md", base_dir / "papers.json"


def article_url(article: Dict, issue: Dict) -> str:
    year = str(article.get("year") or issue.get("year") or "").strip()
    issue_num = str(article.get("issueNum") or issue.get("issueNum") or "").strip()
    fno = str(article.get("fno") or "").strip()
    article_id = str(article.get("id") or "").strip()
    if year and issue_num and fno and article_id:
        return f"{CSDL_SOURCE_URL}/{year}/{issue_num}/{fno}/{article_id}"
    doi = normalize_doi(article.get("doi"))
    return doi_url(doi)


def author_names(article: Dict) -> List[str]:
    names: List[str] = []
    for author in article.get("authors") or []:
        if not isinstance(author, dict):
            continue
        full_name = clean_text(author.get("fullName"))
        if full_name:
            names.append(full_name)
            continue
        given = clean_text(author.get("givenName"))
        surname = clean_text(author.get("surname"))
        joined = " ".join(part for part in (given, surname) if part)
        if joined:
            names.append(joined)
    return names


def is_research_article(article: Dict) -> bool:
    title = clean_title(article.get("title"))
    lowered = title.lower()
    compact = re.sub(r"\s+", "", lowered)
    if not title:
        return False
    if any(lowered.startswith(prefix) for prefix in EXCLUDED_TITLE_PREFIXES):
        return False
    return not compact.startswith("guesteditorial")


def normalize_csdl_article(article: Dict, issue: Dict) -> Dict:
    doi = normalize_doi(article.get("doi"))
    article_id = str(article.get("id") or "").strip()
    paper_id = doi or article_id
    year = str(article.get("year") or issue.get("year") or "").strip()
    issue_num = str(article.get("issueNum") or issue.get("issueNum") or "").strip()
    source_label = f"TPAMI{year}" if year else "TPAMI"
    source_issue_label = f"{source_label}-{issue_num}" if issue_num else source_label
    published = str(article.get("pubDate") or "").strip()
    summary = clean_text(article.get("abstract") or article.get("normalizedAbstract"))
    abs_url = article_url(article, issue)
    return {
        "id": paper_id,
        "base_id": paper_id,
        "title": clean_title(article.get("title")),
        "summary": summary,
        "authors": author_names(article),
        "published": published,
        "updated": published,
        "abs_url": abs_url,
        "pdf_url": doi_url(doi) or abs_url,
        "categories": [source_label, source_issue_label, VENUE_NAME],
        "source_category": source_label,
        "source_categories": [source_label, source_issue_label],
        "fetch_method": "csdl-graphql",
        "venue": VENUE_NAME,
        "conference": f"TPAMI {year}" if year else "TPAMI",
        "track": "journal",
        "publication_year": int(year) if year.isdigit() else year,
        "doi": doi,
        "csdl_id": article_id,
        "fno": str(article.get("fno") or "").strip(),
        "page": clean_text(article.get("pages")),
        "issue": f"{year}-{issue_num}" if year and issue_num else issue_num,
        "issue_label": clean_text(issue.get("label")),
        "volume": clean_text(article.get("volume") or issue.get("volume")),
    }


def graphql_request(
    query: str,
    variables: Dict,
    cache_path: Path,
    no_cache: bool,
    timeout: int,
    user_agent: str,
) -> Tuple[Dict, bool]:
    if cache_path.exists() and not no_cache:
        return json.loads(cache_path.read_text(encoding="utf-8")), True
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    request = urllib.request.Request(
        CSDL_GRAPHQL_URL,
        data=payload,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": user_agent,
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "ignore")
        raise RuntimeError(f"CSDL GraphQL HTTP {exc.code}: {detail[:500]}") from exc
    if data.get("errors"):
        raise RuntimeError(f"CSDL GraphQL errors: {data['errors']}")
    cache_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return data, False


def fetch_issue(
    year: int,
    issue_num: str,
    raw_dir: Path,
    no_cache: bool,
    timeout: int,
    user_agent: str,
) -> Tuple[List[Dict], Dict]:
    variables = {"idPrefix": "tp", "year": str(year), "issueNum": issue_num}
    cache_path = raw_dir / f"{cache_key(['csdl', year, issue_num])}.json"
    payload, cached = graphql_request(
        ISSUE_ARTICLES_QUERY,
        variables=variables,
        cache_path=cache_path,
        no_cache=no_cache,
        timeout=timeout,
        user_agent=user_agent,
    )
    data = payload.get("data") if isinstance(payload.get("data"), dict) else {}
    issue = data.get("issue") if isinstance(data.get("issue"), dict) else {}
    articles = data.get("articles") if isinstance(data.get("articles"), list) else []
    papers = [normalize_csdl_article(article, issue) for article in articles if isinstance(article, dict) and is_research_article(article)]
    return papers, {
        "source": f"TPAMI{year}-{issue_num}",
        "method": "csdl-graphql-cache" if cached else "csdl-graphql",
        "status": "ok" if issue else "missing",
        "count": len(papers),
        "raw_count": len(articles),
        "excluded": len(articles) - len(papers),
        "year": year,
        "issue_num": issue_num,
        "issue_label": issue.get("label", "") if isinstance(issue, dict) else "",
        "volume": issue.get("volume", "") if isinstance(issue, dict) else "",
        "url": f"{CSDL_SOURCE_URL}/{year}/{issue_num}",
    }


def fetch_tpami_years(
    years: Sequence[int],
    raw_dir: Path,
    no_cache: bool,
    timeout: int,
    user_agent: str,
) -> Tuple[List[Dict], List[Dict]]:
    all_papers: List[Dict] = []
    statuses: List[Dict] = []
    for year in years:
        for issue_num in issue_numbers_for_year(year):
            papers, status = fetch_issue(
                year=year,
                issue_num=issue_num,
                raw_dir=raw_dir,
                no_cache=no_cache,
                timeout=timeout,
                user_agent=user_agent,
            )
            statuses.append(status)
            if status.get("status") == "ok":
                all_papers.extend(papers)
            if not no_cache:
                time.sleep(0.1)
    return all_papers, statuses


def format_counts(counts: Dict[str, int]) -> str:
    return ", ".join(f"{key} {value}" for key, value in counts.items()) or "无"


def issue_coverage(statuses: Sequence[Dict]) -> str:
    covered = [
        f"{status.get('year')}-{status.get('issue_num')}"
        for status in statuses
        if status.get("status") == "ok"
    ]
    return ", ".join(covered) or "无"


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
        f"- 来源: [IEEE CSDL: {VENUE_NAME}]({CSDL_SOURCE_URL}) / `idPrefix=tp`",
        f"- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- 年份范围: {', '.join(str(year) for year in years)}",
        f"- 正式卷期覆盖: {issue_coverage(statuses)}",
        "- 范围说明: 仅纳入 TPAMI 正式卷期目录；不包含 Early Access / Preprints。",
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
        lines.append(
            f"  - CSDL 原始记录: {status.get('raw_count')}；剔除非论文记录: {status.get('excluded')}；"
            f"URL: {status.get('url')}"
        )
    lines.append("")
    return "\n".join(lines)


def classification_cache_path(out_dir: Path, classifier: str, years: Sequence[int]) -> Path:
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
    all_papers, statuses = fetch_tpami_years(
        years=years,
        raw_dir=raw_dir,
        no_cache=args.no_cache,
        timeout=args.timeout,
        user_agent=args.user_agent,
    )
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
            "source_url": CSDL_SOURCE_URL,
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "years": years,
            "official_issue_coverage": issue_coverage(statuses),
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
    parser = argparse.ArgumentParser(description="Collect and classify TPAMI official-issue papers from IEEE CSDL.")
    parser.add_argument("--years", default=",".join(str(year) for year in DEFAULT_YEARS), help="Comma-separated years")
    parser.add_argument("--profiles", default="embodied,autonomous-driving", help="Comma-separated report profiles")
    parser.add_argument("--out", default="./reports", help="Output directory")
    parser.add_argument("--no-cache", action="store_true", help="Ignore cached CSDL responses")
    parser.add_argument("--classifier", choices=("codex", "traecli", "rules"), default="traecli", help="Paper classifier backend")
    parser.add_argument("--codex-model", help="Optional model name for codex exec")
    parser.add_argument("--trae-model", default=DEFAULT_TRAE_MODEL, help="TraeCLI model name")
    parser.add_argument("--trae-thinking-effort", choices=("low", "medium", "high"), default=DEFAULT_TRAE_THINKING_EFFORT, help="TraeCLI thinking effort")
    parser.add_argument("--trae-verbosity", choices=("low", "medium", "high"), default=DEFAULT_TRAE_VERBOSITY, help="TraeCLI verbosity")
    parser.add_argument("--llm-batch-size", type=int, default=60, help="Papers per LLM classification batch")
    parser.add_argument("--classifier-timeout", type=int, default=600, help="LLM classifier timeout in seconds")
    parser.add_argument("--no-llm-cache", action="store_true", help="Ignore cached LLM classification results")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout in seconds")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT, help="HTTP User-Agent")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = collect(args)
    except Exception as exc:
        print(f"collect_tpami.py: error: {exc}", file=sys.stderr)
        return 1
    print(f"All papers JSON: {result['all_papers_json']}")
    for report in result["reports"]:
        print(f"Report ({report['profile']}): {report['report_path']}")
        print(f"JSON ({report['profile']}): {report['json_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
