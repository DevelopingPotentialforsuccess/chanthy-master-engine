import streamlit as st
import google.generativeai as genai
import random

# 1. Setup Rotating Keys
keys = st.secrets["GEMINI_API_KEYS"] # Use your list of 10 keys here
genai.configure(api_key=random.choice(keys))

st.sidebar.title("🛠️ Tool Selection")
tool = st.sidebar.radio("Choose a tool:", ["Book Creation", "IELTS Master", "DPSS Studio", "Khmer Program"])

st.title(f"🚀 {tool}")

if tool == "Book Creation":
    st.write("Generating your book structure...")
    # Paste your Book Creation Python logic here

elif tool == "IELTS Master":
    st.write("IELTS Exam Generator...")
    # Paste your IELTS Python logic here

elif tool == "DPSS Studio":
    st.write("Educational Content Studio...")
    # Paste your DPSS Studio Python logic here

elif tool == "Khmer Program":
    st.write("Khmer Language Specialist...")
    # Paste your Khmer Program Python logic here

# Standard prompt box for all
prompt = st.text_area("Enter Instructions:")
if st.button("Start AI Process"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    st.markdown(response.text)
