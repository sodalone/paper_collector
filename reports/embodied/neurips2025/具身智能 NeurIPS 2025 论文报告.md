# 具身智能 NeurIPS 2025 论文报告

- 来源: [NeurIPS 2025 Virtual Papers](https://neurips.cc/virtual/2025/loc/san-diego/papers.html)
- OpenReview 查询: `content.venueid=NeurIPS.cc/2025/Conference`
- 生成时间: 2026-06-28 20:55:04
- 全量论文数: 5286
- 规则预筛候选: 725
- 二次分类输入: 372
- 候选论文数: 319
- 拒绝论文数: 4967
- 高相关: 200
- 中相关: 103
- 低相关: 16
- 主贡献分布: Policy/Control/Planning 110, World Model/Representation 98, Data/Benchmark/Simulation 47, Foundation/VLA Model 25, Safety/Evaluation 24, Agent/System 15
- 任务分布: General/Cross-task 180, Manipulation 114, Navigation 59, Locomotion 31, HRI 17, Whole-body 12
- 录用类型分布: NeurIPS 2025 poster 255, NeurIPS 2025 spotlight 53, NeurIPS 2025 oral 11

## 统计概览

- 候选论文数: 319
- 高相关: 200
- 中相关: 103
- 低相关: 16
- 主贡献分布: Policy/Control/Planning 110, World Model/Representation 98, Data/Benchmark/Simulation 47, Foundation/VLA Model 25, Safety/Evaluation 24, Agent/System 15
- 任务分布: General/Cross-task 180, Manipulation 114, Navigation 59, Locomotion 31, HRI 17, Whole-body 12
- 录用类型分布: NeurIPS 2025 poster 255, NeurIPS 2025 spotlight 53, NeurIPS 2025 oral 11

## Embodied Task 索引

### Navigation
1. **[GTR-Loc: Geospatial Text Regularization Assisted Outdoor LiDAR Localization](https://openreview.net/forum?id=2Y2m0DZBfL)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: navigation, deployment-system-reliability, dataset
   - 解决问题: 论文解决大规模户外激光雷达定位中几何特征相似导致的位置歧义问题。
   - 具体方法: 方法生成与位姿相关的地理文本描述，并把文本嵌入与激光雷达特征动态对齐，再通过蒸馏实现推理阶段仅用激光雷达定位。
   - 分类理由: 核心是机器人户外定位表征增强，任务轴应归为导航。

2. **[Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy](https://openreview.net/forum?id=3XuUnUEI7e)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, navigation
   - 解决问题: 并行遍历搜索生成的候选轨迹可能过于相似，导致区域覆盖和搜索效率不足。
   - 具体方法: 方法在轨迹搜索中引入签名核增强路径差异，并给出无导数进化策略形式以支持黑箱目标和批量评估。
   - 分类理由: 核心是机器人探索轨迹规划，实验覆盖平面搜索、四旋翼覆盖和模型预测控制。

3. **[BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation](https://openreview.net/forum?id=7AMriz7I3K)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, spatial-memory, planning, benchmark
   - 解决问题: 零样本目标导航中，大模型常贪心选择下一目标，缺少全局空间理解和目标位置后验维护。
   - 具体方法: 方法构建三维体素信念图，将语言语义先验、视觉嵌入和实时观测融合为目标位置后验，并结合序列路径规划。
   - 分类理由: 论文直接针对对象导航系统，主贡献是导航中的空间信念建图与规划。

4. **[Memo: Training Memory-Efficient Embodied Agents with Reinforcement Learning](https://openreview.net/forum?id=9eIntNc69t)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, spatial-memory, benchmark
   - 解决问题: 论文解决长程具身决策中视觉输入超出变换器上下文限制、历史信息难以压缩利用的问题。
   - 具体方法: 方法在强化学习训练中交错插入周期性摘要记忆标记，使策略能够创建和检索情景记忆。
   - 分类理由: 核心贡献是具身智能体记忆增强策略，并在室内多对象导航任务中验证。

5. **[NFL-BA: Near-Field Light Bundle Adjustment for SLAM in Dynamic Lighting](https://openreview.net/forum?id=AmZ7uHDJiR)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: navigation, world-model, dataset
   - 解决问题: 论文解决相机与光源共置时动态近场照明带来的视角相关阴影会破坏定位和建图的问题。
   - 具体方法: 方法把近场光照显式写入束调整损失，可集成到神经渲染式同步定位建图系统中提升跟踪和地图质量。
   - 分类理由: 核心是机器人和医疗内窥镜导航中的建图表示问题，属于具身导航感知基础能力。

6. **[Video Perception Models for 3D Scene Synthesis](https://openreview.net/forum?id=D0YNbanYfB)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, sim2real
   - 解决问题: 现有三维场景合成依赖语言模型或图像生成先验，常存在空间推理不足、布局不连贯和多视角不一致问题。
   - 具体方法: 结合视频生成、前馈三维重建和开放词表感知模型，从文本或图像提示生成具有语义与几何一致性的三维场景。
   - 分类理由: 论文明确服务机器人仿真和三维场景世界构建，属于具身环境表示方向。

7. **[DynaNav: Dynamic Feature and Layer Selection for Efficient Visual Navigation](https://openreview.net/forum?id=D4j2K5lknb)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, robot-foundation-model, deployment-system-reliability, dataset, benchmark
   - 解决问题: 视觉导航中的基础模型尤其是带解码器的模型计算开销大、可解释性弱，限制了机器人端侧部署。
   - 具体方法: 论文提出可训练硬特征选择器和早退机制，并用贝叶斯优化确定退出阈值，使模型按场景复杂度选择特征与层数。
   - 分类理由: 核心改进服务于视觉导航策略的高效推理与部署，任务轴明确是导航，因此主类更偏策略控制规划而非通用基础模型。

8. **[WALL-E: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents](https://openreview.net/forum?id=DorAT49sxj)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, spatial-memory
   - 解决问题: 论文要解决大语言模型作为世界模型时，其先验知识与具体环境动力学不匹配，导致智能体在新环境中预测不准、规划效率低的问题。
   - 具体方法: 方法从探索轨迹中抽取动作规则、知识图谱和场景图等符号知识，并编码为可执行约束来对齐世界模型；随后在模型预测控制框架中，让大语言模型智能体与神经符号世界模型交互，进行前瞻式动作选择。
   - 分类理由: 核心贡献是为具身智能体构建和对齐环境世界模型，并在类似我的世界的开放环境与室内具身任务中验证了导航、交互和任务完成能力，因此主类应归为世界模型与表示。

9. **[Active Test-time Vision-Language Navigation](https://openreview.net/forum?id=EY096v0Jmg)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, hri, benchmark, deployment-system-reliability
   - 解决问题: 离线训练的视觉语言导航策略在新环境部署时容易遇到分布偏移，单纯熵最小化会累积错误自信。
   - 具体方法: 方法通过情节级人机反馈和自主动学习校准导航结果不确定性，并用混合熵优化调整动作偏好和置信度。
   - 分类理由: 任务明确是视觉语言导航，并包含人机反馈机制，主贡献是导航策略的测试时适应。

10. **[SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration](https://openreview.net/forum?id=EyOtIOmMUh)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, sim2real, navigation, planning, hri
   - 解决问题: 论文解决现有机器人仿真和基准偏室内家庭场景、缺少大规模动态城市环境和多机器人协作评估的问题。
   - 具体方法: 方法基于虚幻引擎生成真实感城市、行人和交通系统，并设计多模态指令导航与多机器人搜索协作两类基准任务。
   - 分类理由: 主要贡献是仿真平台和机器人基准，而不是单一策略或模型，因此归为数据基准仿真类。

11. **[SimWorld: An Open-ended Simulator for Agents in Physical and Social Worlds](https://openreview.net/forum?id=FxCy8TvQHO)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, navigation, planning, hri
   - 解决问题: 论文解决现有世界模拟器场景手工化、物理和社会规则简化、对大模型智能体接口支持不足的问题。
   - 具体方法: 方法构建虚幻引擎仿真平台，提供语言驱动程序化环境、多模态反馈和开放词表动作接口，并评测导航与多智能体配送任务。
   - 分类理由: 核心是开放式物理社会仿真与评测环境，具身任务包含导航和社会交互。

12. **[Tree-Guided Diffusion Planner](https://openreview.net/forum?id=I1C0a01BZu)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, planning, manipulation, navigation, locomotion
   - 解决问题: 标准梯度引导扩散规划在非凸目标、不可微约束和多奖励结构中效果下降，且监督规划缺少测试时灵活性。
   - 具体方法: 将测试时规划建模为树搜索，先用免训练粒子引导生成多样父轨迹，再用条件去噪细化子轨迹。
   - 分类理由: 核心是面向控制问题的扩散规划算法，并在操作、导航和运动相关任务上评估。

13. **[MindJourney: Test-Time Scaling with World Models for Spatial Reasoning](https://openreview.net/forum?id=L2W4wQsNkY)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, navigation, manipulation, planning, benchmark
   - 解决问题: 论文解决视觉语言模型缺少三维动态内部模型，难以预测自我运动后的场景变化和进行空间推理的问题。
   - 具体方法: 方法让视觉语言模型规划简洁相机轨迹，由视频扩散世界模型合成各步视角，再基于多视图证据进行推理。
   - 分类理由: 核心是利用世界模型进行测试时空间推理扩展，任务明确关联导航和操作。

14. **[Physics-informed Value Learner for Offline Goal-Conditioned Reinforcement Learning](https://openreview.net/forum?id=LRYgQuz7kY)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, locomotion, planning
   - 解决问题: 离线目标条件强化学习在数据覆盖有限和长程任务中难以学习可泛化的价值函数，尤其在导航和运动等交互数据昂贵的领域。
   - 具体方法: 方法从 Eikonal 偏微分方程推导物理启发的价值学习正则，并将其接入现有离线目标条件强化学习算法以改善代价到达结构。
   - 分类理由: 论文明确面向自主导航和运动控制，核心是价值函数与策略学习改进，因此归为控制与规划。

15. **[EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes](https://openreview.net/forum?id=Lf0W2gmNBg)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: navigation, world-model, benchmark
   - 解决问题: 仅依赖普通相机的三维重建方法在动态物体和极端光照下容易失效，影响导航、定位和重建可靠性。
   - 具体方法: 论文在点图重建骨干上加入图像增强、事件适配器、信噪比感知融合和事件光度一致性损失。
   - 分类理由: 核心贡献是鲁棒三维几何表示与重建，应用场景明确包括导航和定位，因此归为世界模型表示与导航任务。

16. **[Embodied Crowd Counting](https://openreview.net/forum?id=NatwrOmOvM)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: navigation, dataset, benchmark, planning
   - 解决问题: 传统人群计数依赖被动相机，遮挡严重；现有具身导航数据又多为室内小规模场景，难以评估密集人群分析。
   - 具体方法: 论文构建交互式大场景人群计数模拟器和数据集，并提出由多模态大模型驱动的粗到细零样本导航计数基线。
   - 分类理由: 核心贡献是新任务、数据集和基准，具体场景是主动导航中的人群计数，因此归入数据基准仿真与导航。

17. **[Building 3D Representations and Generating Motions From a Single Image via Video-Generation](https://openreview.net/forum?id=QNXWTA7PZS)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, navigation
   - 解决问题: 机器人从单张彩色图像恢复环境几何并生成符合场景的无碰撞运动很困难，单目深度误差会影响后续规划。
   - 具体方法: 方法用视频生成模型从单图合成移动相机视角，再交给三维基础模型生成点云，并训练隐式环境表示和运动生成模型。
   - 分类理由: 核心贡献是环境三维表示与运动生成，直接服务自主机器人运动规划。

18. **[Understanding while Exploring: Semantics-driven Active Mapping](https://openreview.net/forum?id=RkHUDvy9QR)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: spatial-memory, navigation, world-model, dataset
   - 解决问题: 未知环境中的自主机器人需要同时探索和理解几何、语义信息，但观测选择不当会降低建图完整性和鲁棒性。
   - 具体方法: 基于三维高斯建图骨干，估计语义和几何不确定性，并用稀疏语义表示指导最有信息量的视角选择。
   - 分类理由: 论文直接面向机器人主动探索和语义地图构建，是导航场景中的世界表示工作。

19. **[Spatial Understanding from Videos: Structured Prompts Meet Simulation Data](https://openreview.net/forum?id=SBYCu5uJJf)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, dataset, navigation, hri
   - 解决问题: 论文解决预训练视觉语言模型在三维空间关系、场景布局和扫描视频推理中受空间不确定性与数据稀缺限制的问题。
   - 具体方法: 方法结合分解式空间提示策略和由三维仿真场景自动构建的问答数据集，对模型进行提示增强与微调。
   - 分类理由: 主要贡献包含可扩展仿真问答数据和评测验证，面向空间理解这一具身通用能力。

20. **[C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](https://openreview.net/forum?id=SbfdxWibDn)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: navigation, benchmark, spatial-memory
   - 解决问题: 对象导航智能体在动态开放世界中需要不断学习新物体类别，同时避免遗忘已有导航知识。
   - 具体方法: 论文构建持续对象导航评测，并提出特征蒸馏、特征回放和自适应采样来保持表示与策略一致性。
   - 分类理由: 贡献包含新导航基准和持续学习框架，基准建设是推动该方向的核心亮点。

21. **[Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation](https://openreview.net/forum?id=W0sqoTL7rL)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: navigation, world-model, spatial-memory
   - 解决问题: 目标导航智能体需要推断室内未观测区域，但确定性语义地图补全难以表达布局不确定性和泛化。
   - 具体方法: 方法将大语言模型推断的空间先验编码为二维高斯场，注入完整语义地图目标，并训练流模型生成室内语义分布。
   - 分类理由: 核心是用于目标导航的环境想象和语义地图世界表示，任务明确为导航。

22. **[STAIR: Addressing Stage Misalignment through Temporal-Aligned Preference Reinforcement Learning](https://openreview.net/forum?id=WI8rrwYJdT)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, manipulation, planning, hri
   - 解决问题: 论文解决导航、抓取等多阶段任务中，不同阶段片段被错误比较会产生无效偏好反馈并阻碍策略学习的问题。
   - 具体方法: 方法用时间距离对任务阶段进行近似划分，优先比较同阶段片段，并通过对比学习动态适应策略变化。
   - 分类理由: 核心是面向多阶段具身控制任务的偏好强化学习方法，任务明确包含导航和操作。

23. **[Imagine Beyond ! Distributionally Robust Autoencoding for State Space Coverage in Online Reinforcement Learning](https://openreview.net/forum?id=XEGDKcoQQ1)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning
   - 解决问题: 论文解决视觉目标条件强化学习中在线表征容易偏向已访问状态，导致探索和技能覆盖不足的问题。
   - 具体方法: 方法把变分自编码器与分布鲁棒优化结合，通过对训练状态进行对抗加权，推动潜在空间覆盖更完整的状态分布。
   - 分类理由: 核心是在线强化学习中的探索与控制性能提升，实验包含迷宫和机器人控制任务。

24. **[IPFormer: Visual 3D Panoptic Scene Completion with Context-Adaptive Instance Proposals](https://openreview.net/forum?id=Y0hymKkn2a)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: navigation, deployment-system-reliability
   - 解决问题: 论文解决仅用相机进行三维全景场景补全时，固定查询难以根据测试场景动态适配实例的问题。
   - 具体方法: 方法从图像上下文自适应初始化全景实例提案，再通过注意力编码解码推理语义、实例和体素关系，实现高效三维补全。
   - 分类理由: 核心贡献是导航相关的三维场景表示与感知，不是策略控制，因此归为世界模型与表示。

25. **[Seeing through Uncertainty: Robust Task-Oriented Optimization in Visual Navigation](https://openreview.net/forum?id=ZTYlxJZF1z)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, planning, deployment-system-reliability
   - 解决问题: 论文解决小样本视觉导航中感知预测噪声大、策略容易过拟合、在未见环境中长程多目标规划不稳的问题。
   - 具体方法: 方法将视觉预测转化为经过校准的凸不确定集合，并把部分可观测规划重写为鲁棒优化问题，使导航策略能根据不确定性约束做决策。
   - 分类理由: 核心贡献是面向视觉导航的鲁棒任务级优化与规划，而不是新数据集或纯感知模型，因此归为控制规划类。

26. **[Efficient Safe Meta-Reinforcement Learning: Provable Near-Optimality and Anytime Safety](https://openreview.net/forum?id=ZtKXAbHQ43)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: safety, locomotion, navigation, planning, benchmark
   - 解决问题: 智能体在适应未见任务时需要保持安全约束始终满足，但现有安全元强化学习在效率、最优性和随时安全上不足。
   - 具体方法: 论文提出一步闭式安全策略适应和无海森元训练算法，并证明适应过程中的安全性和近最优性。
   - 分类理由: 安全保证是论文核心贡献，实验覆盖运动和导航基准，因此主类应为安全评估，任务轴包含导航与移动。

27. **[SEEA-R1: Tree-Structured Reinforcement Fine-Tuning for Self-Evolving Embodied Agents](https://openreview.net/forum?id=dAwKePZvcN)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: planning, benchmark, robot-foundation-model
   - 解决问题: 具身多步任务中间奖励稀缺，手工奖励函数又难以泛化，限制智能体自我改进能力。
   - 具体方法: 框架将蒙特卡洛树搜索融入组相对策略优化形成树结构训练信号，并用多模态生成式奖励模型跨任务估计奖励，实现无需真实奖励的自演化。
   - 分类理由: 论文明确面向具身智能体自我进化和长程任务，核心是智能体训练框架而非单纯控制策略。

28. **[SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://openreview.net/forum?id=dt940loCBT)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: vla, safety, manipulation, benchmark, deployment-system-reliability
   - 解决问题: 视觉语言动作模型真实部署时可能伤害环境、机器人或人类，需要把安全约束系统性地融入策略优化。
   - 具体方法: 方法将安全需求建模为约束马尔可夫决策过程，主动诱发多样不安全行为，用安全强化学习约束策略，并通过针对性评估保证安全性。
   - 分类理由: 虽然对象是视觉语言动作模型，但核心贡献是安全约束、风险诱发和安全保证流程，因此主类为安全评估；任务为移动操作。

29. **[Non-Line-of-Sight 3D Reconstruction with Radar](https://openreview.net/forum?id=f4Wd385vHi)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, dataset, navigation
   - 解决问题: 论文解决复杂遮挡环境中机器人只能检测隐藏物体、难以重建完整视线外三维场景的问题。
   - 具体方法: 方法先生成多返回高分辨率距离图，再用物理引导架构建模射线交互，把镜像观测映射到真实位置。
   - 分类理由: 论文部署在移动机器人上并重建遮挡场景，核心是具身环境表示和导航感知。

30. **[World-aware Planning Narratives Enhance Large Vision-Language Model Planner](https://openreview.net/forum?id=fggSyPPk0K)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: vla, planning, world-model, spatial-memory, navigation, manipulation
   - 解决问题: 论文关注大视觉语言模型在具身任务中难以理解环境上下文、空间关系和多步目标，导致长程交互规划成功率不足的问题。
   - 具体方法: 论文提出世界感知规划叙事增强框架，通过视觉外观建模、空间推理、功能抽象和语法落地四类能力，将原始视觉观察转化为更有环境语义的规划信息，并用课程学习训练和评估模型。
   - 分类理由: 核心贡献是增强模型的具身规划能力，而不是单纯提出新数据集或评测；任务发生在类家庭交互环境中，涉及导航、物体操作和长程任务执行，因此归为规划控制方向且具身相关性高。

31. **[StateSpaceDiffuser: Bringing Long Context to Diffusion World Models](https://openreview.net/forum?id=g52NwTQj0Q)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, navigation, spatial-memory
   - 解决问题: 论文解决动作条件视觉世界模型只依赖近期观测，长时间生成时遗忘早期环境内容并产生场景漂移的问题。
   - 具体方法: 方法把状态空间模型的历史特征注入扩散模型，使其保留完整交互历史，并设计评估协议测试长程内容再现能力。
   - 分类理由: 核心是具身交互场景中的长上下文世界模型，实验包含迷宫导航和三维环境。

32. **[Option-aware Temporally Abstracted Value for Offline Goal-Conditioned Reinforcement Learning](https://openreview.net/forum?id=gfXBNBKx02)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, benchmark, navigation, manipulation
   - 解决问题: 离线目标条件强化学习在长程任务中，高层策略容易生成不合适子目标，优势估计符号错误会阻碍层级策略学习。
   - 具体方法: OTA 将选项感知的时间抽象引入时序差分价值更新，缩短有效规划时域，使高层策略获得更清晰的优势估计。
   - 分类理由: 论文在导航和机器人操作环境中验证，核心贡献是层级策略和价值学习，属于控制与规划。

33. **[RLVR-World: Training World Models with Reinforcement Learning](https://openreview.net/forum?id=jpiSagi8aV)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, navigation, manipulation, dataset
   - 解决问题: 世界模型常用最大似然训练，但该目标与转移预测准确性、感知质量等任务指标并不完全一致。
   - 具体方法: 框架将世界建模表述为令牌序列自回归预测，并用解码后的预测质量作为可验证奖励，通过强化学习直接优化语言和视频世界模型。
   - 分类理由: 核心贡献是世界模型后训练范式，且应用明确包含导航和机器人操作，因此与具身智能高度相关。

34. **[Heterogeneous Graph Transformers for Simultaneous Mobile Multi-Robot Task Allocation and Scheduling under Temporal Constraints](https://openreview.net/forum?id=k1fbdnwjCH)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning
   - 解决问题: 论文解决异构移动机器人团队在时间约束下进行任务分配和调度时规模扩展困难的问题。
   - 具体方法: 方法构建异构图变换器，同时编码机器人能力、行驶时间、时空约束和任务依赖，并用强化学习训练一次性决策模型。
   - 分类理由: 核心贡献是多机器人任务规划和调度决策，任务场景属于移动机器人系统。

35. **[NavBench: Probing Multimodal Large Language Models for Embodied Navigation](https://openreview.net/forum?id=nf8PKQKtl2)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, navigation, deployment-system-reliability
   - 解决问题: 论文解决多模态大模型在具身环境中理解导航指令、估计进度和逐步执行能力缺乏系统评估的问题。
   - 具体方法: 方法构建包含导航理解和逐步执行的零样本基准，并提供将模型输出转换为机器人动作的部署管线。
   - 分类理由: 核心贡献是导航基准和执行评测，任务明确属于具身导航。

36. **[EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval](https://openreview.net/forum?id=qMm7tC1zvj)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: navigation, spatial-memory, planning, deployment-system-reliability, benchmark
   - 解决问题: 现有语言模型驱动的物体目标导航依赖云端大模型，小模型难以理解长导航地图提示且端侧规划延迟高。
   - 具体方法: 论文提出语义感知记忆检索、离散记忆缓存和注意力式聚类，以裁剪导航地图并复用缓存。
   - 分类理由: 贡献是完整端侧导航智能体系统的效率优化，而不仅是单一策略网络，因此主类归为智能体系统。

37. **[AC-DiT: Adaptive Coordination Diffusion Transformer for Mobile Manipulation](https://openreview.net/forum?id=qjee4tiBGZ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, whole-body, navigation, vla
   - 解决问题: 移动操作中底盘运动会影响机械臂控制，而不同阶段对二维语义和三维几何感知的需求也不同。
   - 具体方法: 方法先提取底盘运动表征作为全身动作预测的上下文先验，并根据阶段动态融合二维图像和三维点云特征。
   - 分类理由: 核心贡献是端到端移动操作中的全身协调策略，覆盖导航式底盘运动和机械臂操作。

38. **[Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation](https://openreview.net/forum?id=s6k9l5yX8e)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: navigation, spatial-memory, world-model, robot-foundation-model
   - 解决问题: 视觉语言导航模型在真实三维环境中常缺少几何语义理解、长期环境记忆和动态更新能力。
   - 具体方法: 方法把二维视觉语言特征投影到三维空间，构建补丁、实例和区域多层三维标记，并在线分层更新用于导航动作预测。
   - 分类理由: 核心贡献是导航所需的三维空间表征与记忆机制，任务明确为视觉语言导航。

39. **[Constrained Diffusers for Safe Planning and Control](https://openreview.net/forum?id=tahkGZjjWA)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: diffusion-policy, planning, safety, locomotion, navigation
   - 解决问题: 扩散模型可生成多模态轨迹，但在受约束规划和在线控制中难以保证安全约束满足。
   - 具体方法: 方法在反向扩散采样中加入约束朗之万优化，并结合投影、原始对偶、增广拉格朗日和离散控制屏障函数。
   - 分类理由: 核心关注安全规划控制，实验覆盖迷宫、运动控制和物理仿真任务。

40. **[Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation](https://openreview.net/forum?id=vNmWbINtwH)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: navigation, dataset, planning
   - 解决问题: 视觉语言导航是长时序动作任务，推理策略在其中的作用尚不清楚，推理还可能在推理时损害导航准确率。
   - 具体方法: 方法比较行动前、行动后和无显式推理等策略，提出训练时吸收结构化推理、推理时直接预测动作的框架，并发布标注数据。
   - 分类理由: 虽然提出策略框架，但数据集和系统评估是关键贡献，任务明确是视觉语言导航。

41. **[OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis](https://openreview.net/forum?id=vSLzoUoJt6)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, manipulation, navigation, planning, dataset
   - 解决问题: 开放世界移动操作需要同时应对开放指令、复杂环境、高层决策和低层控制整合，现有专用模型难以系统泛化。
   - 具体方法: OWMM-Agent 维护多视角场景帧和机器人状态，通过函数调用控制机器人，并用智能体式数据合成流水线微调视觉语言模型以减少领域偏移幻觉。
   - 分类理由: 论文直接面向移动操作机器人，核心是具身基础模型和智能体系统，覆盖导航与操作任务。

42. **[STRIDER: Navigation via Instruction-Aligned Structural Decision Space Optimization](https://openreview.net/forum?id=w0xm9oG8im)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, planning, benchmark
   - 解决问题: 论文解决零样本连续环境视觉语言导航中动作难以同时对齐空间结构和任务意图、长程执行容易偏离的问题。
   - 具体方法: 方法提出结构化航点生成器约束动作空间，并用任务对齐调节器根据进展反馈动态调整行为。
   - 分类理由: 核心贡献是导航智能体的决策空间优化与闭环执行策略，任务轴明确是导航。

43. **[Robust Cross-modal Alignment Learning for Cross-Scene Spatial Reasoning and Grounding](https://openreview.net/forum?id=xjC5NqqSHs)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, dataset, navigation, spatial-memory
   - 解决问题: 现有三维视觉定位通常假设目标位于已知场景内，而真实智能体可能需要在大量未知或曾访问场景中检索并定位目标对象。
   - 具体方法: 论文定义跨场景空间推理定位任务，构建数据集和评测协议，并提出先匹配场景再定位对象的框架，通过全局文本场景对齐和细粒度词物体关联降低搜索成本。
   - 分类理由: 核心贡献是新任务、数据集和基准，同时方法面向具身智能体跨场景空间检索与定位，相关性较高。

44. **[TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making](https://openreview.net/forum?id=xrAqVVk2qe)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: benchmark, navigation, planning, spatial-memory
   - 解决问题: 传统需求驱动导航一次只处理一个需求，难以反映现实生活中多子需求和个人偏好的复杂任务。
   - 具体方法: 构建多需求偏好导航基准，设计由指令分解、目标选择、状态监控、空间记忆地图和双节奏动作生成组成的系统。
   - 分类理由: 论文同时提出导航基准和完整具身代理系统，任务场景明确是长程导航。

45. **[Hierarchical Semantic-Augmented Navigation: Optimal Transport and Graph-Driven Reasoning for Vision-Language Navigation](https://openreview.net/forum?id=ypVW5jvguX)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, planning, spatial-memory, dataset
   - 解决问题: 论文解决连续环境视觉语言导航中长程任务场景理解不足、规划效率低和决策鲁棒性弱的问题。
   - 具体方法: 方法构建动态层级语义场景图，用最优传输拓扑规划选择长期目标，并结合图感知强化学习策略完成低层控制。
   - 分类理由: 论文直接以视觉语言导航为任务，核心贡献是层级语义规划与控制。

46. **[CVGL: Causal Learning and Geometric Topology](https://openreview.net/forum?id=1CqEAuRzHc)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: navigation, spatial-memory
   - 解决问题: 街景和航拍图像视角差异大且存在混杂因素，导致跨视角定位鲁棒性不足。
   - 具体方法: 方法结合因果特征提取、鸟瞰道路拓扑融合和数据自适应池化，以增强稳定语义与几何一致性。
   - 分类理由: 任务服务导航和地图定位，但主要是感知匹配而非机器人闭环控制，因此判为中等相关。

47. **[SegMASt3R: Geometry Grounded Segment Matching](https://openreview.net/forum?id=DI2AAFnLrc)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: robot-foundation-model, navigation, spatial-memory
   - 解决问题: 论文解决大视角变化下图像区域级对应难以保持几何一致、遮挡和光照变化导致匹配不稳的问题。
   - 具体方法: 方法利用三维基础模型的空间先验设计片段匹配架构，在宽基线图像对中建立语义和几何区域对应，并验证其对三维实例映射和导航的帮助。
   - 分类理由: 论文主体是三维几何感知表示，具身价值主要体现在导航和建图下游任务，因此为中等相关。

48. **[Video World Models with Long-term Spatial Memory](https://openreview.net/forum?id=HbTxc6U1fO)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, spatial-memory, dataset
   - 解决问题: 自回归视频世界模型受上下文窗口限制，长程生成中容易忘记此前环境并破坏场景一致性。
   - 具体方法: 设计长期空间记忆的存储和检索机制，并构建用于训练和评估显式三维记忆世界模型的数据集。
   - 分类理由: 核心是世界模型和空间记忆，与具身导航和环境生成相关，但不直接展示机器人控制。

49. **[The Matrix: Infinite-Horizon World Generation with Real-Time Moving Control](https://openreview.net/forum?id=Pe18madbPm)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, sim2real, navigation
   - 解决问题: 论文解决真实连续移动数据难收集、世界生成模型难以长时间高保真且响应式控制的问题。
   - 具体方法: 方法结合有限游戏监督数据和大规模真实无监督视频，训练能在第一或第三人称视角下实时生成可控连续场景的视频世界模拟器。
   - 分类理由: 核心是可交互世界模型和模拟器，具身相关性来自移动控制与场景穿越，但例子偏驾驶和虚拟环境。

50. **[Deep RL Needs Deep Behavior Analysis: Exploring Implicit Planning by Model-Free Agents in Open-Ended Environments](https://openreview.net/forum?id=QD06Qv7O0P)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: planning, world-model, safety
   - 解决问题: 复杂深度强化学习智能体的行为结构难以仅靠奖励曲线解释，尤其在部分可观测开放环境中。
   - 具体方法: 作者构建自然化觅食环境，并用行为和神经动态分析方法揭示循环网络智能体的记忆与规划样行为。
   - 分类理由: 论文偏评估分析框架，环境具有空间探索和风险规避属性，但不是直接机器人系统。

51. **[OptiScene: LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization](https://openreview.net/forum?id=ZnrM5RGrgR)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, spatial-memory
   - 解决问题: 现有室内布局生成方法要么依赖昂贵闭源大模型提示，要么受限于粗糙关系图和小规模数据，难以泛化到多样房间。
   - 具体方法: 论文构建大规模人审合成布局数据集，并训练开源布局生成模型，通过监督微调和多轮偏好优化提升空间一致性和人类偏好对齐。
   - 分类理由: 核心产物是室内场景布局数据与生成模型，对具身环境仿真和导航训练有间接价值，但不是机器人策略本身。

52. **[Struct2D: A Perception-Guided Framework for Spatial Reasoning in MLLMs](https://openreview.net/forum?id=rbIlWjTFKj)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, benchmark, planning, spatial-memory
   - 解决问题: 论文解决多模态大模型在不使用显式三维输入时难以进行相对方向、路线规划和物体 grounding 等空间推理的问题。
   - 具体方法: 方法将鸟瞰图、物体标记、对象元数据和必要的第一视角关键帧组合为提示，并构建自动生成的指令微调数据集。
   - 分类理由: 主要产出是结构化输入框架和大规模调优数据，具身相关性来自路线规划与三维室内场景推理。

53. **[A Snapshot of Influence: A Local Data Attribution Framework for Online Reinforcement Learning](https://openreview.net/forum?id=sYK4yPDuT1)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: safety, navigation, locomotion, benchmark
   - 解决问题: 在线强化学习中数据会随策略更新不断变化，传统固定数据集归因方法难以解释样本对行为和回报的影响。
   - 具体方法: 方法针对近期训练缓冲区建立局部归因框架，用梯度相似度衡量样本对动作和累计回报目标的贡献，并据此过滤经验。
   - 分类理由: 论文是通用在线强化学习解释与训练方法，包含导航和移动基准但不专门面向机器人系统，因此相关性为中等。

54. **[Towards Implicit Aggregation: Robust Image Representation for Place Recognition in the Transformer Era](https://openreview.net/forum?id=uVYqwEgIpE)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: navigation
   - 解决问题: 视觉地点识别通常依赖额外聚合器生成全局描述子，在变换器时代可能存在不必要的复杂性。
   - 具体方法: 在变换器骨干中插入可学习聚合标记，利用自注意力隐式聚合图像块信息，并研究插入位置和初始化策略。
   - 分类理由: 论文主要是地点识别表示方法，与机器人导航定位相关，但不直接研究具身代理决策。

55. **[Reinforcing Spatial Reasoning in Vision-Language Models with Interwoven Thinking and Visual Drawing](https://openreview.net/forum?id=yyWeSAsOhs)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `medium`
   - 技术标签: navigation, planning, benchmark
   - 解决问题: 现有多模态推理方法过度依赖文本链式推理，面对需要几何理解和连续空间跟踪的任务时能力不足。
   - 具体方法: 方法为模型提供边界框标注和辅助线绘制等基础视觉操作，并通过合成冷启动、反思式拒绝采样和强化学习三阶段训练培养空间推理能力。
   - 分类理由: 论文主体是大视觉语言模型空间推理能力增强，包含迷宫导航、多视角和视频推理基准，但不是直接机器人控制论文。

56. **[Equilibrium Policy Generalization: A Reinforcement Learning Framework for Cross-Graph Zero-Shot Generalization in Pursuit-Evasion Games](https://openreview.net/forum?id=z67on2D0j1)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: planning
   - 解决问题: 追逃博弈在图结构变化时通常需要重新求解或微调策略，难以满足实时应用需求。
   - 具体方法: 论文用单图均衡策略作为指导，在多种图结构上训练可泛化强化学习策略，并设计动态规划均衡预言机和分组机制。
   - 分类理由: 追逃博弈与机器人和安全场景相关，但论文主要是图博弈强化学习，不是具体物理机器人实验，因此给中等相关。

57. **[SAVVY: Spatial Awareness via Audio-Visual LLMs through Seeing and Hearing](https://openreview.net/forum?id=zwCb9cKHpd)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: benchmark, spatial-memory, navigation
   - 解决问题: 现有视听大模型和基准多关注静态或二维场景，缺少对动态三维方向、距离和时间定位的系统评估。
   - 具体方法: 论文构建包含同步空间音频的三维问答基准，并通过自我中心空间轨迹估计和动态全局地图构建来回答空间关系问题。
   - 分类理由: 核心贡献是空间推理基准和评测流程，具备具身感知价值，但没有直接机器人任务或控制闭环。

58. **[Modelling the control of offline processing with reinforcement learning](https://openreview.net/forum?id=BFW1fkB8ck)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `low`
   - 技术标签: world-model, planning
   - 解决问题: 论文解决大脑或智能体如何在离线阶段选择记忆重放、抽象和生成式模拟来提升未来行为的问题。
   - 具体方法: 方法训练元控制器在睡眠阶段调度低层智能体的离线学习过程，包括近期记忆学习、世界模型抽象和生成数据学习。
   - 分类理由: 包含迷宫求解等行为任务和世界模型概念，但核心是神经科学建模，不是机器人系统。

59. **[Adaptive Frontier Exploration on Graphs with Applications to Network-Based Disease Testing](https://openreview.net/forum?id=mUJU8LmhZY)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `low`
   - 技术标签: planning, navigation
   - 解决问题: 在图结构上逐步选择相邻节点并获得标签奖励时，需要在未知标签和前沿约束下最大化长期收益。
   - 具体方法: 方法设计基于指数的自适应探索策略，并证明其在森林图上最优，同时在公共健康网络测试中验证。
   - 分类理由: 摘要提到机器人探索作为类比场景，但实验主线是图决策和疾病检测，因此具身相关性较低。


### Manipulation
1. **[OpenHOI: Open-World Hand-Object Interaction Synthesis with Multimodal Large Language Model](https://openreview.net/forum?id=0biUwyjKkm)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, planning, diffusion-policy, robot-foundation-model
   - 解决问题: 现有手物交互合成方法难以处理未见物体、开放词汇指令和多阶段长程操作任务。
   - 具体方法: OpenHOI 使用三维多模态大模型进行可供性定位和任务分解，再用可供性驱动的扩散模型生成交互，并通过物理细化减少穿透和提升对齐。
   - 分类理由: 论文明确服务于灵巧机器人操作，核心在开放指令下的手物交互建模、任务分解与动作序列合成。

2. **[Tru-POMDP: Task Planning Under Uncertainty via Tree of Hypotheses and Open-Ended POMDPs](https://openreview.net/forum?id=1GIQOV3NAj)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation
   - 解决问题: 家庭服务机器人面对模糊人类指令、隐藏物体位置和开放词表对象时，规划空间巨大且不确定。
   - 具体方法: 用大语言模型构造层级假设树和粒子信念，再在开放式部分可观测决策模型中进行贝叶斯信念跟踪和规划。
   - 分类理由: 论文核心是具身服务机器人在不确定环境中的任务规划，并以厨房物体重排为评测场景。

3. **[ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning](https://openreview.net/forum?id=1lyKflUOhp)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, manipulation
   - 解决问题: 现有端到端视觉语言动作模型在机器人微调后容易丢失原视觉语言模型的识别、数学和空间推理能力。
   - 具体方法: 模型采用专家混合结构和三阶段训练流程，使模型同时保持开放世界理解能力并将推理转化为机器人动作。
   - 分类理由: 核心贡献是通用视觉语言动作基础模型，实验包含白板数学匹配和物体拾取等机器人操作场景。

4. **[ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://openreview.net/forum?id=2845H8Ua5D)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, tactile, manipulation, dataset, benchmark, robot-foundation-model
   - 解决问题: 现有视觉语言动作模型在插接等接触丰富任务中缺乏精细力控能力，视觉遮挡或动态不确定时尤其困难。
   - 具体方法: 论文提出力感知混合专家融合模块，将视觉语言嵌入与实时力反馈在动作解码中动态路由融合，并发布力觉数据集。
   - 分类理由: 核心是带力觉模态的视觉语言动作基础模型，任务明确是接触丰富机械臂操作。

5. **[$\textit{HiMaCon:}$ Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data](https://openreview.net/forum?id=2aIoEG2Hwz)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, world-model, sim2real, deployment-system-reliability
   - 解决问题: 机器人操作在不同环境和任务间泛化时，缺少能够捕捉稳定交互模式且不依赖人工语义标注的表征。
   - 具体方法: 方法通过跨模态相关网络发现多传感器中的持久交互模式，并用多时间尺度预测器组织短期动作和长期目标相关的层级表征。
   - 分类理由: 核心贡献是操作概念表征学习，而不是单纯控制器设计；评估直接面向机器人操作并包含仿真与真实部署。

6. **[Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents](https://openreview.net/forum?id=3fDypdR4VN)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, manipulation
   - 解决问题: 现有基于人类动作视频的具身预训练过度依赖目标到达启发，容易把无关末尾帧与语言指令错误关联。
   - 具体方法: AcTOL 将视频看作连续轨迹，既对比帧间语义差异以学习自然顺序，又施加局部布朗桥约束保持中间过渡平滑。
   - 分类理由: 论文面向通用具身智能体的视觉语言预训练，并在模拟和真实机器人操作任务中验证，属于具身基础模型方向。

7. **[Blindfolded Experts Generalize Better:  Insights from Robotic Manipulation and Videogames](https://openreview.net/forum?id=4Hzsuzl76a)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, benchmark, robot-foundation-model
   - 解决问题: 完全知情专家给出的示范可能过于直接，行为克隆后策略缺少探索性，导致未见任务泛化不足。
   - 具体方法: 方法在采集示范时隐藏部分任务信息，迫使专家通过探索完成任务，再克隆这种更具探索性的行为。
   - 分类理由: 核心是模仿学习策略泛化，实验包含真实机器人插孔操作，因此属于操作策略学习。

8. **[Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning](https://openreview.net/forum?id=4asFznbzJg)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, manipulation, action-tokenization, deployment-system-reliability
   - 解决问题: 现有双系统机器人方法把高层推理和低层执行分成独立模型，导致执行模块难以充分利用视觉语言模型知识。
   - 具体方法: 论文提出部分共享参数的统一双系统视觉语言动作模型，并用双感知协同训练兼顾上下文理解和高频动作生成。
   - 分类理由: 研究对象是视觉语言动作基础模型，任务明确为机器人操作，并强调真实和仿真执行效率。

9. **[PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models](https://openreview.net/forum?id=4xvE6Iy77Y)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, manipulation, locomotion, planning, benchmark
   - 解决问题: 偏好强化学习在机器人复杂行为学习中受限于大量人类反馈需求、查询歧义和奖励学习中的信用分配困难。
   - 具体方法: PRIMT 以视觉语言模型和大语言模型进行神经符号融合反馈评估，并结合前瞻轨迹生成、回顾轨迹增强和因果辅助损失改善学习。
   - 分类理由: 论文直接面向机器人操作和运动任务，核心是偏好强化学习策略优化，基础模型用于反馈和数据合成。

10. **[Towards Reliable LLM-based Robots Planning via Combined Uncertainty Estimation](https://openreview.net/forum?id=68OW8tLSh2)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: planning, manipulation, safety
   - 解决问题: 大语言模型会产生幻觉和过度自信计划，现有不确定性估计未充分区分知识不足与任务内在歧义。
   - 具体方法: 提出组合不确定性估计方法，将不确定性分为认知不确定性和内在不确定性，并进一步估计任务清晰度和熟悉度。
   - 分类理由: 核心关注机器人规划可靠性和风险评估，实验包含厨房操作和桌面重排。

11. **[RFMPose: Generative Category-level Object Pose Estimation via Riemannian Flow Matching](https://openreview.net/forum?id=6aaixHco6C)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, sim2real
   - 解决问题: 类别级物体姿态估计面临对称歧义、多假设预测和网络结构专用化问题，影响泛化和仿真到现实迁移。
   - 具体方法: 方法在黎曼流匹配框架下学习确定性姿态轨迹，结合测地插值、双不变度量约束、黎曼最优传输和端到端似然估计处理几何一致性与对称性。
   - 分类理由: 论文核心是机器人操作前置的三维姿态表示与估计，并展示仿真到现实迁移能力，因此归为世界表示。

12. **[ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning](https://openreview.net/forum?id=72UR53jN7T)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, planning, manipulation, robot-foundation-model
   - 解决问题: 现有视觉语言动作模型常端到端映射到动作，缺少显式多步推理，难以适应复杂动态任务变化。
   - 具体方法: 训练多模态大模型生成具身推理计划，并用目标完成度和轨迹一致性构造视觉奖励强化，再将计划压缩为视觉潜变量条件化下游动作模型。
   - 分类理由: 核心贡献是面向视觉语言动作任务的模型框架，同时覆盖规划、少样本适应和机器人操作执行。

13. **[Enhancing LLM Planning for Robotics Manipulation through Hierarchical Procedural Knowledge Graphs](https://openreview.net/forum?id=8LO0vLRXpz)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation
   - 解决问题: 语言模型驱动的机器人操作在复杂任务中常缺乏准确过程知识，且使用大模型能耗和部署成本较高。
   - 具体方法: 论文构建任务、步骤和原子动作三层知识图，并用多智能体自动生成知识结构来辅助语言模型规划。
   - 分类理由: 核心是面向机器人操作的高层任务规划增强方法，因此主类为策略控制规划、任务为操作。

14. **[ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning](https://openreview.net/forum?id=ACagRwCCqu)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, locomotion, manipulation, planning, benchmark
   - 解决问题: 流匹配策略适合连续机器人控制，但确定性路径不利于强化学习探索和稳定似然计算，限制在线微调效果。
   - 具体方法: 方法向流策略的确定性路径注入可学习噪声，将其转化为离散时间马尔可夫过程，从而实现精确似然计算、稳定探索和在线强化学习微调。
   - 分类理由: 论文核心是机器人连续控制策略的在线强化学习微调，实验覆盖腿式运动、状态操作和视觉操作任务。

15. **[Inner Speech as Behavior Guides: Steerable Imitation of Diverse Behaviors for Human-AI coordination](https://openreview.net/forum?id=AwLRF1lZvI)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, hri
   - 解决问题: 论文解决人类行为具有多样性和非马尔可夫性，而现有模仿学习难以捕捉并在推理时精细调控的问题。
   - 具体方法: 方法用视觉语言模型生成内在语句作为行为意图表示，再训练条件变分自编码器和扩散行为克隆策略按该意图选动作。
   - 分类理由: 核心贡献是可控模仿策略，实验包含机器人操作和人机协作任务。

16. **[Convergent Functions, Divergent Forms](https://openreview.net/forum?id=B6DhWv3DZo)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, manipulation, sim2real
   - 解决问题: 传统形态控制协同设计需要大量仿真训练，且容易陷入形态多样性不足和泛化差的问题。
   - 具体方法: 方法在学习的形态潜空间中为相似设计复用共享控制策略，同时用动态局部搜索替代简单突变来拓展形态探索。
   - 分类理由: 核心是机器人形态和控制策略协同优化，实验涉及运动和下游操作迁移。

17. **[HoloScene: Simulation‑Ready Interactive 3D Worlds from a Single Video](https://openreview.net/forum?id=BOwPpmRgmW)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, sim2real, manipulation, benchmark
   - 解决问题: 论文解决三维重建方法难以同时具备完整几何、物理合理性、对象可交互性和可用于动态仿真的属性的问题。
   - 具体方法: 方法使用交互式场景图表示几何、外观、物理属性和对象关系，并把观测、物理约束和生成先验统一为能量优化目标。
   - 分类理由: 核心是仿真就绪的交互世界表示，而不是数据集本身；操作只是应用示例之一。

18. **[GoalLadder: Incremental Goal Discovery with Vision-Language Models](https://openreview.net/forum?id=BiowiwzQaO)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation
   - 解决问题: 论文解决视觉环境中仅凭语言指令训练强化学习智能体时奖励构造噪声大、反馈需求高的问题。
   - 具体方法: 方法让视觉语言模型比较并排序更接近任务完成的状态，用评分系统缓解噪声，再在学习嵌入空间中驱动智能体接近高分目标。
   - 分类理由: 核心是语言条件的视觉强化学习策略训练，并在机器人操作环境中验证。

19. **[GenPO: Generative Diffusion Models Meet On-Policy Reinforcement Learning](https://openreview.net/forum?id=BmRNz1TpCc)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, locomotion, benchmark
   - 解决问题: 论文解决扩散策略难以用于近端策略优化等在线强化学习框架，尤其是动作似然难以精确计算的问题。
   - 具体方法: 方法构造可逆动作映射和双虚拟动作机制，精确计算动作似然，并用于熵、散度和自适应学习率估计。
   - 分类理由: 论文直接服务机器人任务的在线策略优化，覆盖腿式运动、灵巧操作、机械臂和飞行控制。

20. **[CADGrasp: Learning Contact and Collision Aware General Dexterous Grasping in Cluttered Scenes](https://openreview.net/forum?id=CB8jwNE2vV)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, tactile, world-model, planning, sim2real
   - 解决问题: 杂乱环境中的灵巧抓取受高自由度手、遮挡、碰撞和复杂物体几何影响，稳定无碰撞姿态难以生成。
   - 具体方法: 方法先预测解耦场景且具备接触碰撞信息的稀疏表示，再结合占用扩散、力闭合过滤和能量优化生成抓取姿态。
   - 分类理由: 核心贡献是面向灵巧操作的几何接触表示和抓取生成，评估包含仿真与真实场景。

21. **[WALL-E: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents](https://openreview.net/forum?id=DorAT49sxj)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, spatial-memory
   - 解决问题: 论文要解决大语言模型作为世界模型时，其先验知识与具体环境动力学不匹配，导致智能体在新环境中预测不准、规划效率低的问题。
   - 具体方法: 方法从探索轨迹中抽取动作规则、知识图谱和场景图等符号知识，并编码为可执行约束来对齐世界模型；随后在模型预测控制框架中，让大语言模型智能体与神经符号世界模型交互，进行前瞻式动作选择。
   - 分类理由: 核心贡献是为具身智能体构建和对齐环境世界模型，并在类似我的世界的开放环境与室内具身任务中验证了导航、交互和任务完成能力，因此主类应归为世界模型与表示。

22. **[Predictive Preference Learning from Human Interventions](https://openreview.net/forum?id=ErEaq1UNaQ)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: safety, manipulation, benchmark, hri
   - 解决问题: 交互式模仿学习通常只修正当前状态动作，无法充分影响未来潜在危险状态，导致安全关键区域学习效率低。
   - 具体方法: PPL 将每次人类干预引导为未来若干步的隐式偏好信号，并在未来状态上做偏好优化，以传播专家纠正并减少示教需求。
   - 分类理由: 论文关注人类干预下的安全学习，并在机器人操作基准上验证，核心贡献是安全与人类反馈机制。

23. **[ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning](https://openreview.net/forum?id=EyNzLH7BZK)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, benchmark
   - 解决问题: 现有三维可供性预测依赖固定类别或外部专家提示，难以泛化到多物体和多步语言指令。
   - 具体方法: 将可供性检测建模为语言条件三维分割，利用几何反馈生成视觉提示并迭代细化可供性掩码，同时构建连续隐式可供性场。
   - 分类理由: 核心是面向具身交互的三维可供性表示，任务与操作前的物体交互理解密切相关。

24. **[EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data](https://openreview.net/forum?id=FGMBxzpgis)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, dataset, sim2real
   - 解决问题: 人类第一人称数据丰富，但人与机器人在外观、传感器和运动学上存在域差距，阻碍操作技能迁移。
   - 具体方法: 论文用最优传输度量对齐人类与机器人策略潜空间和动作相关特征，在共同训练中保持对控制有用的信息。
   - 分类理由: 核心贡献是改进机器人操作模仿策略的跨域学习方法，任务明确为单臂和双臂操作。

25. **[Latent Policy Barrier: Learning Robust Visuomotor Policies by Staying In-Distribution](https://openreview.net/forum?id=FUd016XD4d)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, safety
   - 解决问题: 论文解决行为克隆视觉运动策略在分布偏移下容易偏离专家轨迹并失败的问题。
   - 具体方法: 方法把专家示教的潜在嵌入视为安全分布屏障，结合基础扩散策略和动力学模型，在推理时优化未来潜在状态保持在专家分布内。
   - 分类理由: 核心贡献是面向视觉运动控制的鲁棒策略学习，并在仿真和真实操作任务中验证。

26. **[Learning Parameterized Skills from Demonstrations](https://openreview.net/forum?id=FiZ7gadynD)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, benchmark
   - 解决问题: 论文解决从示教中发现技能时容易出现潜变量退化、技能不具备语义和可迁移性的问题。
   - 具体方法: 方法联合学习离散技能选择、连续技能参数和元策略，并结合时间变分推断与信息正则化获得可解释技能。
   - 分类理由: 核心是机器人操作技能学习，并在操作基准中展示抓取等可解释参数化技能。

27. **[MEgoHand: Multimodal Egocentric Hand-Object Interaction Motion Generation](https://openreview.net/forum?id=GGj0QFSo5m)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, manipulation, vla
   - 解决问题: 论文解决第一视角手物交互生成中视角不稳定、自遮挡、透视畸变、对象先验依赖和开环误差累积问题。
   - 具体方法: 方法用视觉语言模型推断高层运动先验，用单目深度支持空间推理，再用基于流匹配的低层策略生成细粒度手部轨迹，并统一整理大规模数据集。
   - 分类理由: 核心同时包含手物交互数据和运动生成，直接服务机器人模仿与操作学习。

28. **[Improving Generative Behavior Cloning via Self-Guidance and Adaptive Chunking](https://openreview.net/forum?id=GctsZXLCpl)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, planning
   - 解决问题: 论文解决扩散行为克隆中开环动作分块容易因随机采样出错、且对动态扰动响应滞后的问题。
   - 具体方法: 方法提出自引导机制利用过去观测提高动作保真度，并用自适应分块在需要反应性时选择性更新动作序列。
   - 分类理由: 核心贡献是机器人操作策略学习和执行机制优化，属于控制规划。

29. **[Toward Artificial Palpation: Representation Learning of Touch on Soft Bodies](https://openreview.net/forum?id=HtwKJQzt7R)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: tactile, dataset, manipulation
   - 解决问题: 人工触诊高度依赖人类经验，机器人需要从触觉序列中学习软体内部结构和变化信息。
   - 具体方法: 构建仿真环境并采集真实软体触诊数据，用编码器解码器从触觉序列中学习表示，并用于触觉成像和变化检测。
   - 分类理由: 论文以装有触觉传感器的机器人采集和理解软体对象为核心，属于触觉操作感知表示。

30. **[Tree-Guided Diffusion Planner](https://openreview.net/forum?id=I1C0a01BZu)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, planning, manipulation, navigation, locomotion
   - 解决问题: 标准梯度引导扩散规划在非凸目标、不可微约束和多奖励结构中效果下降，且监督规划缺少测试时灵活性。
   - 具体方法: 将测试时规划建模为树搜索，先用免训练粒子引导生成多样父轨迹，再用条件去噪细化子轨迹。
   - 分类理由: 核心是面向控制问题的扩散规划算法，并在操作、导航和运动相关任务上评估。

31. **[Focus-Then-Reuse: Fast Adaptation in Visual Perturbation Environments](https://openreview.net/forum?id=I4fBSpDOha)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, sim2real, robot-foundation-model
   - 解决问题: 从仿真训练得到的视觉策略部署到真实复杂环境时，容易受到背景和视觉扰动影响。
   - 具体方法: 论文利用视觉语言模型先验和环境反馈训练物体选择机制，先聚焦任务相关物体再复用仿真策略。
   - 分类理由: 核心贡献是视觉控制策略的快速适应方法，实验包含控制套件和机械臂任务，因此归为策略控制规划。

32. **[Flattening Hierarchies with Policy Bootstrapping](https://openreview.net/forum?id=KaD2Dw8Ahz)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation, locomotion, benchmark, dataset
   - 解决问题: 离线目标条件强化学习在长时程任务中受稀疏奖励和折扣影响，而层级方法又带来子目标模型和多模块复杂性。
   - 具体方法: 论文通过对子目标条件策略进行自举和优势加权重要性采样，训练扁平目标条件策略，避免显式生成子目标。
   - 分类理由: 核心是长时程控制策略学习，实验覆盖移动和操作基准，因此主类为策略控制规划。

33. **[MindJourney: Test-Time Scaling with World Models for Spatial Reasoning](https://openreview.net/forum?id=L2W4wQsNkY)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, navigation, manipulation, planning, benchmark
   - 解决问题: 论文解决视觉语言模型缺少三维动态内部模型，难以预测自我运动后的场景变化和进行空间推理的问题。
   - 具体方法: 方法让视觉语言模型规划简洁相机轨迹，由视频扩散世界模型合成各步视角，再基于多视图证据进行推理。
   - 分类理由: 核心是利用世界模型进行测试时空间推理扩展，任务明确关联导航和操作。

34. **[HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning](https://openreview.net/forum?id=Mk9ykil8eP)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, benchmark, manipulation, planning, diffusion-policy
   - 解决问题: 论文解决人形机器人双臂和灵巧手操作任务、仿真场景以及高质量示范不足的问题。
   - 具体方法: 方法基于原子灵巧技能和空间标注，用大语言模型生成可执行空间约束链，并结合树搜索增强长程推理和示范采集。
   - 分类理由: 核心贡献是数据生成框架和新基准，虽然涉及规划和扩散策略评估，但主类应为数据基准。

35. **[FreqPolicy: Frequency Autoregressive Visuomotor Policy with Continuous Tokens](https://openreview.net/forum?id=N3UNXzWRRG)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, action-tokenization, benchmark
   - 解决问题: 机器人操作需要精确而高效地产生动作，现有动作表示和网络结构难以充分刻画运动的层级频率结构。
   - 具体方法: 论文把动作分解到频域，逐步建模低频全局运动和高频局部细节，并用连续潜在表示保持动作空间平滑性。
   - 分类理由: 核心贡献是机器人操作动作表示和策略生成方法，因此归为策略控制规划，技术标签包含动作标记化。

36. **[AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models](https://openreview.net/forum?id=N5vXT7AGuo)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, hri, world-model, planning, dataset
   - 解决问题: 现有方法多停留在物体级理解，缺少按指令定位可操作部件并推断运动方式和运动轴的细粒度推理。
   - 具体方法: 方法将三维场景渲染成环绕视图并投影候选元素，使用多模态大模型进行主动视角选择和逐步可供性推理。
   - 分类理由: 核心是三维具身可供性表征与推理，虽然不是直接控制策略，但与操作和人机协作密切相关。

37. **[FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency](https://openreview.net/forum?id=NKNryrCGYn)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, vla, diffusion-policy, deployment-system-reliability, benchmark
   - 解决问题: 生成式视觉运动策略多步采样开销高，而机器人动作轨迹又需要时间连续性和相干性。
   - 具体方法: 论文为流式视觉运动策略加入频域一致性约束和自适应一致性损失，使一步动作生成接近目标分布并保持时序结构。
   - 分类理由: 核心是机器人操作策略的高效动作生成，并可集成到视觉语言动作模型中，因此主类为策略控制规划。

38. **[ROVER: Recursive Reasoning Over Videos with Vision-Language Models for Embodied Tasks](https://openreview.net/forum?id=NNiwGUY50Y)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: manipulation, planning, dataset
   - 解决问题: 具身任务需要模型理解连续视觉流中的长视频轨迹，但现有视觉语言模型在长序列视频推理中容易幻觉且效率较低。
   - 具体方法: 框架将长程视频轨迹递归分解为较短子任务片段，使模型在保留全局上下文的同时聚焦局部帧序列，并可使用子任务滑动窗口降低复杂度。
   - 分类理由: 论文明确服务于具身任务视频理解，并在开放具身视频和机器人操作数据上评估；核心是推理系统而非控制器。

39. **[RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics](https://openreview.net/forum?id=OGxalNUHbJ)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, vla, spatial-memory, dataset, benchmark, manipulation, whole-body
   - 解决问题: 现有视觉语言模型难以在复杂三维场景中准确理解指令指向的位置，并进行动态多步空间推理。
   - 具体方法: 模型通过专门深度编码器监督微调获得精确空间理解，再用带度量敏感过程奖励的强化微调提升多步指代推理，并配套大规模数据集和基准。
   - 分类理由: 核心是机器人场景中的三维空间视觉语言基础模型，同时提供数据与基准；可用于机械臂和人形机器人控制，因此主类为基础模型。

40. **[Time Reversal Symmetry for Efficient Robotic Manipulations in Deep Reinforcement Learning](https://openreview.net/forum?id=OfMCET0hqJ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, benchmark
   - 解决问题: 机器人操作中常见开关门等时间对称任务，但现有强化学习主要利用空间对称性，忽视了时间结构。
   - 具体方法: 提出时间反演增强强化学习，通过可逆轨迹的数据增强和基于反向任务成功轨迹的奖励塑形来加速学习。
   - 分类理由: 论文重点是改进机器人操作策略学习过程，实验也集中在操作基准上的单任务和多任务强化学习。

41. **[DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge](https://openreview.net/forum?id=PK07eretkF)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, world-model, planning, manipulation, diffusion-policy
   - 解决问题: 现有视觉语言动作模型依赖图像级未来预测，信息冗余且缺少关键动态、空间和语义世界知识。
   - 具体方法: 方法构建感知、预测、动作闭环，预测动态区域引导的多模态世界知识，并用结构化注意力和扩散变换器生成未来动作。
   - 分类理由: 核心是面向机器人操作的视觉语言动作基础模型，同时引入世界知识预测支持规划。

42. **[VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models](https://openreview.net/forum?id=PQYazNKEYo)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: vla, planning, manipulation, benchmark
   - 解决问题: 现有视觉语言动作模型的规划范式、表征和数据来源差异很大，难以判断性能增益来自哪个组件。
   - 具体方法: 构建统一视觉语言动作架构套件，在控制变量下比较语言规划、视觉规划、层级范式等不同设计，并覆盖多物体、多模态、多环境和多末端执行器。
   - 分类理由: 论文核心是视觉语言动作模型规划机制的结构化评估，任务明确为复杂长程机器人操作。

43. **[Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies](https://openreview.net/forum?id=PWRORdXJN1)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, benchmark
   - 解决问题: 现有模仿学习常将感知表征和动作生成分离，忽略动作执行会反过来改变后续感知的因果闭环。
   - 具体方法: 方法用动作引导的随机微分方程更新潜在观测，并通过扩散策略噪声预测梯度和循环一致对比损失连接感知与动作。
   - 分类理由: 论文核心是机器人操作扩散策略，评估包含仿真和真实机械臂操作。

44. **[Scaffolding Dexterous Manipulation with Vision-Language Models](https://openreview.net/forum?id=PdRf0O7baQ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, planning, sim2real
   - 解决问题: 灵巧手操作难以收集演示且控制维度高，强化学习又依赖任务特定奖励或难以获得的参考轨迹。
   - 具体方法: 方法让现成视觉语言模型根据任务和图像识别关键点并生成手和物体的粗三维轨迹，随后在仿真中训练低层残差强化学习策略跟踪这些支架轨迹。
   - 分类理由: 论文直接面向灵巧机器人操作策略学习，高层规划和低层控制结合清晰，因此归入策略控制规划。

45. **[Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation](https://openreview.net/forum?id=PtGMadeONU)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: tactile, manipulation, sim2real, dataset
   - 解决问题: 论文解决视觉触觉传感器物理特性复杂、缺少高效准确仿真工具导致触觉机器人研究难以扩展的问题。
   - 具体方法: 方法结合接触物理和仿射体动力学高并行模拟机器人、触觉传感器和物体，并在识别、抓取和关节物体操作中验证仿真到现实迁移。
   - 分类理由: 主要贡献是触觉机器人仿真平台，任务明确覆盖操作与抓取。

46. **[VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching](https://openreview.net/forum?id=QZYZ0Xm58q)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, manipulation, deployment-system-reliability
   - 解决问题: 视觉语言动作模型计算开销大，难以满足机器人实时控制对快速决策的要求。
   - 具体方法: 利用机器人操作视频帧的时间连续性，自适应缓存和复用变化较小的视觉标记，并对任务相关敏感标记选择性重算。
   - 分类理由: 核心是视觉语言动作模型在真实机器人操作中的推理效率和部署可靠性。

47. **[Real-World Reinforcement Learning of Active Perception Behaviors](https://openreview.net/forum?id=RkdTtznSAL)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, planning
   - 解决问题: 机器人在部分可观测环境中需要主动移动来获取缺失信息，但常规机器人学习方法难以稳定学习这种主动感知行为。
   - 具体方法: 方法使用训练时额外传感器学习高质量特权价值函数，再通过非对称优势加权回归从少量演示和粗略初始策略中训练目标策略。
   - 分类理由: 论文直接优化真实机器人操作策略中的主动感知与信息采集行为，属于策略、控制与规划，任务明确为操作。

48. **[RAPID Hand: Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Embodied Intelligence](https://openreview.net/forum?id=T1gVXvbkB1)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: manipulation, tactile, diffusion-policy, deployment-system-reliability
   - 解决问题: 通用机器人自主需要大量真实多指灵巧操作数据，但低成本、高自由度、稳定感知和易遥操作的平台仍然稀缺。
   - 具体方法: RAPID Hand 联合设计二十自由度手、腕部视觉、指尖触觉、本体感知和高自由度遥操作接口，并用采集数据训练扩散策略验证能力。
   - 分类理由: 核心贡献是面向具身智能的硬件软件系统平台，直接服务灵巧操作和数据采集。

49. **[Enhancing Tactile-based Reinforcement Learning for Robotic Control](https://openreview.net/forum?id=Toy96yYopR)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: tactile, manipulation, benchmark, safety
   - 解决问题: 真实机器人操作仅依赖视觉和本体感觉不够安全可靠，而稀疏触觉信号在强化学习中的效果尚不稳定。
   - 具体方法: 论文设计自监督方法利用稀疏二值接触信号，并分析触觉记忆与在线策略记忆解耦对灵巧控制的影响。
   - 分类理由: 贡献围绕触觉机器人控制策略和操作基准，主类是策略控制规划，任务为操作。

50. **[MesaTask: Towards Task-Driven Tabletop Scene Generation via 3D Spatial Reasoning](https://openreview.net/forum?id=U88JlpY0vR)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, manipulation, planning
   - 解决问题: 论文解决机器人根据人类指令执行操作时，缺少与任务相关、布局合理的桌面训练场景问题。
   - 具体方法: 方法构建手工布局的桌面场景数据集，并提出空间推理链，将任务描述分解为对象推断、空间关系推理和场景图生成。
   - 分类理由: 核心是面向机器人桌面操作的数据和场景生成，具身相关性高。

51. **[VideoVLA: Video Generators Can Be Generalizable Robot Manipulators](https://openreview.net/forum?id=UPHlqbZFZB)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, manipulation, world-model, diffusion-policy, robot-foundation-model
   - 解决问题: 现有视觉语言动作模型在新任务、新物体和新环境中的泛化仍有限，缺少对未来视觉结果的联合建模。
   - 具体方法: 基于多模态扩散变换器联合建模视频、语言和动作，输入指令与图像后同时预测动作序列和未来视觉后果。
   - 分类理由: 论文核心是新型视觉语言动作基础模型，任务明确为开放世界机器人操作泛化。

52. **[Real-Time Execution of Action Chunking Flow Policies](https://openreview.net/forum?id=UkR2zO5uww)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: vla, diffusion-policy, action-tokenization, manipulation, benchmark, deployment-system-reliability
   - 解决问题: 动作块策略虽然提升了高频控制的一致性，但模型推理延迟会在动作块边界造成停顿或异常抖动，影响真实机器人执行。
   - 具体方法: 实时动作块方法在执行当前动作块时异步生成下一块动作，对确定会执行的动作进行冻结，并对剩余动作进行补全式更新，可直接用于扩散或流式动作策略。
   - 分类理由: 核心是机器人策略的实时执行与控制算法，不是新基础模型；实验包括动态仿真任务和真实双臂操作任务。

53. **[RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skills](https://openreview.net/forum?id=VZQSrNfNHd)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: manipulation, planning, sim2real
   - 解决问题: 复杂操作任务常需要工具，但人类工具不一定适合机器人使用，现有工具设计方法又受模板或通用三维生成限制。
   - 具体方法: 系统由协作视觉语言模型智能体迭代提出工具设计，在物理仿真中生成低层工具使用轨迹，并联合优化工具几何与使用策略，最后迁移到真实执行。
   - 分类理由: 论文贡献是一个结合智能体、仿真和轨迹优化的端到端工具设计系统，任务明确为复杂机器人操作。

54. **[Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning](https://openreview.net/forum?id=VaC4sa96EI)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, safety, deployment-system-reliability
   - 解决问题: 基于大语言模型的代码即策略方法常因环境 grounding 不足而生成错误或不完整代码，降低任务成功率。
   - 具体方法: 提出神经符号规划框架，在代码生成中加入显式符号验证和主动探索环境的交互式验证，以补全缺失观测。
   - 分类理由: 论文核心是具身任务规划可靠性，覆盖仿真和真实机器人环境。

55. **[Coarse-to-fine Q-Network with Action Sequence for Data-Efficient Reinforcement Learning](https://openreview.net/forum?id=VoFXUNc9Zh)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, locomotion
   - 解决问题: 稀疏奖励强化学习中，单步动作估值难以充分表达执行一段动作序列后的长期后果。
   - 具体方法: 方法让价值网络输出动作序列级别的价值，并以粗到细方式学习动作序列对回报的影响。
   - 分类理由: 核心是机器人控制和强化学习策略改进，实验覆盖人形控制和桌面操作。

56. **[STAIR: Addressing Stage Misalignment through Temporal-Aligned Preference Reinforcement Learning](https://openreview.net/forum?id=WI8rrwYJdT)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, manipulation, planning, hri
   - 解决问题: 论文解决导航、抓取等多阶段任务中，不同阶段片段被错误比较会产生无效偏好反馈并阻碍策略学习的问题。
   - 具体方法: 方法用时间距离对任务阶段进行近似划分，优先比较同阶段片段，并通过对比学习动态适应策略变化。
   - 分类理由: 核心是面向多阶段具身控制任务的偏好强化学习方法，任务明确包含导航和操作。

57. **[Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper](https://openreview.net/forum?id=WabVVQKTUF)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, tactile, deployment-system-reliability
   - 解决问题: 手持夹爪便于采集人类示范，但多数缺少触觉反馈，限制了精细操作中的接触理解和策略学习。
   - 具体方法: 设计集成触觉传感器的轻量夹爪，采集真实场景视触觉数据，并学习保持视觉与触觉差异的跨模态表示用于下游策略。
   - 分类理由: 贡献包含硬件、表示学习和操作策略改进，任务明确是精细机器人操作。

58. **[DynaGuide: Steering Diffusion Polices with Active Dynamic Guidance](https://openreview.net/forum?id=XOw7Yf8qN3)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, planning, manipulation
   - 解决问题: 大型机器人策略部署时需要按场景目标调整行为，但常规目标条件化要求训练时已见过类似目标。
   - 具体方法: 方法在扩散去噪过程中引入外部动力学模型指导，将基础策略和引导信号分离，以支持多目标和低质量目标下的稳健引导。
   - 分类理由: 核心是机器人扩散策略的测试时引导和控制，包含仿真与真实机器人实验。

59. **[SAFE: Multitask Failure Detection for Vision-Language-Action Models](https://openreview.net/forum?id=XPyAukgsFf)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: vla, safety, manipulation, deployment-system-reliability
   - 解决问题: 通用机器人策略在新任务和新环境中成功率有限，需要能跨任务泛化、及时检测失败的安全监控机制。
   - 具体方法: 方法分析视觉语言动作模型内部特征中的成功失败知识，并训练一个从这些特征预测失败概率的检测器，结合保形预测平衡准确率和预警时间。
   - 分类理由: 核心贡献是机器人策略部署安全与失败检测，而不是新视觉语言动作模型本体；任务主要是操作。

60. **[Reinforcement Learning with Action Chunking](https://openreview.net/forum?id=XUks1Y96NR)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: action-tokenization, manipulation
   - 解决问题: 离线到在线强化学习在长程稀疏奖励任务中难以有效利用离线数据形成高效探索策略。
   - 具体方法: 方法直接在分块动作空间中运行强化学习，利用离线数据中的时间一致行为进行探索，并使用无偏多步备份提升价值传播稳定性。
   - 分类理由: 核心是机器人操作任务中的强化学习控制算法，动作块是策略表示与探索机制，而不是数据集贡献。

61. **[Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising](https://openreview.net/forum?id=YY1MPKBHp7)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation
   - 解决问题: 扩散策略在机器人操作中效果强，但推理步骤多，直接沿用视觉生成去噪策略不一定适合低维动作分布。
   - 具体方法: 分析动作分布结构后提出群体采样的遗传去噪，通过选择低分布外风险的去噪轨迹实现两步动作生成。
   - 分类理由: 核心贡献是机器人操作扩散策略的推理加速和稳定化，任务明确为操作控制。

62. **[PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning](https://openreview.net/forum?id=ZR2mdBrhJX)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, benchmark
   - 解决问题: 机器人操作需要同时利用点云几何和图像语义，但现有点云方法易丢失细节，图像方法又缺少几何意识，影响精细操作泛化。
   - 具体方法: PointMapPolicy 将规则网格化点图作为扩散策略条件，保留点级结构并可跨坐标系变换，再用骨干网络融合点图和图像观测。
   - 分类理由: 论文直接研究机器人操作策略，并在操作基准和真实机器人上验证，核心贡献是策略输入表示与模仿控制。

63. **[CoDA: Coordinated Diffusion Noise Optimization for Whole-Body Manipulation of Articulated Objects](https://openreview.net/forum?id=ZY5mzxlnCA)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, whole-body
   - 解决问题: 全身操作关节物体需要身体、双手和物体运动精确协调，尤其是手指与可动部件的细粒度接触。
   - 具体方法: 方法在身体、左手和右手三个扩散模型的噪声空间联合优化，并用统一的空间表示约束手物交互精度。
   - 分类理由: 核心是全身动作生成与关节物体操作控制，属于操作和全身任务交叉。

64. **[DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy](https://openreview.net/forum?id=ZZ09oX2Xpo)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, benchmark, manipulation, sim2real
   - 解决问题: 衣物类别、形状和变形多样，现有仿真难以真实支持双手灵巧衣物操作研究。
   - 具体方法: 环境提供大规模三维资产和任务场景，并用结构对应从单个专家示教生成多样轨迹，再以层次化策略选择可迁移操作点和轨迹。
   - 分类理由: 核心贡献首先是环境和数据生成，同时包含操作策略，主类更适合数据基准仿真。

65. **[DexFlyWheel: A Scalable and Self-improving Data Generation Framework for Dexterous Manipulation](https://openreview.net/forum?id=a49F7EAm6l)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, manipulation, sim2real
   - 解决问题: 灵巧操作缺少多样高质量数据，人工遥操作和专家工程难以支撑策略泛化。
   - 具体方法: 框架从少量种子示教开始，循环执行模仿学习、残差强化学习、轨迹采集和数据增强，不断扩大数据覆盖。
   - 分类理由: 核心贡献是灵巧操作数据生成框架和数据扩展机制，而非单一策略算法。

66. **[Universal Visuo-Tactile Video Understanding for Embodied Interaction](https://openreview.net/forum?id=aPPnmuuNhx)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: tactile, dataset, robot-foundation-model, hri
   - 解决问题: 现有视觉语言方法难以有效纳入触觉信息，无法理解仅凭视觉难以判断的物体物理属性。
   - 具体方法: 构建跨三类触觉传感器的大规模视触觉视频数据集，并通过表示增强、跨模态对齐和文本提示微调训练大模型。
   - 分类理由: 核心是面向具身交互的多模态基础模型，重点模态为触觉、视频和语言。

67. **[$\textit{Hyper-GoalNet}$: Goal-Conditioned Manipulation Policy Learning with HyperNetworks](https://openreview.net/forum?id=aWWRPyGMie)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, planning, deployment-system-reliability
   - 解决问题: 目标条件机器人操作在目标和环境变化较大时，固定策略网络难以稳定保持性能。
   - 具体方法: 方法将目标解释与状态处理分离，由超网络根据目标生成任务特定策略参数，并加入动力学可预测性和目标距离单调性约束。
   - 分类理由: 论文的主要贡献是目标条件操作策略学习，任务场景明确是机器人操作。

68. **[GauDP: Reinventing Multi-Agent Collaboration through Gaussian-Image Synergy in Diffusion Policies](https://openreview.net/forum?id=asS4W7Yw5e)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, world-model, benchmark
   - 解决问题: 论文解决多智能体机器人在局部视角控制和全局场景理解之间难以平衡、协作扩展性不足的问题。
   - 具体方法: 方法从多视角图像重建全局一致的三维高斯场，让各机器人查询任务相关特征，并以此训练多臂协作模仿策略。
   - 分类理由: 核心是多智能体操作策略生成，三维高斯表示服务于扩散策略控制，因此主类为控制规划。

69. **[Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections](https://openreview.net/forum?id=cjcm5LYVWm)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, tactile, hri
   - 解决问题: 真实接触丰富操作中，如何高效收集人类纠正并把纠正整合进策略更新仍然困难。
   - 具体方法: 系统用柔顺控制接口让人类在不中断策略执行的情况下给出增量动作纠正，并学习结合力反馈和力控制的残差策略。
   - 分类理由: 核心是机器人接触操作策略改进，同时包含人类纠正交互，因此标注操作和人机交互。

70. **[SEEA-R1: Tree-Structured Reinforcement Fine-Tuning for Self-Evolving Embodied Agents](https://openreview.net/forum?id=dAwKePZvcN)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: planning, benchmark, robot-foundation-model
   - 解决问题: 具身多步任务中间奖励稀缺，手工奖励函数又难以泛化，限制智能体自我改进能力。
   - 具体方法: 框架将蒙特卡洛树搜索融入组相对策略优化形成树结构训练信号，并用多模态生成式奖励模型跨任务估计奖励，实现无需真实奖励的自演化。
   - 分类理由: 论文明确面向具身智能体自我进化和长程任务，核心是智能体训练框架而非单纯控制策略。

71. **[Human-assisted Robotic Policy Refinement via Action Preference Optimization](https://openreview.net/forum?id=dlQ1iUpQNf)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: vla, manipulation, deployment-system-reliability, dataset
   - 解决问题: 论文解决机器人基础策略依赖离线专家示范，部署后遇到失败难以稳定迭代修正的问题。
   - 具体方法: 方法通过人机协作收集失败纠正轨迹，并用自适应重加权的偏好优化抑制易失败动作、强化纠正动作。
   - 分类理由: 核心贡献是机器人操作策略的后部署对齐与可靠性优化，任务明确为操作。

72. **[SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://openreview.net/forum?id=dt940loCBT)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: vla, safety, manipulation, benchmark, deployment-system-reliability
   - 解决问题: 视觉语言动作模型真实部署时可能伤害环境、机器人或人类，需要把安全约束系统性地融入策略优化。
   - 具体方法: 方法将安全需求建模为约束马尔可夫决策过程，主动诱发多样不安全行为，用安全强化学习约束策略，并通过针对性评估保证安全性。
   - 分类理由: 虽然对象是视觉语言动作模型，但核心贡献是安全约束、风险诱发和安全保证流程，因此主类为安全评估；任务为移动操作。

73. **[Don’t Trade Off Safety: Diffusion Regularization for Constrained Offline RL](https://openreview.net/forum?id=eSIRst0WVy)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: diffusion-policy, safety, dataset, manipulation
   - 解决问题: 真实机器人任务中不能进行危险探索，离线约束强化学习又需要在固定数据上满足安全约束。
   - 具体方法: 方法先用扩散模型捕获离线行为策略，再提取高效策略，并通过梯度操控平衡奖励优化和约束满足。
   - 分类理由: 核心是安全强化学习方法，摘要强调机器人学习任务和安全保证，因此主类归为安全评估。

74. **[Less is More: an Attention-free Sequence Prediction Modeling for Offline Embodied Learning](https://openreview.net/forum?id=fXG1BvwqGt)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, benchmark
   - 解决问题: 论文解决离线强化学习中轨迹序列建模依赖复杂注意力结构、推理慢且状态动作奖励关系建模不清的问题。
   - 具体方法: 方法将序列建模拆成步内关系融合和步间时序混合，提出无参数平均池化混合器与卷积融合器组成决策层次模型。
   - 分类理由: 核心是离线策略学习，并明确扩展到真实机器人操作任务，因此具身相关性高。

75. **[BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models](https://openreview.net/forum?id=ffBF6hYuQv)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, manipulation, benchmark, sim2real, robot-foundation-model
   - 解决问题: 现有基于预训练视觉语言模型的操作方法对三维空间结构利用不足，导致三维操作数据效率低。
   - 具体方法: 方法先训练模型从二维图像预测热图，再将点云投影为多视角图像并在动作生成前保持热图形式的输入输出对齐。
   - 分类理由: 论文明确构建三维视觉语言动作模型，并在多个仿真和真实机器人操作基准上验证。

76. **[World-aware Planning Narratives Enhance Large Vision-Language Model Planner](https://openreview.net/forum?id=fggSyPPk0K)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: vla, planning, world-model, spatial-memory, navigation, manipulation
   - 解决问题: 论文关注大视觉语言模型在具身任务中难以理解环境上下文、空间关系和多步目标，导致长程交互规划成功率不足的问题。
   - 具体方法: 论文提出世界感知规划叙事增强框架，通过视觉外观建模、空间推理、功能抽象和语法落地四类能力，将原始视觉观察转化为更有环境语义的规划信息，并用课程学习训练和评估模型。
   - 分类理由: 核心贡献是增强模型的具身规划能力，而不是单纯提出新数据集或评测；任务发生在类家庭交互环境中，涉及导航、物体操作和长程任务执行，因此归为规划控制方向且具身相关性高。

77. **[Learning and Planning Multi-Agent Tasks via an MoE-based World Model](https://openreview.net/forum?id=fi24ry0BX5)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, manipulation, locomotion
   - 解决问题: 论文解决多任务多智能体强化学习中单一策略难以适应不同任务最优行为差异的问题。
   - 具体方法: 方法提出基于专家混合的世界模型，利用软专家建模动力学、稀疏专家预测回报，并通过模型滚动评估和优化动作。
   - 分类理由: 核心贡献更偏世界模型与规划，且在灵巧手和多智能体运动控制基准上验证，属于具身相关工作。

78. **[URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model](https://openreview.net/forum?id=g3EF5XsapH)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: world-model, sim2real, dataset, robot-foundation-model
   - 解决问题: 准确构建可关节物体数字孪生对机器人仿真训练和世界模型很重要，但传统流程依赖人工或多阶段管线。
   - 具体方法: 基于三维多模态大模型，用点云和文本自回归预测几何分割与运动学参数，并通过专用分割标记增强部件级一致性。
   - 分类理由: 论文主要贡献是面向机器人仿真的可关节物体建模数据与系统能力，服务世界模型和仿真到现实迁移。

79. **[Option-aware Temporally Abstracted Value for Offline Goal-Conditioned Reinforcement Learning](https://openreview.net/forum?id=gfXBNBKx02)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, benchmark, navigation, manipulation
   - 解决问题: 离线目标条件强化学习在长程任务中，高层策略容易生成不合适子目标，优势估计符号错误会阻碍层级策略学习。
   - 具体方法: OTA 将选项感知的时间抽象引入时序差分价值更新，缩短有效规划时域，使高层策略获得更清晰的优势估计。
   - 分类理由: 论文在导航和机器人操作环境中验证，核心贡献是层级策略和价值学习，属于控制与规划。

80. **[Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization](https://openreview.net/forum?id=h6xQClTm4W)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: vla, manipulation, benchmark, dataset, planning
   - 解决问题: 现有视觉语言动作模型在未见操作任务上的跨任务泛化能力缺乏系统评估，实际表现也仍然不足。
   - 具体方法: 论文构建包含未见操作任务的仿真基准，并提出基于上下文示例和动力学引导样本选择的动作序列预测方法。
   - 分类理由: 尽管包含新方法，论文最重要的贡献是操作泛化评测基准，因此主类归为数据基准仿真。

81. **[UniDomain: Pretraining a Unified PDDL Domain from Real-World Demonstrations for Generalizable Robot Task Planning](https://openreview.net/forum?id=hVYp0WzyLK)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation, dataset
   - 解决问题: 机器人任务规划需要处理语言和视觉中的隐式约束，而手工符号域或窄域方法泛化能力有限。
   - 具体方法: 从大量操作视频中抽取原子领域，构建包含算子、谓词和因果边的统一规划域，并按目标任务检索融合为元领域。
   - 分类理由: 核心是机器人操作任务的符号规划知识构建和在线规划。

82. **[Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://openreview.net/forum?id=hVoIz6xD9Q)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, whole-body, manipulation, dataset, sim2real
   - 解决问题: 人形机器人全身模仿常忽视上下身功能差异，导致学习开销大且真实执行容易失稳摔倒。
   - 具体方法: 方法让下身策略负责速度跟踪和稳健移动，上身策略负责动作跟踪，通过迭代对抗更新形成协调控制。
   - 分类理由: 任务直接是人形机器人移动和全身控制，并扩展到移动操作，属于高相关具身控制。

83. **[Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation](https://openreview.net/forum?id=hiiaHn3pWd)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: action-tokenization, diffusion-policy, manipulation
   - 解决问题: 传统视觉运动策略通常逐步向前预测动作，难以让局部动作始终受最终任务目标约束。
   - 具体方法: 方法将稳定关键帧作为首个动作标记，再自回归生成后续连续动作标记，并结合动态停止、反向时间集成和多标记预测。
   - 分类理由: 论文核心是机器人操作策略建模，主要任务是操作，动作标记化是关键技术。

84. **[Learning Spatial-Aware Manipulation Ordering](https://openreview.net/forum?id=iM8154lJCx)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, planning, benchmark
   - 解决问题: 论文解决杂乱环境中对象空间依赖导致错误操作顺序会碰撞或阻塞目标的问题。
   - 具体方法: 方法构建空间图编码对象和机械臂交互，用时序优先级模块预测操作优先级，并用视觉语言模型生成监督顺序进行蒸馏。
   - 分类理由: 核心贡献是面向机器人操作的空间感知顺序规划，并包含仿真和真实实验。

85. **[EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation](https://openreview.net/forum?id=igtjRQfght)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, world-model, diffusion-policy, manipulation, sim2real, dataset
   - 解决问题: 机器人操作需要能够预测未来具身空间、处理三维落地和长期推理，同时还要缓解仿真到真实的差距。
   - 具体方法: 论文采用分块自回归视频扩散预测多视角未来空间，引入稀疏上下文记忆和四维高斯数据引擎，并用动作头转化为物理动作。
   - 分类理由: 虽然包含数据引擎和世界模型，但论文自称生成式机器人基础模型，并输出操作动作，因此主类为基础模型、任务为操作。

86. **[Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges](https://openreview.net/forum?id=inEpyClGV2)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation
   - 解决问题: 论文解决不同形态机器人手之间缺少成对示范或专用仿真时，如何迁移相同抓取意图的问题。
   - 具体方法: 方法把源手和目标手抓取分布之间的映射建模为随机传输问题，结合视觉条件、分数匹配、流匹配和物理启发代价生成目标抓取。
   - 分类理由: 论文的核心是视觉条件下的灵巧抓取生成和迁移，属于操作策略生成。

87. **[AdvEDM: Fine-grained Adversarial Attack against VLM-based Embodied Agents](https://openreview.net/forum?id=jmLCBLeEC4)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: safety, planning, manipulation, vla
   - 解决问题: 针对具身决策中视觉语言模型的攻击若破坏过多语义，容易导致输出无效，难以真实影响物理交互。
   - 具体方法: 方法只修改少数关键对象的感知语义，设计删除和添加两类细粒度攻击，使模型产生有效但错误的决策。
   - 分类理由: 核心贡献是具身智能体安全攻击评估，涉及自动驾驶和机器人操作等具身决策任务。

88. **[RLVR-World: Training World Models with Reinforcement Learning](https://openreview.net/forum?id=jpiSagi8aV)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, navigation, manipulation, dataset
   - 解决问题: 世界模型常用最大似然训练，但该目标与转移预测准确性、感知质量等任务指标并不完全一致。
   - 具体方法: 框架将世界建模表述为令牌序列自回归预测，并用解码后的预测质量作为可验证奖励，通过强化学习直接优化语言和视频世界模型。
   - 分类理由: 核心贡献是世界模型后训练范式，且应用明确包含导航和机器人操作，因此与具身智能高度相关。

89. **[3D Equivariant Visuomotor Policy Learning via Spherical Projection](https://openreview.net/forum?id=kXJd4JxF34)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation
   - 解决问题: 现有等变扩散策略多依赖多相机点云，难以适配常见的手眼单目彩色相机机器人操作设置。
   - 具体方法: 方法将二维图像特征投影到球面，在不显式重建点云的情况下进行三维旋转对称性建模，并嵌入扩散策略。
   - 分类理由: 论文聚焦视觉运动策略学习，核心应用是机器人操作，技术上属于扩散策略与等变控制。

90. **[SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation](https://openreview.net/forum?id=kmv7yg6QXv)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, dataset, robot-foundation-model, planning
   - 解决问题: 论文解决传统位姿表示依赖预定义坐标系或模板、难以泛化到开放词表语义朝向和精细操作的问题。
   - 具体方法: 方法定义语义朝向，构建大规模三维物体朝向标注数据集，训练零样本预测模型，并将朝向信息接入视觉语言智能体生成操作动作。
   - 分类理由: 虽然包含数据集，但核心新意是面向机器人操作的语言落地空间表示，因此归为世界表示类更合适。

91. **[Object-centric 3D Motion Field for Robot Learning from Human Videos](https://openreview.net/forum?id=kp9B9iQDIt)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, sim2real
   - 解决问题: 论文解决从人类视频中提取可迁移动作知识用于机器人策略学习时，视频帧、光流和点云流表示各有信息损失或建模复杂的问题。
   - 具体方法: 方法训练去噪三维运动场估计器，并设计密集对象中心三维运动场预测架构，以支持跨身体迁移和真实机器人控制。
   - 分类理由: 核心是从人类视频学习机器人操作策略，真实实验包括插入等细粒度操作技能。

92. **[InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning](https://openreview.net/forum?id=nzwjvpCO4F)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation, benchmark
   - 解决问题: 论文解决长程机器人操作中语言模型规划器难以分解任务、满足空间时间物理约束并从失败中恢复的问题。
   - 具体方法: 方法用层级指令图分解目标，生成可执行代码；执行失败后由约束生成器归纳符号约束并回写图结构以局部修正代码。
   - 分类理由: 核心是机器人操作任务的长程规划和失败恢复，属于控制规划。

93. **[Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy](https://openreview.net/forum?id=oDoPiR8wZJ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, planning, benchmark, deployment-system-reliability
   - 解决问题: 扩散或流式机器人策略通常在每个控制步使用固定推理预算，简单子任务浪费计算，困难子任务又可能计算不足。
   - 具体方法: 论文提出难度感知随机插值策略，用视觉观测判断当前难度，并动态选择积分步数、求解器类型和随机或确定性积分方式。
   - 分类理由: 核心在机器人控制策略推理预算的动态调度，实验集中在长时程操作任务，因此主类为策略控制规划、任务为操作。

94. **[Contact Map Transfer with Conditional Diffusion Model for Generalizable Dexterous Grasp Generation](https://openreview.net/forum?id=ou9HeYvNhB)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation
   - 解决问题: 灵巧抓取需要兼顾稳定性、效率和任务适应性，但生成方法常受数据限制而泛化不足。
   - 具体方法: 方法把抓取迁移重构为物体接触图生成，结合形状相似性、任务条件、双映射机制和级联扩散模型。
   - 分类理由: 核心是灵巧机器人抓取生成，明确属于操作控制。

95. **[A Smooth Sea Never Made a Skilled SAILOR: Robust Imitation via Learning to Search](https://openreview.net/forum?id=qN5hmLkBtC)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, world-model, planning, diffusion-policy, benchmark
   - 解决问题: 行为克隆只学习专家访问过的状态，机器人一旦偏离示范分布就难以恢复。
   - 具体方法: 方法从专家示范中学习世界模型和奖励模型，在测试时进行搜索规划，并通过系统消融稳定地学习恢复行为。
   - 分类理由: 核心贡献是面向视觉操作任务的鲁棒模仿与测试时规划策略，任务明确为机器人操作。

96. **[AC-DiT: Adaptive Coordination Diffusion Transformer for Mobile Manipulation](https://openreview.net/forum?id=qjee4tiBGZ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, whole-body, navigation, vla
   - 解决问题: 移动操作中底盘运动会影响机械臂控制，而不同阶段对二维语义和三维几何感知的需求也不同。
   - 具体方法: 方法先提取底盘运动表征作为全身动作预测的上下文先验，并根据阶段动态融合二维图像和三维点云特征。
   - 分类理由: 核心贡献是端到端移动操作中的全身协调策略，覆盖导航式底盘运动和机械臂操作。

97. **[DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation](https://openreview.net/forum?id=r4dzaP61QH)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, manipulation, benchmark, sim2real
   - 解决问题: 机器人操作缺少多样真实数据，现有二维预训练或视频预测表征难以同时捕获几何、语义和任务相关动态。
   - 具体方法: 论文通过多视角深度视频预训练三平面表征，使用可微体渲染进行遮蔽重建和未来预测，再迁移到动作价值图预测。
   - 分类理由: 核心贡献是面向操作的三维动态表征学习，而非直接提出新控制算法，因此主类为世界模型表示、任务为操作。

98. **[1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities](https://openreview.net/forum?id=s0JVsx3bx1)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, manipulation, planning
   - 解决问题: 自监督强化学习在无奖励、无示范的目标条件设置中，常受浅层网络容量限制，难以学到有效目标到达行为。
   - 具体方法: 方法系统扩展对比式强化学习中的网络深度到上千层，并在无监督目标条件探索中评估深度对成功率和行为复杂度的影响。
   - 分类理由: 核心是强化学习策略能力缩放，实验覆盖仿真的移动与操作任务，属于具身控制学习。

99. **[Curious Causality-Seeking Agents in Open-ended Worlds](https://openreview.net/forum?id=sdK5Ufoo2d)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, manipulation
   - 解决问题: 开放环境中的因果机制会随潜在状态和策略变化而漂移，固定因果规则世界模型难以泛化。
   - 具体方法: 方法用元因果图表示多个由潜在元状态触发的因果子图，并让智能体通过好奇心驱动干预来发现和更新因果结构。
   - 分类理由: 核心是用于具身智能体探索和规划的世界模型，实验包含机器人手臂操作任务。

100. **[Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training](https://openreview.net/forum?id=ufKaXYJt1F)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, sim2real
   - 解决问题: 论文解决操作策略依赖昂贵真实示范，而仿真数据到真实部署存在观测和动作联合分布差距的问题。
   - 具体方法: 方法学习任务相关且域不变的特征空间，用最优传输启发的损失对齐仿真和真实的观测动作联合分布，并处理仿真多、真实少的数据不平衡。
   - 分类理由: 主要贡献是机器人操作策略的域适应和共训练，属于控制与策略学习。

101. **[OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis](https://openreview.net/forum?id=vSLzoUoJt6)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, manipulation, navigation, planning, dataset
   - 解决问题: 开放世界移动操作需要同时应对开放指令、复杂环境、高层决策和低层控制整合，现有专用模型难以系统泛化。
   - 具体方法: OWMM-Agent 维护多视角场景帧和机器人状态，通过函数调用控制机器人，并用智能体式数据合成流水线微调视觉语言模型以减少领域偏移幻觉。
   - 分类理由: 论文直接面向移动操作机器人，核心是具身基础模型和智能体系统，覆盖导航与操作任务。

102. **[MonoLift: Learning 3D Manipulation Policies from Monocular RGB via Distillation](https://openreview.net/forum?id=wZzC5rpDY1)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, deployment-system-reliability
   - 解决问题: 论文解决单目彩色机器人操作缺少结构信息导致动作估计不准，而深度输入又增加传感和推理成本的问题。
   - 具体方法: 方法用深度引导教师向单目学生进行空间、时间和动作三层知识蒸馏，使部署时仅凭单目图像进行三维感知控制。
   - 分类理由: 核心是视觉机器人操作策略学习，并强调真实和仿真操作验证及部署效率。

103. **[RoboScape: Physics-informed Embodied World Model](https://openreview.net/forum?id=wbZCBBrq3W)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, manipulation, dataset
   - 解决问题: 现有具身世界模型在接触丰富的机器人场景中缺乏三维几何和运动动力学意识，生成视频容易不符合物理规律。
   - 具体方法: 框架联合学习机器人视频生成与物理知识，通过时间深度预测增强几何一致性，并用关键点动力学学习隐式编码形状、材质和运动属性。
   - 分类理由: 论文明确面向具身智能世界模型，且下游验证包括机器人策略训练和策略评估，主类为世界模型与表示。

104. **[Token Bottleneck: One Token to Remember Dynamics](https://openreview.net/forum?id=x7t7B5CFHm)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, manipulation
   - 解决问题: 连续场景理解和机器人操作需要紧凑且具有时间意识的视觉表示，现有表示难以稳定捕捉动态转移。
   - 具体方法: 提出自监督流程，将参考场景压缩到单个瓶颈标记，再结合少量目标图像提示预测后续场景，以逼迫视觉骨干编码时序依赖。
   - 分类理由: 核心贡献是动态视觉表示学习，且面向机器人操作的仿真和真实部署，因此归为世界模型或表示。

105. **[VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents](https://openreview.net/forum?id=xpjWEgf8zi)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, manipulation, planning
   - 解决问题: 视觉语言代理面对复杂视觉观测和部分可观测状态，需要稳定的内部世界模型来支持多轮决策。
   - 具体方法: 将推理过程结构化为状态估计和转移建模，并用世界模型奖励和分层优势估计进行强化学习训练。
   - 分类理由: 核心贡献是多轮视觉代理的世界模型推理训练，并包含高精度操作等具身任务分析。

106. **[Temporal Representation Alignment: Successor Features Enable Emergent Compositionality in Robot Instruction Following](https://openreview.net/forum?id=yaS3JWQRQ6)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, planning
   - 解决问题: 论文解决机器人学会基础任务后，仍难以把多个步骤组合成复合语言或图像目标任务的问题。
   - 具体方法: 方法用当前状态与未来状态表示的时间对齐损失学习后继特征，使任务表示可组合，而不依赖显式子任务规划或强化学习。
   - 分类理由: 核心是机器人操作指令跟随中的可组合任务表示，虽然不是控制器本身，但直接服务操作策略泛化。

107. **[RDD: Retrieval-Based Demonstration Decomposer for Planner Alignment in Long-Horizon Tasks](https://openreview.net/forum?id=zY5J1vp7tZ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: vla, manipulation, planning
   - 解决问题: 长程操作任务需要把复杂目标拆成低层策略可执行的子任务，但人工或启发式分段成本高且容易偏离低层策略训练分布。
   - 具体方法: 方法从低层策略训练数据中检索视觉特征先验，并将演示视频自动切分为与这些先验对齐的子任务区间，从而辅助视觉语言规划器学习任务分解。
   - 分类理由: 论文直接面向层级视觉语言动作框架中的任务分解和规划对齐，实验包含仿真与真实操作任务，因此主类是策略、控制与规划。

108. **[Localist Topographic Expert Routing: A Barrel Cortex-Inspired Modular Network for Sensorimotor Processing](https://openreview.net/forum?id=1Y8MXuJlIY)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: tactile, benchmark, manipulation
   - 解决问题: 论文解决触觉感知中如何利用局部拓扑组织和专家约束来提高三维触觉对象分类效率的问题。
   - 具体方法: 方法将每个触须或传感通道映射到局部专家柱，限制信号路由和邻域通信，并通过稀疏门控减少冗余。
   - 分类理由: 核心是触觉感知网络和分类基准，不是操作策略，但触觉是机器人操作的重要感知模态。

109. **[Text-to-Decision Agent: Offline Meta-Reinforcement Learning from Natural Language Supervision](https://openreview.net/forum?id=9qCejdqPXa)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: world-model, planning, benchmark
   - 解决问题: 论文解决离线元强化学习依赖高质量样本或预探索来推断任务，难以利用更广泛自然语言监督的问题。
   - 具体方法: 方法学习泛化世界模型编码多任务决策数据，并通过语言与决策嵌入的对比预训练对齐文本描述和环境动态，再训练文本条件策略。
   - 分类理由: 实验包含MuJoCo和Meta-World等具身控制基准，但核心仍是通用文本条件决策框架，因此为中等到高相关。

110. **[From Pose to Muscle: Multimodal Learning for Piano Hand Muscle Electromyography](https://openreview.net/forum?id=ftZEltGArK)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, manipulation
   - 解决问题: 论文解决细粒度手部肌电难以低成本、高保真估计，并且跨用户、跨任务泛化不足的问题。
   - 具体方法: 方法构建钢琴演奏多模态数据集，并训练姿态到肌电的估计网络，评估未见用户和任务上的适应能力。
   - 分类理由: 核心贡献是人体手部感知数据和估计框架，与机器人操作间接相关，因此具身相关性为中等。

111. **[SAGE: A Unified Framework for Generalizable Object State Recognition with State-Action Graph Embedding](https://openreview.net/forum?id=jRXgRC6fu7)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: manipulation, world-model
   - 解决问题: 预训练视觉语言模型难以捕捉物体细粒度物理状态及其时间变化，专用状态识别方法又难以泛化到新物体和新动作。
   - 具体方法: 方法用大语言模型构建状态动作图，将物体状态分解为可共享的语言描述视觉概念，再用视觉语言模型进行多模态细化和识别。
   - 分类理由: 核心是物体状态转移表示与视频理解，具身相关性来自机器人操作所需的状态识别，但不是直接控制论文。

112. **[Task-Optimized Convolutional Recurrent Networks Align with Tactile Processing in the Rodent Brain](https://openreview.net/forum?id=m7MD0sa8Re)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: tactile
   - 解决问题: 论文解决触觉感知在人工系统中表征能力不足、现实触觉输入的时序归纳偏置尚不清楚的问题。
   - 具体方法: 方法用定制胡须阵列触觉模拟器训练编码注意解码框架，比较卷积循环网络等结构并分析其与啮齿动物体感皮层数据的对齐。
   - 分类理由: 主体偏神经科学和触觉表征，具身价值是触觉感知模块而非完整机器人操作策略。

113. **[Towards Dynamic 3D Reconstruction of Hand-Instrument Interaction in Ophthalmic Surgery](https://openreview.net/forum?id=pOJBw1YQgL)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: benchmark, dataset, manipulation
   - 解决问题: 眼科显微手术中的手和器械三维重建缺少大规模真实数据和可靠标注工具。
   - 具体方法: 构建大规模动态三维重建数据集，设计多阶段自动标注流水线，并建立双手姿态和手器械交互重建基准。
   - 分类理由: 核心是人手和工具交互的三维感知数据集，不是机器人操作策略，但与操作场景理解密切相关。

114. **[Revisiting Multi-Agent World Modeling from a Diffusion-Inspired Perspective](https://openreview.net/forum?id=rRxFIOoEeF)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark, whole-body, manipulation
   - 解决问题: 多智能体强化学习中的世界模型需要处理指数级联合动作空间和高度不确定动力学，建模复杂度很高。
   - 具体方法: 方法不直接联合建模完整状态动作转移，而是按智能体顺序逐步揭示动作影响，用类似扩散反向过程的方式解析不确定性并预测状态演化。
   - 分类理由: 核心贡献是多智能体控制环境的世界模型；实验包含多智能体运动控制和双手操作基准，因此具身相关性为中等到高。


### Locomotion
1. **[Accelerating Visual-Policy Learning through Parallel Differentiable Simulation](https://openreview.net/forum?id=4frj038M6W)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, sim2real, benchmark
   - 解决问题: 视觉策略训练通常计算开销大、梯度不稳定，尤其在高维移动控制任务中训练时间较长。
   - 具体方法: 方法将渲染过程从计算图中解耦，利用可微仿真和一阶解析策略梯度稳定优化视觉控制策略。
   - 分类理由: 主要贡献是视觉控制策略训练算法，实验重点包含人形移动等具身控制任务。

2. **[PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models](https://openreview.net/forum?id=4xvE6Iy77Y)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, manipulation, locomotion, planning, benchmark
   - 解决问题: 偏好强化学习在机器人复杂行为学习中受限于大量人类反馈需求、查询歧义和奖励学习中的信用分配困难。
   - 具体方法: PRIMT 以视觉语言模型和大语言模型进行神经符号融合反馈评估，并结合前瞻轨迹生成、回顾轨迹增强和因果辅助损失改善学习。
   - 分类理由: 论文直接面向机器人操作和运动任务，核心是偏好强化学习策略优化，基础模型用于反馈和数据合成。

3. **[ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning](https://openreview.net/forum?id=ACagRwCCqu)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, locomotion, manipulation, planning, benchmark
   - 解决问题: 流匹配策略适合连续机器人控制，但确定性路径不利于强化学习探索和稳定似然计算，限制在线微调效果。
   - 具体方法: 方法向流策略的确定性路径注入可学习噪声，将其转化为离散时间马尔可夫过程，从而实现精确似然计算、稳定探索和在线强化学习微调。
   - 分类理由: 论文核心是机器人连续控制策略的在线强化学习微调，实验覆盖腿式运动、状态操作和视觉操作任务。

4. **[Convergent Functions, Divergent Forms](https://openreview.net/forum?id=B6DhWv3DZo)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, manipulation, sim2real
   - 解决问题: 传统形态控制协同设计需要大量仿真训练，且容易陷入形态多样性不足和泛化差的问题。
   - 具体方法: 方法在学习的形态潜空间中为相似设计复用共享控制策略，同时用动态局部搜索替代简单突变来拓展形态探索。
   - 分类理由: 核心是机器人形态和控制策略协同优化，实验涉及运动和下游操作迁移。

5. **[Periodic Skill Discovery](https://openreview.net/forum?id=BPSU46emit)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, planning
   - 解决问题: 无监督技能发现方法通常忽视机器人任务中普遍存在的周期性行为，难以获得跨时间尺度的多样运动技能。
   - 具体方法: PSD 将状态编码到圆形潜空间以自然表达周期性，并通过时间距离学习不同周期的技能，可与现有技能发现方法结合。
   - 分类理由: 论文明确以机器人运动技能为动机，并在运动下游任务中验证，属于控制策略学习。

6. **[GenPO: Generative Diffusion Models Meet On-Policy Reinforcement Learning](https://openreview.net/forum?id=BmRNz1TpCc)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, locomotion, benchmark
   - 解决问题: 论文解决扩散策略难以用于近端策略优化等在线强化学习框架，尤其是动作似然难以精确计算的问题。
   - 具体方法: 方法构造可逆动作映射和双虚拟动作机制，精确计算动作似然，并用于熵、散度和自适应学习率估计。
   - 分类理由: 论文直接服务机器人任务的在线策略优化，覆盖腿式运动、灵巧操作、机械臂和飞行控制。

7. **[Tree-Guided Diffusion Planner](https://openreview.net/forum?id=I1C0a01BZu)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, planning, manipulation, navigation, locomotion
   - 解决问题: 标准梯度引导扩散规划在非凸目标、不可微约束和多奖励结构中效果下降，且监督规划缺少测试时灵活性。
   - 具体方法: 将测试时规划建模为树搜索，先用免训练粒子引导生成多样父轨迹，再用条件去噪细化子轨迹。
   - 分类理由: 核心是面向控制问题的扩散规划算法，并在操作、导航和运动相关任务上评估。

8. **[Focus-Then-Reuse: Fast Adaptation in Visual Perturbation Environments](https://openreview.net/forum?id=I4fBSpDOha)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, sim2real, robot-foundation-model
   - 解决问题: 从仿真训练得到的视觉策略部署到真实复杂环境时，容易受到背景和视觉扰动影响。
   - 具体方法: 论文利用视觉语言模型先验和环境反馈训练物体选择机制，先聚焦任务相关物体再复用仿真策略。
   - 分类理由: 核心贡献是视觉控制策略的快速适应方法，实验包含控制套件和机械臂任务，因此归为策略控制规划。

9. **[Flattening Hierarchies with Policy Bootstrapping](https://openreview.net/forum?id=KaD2Dw8Ahz)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation, locomotion, benchmark, dataset
   - 解决问题: 离线目标条件强化学习在长时程任务中受稀疏奖励和折扣影响，而层级方法又带来子目标模型和多模块复杂性。
   - 具体方法: 论文通过对子目标条件策略进行自举和优势加权重要性采样，训练扁平目标条件策略，避免显式生成子目标。
   - 分类理由: 核心是长时程控制策略学习，实验覆盖移动和操作基准，因此主类为策略控制规划。

10. **[KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](https://openreview.net/forum?id=LCPoXt0pzm)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: whole-body, locomotion, sim2real
   - 解决问题: 论文解决现有人形控制方法难以稳定跟踪高速、高动态人类动作的问题。
   - 具体方法: 方法先对动作进行提取、过滤、修正和重定向，再通过自适应课程式运动模仿和非对称演员评论家训练全身控制策略。
   - 分类理由: 核心贡献是可部署的人形机器人全身控制策略，任务明确为全身高动态运动。

11. **[Physics-informed Value Learner for Offline Goal-Conditioned Reinforcement Learning](https://openreview.net/forum?id=LRYgQuz7kY)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, locomotion, planning
   - 解决问题: 离线目标条件强化学习在数据覆盖有限和长程任务中难以学习可泛化的价值函数，尤其在导航和运动等交互数据昂贵的领域。
   - 具体方法: 方法从 Eikonal 偏微分方程推导物理启发的价值学习正则，并将其接入现有离线目标条件强化学习算法以改善代价到达结构。
   - 分类理由: 论文明确面向自主导航和运动控制，核心是价值函数与策略学习改进，因此归为控制与规划。

12. **[Coarse-to-fine Q-Network with Action Sequence for Data-Efficient Reinforcement Learning](https://openreview.net/forum?id=VoFXUNc9Zh)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, locomotion
   - 解决问题: 稀疏奖励强化学习中，单步动作估值难以充分表达执行一段动作序列后的长期后果。
   - 具体方法: 方法让价值网络输出动作序列级别的价值，并以粗到细方式学习动作序列对回报的影响。
   - 分类理由: 核心是机器人控制和强化学习策略改进，实验覆盖人形控制和桌面操作。

13. **[Learning to Control Free-Form Soft Swimmers](https://openreview.net/forum?id=Z01gNsO9SW)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, sim2real
   - 解决问题: 论文解决软体游泳器形态多样、流固耦合复杂、控制维度高导致自动学习困难的问题。
   - 具体方法: 方法结合统一降维控制空间和图形处理器加速的高保真流体仿真器，自动学习不同形态的游泳模式。
   - 分类理由: 核心是软体机器人在流体环境中的运动控制，属于明确的具身运动任务。

14. **[From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots](https://openreview.net/forum?id=ZBSkyMwdEB)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: whole-body, locomotion, sim2real
   - 解决问题: 论文解决人形机器人在多样高动态动作之间控制需求冲突、数据分布不匹配以及仿真到真实迁移困难的问题。
   - 具体方法: 方法先用自编码聚类把相似动作分组，为每组训练专家策略，再通过真实数据和增量动作建模缩小仿真现实差距，最后蒸馏为统一的通用控制器。
   - 分类理由: 核心贡献是人形机器人全身策略学习与真实部署，不是单纯数据或模型预训练，因此主类为控制规划。

15. **[Efficient Safe Meta-Reinforcement Learning: Provable Near-Optimality and Anytime Safety](https://openreview.net/forum?id=ZtKXAbHQ43)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: safety, locomotion, navigation, planning, benchmark
   - 解决问题: 智能体在适应未见任务时需要保持安全约束始终满足，但现有安全元强化学习在效率、最优性和随时安全上不足。
   - 具体方法: 论文提出一步闭式安全策略适应和无海森元训练算法，并证明适应过程中的安全性和近最优性。
   - 分类理由: 安全保证是论文核心贡献，实验覆盖运动和导航基准，因此主类应为安全评估，任务轴包含导航与移动。

16. **[RLZero: Direct Policy Inference from Language Without In-Domain Supervision](https://openreview.net/forum?id=eyH8QLn2Qx)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, world-model, robot-foundation-model
   - 解决问题: 语言条件强化学习通常需要昂贵监督、标注轨迹或测试时训练，而奖励设计本身也难以准确表达人类意图。
   - 具体方法: 方法先用视频生成模型想象语言描述对应的观测序列，再将其投影到目标环境域，最后由无监督强化学习预训练智能体闭式模仿该观测序列生成行为。
   - 分类理由: 论文直接关注从语言到行为的策略推断和跨具身迁移，是策略生成问题；任务跨多环境且包含类人具身，因此标为通用和运动。

17. **[Learning and Planning Multi-Agent Tasks via an MoE-based World Model](https://openreview.net/forum?id=fi24ry0BX5)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, manipulation, locomotion
   - 解决问题: 论文解决多任务多智能体强化学习中单一策略难以适应不同任务最优行为差异的问题。
   - 具体方法: 方法提出基于专家混合的世界模型，利用软专家建模动力学、稀疏专家预测回报，并通过模型滚动评估和优化动作。
   - 分类理由: 核心贡献更偏世界模型与规划，且在灵巧手和多智能体运动控制基准上验证，属于具身相关工作。

18. **[Intrinsic Goals for Autonomous Agents: Model-Based Exploration in Virtual Zebrafish Predicts Ethological Behavior and Whole-Brain Dynamics](https://openreview.net/forum?id=g2vViuEVDS)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: world-model, planning, locomotion
   - 解决问题: 论文解决无外部奖励环境中现有模型式内在动机探索不稳定、难以形成类似动物自主行为的问题。
   - 具体方法: 方法让智能体追踪在线世界模型与生态先验模型之间的差异，以此驱动探索，并比较虚拟斑马鱼行为和脑动态数据。
   - 分类理由: 核心是自主具身智能体的内在动机和策略形成，虽有神经科学目标，但方法属于控制规划。

19. **[Real-DRL: Teach and Learn at Runtime](https://openreview.net/forum?id=gXZlZAeqay)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: locomotion, safety, sim2real, deployment-system-reliability
   - 解决问题: 深度强化学习智能体在真实系统中在线学习时会遇到未知风险和仿真到现实差距，容易造成安全事故或性能退化。
   - 具体方法: 框架由强化学习学生、物理模型教师和触发器组成，教师在安全关键时刻提供实时补丁和备份控制，学生通过安全状态相关采样逐步学习高性能策略。
   - 分类理由: 论文的关键贡献是安全关键自主系统中的运行时学习与安全保障，并在真实四足机器人上验证，因此归入安全评估轴，任务为运动控制。

20. **[Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://openreview.net/forum?id=hVoIz6xD9Q)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, whole-body, manipulation, dataset, sim2real
   - 解决问题: 人形机器人全身模仿常忽视上下身功能差异，导致学习开销大且真实执行容易失稳摔倒。
   - 具体方法: 方法让下身策略负责速度跟踪和稳健移动，上身策略负责动作跟踪，通过迭代对抗更新形成协调控制。
   - 分类理由: 任务直接是人形机器人移动和全身控制，并扩展到移动操作，属于高相关具身控制。

21. **[1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities](https://openreview.net/forum?id=s0JVsx3bx1)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, manipulation, planning
   - 解决问题: 自监督强化学习在无奖励、无示范的目标条件设置中，常受浅层网络容量限制，难以学到有效目标到达行为。
   - 具体方法: 方法系统扩展对比式强化学习中的网络深度到上千层，并在无监督目标条件探索中评估深度对成功率和行为复杂度的影响。
   - 分类理由: 核心是强化学习策略能力缩放，实验覆盖仿真的移动与操作任务，属于具身控制学习。

22. **[Constrained Diffusers for Safe Planning and Control](https://openreview.net/forum?id=tahkGZjjWA)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: diffusion-policy, planning, safety, locomotion, navigation
   - 解决问题: 扩散模型可生成多模态轨迹，但在受约束规划和在线控制中难以保证安全约束满足。
   - 具体方法: 方法在反向扩散采样中加入约束朗之万优化，并结合投影、原始对偶、增广拉格朗日和离散控制屏障函数。
   - 分类理由: 核心关注安全规划控制，实验覆盖迷宫、运动控制和物理仿真任务。

23. **[Improving Model-Based Reinforcement Learning by Converging to Flatter Minima](https://openreview.net/forum?id=vcB1OwtWUZ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: world-model, planning, benchmark, whole-body, locomotion
   - 解决问题: 论文解决模型式强化学习中学习动力学模型误差沿想象轨迹累积、影响下游策略表现的问题。
   - 具体方法: 方法把锐度感知最小化作为世界模型训练目标，并从理论和实验上说明更平坦的模型解能降低价值估计和策略性能差距。
   - 分类理由: 虽然方法通用，但实验覆盖人形控制和高自由度控制任务，核心影响在策略学习。

24. **[Bootstrap Off-policy with World Model](https://openreview.net/forum?id=zNqDCSokDR)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: world-model, planning, locomotion
   - 解决问题: 用规划器与环境交互会使采集数据和策略自身行为产生偏差，从而影响模型学习和策略改进。
   - 具体方法: 方法联合学习世界模型，让策略初始化规划器、规划器改进行为并通过软价值加权的无似然对齐损失反哺策略。
   - 分类理由: 核心是模型式强化学习和规划控制，评估包含高维控制与人形基准，属于具身控制相关。

25. **[Bigger, Regularized, Categorical: High-Capacity Value Functions are Efficient Multi-Task Learners](https://openreview.net/forum?id=zhOUfuOIzA)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: benchmark, locomotion
   - 解决问题: 多任务在线强化学习中稀疏奖励和梯度冲突会使时序差分优化脆弱，限制通用策略训练。
   - 具体方法: 方法使用高容量价值模型、交叉熵训练和可学习任务嵌入，缓解任务干扰并提升样本效率。
   - 分类理由: 论文是通用强化学习方法，但覆盖高自由度人形控制等具身基准，因此相关性高。

26. **[Text-to-Decision Agent: Offline Meta-Reinforcement Learning from Natural Language Supervision](https://openreview.net/forum?id=9qCejdqPXa)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: world-model, planning, benchmark
   - 解决问题: 论文解决离线元强化学习依赖高质量样本或预探索来推断任务，难以利用更广泛自然语言监督的问题。
   - 具体方法: 方法学习泛化世界模型编码多任务决策数据，并通过语言与决策嵌入的对比预训练对齐文本描述和环境动态，再训练文本条件策略。
   - 分类理由: 实验包含MuJoCo和Meta-World等具身控制基准，但核心仍是通用文本条件决策框架，因此为中等到高相关。

27. **[Flow-Based Policy for Online Reinforcement Learning](https://openreview.net/forum?id=CANUXhPoyn)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: locomotion, benchmark
   - 解决问题: 流模型能表达多峰动作分布，但标准流训练与强化学习中的价值优化目标不匹配。
   - 具体方法: 论文用状态相关速度场生成动作，并推导带二阶瓦瑟斯坦约束的策略搜索目标，使流策略与价值优化对齐。
   - 分类理由: 论文是通用在线强化学习控制方法，实验包含运动控制基准，但不专门面向机器人系统，因此相关性为中等。

28. **[Scaling Off-Policy Reinforcement Learning with Batch and Weight Normalization](https://openreview.net/forum?id=F9jumRh9iu)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: locomotion, whole-body, benchmark
   - 解决问题: 强化学习在真实应用中受样本效率限制，高更新数据比例会放大训练动态不稳定问题。
   - 具体方法: 方法在高更新比例的离策略框架中加入权重归一化，以稳定训练、防止可塑性损失并保持有效学习率稳定。
   - 分类理由: 论文是通用模型无关强化学习算法，但实验包含连续控制、犬形和人形环境，因而与具身运动控制中等相关。

29. **[DyMoDreamer: World Modeling with Dynamic Modulation](https://openreview.net/forum?id=SYKwGnik3w)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark, locomotion
   - 解决问题: 传统世界模型整体处理观测，难以区分动态物体和静态背景，造成视觉控制任务中的计算和样本效率问题。
   - 具体方法: 方法用帧间差分掩码提取运动线索，将动态调制作为随机类别分布注入循环状态空间模型。
   - 分类理由: 论文是通用视觉强化学习世界模型，包含视觉控制基准但不专注实体机器人，因此中等相关。

30. **[To Distill or Decide? Understanding the Algorithmic Trade-off in Partially Observable RL](https://openreview.net/forum?id=iEgaS6wbLa)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: locomotion
   - 解决问题: 部分可观测强化学习需要学习依赖历史的策略，而特权信息蒸馏虽然高效却存在失效模式。
   - 具体方法: 通过扰动块马尔可夫决策过程的理论模型和模拟运动任务实验，研究潜在动力学随机性如何影响蒸馏与强化学习的优劣。
   - 分类理由: 贡献偏算法分析，但实验包含具身运动控制任务，因此归为运动策略学习的中等相关论文。

31. **[A Snapshot of Influence: A Local Data Attribution Framework for Online Reinforcement Learning](https://openreview.net/forum?id=sYK4yPDuT1)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: safety, navigation, locomotion, benchmark
   - 解决问题: 在线强化学习中数据会随策略更新不断变化，传统固定数据集归因方法难以解释样本对行为和回报的影响。
   - 具体方法: 方法针对近期训练缓冲区建立局部归因框架，用梯度相似度衡量样本对动作和累计回报目标的贡献，并据此过滤经验。
   - 分类理由: 论文是通用在线强化学习解释与训练方法，包含导航和移动基准但不专门面向机器人系统，因此相关性为中等。


### Whole-body
1. **[KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](https://openreview.net/forum?id=LCPoXt0pzm)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: whole-body, locomotion, sim2real
   - 解决问题: 论文解决现有人形控制方法难以稳定跟踪高速、高动态人类动作的问题。
   - 具体方法: 方法先对动作进行提取、过滤、修正和重定向，再通过自适应课程式运动模仿和非对称演员评论家训练全身控制策略。
   - 分类理由: 核心贡献是可部署的人形机器人全身控制策略，任务明确为全身高动态运动。

2. **[HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning](https://openreview.net/forum?id=Mk9ykil8eP)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, benchmark, manipulation, planning, diffusion-policy
   - 解决问题: 论文解决人形机器人双臂和灵巧手操作任务、仿真场景以及高质量示范不足的问题。
   - 具体方法: 方法基于原子灵巧技能和空间标注，用大语言模型生成可执行空间约束链，并结合树搜索增强长程推理和示范采集。
   - 分类理由: 核心贡献是数据生成框架和新基准，虽然涉及规划和扩散策略评估，但主类应为数据基准。

3. **[RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics](https://openreview.net/forum?id=OGxalNUHbJ)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, vla, spatial-memory, dataset, benchmark, manipulation, whole-body
   - 解决问题: 现有视觉语言模型难以在复杂三维场景中准确理解指令指向的位置，并进行动态多步空间推理。
   - 具体方法: 模型通过专门深度编码器监督微调获得精确空间理解，再用带度量敏感过程奖励的强化微调提升多步指代推理，并配套大规模数据集和基准。
   - 分类理由: 核心是机器人场景中的三维空间视觉语言基础模型，同时提供数据与基准；可用于机械臂和人形机器人控制，因此主类为基础模型。

4. **[Whole-Body Conditioned Egocentric Video Prediction](https://openreview.net/forum?id=XDTTwmjhAg)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, whole-body, dataset
   - 解决问题: 论文关注如何根据过去第一人称视频和未来全身动作轨迹，预测具身主体接下来会看到的真实环境变化，从而支持可控的具身仿真与行为理解。
   - 具体方法: 方法使用自回归条件扩散变换器，将相对三维人体姿态轨迹作为动作条件，并利用人体关节层级结构组织运动信息，在大规模真实第一人称视频与身体姿态数据上训练，同时设计分层评测协议检验预测和控制能力。
   - 分类理由: 核心贡献不是单纯发布数据集，而是构建一种以身体运动为条件的具身视频世界模型；任务场景围绕全身动作和第一人称具身观察，因此归为全身与跨任务具身建模。

5. **[From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots](https://openreview.net/forum?id=ZBSkyMwdEB)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: whole-body, locomotion, sim2real
   - 解决问题: 论文解决人形机器人在多样高动态动作之间控制需求冲突、数据分布不匹配以及仿真到真实迁移困难的问题。
   - 具体方法: 方法先用自编码聚类把相似动作分组，为每组训练专家策略，再通过真实数据和增量动作建模缩小仿真现实差距，最后蒸馏为统一的通用控制器。
   - 分类理由: 核心贡献是人形机器人全身策略学习与真实部署，不是单纯数据或模型预训练，因此主类为控制规划。

6. **[CoDA: Coordinated Diffusion Noise Optimization for Whole-Body Manipulation of Articulated Objects](https://openreview.net/forum?id=ZY5mzxlnCA)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, whole-body
   - 解决问题: 全身操作关节物体需要身体、双手和物体运动精确协调，尤其是手指与可动部件的细粒度接触。
   - 具体方法: 方法在身体、左手和右手三个扩散模型的噪声空间联合优化，并用统一的空间表示约束手物交互精度。
   - 分类理由: 核心是全身动作生成与关节物体操作控制，属于操作和全身任务交叉。

7. **[Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://openreview.net/forum?id=hVoIz6xD9Q)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: locomotion, whole-body, manipulation, dataset, sim2real
   - 解决问题: 人形机器人全身模仿常忽视上下身功能差异，导致学习开销大且真实执行容易失稳摔倒。
   - 具体方法: 方法让下身策略负责速度跟踪和稳健移动，上身策略负责动作跟踪，通过迭代对抗更新形成协调控制。
   - 分类理由: 任务直接是人形机器人移动和全身控制，并扩展到移动操作，属于高相关具身控制。

8. **[AC-DiT: Adaptive Coordination Diffusion Transformer for Mobile Manipulation](https://openreview.net/forum?id=qjee4tiBGZ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, whole-body, navigation, vla
   - 解决问题: 移动操作中底盘运动会影响机械臂控制，而不同阶段对二维语义和三维几何感知的需求也不同。
   - 具体方法: 方法先提取底盘运动表征作为全身动作预测的上下文先验，并根据阶段动态融合二维图像和三维点云特征。
   - 分类理由: 核心贡献是端到端移动操作中的全身协调策略，覆盖导航式底盘运动和机械臂操作。

9. **[Improving Model-Based Reinforcement Learning by Converging to Flatter Minima](https://openreview.net/forum?id=vcB1OwtWUZ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: world-model, planning, benchmark, whole-body, locomotion
   - 解决问题: 论文解决模型式强化学习中学习动力学模型误差沿想象轨迹累积、影响下游策略表现的问题。
   - 具体方法: 方法把锐度感知最小化作为世界模型训练目标，并从理论和实验上说明更平坦的模型解能降低价值估计和策略性能差距。
   - 分类理由: 虽然方法通用，但实验覆盖人形控制和高自由度控制任务，核心影响在策略学习。

10. **[Scaling Off-Policy Reinforcement Learning with Batch and Weight Normalization](https://openreview.net/forum?id=F9jumRh9iu)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: locomotion, whole-body, benchmark
   - 解决问题: 强化学习在真实应用中受样本效率限制，高更新数据比例会放大训练动态不稳定问题。
   - 具体方法: 方法在高更新比例的离策略框架中加入权重归一化，以稳定训练、防止可塑性损失并保持有效学习率稳定。
   - 分类理由: 论文是通用模型无关强化学习算法，但实验包含连续控制、犬形和人形环境，因而与具身运动控制中等相关。

11. **[ToF-IP: Time-of-Flight Enhanced Sparse Inertial Poser for Real-time Human Motion Capture](https://openreview.net/forum?id=fLKrX29Zy6)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, whole-body
   - 解决问题: 仅依赖稀疏惯性传感器进行人体姿态估计容易受漂移和噪声影响，长时间积分会累积误差。
   - 具体方法: 在少量惯性节点上加入飞行时间测距，设计节点中心数据融合和动态空间位置编码，并采集同步传感器与光学真值数据集。
   - 分类理由: 核心是全身人体姿态捕捉系统和数据集，不是机器人控制本身，但与全身具身感知相关。

12. **[Revisiting Multi-Agent World Modeling from a Diffusion-Inspired Perspective](https://openreview.net/forum?id=rRxFIOoEeF)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark, whole-body, manipulation
   - 解决问题: 多智能体强化学习中的世界模型需要处理指数级联合动作空间和高度不确定动力学，建模复杂度很高。
   - 具体方法: 方法不直接联合建模完整状态动作转移，而是按智能体顺序逐步揭示动作影响，用类似扩散反向过程的方式解析不确定性并预测状态演化。
   - 分类理由: 核心贡献是多智能体控制环境的世界模型；实验包含多智能体运动控制和双手操作基准，因此具身相关性为中等到高。


### HRI
1. **[Inner Speech as Behavior Guides: Steerable Imitation of Diverse Behaviors for Human-AI coordination](https://openreview.net/forum?id=AwLRF1lZvI)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, manipulation, hri
   - 解决问题: 论文解决人类行为具有多样性和非马尔可夫性，而现有模仿学习难以捕捉并在推理时精细调控的问题。
   - 具体方法: 方法用视觉语言模型生成内在语句作为行为意图表示，再训练条件变分自编码器和扩散行为克隆策略按该意图选动作。
   - 分类理由: 核心贡献是可控模仿策略，实验包含机器人操作和人机协作任务。

2. **[Active Test-time Vision-Language Navigation](https://openreview.net/forum?id=EY096v0Jmg)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: navigation, hri, benchmark, deployment-system-reliability
   - 解决问题: 离线训练的视觉语言导航策略在新环境部署时容易遇到分布偏移，单纯熵最小化会累积错误自信。
   - 具体方法: 方法通过情节级人机反馈和自主动学习校准导航结果不确定性，并用混合熵优化调整动作偏好和置信度。
   - 分类理由: 任务明确是视觉语言导航，并包含人机反馈机制，主贡献是导航策略的测试时适应。

3. **[SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration](https://openreview.net/forum?id=EyOtIOmMUh)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, sim2real, navigation, planning, hri
   - 解决问题: 论文解决现有机器人仿真和基准偏室内家庭场景、缺少大规模动态城市环境和多机器人协作评估的问题。
   - 具体方法: 方法基于虚幻引擎生成真实感城市、行人和交通系统，并设计多模态指令导航与多机器人搜索协作两类基准任务。
   - 分类理由: 主要贡献是仿真平台和机器人基准，而不是单一策略或模型，因此归为数据基准仿真类。

4. **[SimWorld: An Open-ended Simulator for Agents in Physical and Social Worlds](https://openreview.net/forum?id=FxCy8TvQHO)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, navigation, planning, hri
   - 解决问题: 论文解决现有世界模拟器场景手工化、物理和社会规则简化、对大模型智能体接口支持不足的问题。
   - 具体方法: 方法构建虚幻引擎仿真平台，提供语言驱动程序化环境、多模态反馈和开放词表动作接口，并评测导航与多智能体配送任务。
   - 分类理由: 核心是开放式物理社会仿真与评测环境，具身任务包含导航和社会交互。

5. **[MEgoHand: Multimodal Egocentric Hand-Object Interaction Motion Generation](https://openreview.net/forum?id=GGj0QFSo5m)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, manipulation, vla
   - 解决问题: 论文解决第一视角手物交互生成中视角不稳定、自遮挡、透视畸变、对象先验依赖和开环误差累积问题。
   - 具体方法: 方法用视觉语言模型推断高层运动先验，用单目深度支持空间推理，再用基于流匹配的低层策略生成细粒度手部轨迹，并统一整理大规模数据集。
   - 分类理由: 核心同时包含手物交互数据和运动生成，直接服务机器人模仿与操作学习。

6. **[AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models](https://openreview.net/forum?id=N5vXT7AGuo)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, hri, world-model, planning, dataset
   - 解决问题: 现有方法多停留在物体级理解，缺少按指令定位可操作部件并推断运动方式和运动轴的细粒度推理。
   - 具体方法: 方法将三维场景渲染成环绕视图并投影候选元素，使用多模态大模型进行主动视角选择和逐步可供性推理。
   - 分类理由: 核心是三维具身可供性表征与推理，虽然不是直接控制策略，但与操作和人机协作密切相关。

7. **[Spatial Understanding from Videos: Structured Prompts Meet Simulation Data](https://openreview.net/forum?id=SBYCu5uJJf)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, dataset, navigation, hri
   - 解决问题: 论文解决预训练视觉语言模型在三维空间关系、场景布局和扫描视频推理中受空间不确定性与数据稀缺限制的问题。
   - 具体方法: 方法结合分解式空间提示策略和由三维仿真场景自动构建的问答数据集，对模型进行提示增强与微调。
   - 分类理由: 主要贡献包含可扩展仿真问答数据和评测验证，面向空间理解这一具身通用能力。

8. **[Universal Visuo-Tactile Video Understanding for Embodied Interaction](https://openreview.net/forum?id=aPPnmuuNhx)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: tactile, dataset, robot-foundation-model, hri
   - 解决问题: 现有视觉语言方法难以有效纳入触觉信息，无法理解仅凭视觉难以判断的物体物理属性。
   - 具体方法: 构建跨三类触觉传感器的大规模视触觉视频数据集，并通过表示增强、跨模态对齐和文本提示微调训练大模型。
   - 分类理由: 核心是面向具身交互的多模态基础模型，重点模态为触觉、视频和语言。

9. **[HoloLLM: Multisensory Foundation Model for Language-Grounded Human Sensing and Reasoning](https://openreview.net/forum?id=cHMP2IAhML)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, hri, benchmark, dataset
   - 解决问题: 论文解决智能家居具身智能体在遮挡、弱光和隐私约束下仅依赖视觉感知不鲁棒的问题。
   - 具体方法: 方法把激光雷达、红外、毫米波雷达和无线信号等稀有传感模态注入多模态大模型，并通过协作标注流程构建传感文本数据。
   - 分类理由: 核心贡献是面向具身人类感知的多模态基础模型和基准，任务轴包含人机交互。

10. **[Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections](https://openreview.net/forum?id=cjcm5LYVWm)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, tactile, hri
   - 解决问题: 真实接触丰富操作中，如何高效收集人类纠正并把纠正整合进策略更新仍然困难。
   - 具体方法: 系统用柔顺控制接口让人类在不中断策略执行的情况下给出增量动作纠正，并学习结合力反馈和力控制的残差策略。
   - 分类理由: 核心是机器人接触操作策略改进，同时包含人类纠正交互，因此标注操作和人机交互。

11. **[Human-assisted Robotic Policy Refinement via Action Preference Optimization](https://openreview.net/forum?id=dlQ1iUpQNf)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: vla, manipulation, deployment-system-reliability, dataset
   - 解决问题: 论文解决机器人基础策略依赖离线专家示范，部署后遇到失败难以稳定迭代修正的问题。
   - 具体方法: 方法通过人机协作收集失败纠正轨迹，并用自适应重加权的偏好优化抑制易失败动作、强化纠正动作。
   - 分类理由: 核心贡献是机器人操作策略的后部署对齐与可靠性优化，任务明确为操作。

12. **[COOPERA: Continual Open-Ended Human-Robot Assistance](https://openreview.net/forum?id=wOSZVnYH5w)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, hri
   - 解决问题: 机器人助手通常只处理预定义任务，缺少对人类长期习惯、特质和意图的建模能力。
   - 具体方法: 框架构建带心理特质和长期意图的模拟人类，并通过持续人类反馈学习个性化协作动作。
   - 分类理由: 核心贡献是人机协作环境、基准和个性化框架，任务为长期人机协助。

13. **[Gaze-VLM: Bridging Gaze and VLMs through Attention Regularization for Egocentric Understanding](https://openreview.net/forum?id=0rVD66dXqT)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: hri
   - 解决问题: 论文解决第一视角活动理解和未来事件预测中模型注意力与人类关注目标不一致的问题。
   - 具体方法: 方法在训练阶段用凝视信号正则化变换器注意力，使模型关注更接近人类视觉注意，同时推理时不需要凝视输入。
   - 分类理由: 核心是第一视角行为理解表征，具身相关来自辅助机器人和人机协作应用，非直接控制或安全评测。

14. **[Gaze Beyond the Frame: Forecasting Egocentric 3D Visual Span](https://openreview.net/forum?id=8rKSfL3GsK)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: spatial-memory, benchmark
   - 解决问题: 论文解决第一视角场景中人类未来视觉关注范围缺少三维预测建模的问题。
   - 具体方法: 方法将同步定位建图关键点转为凝视兼容的三维几何，提取体素化视觉范围，并结合三维网络和时序变换器预测未来关注区域。
   - 分类理由: 论文偏人体第一视角感知表示，与具身交互和辅助技术相关，但不是直接机器人控制。

15. **[From Pose to Muscle: Multimodal Learning for Piano Hand Muscle Electromyography](https://openreview.net/forum?id=ftZEltGArK)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, manipulation
   - 解决问题: 论文解决细粒度手部肌电难以低成本、高保真估计，并且跨用户、跨任务泛化不足的问题。
   - 具体方法: 方法构建钢琴演奏多模态数据集，并训练姿态到肌电的估计网络，评估未见用户和任务上的适应能力。
   - 分类理由: 核心贡献是人体手部感知数据和估计框架，与机器人操作间接相关，因此具身相关性为中等。

16. **[Adaptive Re-calibration Learning for Balanced Multimodal Intention Recognition](https://openreview.net/forum?id=k71nsscO9b)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: hri, deployment-system-reliability, benchmark
   - 解决问题: 多模态意图识别中不同模态的信息量和噪声水平不均衡，模型容易过度依赖强模态而泛化不足。
   - 具体方法: 方法从样本级和结构级两条路径重新校准模态贡献，动态遮蔽过强模态并按全局贡献调整编码器权重。
   - 分类理由: 任务与服务机器人和人机交互相关，但论文主要是通用多模态识别方法，不是完整具身系统。

17. **[AutoToM: Scaling Model-based Mental Inference via Automated Agent Modeling](https://openreview.net/forum?id=oeZZusZheP)**
   - 六类分类: `Agent/System`
   - 相关度: `medium`
   - 技术标签: planning, hri, benchmark
   - 解决问题: 心智理论推理要么依赖容易出错的语言模型提示，要么依赖手工智能体模型而难以跨领域泛化。
   - 具体方法: 方法自动提出初始智能体模型，基于贝叶斯逆向规划推断心理状态，并按不确定性迭代引入新心理变量和更多时序上下文。
   - 分类理由: 主要是社会智能体推理系统，摘要明确提到可用于具身决策，但并非机器人任务专用。


### General/Cross-task
1. **[Tru-POMDP: Task Planning Under Uncertainty via Tree of Hypotheses and Open-Ended POMDPs](https://openreview.net/forum?id=1GIQOV3NAj)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation
   - 解决问题: 家庭服务机器人面对模糊人类指令、隐藏物体位置和开放词表对象时，规划空间巨大且不确定。
   - 具体方法: 用大语言模型构造层级假设树和粒子信念，再在开放式部分可观测决策模型中进行贝叶斯信念跟踪和规划。
   - 分类理由: 论文核心是具身服务机器人在不确定环境中的任务规划，并以厨房物体重排为评测场景。

2. **[ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning](https://openreview.net/forum?id=1lyKflUOhp)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, manipulation
   - 解决问题: 现有端到端视觉语言动作模型在机器人微调后容易丢失原视觉语言模型的识别、数学和空间推理能力。
   - 具体方法: 模型采用专家混合结构和三阶段训练流程，使模型同时保持开放世界理解能力并将推理转化为机器人动作。
   - 分类理由: 核心贡献是通用视觉语言动作基础模型，实验包含白板数学匹配和物体拾取等机器人操作场景。

3. **[DEAL: Diffusion Evolution Adversarial Learning for Sim-to-Real Transfer](https://openreview.net/forum?id=284GWLFtjU)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: sim2real, deployment-system-reliability, safety
   - 解决问题: 仿真训练的控制策略在真实环境中常因物理参数差异而性能下降，高维系统辨识又不稳定。
   - 具体方法: 方法结合扩散演化和对抗学习，迭代优化物理参数分布，使仿真和真实状态转移更一致。
   - 分类理由: 核心是仿真环境校准和迁移，服务机器人强化学习真实部署。

4. **[Diversifying Parallel Ergodic Search: A Signature Kernel Evolution Strategy](https://openreview.net/forum?id=3XuUnUEI7e)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, navigation
   - 解决问题: 并行遍历搜索生成的候选轨迹可能过于相似，导致区域覆盖和搜索效率不足。
   - 具体方法: 方法在轨迹搜索中引入签名核增强路径差异，并给出无导数进化策略形式以支持黑箱目标和批量评估。
   - 分类理由: 核心是机器人探索轨迹规划，实验覆盖平面搜索、四旋翼覆盖和模型预测控制。

5. **[Quantization-Free Autoregressive Action Transformer](https://openreview.net/forum?id=3a18D8IeQ1)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: action-tokenization, planning
   - 解决问题: 当前基于 Transformer 的模仿学习常先离散化动作再自回归生成，量化会破坏连续动作空间结构并限制策略表达。
   - 具体方法: 论文使用生成式无限词表 Transformer 直接参数化连续动作策略，并研究采样算法以提升策略执行效果。
   - 分类理由: 方法在多个模拟机器人任务上达到领先表现，核心是连续动作决策和模仿控制策略。

6. **[ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning](https://openreview.net/forum?id=72UR53jN7T)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, planning, manipulation, robot-foundation-model
   - 解决问题: 现有视觉语言动作模型常端到端映射到动作，缺少显式多步推理，难以适应复杂动态任务变化。
   - 具体方法: 训练多模态大模型生成具身推理计划，并用目标完成度和轨迹一致性构造视觉奖励强化，再将计划压缩为视觉潜变量条件化下游动作模型。
   - 分类理由: 核心贡献是面向视觉语言动作任务的模型框架，同时覆盖规划、少样本适应和机器人操作执行。

7. **[OpenMMEgo: Enhancing Egocentric Understanding for LMMs with Open Weights and Data](https://openreview.net/forum?id=9OyMsbuzL5)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, dataset, robot-foundation-model
   - 解决问题: 现有大多模态模型在第一视角视频场景中表现不足，难以捕捉交互性强、视角变化频繁的具身视觉上下文。
   - 具体方法: OpenMMEgo 构建包含数百万第一视角视频问答的数据集和综合基准，并结合语义感知视觉令牌压缩与课程学习训练策略。
   - 分类理由: 论文核心是面向第一视角具身理解的数据、模型和评测体系，适合归入数据与基准方向。

8. **[EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT](https://openreview.net/forum?id=9Zwl2Ly28N)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, benchmark, robot-foundation-model
   - 解决问题: 现有多模态大模型擅长可见事件推理，但缺乏对第一人称视频中隐藏意图和细粒度交互的具身理解。
   - 具体方法: 论文构建带时空思维链和手物定位标注的第一人称问答数据集，并通过监督微调和强化微调训练模型。
   - 分类理由: 虽然提出模型训练框架，但关键贡献是大规模数据集和第一人称评测能力，因此主类为数据基准仿真。

9. **[PhysVLM-AVR: Active Visual Reasoning for Multimodal Large Language Models in Physical Environments](https://openreview.net/forum?id=AYDMNzpJPv)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, dataset, planning, robot-foundation-model
   - 解决问题: 多模态大模型通常在被动静态图像上推理，难以处理具身智能体在部分可观测物理环境中需要主动探索的信息不足问题。
   - 具体方法: 论文定义主动视觉推理任务，构建交互式模拟基准和带推理链标注的数据集，并训练 PhysVLM-AVR 来选择信息增益最大的动作。
   - 分类理由: 贡献重点是具身闭环感知、推理和行动评测资源，属于数据与基准，同时具备规划和基础模型属性。

10. **[DynamicVerse: A Physically-Aware Multimodal Framework for 4D World Modeling](https://openreview.net/forum?id=B1nCWzpnE4)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: world-model, dataset, benchmark, robot-foundation-model
   - 解决问题: 现有动态世界数据常来自有限仿真或弱尺度标注，难以让基础模型准确理解真实视频中的几何、运动和语义。
   - 具体方法: 论文结合视觉、几何和多模态模型，估计静态几何、动态运动、实例掩码和描述文本，并通过优化生成长视频的四维多模态标注。
   - 分类理由: 虽然包含世界建模方法，但最突出的贡献是大规模数据集和评测任务，因此主类归为数据基准仿真。

11. **[HoloScene: Simulation‑Ready Interactive 3D Worlds from a Single Video](https://openreview.net/forum?id=BOwPpmRgmW)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, sim2real, manipulation, benchmark
   - 解决问题: 论文解决三维重建方法难以同时具备完整几何、物理合理性、对象可交互性和可用于动态仿真的属性的问题。
   - 具体方法: 方法使用交互式场景图表示几何、外观、物理属性和对象关系，并把观测、物理约束和生成先验统一为能量优化目标。
   - 分类理由: 核心是仿真就绪的交互世界表示，而不是数据集本身；操作只是应用示例之一。

12. **[Failure Prediction at Runtime for Generative Robot Policies](https://openreview.net/forum?id=BXJWKpEfro)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: safety, deployment-system-reliability, diffusion-policy
   - 解决问题: 生成式模仿学习策略在分布偏移或误差累积下可能产生不可预测失败，需要在运行时提前报警。
   - 具体方法: 论文同时检测策略嵌入空间中的分布外观测和动作块熵所反映的不确定性，并用成功轨迹进行保形校准。
   - 分类理由: 核心贡献是机器人策略运行时失败预测和安全评估，因此主类为安全评估；任务覆盖多种机器人环境，归为通用。

13. **[GoalLadder: Incremental Goal Discovery with Vision-Language Models](https://openreview.net/forum?id=BiowiwzQaO)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, manipulation
   - 解决问题: 论文解决视觉环境中仅凭语言指令训练强化学习智能体时奖励构造噪声大、反馈需求高的问题。
   - 具体方法: 方法让视觉语言模型比较并排序更接近任务完成的状态，用评分系统缓解噪声，再在学习嵌入空间中驱动智能体接近高分目标。
   - 分类理由: 核心是语言条件的视觉强化学习策略训练，并在机器人操作环境中验证。

14. **[DMWM: Dual-Mind World Model with Long-Term Imagination](https://openreview.net/forum?id=Bzlt5tPFT6)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning
   - 解决问题: 基于循环状态空间的世界模型依赖单步统计推断，长时程想象中容易积累误差并失去逻辑一致性。
   - 具体方法: 方法将直觉式状态转移模块与逻辑集成神经网络模块结合，通过系统间反馈约束想象过程符合环境逻辑规则。
   - 分类理由: 核心贡献是具身智能体世界模型和长时程规划表征，实验含机器人环境。

15. **[Video Perception Models for 3D Scene Synthesis](https://openreview.net/forum?id=D0YNbanYfB)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, sim2real
   - 解决问题: 现有三维场景合成依赖语言模型或图像生成先验，常存在空间推理不足、布局不连贯和多视角不一致问题。
   - 具体方法: 结合视频生成、前馈三维重建和开放词表感知模型，从文本或图像提示生成具有语义与几何一致性的三维场景。
   - 分类理由: 论文明确服务机器人仿真和三维场景世界构建，属于具身环境表示方向。

16. **[What Do Latent Action Models Actually Learn?](https://openreview.net/forum?id=DQMjemrVhe)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: action-tokenization, world-model
   - 解决问题: 论文要解决潜在动作模型从无标注视频中学习动作相关变化时，可能把外部噪声而非可控动作因素编码进潜变量的问题。
   - 具体方法: 方法建立一个可解析的线性潜在动作模型，分析其与主成分分析的关系、数据生成策略的要求，以及数据增强、数据清洗和辅助动作预测为何能促进学习可控变化。
   - 分类理由: 论文直接研究具身智能中常用的潜在动作模型，核心贡献是解释动作相关潜变量的表征机制，而不是提出具体控制器或机器人系统，因此主类归为世界模型与表示。

17. **[WALL-E: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents](https://openreview.net/forum?id=DorAT49sxj)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, spatial-memory
   - 解决问题: 论文要解决大语言模型作为世界模型时，其先验知识与具体环境动力学不匹配，导致智能体在新环境中预测不准、规划效率低的问题。
   - 具体方法: 方法从探索轨迹中抽取动作规则、知识图谱和场景图等符号知识，并编码为可执行约束来对齐世界模型；随后在模型预测控制框架中，让大语言模型智能体与神经符号世界模型交互，进行前瞻式动作选择。
   - 分类理由: 核心贡献是为具身智能体构建和对齐环境世界模型，并在类似我的世界的开放环境与室内具身任务中验证了导航、交互和任务完成能力，因此主类应归为世界模型与表示。

18. **[Learning Interactive World Model for Object-Centric Reinforcement Learning](https://openreview.net/forum?id=E0cjqfM55C)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, benchmark
   - 解决问题: 论文解决对象中心强化学习中只分解对象状态、却没有显式建模对象交互的问题。
   - 具体方法: 方法从像素学习对象潜变量和交互结构，将任务分解为可组合交互原语，并在其上训练高低层策略。
   - 分类理由: 核心贡献是面向具身控制的对象交互世界模型，且在机器人和具身智能基准上评估。

19. **[ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning](https://openreview.net/forum?id=EyNzLH7BZK)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, benchmark
   - 解决问题: 现有三维可供性预测依赖固定类别或外部专家提示，难以泛化到多物体和多步语言指令。
   - 具体方法: 将可供性检测建模为语言条件三维分割，利用几何反馈生成视觉提示并迭代细化可供性掩码，同时构建连续隐式可供性场。
   - 分类理由: 核心是面向具身交互的三维可供性表示，任务与操作前的物体交互理解密切相关。

20. **[CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification](https://openreview.net/forum?id=Fg9HufTI0K)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, deployment-system-reliability
   - 解决问题: 现有视觉语言动作模型后训练和推理计算负担较高，限制大规模部署和实时机器人控制。
   - 具体方法: 方法通过指令驱动的视觉聚合路由、语言标记剪枝路由以及视觉语言动作耦合注意力实现端到端稀疏化。
   - 分类理由: 核心贡献是高效通用视觉语言动作基础模型，技术重点是部署友好的模型结构。

21. **[Self-Improving Embodied Foundation Models](https://openreview.net/forum?id=KXMIIVUB9U)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, deployment-system-reliability
   - 解决问题: 论文解决机器人基础模型低层控制长期依赖行为克隆、难以在少量示范之外自主练习和获得新技能的问题。
   - 具体方法: 方法先用行为克隆和剩余步数预测进行监督微调，再利用剩余步数预测构造奖励和成功检测器，让机器人车队自主练习下游任务。
   - 分类理由: 核心贡献围绕具身基础模型的后训练与自我改进，任务覆盖多种机器人形态和技能，因此归为基础模型类。

22. **[Object-Centric Representation Learning for Enhanced 3D Semantic Scene Graph Prediction](https://openreview.net/forum?id=LjmXrUsSrg)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, spatial-memory
   - 解决问题: 现有三维语义场景图方法过度依赖图神经网络传播关系信息，但物体特征本身判别性不足，导致物体分类和关系预测共同受限。
   - 具体方法: 论文设计高判别性的物体特征编码器，并通过对比式预训练将物体表征学习与场景图预测解耦，再融合几何与语义信息增强关系建模。
   - 分类理由: 核心贡献是三维环境中物体与关系的结构化表示学习，面向机器人和增强现实等场景理解需求，属于具身智能上游感知表征。

23. **[Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations](https://openreview.net/forum?id=MWikv8GJfY)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: 无
   - 解决问题: 稀疏奖励强化学习可借助示范加速，但智能体何时模仿示范、何时依赖自身策略仍难判断。
   - 具体方法: 用集成方法估计示范动作和策略动作的价值分布，并依据不确定性连续调节模仿正则权重。
   - 分类理由: 核心是机器人任务中的强化学习策略训练方法，虽不限定具体任务类型，因此归为通用具身策略。

24. **[Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics](https://openreview.net/forum?id=N2bLuwofZ0)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, vla, planning
   - 解决问题: 机器人具身推理常依赖启发式监督微调数据，容易与实际控制目标不一致，并导致遗忘和泛化下降。
   - 具体方法: 方法让模型根据场景图像和专家演示元数据预测完成任务所需的下一关键点状态，并通过强化学习奖励更准确的推理式响应。
   - 分类理由: 核心是面向机器人控制的视觉语言模型推理能力强化，而不是单一控制器或数据集，因此归入基础模型。

25. **[AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models](https://openreview.net/forum?id=N5vXT7AGuo)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: manipulation, hri, world-model, planning, dataset
   - 解决问题: 现有方法多停留在物体级理解，缺少按指令定位可操作部件并推断运动方式和运动轴的细粒度推理。
   - 具体方法: 方法将三维场景渲染成环绕视图并投影候选元素，使用多模态大模型进行主动视角选择和逐步可供性推理。
   - 分类理由: 核心是三维具身可供性表征与推理，虽然不是直接控制策略，但与操作和人机协作密切相关。

26. **[CAML: Collaborative Auxiliary Modality Learning for Multi-Agent Systems](https://openreview.net/forum?id=OhUu5PlRkF)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: dataset, deployment-system-reliability
   - 解决问题: 多智能体系统训练时可能拥有多模态信息，但部署时常因资源或传感器限制缺失部分模态，导致协作决策出现盲区。
   - 具体方法: 方法在训练阶段让多个智能体共享多模态辅助信息，在测试阶段允许每个智能体只用较少模态推理，并在协同事故检测和空地机器人语义分割中验证。
   - 分类理由: 核心贡献是多智能体协作学习系统，而不是单纯数据集；具身相关性来自机器人和车路协同场景，任务较跨域。

27. **[SAMPO: Scale-wise Autoregression with Motion Prompt for Generative World Models](https://openreview.net/forum?id=PJOwQ77Mul)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning
   - 解决问题: 现有自回归世界模型在空间结构保持、解码效率和运动建模方面不足，导致长程视觉预测不连贯。
   - 具体方法: 方法结合尺度级视觉自回归和下一帧因果建模，引入非对称多尺度分词器与轨迹感知运动提示，以强化动态区域和物理一致性。
   - 分类理由: 核心是用于规划、控制和长程决策的行动条件世界模型，并评估模型式控制，因此高度相关。

28. **[SPiDR: A Simple Approach for Zero-Shot Safety in Sim-to-Real Transfer](https://openreview.net/forum?id=Pe1ypX9gBO)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: safety, sim2real, benchmark, deployment-system-reliability
   - 解决问题: 论文解决强化学习策略从仿真迁移到真实机器人时，仿真现实差距会引发不安全行为的问题。
   - 具体方法: 方法用悲观域随机化把迁移不确定性纳入安全约束，并兼容现有训练管线，在真实机器人平台上验证安全性。
   - 分类理由: 核心目标是安全仿真到现实迁移，而不是构建数据集，因此优先归为安全评估类。

29. **[Dynamic Focused Masking for Autoregressive Embodied Occupancy Prediction](https://openreview.net/forum?id=PvEnRUWSfn)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, benchmark
   - 解决问题: 现有室内三维占用预测多依赖密集体素和重卷积网络，在多尺度自回归建模时计算成本较高。
   - 具体方法: 论文提出在三维高斯参数空间中进行动态聚焦掩码和逐尺度自回归细化，并用重要性引导策略只传播信息量高的高斯元素。
   - 分类理由: 核心贡献是面向三维占用的表示与世界建模方法，而非具体控制策略；任务未限定某一机器人任务，因此归为通用具身场景。

30. **[Building 3D Representations and Generating Motions From a Single Image via Video-Generation](https://openreview.net/forum?id=QNXWTA7PZS)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, navigation
   - 解决问题: 机器人从单张彩色图像恢复环境几何并生成符合场景的无碰撞运动很困难，单目深度误差会影响后续规划。
   - 具体方法: 方法用视频生成模型从单图合成移动相机视角，再交给三维基础模型生成点云，并训练隐式环境表示和运动生成模型。
   - 分类理由: 核心贡献是环境三维表示与运动生成，直接服务自主机器人运动规划。

31. **[Direct Numerical Layout Generation for 3D Indoor Scene Synthesis via Spatial Reasoning](https://openreview.net/forum?id=Qku7g56aWf)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: planning, dataset
   - 解决问题: 三维室内场景布局数据有限，现有方法难以生成开放词汇且符合细粒度指令的物理合理布局。
   - 具体方法: 方法用大语言模型直接生成数值三维布局，分为鸟瞰布局、三维提升和位置细化，并通过思维链激活和布局奖励增强空间推理。
   - 分类理由: 核心是具身环境合成与仿真资产布局，不是机器人操作策略；任务场景较通用。

32. **[EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models](https://openreview.net/forum?id=SELYlDHZk2)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, diffusion-policy, deployment-system-reliability, benchmark
   - 解决问题: 视觉语言动作模型计算和显存需求高，已有加速方法多只处理局部瓶颈，难以覆盖完整推理链路。
   - 具体方法: 论文分别裁剪语言层、选择任务相关视觉标记，并缓存扩散动作头的中间特征，实现结构化训练无关加速。
   - 分类理由: 研究对象明确是视觉语言动作模型，核心贡献是基础模型推理加速，因此主类为基础模型。

33. **[Progress Reward Model for Reinforcement Learning via Large Language Models](https://openreview.net/forum?id=TJhHb6CscW)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, robot-foundation-model
   - 解决问题: 传统强化学习在长程稀疏奖励任务中学习困难，而现有大模型规划方法常依赖预定义技能库且难以优化低层控制。
   - 具体方法: PRM4RL 将复杂任务分解为子任务，构造细粒度进度函数，并基于势函数奖励塑形生成具有收敛保证的进度奖励模型。
   - 分类理由: 论文在机器人控制任务上验证，核心是任务规划与奖励生成结合的策略优化。

34. **[Generative Trajectory Stitching through Diffusion Composition](https://openreview.net/forum?id=VCTt5DXiBe)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, diffusion-policy, benchmark
   - 解决问题: 论文解决长程规划中生成模型难以把已学短轨迹片段组合成新任务可执行轨迹的问题。
   - 具体方法: 方法把轨迹分成重叠片段，用双向扩散模型学习片段间条件关系，使生成时信息能在片段间传播并保持物理一致。
   - 分类理由: 核心贡献是生成式轨迹规划，任务覆盖多种智能体环境，属于通用具身控制规划。

35. **[Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning](https://openreview.net/forum?id=VaC4sa96EI)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, safety, deployment-system-reliability
   - 解决问题: 基于大语言模型的代码即策略方法常因环境 grounding 不足而生成错误或不完整代码，降低任务成功率。
   - 具体方法: 提出神经符号规划框架，在代码生成中加入显式符号验证和主动探索环境的交互式验证，以补全缺失观测。
   - 分类理由: 论文核心是具身任务规划可靠性，覆盖仿真和真实机器人环境。

36. **[Whole-Body Conditioned Egocentric Video Prediction](https://openreview.net/forum?id=XDTTwmjhAg)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, whole-body, dataset
   - 解决问题: 论文关注如何根据过去第一人称视频和未来全身动作轨迹，预测具身主体接下来会看到的真实环境变化，从而支持可控的具身仿真与行为理解。
   - 具体方法: 方法使用自回归条件扩散变换器，将相对三维人体姿态轨迹作为动作条件，并利用人体关节层级结构组织运动信息，在大规模真实第一人称视频与身体姿态数据上训练，同时设计分层评测协议检验预测和控制能力。
   - 分类理由: 核心贡献不是单纯发布数据集，而是构建一种以身体运动为条件的具身视频世界模型；任务场景围绕全身动作和第一人称具身观察，因此归为全身与跨任务具身建模。

37. **[Imagine Beyond ! Distributionally Robust Autoencoding for State Space Coverage in Online Reinforcement Learning](https://openreview.net/forum?id=XEGDKcoQQ1)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning
   - 解决问题: 论文解决视觉目标条件强化学习中在线表征容易偏向已访问状态，导致探索和技能覆盖不足的问题。
   - 具体方法: 方法把变分自编码器与分布鲁棒优化结合，通过对训练状态进行对抗加权，推动潜在空间覆盖更完整的状态分布。
   - 分类理由: 核心是在线强化学习中的探索与控制性能提升，实验包含迷宫和机器人控制任务。

38. **[DynaGuide: Steering Diffusion Polices with Active Dynamic Guidance](https://openreview.net/forum?id=XOw7Yf8qN3)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, planning, manipulation
   - 解决问题: 大型机器人策略部署时需要按场景目标调整行为，但常规目标条件化要求训练时已见过类似目标。
   - 具体方法: 方法在扩散去噪过程中引入外部动力学模型指导，将基础策略和引导信号分离，以支持多目标和低质量目标下的稳健引导。
   - 分类理由: 核心是机器人扩散策略的测试时引导和控制，包含仿真与真实机器人实验。

39. **[Learning 3D Persistent Embodied World Models](https://openreview.net/forum?id=XTTbzC7O2T)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, spatial-memory, planning
   - 解决问题: 论文解决视频世界模型缺少场景持久记忆，难以在部分可观测环境中进行一致长时预测的问题。
   - 具体方法: 方法生成未来第一视角的彩色深度视频，并把生成结果聚合进持久三维地图，再用该空间地图条件化后续视频扩散模型。
   - 分类理由: 核心贡献明确是具身世界模型与空间记忆，并面向规划和策略学习下游应用。

40. **[NeSyPr: Neurosymbolic Proceduralization For Efficient Embodied Reasoning](https://openreview.net/forum?id=a8sJEH4Cjb)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: planning, deployment-system-reliability, benchmark
   - 解决问题: 论文解决动态具身环境中大模型推理和符号规划器在线调用受延迟、连接和算力限制的问题。
   - 具体方法: 方法先由符号工具生成任务计划，再把计划转成可组合过程表示，注入语言模型推理以实现单步高效决策。
   - 分类理由: 核心是具身推理系统，并在多个具身基准上验证部署效率。

41. **[HoloLLM: Multisensory Foundation Model for Language-Grounded Human Sensing and Reasoning](https://openreview.net/forum?id=cHMP2IAhML)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, hri, benchmark, dataset
   - 解决问题: 论文解决智能家居具身智能体在遮挡、弱光和隐私约束下仅依赖视觉感知不鲁棒的问题。
   - 具体方法: 方法把激光雷达、红外、毫米波雷达和无线信号等稀有传感模态注入多模态大模型，并通过协作标注流程构建传感文本数据。
   - 分类理由: 核心贡献是面向具身人类感知的多模态基础模型和基准，任务轴包含人机交互。

42. **[ActiveVOO: Value of Observation Guided Active Knowledge Acquisition for Open-World Embodied Lifted Regression Planning](https://openreview.net/forum?id=cZVYswQQMt)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, benchmark
   - 解决问题: 开放世界环境中对象众多且知识不完整，被动收集所有信息会浪费感知资源并削弱目标导向规划。
   - 具体方法: 方法用提升回归生成一阶子目标描述，再结合大模型常识先验评估感知动作价值，优先获取任务相关对象信息。
   - 分类理由: 核心是开放世界具身规划中的主动知识获取，虽非单一机器人任务，但属于通用具身规划。

43. **[Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better](https://openreview.net/forum?id=cb0xbZ3APM)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, diffusion-policy, deployment-system-reliability
   - 解决问题: 论文解决大型视觉语言模型接入连续动作专家后，训练速度、实时推理和语义知识迁移可能受损的问题。
   - 具体方法: 方法系统分析连续扩散或流匹配动作专家对模型知识迁移的影响，并提出隔离视觉语言骨干知识的训练技术。
   - 分类理由: 核心贡献直接针对机器人视觉语言动作基础模型架构和训练机制，因此主类为基础模型。

44. **[ESCA: Contextualizing Embodied Agents via Scene-Graph Generation](https://openreview.net/forum?id=cjjPn1EIwq)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, spatial-memory, robot-foundation-model, benchmark
   - 解决问题: 现有多模态大模型难以稳定捕获低层视觉特征与高层文本语义之间的细粒度关系，导致具身感知不可靠。
   - 具体方法: 论文训练开放域可提示的场景图生成模型，并将其生成的时空场景图作为上下文注入具身智能体。
   - 分类理由: 核心贡献是场景图形式的具身环境表示与上下文化感知，而不是控制策略本身，因此归为世界模型表示。

45. **[SEEA-R1: Tree-Structured Reinforcement Fine-Tuning for Self-Evolving Embodied Agents](https://openreview.net/forum?id=dAwKePZvcN)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: planning, benchmark, robot-foundation-model
   - 解决问题: 具身多步任务中间奖励稀缺，手工奖励函数又难以泛化，限制智能体自我改进能力。
   - 具体方法: 框架将蒙特卡洛树搜索融入组相对策略优化形成树结构训练信号，并用多模态生成式奖励模型跨任务估计奖励，实现无需真实奖励的自演化。
   - 分类理由: 论文明确面向具身智能体自我进化和长程任务，核心是智能体训练框架而非单纯控制策略。

46. **[Don’t Trade Off Safety: Diffusion Regularization for Constrained Offline RL](https://openreview.net/forum?id=eSIRst0WVy)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: diffusion-policy, safety, dataset, manipulation
   - 解决问题: 真实机器人任务中不能进行危险探索，离线约束强化学习又需要在固定数据上满足安全约束。
   - 具体方法: 方法先用扩散模型捕获离线行为策略，再提取高效策略，并通过梯度操控平衡奖励优化和约束满足。
   - 分类理由: 核心是安全强化学习方法，摘要强调机器人学习任务和安全保证，因此主类归为安全评估。

47. **[OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation](https://openreview.net/forum?id=eXO6g7BmOA)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: world-model, planning, sim2real
   - 解决问题: 现有单次视觉模仿方法通常只在同类任务内泛化，缺少显式环境动力学建模，难以处理语义或结构不同的未见任务。
   - 具体方法: OSVI-WM 根据专家视频和机器人初始观测，用学习到的世界模型预测潜在状态与动作序列，再解码为物理路点指导执行。
   - 分类理由: 核心是机器人视觉模仿和轨迹生成策略，世界模型服务于行动规划，且包含真实机器人评估。

48. **[RLZero: Direct Policy Inference from Language Without In-Domain Supervision](https://openreview.net/forum?id=eyH8QLn2Qx)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning, world-model, robot-foundation-model
   - 解决问题: 语言条件强化学习通常需要昂贵监督、标注轨迹或测试时训练，而奖励设计本身也难以准确表达人类意图。
   - 具体方法: 方法先用视频生成模型想象语言描述对应的观测序列，再将其投影到目标环境域，最后由无监督强化学习预训练智能体闭式模仿该观测序列生成行为。
   - 分类理由: 论文直接关注从语言到行为的策略推断和跨具身迁移，是策略生成问题；任务跨多环境且包含类人具身，因此标为通用和运动。

49. **[Non-Line-of-Sight 3D Reconstruction with Radar](https://openreview.net/forum?id=f4Wd385vHi)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, dataset, navigation
   - 解决问题: 论文解决复杂遮挡环境中机器人只能检测隐藏物体、难以重建完整视线外三维场景的问题。
   - 具体方法: 方法先生成多返回高分辨率距离图，再用物理引导架构建模射线交互，把镜像观测映射到真实位置。
   - 分类理由: 论文部署在移动机器人上并重建遮挡场景，核心是具身环境表示和导航感知。

50. **[Less is More: an Attention-free Sequence Prediction Modeling for Offline Embodied Learning](https://openreview.net/forum?id=fXG1BvwqGt)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: manipulation, benchmark
   - 解决问题: 论文解决离线强化学习中轨迹序列建模依赖复杂注意力结构、推理慢且状态动作奖励关系建模不清的问题。
   - 具体方法: 方法将序列建模拆成步内关系融合和步间时序混合，提出无参数平均池化混合器与卷积融合器组成决策层次模型。
   - 分类理由: 核心是离线策略学习，并明确扩展到真实机器人操作任务，因此具身相关性高。

51. **[Learning and Planning Multi-Agent Tasks via an MoE-based World Model](https://openreview.net/forum?id=fi24ry0BX5)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, manipulation, locomotion
   - 解决问题: 论文解决多任务多智能体强化学习中单一策略难以适应不同任务最优行为差异的问题。
   - 具体方法: 方法提出基于专家混合的世界模型，利用软专家建模动力学、稀疏专家预测回报，并通过模型滚动评估和优化动作。
   - 分类理由: 核心贡献更偏世界模型与规划，且在灵巧手和多智能体运动控制基准上验证，属于具身相关工作。

52. **[Intrinsic Goals for Autonomous Agents: Model-Based Exploration in Virtual Zebrafish Predicts Ethological Behavior and Whole-Brain Dynamics](https://openreview.net/forum?id=g2vViuEVDS)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: world-model, planning, locomotion
   - 解决问题: 论文解决无外部奖励环境中现有模型式内在动机探索不稳定、难以形成类似动物自主行为的问题。
   - 具体方法: 方法让智能体追踪在线世界模型与生态先验模型之间的差异，以此驱动探索，并比较虚拟斑马鱼行为和脑动态数据。
   - 分类理由: 核心是自主具身智能体的内在动机和策略形成，虽有神经科学目标，但方法属于控制规划。

53. **[URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model](https://openreview.net/forum?id=g3EF5XsapH)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: world-model, sim2real, dataset, robot-foundation-model
   - 解决问题: 准确构建可关节物体数字孪生对机器人仿真训练和世界模型很重要，但传统流程依赖人工或多阶段管线。
   - 具体方法: 基于三维多模态大模型，用点云和文本自回归预测几何分割与运动学参数，并通过专用分割标记增强部件级一致性。
   - 分类理由: 论文主要贡献是面向机器人仿真的可关节物体建模数据与系统能力，服务世界模型和仿真到现实迁移。

54. **[PhysX-3D: Physical-Grounded 3D Asset Generation](https://openreview.net/forum?id=hLJLP3CmHR)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: dataset, world-model
   - 解决问题: 现有三维生成模型主要关注几何和纹理，缺少尺度、材料、可供性、运动学和功能等物理属性，限制其在仿真和具身智能中的使用。
   - 具体方法: PhysX-3D 构建物理标注三维数据集，并提出双分支生成框架，将物理知识注入预训练三维结构空间以生成具备合理物理属性的资产。
   - 分类理由: 核心是物理化三维资产数据与生成，直接支撑具身仿真环境和交互对象建模。

55. **[Staggered Environment Resets Improve Massively Parallel On-Policy Reinforcement Learning](https://openreview.net/forum?id=hesM5BWtOJ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: deployment-system-reliability
   - 解决问题: 论文解决大规模并行在线强化学习中同步重置和短回放导致状态分布偏斜、学习信号非平稳的问题。
   - 具体方法: 方法让不同环境在任务时间轴的不同位置初始化和重置，使训练批次覆盖更均匀的状态分布，并在高维机器人环境中验证。
   - 分类理由: 核心是机器人强化学习训练机制和策略学习稳定性，属于控制规划范畴。

56. **[AdvEDM: Fine-grained Adversarial Attack against VLM-based Embodied Agents](https://openreview.net/forum?id=jmLCBLeEC4)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: safety, planning, manipulation, vla
   - 解决问题: 针对具身决策中视觉语言模型的攻击若破坏过多语义，容易导致输出无效，难以真实影响物理交互。
   - 具体方法: 方法只修改少数关键对象的感知语义，设计删除和添加两类细粒度攻击，使模型产生有效但错误的决策。
   - 分类理由: 核心贡献是具身智能体安全攻击评估，涉及自动驾驶和机器人操作等具身决策任务。

57. **[Heterogeneous Graph Transformers for Simultaneous Mobile Multi-Robot Task Allocation and Scheduling under Temporal Constraints](https://openreview.net/forum?id=k1fbdnwjCH)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning
   - 解决问题: 论文解决异构移动机器人团队在时间约束下进行任务分配和调度时规模扩展困难的问题。
   - 具体方法: 方法构建异构图变换器，同时编码机器人能力、行驶时间、时空约束和任务依赖，并用强化学习训练一次性决策模型。
   - 分类理由: 核心贡献是多机器人任务规划和调度决策，任务场景属于移动机器人系统。

58. **[Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](https://openreview.net/forum?id=nI7wKr4eop)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model
   - 解决问题: 现有三维物体嵌入常服务于单一任务，难以同时支持语义理解、显式几何重建和跨任务复用。
   - 具体方法: Object-X 将图像、点云和文本等模态几何锚定到三维体素网格中，学习融合属性的物体嵌入，并可解码为三维高斯重建和用于定位、对齐等任务。
   - 分类理由: 论文核心是面向物体级三维环境理解的通用表示，而非具体控制策略，具身相关性来自机器人需要的对象建模与定位能力。

59. **[Uncertainty-aware Preference Alignment for Diffusion Policies](https://openreview.net/forum?id=oG1CIBWQ77)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, safety
   - 解决问题: 偏好数据来自不同人群，存在不一致和不确定性，直接用于扩散策略更新会影响可靠性。
   - 具体方法: 提出迭代偏好对齐框架，用带信息先验的最大后验目标直接优化扩散策略，并缓解不同用户偏好的冲突。
   - 分类理由: 论文关注机器人任务中的扩散策略偏好对齐与可靠性，属于策略优化方向。

60. **[Adaptive Surrogate Gradients for Sequential Reinforcement Learning in Spiking Neural Networks](https://openreview.net/forum?id=oGmROC4e4W)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: deployment-system-reliability, sim2real
   - 解决问题: 脉冲神经网络用于复杂控制时，非可微脉冲和序列训练困难会限制强化学习性能和真实部署。
   - 具体方法: 方法分析替代梯度斜率对训练的影响，并引入特权引导策略帮助脉冲策略在线交互学习。
   - 分类理由: 论文明确面向能耗受限机器人控制，并包含真实无人机位置控制结果，属于具身控制方法。

61. **[Conditioning Matters:  Training Diffusion Policies is Faster Than You Think](https://openreview.net/forum?id=pKQcmLHoGG)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: diffusion-policy, vla
   - 解决问题: 条件扩散策略在条件难以区分时会退化为拟合边缘动作分布，导致训练效率和控制性能下降。
   - 具体方法: 方法让条件流匹配的源分布依赖条件输入语义，把源分布锚定在条件语义附近以强化条件整合。
   - 分类理由: 核心是机器人视觉语言动作和扩散策略训练机制，任务跨仿真与真实机器人基准。

62. **[3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model](https://openreview.net/forum?id=q5QaTQcUbS)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, spatial-memory, world-model, planning
   - 解决问题: 大型语言模型在动态多房间三维环境中规划和行动时，缺少有效的长期空间与时间记忆机制。
   - 具体方法: 论文构建包含轨迹、任务、问答和描述的记忆基准，并提出用工作记忆查询情景记忆的动态融合模型。
   - 分类理由: 贡献同时包含基准和记忆模型，但摘要强调新基准规模与评测，因此主类归为数据与评测资源。

63. **[What Can RL Bring to VLA Generalization? An Empirical Study](https://openreview.net/forum?id=qmBMPInbZC)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, benchmark
   - 解决问题: 论文关注视觉语言动作模型主要依赖监督微调时，在分布变化下容易出现误差累积和泛化不足的问题，并追问强化学习微调相比监督微调到底能带来哪些泛化收益。
   - 具体方法: 方法构建覆盖视觉、语义和执行维度的泛化评测基准，比较监督微调与多种强化学习微调方法，并总结出面向视觉语言动作模型的高效近端策略优化训练方案。
   - 分类理由: 论文对象明确是具身智能中的视觉语言动作模型，核心贡献是评测和分析强化学习微调对泛化性的作用，并提出训练配方；由于主要是经验研究和基准评估，主类更适合归为安全与评估而非单纯模型提出。

64. **[Online Segment Any 3D Thing as Instance Tracking](https://openreview.net/forum?id=qu7swcInlt)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: robot-foundation-model, spatial-memory, world-model
   - 解决问题: 现有三维开放分割方法缺少时间建模，面对机器人视角变化和部分可见物体时容易出现过分割和实例身份不一致。
   - 具体方法: AutoSeg3D 使用物体查询在时间维度上传播实例信息，通过长期实例关联、短期实例更新和空间一致性学习提升分割连贯性。
   - 分类理由: 论文直接面向具身智能体的在线三维环境感知，核心是动态三维实例表示和跟踪，因此归为世界模型与表示。

65. **[BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization](https://openreview.net/forum?id=rEhVHla9zp)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `high`
   - 技术标签: vla, safety, benchmark, deployment-system-reliability
   - 解决问题: 视觉语言动作模型端到端控制架构可能存在隐蔽持久的后门漏洞，但相关攻击与防护仍缺少系统研究。
   - 具体方法: 方法通过目标解耦优化先分离触发器特征，再在触发条件下诱导控制偏移，同时保持正常任务性能。
   - 分类理由: 核心是具身基础模型安全评估，而非提出新控制能力，因此主类应为安全与评估。

66. **[BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning](https://openreview.net/forum?id=rQCl1sf62w)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: action-tokenization, benchmark, robot-foundation-model
   - 解决问题: 现有动作分词方法常需额外训练，生成效率和轨迹平滑性难以同时满足连续机器人控制需求。
   - 具体方法: 方法用样条曲线把动作序列编码成定长离散或连续令牌，支持并行解码并天然生成平滑轨迹。
   - 分类理由: 核心是机器人模仿学习中的动作表示和控制生成，评估包含大量仿真任务与真实机器人任务。

67. **[Curious Causality-Seeking Agents in Open-ended Worlds](https://openreview.net/forum?id=sdK5Ufoo2d)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, planning, manipulation
   - 解决问题: 开放环境中的因果机制会随潜在状态和策略变化而漂移，固定因果规则世界模型难以泛化。
   - 具体方法: 方法用元因果图表示多个由潜在元状态触发的因果子图，并让智能体通过好奇心驱动干预来发现和更新因果结构。
   - 分类理由: 核心是用于具身智能体探索和规划的世界模型，实验包含机器人手臂操作任务。

68. **[Improving Model-Based Reinforcement Learning by Converging to Flatter Minima](https://openreview.net/forum?id=vcB1OwtWUZ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: world-model, planning, benchmark, whole-body, locomotion
   - 解决问题: 论文解决模型式强化学习中学习动力学模型误差沿想象轨迹累积、影响下游策略表现的问题。
   - 具体方法: 方法把锐度感知最小化作为世界模型训练目标，并从理论和实验上说明更平坦的模型解能降低价值估计和策略性能差距。
   - 分类理由: 虽然方法通用，但实验覆盖人形控制和高自由度控制任务，核心影响在策略学习。

69. **[COOPERA: Continual Open-Ended Human-Robot Assistance](https://openreview.net/forum?id=wOSZVnYH5w)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, hri
   - 解决问题: 机器人助手通常只处理预定义任务，缺少对人类长期习惯、特质和意图的建模能力。
   - 具体方法: 框架构建带心理特质和长期意图的模拟人类，并通过持续人类反馈学习个性化协作动作。
   - 分类理由: 核心贡献是人机协作环境、基准和个性化框架，任务为长期人机协助。

70. **[RoboScape: Physics-informed Embodied World Model](https://openreview.net/forum?id=wbZCBBrq3W)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, manipulation, dataset
   - 解决问题: 现有具身世界模型在接触丰富的机器人场景中缺乏三维几何和运动动力学意识，生成视频容易不符合物理规律。
   - 具体方法: 框架联合学习机器人视频生成与物理知识，通过时间深度预测增强几何一致性，并用关键点动力学学习隐式编码形状、材质和运动属性。
   - 分类理由: 论文明确面向具身智能世界模型，且下游验证包括机器人策略训练和策略评估，主类为世界模型与表示。

71. **[SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent](https://openreview.net/forum?id=x1wZoyS0rC)**
   - 六类分类: `Agent/System`
   - 相关度: `high`
   - 技术标签: planning, world-model
   - 解决问题: 现有室内场景合成方法受固定类别限制，物体级细节、物理一致性和复杂指令对齐能力不足。
   - 具体方法: 系统使用语言模型规划器在多种场景生成工具间选择，并通过物理合理性、视觉真实感和语义对齐自评进行迭代修正。
   - 分类理由: 论文目标是为具身智能生成三维环境，核心形态是可扩展、自反思的智能体系统，而不是单一世界模型。

72. **[Robust Cross-modal Alignment Learning for Cross-Scene Spatial Reasoning and Grounding](https://openreview.net/forum?id=xjC5NqqSHs)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: benchmark, dataset, navigation, spatial-memory
   - 解决问题: 现有三维视觉定位通常假设目标位于已知场景内，而真实智能体可能需要在大量未知或曾访问场景中检索并定位目标对象。
   - 具体方法: 论文定义跨场景空间推理定位任务，构建数据集和评测协议，并提出先匹配场景再定位对象的框架，通过全局文本场景对齐和细粒度词物体关联降低搜索成本。
   - 分类理由: 核心贡献是新任务、数据集和基准，同时方法面向具身智能体跨场景空间检索与定位，相关性较高。

73. **[Policy Compatible Skill Incremental Learning via Lazy Learning Interface](https://openreview.net/forum?id=xmYT1JqVpj)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: planning
   - 解决问题: 具身智能体在增量学习新技能时，技能空间变化可能破坏已有基于技能的层级策略，降低可复用性和泛化能力。
   - 具体方法: SIL-C 使用双向惰性学习映射，将策略引用的子任务空间与技能解码出的行为空间动态对齐，并按轨迹分布相似性选择技能执行。
   - 分类理由: 论文明确以具身智能体的技能增量学习为对象，核心是层级策略和技能兼容控制。

74. **[VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents](https://openreview.net/forum?id=xpjWEgf8zi)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: world-model, manipulation, planning
   - 解决问题: 视觉语言代理面对复杂视觉观测和部分可观测状态，需要稳定的内部世界模型来支持多轮决策。
   - 具体方法: 将推理过程结构化为状态估计和转移建模，并用世界模型奖励和分层优势估计进行强化学习训练。
   - 分类理由: 核心贡献是多轮视觉代理的世界模型推理训练，并包含高精度操作等具身任务分析。

75. **[4D-VLA:  Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration](https://openreview.net/forum?id=yFjgV3cJje)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `high`
   - 技术标签: vla, robot-foundation-model, spatial-memory, benchmark, sim2real
   - 解决问题: 机器人预训练数据中的坐标系和状态信息不一致，会导致动作条件分布分散，降低预训练效率。
   - 具体方法: 方法使用连续彩色深度输入引入深度和时间信息，对齐机器人与场景坐标，并用记忆库采样选择有信息量的历史帧。
   - 分类理由: 核心是通用视觉语言动作预训练框架，且在仿真和真实机器人上验证，符合基础模型类别。

76. **[Point3R: Streaming 3D Reconstruction with Explicit Spatial Pointer Memory](https://openreview.net/forum?id=yk1iqV9Etr)**
   - 六类分类: `World Model/Representation`
   - 相关度: `high`
   - 技术标签: spatial-memory, world-model
   - 解决问题: 现有多图像三维重建方法依赖隐式记忆，容量有限且容易丢失早期帧信息，难以稳定进行在线稠密场景整合。
   - 具体方法: Point3R 维护与当前三维结构直接关联的显式空间指针记忆，让最新帧特征与全局坐标中的指针交互，并通过层级位置编码和融合机制更新场景。
   - 分类理由: 核心是在线三维重建与空间记忆，虽然是视觉方法，但与具身智能体持续建图和环境表征高度相关。

77. **[Bootstrap Off-policy with World Model](https://openreview.net/forum?id=zNqDCSokDR)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: world-model, planning, locomotion
   - 解决问题: 用规划器与环境交互会使采集数据和策略自身行为产生偏差，从而影响模型学习和策略改进。
   - 具体方法: 方法联合学习世界模型，让策略初始化规划器、规划器改进行为并通过软价值加权的无似然对齐损失反哺策略。
   - 分类理由: 核心是模型式强化学习和规划控制，评估包含高维控制与人形基准，属于具身控制相关。

78. **[Imagined Autocurricula](https://openreview.net/forum?id=zXlB9A5xya)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `high`
   - 技术标签: world-model, dataset
   - 解决问题: 论文解决具身智能体训练需要大量环境交互或高保真仿真，而许多真实场景难以满足的问题。
   - 具体方法: 方法在离线学习的世界模型内生成想象环境，并用无监督环境设计形成自动课程，训练能泛化到未见程序化任务的智能体。
   - 分类理由: 核心是利用世界模型生成训练环境和课程，主贡献更接近数据、仿真与训练环境设计。

79. **[Bigger, Regularized, Categorical: High-Capacity Value Functions are Efficient Multi-Task Learners](https://openreview.net/forum?id=zhOUfuOIzA)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `high`
   - 技术标签: benchmark, locomotion
   - 解决问题: 多任务在线强化学习中稀疏奖励和梯度冲突会使时序差分优化脆弱，限制通用策略训练。
   - 具体方法: 方法使用高容量价值模型、交叉熵训练和可学习任务嵌入，缓解任务干扰并提升样本效率。
   - 分类理由: 论文是通用强化学习方法，但覆盖高自由度人形控制等具身基准，因此相关性高。

80. **[Gaze-VLM: Bridging Gaze and VLMs through Attention Regularization for Egocentric Understanding](https://openreview.net/forum?id=0rVD66dXqT)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: hri
   - 解决问题: 论文解决第一视角活动理解和未来事件预测中模型注意力与人类关注目标不一致的问题。
   - 具体方法: 方法在训练阶段用凝视信号正则化变换器注意力，使模型关注更接近人类视觉注意，同时推理时不需要凝视输入。
   - 分类理由: 核心是第一视角行为理解表征，具身相关来自辅助机器人和人机协作应用，非直接控制或安全评测。

81. **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://openreview.net/forum?id=0sUihPtncP)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: benchmark, spatial-memory
   - 解决问题: 论文解决现有三维高斯表面重建需要密集视角和逐场景优化，难以快速泛化到新场景的问题。
   - 具体方法: 方法用前馈网络从稀疏视图生成像素对齐高斯面元，并通过跨视角特征聚合恢复精确几何。
   - 分类理由: 核心是三维几何表示和重建，具身相关性来自机器人感知下游，但实验主要是重建基准。

82. **[Memory-Augmented Potential Field Theory: A Framework for Adaptive Control in Non-Convex Domains](https://openreview.net/forum?id=15GCs8DoSm)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: planning
   - 解决问题: 论文解决随机最优控制在复杂非凸地形中容易陷入局部最优且难以利用历史轨迹的问题。
   - 具体方法: 方法构建记忆增强势场来编码状态空间拓扑特征，并将其实现为记忆增强模型预测路径积分控制器。
   - 分类理由: 核心是通用控制理论和控制器，明确提到机器人动力学适用但缺少具体任务分类。

83. **[Trust Region Reward Optimization and Proximal Inverse Reward Optimization Algorithm](https://openreview.net/forum?id=40M1uJl2GX)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: benchmark
   - 解决问题: 现代逆强化学习的对抗式训练容易不稳定，非对抗式方法虽更稳却缺乏形式化保证。
   - 具体方法: 提出信赖域奖励优化理论，并实例化为近端逆奖励优化算法，以单调改进专家行为似然。
   - 分类理由: 方法是通用逆强化学习，实验包含机器人基准但不是专门的具身系统或任务设计。

84. **[Dynamics-Aligned Latent Imagination in Contextual World Models for Zero-Shot Generalization](https://openreview.net/forum?id=41bIzD5sit)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, planning, benchmark
   - 解决问题: 现实强化学习需要在未见环境条件下零样本适应，但许多方法依赖可观测的摩擦、重力等显式上下文变量。
   - 具体方法: 论文在世界模型框架中加入自监督动力学对齐编码器，从智能体交互中推断潜在上下文，并用该表示条件化模型和策略。
   - 分类理由: 论文主要是世界模型和潜在表示学习，虽不专注某类机器人任务，但与具身智能的环境泛化相关，因此给中等相关。

85. **[LiteReality: Graphics-Ready 3D Scene Reconstruction from RGB-D Scans](https://openreview.net/forum?id=4JLZsmWBJf)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, sim2real, world-model
   - 解决问题: 论文解决从彩色深度扫描自动构建紧凑、可编辑、具备材质和关节对象的真实感三维场景困难的问题。
   - 具体方法: 方法通过场景理解和结构化场景图解析布局，检索艺术家三维资产，恢复物理材质，并集成进仿真引擎。
   - 分类理由: 核心是三维场景重建和仿真资产生成，不是具体机器人策略，但对具身仿真数据有价值。

86. **[PointMAC: Meta-Learned Adaptation for Robust Test-Time Point Cloud Completion](https://openreview.net/forum?id=4xl00JWQ1z)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: deployment-system-reliability, safety, world-model
   - 解决问题: 点云补全模型在测试时通常静态推理，面对新结构模式和传感器导致的缺失或畸变时适应能力不足。
   - 具体方法: PointMAC 使用元学习的测试时适应框架，通过模拟结构和传感缺失的自监督辅助目标在线微调编码器，并用梯度平衡机制稳定适应。
   - 分类理由: 论文是三维感知鲁棒性方法，应用背景包含机器人和安全关键场景，但没有具体具身任务闭环，因此为中等相关。

87. **[Aha! - Predicting What Matters Next: Online Highlight Detection Without Looking Ahead](https://openreview.net/forum?id=7PP2yyeDv6)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: planning, dataset, benchmark, deployment-system-reliability
   - 解决问题: 多数视频高光检测方法依赖完整视频，无法支持智能体在流式环境中逐帧判断哪些信息重要。
   - 具体方法: 方法用多模态视觉语言模型自回归评估每帧与自然语言任务的相关性，并通过常量记忆缓存支持长视频流。
   - 分类理由: 论文主要是通用视频理解方法，只探索机器人潜力，未直接验证具身控制任务，因此为中等相关。

88. **[EA3D: Online Open-World 3D Object Extraction from Streaming Videos](https://openreview.net/forum?id=7aDKD8RBUw)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, spatial-memory, benchmark
   - 解决问题: 现有三维场景理解常依赖离线多视角数据或预构建几何，难以在流式视频中同步重建几何和理解语义。
   - 具体方法: 论文用视觉语言和二维视觉编码器逐帧抽取物体知识，并把语义和几何信息在线更新到高斯特征地图中。
   - 分类理由: 该工作主要是开放世界三维重建与场景理解，具身相关性来自下游机器人感知需求，未绑定具体任务，因此为中等相关。

89. **[COS3D: Collaborative Open-Vocabulary 3D Segmentation](https://openreview.net/forum?id=7bP1wHsJgR)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark
   - 解决问题: 开放词汇三维分割需要同时理解语言和三维实例，但现有方法容易在语言场或预分割误差中受限。
   - 具体方法: 方法构建实例场和语言场协作的三维表示，通过实例到语言映射训练，并在推理时自适应细化语言到实例提示。
   - 分类理由: 论文核心是三维开放词汇感知表征，机器人只是潜在应用，因此具身相关性为中等。

90. **[Lattice Boltzmann Model for Learning Real-World Pixel Dynamicity](https://openreview.net/forum?id=89ZIautowR)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark
   - 解决问题: 论文解决真实视觉跟踪中像素运动状态难以在线、高效、实时估计的问题。
   - 具体方法: 方法用格子玻尔兹曼式的碰撞和流动过程建模动态像素格，并通过预测更新网络估计目标像素位置和可见性。
   - 分类理由: 核心是视觉跟踪表示而非机器人策略，但包含机器人相关点跟踪评测，具身相关性为中等。

91. **[HEIR: Learning Graph-Based Motion Hierarchies](https://openreview.net/forum?id=8VkTkb6WL6)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 论文解决复杂动态系统中运动层级通常依赖人工规则、难以跨任务泛化的问题。
   - 具体方法: 方法用图结构表示运动层级，把全局运动分解为父节点继承模式和局部残差，并通过图神经网络可微学习层级关系。
   - 分类理由: 贡献是通用运动表示学习，具身相关性来自机器人运动建模应用，但实验不以机器人任务为主。

92. **[Gaze Beyond the Frame: Forecasting Egocentric 3D Visual Span](https://openreview.net/forum?id=8rKSfL3GsK)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: spatial-memory, benchmark
   - 解决问题: 论文解决第一视角场景中人类未来视觉关注范围缺少三维预测建模的问题。
   - 具体方法: 方法将同步定位建图关键点转为凝视兼容的三维几何，提取体素化视觉范围，并结合三维网络和时序变换器预测未来关注区域。
   - 分类理由: 论文偏人体第一视角感知表示，与具身交互和辅助技术相关，但不是直接机器人控制。

93. **[Elevating Visual Perception in Multimodal LLMs with Visual Embedding Distillation](https://openreview.net/forum?id=AZ1iyo58F8)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `medium`
   - 技术标签: robot-foundation-model, benchmark
   - 解决问题: 多模态大模型只用语言监督训练时容易偏向语言理解，削弱对空间和视觉细节的感知能力。
   - 具体方法: 论文在预训练阶段加入视觉嵌入蒸馏目标，让语言模型隐藏表示同时学习视觉专家编码器的感知知识。
   - 分类理由: 论文不是直接的机器人系统或任务，但强调具身空间推理所需的视觉感知，因此作为具身基础模型相关工作给中等相关。

94. **[STITCH-OPE: Trajectory Stitching with Guided Diffusion for Off-Policy Evaluation](https://openreview.net/forum?id=AghtKxDf7f)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: diffusion-policy, benchmark, safety
   - 解决问题: 论文解决离策略评估在高维长程任务中重要性采样方差爆炸、学习动力学误差累积的问题。
   - 具体方法: 方法在行为数据上预训练扩散模型，用目标策略得分引导去噪，并通过行为策略负引导和短轨迹拼接生成长程评估轨迹。
   - 分类理由: 论文明确提到机器人等昂贵或不安全交互领域，但实验主要是通用离线强化学习基准，因此相关性为中等。

95. **[FHGS: Feature-Homogenized Gaussian Splatting](https://openreview.net/forum?id=BEYzDKMEhX)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark, dataset
   - 解决问题: 三维高斯的各向异性颜色表达与语义特征的视角无关需求存在矛盾，导致跨视角语义特征不一致。
   - 具体方法: 论文冻结二维预训练特征并蒸馏到三维高斯结构中，设计特征融合、非可微融合和电势场启发的双驱动优化。
   - 分类理由: 该工作是三维场景语义表示方法，具身相关性来自环境理解下游需求，未明确具体导航或操作任务，因此给中等相关。

96. **[SceneForge: Enhancing 3D-text alignment with Structured Scene Compositions](https://openreview.net/forum?id=BNpIO5iYGc)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, spatial-memory
   - 解决问题: 三维文本对比学习缺少大规模复杂组合场景数据，导致模型对多物体关系和空间指令的泛化不足。
   - 具体方法: 方法用单个三维形状构造带显式空间关系的多物体场景，并用大语言模型生成连贯描述，将这些组合样本加入对比训练。
   - 分类理由: 核心是三维文本训练数据增强和场景组合，对具身空间理解有帮助，但没有具体机器人任务。

97. **[ReAgent-V: A Reward-Driven Multi-Agent Framework for Video Understanding](https://openreview.net/forum?id=D1Iw4Unvfc)**
   - 六类分类: `Agent/System`
   - 相关度: `medium`
   - 技术标签: vla, deployment-system-reliability
   - 解决问题: 现有大视觉语言模型的视频理解多为单轮推理，缺乏推理过程中的动态反馈、自我纠错和高效帧选择机制。
   - 具体方法: 框架在推理时进行高效帧选择和实时奖励生成，并通过保守、中立、激进等多视角反思迭代修正答案，同时筛选高质量数据用于后续优化训练。
   - 分类理由: 核心是通用视频理解智能体系统，不是机器人策略本身；摘要提到视觉语言动作模型对齐和机器人控制，因此保留中等具身相关性。

98. **[Abstract Rendering:  Certified Rendering Under 3D Semantic Uncertainty](https://openreview.net/forum?id=EXIKFM1Q9R)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: safety, world-model
   - 解决问题: 相机位姿和三维场景连续变化如何影响渲染图像及下游视觉模型行为，现有安全评估缺少可证明界限。
   - 具体方法: 方法将相机和场景不确定性传播到抽象图像约束中，并为三维高斯和神经辐射场渲染设计分段线性界限传播。
   - 分类理由: 工作本身主要是三维视觉模型认证，不直接研究具身任务，但可用于具身感知安全评估，因此为中等相关。

99. **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://openreview.net/forum?id=FeUGQ6AiKR)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, dataset
   - 解决问题: 大规模动态场景重建通常可扩展性不足，且常依赖标注或预训练先验来分离动态物体。
   - 具体方法: 论文直接预测三维高斯及其运动动态，用光度损失和尽量静态正则在多场景训练中学习动态分解。
   - 分类理由: 该工作主要基于驾驶场景做四维重建，规则下普通自动驾驶不应高估，但其核心是通用动态世界表示，因此保留中等相关。

100. **[Learning World Models for Interactive Video Generation](https://openreview.net/forum?id=FzfYoUp8F1)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, planning, benchmark
   - 解决问题: 论文解决长视频生成世界模型在动作条件下容易误差累积、缺少长期记忆机制的问题。
   - 具体方法: 方法为图像到视频模型加入动作条件和自回归生成，并提出视频检索增强生成与显式全局状态条件来维持时空一致性。
   - 分类理由: 核心是交互式世界模型和规划基础能力，但摘要没有明确机器人执行任务。

101. **[State-Covering Trajectory Stitching for Diffusion Planners](https://openreview.net/forum?id=GEzd5K5s5u)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: diffusion-policy, planning, dataset, benchmark
   - 解决问题: 论文解决离线扩散规划器受训练轨迹质量和多样性限制、难以泛化到分布外任务或更长规划 horizon 的问题。
   - 具体方法: 方法学习保持时间距离的潜在表示，并以新颖性和方向探索为引导拼接短轨迹，生成覆盖更广状态空间的长轨迹。
   - 分类理由: 核心是离线强化学习中的长程规划与数据增强，具身相关性取决于具体环境，摘要未强调机器人本体。

102. **[seq-JEPA: Autoregressive Predictive Learning of Invariant-Equivariant World Models](https://openreview.net/forum?id=GKt3VRaCU1)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 论文解决自监督视觉表征在高层语义任务与细粒度等变任务之间存在性能折中的问题。
   - 具体方法: 方法处理由视角和动作变换构成的短序列，用变换嵌入条件化预测下一观测表示，从而分离学习不变和等变表征。
   - 分类理由: 核心是通用世界模型和表征学习，没有明确机器人任务，因此具身相关性为中等。

103. **[PlayerOne: Egocentric World Simulator](https://openreview.net/forum?id=Gq4Gay8rDB)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: world-model, dataset
   - 解决问题: 现有世界模拟缺少能够从第一视角场景图像出发，并与真实人体运动严格对齐的沉浸式动态环境生成能力。
   - 具体方法: PlayerOne 先用大规模第一视角文本视频预训练，再利用同步内外视角数据微调，并通过部位解耦运动注入和联合重建保持长视频场景一致性。
   - 分类理由: 论文是第一视角世界模拟与生成模型，对具身世界模型有潜在价值，但未明确用于机器人训练或控制闭环。

104. **[Video World Models with Long-term Spatial Memory](https://openreview.net/forum?id=HbTxc6U1fO)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, spatial-memory, dataset
   - 解决问题: 自回归视频世界模型受上下文窗口限制，长程生成中容易忘记此前环境并破坏场景一致性。
   - 具体方法: 设计长期空间记忆的存储和检索机制，并构建用于训练和评估显式三维记忆世界模型的数据集。
   - 分类理由: 核心是世界模型和空间记忆，与具身导航和环境生成相关，但不直接展示机器人控制。

105. **[MLLM-For3D: Adapting Multimodal Large Language Model for 3D Reasoning Segmentation](https://openreview.net/forum?id=IiPSP4OUYx)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: benchmark
   - 解决问题: 论文解决三维场景中根据人类意图和空间关系分割目标对象缺少标注数据和跨视角一致性的问题。
   - 具体方法: 方法用多模态大模型生成多视角伪掩码和文本嵌入，过滤无关视角，再通过查询标记对齐和空间一致性约束训练三维模型。
   - 分类理由: 核心是三维场景理解与分割，可作为具身感知模块，但没有动作执行或机器人闭环。

106. **[Off-policy Reinforcement Learning with Model-based Exploration Augmentation](https://openreview.net/forum?id=JGkZgEEjiM)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: world-model, diffusion-policy, planning
   - 解决问题: 离策略强化学习中的被动探索依赖回放数据，容易缺少多样且关键的欠探索经验，从而限制复杂环境中的学习效率。
   - 具体方法: MoGE 使用扩散生成器在熵和时序差分误差引导下生成关键状态，再用一步想象世界模型合成动力学一致的转移样本。
   - 分类理由: 方法主要是通用强化学习探索增强，在控制基准上验证但未明确聚焦机器人真实任务，因此具身相关性为中等。

107. **[Fast Monte Carlo Tree Diffusion: 100× Speedup via Parallel and Sparse Planning](https://openreview.net/forum?id=JRVZTACwb0)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: planning, diffusion-policy
   - 解决问题: 蒙特卡洛树扩散能处理复杂规划，但树搜索串行性和迭代去噪带来很高推理开销。
   - 具体方法: 论文提出并行展开、延迟树更新、冗余感知选择和稀疏轨迹粗化，以减少规划计算量。
   - 分类理由: 论文是通用扩散规划方法，未明确绑定机器人任务，但与具身规划技术相关，因此为中等相关。

108. **[Agents Robust to Distribution Shifts Learn Causal World Models Even Under Mediation](https://openreview.net/forum?id=JvHif4fyeP)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, planning
   - 解决问题: 智能体在动作会影响环境的中介场景下，如何从鲁棒行为中恢复环境因果结构仍缺少理论刻画。
   - 具体方法: 方法使用最优策略预言机从鲁棒智能体中引出因果知识，并分析单智能体、多智能体和部分可观测序列决策条件。
   - 分类理由: 论文是通用因果与决策理论，具身例子存在但非主要实验对象，因此相关性为中等。

109. **[Vector Quantization in the Brain: Grid-like Codes in World Models](https://openreview.net/forum?id=M44RvNMZs4)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, planning, action-tokenization
   - 解决问题: 动态观测动作序列需要同时压缩空间和时间信息，静态向量量化方法难以充分建模动作条件下的时空结构。
   - 具体方法: 用连续吸引子网络生成网格样编码本，并根据动作动态选择码字，对观测动作序列进行时空压缩。
   - 分类理由: 方法是通用世界模型表示，具备规划用途，但缺少明确机器人任务细节。

110. **[Learning from Demonstrations via Capability-Aware Goal Sampling](https://openreview.net/forum?id=NM5dprhsGK)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: planning
   - 解决问题: 论文解决长时任务中直接模仿专家轨迹过于脆弱、小误差会不断累积的问题。
   - 具体方法: 方法动态估计智能体沿专家轨迹的能力水平，并选择略高于当前能力的中间步骤作为目标形成自适应课程。
   - 分类理由: 核心是通用示教学习算法，摘要未明确机器人任务，但方法适用于具身长程控制。

111. **[VideoHallu: Evaluating and Mitigating Multi-modal Hallucinations on Synthetic Video Understanding](https://openreview.net/forum?id=NoC9HT7Kf7)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: benchmark, dataset, safety
   - 解决问题: 视觉语言模型在真实视频基准上表现好，但可能只是利用表面相关性，未真正理解物理和常识线索。
   - 具体方法: 生成包含物理或逻辑违背场景的合成视频数据集，并用专家问答评测模型识别反常现象的能力。
   - 分类理由: 贡献是多模态物理常识评测，虽非机器人任务，但与具身系统安全理解物理世界相关。

112. **[RaySt3R: Predicting Novel Depth Maps for Zero-Shot Object Completion](https://openreview.net/forum?id=NpRbTTgRBG)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 现有三维形状补全方法在三维一致性、计算成本和物体边界细节上仍有不足，难以从有限观测可靠恢复完整物体结构。
   - 具体方法: 论文将三维补全转化为新视角深度预测，使用前馈变换器根据单张彩色深度图和查询射线预测深度、掩码与置信度，并融合多视角预测重建完整形状。
   - 分类理由: 核心贡献是物体三维表示与补全能力，而不是机器人控制或数据集构建；具身相关性来自机器人可用的几何感知能力，但摘要没有指定具体操作或导航任务。

113. **[Offline Goal-conditioned Reinforcement Learning with Quasimetric Representations](https://openreview.net/forum?id=P23UMiw7iJ)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: planning
   - 解决问题: 离线目标条件强化学习需要从有限数据中学习可靠的目标到达策略，但对比表示和时间距离方法各自存在长程拼接或噪声环境下的不足。
   - 具体方法: 论文将后继表示与准度量空间结构结合，通过三角不等式等约束学习可支持最优目标到达的时间距离表示。
   - 分类理由: 核心是目标条件策略学习与规划表示，可能用于导航或操作，但摘要未强调机器人实验，因此按具身候选中等相关处理。

114. **[Image as a World: Generating Interactive World from Single Image via Panoramic Video Generation](https://openreview.net/forum?id=PA47sKU8CU)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 论文解决单视角图像难以扩展为可控、连续且时序一致的全景动态世界的问题。
   - 具体方法: 方法分为世界初始化、视角探索和时间延续三阶段，使用带球面三维位置编码和多视图组合的扩散世界模型生成全景视频。
   - 分类理由: 论文偏视觉世界生成，具身相关来自可交互环境和虚拟现实应用，但缺少机器人任务闭环。

115. **[LabelAny3D: Label Any Object 3D in the Wild](https://openreview.net/forum?id=Q2fU0JDHuW)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, benchmark
   - 解决问题: 论文解决野外图像缺少三维标注数据，导致单目三维检测模型难以泛化到开放类别场景的问题。
   - 具体方法: 方法用分析合成式流程从二维图像重建整体三维场景并生成三维框标注，构建开放词汇单目三维检测基准。
   - 分类理由: 贡献是三维感知数据和自动标注，和具身感知相关但没有机器人交互或控制实验。

116. **[Deep RL Needs Deep Behavior Analysis: Exploring Implicit Planning by Model-Free Agents in Open-Ended Environments](https://openreview.net/forum?id=QD06Qv7O0P)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: planning, world-model, safety
   - 解决问题: 复杂深度强化学习智能体的行为结构难以仅靠奖励曲线解释，尤其在部分可观测开放环境中。
   - 具体方法: 作者构建自然化觅食环境，并用行为和神经动态分析方法揭示循环网络智能体的记忆与规划样行为。
   - 分类理由: 论文偏评估分析框架，环境具有空间探索和风险规避属性，但不是直接机器人系统。

117. **[Trajectory Graph Learning: Aligning with Long Trajectories in Reinforcement Learning Without Reward Design](https://openreview.net/forum?id=QtnCPZMxYg)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: planning
   - 解决问题: 强化学习奖励函数难设计，普通模仿学习又常只对齐单步动作，难以保持长程轨迹一致性。
   - 具体方法: 将策略学习表述为最大化专家轨迹生成概率，并在结构化假设下提出基于图的规划算法和未知动力学的探索算法。
   - 分类理由: 方法是通用强化学习规划，实验偏网格世界，具身相关性为潜在应用而非直接机器人系统。

118. **[Spatial-MLLM: Boosting MLLM Capabilities in Visual-based Spatial Intelligence](https://openreview.net/forum?id=RnXS7aK4rK)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `medium`
   - 技术标签: robot-foundation-model, dataset
   - 解决问题: 论文解决现有三维多模态模型依赖额外深度或三维数据，难以在只有图像或视频输入时进行空间推理的问题。
   - 具体方法: 方法采用语义视觉编码器和由视觉几何基础模型初始化的三维空间编码器，并加入空间感知帧采样和监督加偏好训练。
   - 分类理由: 核心是空间多模态大模型能力建设，具身相关性来自空间智能但没有直接机器人任务。

119. **[DyMoDreamer: World Modeling with Dynamic Modulation](https://openreview.net/forum?id=SYKwGnik3w)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark, locomotion
   - 解决问题: 传统世界模型整体处理观测，难以区分动态物体和静态背景，造成视觉控制任务中的计算和样本效率问题。
   - 具体方法: 方法用帧间差分掩码提取运动线索，将动态调制作为随机类别分布注入循环状态空间模型。
   - 分类理由: 论文是通用视觉强化学习世界模型，包含视觉控制基准但不专注实体机器人，因此中等相关。

120. **[Structural Information-based Hierarchical Diffusion for Offline Reinforcement Learning](https://openreview.net/forum?id=SbGtQpm2vP)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: diffusion-policy, planning, dataset
   - 解决问题: 论文解决固定两层扩散层级难以适配不同下游任务和时间尺度、长程稀疏奖励决策不稳定的问题。
   - 具体方法: 方法根据离线轨迹中的结构信息自适应构建多时间尺度扩散层级，并用结构信息增益作为条件信号，加入结构熵正则促进安全探索。
   - 分类理由: 核心是通用离线策略学习与长程规划，具身相关性可能存在但摘要未给出明确机器人任务。

121. **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://openreview.net/forum?id=V56unBiTHP)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, dataset
   - 解决问题: 论文解决长时单目视频中动态场景重建训练开销大、视角变化和多主体交互难以处理的问题。
   - 具体方法: 方法将场景分解为静态背景和动态前景对象，用可逆高斯变形网络建模刚体、骨架和非刚体变化，实现高效自由视角渲染。
   - 分类理由: 研究重点是具身视角场景表示和重建，不是动作策略，因此归为世界模型与表示。

122. **[TC-Light: Temporally Coherent Generative Rendering for Realistic World Transfer](https://openreview.net/forum?id=Wd9Y1C3KXs)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: sim2real, benchmark
   - 解决问题: 论文解决世界到世界视觉迁移中长视频动态复杂、光照纹理重渲染容易时间不一致且计算成本高的问题。
   - 具体方法: 方法采用两阶段后优化，先对齐全局光照，再优化规范视频表示以细化纹理和光照，并建立长动态视频基准。
   - 分类理由: 核心是视觉数据迁移和基准，具身相关性来自对仿真到现实数据扩增的支持。

123. **[DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular Videos](https://openreview.net/forum?id=X2u8esISdb)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, dataset
   - 解决问题: 前馈场景重建多局限于静态场景，难以从单目视频恢复动态物体运动和三维形变。
   - 具体方法: 方法使用增强合成数据、可变形三维高斯表示和大型变换器网络，预测动态场景的三维高斯和形变。
   - 分类理由: 论文是动态三维表示学习，不直接做机器人控制，但可支撑具身环境建模。

124. **[3D-Agent: A Tri-Modal Multi-Agent Responsive Framework for Comprehensive 3D Object Annotation](https://openreview.net/forum?id=YGIbwfNWot)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, robot-foundation-model
   - 解决问题: 三维对象标注受空间复杂性、遮挡和视角不一致影响，单模型方法难以兼顾准确性与吞吐。
   - 具体方法: 方法构建多智能体框架，融合多视图图像、文本和点云，由描述生成、信息聚合和几何对齐代理协同完成精细标注。
   - 分类理由: 论文不是直接的具身策略或机器人系统，但其三维对象标注数据能力与具身感知数据建设相关，因此相关性为中等。

125. **[OptiScene: LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization](https://openreview.net/forum?id=ZnrM5RGrgR)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, spatial-memory
   - 解决问题: 现有室内布局生成方法要么依赖昂贵闭源大模型提示，要么受限于粗糙关系图和小规模数据，难以泛化到多样房间。
   - 具体方法: 论文构建大规模人审合成布局数据集，并训练开源布局生成模型，通过监督微调和多轮偏好优化提升空间一致性和人类偏好对齐。
   - 分类理由: 核心产物是室内场景布局数据与生成模型，对具身环境仿真和导航训练有间接价值，但不是机器人策略本身。

126. **[Dyn-O: Building Structured World Models with  Object-Centric Representations](https://openreview.net/forum?id=b2u1yrTwFK)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 多数世界模型使用整体表征，难以有效捕捉物体间交互并支持组合泛化。
   - 具体方法: 方法改进物体中心表示学习和动态建模，并将特征拆为动态无关与动态相关部分以生成多样想象轨迹。
   - 分类理由: 核心是世界模型表征，实验在游戏环境而非机器人；具身意义在于物体交互建模。

127. **[Towards Physical Understanding in Video Generation: A 3D Point Regularization Approach](https://openreview.net/forum?id=bYF7Gvv0s0)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, dataset
   - 解决问题: 现有视频生成模型缺少形状和三维运动意识，容易出现非物理变形和物体形态漂移。
   - 具体方法: 用三维点轨迹增强二维视频数据，并微调潜扩散模型，使其能跟踪带三维坐标的物体并正则化形状和运动。
   - 分类理由: 核心是物理感知视频生成，不直接控制机器人，但对接触丰富场景和具身模拟有潜在作用。

128. **[Force Prompting: Video Generation Models Can Learn And Generalize Physics-based Control Signals](https://openreview.net/forum?id=eX5aXfJQZc)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, dataset
   - 解决问题: 现有视频世界模型更多关注视觉动态，对真实力作用导致的物理交互建模不足，且力视频配对数据难获取。
   - 具体方法: 论文用合成视频训练视频生成模型理解局部点力和全局风力等力提示，并验证其跨形状、材料和场景泛化。
   - 分类理由: 论文不直接训练机器人策略，但围绕物理交互世界模型，具身相关性较明确但偏间接，因此为中等相关。

129. **[Self-Supervised Learning of Motion Concepts by Optimizing Counterfactuals](https://openreview.net/forum?id=fGuTN7huo5)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 论文解决真实视频中光流和遮挡等运动基元依赖标注或合成数据、泛化到真实场景受限的问题。
   - 具体方法: 方法通过反事实探针从预训练视频预测模型中零样本读出运动信息，并用稀疏预测原则自监督优化探针生成参数。
   - 分类理由: 贡献是运动表征学习而非机器人策略，具身相关性来自运动感知对机器人和可控视频的下游价值。

130. **[Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations](https://openreview.net/forum?id=fV46JjrrOm)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 单独二维或三维自监督表征难以同时获得细粒度几何一致性和语义一致性。
   - 具体方法: 方法结合三维模态内自蒸馏和二维三维跨模态联合嵌入，并可将表征投影到语言空间以支持开放世界感知。
   - 分类理由: 论文不是直接机器人系统，但其空间表征可支撑具身感知，因此判为中等相关。

131. **[Talk2Event: Grounded Understanding of Dynamic Scenes from Event Cameras](https://openreview.net/forum?id=fxERuSBpfQ)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: benchmark, dataset, deployment-system-reliability
   - 解决问题: 论文解决事件相机异步动态信号难以与自然语言表达对齐、缺少语言驱动物体定位基准的问题。
   - 具体方法: 方法从真实驾驶数据构建大规模指代表达数据集，并设计多属性事件专家混合模型融合外观、状态和关系线索。
   - 分类理由: 核心是动态感知数据集和基准，虽来自驾驶数据但目标可服务真实机器人和自主系统感知。

132. **[DINO-Foresight: Looking into the Future with DINO](https://openreview.net/forum?id=gimtybo07H)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: robot-foundation-model, world-model
   - 解决问题: 未来动态预测若在像素空间进行，计算开销高且容易关注与任务无关的细节。
   - 具体方法: 方法在预训练视觉基础模型语义特征空间中，用自监督掩码特征变换器预测未来特征，再接入任务头完成未来帧分析。
   - 分类理由: 贡献是通用场景动态表征，不是直接机器人策略；因明确服务机器人环境理解，判为中等相关。

133. **[DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning](https://openreview.net/forum?id=guZBnsKPsw)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: planning
   - 解决问题: 高维长时程稀疏奖励任务需要有方向的探索，否则智能体很难发现与目标相关的中间任务。
   - 具体方法: 方法从现有强化学习算法中提取目标方向，选择朝向目标任务的探索目标，并给出样本复杂度分析。
   - 分类理由: 论文是通用强化学习探索方法，摘要未明确机器人任务，但可迁移到具身长时程控制。

134. **[SpatialReasoner: Towards Explicit and Generalizable 3D Spatial Reasoning](https://openreview.net/forum?id=hFaXVjRFHI)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `medium`
   - 技术标签: robot-foundation-model, benchmark
   - 解决问题: 论文解决现有多模态模型三维空间推理隐式且不稳定、面对简单但需要几何计算的问题也容易出错的问题。
   - 具体方法: 方法在三维感知、计算和推理阶段共享显式三维表示，并通过推理轨迹分析模型事实错误。
   - 分类理由: 主要贡献是视觉语言基础模型的三维空间推理能力，具身相关但未聚焦机器人执行。

135. **[InfiniPot-V: Memory-Constrained KV Cache Compression for Streaming Video Understanding](https://openreview.net/forum?id=hFxOZjHyTg)**
   - 六类分类: `Agent/System`
   - 相关度: `medium`
   - 技术标签: deployment-system-reliability, benchmark
   - 解决问题: 论文解决多模态大模型处理长时流式视频时键值缓存随时间线性增长、无法在固定内存设备上运行的问题。
   - 具体方法: 方法在缓存达到阈值时执行无训练压缩，删除时间冗余令牌并保留语义重要令牌，从而维持长度无关的内存上限。
   - 分类理由: 论文不是具身任务方法，但面向边缘机器人视频助手的系统可靠部署，因此具身相关性为中等。

136. **[Taming generative video models for zero-shot optical flow extraction](https://openreview.net/forum?id=hfOgywCQ8j)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark, dataset, sim2real
   - 解决问题: 论文解决光流标注稀缺且合成数据存在仿真到现实差距，冻结视频生成模型难以直接读出运动对应的问题。
   - 具体方法: 方法用局部扰动追踪预测分布变化，并基于具备随机访问解码的序列架构进行测试时反事实提示来估计光流。
   - 分类理由: 贡献是运动世界模型表征和零样本视觉读出，具身相关性间接来自机器人动态感知。

137. **[Gaussian-Augmented Physics Simulation and System Identification with Complex Colliders](https://openreview.net/forum?id=hvykiwFiF8)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: sim2real
   - 解决问题: 论文解决从视频估计物体几何、外观和物理属性时，现有可微仿真难以处理任意形状刚体碰撞的问题。
   - 具体方法: 方法扩展可微材料点法，引入可微碰撞处理机制，使目标物体能与复杂刚体交互并保持端到端优化。
   - 分类理由: 贡献集中在物理仿真和系统辨识，可支撑具身系统建模，但没有直接机器人任务策略。

138. **[Actial: Activate Spatial Reasoning Ability of Multimodal Large Language Models](https://openreview.net/forum?id=jquTBzt3Av)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, world-model, robot-foundation-model
   - 解决问题: 多模态大模型在二维视觉理解上进展明显，但是否具备跨视角一致的精细三维空间推理能力仍不清楚。
   - 具体方法: 方法构建视角问答数据集，并通过监督微调、强化学习和冷启动初始化提升模型的视角表征与空间推理。
   - 分类理由: 贡献更偏空间推理数据与模型训练，不直接执行具身任务，但与机器人三维理解相关。

139. **[Adaptive Re-calibration Learning for Balanced Multimodal Intention Recognition](https://openreview.net/forum?id=k71nsscO9b)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: hri, deployment-system-reliability, benchmark
   - 解决问题: 多模态意图识别中不同模态的信息量和噪声水平不均衡，模型容易过度依赖强模态而泛化不足。
   - 具体方法: 方法从样本级和结构级两条路径重新校准模态贡献，动态遮蔽过强模态并按全局贡献调整编码器权重。
   - 分类理由: 任务与服务机器人和人机交互相关，但论文主要是通用多模态识别方法，不是完整具身系统。

140. **[Near-Optimal Sample Complexity for Online Constrained MDPs](https://openreview.net/forum?id=kYisDXzTk7)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: safety, benchmark
   - 解决问题: 论文解决安全强化学习中既要优化回报又要控制约束违背，同时保持低样本复杂度的问题。
   - 具体方法: 方法提出基于模型的原始对偶在线算法，分别处理允许小违约和严格零违约两种可行性设置，并证明样本复杂度界。
   - 分类理由: 核心是安全强化学习理论，应用可覆盖机器人但没有具体具身任务实验。

141. **[Explainably Safe Reinforcement Learning](https://openreview.net/forum?id=l6hAqx4eoB)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: safety, world-model, deployment-system-reliability
   - 解决问题: 形式化合成的安全屏蔽器可以约束强化学习动作，但其非确定性决策往往难以被人理解。
   - 具体方法: 论文用世界模型分析动作风险，构建高层风险分类决策树，并在运行时生成局部决策树解释允许或禁止的动作。
   - 分类理由: 论文核心是安全与解释性强化学习，未聚焦具体机器人任务，因此作为通用具身安全相关工作给中等相关。

142. **[Prior-Guided Diffusion Planning for Offline Reinforcement Learning](https://openreview.net/forum?id=lC4WKmTScD)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: diffusion-policy, planning, benchmark
   - 解决问题: 现有扩散规划在引导采样时可能产生次优多模态动作、分布漂移或推理成本过高，限制长程离线决策质量。
   - 具体方法: Prior Guidance 用可学习先验替代行为克隆扩散模型的高斯先验，并通过行为正则目标在潜空间训练，从而直接生成高价值轨迹。
   - 分类理由: 核心是通用离线强化学习和扩散规划，具身相关性来自轨迹生成与控制方法，但摘要未指出机器人任务。

143. **[Towards Comprehensive Scene Understanding: Integrating First and Third-Person Views for LVLMs](https://openreview.net/forum?id=m5wrqqcWbN)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: benchmark, dataset
   - 解决问题: 单一第一人称视角视野有限，缺少全局上下文，导致大视觉语言模型在空间和场景问题上出错。
   - 具体方法: 构建同步自我视角和外部视角图像问答基准，并提出无需训练的多视角场景图推理提示方法。
   - 分类理由: 任务不是机器人控制，但多视角场景理解与具身智能中的第一人称感知和空间推理高度相关。

144. **[G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems](https://openreview.net/forum?id=mmIAp3cVS0)**
   - 六类分类: `Agent/System`
   - 相关度: `medium`
   - 技术标签: benchmark
   - 解决问题: 论文解决大语言模型多智能体系统缺少细粒度协作记忆、跨轮次经验和个体化记忆的问题。
   - 具体方法: 方法构建洞察、查询和交互三层图记忆，通过双向遍历检索可泛化经验和压缩协作轨迹，并在执行后持续更新记忆。
   - 分类理由: 核心贡献是智能体系统记忆架构，具身任务只是部分验证场景，因此不是数据基准主类。

145. **[SPAZER: Spatial-Semantic Progressive Reasoning Agent for Zero-shot 3D Visual Grounding](https://openreview.net/forum?id=nfxTpNiSMH)**
   - 六类分类: `Agent/System`
   - 相关度: `medium`
   - 技术标签: benchmark, planning, spatial-memory
   - 解决问题: 论文解决零样本三维视觉定位中空间理解和语义理解割裂、复杂真实场景定位不稳的问题。
   - 具体方法: 方法让视觉语言智能体先整体分析场景并选择视角，再用锚点筛选候选物体，最后融合三维和二维图像信息做联合决策。
   - 分类理由: 贡献形态是一个面向三维定位的推理智能体系统，具身相关性来自物体查找和场景理解下游。

146. **[Learning from Videos for 3D World: Enhancing MLLMs with 3D Vision Geometry Priors](https://openreview.net/forum?id=oUYmk8WaG0)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 论文解决多模态大模型依赖点云或鸟瞰图等显式三维输入才能进行三维场景理解的问题。
   - 具体方法: 方法用三维视觉几何编码器从视频序列抽取空间先验，并与视觉标记融合后输入多模态大模型进行空间推理。
   - 分类理由: 核心是三维场景理解表示，对导航和操作有基础价值，但没有直接闭环具身任务。

147. **[PoE-World: Compositional World Modeling with Products of Programmatic Experts](https://openreview.net/forum?id=obwRcksFZw)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, planning
   - 解决问题: 传统深度世界模型需要大量数据且难以从稀疏观测快速更新，程序化世界模型又多局限于语言和网格世界。
   - 具体方法: PoE-World 使用大语言模型合成多个程序专家，并以指数加权乘积组合形成复杂随机世界模型，再嵌入模型规划智能体中评估。
   - 分类理由: 核心是世界模型和模型式规划，评估在游戏环境而非机器人场景，因此具身相关性为中等。

148. **[Extremely Simple Multimodal Outlier Synthesis for Out-of-Distribution Detection and Segmentation](https://openreview.net/forum?id=ocBuEUl6Yz)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `medium`
   - 技术标签: safety, dataset, benchmark
   - 解决问题: 安全关键场景需要识别分布外样本，但多模态异常检测缺少未知数据监督，模型容易对异常过度自信。
   - 具体方法: 论文提出特征混合方式合成多模态异常样本，并构建包含合成异常物体的仿真分割数据集。
   - 分类理由: 该工作不是专门机器人任务，且含自动驾驶数据；但主题是安全感知与异常检测，可作为具身安全评估的中等相关候选。

149. **[AutoToM: Scaling Model-based Mental Inference via Automated Agent Modeling](https://openreview.net/forum?id=oeZZusZheP)**
   - 六类分类: `Agent/System`
   - 相关度: `medium`
   - 技术标签: planning, hri, benchmark
   - 解决问题: 心智理论推理要么依赖容易出错的语言模型提示，要么依赖手工智能体模型而难以跨领域泛化。
   - 具体方法: 方法自动提出初始智能体模型，基于贝叶斯逆向规划推断心理状态，并按不确定性迭代引入新心理变量和更多时序上下文。
   - 分类理由: 主要是社会智能体推理系统，摘要明确提到可用于具身决策，但并非机器人任务专用。

150. **[EDELINE: Enhancing Memory in Diffusion-based World Models via Linear-Time Sequence Modeling](https://openreview.net/forum?id=ph1V6n7BSv)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, benchmark
   - 解决问题: 扩散世界模型虽然能生成高保真观测，但固定上下文长度限制了长期记忆，影响需要记忆的环境建模。
   - 具体方法: 论文将状态空间模型与扩散模型结合，构建统一世界模型，在多个视觉强化学习环境中验证记忆和预测能力。
   - 分类理由: 研究对象是通用强化学习世界模型，包含三维第一人称环境但不是机器人专用，因此具身相关性为中等。

151. **[ReCAP: Recursive Context-Aware Reasoning and Planning for Large Language Model Agents](https://openreview.net/forum?id=r2ykUnzuGt)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: planning, benchmark, deployment-system-reliability
   - 解决问题: 大语言模型在长程任务中容易出现上下文漂移、目标遗忘和失败循环，层级提示又可能带来跨层信息断裂或较高开销。
   - 具体方法: 框架先生成完整子任务列表，执行首个子任务并递归细化剩余计划，同时在递归返回时重新注入父级计划，并限制活动提示长度以降低成本。
   - 分类理由: 方法面向长程推理与规划，包含具身风格基准但不直接提出机器人控制系统，因此具身相关性为中等并归入通用任务。

152. **[Struct2D: A Perception-Guided Framework for Spatial Reasoning in MLLMs](https://openreview.net/forum?id=rbIlWjTFKj)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: dataset, benchmark, planning, spatial-memory
   - 解决问题: 论文解决多模态大模型在不使用显式三维输入时难以进行相对方向、路线规划和物体 grounding 等空间推理的问题。
   - 具体方法: 方法将鸟瞰图、物体标记、对象元数据和必要的第一视角关键帧组合为提示，并构建自动生成的指令微调数据集。
   - 分类理由: 主要产出是结构化输入框架和大规模调优数据，具身相关性来自路线规划与三维室内场景推理。

153. **[MaNGO — Adaptable Graph Network Simulators via Meta-Learning](https://openreview.net/forum?id=rc3XO4RARL)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: sim2real
   - 解决问题: 论文解决数据驱动物理模拟器遇到新物理参数时需要重新训练且数据收集成本高的问题。
   - 具体方法: 方法用条件神经过程编码图轨迹得到共享潜在表示，并结合神经算子减少长期模拟误差累积。
   - 分类理由: 核心是物理仿真器适应性，应用包含机器人但没有具体具身任务，相关性为中等。

154. **[SpatialLM: Training Large Language Models for Structured Indoor Modeling](https://openreview.net/forum?id=u1lNQH5upa)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `medium`
   - 技术标签: robot-foundation-model, dataset, benchmark, spatial-memory
   - 解决问题: 论文解决室内三维结构建模依赖任务专用网络、难以纳入标准多模态大模型框架的问题。
   - 具体方法: 方法从开源语言模型微调出能处理点云的模型，并用大规模合成室内场景数据训练其输出墙、门窗和物体框等结构描述。
   - 分类理由: 核心贡献是面向三维场景理解的多模态语言模型和训练数据，具身应用为重要下游但非直接控制。

155. **[SPARTAN: A Sparse Transformer World Model Attending to What Matters](https://openreview.net/forum?id=uS5ch7GjZ4)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 论文解决对象中心世界模型难以可靠发现复杂场景中局部因果交互、面对动态变化和干扰物适应性不足的问题。
   - 具体方法: 方法在对象因子化令牌之间加入注意力稀疏正则，使变换器世界模型学习上下文相关的稀疏交互图并预测未来对象状态。
   - 分类理由: 论文核心是对象交互世界模型，可支撑具身预测和规划，但没有明确机器人任务。

156. **[Rig3R: Rig-Aware Conditioning and Discovery for 3D Reconstruction](https://openreview.net/forum?id=vEFPm6gw2s)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 现有多视角重建模型常把图像视为无结构集合，无法充分利用同步相机阵列的已知或可推断结构。
   - 具体方法: 方法在模型中引入可选的相机编号、时间和位姿等阵列元数据，并联合预测点图、全局位姿射线图和阵列中心射线图来恢复场景与相机结构。
   - 分类理由: 核心是多相机三维重建、相机位姿估计和阵列发现；具身相关性来自机器人或车辆的视觉感知，但不涉及具体控制任务。

157. **[Zero-shot World Models via Search in Memory](https://openreview.net/forum?id=vHaShO76T8)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 论文关注传统神经网络世界模型需要训练且可能在长时域预测中受限的问题，希望在视觉环境中更高效地预测未来动态。
   - 具体方法: 论文利用相似性搜索和随机表示从记忆中近似世界模型，不经过显式训练，并与经典模型式强化学习世界模型进行潜变量重建、图像相似度和长程动态预测比较。
   - 分类理由: 核心贡献是世界模型和环境动态表示，而非具体机器人策略或控制器；虽然实验主要是视觉强化学习环境，不一定是真实机器人，但世界模型是具身智能规划和交互的重要基础，因此具身相关性为中等。

158. **[World Models as Reference Trajectories for Rapid Motor Adaptation](https://openreview.net/forum?id=xj0DXLQZCS)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `medium`
   - 技术标签: world-model, planning
   - 解决问题: 论文关注已学习控制策略在真实部署时遇到系统动力学变化会性能下降、重新训练成本高的问题，目标是在连续控制场景中实现低开销快速适应。
   - 具体方法: 方法提出反射式世界模型框架，将长期强化学习奖励最大化与无奖励的潜空间快速控制分离，用世界模型预测提供隐式参考轨迹，从而在动力学变化时快速进行误差修正。
   - 分类理由: 论文核心是控制与快速运动适应，而世界模型是服务于控制执行的参考机制；摘要未指明具体机器人形态或任务，因此任务轴标为跨任务具身控制。

159. **[ORIGAMISPACE: Benchmarking Multimodal LLMs in Multi-Step Spatial Reasoning with Mathematical Constraints](https://openreview.net/forum?id=y7ahj9RoXQ)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: benchmark, dataset, planning
   - 解决问题: 现有多模态大模型在需要多步空间推理和精确数学约束的复杂任务上缺乏系统评测。
   - 具体方法: ORIGAMISPACE 构建包含折痕图、折叠过程和最终形状的数据集，并设计图案预测、空间关系预测和代码生成等评测任务。
   - 分类理由: 论文是空间推理基准，非机器人任务，但多步空间推理是具身智能的重要基础能力，因此为中等相关。

160. **[Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting](https://openreview.net/forum?id=ycPVp0577R)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model, spatial-memory
   - 解决问题: 论文解决二维解析方法在三维开放词表查询中多视角不一致、动态场景对象与高斯表示错配的问题。
   - 具体方法: 方法先按对象划分高斯集合再进行重建，使场景天然形成对象级三维分割，并为对象分配语言嵌入以支持开放词表查询。
   - 分类理由: 核心是三维场景对象表示与语义查询能力，虽未直接控制机器人，但属于具身感知表示的通用支撑。

161. **[Reinforcing Spatial Reasoning in Vision-Language Models with Interwoven Thinking and Visual Drawing](https://openreview.net/forum?id=yyWeSAsOhs)**
   - 六类分类: `Foundation/VLA Model`
   - 相关度: `medium`
   - 技术标签: navigation, planning, benchmark
   - 解决问题: 现有多模态推理方法过度依赖文本链式推理，面对需要几何理解和连续空间跟踪的任务时能力不足。
   - 具体方法: 方法为模型提供边界框标注和辅助线绘制等基础视觉操作，并通过合成冷启动、反思式拒绝采样和强化学习三阶段训练培养空间推理能力。
   - 分类理由: 论文主体是大视觉语言模型空间推理能力增强，包含迷宫导航、多视角和视频推理基准，但不是直接机器人控制论文。

162. **[Spatially-aware Weights Tokenization for NeRF-Language Models](https://openreview.net/forum?id=z9MxyboJ7R)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: dataset, benchmark, spatial-memory
   - 解决问题: 论文解决直接用全局权重表示理解神经辐射场时，难以进行局部细节和空间关系推理的问题。
   - 具体方法: 方法提出自监督元编码器从神经辐射场权重中生成空间令牌，并构建面向描述和问答的多模态模型与空间标注数据。
   - 分类理由: 核心是三维对象空间表示与语言理解，机器人价值为间接感知支撑。

163. **[Learnable Burst-Encodable Time-of-Flight Imaging for High-Fidelity Long-Distance Depth Sensing](https://openreview.net/forum?id=zL4ifL17bU)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: 无
   - 解决问题: 论文解决远距离飞行时间深度成像中相位缠绕、信噪比下降和硬件可实现性之间的矛盾。
   - 具体方法: 方法提出脉冲串编码飞行时间成像，并端到端联合优化编码函数和深度重建网络，同时加入硬件约束项。
   - 分类理由: 核心贡献是深度传感与成像范式，不是具身策略本身，但可作为机器人感知模块。

164. **[OpenHype: Hyperbolic Embeddings for Hierarchical Open-Vocabulary Radiance Fields](https://openreview.net/forum?id=zQmXDUbZ5D)**
   - 六类分类: `World Model/Representation`
   - 相关度: `medium`
   - 技术标签: world-model
   - 解决问题: 现有隐式三维场景表示难以高效表达开放世界中的层级结构，离散闭集层级也难以泛化到真实复杂场景。
   - 具体方法: OpenHype 使用连续双曲潜空间表示场景层级，借助双曲几何编码多尺度关系，并通过测地路径实现层级平滑遍历。
   - 分类理由: 核心是三维场景层级表示，对具身环境理解有潜在价值，但摘要没有具体机器人任务或交互实验。

165. **[SAVVY: Spatial Awareness via Audio-Visual LLMs through Seeing and Hearing](https://openreview.net/forum?id=zwCb9cKHpd)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `medium`
   - 技术标签: benchmark, spatial-memory, navigation
   - 解决问题: 现有视听大模型和基准多关注静态或二维场景，缺少对动态三维方向、距离和时间定位的系统评估。
   - 具体方法: 论文构建包含同步空间音频的三维问答基准，并通过自我中心空间轨迹估计和动态全局地图构建来回答空间关系问题。
   - 分类理由: 核心贡献是空间推理基准和评测流程，具备具身感知价值，但没有直接机器人任务或控制闭环。

166. **[Asymptotically Stable Quaternion-valued Hopfield-structured Neural Network with Periodic Projection-based Supervised Learning Rules](https://openreview.net/forum?id=2FmTcj6WMB)**
   - 六类分类: `World Model/Representation`
   - 相关度: `low`
   - 技术标签: planning
   - 解决问题: 四元数适合表示旋转和姿态，但在霍普菲尔德结构神经网络中保持稳定性和四元数一致性并不容易。
   - 具体方法: 方法将连续时间霍普菲尔德网络扩展到四元数域，并用周期投影学习规则保持权重结构和收敛性质。
   - 分类理由: 摘要仅将机器人手臂控制和路径规划作为潜在应用，主要贡献是数学神经网络模型，因此具身相关性较低。

167. **[Modelling the control of offline processing with reinforcement learning](https://openreview.net/forum?id=BFW1fkB8ck)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `low`
   - 技术标签: world-model, planning
   - 解决问题: 论文解决大脑或智能体如何在离线阶段选择记忆重放、抽象和生成式模拟来提升未来行为的问题。
   - 具体方法: 方法训练元控制器在睡眠阶段调度低层智能体的离线学习过程，包括近期记忆学习、世界模型抽象和生成数据学习。
   - 分类理由: 包含迷宫求解等行为任务和世界模型概念，但核心是神经科学建模，不是机器人系统。

168. **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://openreview.net/forum?id=O1MHVstfBQ)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `low`
   - 技术标签: dataset, benchmark, world-model
   - 解决问题: 论文解决增强现实和三维场景对象合成中多视角一致、光照阴影协调和规模化训练困难的问题。
   - 具体方法: 方法提出两阶段前馈框架，直接建模光照和阴影，并用空间映射对齐二维图像输入与三维高斯场景表示，同时构建大规模合成数据集。
   - 分类理由: 核心是图形合成和数据集，不是机器人任务；具身价值主要来自仿真和增强现实素材。

169. **[Seeing the Arrow of Time in Large Multimodal Models](https://openreview.net/forum?id=OYciB30Z4n)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `low`
   - 技术标签: benchmark
   - 解决问题: 大多模态模型对视频中时间不可逆性理解不足，影响其回答需要时间方向感知的问题。
   - 具体方法: 论文构建时间方向基准，并设计带反向奖励的强化学习训练策略，使模型对正放和倒放视频形成不同解释以增强时间感知。
   - 分类理由: 论文主要是通用视频问答和多模态时间理解，不直接涉及机器人任务；具身相关性来自物理事件时序理解的潜在价值。

170. **[Safely Learning Controlled Stochastic Dynamics](https://openreview.net/forum?id=QQybz4enRc)**
   - 六类分类: `Safety/Evaluation`
   - 相关度: `low`
   - 技术标签: safety, deployment-system-reliability
   - 解决问题: 在学习受控随机动力学时，训练和部署过程都需要系统轨迹始终保持在预定义安全区域内。
   - 具体方法: 方法从初始安全控制集合出发，利用核置信界逐步扩展可安全探索的控制集合，同时学习动力学并支持对任意控制进行安全验证。
   - 分类理由: 论文强调安全探索和动力学估计理论，应用包括机器人但没有具身任务实验，因此只给低相关。

171. **[Scaling RL to Long Videos](https://openreview.net/forum?id=TxedB8hI5O)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `low`
   - 技术标签: dataset, benchmark, deployment-system-reliability
   - 解决问题: 长视频视觉语言模型强化学习面临数据、训练流程和基础设施瓶颈，难以处理小时级视频和大量帧。
   - 具体方法: 论文构建长视频问答推理数据集，采用链式思维监督微调加强化学习，并设计面向长视频的多模态序列并行训练基础设施。
   - 分类理由: 核心是通用长视频理解和训练系统，缺少机器人或物理交互任务；仅因长时序视觉推理对具身智能有潜在价值而保留低相关。

172. **[MetaGS: A Meta-Learned Gaussian-Phong Model for Out-of-Distribution 3D Scene Relighting](https://openreview.net/forum?id=UXc87Orcri)**
   - 六类分类: `World Model/Representation`
   - 相关度: `low`
   - 技术标签: world-model
   - 解决问题: 论文解决三维重光照方法在未见光照分布下几何和外观重建退化的问题。
   - 具体方法: 方法用元学习训练三维高斯表示，并嵌入物理反射先验来解耦阴影和外观成分。
   - 分类理由: 核心是三维视觉重建与渲染，不是具身任务；仅作为环境表示或仿真资产间接相关。

173. **[Restage4D: Reanimating Deformable 3D Reconstruction from a Single Video](https://openreview.net/forum?id=e50L5Mx93u)**
   - 六类分类: `World Model/Representation`
   - 相关度: `low`
   - 技术标签: world-model
   - 解决问题: 生成视频用于四维重建时常出现几何伪影、不合理运动和遮挡问题，导致重建缺乏物理一致性。
   - 具体方法: 方法利用原始未编辑视频作为额外监督，通过视频回放训练、遮挡感知刚性正则和反遮挡回溯补全机制提升动态重建稳定性。
   - 分类理由: 核心是通用可变形三维重建与视频生成纠错，具身相关性仅来自动态场景表示潜力，没有机器人任务验证。

174. **[Interactive Cross-modal Learning for Text-3D Scene Retrieval](https://openreview.net/forum?id=fohuurA03P)**
   - 六类分类: `World Model/Representation`
   - 相关度: `low`
   - 技术标签: dataset
   - 解决问题: 论文解决文本三维场景检索中用户查询信息不完整导致检索对齐不足的问题。
   - 具体方法: 方法通过多轮问答交互补充场景描述，再在特征和语义层面融合交互文本以重排序三维场景，并用适配训练缩小查询域差距。
   - 分类理由: 论文没有机器人动作或交互闭环，主要是三维检索任务，因此仅弱相关。

175. **[Open-Vocabulary Part Segmentation via Progressive and Boundary-Aware Strategy](https://openreview.net/forum?id=gwT1GOKiaO)**
   - 六类分类: `World Model/Representation`
   - 相关度: `low`
   - 技术标签: robot-foundation-model
   - 解决问题: 开放词汇部件分割在结构相连的物体部件边界处容易混淆，连续图像特征与离散分类机制之间存在冲突。
   - 具体方法: PBAPS 采用训练自由流程，利用物体部件结构知识进行从整体到部件的渐进分割，并通过边界感知细化模块处理不确定边界区域。
   - 分类理由: 方法本身是通用图像分割，并未体现机器人任务或三维交互；但部件理解对操作具有间接价值，因此保留低相关。

176. **[Regret Lower Bounds for Decentralized Multi-Agent Stochastic Shortest Path Problems](https://openreview.net/forum?id=lDh9wSb9nP)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `low`
   - 技术标签: planning
   - 解决问题: 去中心化多智能体随机最短路问题在学习复杂度和理论下界方面研究不足，难以理解分布式控制的固有难度。
   - 具体方法: 论文在线性函数逼近设定下分析去中心化多智能体随机最短路，利用对称性论证刻画最优策略结构，并构造难学习实例给出遗憾下界。
   - 分类理由: 贡献主要是强化学习理论，虽提及群体机器人等应用，但没有具体具身实验或机器人系统，因此仅为低相关。

177. **[Zero-Shot Context Generalization in Reinforcement Learning from Few Training Contexts](https://openreview.net/forum?id=s14llhrkjA)**
   - 六类分类: `Policy/Control/Planning`
   - 相关度: `low`
   - 技术标签: planning
   - 解决问题: 论文解决深度强化学习策略在训练上下文很少时，面对环境参数变化容易泛化失败的问题。
   - 具体方法: 论文提出上下文增强贝尔曼方程，并由此推导上下文样本增强方法，用数据增强方式近似多上下文训练效果，提升确定性控制环境中的零样本泛化能力。
   - 分类理由: 论文核心是通用强化学习理论和数据增强方法，摘要只将机器人作为应用领域之一，并未聚焦真实机器人、具身感知或具体具身任务；因此仅作为低相关的通用策略学习方法保留。

178. **[Latent Mixture of Symmetries for Sample-Efficient Dynamic Learning](https://openreview.net/forum?id=t7NLyOtPEi)**
   - 六类分类: `World Model/Representation`
   - 相关度: `low`
   - 技术标签: world-model
   - 解决问题: 论文关注在观测有限、环境变化的动力系统中，如何避免单一全局对称假设导致的表达不足和误差累积。
   - 具体方法: 方法提出潜在对称混合模型，在局部保持不同对称变换，并通过多时间尺度层次结构捕获长期时间等价关系。
   - 分类理由: 核心贡献是通用动力学表示学习而非具体机器人任务，因此具身相关性较弱，但可服务模型预测控制和安全分析。

179. **[Balanced Token Pruning: Accelerating Vision Language Models Beyond Local Optimization](https://openreview.net/forum?id=tle6DK5Tad)**
   - 六类分类: `Agent/System`
   - 相关度: `low`
   - 技术标签: deployment-system-reliability, benchmark
   - 解决问题: 大视觉语言模型使用大量图像令牌，动态高分辨率输入会造成显著计算负担。
   - 具体方法: 方法用小规模校准集分阶段剪枝视觉令牌，前期重视对后续层的全局影响，后期重视当前层输出一致性。
   - 分类理由: 论文是通用视觉语言模型加速方法，没有直接具身任务或机器人实验，因此具身相关性较低。

180. **[Multi-scale Temporal Prediction via Incremental Generation and Multi-agent Collaboration](https://openreview.net/forum?id=wTBhWbCRpN)**
   - 六类分类: `Data/Benchmark/Simulation`
   - 相关度: `low`
   - 技术标签: benchmark, planning
   - 解决问题: 论文解决视觉语言模型难以在多个时间尺度和状态粒度上预测场景未来状态的问题。
   - 具体方法: 方法构建多尺度时间预测任务和基准，并提出增量生成与多智能体协作框架，同步生成视觉预览和状态判断。
   - 分类理由: 摘要声称连接具身智能，但主要场景包含通用和手术视频预测，未体现机器人闭环控制。


## 抓取状态

- `neurips_virtual_page`: ok / html / 5858 poster links
- `openreview`: ok / api2 / 5286 篇
- `classifier`: ok_after_retry / traecli / selected 319 / rejected 4967
- `prefilter`: neurips-embodied-title-abstract-gate / rule_selected 725 / candidates 372 / cheap_rejected 4914
- `traecli`: model GPT-5.5 / thinking high / verbosity high / calls 12 / cache_hits 0 / batch 40
- `retry_errors`:
  - embodied: batch size=12 failed: traecli assistant content parse failed: expected JSON object
  - embodied: batch size=6 failed: Expecting value: line 1 column 1 (char 0)
