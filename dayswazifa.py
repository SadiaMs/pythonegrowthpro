import streamlit as st
import time

# Wazifa dictionary
wazifa_messages = {
    "Monday": "Recite Surah Al-Fatiha 7 times for blessings in your week.",
    "Tuesday": "Recite 'Ya Hayyu Ya Qayyum' 100 times for strength and guidance.",
    "Wednesday": "Recite Surah Al-Waqia before sleeping for financial stability.",
    "Thursday": "Recite 'Astaghfirullah' 100 times for forgiveness and mercy.",
    "Friday": "Recite Durood Pak 100 times for blessings and peace.",
    "Saturday": "Recite Surah Al-Kahf for protection from trials.",
    "Sunday": "Recite 'La ilaha illallah' 100 times for peace and success."
}

# Streamlit UI
st.title("🕌 Days Wazifa Recommendation")

# Select a day
selected_day = st.selectbox("Choose a day:", list(wazifa_messages.keys()))

# Button to get wazifa
if st.button("Get Wazifa"):
    with st.spinner("✨ Fetching your Wazifa..."):
        time.sleep(2)  # Fake loading effect
    st.success(f"📖 **{wazifa_messages[selected_day]}**")
