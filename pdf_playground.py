import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO

# Function to extract images from PDF
def extract_images_from_pdf(pdf_file):
    document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    images = []
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(BytesIO(image_bytes))
            images.append((page_num + 1, img_index + 1, image))
    
    return images

# Streamlit app setup
st.set_page_config(page_title="PDF Image Extractor", layout="wide")
st.title("PDF Image Extractor")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    images = extract_images_from_pdf(uploaded_file)
    
    if images:
        st.write(f"Found {len(images)} image(s) in the PDF.")
        
        for page_num, img_index, image in images:
            st.write(f"Page Number: {page_num}, Image Number: {img_index}")
            st.image(image, use_column_width=True)
    else:
        st.write("No images found in the PDF.")
