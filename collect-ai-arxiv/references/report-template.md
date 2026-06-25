# 报告模板

## `embodied` profile

文件位置：`.md` 使用完整 H1 标题命名，例如 `reports/embodied/daily/具身智能 arXiv YYYY-MM-DD 日报.md`；`papers.json` 和 `raw/` 使用短 label bundle，例如 `reports/embodied/daily/YYYY-MM-DD/`。

```md
# 具身智能 arXiv YYYY-MM-DD 日报

或

# 具身智能 arXiv YYYY-Www-MMDD-MMDD 周报

- 报告周期: `YYYY-MM-DD` 或 `YYYY-Www`
- 本地时间范围: ...
- UTC 查询范围: ...

## 统计概览

- 候选论文数:
- 高相关:
- 中相关:
- 低相关:
- 主贡献分布:
- 任务分布:

## Embodied Task 索引

### Navigation

1. **[Title](https://arxiv.org/abs/...)**
   - 六类分类: `Foundation/VLA Model | Agent/System | World Model/Representation | Policy/Control/Planning | Data/Benchmark/Simulation | Safety/Evaluation`
   - 相关度: `high | medium | low`
   - 技术标签:
   - 解决问题:
   - 具体方法:
   - 分类理由:

### Manipulation

同上。多任务论文可以在多个任务小节重复出现。

### General/Cross-task

同上。多任务论文可以在多个任务小节重复出现。

## 抓取状态

- `classifier`: ok / codex / selected N / rejected M
- `cs.RO`: ok / api / N 篇
- `cs.CV`: ok / api / N 篇
```

## `autonomous-driving` profile

文件位置：`.md` 使用完整 H1 标题命名，例如 `reports/autonomous-driving/weekly/自动驾驶 arXiv YYYY-Www-MMDD-MMDD 周报.md`；`papers.json` 和 `raw/` 使用短 label bundle，例如 `reports/autonomous-driving/weekly/YYYY-Www/`。

```md
# 自动驾驶 arXiv YYYY-MM-DD 日报

或

# 自动驾驶 arXiv YYYY-Www-MMDD-MMDD 周报

- 报告周期: `YYYY-MM-DD` 或 `YYYY-Www`
- 本地时间范围: ...
- UTC 查询范围: ...

## 统计概览

- 候选论文数:
- 高相关:
- 中相关:
- 低相关:
- 技术栈分布:

## Driving Stack 索引

### 端到端

1. **[Title](https://arxiv.org/abs/...)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high | medium | low`
   - 技术标签:
   - 解决问题:
   - 具体方法:
   - 分类理由:

### 感知

同上。每篇论文只出现在一个 Driving Stack 小节。

### 规控

同上。

### 数据&仿真

同上。

## 抓取状态

- `classifier`: ok / codex / selected N / rejected M
- `cs.RO`: ok / api / N 篇
- `cs.CV`: ok / api / N 篇
```
