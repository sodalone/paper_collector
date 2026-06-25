# Paper Collector

面向 AI 论文监控的本地 arXiv 收集仓库。当前核心能力是通过 `collect-ai-arxiv` Skill 从 arXiv `cs.RO` 和 `cs.CV` 抓取论文，按不同 profile 分类，并生成中文 Markdown 日报或周报。

## 能力范围

- `embodied`: 具身智能论文日报/周报。
- `autonomous-driving`: 自动驾驶论文日报/周报。
- 默认 source 固定为 `cs.RO,cs.CV`。
- 默认按 Asia/Shanghai 自然日或自然周生成报告。
- 输出 Markdown 报告，并保留本地 JSON、raw、分类缓存等可再生成中间产物。

## 目录结构

```text
collect-ai-arxiv/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── report-template.md
│   └── taxonomy.md
└── scripts/collect_arxiv.py

reports/
├── embodied/
└── autonomous-driving/

tests/
└── test_collect_arxiv.py
```

`reports/**/*.md` 是可提交的报告正文；`papers.json`、`raw/` 和 `reports/.cache/` 是可再生成的本地中间产物，已通过 `.gitignore` 忽略。

## 使用方式

从仓库根目录运行：

```bash
python3 collect-ai-arxiv/scripts/collect_arxiv.py daily --profile embodied --out ./reports
python3 collect-ai-arxiv/scripts/collect_arxiv.py weekly --profile embodied --out ./reports
python3 collect-ai-arxiv/scripts/collect_arxiv.py daily --profile autonomous-driving --out ./reports
python3 collect-ai-arxiv/scripts/collect_arxiv.py weekly --profile autonomous-driving --out ./reports
```

指定日期或周：

```bash
python3 collect-ai-arxiv/scripts/collect_arxiv.py daily --profile embodied --date 2026-06-24 --out ./reports
python3 collect-ai-arxiv/scripts/collect_arxiv.py weekly --profile autonomous-driving --week 2026-W25 --out ./reports
```

默认分类器会调用本机 `codex exec`。需要快速离线草稿时可以使用规则分类器：

```bash
python3 collect-ai-arxiv/scripts/collect_arxiv.py weekly --profile autonomous-driving --week 2026-W25 --out ./reports --classifier rules
```

## 报告命名

Markdown 文件名与报告标题保持一致：

```text
reports/embodied/daily/具身智能 arXiv YYYY-MM-DD 日报.md
reports/embodied/weekly/具身智能 arXiv YYYY-Www-MMDD-MMDD 周报.md
reports/autonomous-driving/daily/自动驾驶 arXiv YYYY-MM-DD 日报.md
reports/autonomous-driving/weekly/自动驾驶 arXiv YYYY-Www-MMDD-MMDD 周报.md
```

中间产物继续使用短 label bundle：

```text
reports/embodied/daily/YYYY-MM-DD/papers.json
reports/autonomous-driving/weekly/YYYY-Www/raw/
```

## 验证

```bash
python3 -m unittest tests/test_collect_arxiv.py
python3 -m py_compile collect-ai-arxiv/scripts/collect_arxiv.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py collect-ai-arxiv
```

## 设计原则

- 分类先看论文核心贡献，不按关键词顺序抢主类。
- 具身报告正文以 `Embodied Task` 索引为唯一正文入口。
- 自动驾驶报告正文以 `Driving Stack` 索引为唯一正文入口。
- 可再生成的抓取结果、raw cache 和分类 cache 不进版本库。
