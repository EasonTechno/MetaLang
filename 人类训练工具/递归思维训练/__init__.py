"""
人类训练工具 - 递归思维加速器
目标：通过"状态-转移"语言训练，突破主谓宾结构的认知局限
"""
import streamlit as st
import graphviz


def render_recursion_training():
    """渲染递归思维训练页面"""

    st.title("∞ 递归思维加速器")
    st.caption("目标：用状态-转移语言突破主谓宾结构的认知局限")
    st.markdown("---")

    module = st.selectbox(
        "学习模块",
        options=[
            "📚 为什么主谓宾不擅长递归",
            "🔤 状态转移语言入门",
            "🧠 递归理解专项训练",
            "💻 通往编程思维的桥梁"
        ]
    )

    st.markdown("---")

    if module == "📚 为什么主谓宾不擅长递归":
        render_why_svo_sucks()
    elif module == "🔤 状态转移语言入门":
        render_state_transition_language()
    elif module == "🧠 递归理解专项训练":
        render_recursion_drills()
    elif module == "💻 通往编程思维的桥梁":
        render_programming_bridge()


def render_why_svo_sucks():
    """解释为什么主谓宾结构不擅长递归"""

    st.info("""
    💡 **核心洞见**

    中文（和所有自然语言）都是**主谓宾结构**：
    - 主语 做 宾语
    - 小明 吃 苹果
    - 函数 处理 数据

    这种结构擅长描述"谁对谁做了什么"，但天生不擅长描述"状态如何变化"。

    而递归、循环、状态机——这些恰恰是编程和数学的核心思维模式。
    """)

    st.markdown("### ❌ 用主谓宾描述递归的痛苦")

    st.code("""
    # 尝试用中文描述斐波那契：

    "斐波那契数列的第一个数是0，第二个数是1，
    然后后面的每一个数是前面两个数相加的结果。"

    你看懂了吗？也许吧。但你在脑子里要：
    1. 先理解"第一个"、"第二个"是什么意思
    2. 然后理解"后面"指的是什么
    3. 然后理解"前面两个"指的是哪两个
    4. 最后才能在脑子里推演

    主谓宾让简单的递归变得像绕口令！
    """, language="text")

    st.markdown("### ✅ 用状态转移描述递归的优雅")

    st.code("""
    # 状态转移语言描述斐波那契：

    状态 A: a=0, b=1
         ↓
         a, b = b, a+b
         ↓
         回到 A

    就这么简单！没有"第一个"、"第二个"、"后面"、"前面"
    只有状态和转移。
    """, language="text")

    st.divider()

    st.markdown("### 🎯 认知神经科学解释")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("#### 🧠 主谓宾激活的脑区")
            st.markdown("""
            - **布洛卡区**（语言产生）
            - **韦尼克区**（语言理解）
            - **颞叶**（语义记忆）

            这些脑区是为**社交和故事理解**进化的，
            不是为抽象逻辑推理进化的。
            """)

    with col2:
        with st.container(border=True):
            st.markdown("#### 🧠 状态转移激活的脑区")
            st.markdown("""
            - **前额叶**（工作记忆）
            - **顶叶**（空间推理）
            - **前扣带回**（认知控制）

            这些脑区是为**处理空间关系和状态变化**进化的，
            天生擅长理解递归！
            """)

    st.success("""
    🎉 **结论**

    不是你"没有编程天赋"，是你一直在用"讲故事的脑区"学编程。

    只要切换到"状态转移"的思维模式，你就能激活正确的脑区，
    递归就会变得像走路一样自然！
    """)


def render_state_transition_language():
    """状态转移语言入门"""

    st.info("""
    💡 **状态转移语言**是我们专门为递归思维设计的人工语言。

    它没有主语、没有谓语、没有宾语。
    它只有两个东西：`状态(State)` 和 `转移(Transition)`
    """)

    st.markdown("### 🔤 基本语法")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 语法规则")
        st.code("""
        # 定义一个状态
        状态名:
            变量名 = 值
            变量名 = 值

        # 定义转移
            → 下一个状态

        # 条件转移
            如果 条件 → 状态A
            否则 → 状态B

        # 完整例子：计数器
        开始:
            n = 0
            → 循环

        循环:
            如果 n < 10 → 继续
            否则 → 结束

        继续:
            n = n + 1
            → 循环

        结束:
            (停止)
        """)

    with col2:
        st.markdown("#### 可视化")
        # 画状态转移图
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR')
        dot.node('开始', shape='circle')
        dot.node('循环', shape='circle')
        dot.node('继续', shape='circle')
        dot.node('结束', shape='doublecircle')

        dot.edge('开始', '循环', label='n=0')
        dot.edge('循环', '继续', label='n<10')
        dot.edge('继续', '循环', label='n=n+1')
        dot.edge('循环', '结束', label='n≥10')

        st.graphviz_chart(dot)

    st.divider()

    st.markdown("### ✏️ 练习：把主谓宾翻译成状态转移")

    exercise = st.selectbox(
        "选择练习",
        options=[
            "倒计时",
            "累加求和",
            "斐波那契数列"
        ]
    )

    if exercise == "倒计时":
        st.markdown("""
        #### 练习1：倒计时

        **主谓宾描述**：
        > 我们从10开始数，每次减1，数到0的时候停止。

        **你的任务**：把它翻译成状态转移语言
        """)

        with st.expander("查看参考答案"):
            st.code("""
            开始:
                count = 10
                → 数数

            数数:
                如果 count > 0 → 减1
                否则 → 结束

            减1:
                count = count - 1
                → 数数

            结束:
                (停止)
            """)
            st.success("""
            发现了吗？一旦翻译成状态转移语言，
            这个逻辑就变得**无法被误解**！

            没有"我们"、"开始数"、"每次减"这些模糊的词，
            只有精确的状态和转移。
            """)

    elif exercise == "累加求和":
        st.markdown("""
        #### 练习2：累加求和（1加到100）

        **主谓宾描述**：
        > 我们有一个总和，一开始是0。然后我们从1加到100，每次把数加到总和里。

        **你的任务**：把它翻译成状态转移语言
        """)

        with st.expander("查看参考答案"):
            st.code("""
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
                sum 就是答案
            """)

    elif exercise == "斐波那契数列":
        st.markdown("""
        #### 练习3：斐波那契数列

        **主谓宾描述**：
        > 第一个数是0，第二个数是1，后面的每个数是前面两个数相加。

        **你的任务**：把它翻译成状态转移语言
        """)

        with st.expander("查看参考答案"):
            st.code("""
            开始:
                a = 0
                b = 1
                → 生成

            生成:
                输出 a
                → 转移

            转移:
                a, b = b, a+b
                → 生成

            # 永动机！（加终止条件自己想）
            """)


def render_recursion_drills():
    """递归理解专项训练"""

    st.info("""
    💡 **训练原理**

    递归不是"难"，是你的大脑**不习惯**用这种方式思考。

    通过刻意练习，让"状态转移思维"变成你的第二本能。
    """)

    st.markdown("### 🎯 训练1：识别递归模式")

    patterns = {
        "阶乘": "n! = n × (n-1)!",
        "汉诺塔": "把n个盘子从A移到C = 把n-1个从A移到B + 把第n个从A移到C + 把n-1个从B移到C",
        "树遍历": "访问节点 = 访问左子树 + 访问节点本身 + 访问右子树"
    }

    selected = st.selectbox("选择递归模式", list(patterns.keys()))

    st.markdown(f"**{selected}**：`{patterns[selected]}`")

    st.markdown("### 🧩 训练2：递归可视化")

    # 递归深度可视化
    depth = st.slider("递归深度", 1, 8, 3)

    def draw_recursion(d, indent=0):
        if d == 0:
            return "  " * indent + "🔵 基准情况\n"
        result = "  " * indent + f"📦 f({d}) 调用 f({d-1})\n"
        result += draw_recursion(d-1, indent+1)
        result += "  " * indent + f"📦 f({d}) 返回\n"
        return result

    st.text(draw_recursion(depth))

    st.markdown("### 🎮 训练3：递归迷宫")

    st.warning("""
    🎯 任务：找到走出迷宫的递归策略

    ```
    S → ? → ? → ? → ? → E
                ↓
          ? ← ? ← ?
          ↓
          ? → ? → ?
    ```

    **提示**：递归解迷宫只有4条规则：
    1. 如果当前是出口 → 成功！
    2. 如果当前是墙或已访问 → 失败
    3. 标记当前位置为已访问
    4. 递归尝试四个方向，任意一个成功就成功
    """)

    with st.expander("查看策略（先自己想）"):
        st.code("""
        定义 走迷宫(当前位置):

            如果 当前位置 是 出口 → 返回 成功

            如果 当前位置 是 墙 或 已访问 → 返回 失败

            标记 当前位置 为 已访问

            如果 走迷宫(上) 成功 → 返回 成功
            如果 走迷宫(下) 成功 → 返回 成功
            如果 走迷宫(左) 成功 → 返回 成功
            如果 走迷宫(右) 成功 → 返回 成功

            返回 失败

        就这么简单！没有复杂的循环，只有4条规则。
        这就是递归的威力。
        """)


def render_programming_bridge():
    """通往编程思维的桥梁"""

    st.info("""
    💡 **桥梁原理**

    状态转移语言 ↔ 伪代码 ↔ 真实代码

    一旦你掌握了状态转移思维，编程就只是语法翻译。
    """)

    st.markdown("### 🌉 三重翻译练习")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🔤 状态转移语言")
        st.code("""
        开始:
            a = 0
            b = 1
            n = 10
            → 循环

        循环:
            如果 n > 0 → 继续
            否则 → 结束

        继续:
            输出 a
            a, b = b, a+b
            n = n - 1
            → 循环

        结束:
            (停止)
        """, language="text")

    with col2:
        st.markdown("#### 📝 伪代码")
        st.code("""
        a = 0
        b = 1
        n = 10

        while n > 0:
            print(a)
            a, b = b, a + b
            n = n - 1
        """, language="python")

    with col3:
        st.markdown("#### 💻 Python 代码")
        st.code("""
        def fibonacci(n):
            a, b = 0, 1
            for _ in range(n):
                print(a)
                a, b = b, a + b

        fibonacci(10)
        """, language="python")

    st.success("""
    🎉 发现了吗？三者的结构完全一样！

    区别只是语法符号不同，核心的**状态转移逻辑**完全一致。

    当你写代码时，先在脑子里用状态转移语言想清楚，
    然后翻译成任何编程语言都是机械工作。
    """)

    st.divider()

    st.markdown("### 🎓 毕业测试")

    st.markdown("""
    如果你能用状态转移语言想清楚以下问题，
    你就掌握了程序员的核心思维方式：

    ✅ 如何反转一个链表？
    ✅ 如何用二分法查找一个数？
    ✅ 如何对一个数组进行快速排序？
    ✅ 如何深度优先遍历一棵树？

    这些问题的答案，用状态转移语言描述都不超过5行。
    """)


if __name__ == "__main__":
    pass
