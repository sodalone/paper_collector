# AI arXiv 多 profile 分类参考

同一批 `cs.RO` / `cs.CV` 论文按 `Report Profile` 进入不同报告。不要把不同 profile 的分类字段混用。

## `embodied` Profile

具身报告正文只使用 `Embodied Task` 索引；每篇论文同时展示 `Primary Contribution` 与 `Technique Tag`。

### Primary Contribution

每篇候选论文只能有一个主贡献轴：

**Foundation/VLA Model**:
通用机器人模型、VLA/VLM-to-action、动作 token/action head、跨任务或跨 embodiment 的基础模型训练范式。
_Avoid_: 只是把现成 VLA 用在某个任务上的论文；这类通常主贡献是策略、控制或任务能力。

**Agent/System**:
长程任务执行系统、AgentOS、技能编排、资源调度、闭环反馈、跨机器人协作、真实部署框架。
_Avoid_: 普通 LLM/VLM agent、没有实体机器人行动链路的数字环境 agent。

**World Model/Representation**:
机器人可行动的世界表示、预测或空间记忆，包括 world model、scene graph、semantic map、occupancy、3D representation、affordance。
_Avoid_: 普通 3D/CV 重建；必须服务于具身行动、机器人任务或物理世界交互。

**Policy/Control/Planning**:
具体策略学习、控制、规划、运动生成、轨迹优化、强化学习、模仿学习、whole-body 或 loco-manipulation 控制方法。
_Avoid_: 泛泛的形式化控制、状态估计或交通规划，除非明确连接到具身智能任务。

**Data/Benchmark/Simulation**:
数据集、benchmark、仿真器、评测协议、数据生成 pipeline、teleoperation 或 data engine。
_Avoid_: 只是使用某个数据集做实验，不是数据或评测本身的贡献。

**Safety/Evaluation**:
安全约束、验证、红队评测、风险检测、鲁棒性评估、人类偏好或安全对齐。
_Avoid_: 只在安全场景里实验但核心贡献不是安全或评测的论文。

### Embodied Task

任务轴可以多选；没有明确具体任务时必须使用 `General/Cross-task`：

```text
Navigation
Manipulation
Locomotion
Whole-body
HRI
General/Cross-task
```

普通 autonomous driving、trajectory prediction、traffic-rule planning 不进入具身任务轴；只有明确是通用具身/机器人贡献时才作为具身候选。

## `autonomous-driving` Profile

自动驾驶报告正文只使用 `Driving Stack` 索引；每篇论文只进入一个小节。

### Driving Stack Category

```text
End-to-End Driving
Perception
Planning/Control
Data/Simulation
```

**End-to-End Driving**:
端到端驾驶、VLM/LLM driving agent、foundation driving model、从观测直接输出 ego actions 或驾驶决策的闭环模型。

**Perception**:
自动驾驶感知与环境理解，包括 BEV、occupancy、3D detection、segmentation、tracking、prediction、mapping、localization、sensor fusion。

**Planning/Control**:
规划、规控、MPC、trajectory optimization、motion planning、control policy，以及安全约束控制。

**Data/Simulation**:
dataset、benchmark、simulator、scenario generation、closed-loop benchmark、safety evaluation、合成数据和仿真评测。

纯交通工程、普通 CV、普通机器人且没有自动驾驶栈语境时不是自动驾驶候选。

## Report Fields

Markdown 中每篇论文只展示这些内容：

- `Profile Category`: 具身为六类 `Primary Contribution`；自驾为四类 `Driving Stack Category`。
- `Relevance Tier`: high、medium、low；每个小节内按这个顺序排序。
- `arXiv link`: 标题链接到 arXiv abs page。
- `Technique Tag`: 横向技术标签。
- `Problem Statement`: 论文解决的问题。
- `Method Summary`: 论文采用的具体方法。
- `Classification Reason`: 分类理由。

## Technique Tag

`embodied` 常用横向标签：

```text
vla
robot-foundation-model
action-tokenization
diffusion-policy
manipulation
tactile
locomotion
whole-body
navigation
world-model
spatial-memory
planning
benchmark
dataset
sim2real
hri
safety
deployment-system-reliability
```

`autonomous-driving` 常用横向标签：

```text
end-to-end
foundation-driving-model
vlm-driving
bev
occupancy
3d-detection
tracking
prediction
mapping
localization
planning
control
safety
dataset
benchmark
simulation
closed-loop
sensor-fusion
lidar
camera
radar
v2x
deployment-system-reliability
```

## Relevance Tier

**high**:
标题或摘要明确落在当前 profile 的核心对象和任务链路上。

**medium**:
论文可能服务于当前 profile，但贡献偏表示、工具、评测或系统支撑，主链路不够直接。

**low**:
只命中弱线索，或 HTML fallback 缺摘要/时间，必须人工复核。

**none**:
不是当前 profile 候选；不要写进 Markdown 正文，但保留在 JSON `rejected_papers` 中说明原因。
