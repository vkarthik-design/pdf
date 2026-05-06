import streamlit as st
from PyPDF2 import PdfMerger

st.title("PDF Merger")

uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if st.button("Merge PDFs"):
    if uploaded_files:
        merger = PdfMerger()

        for file in uploaded_files:
            merger.append(file)

        output_path = "merged.pdf"
        merger.write(output_path)
        merger.close()

        with open(output_path, "rb") as f:
            st.download_button("Download Merged PDF", f, file_name="merged.pdf")
    else:
        st.warning("Upload at least 2 PDFs")
