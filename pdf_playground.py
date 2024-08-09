#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#----------------------------------------
import os
import sys
import traceback
from io import BytesIO
from PIL import Image
#----------------------------------------
from io import BytesIO
#----------------------------------------
import fitz
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_bytes

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="PDF Playground | v0.1",
                    layout="wide",
                    page_icon="📘",            
                    initial_sidebar_state="collapsed")
#----------------------------------------
st.title(f""":rainbow[PDF Playground]""")
st.markdown(
    '''
    Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a> |
    for best view of the app, please **zoom-out** the browser to **75%**.
    ''',
    unsafe_allow_html=True)
st.info('**An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs**', icon="ℹ️")
#----------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------


@st.cache_data(ttl="2h") 
def extract_metadata(pdf_file):
    pdf_reader = PdfFileReader(pdf_file)
    metadata = pdf_reader.getDocumentInfo()
    return metadata

@st.cache_data(ttl="2h")
def pdf_to_images(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    return images
#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

tab1, tab2, tab3, tab4, tab5, tab6  = st.tabs(["**Preview**","**Extract**","**Merge**","**Compress**","**Protect**","**Unlock**"])

#---------------------------------------------------------------------------------------------------------------------------------
### Content
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Preview
#---------------------------------------------------------------------------------------------------------------------------------

with tab1:

    col1, col2 = st.columns((0.2,0.8))
    with col1:

        st.subheader("Input", divider='blue') 
        uploaded_file = st.file_uploader("**Choose PDF file**", type="pdf")

        if uploaded_file is not None:
            
            with col2:

                st.subheader("View", divider='blue') 
                with st.container(height=750,border=True):
                    images = pdf_to_images(uploaded_file)
                    for i, image in enumerate(uploaded_file.read()):
                        st.image(image, caption=f'Page {i + 1}', use_column_width=True)

                stats_expander = st.expander("**MetaData**", expanded=False)
                with stats_expander:

                    pdf_file = BytesIO(uploaded_file.read())
                    metadata = extract_metadata(pdf_file)
                    if metadata:
                        for key, value in metadata.items():
                            st.write(f"**{key}:** {value}")
                    else:
                        st.write("No metadata found in the PDF file.")
        
#---------------------------------------------------------------------------------------------------------------------------------
### Extract
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Merge
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Compress
#---------------------------------------------------------------------------------------------------------------------------------











#---------------------------------------------------------------------------------------------------------------------------------
