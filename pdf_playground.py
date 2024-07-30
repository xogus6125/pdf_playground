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
    return metadata, document

# Function to convert PDF page to image
def pdf_page_to_image(doc, page_num):
    page = doc.load_page(page_num)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img

# Function to display PDF using iframe
def display_pdf(pdf_file):
    base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit app setup
st.set_page_config(page_title="PDF Uploader and Viewer", layout="wide")
st.title("PDF Uploader and Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Display the PDF
    display_pdf(uploaded_file)

    # Extract metadata and text
    uploaded_file.seek(0)  # Reset file pointer after reading
    metadata, document = extract_pdf_info(uploaded_file)
    
    st.write("## PDF Metadata")
    metadata_df = pd.DataFrame(list(metadata.items()), columns=["Key", "Value"])
    st.table(metadata_df)
    
    st.write("## PDF Preview")
    page_numbers = list(range(len(document)))
    
    # Display all pages
    for page_num in page_numbers:
        st.write(f"### Page {page_num + 1}")
        img = pdf_page_to_image(document, page_num)
        st.image(img, caption=f"Page {page_num + 1}", use_column_width=True)
