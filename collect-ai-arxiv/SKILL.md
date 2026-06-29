---
name: collect-ai-arxiv
description: Collect and classify AI papers from arXiv cs.RO and cs.CV with profile-specific Chinese daily or weekly Markdown reports. Use when the user asks for 具身智能 arXiv 论文收集、自动驾驶 arXiv 日报/周报、论文分类、VLA/robotics/embodied AI monitoring, autonomous-driving paper monitoring, or maintaining local AI paper digests.
---

# Collect AI arXiv

## Overview

生成 AI 方向 arXiv 日报或周报。默认只扫 `cs.RO` 和 `cs.CV`，通过 `--profile` 选择报告语义：

- `embodied`: 具身智能论文日报/周报，默认 profile。
- `autonomous-driving`: 自动驾驶论文日报/周报。

脚本默认用本机 `codex exec` 做 profile-specific 分类，输出本地 Markdown 报告和 `papers.json`；不写 Notion、飞书或邮件。做论文分析和正式周报重生成时，优先使用 `traecli` 分类器，并指定 `GPT-5.5`、`thinking_effort=high`、`verbosity=high`。

## Workflow

从 Skill 目录运行脚本：

```bash
cd /Users/bytedance/sodalone/paper_collector/collect-ai-arxiv
python scripts/collect_arxiv.py daily --profile embodied --out ../reports
python scripts/collect_arxiv.py weekly --profile embodied --out ../reports
python scripts/collect_arxiv.py daily --profile autonomous-driving --out ../reports
python scripts/collect_arxiv.py weekly --profile autonomous-driving --out ../reports
```

需要指定时间时使用：

```bash
python scripts/collect_arxiv.py daily --profile embodied --date 2026-06-24 --out ../reports
python scripts/collect_arxiv.py weekly --profile autonomous-driving --week 2026-W25 --out ../reports
```

正式重生成论文分析时优先使用 TraeCLI：

```bash
python scripts/collect_arxiv.py weekly --profile embodied --week 2026-W24 --out ../reports --classifier traecli --trae-model GPT-5.5 --trae-thinking-effort high --trae-verbosity high --no-cache --no-llm-cache
```

默认日报是 Asia/Shanghai 的昨天自然日；默认周报是上一个完整自然周，周一到周日。

## Output

默认输出结构：

```text
reports/
├── embodied/
│   ├── daily/
│   │   ├── 具身智能 arXiv YYYY-MM-DD 日报.md
│   │   └── YYYY-MM-DD/
│   │       ├── papers.json
│   │       └── raw/
│   └── weekly/
│       ├── 具身智能 arXiv YYYY-Www-MMDD-MMDD 周报.md
│       └── YYYY-Www/
│           ├── papers.json
│           └── raw/
└── autonomous-driving/
    ├── daily/
    │   ├── 自动驾驶 arXiv YYYY-MM-DD 日报.md
    │   └── YYYY-MM-DD/
    │       ├── papers.json
    │       └── raw/
    └── weekly/
        ├── 自动驾驶 arXiv YYYY-Www-MMDD-MMDD 周报.md
        └── YYYY-Www/
            ├── papers.json
            └── raw/
```

旧 `reports/daily` 和 `reports/weekly` 保留；运行 `embodied` profile 时会复制历史具身报告到 `reports/embodied/...`。
报告 `.md` 文件名与 H1 标题保持一致；`papers.json` 和 `raw/` 继续放在短 label bundle 目录，根目录 `.gitignore` 会忽略这些可再生成中间产物。

报告标题格式：

- `具身智能 arXiv YYYY-MM-DD 日报`
- `具身智能 arXiv YYYY-Www-MMDD-MMDD 周报`
- `自动驾驶 arXiv YYYY-MM-DD 日报`
- `自动驾驶 arXiv YYYY-Www-MMDD-MMDD 周报`

周报标题中的 `MMDD-MMDD` 使用 Asia/Shanghai 自然周周一到周日。

## Classification Rules

读取 `references/taxonomy.md` 作为唯一分类参考。

`embodied` profile:

- `Primary Contribution` 看论文核心贡献，不看关键词出现顺序。
- `Embodied Task` 是任务/场景轴，可多选；报告展示顺序为 `Navigation`、`Manipulation`、`Locomotion`、`Whole-body`、`HRI`、`General/Cross-task`。
- 没有明确具体任务时使用 `General/Cross-task`，保证 Embodied Task 索引覆盖全部候选论文。
- 普通自动驾驶论文默认不进入具身报告；只有明确是通用具身/机器人贡献时才保留。

`autonomous-driving` profile:

- 使用唯一主类 `Driving Stack Category`，正文目录为 `端到端`、`感知`、`规控`、`数据&仿真`。
- 每篇论文只进入一个正文小节；其他能力放 `Technique Tag`。
- prediction、tracking、mapping、localization 归 `Perception`。
- safety evaluation、benchmark、dataset、simulator 归 `Data/Simulation`。
- 安全约束规划、MPC、trajectory optimization、control policy 归 `Planning/Control`。
- 端到端驾驶、VLM/LLM driving agent、foundation driving model 归 `End-to-End Driving`。

## Script Notes

- `--profile` 默认为 `embodied`，推荐显式传入。
- `--sources` 默认为 `cs.RO,cs.CV`；不要自动扩到 `cs.AI`、`cs.LG`、`cs.CL`，除非用户明确要求。
- `--max-results` 是每个 source 的最大抓取数。
- `--classifier` 支持 `traecli`、`codex`、`rules`；正式论文分析优先 `traecli`，默认模型参数为 `--trae-model GPT-5.5 --trae-thinking-effort high --trae-verbosity high`；需要离线快速草稿时用 `--classifier rules`。
- Codex 分类缓存位于输出目录的 `.cache/codex-classifications.json`，按 `profile + taxonomy_version + paper content` 隔离；需要强制重分时加 `--no-llm-cache`。
- TraeCLI 分类缓存位于输出目录的 `.cache/traecli-classifications.json`，同样按 `profile + taxonomy_version + paper content` 隔离；重生成 Trae 分析缓存时加 `--no-llm-cache`。
- LLM 分类输出中的 `解决问题`、`具体方法`、`分类理由` 等自然语言字段必须使用中文；英文摘要只能作为依据，不能直接复制到报告字段。
- 脚本优先用 arXiv API；API 超时、`429` 或解析失败时使用 arXiv HTML recent 列表兜底，并在抓取状态里标注。

## Report Review

复核报告时按这个顺序：

1. 先看 `抓取状态`，确认是否 API 成功或 fallback。
2. 看 `classifier` 状态；如果是 `fallback_rules`，分类只是规则草稿，需要优先复核。
3. `embodied` 检查 `Embodied Task 索引` 是否覆盖全部候选论文；无具体任务时应进入 `General/Cross-task`。
4. `autonomous-driving` 检查每篇论文是否只进入一个 Driving Stack 小节。
5. 检查每篇论文的 `解决问题`、`具体方法`、`分类理由` 是否能直接支撑阅读决策。
