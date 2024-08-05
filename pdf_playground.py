import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import fitz  # PyMuPDF
import pandas as pd

# Function to extract metadata from PDF
def extract_pdf_metadata(pdf_file_path):
    document = fitz.open(pdf_file_path)
    metadata = document.metadata
    return metadata

# Streamlit app setup
st.set_page_config(page_title="Multiple PDF Viewer and Metadata Extractor", layout="wide")
st.title("Multiple PDF Viewer and Metadata Extractor")

# File uploader for multiple files
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save the uploaded PDF to a temporary location
        temp_pdf_path = f"/tmp/{uploaded_file.name}"
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the PDF using streamlit-pdf-viewer
        st.subheader(f"Viewing PDF: {uploaded_file.name}")
        pdf_viewer(temp_pdf_path)

        # Extract and display metadata
        metadata = extract_pdf_metadata(temp_pdf_path)
        st.write("## PDF Metadata")
        metadata_df = pd.DataFrame(list(metadata.items()), columns=["Key", "Value"])
        st.table(metadata_df)

        st.write("---")  # Divider between different PDFs
