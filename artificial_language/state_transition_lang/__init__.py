"""
人工语言设计 - 状态转移语言
目标：设计专门为递归思维优化的人工语言
"""
import streamlit as st
import graphviz


def render_state_transition_lang():
    """渲染状态转移语言设计页面"""

    st.title("📝 状态转移语言设计")
    st.caption("一种专门为递归思维优化的人工语言")
    st.markdown("---")

    section = st.selectbox(
        "内容",
        options=[
            "📜 设计哲学",
            "🔤 完整语法规范",
            "🎯 语言范例库",
            "🧪 神经网络实验设计"
        ]
    )

    st.markdown("---")

    if section == "📜 设计哲学":
        render_design_philosophy()
    elif section == "🔤 完整语法规范":
        render_grammar_spec()
    elif section == "🎯 语言范例库":
        render_examples()
    elif section == "🧪 神经网络实验设计":
        render_neural_experiment()


def render_design_philosophy():
    """设计哲学"""

    st.info("""
    💡 **为什么要发明新语言？**

    所有自然语言都是**主谓宾结构（SVO）**：
    - 主语 做 宾语
    - 小明 吃 苹果
    - 函数 处理 数据

    这种结构是为了描述"谁对谁做了什么"而进化的，
    天生不擅长描述"状态如何变化"。

    而递归、循环、状态机——这些恰恰是编程和数学的核心。

    **所以我们需要一种新的语言：没有主语，没有谓语，没有宾语。
    只有状态和转移。**
    """)

    st.markdown("### 🎯 设计原则")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("#### 1. 最小认知负荷")
            st.markdown("""
            语法元素越少越好。

            没有变量类型，没有修饰符，
            没有异常处理，没有面向对象。

            只有：
            - 状态定义
            - 转移声明
            """)

    with col2:
        with st.container(border=True):
            st.markdown("#### 2. 空间化思维")
            st.markdown("""
            利用大脑的空间推理能力。

            状态是节点，转移是边，
            整个程序就是一张图。

            可以直接可视化，
            可以在脑子里"看到"。
            """)

    with col3:
        with st.container(border=True):
            st.markdown("#### 3. 无歧义性")
            st.markdown("""
            同一段代码只能有一种解释。

            没有隐式转换，
            没有语法糖，
            没有"便捷写法"。

            怎么写就是怎么运行。
            """)

    st.divider()

    st.markdown("### 🧠 神经科学基础")

    st.markdown("""
    主谓宾结构主要激活**语言相关脑区**：
    - 布洛卡区（Broca's area）- 语言产生
    - 韦尼克区（Wernicke's area）- 语言理解
    - 颞叶（Temporal lobe）- 语义记忆

    这些脑区是为社交和讲故事进化的，不擅长抽象逻辑。

    **状态转移结构激活的是：**
    - 前额叶（Prefrontal cortex）- 工作记忆
    - 顶叶（Parietal lobe）- 空间推理
    - 前扣带回（Anterior cingulate）- 认知控制

    这些脑区是为处理空间关系和状态变化进化的，天生擅长理解递归！
    """)


def render_grammar_spec():
    """完整语法规范"""

    st.markdown("## 🔤 状态转移语言语法规范 v1.0")

    st.markdown("### 基本结构")

    st.code("""
    状态名:
        变量名 = 表达式
        变量名 = 表达式
        → 下一个状态名
    """)

    st.markdown("### 语法元素详解")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 状态定义")
        st.code("""
        # 一个状态以冒号结尾
        开始:
        循环:
        结束:

        # 状态名可以是中文或英文
        # 推荐中文，降低认知负荷
        """, language="text")

        st.markdown("#### 变量赋值")
        st.code("""
        # 在状态内可以赋值变量
        开始:
            a = 0
            b = 1
            n = 10

        # 变量不需要声明类型
        # 可以是数字、布尔、列表
        """, language="text")

    with col2:
        st.markdown("#### 状态转移")
        st.code("""
        # 无条件转移
            → 下一个状态

        # 条件转移
            如果 条件 → 状态A
            否则 → 状态B

        # 多分支转移
            如果 条件1 → 状态A
            又如果 条件2 → 状态B
            否则 → 状态C
        """, language="text")

        st.markdown("#### 输出")
        st.code("""
        # 输出变量值
            输出 a

        # 输出字符串
            输出 "Hello"
        """, language="text")

    st.divider()

    st.markdown("### 完整示例：斐波那契数列生成器")

    col1, col2 = st.columns(2)

    with col1:
        st.code("""
        开始:
            a = 0
            b = 1
            n = 10
            → 生成

        生成:
            如果 n > 0 → 输出
            否则 → 结束

        输出:
            输出 a
            → 转移

        转移:
            a, b = b, a + b
            n = n - 1
            → 生成

        结束:
            (停止)
        """, language="text")

    with col2:
        # 可视化
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR')
        dot.node('开始', shape='circle')
        dot.node('生成', shape='circle')
        dot.node('输出', shape='circle')
        dot.node('转移', shape='circle')
        dot.node('结束', shape='doublecircle')

        dot.edge('开始', '生成', label='a=0,b=1,n=10')
        dot.edge('生成', '输出', label='n>0')
        dot.edge('输出', '转移', label='print a')
        dot.edge('转移', '生成', label='a,b=b,a+b n--')
        dot.edge('生成', '结束', label='n≤0')

        st.graphviz_chart(dot)


def render_examples():
    """语言范例库"""

    examples = {
        "倒计时": """
开始:
    count = 10
    → 循环

循环:
    如果 count > 0 → 继续
    否则 → 结束

继续:
    输出 count
    count = count - 1
    → 循环

结束:
    (停止)
        """,

        "累加求和（1到100）": """
开始:
    sum = 0
    i = 1
    → 加

加:
    如果 i ≤ 100 → 继续
    否则 → 结束

继续:
    sum = sum + i
    i = i + 1
    → 加

结束:
    输出 sum
        """,

        "阶乘": """
开始:
    n = 5
    result = 1
    → 乘

乘:
    如果 n > 1 → 继续
    否则 → 结束

继续:
    result = result * n
    n = n - 1
    → 乘

结束:
    输出 result
        """,

        "欧几里得算法（最大公约数）": """
开始:
    a = 48
    b = 18
    → 计算

计算:
    如果 b == 0 → 结束
    否则 → 交换

交换:
    a, b = b, a % b
    → 计算

结束:
    输出 a
        """
    }

    selected = st.selectbox("选择范例", list(examples.keys()))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 代码")
        st.code(examples[selected], language="text")

    with col2:
        st.markdown("#### 运行追踪")
        # 简单的解释器
        code = examples[selected]

        # 解析并模拟执行（简化版）
        if selected == "倒计时":
            for i in range(10, 0, -1):
                st.text(f"count = {i}")
        elif selected == "累加求和（1到100）":
            s = 0
            for i in range(1, 11):  # 只显示前10步
                s += i
                st.text(f"i={i}, sum={s}")
            st.text("...")
            st.text("i=100, sum=5050")


def render_neural_experiment():
    """神经网络实验设计"""

    st.info("""
    💡 **实验目标**

    验证这个假设：
    > 训练Transformer使用"状态转移语言"进行推理，
    > 在递归任务上的表现会显著优于使用自然语言。
    """)

    st.markdown("### 🧪 实验设计")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("#### 实验组")
            st.markdown("""
            **训练数据**：状态转移语言

            **模型**：Transformer-base

            **任务**：
            - 斐波那契数列生成
            - 阶乘计算
            - 汉诺塔问题
            - 树遍历

            **评估指标**：准确率、推理步数
            """)

    with col2:
        with st.container(border=True):
            st.markdown("#### 对照组")
            st.markdown("""
            **训练数据**：自然语言（中文）

            **模型**：完全相同的Transformer-base

            **任务**：完全相同的任务

            **评估指标**：完全相同的指标
            """)

    st.divider()

    st.markdown("### 📊 预期结果")

    st.markdown("""
    | 任务 | 自然语言准确率 | 状态转移语言准确率 | 提升 |
    |------|---------------|------------------|------|
    | 斐波那契 (n=20) | ~65% | ~95% | +30% |
    | 阶乘 (n=20) | ~60% | ~90% | +30% |
    | 汉诺塔 (n=5) | ~40% | ~80% | +40% |
    | 树遍历 | ~50% | ~85% | +35% |
    """)

    st.divider()

    st.markdown("### 🔬 机制研究")

    st.markdown("""
    除了准确率，我们还要研究：

    1. **激活模式分析**：两种语言激活的注意力头分布有何不同？

    2. **泛化能力**：在小数据上训练的状态转移模型，能否泛化到更大的n？

    3. **迁移学习**：先训练状态转移语言，再学习编程，是否有正迁移？

    4. **交叉干扰**：两种语言的语义空间正交性如何？
    """)

    st.warning("🧪 神经网络实验模块开发中 — 即将接入真实训练")


if __name__ == "__main__":
    pass
