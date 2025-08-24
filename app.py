# app.py
import streamlit as st
from summarizer import generate_summary

# App title
st.set_page_config(page_title="Text Summarizer", layout="centered")
st.title("📝 AI Text Summarizer")
st.write("Paste any long text below and get a short summary using Transformers (BART).")

# Text input
input_text = st.text_area("Enter your text here:", height=250)

# Parameters
min_len = st.slider("Minimum summary length", 20, 200, 30)
max_len = st.slider("Maximum summary length", 50, 500, 120)

# Summarize button
if st.button("Summarize"):
    if input_text.strip():
        with st.spinner("Generating summary..."):
            summary = generate_summary(input_text, min_length=min_len, max_length=max_len)
            st.subheader("📌 Summary:")
            st.success(summary)
    else:
        st.warning("⚠️ Please enter some text to summarize.")
