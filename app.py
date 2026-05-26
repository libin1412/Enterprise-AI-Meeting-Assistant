# Enterprise-AI-Meeting-Assistant/app.py

import streamlit as st

from src.meeting_engine import analyze_meeting


st.set_page_config(
    page_title="Enterprise AI Meeting Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Enterprise AI Meeting Assistant")

st.write(
    "AI-powered meeting summarization and action-item extraction system."
)

uploaded_file = st.file_uploader(
    "Upload meeting transcript (.txt)",
    type=["txt"]
)

meeting_transcript = ""

if uploaded_file is not None:

    meeting_transcript = uploaded_file.read().decode("utf-8")

    st.text_area(
        "Uploaded Transcript",
        meeting_transcript,
        height=300
    )

else:

    meeting_transcript = st.text_area(
        "Paste meeting transcript:",
        height=300
    )

if st.button("Analyze Meeting"):

    if meeting_transcript.strip() == "":

        st.warning("Please enter a meeting transcript.")

    else:

        with st.spinner("Analyzing meeting..."):

            result = analyze_meeting(meeting_transcript)

        st.subheader("Meeting Analysis")

        st.write(result)