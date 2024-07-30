import streamlit as st
import fitz  # PyMuPDF
import pandas as pd
from PIL import Image
from io import BytesIO
import base64

# Function to extract text and metadata from PDF
def extract_pdf_info(pdf_file):
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    metadata = document.metadata
    text = [document.load_page(page_num).get_text() for page_num in range(len(document))]
    return metadata, text, document

# Function to convert PDF page to image
def pdf_page_to_image(doc, page_num):
    page = doc.load_page(page_num)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img

# Streamlit app setup
st.set_page_config(page_title="PDF Uploader and Viewer", layout="wide")
st.title("PDF Uploader and Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    metadata, text, document = extract_pdf_info(uploaded_file)
    
    st.write("## PDF Metadata")
    metadata_df = pd.DataFrame(list(metadata.items()), columns=["Key", "Value"])
    st.table(metadata_df)
    
    st.write("## PDF Preview")
    page_numbers = list(range(len(document)))
    page_num = st.selectbox("Select Page Number", page_numbers)
    
    # Display selected page image
    img = pdf_page_to_image(document, page_num)
    st.image(img, caption=f"Page {page_num + 1}", use_column_width=True)
    
    st.write("## Extracted Text")
    st.write(text[page_num])

# Optional: Display all pages in a single view
st.write("### View All Pages")
for page_num in page_numbers:
    st.write(f"### Page {page_num + 1}")
    img = pdf_page_to_image(document, page_num)
    st.image(img, caption=f"Page {page_num + 1}", use_column_width=True)
    st.write(text[page_num
