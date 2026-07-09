import streamlit as st
from summarizer import summarize_text
from file_utils import clean_file_name, create_txt, create_pdf

st.set_page_config(page_title="AI Summarization Tool", page_icon="📝")

st.title("AI Summarization Tool")

text = st.text_area(
    "Enter the text to be summarized and mention if you want PDF or text file:",
    height=250
)

file_name = st.text_input("Enter the file name:")

if st.button("Generate Summary"):
    if not text.strip():
        st.error("Please enter text to summarize.")
    else:
        file_name = clean_file_name(file_name)
        summary = summarize_text(text)

        st.subheader("Summary")
        st.write(summary)

        text_lower = text.lower()

        if "pdf" in text_lower or "bdf" in text_lower:
            create_pdf(summary, file_name)
            st.success(f"PDF file created: {file_name}.pdf")
        else:
            create_txt(summary, file_name)
            st.success(f"Text file created: {file_name}.txt")