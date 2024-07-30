import streamlit as st
import fitz  # PyMuPDF

# Function to extract text and metadata from PDF
def extract_pdf_info(pdf_file):
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    metadata = document.metadata
    text = ""
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    return metadata, text

# Streamlit app setup
st.set_page_config(page_title="PDF Uploader and Viewer", layout="wide")
st.title("PDF Uploader and Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.write("## PDF Preview")
    # Display PDF using an iframe
    base64_pdf = uploaded_file.getvalue().hex()
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    # Extract text and metadata
    metadata, text = extract_pdf_info(uploaded_file)
    
    st.write("## PDF Metadata")
    st.json(metadata)
    
    st.write("## Extracted Text")
    st.write(text)
