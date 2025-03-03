import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Grammar Growth Challenge", page_icon="📚")

# Title and Introduction
st.title("📖 Grammar Growth Challenge")
st.header("Develop Your English Grammar Skills with a Growth Mindset!")
st.write("A growth mindset helps us improve through continuous learning. Let's embrace challenges and refine our grammar skills together!")

# Daily Grammar Tip
st.subheader("🌟 Daily Grammar Tip")
grammar_tips = [
    "Use 'their' for possession, 'there' for location, and 'they're' for 'they are'.",
    "Always capitalize the first letter of a sentence and proper nouns.",
    "Use 'its' for possession and 'it's' for 'it is'.",
    "A sentence must have a subject, a verb, and a complete thought.",
    "Use commas to separate items in a list: 'I bought apples, oranges, and bananas.'",
]
daily_tip = random.choice(grammar_tips)
st.write(f"**{daily_tip}**")

# Interactive Grammar Quiz
st.subheader("✍️ Grammar Quiz")
quiz_questions = {
    "Which sentence is grammatically correct?": [
        "I am going too the store.",
        "She don’t like ice cream.",
        "They're going to the park.",
    ],
    "Which word correctly completes the sentence: 'She ___ a beautiful song yesterday.'": [
        "singed",
        "sang",
        "sung",
    ],
    "Choose the correct word: 'I am taller ___ my brother.'": [
        "then",
        "than",
        "them",
    ],
}

selected_question = random.choice(list(quiz_questions.keys()))
options = quiz_questions[selected_question]

st.write(f"**{selected_question}**")
user_answer = st.radio("Choose the correct answer:", options)

correct_answers = {
    "Which sentence is grammatically correct?": "They're going to the park.",
    "Which word correctly completes the sentence: 'She ___ a beautiful song yesterday.'": "sang",
    "Choose the correct word: 'I am taller ___ my brother.'": "than",
}

if user_answer:
    if user_answer == correct_answers[selected_question]:
        st.success("✅ Correct! Keep up the great work!")
    else:
        st.error(f"❌ Oops! The correct answer is: **{correct_answers[selected_question]}**. Keep learning!")

# Reflection Section
st.subheader("📝 Reflection")
reflection = st.text_area("Write about what you learned today:")

if reflection:
    st.success("Great! Reflecting on learning helps reinforce knowledge.")

# Celebrate Achievements
st.subheader("🏆 Celebrate Your Progress!")
achievement = st.text_input("Share a recent grammar improvement or milestone:")

if achievement:
    st.success(f"🎉 Awesome! You're improving: {achievement}")

# Footer
st.write("---")
st.write("Keep challenging yourself, learning from mistakes, and growing with every step! 🚀")
st.write("**Created by Sadia, GIAIC Student.**")
