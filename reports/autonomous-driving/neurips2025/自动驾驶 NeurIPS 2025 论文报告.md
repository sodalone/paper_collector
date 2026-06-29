# 自动驾驶 NeurIPS 2025 论文报告

- 来源: [NeurIPS 2025 Virtual Papers](https://neurips.cc/virtual/2025/loc/san-diego/papers.html)
- OpenReview 查询: `content.venueid=NeurIPS.cc/2025/Conference`
- 生成时间: 2026-06-28 21:25:26
- 全量论文数: 5286
- 规则预筛候选: 87
- 二次分类输入: 87
- 候选论文数: 73
- 拒绝论文数: 5213
- 高相关: 63
- 中相关: 10
- 低相关: 0
- 技术栈分布: Perception 35, End-to-End Driving 16, Data/Simulation 15, Planning/Control 7
- 录用类型分布: NeurIPS 2025 poster 58, NeurIPS 2025 spotlight 15

## 统计概览

- 候选论文数: 73
- 高相关: 63
- 中相关: 10
- 低相关: 0
- 技术栈分布: Perception 35, End-to-End Driving 16, Data/Simulation 15, Planning/Control 7
- 录用类型分布: NeurIPS 2025 poster 58, NeurIPS 2025 spotlight 15

## Driving Stack 索引

### 端到端
1. **[Embodied Cognition Augmented End2End Autonomous Driving](https://openreview.net/forum?id=0MXUkBmm09)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, camera, planning, closed-loop, dataset
   - 解决问题: 论文关注视觉端到端自动驾驶模型监督信号有限、泛化能力和规划表现受限的问题，尝试引入人类驾驶认知信息来提升自车规划能力。
   - 具体方法: 论文提出一种结合具身认知的端到端驾驶范式，采集驾驶认知数据，并通过视觉特征网络与脑电大模型之间的对比学习，使模型学习潜在的人类驾驶认知表征，再用于增强端到端规划；实验同时覆盖开环和闭环评测。
   - 分类理由: 核心目标是提升端到端自动驾驶模型的自车规划输出，方法围绕端到端驾驶模型、认知增强和闭环规划评测展开，因此应归入端到端目录，而不是单纯的数据集或仿真评测。

2. **[AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://openreview.net/forum?id=28qUA2bSe5)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, vlm-driving, planning, closed-loop, benchmark, dataset
   - 解决问题: 论文解决端到端自动驾驶视觉语言动作模型中动作不可行、结构复杂和推理冗长的问题。
   - 具体方法: 方法把语义推理和轨迹生成统一到自回归模型中，将连续轨迹离散化为可行动作，并结合监督微调和强化微调实现快慢两种推理模式。
   - 分类理由: 模型直接从视觉和语言输入生成驾驶轨迹与动作，并在开环和闭环自动驾驶基准上验证，明确属于端到端驾驶。

3. **[Model-Based Policy Adaptation for Closed-Loop End-to-end Autonomous Driving](https://openreview.net/forum?id=4OLbpaTKJe)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, closed-loop, simulation, safety, deployment-system-reliability, planning
   - 解决问题: 论文解决端到端自动驾驶模型在开环评测表现较好但闭环部署中容易产生级联误差、泛化不足和安全性下降的问题。
   - 具体方法: 方法使用几何一致的仿真生成反事实轨迹数据，训练扩散式策略适配器修正基础策略，并用多步价值模型在推理时选择长期收益更高的候选轨迹。
   - 分类理由: 论文直接改进端到端驾驶智能体的闭环轨迹决策与部署鲁棒性，输出面向自车行动的策略，因此归入端到端目录。

4. **[RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-based Reinforcement Learning](https://openreview.net/forum?id=9V3crVSPH7)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, closed-loop, simulation, safety, benchmark
   - 解决问题: 现有端到端自动驾驶多依赖模仿学习，容易受到因果混淆和开环训练评测差距影响，难以在安全关键和分布外场景中稳定学习驾驶策略。
   - 具体方法: 论文提出基于三维高斯重建环境的闭环强化学习框架，利用逼真的数字场景进行大规模试错训练，并通过安全奖励和模仿学习正则约束，使端到端驾驶策略更好地学习因果关系和人类驾驶行为。
   - 分类理由: 核心目标是训练直接输出自动驾驶行为的端到端驾驶策略，虽然使用仿真环境、强化学习和安全评测，但主线属于端到端驾驶模型训练与闭环策略学习。

5. **[Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2)](https://openreview.net/forum?id=CAz7UGRdLs)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, planning, closed-loop, simulation, foundation-driving-model
   - 解决问题: 端到端自动驾驶中，直接用原始传感器输入进行强化学习训练仍然困难，而仅依赖模仿学习容易出现因果混淆和分布偏移。
   - 具体方法: 论文提出双流模型式强化学习方法，先训练使用特权信息的世界模型和神经规划器，再通过引导机制让原始传感器世界模型在展开过程中对齐特权世界模型，从而支持原始传感器输入下的端到端驾驶训练。
   - 分类理由: 论文关注从原始传感器到驾驶决策的端到端自动驾驶强化学习框架，规划器和世界模型是服务于端到端策略训练的组成部分，因此归入端到端目录。

6. **[Future-Aware End-to-End Driving: Bidirectional Modeling of Trajectory Planning and Scene Evolution](https://openreview.net/forum?id=FU62P5IXhK)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, bev, planning, prediction, closed-loop, benchmark
   - 解决问题: 论文解决端到端自动驾驶中过度依赖当前场景、对未来场景演化建模不足，导致复杂场景下决策适应性受限的问题。
   - 具体方法: 方法联合预测未来鸟瞰图表示和自车轨迹，通过未来感知规划模块把预测场景特征注入轨迹规划器，并迭代优化场景演化与车辆规划。
   - 分类理由: 论文明确是从原始传感输入到未来轨迹的端到端驾驶框架，并包含闭环自车动作输出，因此归入端到端。

7. **[GaussianFusion: Gaussian-Based Multi-Sensor Fusion for End-to-End Autonomous Driving](https://openreview.net/forum?id=LBo4e6Y7Zg)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, sensor-fusion, planning, prediction, benchmark
   - 解决问题: 论文解决端到端自动驾驶中多传感器融合表示可解释性不足、计算开销较高以及对轨迹规划支持不充分的问题。
   - 具体方法: 方法使用高斯表示作为多传感器信息融合的中间载体，并设计级联规划头，让轨迹预测与场景高斯表示反复交互以提升规划质量。
   - 分类理由: 论文明确面向端到端自动驾驶，并以融合后的表示直接服务轨迹规划输出，因此应归入端到端目录，而不是单独归为感知。

8. **[VR-Drive: Viewpoint-Robust End-to-End Driving with Feed-Forward 3D Gaussian Splatting](https://openreview.net/forum?id=NXPaQRErIT)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, camera, planning, benchmark
   - 解决问题: 论文关注端到端自动驾驶在不同摄像头视角和车辆配置下鲁棒性不足的问题，视角变化会影响规划表现。
   - 具体方法: 方法在端到端驾驶框架中联合学习三维场景重建，通过前馈式高斯表示生成辅助视角，并结合多视角记忆和一致性蒸馏提升视角泛化能力。
   - 分类理由: 模型以端到端自动驾驶和规划输出为目标，三维重建只是辅助任务，因此归入端到端。

9. **[Prioritizing Perception-Guided Self-Supervision: A New Paradigm for Causal Modeling in End-to-End Autonomous Driving](https://openreview.net/forum?id=PZqII8EoFG)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, closed-loop, planning, safety
   - 解决问题: 论文针对端到端自动驾驶在闭环场景中因模仿学习产生因果混淆而性能下降的问题，目标是让决策模块更可靠地理解环境与驾驶动作之间的因果关系。
   - 具体方法: 方法使用感知结果作为主要自监督信号，将决策模块的输入和输出与车道中心线等感知结构对齐，从而引导模型学习更明确的环境到动作映射关系。
   - 分类理由: 论文明确研究端到端自动驾驶训练范式，并以闭环驾驶效果为核心目标，属于端到端驾驶目录，而不是单独的感知或传统规控方法。

10. **[DiffE2E: Rethinking End-to-End Driving with a Hybrid Diffusion-Regression-Classification Policy](https://openreview.net/forum?id=WJnqeSPkQe)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, closed-loop, control, benchmark, sensor-fusion, deployment-system-reliability
   - 解决问题: 论文解决端到端驾驶中行为多模态带来的轨迹生成不稳定和部署鲁棒性问题。
   - 具体方法: 方法先对多传感器感知特征做多尺度对齐，再用扩散、回归和分类混合解码器联合建模未来轨迹分布、速度等控制变量，并融合高层目标生成可控轨迹。
   - 分类理由: 论文明确提出端到端自动驾驶框架，并在闭环驾驶基准上评估轨迹与控制输出，属于端到端驾驶。

11. **[DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving](https://openreview.net/forum?id=eIf9GNcA5n)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, safety, benchmark
   - 解决问题: 论文解决端到端自动驾驶中模仿学习容易产生表面像人类但实际不安全轨迹的问题，重点提升直接从感知输入预测未来轨迹的策略安全性和可靠性。
   - 具体方法: 方法提出安全偏好直接优化框架，将人类模仿相似度与规则安全评分蒸馏成统一策略分布，并进一步通过轨迹级偏好对齐进行迭代优化，在基准测试中提升驾驶行为安全性。
   - 分类理由: 该论文明确面向端到端自动驾驶策略学习，直接优化未来轨迹输出，并以安全偏好改进驾驶策略，因此唯一归入端到端驾驶，而不是单独的规控或评测数据方向。

12. **[FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving](https://openreview.net/forum?id=fCirUh6FRb)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, vlm-driving, foundation-driving-model, planning, prediction, safety, benchmark
   - 解决问题: 论文解决视觉语言动作驾驶模型使用文本推理链时容易丢失时空视觉细节、造成感知到规划跨模态鸿沟的问题。
   - 具体方法: 方法让模型生成包含未来车道线和三维框等先验的未来视觉帧作为视觉时空推理链，再由同一模型根据当前观测和视觉推理结果规划轨迹，并通过视觉词元扩展和联合预训练增强未来生成能力。
   - 分类理由: 论文以视觉语言动作模型直接服务端到端驾驶规划，输出轨迹并评估碰撞和轨迹效果，属于端到端驾驶而非单纯感知。

13. **[Temporal Logic-Based Multi-Vehicle Backdoor Attacks against Offline RL Agents in End-to-end Autonomous Driving](https://openreview.net/forum?id=ifavjJaKQa)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, safety, deployment-system-reliability
   - 解决问题: 论文研究端到端自动驾驶系统在真实可部署触发条件下可能遭受的后门攻击风险，重点评估多车轨迹触发器对驾驶智能体安全性的影响。
   - 具体方法: 论文用时序逻辑描述攻击车辆行为，通过可配置行为模型生成触发轨迹，并结合负样本训练增强攻击隐蔽性，在多个离线强化学习端到端驾驶智能体上进行实验。
   - 分类理由: 研究对象是直接输出驾驶行为的端到端自动驾驶智能体，方法围绕端到端驾驶策略的安全攻击与可靠性评估展开，因此归入端到端类别。

14. **[AdvEDM: Fine-grained Adversarial Attack against VLM-based Embodied Agents](https://openreview.net/forum?id=jmLCBLeEC4)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: vlm-driving, safety, planning
   - 解决问题: 论文研究视觉语言模型驱动的具身智能体在自动驾驶等任务中容易受到细粒度对抗攻击的问题，攻击会诱导智能体输出错误但看似有效的决策。
   - 具体方法: 方法只修改图像中少数关键目标的语义，同时保留其他区域语义一致性，使模型在任务上下文中产生错误动作或决策，并设计了移除目标语义和添加目标语义两类攻击。
   - 分类理由: 该工作针对视觉语言具身驾驶智能体的决策与动作输出安全性，符合端到端驾驶和智能体驾驶范畴。

15. **[CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action Model](https://openreview.net/forum?id=qUmULptJuY)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `high`
   - 技术标签: end-to-end, vlm-driving, simulation, dataset, deployment-system-reliability
   - 解决问题: 论文解决视觉语言驾驶模型难以把仿真中的长尾场景处理能力迁移到真实部署场景的问题。
   - 具体方法: 方法构建因果链视觉语言动作框架，分别训练仿真教师模型和真实数据学生模型，并通过对抗式迁移把长尾驾驶能力从仿真域传递到真实域。
   - 分类理由: 该方法面向可解释自动驾驶的视觉语言动作模型，并强调端到端驾驶逻辑推理与部署迁移，因此归入端到端驾驶。

16. **[Each Complexity Deserves a Pruning Policy](https://openreview.net/forum?id=bHCB8H90aZ)**
   - 四类分类: `End-to-End Driving`
   - 相关度: `medium`
   - 技术标签: vlm-driving, end-to-end, deployment-system-reliability
   - 解决问题: 论文关注大视觉语言模型在不同输入复杂度下视觉令牌裁剪策略固定的问题，并将该效率问题扩展评估到自动驾驶视觉语言动作模型中。
   - 具体方法: 方法提出无需训练的复杂度自适应裁剪框架，通过估计视觉令牌与文本令牌之间的信息关联，生成满足计算预算的动态保留曲线，从而为不同样本和任务调整裁剪强度。
   - 分类理由: 虽然方法是通用视觉语言模型加速技术，但明确评估在自动驾驶视觉语言动作模型上，关联端到端驾驶智能体的部署效率，因此归入端到端目录。


### 感知
1. **[OpenBox: Annotate Any Bounding Boxes in 3D](https://openreview.net/forum?id=7ieZWCc7rB)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: 3d-detection, lidar, camera, dataset, foundation-driving-model
   - 解决问题: 论文关注自动驾驶三维目标检测中的标注成本和开放词汇识别问题，目标是在不依赖大量人工标注和多轮自训练的情况下，为三维点云生成高质量三维框标注。
   - 具体方法: 方法采用两阶段自动标注流程，先利用二维视觉基础模型从图像中提取实例线索，并与三维点云进行上下文感知关联；随后根据目标的刚性和运动状态分类，结合类别尺度统计生成自适应三维边界框。
   - 分类理由: 论文直接服务于自动驾驶三维检测标注和开放词汇目标识别，核心是感知数据标注与三维检测能力建设，但最终目标仍是感知检测，因此归入感知而不是数据仿真。

2. **[CodeMerge: Codebook-Guided Model Merging for Robust Test-Time Adaptation in Autonomous Driving](https://openreview.net/forum?id=9eVXIN9Vij)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: 3d-detection, lidar, mapping, prediction, planning, benchmark, deployment-system-reliability
   - 解决问题: 论文解决自动驾驶三维感知模型在动态测试环境下鲁棒性不足，以及测试时自适应模型合并成本过高的问题。
   - 具体方法: 方法用低维特征指纹表示不同检查点，构建键值码本，并根据指纹计算合并系数，从而高效组合模型以适应测试时分布变化。
   - 分类理由: 尽管方法也影响端到端驾驶和下游规划，主要实验与问题聚焦激光雷达三维检测和在线感知适应，因此归入感知。

3. **[TREND: Unsupervised 3D Representation Learning via Temporal Forecasting for LiDAR Perception](https://openreview.net/forum?id=AHccBzULR7)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: 3d-detection, lidar
   - 解决问题: 论文关注激光雷达感知中标注成本高的问题，希望通过无监督方式学习可迁移的三维表示，提升检测和分割任务表现。
   - 具体方法: 方法利用时序激光雷达序列预测未来观测，通过循环嵌入和面向激光雷达的时序神经场进行可微渲染训练，从而获得预训练三维特征。
   - 分类理由: 下游验证集中在三维目标检测和激光雷达语义分割，属于自动驾驶感知预训练与表征学习，因此归入感知。

4. **[TopoPoint: Enhance Topology Reasoning via Endpoint Detection in Autonomous Driving](https://openreview.net/forum?id=C2fJE8t0lH)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: mapping
   - 解决问题: 论文关注自动驾驶路口场景中的车道拓扑推理问题，现有方法容易因车道端点偏移导致连接关系构建错误。
   - 具体方法: 方法显式检测车道端点，并通过点与车道的交互注意力、图卷积特征聚合以及几何匹配细化端点位置，从而提升拓扑结构推理的稳定性。
   - 分类理由: 核心任务是车道结构与拓扑理解，属于高精地图和结构化场景感知范畴，因此归入感知。

5. **[ODG: Occupancy Prediction Using Dual Gaussians](https://openreview.net/forum?id=CkmLys7ipp)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: occupancy, prediction, camera, bev
   - 解决问题: 论文关注自动驾驶场景中的三维占据预测问题，目标是从车载相机图像中恢复周围环境的细粒度几何结构和语义信息，同时缓解高分辨率体素表示难扩展、单一稀疏查询难以刻画复杂物体差异的问题。
   - 具体方法: 方法将驾驶场景拆分为静态部分和动态部分，设计双重稀疏高斯查询来分别建模不同类型目标，并使用分层高斯变换器预测占据体素中心、语义类别和高斯参数；同时借助三维高斯渲染能力，引入深度和语义图监督以增强像素级对齐。
   - 分类理由: 核心任务是三维占据预测和语义占据建模，属于自动驾驶感知栈中的环境理解问题，而不是直接规划控制或端到端动作输出。

6. **[COME: Adding Scene-Centric Forecasting Control to Occupancy World Model](https://openreview.net/forum?id=EYxLmZRSK1)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: occupancy, prediction, camera, sensor-fusion, simulation, dataset
   - 解决问题: 论文解决自动驾驶占用世界模型中自车运动视角变化与场景自身演化纠缠，导致未来占用预测不准确的问题。
   - 具体方法: 方法引入场景中心预测分支生成与自车运动无关的未来特征，再通过控制模块把这些条件注入占用世界模型，提升未来占用预测可控性和精度。
   - 分类理由: 核心输出是未来占用预测，属于感知中的占用建模和时空预测，而不是直接规划控制。

7. **[DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving](https://openreview.net/forum?id=HF5A73jmxq)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: mapping, foundation-driving-model
   - 解决问题: 论文关注自动驾驶场景中大规模四维高斯重建能力不足的问题，希望提升未见驾驶场景与动态目标的时空几何重建质量，并为下游任务提供可用表征。
   - 具体方法: 方法构建了一个面向自动驾驶的四维高斯重建模型，通过剪枝与膨胀模块减少冗余高斯点并补强复杂物体表达，同时将动态与静态部分解耦，以学习跨时间一致的场景几何。
   - 分类理由: 核心贡献是驾驶场景的四维重建与几何表征，属于自动驾驶环境感知和场景建图范畴，而不是直接输出驾驶动作或规划控制。

8. **[BevSplat: Resolving Height Ambiguity via Feature-Based Gaussian Primitives for Weakly-Supervised Cross-View Localization](https://openreview.net/forum?id=Ig5mtZ8etr)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: bev, camera, localization, dataset
   - 解决问题: 论文解决地面相机与卫星图像跨视角定位中，由缺少深度信息导致高度歧义和位姿估计不准的问题。
   - 具体方法: 方法把地面图像像素表示为带语义和空间特征的三维高斯基元，再合成为鸟瞰特征图，用于相对位姿估计。
   - 分类理由: 任务是跨视角相机定位和位姿估计，属于自动驾驶感知中的定位方向。

9. **[Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation](https://openreview.net/forum?id=KWNabnuuct)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: foundation-driving-model, camera
   - 解决问题: 论文解决开放词汇语义分割在未知类别和未知域中同时保持像素级识别能力与鲁棒性的问题，面向真实自动驾驶恶劣环境具有应用价值。
   - 具体方法: 方法冻结视觉基础模型，引入深度基础模型提取几何结构特征，并通过几何文本查询、粗掩码先验和融合预测头增强跨域开放词汇分割能力。
   - 分类理由: 研究对象是语义分割与开放词汇场景理解，属于自动驾驶视觉感知能力，因此归入感知目录。

10. **[SynCL: A Synergistic Training Strategy with Instance-Aware Contrastive Learning for End-to-End Multi-Camera 3D Tracking](https://openreview.net/forum?id=LrIRYbn3Rn)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: tracking, camera, 3d-detection, dataset
   - 解决问题: 论文解决端到端多摄像头三维跟踪中检测查询和跟踪查询共享注意力时相互干扰、优化困难的问题。
   - 具体方法: 作者提出实例感知对比学习协同训练策略，缓解对象查询过度去重和轨迹查询自中心注意力带来的表示冲突。
   - 分类理由: 任务是多摄像头三维目标跟踪，属于自动驾驶感知链路；虽然标题出现 end-to-end，但输出不是自车驾驶动作，因此归入感知。

11. **[SDTagNet: Leveraging Text-Annotated Navigation Maps for Online HD Map Construction](https://openreview.net/forum?id=N3E1cU8Cv3)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: mapping, sensor-fusion, deployment-system-reliability
   - 解决问题: 论文解决在线高精地图构建受车载传感器感知距离限制的问题，并希望利用更易维护的标准导航地图提升远距离地图元素识别和整体建图质量。
   - 具体方法: 论文提出一种利用带文本标注导航地图的在线高精地图构建方法，通过自然语言方式编码标准地图中的道路语义信息，并将其作为先验增强局部高精地图生成。
   - 分类理由: 核心任务是在线高精地图构建，属于自动驾驶感知与地图构建方向；虽然涉及部署可扩展性，但主要贡献不是数据集、仿真或规划控制。

12. **[CAML: Collaborative Auxiliary Modality Learning for Multi-Agent Systems](https://openreview.net/forum?id=OhUu5PlRkF)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: sensor-fusion, v2x, safety, deployment-system-reliability
   - 解决问题: 论文解决多智能体或网联自动驾驶场景中，训练时可用多模态信息但测试时部分模态缺失导致感知盲区的问题。
   - 具体方法: 方法让多个智能体在训练阶段协作共享多模态数据，同时学习在测试阶段使用更少模态完成事故检测和语义分割。
   - 分类理由: 论文验证任务包括网联自动驾驶事故检测和协同语义分割，主要落在协同感知与鲁棒融合。

13. **[T-norm Selection for Object Detection in Autonomous Driving with Logical Constraints](https://openreview.net/forum?id=QsguopCLfc)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: 3d-detection, safety, dataset
   - 解决问题: 论文关注自动驾驶目标检测模型中逻辑约束损失的选择问题，试图提升检测结果对常识规则和安全约束的符合程度。
   - 具体方法: 论文提出神经符号框架，在训练中比较并自适应选择不同的T范数，同时用调度机制控制逻辑约束损失的影响，并在自动驾驶目标检测数据集上验证效果。
   - 分类理由: 核心任务是自动驾驶场景下的目标检测模型改进，虽然涉及安全约束和数据集评测，但主体仍属于感知栈中的检测方法。

14. **[DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method](https://openreview.net/forum?id=T9qNDtvAJX)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: tracking, prediction, lidar, dataset
   - 解决问题: 论文解决三维场景流估计中过度依赖两帧输入、难以高效利用多帧时序信息的问题，同时处理类别不均衡和运动不一致。
   - 具体方法: 方法用轻量级多帧三维框架提取增量运动线索，并加入类别均衡损失和实例一致性损失，以提升运动估计准确性和推理效率。
   - 分类理由: 场景流估计是自动驾驶感知中的三维运动理解任务，直接服务于动态目标运动感知。

15. **[GaRA-SAM: Robustifying Segment Anything Model with Gated-Rank Adaptation](https://openreview.net/forum?id=VXygIRRHxz)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: camera, deployment-system-reliability, benchmark
   - 解决问题: 论文关注在自动驾驶等高风险场景中，通用分割模型面对图像退化和污染输入时鲁棒性不足的问题。
   - 具体方法: 方法在冻结的分割基础模型中加入轻量门控低秩适配器，根据输入内容动态调整有效秩，从而在保持泛化能力的同时提升鲁棒分割表现。
   - 分类理由: 核心任务是图像分割模型的鲁棒感知能力提升，虽然提到部署可靠性和评测集，但主要贡献属于自动驾驶感知栈。

16. **[DepthVanish: Optimizing Adversarial Interval Structures for Stereo-Depth-Invisible Patches](https://openreview.net/forum?id=eD1VyYURiq)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: camera, safety, deployment-system-reliability
   - 解决问题: 论文解决立体深度估计系统在物理世界中可能被对抗补丁误导的问题，这会让近处物体被错误判断为远处物体并带来安全风险。
   - 具体方法: 方法发现并优化带规则间隔的重复纹理网格结构，同时联合优化间隔和纹理内容，使补丁能攻击不同立体深度算法和真实商用深度相机。
   - 分类理由: 研究对象是自动驾驶关键感知能力中的立体深度估计安全性，因此归入感知。

17. **[RayFusion: Ray Fusion Enhanced Collaborative Visual Perception](https://openreview.net/forum?id=eK61hWzAAl)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: sensor-fusion, v2x, camera, occupancy, 3d-detection
   - 解决问题: 纯相机协同感知在自动驾驶场景中缺少显式深度信息，容易产生深度估计歧义，导致三维目标检测结果不准确。
   - 具体方法: 论文提出基于射线占用信息的协同视觉感知融合方法，利用协作者提供的射线占用线索减少相机射线方向上的冗余和误检，从而提升纯相机协同三维检测性能。
   - 分类理由: 该工作解决的是协同视觉感知和三维检测问题，主要技术围绕相机、占用信息和多车协同融合展开，属于自动驾驶感知栈。

18. **[QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction](https://openreview.net/forum?id=eZNdkwJYbN)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: occupancy, prediction
   - 解决问题: 论文解决自动驾驶三维占用预测中稠密体素表示效率低、稀疏高斯形状表达能力不足的问题，目标是更高效地表达复杂道路场景的几何和语义结构。
   - 具体方法: 方法使用超二次曲面作为场景基元，构建概率混合表示来描述占用概率和语义信息，并设计相应模型用较少基元表达多样化物体形状。
   - 分类理由: 论文核心任务是三维语义占用预测，属于自动驾驶环境感知范畴；其输出服务于场景理解而非直接规划控制，因此归入感知。

19. **[Availability-aware Sensor Fusion via Unified Canonical Space](https://openreview.net/forum?id=foy0BWzOFL)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: sensor-fusion, camera, lidar, radar, bev, 3d-detection, dataset
   - 解决问题: 论文解决自动驾驶多传感器融合在传感器退化或失效时鲁棒性不足，以及跨传感器表示和计算成本难以兼顾的问题。
   - 具体方法: 方法将相机、激光雷达和四维毫米波雷达特征投影到统一规范空间，并用跨传感器块级注意力增强融合鲁棒性。
   - 分类理由: 核心任务是多传感器三维目标检测与特征融合，属于自动驾驶感知。

20. **[Real-Time Scene-Adaptive Tone Mapping for High-Dynamic Range Object Detection](https://openreview.net/forum?id=hAi0JapiZ7)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: camera, 3d-detection, deployment-system-reliability
   - 解决问题: 车载高动态范围图像虽然能保留更多明暗细节，但现有嵌入式视觉检测网络通常面向低动态范围输入训练，直接处理高位深原始图像时检测性能会明显下降。
   - 具体方法: 论文提出面向检测任务优化的实时场景自适应色调映射方法，通过神经光度校准约束动态范围，并用尺度不变的局部色调映射模块保留图像细节，同时支持低成本的性能迁移微调。
   - 分类理由: 该工作服务于自动驾驶车载视觉目标检测前端，重点是提升高动态范围相机输入下的检测可靠性，不是驾驶策略或规划控制，因此归入感知目录。

21. **[Layer-Wise Modality Decomposition for Interpretable Multimodal Sensor Fusion](https://openreview.net/forum?id=j7L5AiVqJQ)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: sensor-fusion, camera, lidar, radar, prediction
   - 解决问题: 论文解决自动驾驶多传感器感知模型缺乏可解释性的问题，尤其是融合网络中不同模态信息相互纠缠后，难以判断相机、雷达和激光雷达分别如何影响预测结果。
   - 具体方法: 论文提出逐层模态分解方法，对已训练的多模态融合感知模型进行后验分析，在各网络层中拆解不同传感器模态的贡献，并通过扰动指标和可视化方式验证解释效果。
   - 分类理由: 研究对象是自动驾驶感知模型中的多传感器融合解释，实验覆盖相机、毫米波雷达和激光雷达组合，核心任务属于感知系统分析，因此归入感知类别。

22. **[Scaling Data-Driven Probabilistic Robustness Analysis for Semantic Segmentation Neural Networks](https://openreview.net/forum?id=liefJOFVfH)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: safety
   - 解决问题: 论文关注语义分割神经网络在输入扰动和对抗样本下的概率鲁棒性验证问题，尤其是现代分割模型输出维度高、结构复杂，传统验证方法难以扩展且容易给出过于保守的安全保证。
   - 具体方法: 论文提出一种与模型架构无关的数据驱动概率验证算法，结合采样式可达性分析和共形推断思想，在保持计算可行性的同时估计高维分割输出的不确定性与鲁棒边界。
   - 分类理由: 研究对象是语义分割网络的鲁棒性与安全验证，语义分割属于自动驾驶感知栈核心任务，因此归入感知，而不是端到端驾驶或规控。

23. **[Learning Temporal 3D Semantic Scene Completion via Optical Flow Guidance](https://openreview.net/forum?id=nK5WovvHk2)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: occupancy, camera, prediction
   - 解决问题: 论文解决自动驾驶三维语义场景补全中时序信息利用不足、运动动态被忽略以及跨帧一致性较弱的问题。
   - 具体方法: 方法利用光流引导时序特征对齐与聚合，并结合遮挡信息对三维体素进行细化，从而提升场景几何与语义补全的准确性。
   - 分类理由: 核心任务是三维语义场景补全，直接服务于自动驾驶环境感知与占用理解，因此归入感知目录。

24. **[Extremely Simple Multimodal Outlier Synthesis for Out-of-Distribution Detection and Segmentation](https://openreview.net/forum?id=ocBuEUl6Yz)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: sensor-fusion, safety, dataset, benchmark
   - 解决问题: 论文关注多模态自动驾驶感知模型在分布外目标检测与分割中的过度自信问题，尤其是在安全关键场景下缺少未知异常样本监督的问题。
   - 具体方法: 论文提出一种特征混合方法，在特征空间快速合成多模态异常样本，并引入面向异常分割的数据集，用于提升模型区分正常数据与异常数据的能力。
   - 分类理由: 核心任务是分布外检测与分割，实验涉及自动驾驶感知数据集和异常目标分割，因此归入感知，而不是数据集或仿真主导的工作。

25. **[Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting](https://openreview.net/forum?id=p3z75I8lVq)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: mapping, camera
   - 解决问题: 论文关注真实驾驶场景重建中的光照和成像不一致问题，这会影响神经渲染得到的几何精度，进而影响环境建模质量。
   - 具体方法: 方法将外观编码与多尺度双边网格统一起来，在像素级进行颜色映射约束，以改善动态驾驶场景高斯重建中的几何准确性。
   - 分类理由: 论文重点是驾驶场景三维重建和几何建图，虽然提到控制应用价值，但核心技术贡献仍属于感知建图。

26. **[SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving](https://openreview.net/forum?id=plpAecfkf4)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: 3d-detection, occupancy, prediction, bev, camera
   - 解决问题: 论文解决自动驾驶稀疏感知模型虽然推理高效但特征表达不够细致的问题，目标是在不显式构建密集鸟瞰或体素表示的情况下提升三维检测和占用预测性能。
   - 具体方法: 论文提出一种基于查询的自监督预训练框架，让稀疏查询预测三维高斯表示，并通过重建多视角图像和深度图学习上下文特征，再在下游任务中通过查询交互机制迁移到检测和占用预测网络。
   - 分类理由: 论文直接服务于三维目标检测和占用预测等自动驾驶感知任务，核心贡献是感知模型预训练与特征增强，因此归入感知。

27. **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://openreview.net/forum?id=q3CU6ltlqE)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: camera, lidar, mapping, localization, foundation-driving-model, prediction
   - 解决问题: 论文解决自动驾驶城市三维重建依赖激光雷达深度先验的问题，避免多传感器标定和重投影误差带来的几何不准。
   - 具体方法: 方法从多视角图像深度预测初始化稠密点云，通过渐进剪枝提升一致性，再用深度基础模型的扩散先验联合优化高斯几何和深度图，并加强道路区域几何约束。
   - 分类理由: 任务是城市三维场景重建和几何感知，属于自动驾驶感知与地图建模方向。

28. **[Rig3R: Rig-Aware Conditioning and Discovery for 3D Reconstruction](https://openreview.net/forum?id=vEFPm6gw2s)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: camera, sensor-fusion, mapping, localization
   - 解决问题: 论文关注多相机刚性平台中的三维重建问题，目标是在自动驾驶等具身场景里同时估计载体位姿和三维场景结构，并缓解现有多视角模型忽略相机阵列结构带来的效果限制。
   - 具体方法: 方法将相机编号、时间和平台位姿等可选元数据作为条件，学习具有平台结构感知能力的潜在表示，并联合预测点图以及全局位姿射线图、平台中心射线图；在元数据缺失时，也能从图像中推断相机平台结构。
   - 分类理由: 核心任务是多相机三维场景结构和自运动位姿估计，服务于自动驾驶环境理解与空间重建，因此归入感知目录，而不是端到端驾驶或规控。

29. **[Alligat0R: Pre-Training through Covisibility Segmentation for Relative Camera Pose Regression](https://openreview.net/forum?id=yHJRI6rzaA)**
   - 四类分类: `Perception`
   - 相关度: `high`
   - 技术标签: camera, dataset, localization, prediction
   - 解决问题: 论文解决双视图位姿估计预训练中非共视区域难以建模的问题，这会影响三维重建和相对位姿回归效果。
   - 具体方法: 方法将跨视图补全替换为共视性分割预训练，预测像素在另一视图中是共视、被遮挡还是视野外，并构建包含道路场景的大规模标注数据。
   - 分类理由: 核心任务是相机相对位姿回归与定位相关视觉感知，因此归入感知。

30. **[OmniSegmentor: A Flexible Multi-Modal Learning Framework for Semantic Segmentation](https://openreview.net/forum?id=Kdqzbx8YGU)**
   - 四类分类: `Perception`
   - 相关度: `medium`
   - 技术标签: sensor-fusion, camera, dataset
   - 解决问题: 论文研究多模态语义分割的通用预训练与微调问题，希望模型能够在不同视觉模态组合下获得更鲁棒的场景感知能力，并在包含自动驾驶相关数据集的分割任务中提升效果。
   - 具体方法: 方法构建了包含多种视觉模态的大规模预训练数据，并设计统一的多模态预训练框架，使模型能够编码不同模态信息，再迁移到多个语义分割数据集上进行微调和评测。
   - 分类理由: 虽然论文并非专门面向自动驾驶系统，但其任务是语义分割，并在自动驾驶相关数据集上验证感知能力，因此归入感知；相关性低于专门自动驾驶论文。

31. **[PointTruss: K-Truss for Point Cloud Registration](https://openreview.net/forum?id=MuxBO5f8mL)**
   - 四类分类: `Perception`
   - 相关度: `medium`
   - 技术标签: lidar, localization, mapping
   - 解决问题: 论文关注点云配准中的外点剔除问题，目标是在复杂三维场景中兼顾鲁棒性与计算效率。该任务可服务于自动驾驶中的激光雷达定位和建图，但论文主体更偏通用三维视觉方法。
   - 具体方法: 方法将图论中的三角支撑约束引入点云配准，用较宽松但高效的结构约束筛选内点，并结合共识投票采样和空间分布评分，使匹配点既可靠又分布均匀。
   - 分类理由: 论文处理点云配准，和自动驾驶感知、定位、建图链路相关；虽然实验包含驾驶数据集，但核心不是端到端驾驶或规控，因此归入感知。

32. **[GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion](https://openreview.net/forum?id=UkBwyp3aXG)**
   - 四类分类: `Perception`
   - 相关度: `medium`
   - 技术标签: lidar, localization, mapping, dataset
   - 解决问题: 论文关注彩色三维点云在低重叠和不完整场景下配准困难的问题，这类能力可服务于定位、建图和点云感知。
   - 具体方法: 方法采用两阶段点云配准框架，融合几何、颜色和三维高斯信息，并通过可微渲染与联合光度损失细化配准结果。
   - 分类理由: 虽然方法具有通用三维视觉属性，但涉及点云配准、激光雷达数据和道路数据集，最接近自动驾驶感知中的定位与建图能力。

33. **[DINO-Foresight: Looking into the Future with DINO](https://openreview.net/forum?id=gimtybo07H)**
   - 四类分类: `Perception`
   - 相关度: `medium`
   - 技术标签: foundation-driving-model, prediction
   - 解决问题: 论文关注动态场景中未来语义信息的预测问题，目标是在自动驾驶和机器人等场景下更高效地理解未来环境状态，避免直接在像素层面预测带来的高计算开销和无关细节干扰。
   - 具体方法: 方法将预训练视觉基础模型的特征作为语义潜空间，训练一个掩码特征变换器来自监督预测这些特征随时间的演化，再接入不同任务头完成未来帧的场景理解任务。
   - 分类理由: 该工作主要输出未来语义特征并服务于场景理解任务，没有直接生成自车动作或闭环驾驶决策，因此不归入端到端驾驶；其核心是未来场景语义感知与预测，最适合归入感知。

34. **[Approximate Domain Unlearning for Vision-Language Models](https://openreview.net/forum?id=lv4zLWzOi2)**
   - 四类分类: `Perception`
   - 相关度: `medium`
   - 技术标签: vlm-driving, safety
   - 解决问题: 论文关注视觉语言模型在特定下游任务中保留无关领域知识的问题，例如自动驾驶需要识别真实车辆而避免把广告插画误认为真实车辆。
   - 具体方法: 方法提出按领域遗忘的设定，通过领域解耦和逐实例提示等技术，降低模型对指定领域图像的识别能力，同时保持其他领域性能。
   - 分类理由: 虽然方法较通用，但摘要给出的自动驾驶问题落在视觉识别鲁棒性与安全感知上，因此归入感知。

35. **[Learnable Burst-Encodable Time-of-Flight Imaging for High-Fidelity Long-Distance Depth Sensing](https://openreview.net/forum?id=zL4ifL17bU)**
   - 四类分类: `Perception`
   - 相关度: `medium`
   - 技术标签: camera, lidar
   - 解决问题: 论文解决长距离高精度深度成像在光源脉冲宽度和时间数字转换器分辨率上要求过高、难以低成本部署的问题。
   - 具体方法: 作者提出可学习的 burst 编码飞行时间成像机制，通过编码和重建联合优化提高远距离深度测量质量。
   - 分类理由: 该工作不是端到端驾驶策略，而是可服务自动驾驶和机器人远距离深度感知的传感成像方法，因此归入感知，相关性降为中等。


### 规控
1. **[HCRMP: An LLM-Hinted Contextual Reinforcement Learning Framework for Autonomous Driving](https://openreview.net/forum?id=1BOiVpBtZy)**
   - 四类分类: `Planning/Control`
   - 相关度: `high`
   - 技术标签: planning, control, safety
   - 解决问题: 论文关注大语言模型辅助自动驾驶运动规划时可能产生幻觉，从而影响强化学习驾驶策略安全性和可靠性的问题。
   - 具体方法: 方法提出大语言模型提示的上下文强化学习运动规划框架，将语言模型输出作为语义提示用于状态增强和策略优化，同时保持强化学习策略的相对独立性。
   - 分类理由: 论文的目标是运动规划和驾驶策略优化，重点在规控安全与轨迹决策，不是通用端到端驾驶基础模型。

2. **[From Faults to Features: Pretraining to Learn Robust Representations against Sensor Failures](https://openreview.net/forum?id=9aElHWiZ72)**
   - 四类分类: `Planning/Control`
   - 相关度: `high`
   - 技术标签: control, safety, closed-loop, deployment-system-reliability, prediction
   - 解决问题: 论文关注自动驾驶和辅助驾驶中传感器失效会破坏输入信号，进而影响闭环控制可靠性的问题。
   - 具体方法: 方法在预训练阶段模拟常见传感器中断，用自监督掩码恢复原始信号，使模型学到对已见和未见故障更鲁棒的车辆动态表示，并在真实车辆闭环控制中替代物理传感器。
   - 分类理由: 虽然方法涉及表征学习和传感器输入，但验证重点是传感器故障下的闭环控制与安全可靠运行，因此归入规控更合适。

3. **[Predictive Preference Learning from Human Interventions](https://openreview.net/forum?id=ErEaq1UNaQ)**
   - 四类分类: `Planning/Control`
   - 相关度: `high`
   - 技术标签: planning, control, prediction, safety, benchmark
   - 解决问题: 论文解决人类介入式学习中只修正当前动作、难以影响未来高风险状态的问题，目标是让智能体在后续可能危险区域也能学到更安全的行为偏好。
   - 具体方法: 方法把一次人类干预扩展到未来多个时间步，将其转化为偏好监督信号，并在未来状态上进行偏好优化，从而减少人工示范需求并提升安全相关行为学习效率。
   - 分类理由: 论文核心是利用人类干预改进智能体未来动作和安全控制策略，虽然也涉及预测与基准测试，但主要落在决策、规划和控制学习，因此归入规控。

4. **[Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling](https://openreview.net/forum?id=MQVyuWBfSH)**
   - 四类分类: `Planning/Control`
   - 相关度: `high`
   - 技术标签: planning, prediction
   - 解决问题: 论文解决复杂交互驾驶场景中的自动驾驶轨迹规划问题，重点是学习式规划方法难以充分建模车辆之间高价值交互行为。
   - 具体方法: 论文提出基于流匹配的规划框架，将轨迹细粒度切分为重叠片段，并通过时空融合结构和引导式多模态行为生成来建模交互驾驶策略。
   - 分类理由: 论文目标是输出自动驾驶规划轨迹并提升交互场景中的规划表现，方法围绕行为生成和轨迹规划展开，因此归入规控。

5. **[UniMotion: A Unified Motion Framework for Simulation, Prediction and Planning](https://openreview.net/forum?id=Phrzarx9NG)**
   - 四类分类: `Planning/Control`
   - 相关度: `high`
   - 技术标签: planning, prediction, simulation
   - 解决问题: 论文关注自动驾驶中运动仿真、轨迹预测和运动规划被分开建模的问题，这种割裂限制了多任务共享、泛化能力和系统扩展性。
   - 具体方法: 论文提出统一运动框架，使用解码器式变换器建模多智能体交互和时空运动规律，并通过不同交互模式与训练策略同时支持仿真、预测和规划。
   - 分类理由: 虽然覆盖预测和仿真，但论文明确包含轨迹规划并以运动决策任务为核心统一目标，因此按唯一目录归入规控。

6. **[REDOUBT: Duo Safety Validation for Autonomous Vehicle Motion Planning](https://openreview.net/forum?id=lEsvczuPVj)**
   - 四类分类: `Planning/Control`
   - 相关度: `high`
   - 技术标签: planning, safety, closed-loop, deployment-system-reliability
   - 解决问题: 论文解决自动驾驶运动规划安全验证难以同时判断输入场景合理性和规划输出安全性的问题。
   - 具体方法: 作者提出 REDOUBT 双重安全验证框架，分别验证场景输入和规划决策，并面向自动车运动规划的复杂上下文进行适配。
   - 分类理由: 研究对象是自动驾驶车辆运动规划的安全验证，核心落在规控链路的安全部署，因此归入规控。

7. **[Neurosymbolic Diffusion Models](https://openreview.net/forum?id=HfdzglsZQH)**
   - 四类分类: `Planning/Control`
   - 相关度: `medium`
   - 技术标签: planning, prediction, benchmark, safety
   - 解决问题: 论文关注神经符号模型在推理任务中难以刻画符号依赖和不确定性的问题，这会影响路径规划和规则化自动驾驶等场景中的可靠决策。
   - 具体方法: 论文提出神经符号扩散模型，用离散扩散过程建模符号之间的依赖关系，并在每一步复用较简单的独立性假设，从而兼顾可扩展学习、不确定性估计和校准能力。
   - 分类理由: 摘要中与自动驾驶最直接相关的是视觉路径规划和基于规则的驾驶决策评测，重点落在规划推理和决策可靠性，而不是传感器感知或数据集构建，因此归入规控。


### 数据&仿真
1. **[RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation](https://openreview.net/forum?id=EATkC9iHE3)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: simulation, dataset, benchmark, 3d-detection, occupancy
   - 解决问题: 论文解决自动驾驶合成视频数据存在几何畸变的问题，这类畸变会削弱合成数据对下游三维检测等感知任务的训练价值。
   - 具体方法: 论文提出一种带几何反馈的强化学习优化方法，用自动驾驶感知模型提供潜空间奖励，引入窗口化优化和分层几何奖励，约束点、线、面一致性以及场景占用一致性，并用几何评分量化失真程度。
   - 分类理由: 虽然评估涉及三维检测和占用一致性，但论文主体是改进自动驾驶视频生成与合成数据质量，属于数据生成和仿真评测方向，因此唯一归入数据与仿真目录。

2. **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://openreview.net/forum?id=FeUGQ6AiKR)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: simulation, camera
   - 解决问题: 论文解决大规模动态驾驶场景中四维重建难以扩展、依赖标注或逐场景优化的问题。
   - 具体方法: 方法直接从视觉观测预测三维高斯及其运动动态，通过光度损失和尽量静态的正则约束，在无监督条件下分解动态元素并重建驾驶场景。
   - 分类理由: 核心目标是为大规模驾驶场景生成可泛化的动态四维重建表示，更接近数据资产构建和仿真场景重建，而不是在线感知或规划控制。

3. **[Multimodal LiDAR-Camera Novel View Synthesis with Unified  Pose-free  Neural  Fields](https://openreview.net/forum?id=GQHUET0V6f)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: simulation, sensor-fusion, lidar, camera
   - 解决问题: 论文解决自动驾驶大规模场景中新视角合成依赖精确位姿、单一模态容易陷入局部最优，以及图像与激光雷达联合生成能力不足的问题。
   - 具体方法: 方法构建无需预先精确位姿的多模态神经场框架，联合图像纹理和激光雷达几何进行渲染监督与位姿优化，实现相机和点云的新视角合成。
   - 分类理由: 核心贡献是用于自动驾驶场景的多模态新视角合成和神经渲染，可用于数据生成与仿真，而不是检测、跟踪等直接感知输出，因此归入数据与仿真目录。

4. **[Overcoming Challenges of Long-Horizon Prediction in Driving World Models](https://openreview.net/forum?id=OACw1Fqy6Y)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: simulation, prediction, camera, foundation-driving-model
   - 解决问题: 论文关注自动驾驶世界模型在长时域生成和复杂交通场景泛化方面的不足，希望模型能够在转弯、城市交通等困难场景中进行稳定的长期视觉滚动预测。
   - 具体方法: 方法基于驾驶视频训练下一帧预测模型，不依赖地图、深度或多相机等额外监督，并比较离散令牌模型与连续自回归生成模型，最终表明连续建模在稳定性和生成能力上更有优势。
   - 分类理由: 论文核心是驾驶世界模型的长时域场景生成和滚动预测，可用于仿真与数据生成评测，并未直接输出自车动作或执行规划控制，因此优先归入数据与仿真。

5. **[LabelAny3D: Label Any Object 3D in the Wild](https://openreview.net/forum?id=Q2fU0JDHuW)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: 3d-detection, dataset, benchmark, camera
   - 解决问题: 论文解决开放世界单目三维检测缺少大规模三维标注数据和通用评测基准的问题。
   - 具体方法: 方法提出基于分析合成的三维自动标注框架，从二维图像重建完整三维场景并生成高质量三维框，同时构建面向开放词汇单目三维检测的新基准。
   - 分类理由: 论文核心贡献是三维标注生成流程和新的三维检测数据集基准，虽服务于感知任务，但正文目录应归入数据与评测方向。

6. **[Genesis: Multimodal Driving Scene Generation with Spatio-Temporal and Cross-Modal Consistency](https://openreview.net/forum?id=Q7YnqREWLq)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: simulation, dataset, benchmark, lidar, camera, bev, 3d-detection
   - 解决问题: 论文解决自动驾驶多模态场景数据生成中视频与激光雷达序列在时空一致性和跨模态一致性上不足的问题。
   - 具体方法: 方法构建统一世界模型，联合生成多视角驾驶视频和激光雷达序列，并利用视觉语言标注模块提供场景级与实例级语义条件。
   - 分类理由: 核心贡献是合成驾驶场景数据与多模态生成系统，尽管可辅助检测和分割等下游任务，但正文目录应归入数据与仿真。

7. **[X-Scene: Large-Scale Driving Scene Generation with High Fidelity and Flexible Controllability](https://openreview.net/forum?id=QclFsekj9B)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: simulation, dataset, occupancy, closed-loop
   - 解决问题: 论文解决大规模三维驾驶场景生成需要同时满足高保真、空间一致性和可控编辑的问题。
   - 具体方法: 作者提出 X-Scene，用扩散式场景生成和可控结构约束生成高质量驾驶场景，支持仿真、数据合成和闭环评测。
   - 分类理由: 核心贡献是驾驶场景生成与合成数据能力，而不是传统规控算法，因此归入数据与仿真。

8. **[Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding](https://openreview.net/forum?id=SoqzNbcBjy)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: simulation, dataset, benchmark, lidar
   - 解决问题: 论文关注激光雷达场景生成中语义标签缺失和几何语义一致性不足的问题，希望生成既包含深度与反射强度又包含语义信息的标注雷达场景数据。
   - 具体方法: 论文提出一种语义感知的渐进式激光雷达扩散生成模型，在距离视图表示下同时生成深度、反射强度和语义图，并设计新的语义感知指标评估生成质量。
   - 分类理由: 尽管方法涉及语义理解和激光雷达表征，但论文主线是生成带标签的雷达场景数据及其评测，更符合数据生成与仿真目录，而不是在线感知模型。

9. **[ReSim: Reliable World Simulation for Autonomous Driving](https://openreview.net/forum?id=T0CiI4gDFB)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: simulation, prediction, planning, safety
   - 解决问题: 论文解决驾驶世界模型在不同自车行为条件下生成未来场景时可靠性不足、难以支持安全测试的问题。
   - 具体方法: 作者提出可由多种动作条件精确控制的可靠驾驶世界仿真模型，用于生成真实且行为一致的未来驾驶视频和场景。
   - 分类理由: 核心贡献是自动驾驶世界模型和场景仿真能力，服务训练、测试和安全验证，因此归入数据与仿真。

10. **[3D-Agent: A Tri-Modal Multi-Agent Responsive Framework for Comprehensive 3D Object Annotation](https://openreview.net/forum?id=YGIbwfNWot)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, lidar, vlm-driving
   - 解决问题: 论文关注三维物体标注中的空间复杂、遮挡和视角不一致问题，这类高质量三维标注对自动驾驶等场景的数据生产有价值。
   - 具体方法: 方法将多视角二维图像、文本描述和三维点云结合起来，用多个专门智能体分别生成描述、聚合信息并对齐文本与三维几何，从而提升标注质量和吞吐量。
   - 分类理由: 核心贡献是提升三维对象标注与数据处理流程，而不是直接做感知模型、规划控制或端到端驾驶，因此归入数据与仿真。

11. **[Adv-BMT: Bidirectional Motion Transformer for Safety-Critical Traffic Scenario Generation](https://openreview.net/forum?id=avZ01E4aYt)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, prediction, safety, simulation
   - 解决问题: 论文解决自动驾驶系统测试中长尾安全关键场景稀缺的问题，尤其是缺少真实且多样的碰撞交互样本。
   - 具体方法: 方法先进行对抗式场景初始化，再用双向运动模型从最后一帧反向预测交通运动，生成多样且真实的危险交互场景。
   - 分类理由: 论文主要目标是生成安全关键交通场景并扩充测试数据，属于场景生成和仿真评测范畴。

12. **[CymbaDiff: Structured Spatial Diffusion for Sketch-based 3D Semantic Urban Scene Generation](https://openreview.net/forum?id=hFyIIqmcqf)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, benchmark, simulation, lidar
   - 解决问题: 论文解决户外三维语义场景生成缺少公开、规范且标注充分的数据集和评测基准的问题。
   - 具体方法: 方法构建从手绘草图生成三维户外语义场景的数据集，并提出基于柱面结构和扩散建模的方法来提升空间连续性、垂直层次和语义一致性。
   - 分类理由: 核心贡献是自动驾驶相关户外三维场景生成数据集、基准和生成方法，属于数据与仿真。

13. **[Towards Physics-informed Spatial Intelligence with Human Priors: An Autonomous Driving Pilot Study](https://openreview.net/forum?id=pEUBqS8nTk)**
   - 四类分类: `Data/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, foundation-driving-model
   - 解决问题: 论文关注基础模型在驾驶场景中空间智能评测不充分的问题，传统问答式评估容易混入语言捷径，难以真实衡量几何和物理空间理解能力。
   - 具体方法: 论文提出网格化空间表示，将物体布局、相互关系和物理先验编码为结构化信息，并构建驾驶场景基准用于评估多模态大模型的空间智能。
   - 分类理由: 主要贡献是面向驾驶场景的评测表示、指标和基准数据，而不是直接感知、规划或端到端驾驶控制，因此归入数据与仿真。

14. **[Neural Atlas Graphs for Dynamic Scene Decomposition and Editing](https://openreview.net/forum?id=pkuVonMwhT)**
   - 四类分类: `Data/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, simulation
   - 解决问题: 论文关注动态场景的高分辨率可编辑表示问题，尤其是在多物体遮挡和交互复杂时，传统二维图层式表示难以稳定分解和编辑场景。
   - 具体方法: 论文提出神经图谱图表示，将场景图节点与视角相关的神经图谱结合，使每个节点既能进行二维外观编辑，又能表达三维排序和位置关系，并在自动驾驶数据集上验证效果。
   - 分类理由: 该工作虽然使用自动驾驶数据集并涉及动态场景，但核心目标是场景表示、编辑和可生成资产能力，更接近数据构建与仿真内容生成，而不是直接的感知、规控或端到端驾驶。

15. **[MuSLR: Multimodal Symbolic Logical Reasoning](https://openreview.net/forum?id=uWEcZkrSkZ)**
   - 四类分类: `Data/Simulation`
   - 相关度: `medium`
   - 技术标签: benchmark, vlm-driving, safety
   - 解决问题: 论文关注多模态模型在自动驾驶、医疗等高风险场景中进行形式逻辑推理时缺少系统评测的问题。
   - 具体方法: 作者构建 MuSLR 多模态符号逻辑推理基准，用视觉、文本和逻辑规则检验模型能否可靠推出新事实。
   - 分类理由: 贡献是面向 VLM 推理能力的评测基准，自动驾驶只是重要应用场景之一，因此归入数据与仿真，相关性为中等。


## 抓取状态

- `neurips_virtual_page`: ok / html / 5858 poster links
- `openreview`: ok / api2 / 5286 篇
- `classifier`: partial_fallback_rules_manual_patched / traecli / selected 73 / rejected 5213
- `prefilter`: autonomous-driving-rules / candidates 87 / cheap_rejected 5199
- `traecli`: model GPT-5.5 / thinking high / verbosity high / calls 7 / cache_hits 38 / batch 8 / summary_limit 1200
- `manual_patch`: patched 7 / rejected 1
- `errors`:
  - autonomous-driving batch size=8 failed: missing ids: ['25C8oC1pb2', 'lNPo3FAMsl', 'M4Laq0Y5WG', 'Q2fU0JDHuW', 't7NLyOtPEi']
  - autonomous-driving batch size=4 failed: missing ids: ['t7NLyOtPEi', 'j7L5AiVqJQ', 'zL4ifL17bU', 'gEpXPbX8VV']
  - autonomous-driving batch size=2 failed: missing ids: ['zL4ifL17bU', 'gEpXPbX8VV']
  - autonomous-driving batch size=1 failed: missing ids: ['zL4ifL17bU']
  - autonomous-driving batch size=8 failed: Expecting value: line 1 column 1 (char 0)
  - autonomous-driving batch size=4 failed: missing ids: ['uWEcZkrSkZ', 'kYisDXzTk7', 'pkuVonMwhT', 'HfdzglsZQH']
  - autonomous-driving batch size=2 failed: missing ids: ['uWEcZkrSkZ', 'kYisDXzTk7']
  - autonomous-driving batch size=1 failed: missing ids: ['uWEcZkrSkZ']
