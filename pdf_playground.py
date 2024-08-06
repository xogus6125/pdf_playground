import streamlit as st
from PyPDF2 import PdfMerger
import io

# Function to merge multiple PDFs
def merge_pdfs(pdf_files):
    merger = PdfMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merged_pdf = io.BytesIO()
    merger.write(merged_pdf)
    merger.close()
    merged_pdf.seek(0)

    return merged_pdf

# Streamlit app setup
st.set_page_config(page_title="PDF Merger", layout="centered")
st.title("Merge Multiple PDFs")

# File uploader
uploaded_files = st.file_uploader("Choose PDF files to merge", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.write(f"You have selected {len(uploaded_files)} PDF file(s) for merging.")
    
    if st.button("Merge PDFs"):
        with st.spinner("Merging PDFs..."):
            merged_pdf = merge_pdfs(uploaded_files)

        st.success("PDFs merged successfully!")
        
        # Create a download button for the merged PDF
        st.download_button(
            label="Download Merged PDF",
            data=merged_pdf,
            file_name="merged_pdf.pdf",
            mime="application/pdf"
        )
else:
    st.info("Please upload multiple PDF files to merge them into a single PDF.")
