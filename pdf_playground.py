import streamlit as st
import fitz  # PyMuPDF
import pandas as pd
import base64

# Function to extract metadata from PDF
def extract_pdf_metadata(pdf_file):
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    metadata = document.metadata
    return metadata

# Function to display PDF using iframe
def display_pdf(pdf_file):
    base64_pdf = base64.b64encode(pdf_file.getvalue()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit app setup
st.set_page_config(page_title="PDF Uploader and Viewer", layout="wide")
st.title("PDF Uploader and Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract metadata and reset file pointer
    metadata = extract_pdf_metadata(uploaded_file)
    uploaded_file.seek(0)  # Reset file pointer after reading

    st.write("## PDF Metadata")
    metadata_df = pd.DataFrame(list(metadata.items()), columns=["Key", "Value"])
    st.table(metadata_df)
    
    st.write("## PDF Preview")
    display_pdf(uploaded_file)
