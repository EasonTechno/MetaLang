"""
人类训练工具 - 外语直接思考训练
目标：训练大脑跳过中文翻译，建立英文概念的直接联结
"""
import streamlit as st
import random
import time


def render_foreign_language():
    """渲染外语直接思考训练页面"""

    st.title("🔤 外语直接思考训练")
    st.caption("目标：训练你的大脑跳过母语翻译，直接用英语思考")
    st.markdown("---")

    # 训练模式选择
    mode = st.selectbox(
        "训练模式",
        options=[
            "🌱 概念联结入门",
            "📖 无翻译阅读",
            "✍ 英语作文训练",
            "🎯 考试模拟"
        ],
        key="training_mode"
    )

    st.markdown("---")

    if mode == "🌱 概念联结入门":
        render_concept_connection()
    elif mode == "📖 无翻译阅读":
        render_no_translation_reading()
    elif mode == "✍ 英语作文训练":
        render_english_writing()
    elif mode == "🎯 考试模拟":
        render_exam_simulation()


def render_concept_connection():
    """概念联结入门训练"""

    st.info("""
    💡 **训练原理**

    大多数人学英语时建立的是：
    `英文单词 → 中文翻译 → 概念理解`

    我们要建立的是：
    `英文单词 → 概念理解`

    这个练习训练你看到英文词时，直接联想相关的英文词，跳过中文翻译。
    """)

    st.markdown("### 🎮 联想游戏")

    # 单词库（按语义场分类）
    semantic_fields = {
        "时间": ["time", "clock", "hour", "minute", "second", "morning", "afternoon", "evening", "night", "day", "week", "month", "year", "past", "present", "future", "early", "late"],
        "空间": ["space", "place", "area", "position", "location", "up", "down", "left", "right", "front", "back", "inside", "outside", "near", "far", "big", "small"],
        "情感": ["happy", "sad", "angry", "afraid", "love", "hate", "joy", "sorrow", "fear", "hope", "desire", "excited", "calm", "nervous", "relaxed"],
        "思考": ["think", "know", "believe", "understand", "remember", "forget", "learn", "realize", "imagine", "reason", "logic", "idea", "concept", "theory"]
    }

    if 'concept_practice_started' not in st.session_state:
        st.session_state.concept_practice_started = False
        st.session_state.current_word = ""
        st.session_state.current_field = ""
        st.session_state.user_associations = []
        st.session_state.score = 0
        st.session_state.rounds = 0

    if not st.session_state.concept_practice_started:
        if st.button("🚀 开始练习", type="primary"):
            field = random.choice(list(semantic_fields.keys()))
            word = random.choice(semantic_fields[field])
            st.session_state.current_word = word
            st.session_state.current_field = field
            st.session_state.user_associations = []
            st.session_state.concept_practice_started = True
            st.rerun()

    else:
        col1, col2 = st.columns([1, 1])

        with col1:
            st.success(f"### 中心词：**{st.session_state.current_word.upper()}**")
            st.caption(f"语义场：{st.session_state.current_field}")
            st.markdown("""
            🎯 任务：输入与这个词相关的 **英文单词**

            ❌ **禁止用中文思考**
            """)

            user_input = st.text_input("输入英文单词（按回车确认）", "", key="concept_input")

            if user_input and st.session_state.concept_practice_started:
                user_word = user_input.lower().strip()
                if user_word and user_word not in st.session_state.user_associations:
                    st.session_state.user_associations.append(user_word)
                    # 检查是否在语义场中
                    if user_word in semantic_fields[st.session_state.current_field]:
                        st.session_state.score += 1
                        st.balloons()
                    else:
                        st.session_state.score += 0.5  # 相关但不在预定义列表中

        with col2:
            st.markdown("### 📝 你的联想")
            for i, word in enumerate(st.session_state.user_associations):
                is_correct = word in semantic_fields[st.session_state.current_field]
                if is_correct:
                    st.markdown(f"{i+1}. ✅ **{word}**")
                else:
                    st.markdown(f"{i+1}. ⚠️ {word}")

            st.metric("得分", st.session_state.score)

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔄 换一个词"):
                field = random.choice(list(semantic_fields.keys()))
                word = random.choice(semantic_fields[field])
                st.session_state.current_word = word
                st.session_state.current_field = field
                st.session_state.user_associations = []
                st.rerun()
        with col2:
            if st.button("⏹ 结束练习"):
                st.session_state.concept_practice_started = False
                st.rerun()


def render_no_translation_reading():
    """无翻译阅读训练"""

    st.info("""
    💡 **训练原理**

    普通阅读：`英文句子 → 翻译中文 → 理解意思`

    目标模式：`英文句子 → 直接理解意思`

    这个练习提供纯英文阅读材料，隐藏所有中文。你需要回答问题来证明你理解了内容。
    """)

    # 英文阅读材料（分级）
    reading_passages = {
        "初级": {
            "title": "The City Park",
            "content": """
            The city park is a beautiful place. Many people go there every day.
            Some people walk their dogs. Others play sports or read books.
            There are many trees and flowers in the park.
            Children like to play on the playground.
            Old people like to sit on benches and talk to each other.
            The park is open from early morning until late at night.
            It is free for everyone to enjoy.
            """,
            "questions": [
                {
                    "question": "When is the park open?",
                    "options": ["Only in the morning", "From morning until night", "Only on weekends", "It is always closed"],
                    "correct": 1
                },
                {
                    "question": "What do old people like to do in the park?",
                    "options": ["Play sports", "Walk dogs", "Sit and talk", "Play on the playground"],
                    "correct": 2
                }
            ]
        },
        "中级": {
            "title": "The Power of Habits",
            "content": """
            Habits shape our lives more than we realize. Researchers say that about 40 percent
            of the actions people perform each day are not actual decisions, but habits.
            This is not necessarily a bad thing. Habits allow our brains to conserve energy
            for more demanding tasks. However, bad habits can hold us back from reaching our goals.
            The good news is that habits can be changed. To change a habit, you need to understand
            its structure: cue, routine, and reward. By identifying these components, you can
            replace bad routines with better ones while keeping the same cues and rewards.
            """,
            "questions": [
                {
                    "question": "What percentage of our daily actions are habits?",
                    "options": ["10%", "25%", "40%", "75%"],
                    "correct": 2
                },
                {
                    "question": "What are the three parts of a habit?",
                    "options": ["Start, middle, end", "Cue, routine, reward", "Think, act, feel", "Morning, afternoon, night"],
                    "correct": 1
                }
            ]
        }
    }

    level = st.select_slider("难度选择", options=["初级", "中级"], value="初级")

    passage = reading_passages[level]

    with st.container(border=True):
        st.subheader(f"📖 {passage['title']}")
        st.caption(f"难度：{level} | 纯英文阅读，不要翻译")
        st.markdown(passage['content'])

    st.markdown("### ✅ 理解测试（用英语思考，选择答案）")

    for i, q in enumerate(passage['questions']):
        st.markdown(f"**问题 {i+1}:** {q['question']}")
        selected = st.radio(f"q{i}", q['options'], label_visibility="collapsed")
        if st.button(f"检查答案 {i+1}", key=f"check_{i}"):
            if selected == q['options'][q['correct']]:
                st.success("✅ 正确！你直接理解了！")
            else:
                st.error("❌ 再读一遍，用英语理解")


def render_english_writing():
    """英语作文训练"""

    st.info("""
    💡 **训练原理**

    普通写作：`中文思路 → 翻译英文`

    目标模式：`直接用英文构思和写作`

    这个练习要求你全程用英文思考并写作，禁止出现任何中文。
    """)

    topics = [
        "Describe your favorite place and explain why you like it.",
        "What is the most important thing you have learned in the last year?",
        "If you could have any superpower, what would it be and why?",
        "Describe a time you overcame a difficulty.",
        "What does success mean to you?"
    ]

    topic = random.choice(topics)

    st.markdown("### 📝 作文题目")
    with st.container(border=True):
        st.markdown(f"**{topic}**")

    st.warning("""
    ⚠️ **规则**
    1. 全程用英文思考
    2. 作文中不能出现任何中文
    3. 不要在心里翻译，直接用英文组织思路
    """)

    essay = st.text_area("开始写作（英文）", height=200, placeholder="Write your essay here...")

    if essay:
        if any('\u4e00' <= c <= '\u9fff' for c in essay):
            st.error("❌ 检测到中文字符！请全程用英文思考")
        else:
            st.success("✅ 很好！你做到了直接用英文表达")
            word_count = len(essay.split())
            st.metric("词数", word_count)


def render_exam_simulation():
    """考试模拟"""

    st.info("""
    💡 **训练原理**

    真实考试时，没有时间逐句翻译。你需要训练大脑在考试环境下直接用英文处理信息。

    这个模块模拟真实考试的计时压力，训练你"用英语做题"而不是"用翻译做题"。
    """)

    st.markdown("### 🎯 阅读理解（考试模式）")

    # 模拟高考英语阅读题
    exam_passage = """
    In the 1960s, while studying the volcanic history of Yellowstone National Park,
    Bob Christiansen became puzzled about something that, oddly, had not troubled anyone before:
    he couldn't find the park's volcano. It had been known for a long time that Yellowstone
    was volcanic in nature - that's what accounted for all its hot springs and other steamy features.
    But Christiansen couldn't find the Yellowstone volcano anywhere.

    Most of us, when we talk about volcanoes, think of the classic cone shapes of a Fuji or Kilimanjaro,
    which are created when erupting magma piles up. These can form remarkably quickly. In 1943,
    a Mexican farmer was surprised to see smoke rising from a small part of his land. In one week
    he was the confused owner of a cone five hundred feet high. At the end of two years it had topped
    out at almost fourteen hundred feet. Altogether there are some ten thousand of these volcanoes on Earth,
    all but a few hundred of them extinct.

    There is, however, a second less known type of volcano that doesn't involve mountain building.
    These are volcanoes so explosive that they burst open in a single big crack, leaving behind a vast hole,
    the caldera. Yellowstone obviously was of this second type, but Christiansen couldn't find the caldera itself.
    """

    questions = [
        {
            "question": "What puzzled Christiansen when he was studying Yellowstone?",
            "options": [
                "Its complicated geographical features",
                "Its ever-lasting influence on tourism",
                "The mysterious history of the park",
                "The exact location of the volcano"
            ],
            "correct": 3
        },
        {
            "question": "What does the second paragraph mainly talk about?",
            "options": [
                "The shapes of volcanoes",
                "The impacts of volcanoes",
                "The activities of volcanoes",
                "The heights of volcanoes"
            ],
            "correct": 0
        }
    ]

    if 'exam_started' not in st.session_state:
        st.session_state.exam_started = False
        st.session_state.start_time = 0

    if not st.session_state.exam_started:
        st.info("""
        📋 考试规则
        - 限时 10 分钟完成 2 道阅读题
        - 请直接用英文理解，不要翻译
        - 开始后倒计时自动启动
        """)
        if st.button("🚀 开始考试", type="primary"):
            st.session_state.exam_started = True
            st.session_state.start_time = time.time()
            st.rerun()
    else:
        elapsed = int(time.time() - st.session_state.start_time)
        remaining = max(0, 600 - elapsed)
        minutes, seconds = divmod(remaining, 60)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.metric("⏱ 剩余时间", f"{minutes}:{seconds:02d}")

        with st.container(border=True):
            st.markdown(exam_passage)

        st.markdown("### 问题")

        answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['question']}**")
            ans = st.radio(f"q{i}_exam", q['options'], label_visibility="collapsed")
            answers.append(ans)

        if st.button("提交答案"):
            correct = 0
            for i, q in enumerate(questions):
                if answers[i] == q['options'][q['correct']]:
                    correct += 1
                    st.success(f"✅ Q{i+1} 正确")
                else:
                    st.error(f"❌ Q{i+1} 错误")
            st.markdown(f"### 得分：{correct}/{len(questions)}")
            st.session_state.exam_started = False


if __name__ == "__main__":
    pass
