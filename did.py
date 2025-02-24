# streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="☃️")

st.title("Growth Mindset AI Project")
st.header("This is a project to help you develop a growth mindset.")
st.write("Embrace challenges, learn from criticism, and be inspired by the success of others.")
st.write("This project will help you develop a growth mindset by providing you with daily quotes, articles, and videos.")
st.write("Start your journey to a growth mindset today!")
st.write("Click the button below to get started.")

# Quote section
st.header("Daily Quotes")
st.write("Here is a quote to inspire you today:")
quote = "The only way to get better is to challenge yourself."
st.write(f"**{quote}**")

# Challenge section
st.header("What's your challenge today?")
st.write("Today's challenge is to learn something new.")
st.write("Choose a topic that interests you and spend 30 minutes learning about it.")
st.write("You can read an article, watch a video, or listen to a podcast.")
st.write("The important thing is to challenge yourself and expand your knowledge.")

user_input = st.text_input("What topic are you interested in learning about today?")

if user_input:
    st.success(f"You are learning about: {user_input}. Keep pushing yourself to learn more.")
else:
    st.warning("Please enter a topic to continue.")

# Reflection section
st.header("Reflection")
reflection = st.text_area("Write Your Reflection Here:")

if reflection:
    st.success(f"Thank you for sharing your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow. Share your thoughts here.")

# Achievements section
st.header("Celebrate Your Achievements")
achievement = st.text_input("Share something you recently accomplished:")

if achievement:
    st.success(f"Congratulations on your achievement: {achievement}")
else:
    st.info("Share your recent achievements to celebrate your progress.")

# Footer
st.write("---")
st.write("You are making great progress on your journey to a growth mindset.")
st.write("Thank you for using the Growth Mindset AI Project.")  
st.write("Keep challenging yourself, learning from your experiences, and celebrating your achievements.")
st.write("Remember, the only way to get better is to challenge yourself.")
st.write("**Created by Sadia, GIAIC Student.**")
