"""
元语言计划 - MetaLanguage Project
通过神经网络模拟语言如何塑造人类思维
主程序入口
"""
import streamlit as st
import random
from pathlib import Path
import sys

# 设置页面配置
st.set_page_config(
    page_title="元语言计划 | MetaLanguage Project",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

# 导入各个模块
from 神经网络实验.母语锚定网络 import render_neural_simulation
from 人类训练工具.外语直接思考训练 import render_foreign_language
from 人类训练工具.递归思维训练 import render_recursion_training
from 人类训练工具.数学语言推理 import render_math_reasoning
from 人工语言设计.状态转移语 import render_state_transition_lang


def main():
    # 初始化会话状态
    if 'user_id' not in st.session_state:
        st.session_state.user_id = "explorer"
    if 'native_language' not in st.session_state:
        st.session_state.native_language = "中文（锚定）"

    # 侧边栏导航
    with st.sidebar:
        st.title("🧠 元语言计划")
        st.caption("MetaLanguage Project")

        st.divider()

        page = st.radio(
            "研究方向",
            options=[
                "🏠 项目概览",
                "🧬 神经网络模拟",
                "🔤 外语直接思考训练",
                "∞ 递归思维增强",
                "∑ 数学语言推理",
                "📝 人工语言设计",
                "📊 实验数据中心",
                "🔬 研究方法论"
            ]
        )

        st.divider()

        # 母语锚定设置
        with st.expander("🔗 母语锚定", expanded=True):
            st.info("""
            **母语是不可改变的认知锚点**

            所有后续语言学习都建立在母语的神经结构之上。
            本项目的核心目标：找到绕过母语翻译、实现独立思考的方法。
            """)
            native_lang = st.selectbox(
                "你的母语（锚定）",
                options=["中文", "English", "日本語", "Deutsch"]
            )

        # 核心理念
        st.success("""
        💡 **核心假设**

        语言的结构决定思维的边界。

        通过设计特殊语言并训练神经网络（及人类）使用其思考，
        我们可以系统性地增强特定认知能力。
        """)

    # 页面路由
    if page == "🏠 项目概览":
        render_project_overview()
    elif page == "🧬 神经网络模拟":
        render_neural_simulation()
    elif page == "🔤 外语直接思考训练":
        render_foreign_language()
    elif page == "∞ 递归思维增强":
        render_recursion_training()
    elif page == "∑ 数学语言推理":
        render_math_reasoning()
    elif page == "📝 人工语言设计":
        render_state_transition_lang()
    elif page == "📊 实验数据中心":
        render_data_center()
    elif page == "🔬 研究方法论":
        render_methodology()


def render_project_overview():
    """渲染项目概览首页"""

    # Hero Section
    st.title("🧠 元语言计划")
    st.subheader("MetaLanguage Project — 探索语言如何塑造思维")

    st.markdown("---")

    # 核心理念
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        ## 🎯 研究使命

        我们正在验证一个革命性的假设：

        > **语言的语法结构直接决定其使用者的推理模式和认知能力。**

        如果这个假设成立，我们就可以：
        - 🔓 通过学习特殊设计的语言，突破母语的认知局限
        - 🚀 系统性地增强递归理解、逻辑推理等高级思维能力
        - 📚 实现"用外语直接思考"，彻底改变外语学习方式

        这不仅仅是语言学研究——这是**认知增强工程**。
        """)

    with col2:
        st.image("https://picsum.photos/seed/neuroscience/400/300", caption="语言塑造神经通路")

    st.markdown("---")

    # 三个平行研究方向
    st.header("🔬 三大研究方向")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🔤 外语直接思考")
            st.markdown("""
            **目标**：让你在考试时直接用英语思考，无需中文翻译

            **原理**：
            - 强制"无中文"沉浸式环境
            - 建立英文概念↔英文概念的直接联结
            - 模拟真实考试场景训练
            """)
            if st.button("开始训练 →", key="btn_english"):
                st.switch_page("app.py")

    with col2:
        with st.container(border=True):
            st.markdown("### ∞ 递归思维增强")
            st.markdown("""
            **目标**：通过"状态-转移"语言直观理解递归

            **原理**：
            - 主谓宾结构不擅长表达递归
            - 设计基于状态和转移的人工语言
            - 训练后递归任务准确率显著提升
            """)
            if st.button("探索人工语言 →", key="btn_recursion"):
                st.switch_page("app.py")

    with col3:
        with st.container(border=True):
            st.markdown("### ∑ 数学语言推理")
            st.markdown("""
            **目标**：用形式语言替代中文的模糊思维

            **原理**：
            - 自然语言本质是模糊的、联想式的
            - 数学/逻辑语言是精确的、演绎式的
            - 训练用符号语言进行推理
            """)
            if st.button("开始推理练习 →", key="btn_math"):
                st.switch_page("app.py")

    st.divider()

    # 技术架构说明
    st.header("🏗 技术架构")

    st.markdown("""
    ```
                        ┌─────────────────────────────────┐
                        │         母语锚定网络             │
                        │  (固定权重 - 模拟不可改变的母语)  │
                        └─────────────┬───────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
    ┌─────────▼─────────┐   ┌─────────▼─────────┐   ┌─────────▼─────────┐
    │   英语子网络      │   │   状态转移语言    │   │   数学语言子网络  │
    │  (独立思考模式)   │   │  (递归增强训练)   │   │  (符号推理训练)   │
    └─────────┬─────────┘   └─────────┬─────────┘   └─────────┬─────────┘
              │                       │                       │
              └───────────────────────┼───────────────────────┘
                                    │
                      ┌─────────────▼───────────────────┐
                      │      认知表现评估层              │
                      │  - 推理任务准确率                │
                      │  - 反应时间差异                  │
                      │  - 思维模式特征提取              │
                      └─────────────────────────────────┘
    ```
    """)

    st.divider()

    # 核心实验
    st.header("🧪 关键实验")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### 实验1：母语锚定的不可逆性

        **假设**：先训练中文网络，再训练英语，会观察到中文语义空间的"引力效应"。

        **方法**：测量双语激活向量的正交性。

        **预期结果**：后学的语言会向母语的语义空间靠拢，无法完全独立。
        """)

    with col2:
        st.markdown("""
        #### 实验2：状态转移语言对递归的增强

        **假设**：训练"状态-转移"语言的网络，在递归任务上的表现显著优于主谓宾语言。

        **方法**：斐波那契、汉诺塔、树遍历等任务的准确率对比。

        **预期结果**：状态转移语言组准确率提升30%以上。
        """)

    st.divider()

    # 为什么这很重要
    st.header("💡 为什么这很重要")

    st.markdown("""
    如果我们的假设被验证，这将带来：

    1. **外语教育革命** —— 人人都可以获得"直接用外语思考"的能力，告别"哑巴英语"

    2. **认知增强技术** —— 通过学习特殊设计的人工语言，系统性增强数学、编程等抽象思维

    3. **思维自由** —— 认识到母语的认知牢笼，并有意识地选择最适合当前问题的"思考语言"

    > "能用不同的语言思考，就等于拥有多个灵魂。"
    """)


def render_neural_simulation():
    """渲染神经网络模拟页面"""

    st.title("🧬 神经网络模拟")
    st.markdown("---")

    st.markdown("""
    ## 实验环境配置

    我们使用Transformer架构模拟语言习得过程，核心创新是**"母语锚定 + 子网络隔离"**机制：
    """)

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("🔗 母语锚定网络")
            st.selectbox(
                "母语选择",
                options=["中文 (12层, 768d)", "English (12层, 768d)"],
                index=0
            )
            st.info("""
            母语网络一旦训练完成，权重将被**冻结**，模拟母语在大脑中不可改变的认知基础。
            """)
            st.slider("锚定强度", 0.0, 1.0, 0.8,
                     help="子网络向母语语义空间靠拢的倾向")

    with col2:
        with st.container(border=True):
            st.subheader("🌐 训练子网络")
            st.multiselect(
                "同时训练的语言",
                options=["English", "状态转移语", "λ演算语言", "日语", "德语"],
                default=["English", "状态转移语"]
            )
            st.info("""
            每个子网络有独立的注意力头，但共享底层嵌入。
            训练时通过梯度隔离确保子网络的独立性。
            """)

    st.divider()

    st.subheader("📊 训练状态监控")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("英语子网络独立性", "67%", "+5%",
                 delta_color="normal",
                 help="与母语语义空间的正交度，越高越独立")

    with col2:
        st.metric("递归任务准确率", "78%", "+12%",
                 delta_color="normal",
                 help="状态转移语训练后的递归任务表现")

    with col3:
        st.metric("跨语言干扰度", "23%", "-8%",
                 delta_color="inverse",
                 help="切换语言时母语通路的激活程度，越低越好")

    st.divider()

    with st.expander("🔬 详细实验设计", expanded=True):
        st.markdown("""
        ### 实验1：母语锚定的不可逆性

        **对照组A**：先训练中文，再训练英文
        **对照组B**：先训练英文，再训练中文
        **实验组**：同时训练中英双语

        **测量指标**：
        - 语义空间夹角（正交度）
        - 概念对齐程度
        - 切换语言时的激活模式

        **预期结果**：先学的语言会对后学的语言产生"引力"，语义空间无法完全正交。
        """)

    st.warning("🧪 神经网络模拟模块开发中 — 即将接入真实的模型训练")


def render_data_center():
    """渲染实验数据中心"""

    st.title("📊 实验数据中心")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("🧬 神经网络实验数据")
            st.metric("已完成实验", "12")
            st.metric("训练步数", "1.2M")
            st.metric("模型检查点", "48")
            st.json({
                "实验1_母语锚定": "完成",
                "实验2_递归增强": "进行中",
                "实验3_外语直接思考": "待开始"
            }, expanded=False)

    with col2:
        with st.container(border=True):
            st.subheader("👤 人类受试者数据")
            st.metric("受试者数量", "0 (等待招募)")
            st.metric("训练总时长", "0小时")
            st.info("""
            人类对照实验即将开始招募。

            实验组：使用本平台的"外语直接思考"训练法
            对照组：使用传统翻译法学外语
            """)

    st.divider()

    st.info("📊 数据中心模块开发中 — 即将接入实验可视化")


def render_methodology():
    """渲染研究方法论页面"""

    st.title("🔬 研究方法论")
    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs([
        "核心研究假说",
        "实验设计原则",
        "认知评估指标",
        "伦理与隐私"
    ])

    with tab1:
        st.markdown("""
        ## 四个递进的研究假说

        ### H1：母语锚定假说（强）
        > 人类的第一语言构建了不可磨灭的基础认知结构，所有后续语言学习都无法完全摆脱母语的映射。

        ### H2：语言决定思维（弱萨丕尔-沃尔夫）
        > 不同语言的语法结构（时态、量词、语态等）直接塑造使用者的推理模式和认知偏好。

        ### H3：独立思考的可能性
        > 通过特定训练方法，神经网络（及人类）可以获得"用外语直接思考"的能力，显著降低母语翻译依赖。

        ### H4：人工语言的认知增强
        > 设计特殊语法的人工语言，可以系统性地增强特定认知能力（递归理解、逻辑推理等）。
        """)

    with tab2:
        st.markdown("""
        ## 实验设计原则

        ### 双盲对照
        - 实验组：使用本项目开发的训练方法
        - 对照组：使用传统学习方法
        - 评估者不知道分组情况

        ### 严格控制变量
        - 匹配年龄、教育水平、初始语言能力
        - 相同的训练时长
        - 相同的测试材料

        ### 可重复性
        - 所有实验材料开源
        - 所有数据分析代码公开
        - 详细记录每一个参数设置
        """)

    with tab3:
        st.markdown("""
        ## 认知评估指标体系

        ### 客观指标
        - **反应时间**：完成任务的速度（跨语言差异）
        - **准确率**：任务正确率
        - **错误模式**：错误类型的分布差异
        - **眼动追踪**：阅读/思考时的眼动模式

        ### 主观指标
        - **自我报告**：是否感觉到"直接思考"
        - **思维报告**：出声思考（think-aloud）的内容分析
        - **元认知判断**：对自己答案的信心程度

        ### 神经指标（未来）
        - fMRI：不同语言激活的脑区
        - EEG：语言切换时的脑电信号
        """)

    with tab4:
        st.markdown("""
        ## 伦理与隐私

        ### 数据隐私
        - 🔒 所有用户数据默认本地存储
        - ✅ 用户可选择是否贡献数据
        - 📦 贡献数据将经过严格匿名化
        - 🗑 用户随时可导出或删除数据

        ### 研究伦理
        - 所有受试者签署知情同意书
        - 实验无任何有害风险
        - 受试者可随时退出
        - 研究结果将完全公开
        """)


if __name__ == "__main__":
    main()
