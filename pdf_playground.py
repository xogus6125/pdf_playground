import streamlit as st
import fitz  # PyMuPDF
import pandas as pd
import base64
from pdf2image import convert_from_bytes
from PIL import Image
import io

# Function to extract metadata from PDF
def extract_pdf_metadata(pdf_file):
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    metadata = document.metadata
    return metadata

# Function to convert PDF to images
def pdf_to_images(pdf_file):
    images = convert_from_bytes(pdf_file.getvalue())
    return images

# Function to display PDF as images
def display_pdf_images(images):
    for img in images:
        st.image(img, use_column_width=True)

# Streamlit app setup
st.set_page_config(page_title="PDF Uploader and Viewer", layout="wide")
st.title("PDF Uploader and Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract metadata and reset file pointer
    uploaded_file.seek(0)  # Reset file pointer after reading
    metadata = extract_pdf_metadata(uploaded_file)
    uploaded_file.seek(0)  # Reset file pointer again for display
    
    st.write("## PDF Metadata")
    metadata_df = pd.DataFrame(list(metadata.items()), columns=["Key", "Value"])
    st.table(metadata_df)
    
    st.write("## PDF Preview")
    images = pdf_to_images(uploaded_file)
    display_pdf_images(images)
