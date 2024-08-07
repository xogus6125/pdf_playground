import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

def compress_pdf(input_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)
    
    output_pdf = io.BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)

    return output_pdf

st.set_page_config(page_title="PDF Compressor", layout="wide")
st.title("PDF Compressor")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file to compress", type="pdf")

if uploaded_file is not None:
    # Display original PDF size
    original_size = len(uploaded_file.getbuffer())
    st.write(f"Original PDF size: {original_size / 1024:.2f} KB")

    # Compress PDF
    with st.spinner("Compressing PDF..."):
        compressed_pdf = compress_pdf(uploaded_file)

    # Display compressed PDF size
    compressed_size = len(compressed_pdf.getbuffer())
    st.write(f"Compressed PDF size: {compressed_size / 1024:.2f} KB")

    # Download button for the compressed PDF
    st.download_button(
        label="Download Compressed PDF",
        data=compressed_pdf,
        file_name="compressed_pdf.pdf",
        mime="application/pdf"
    )
