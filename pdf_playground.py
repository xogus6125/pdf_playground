import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# Streamlit app setup
st.set_page_config(page_title="PDF Viewer", layout="wide")
st.title("PDF Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded PDF to a temporary location
    temp_pdf_path = "/tmp/temp_uploaded_file.pdf"
    with open(temp_pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Display the PDF using streamlit-pdf-viewer
    pdf_viewer(temp_pdf_path)
