#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#----------------------------------------
import os
import sys
import traceback
from io import BytesIO
#----------------------------------------
#import utils
import fitz
import re
import contextlib
from io import BytesIO
from pathlib import Path
from random import random
from datetime import datetime
from typing import Callable, Dict, Literal, Optional, Tuple, Union
#----------------------------------------
import requests
from PIL import Image
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.errors import PdfReadError, PdfStreamError
from streamlit import session_state
from streamlit.runtime.uploaded_file_manager import UploadedFile
from streamlit_pdf_viewer import pdf_viewer
#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
VERSION = "0.1.0"
#import custom_style()
st.set_page_config(
    page_title="PDF Playground",
    layout="wide",
    page_icon="📄",
    menu_items={
            "About": f"PDF Playground v{VERSION}  "
            f"\nDeveloper contact: [Avijit Chakraborty](mailto:avijit.mba18@gmail.com)",
            "Get help": None,},            
    initial_sidebar_state="auto")
#----------------------------------------
st.title(f""":rainbow[PDF Playground | v0.1]""")
st.markdown(
    '''
    Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a>' |
    for best view of the app, please **zoom-out** the browser to **75%**.
    ''',
    unsafe_allow_html=True)
st.info('**An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs**', icon="ℹ️")
#----------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

@st.cache_data(ttl="2h")
def extract_pdf_info(pdf_file):
    document = fitz.open(stream=pdf_file, filetype="pdf")
    metadata = document.metadata
    text = [document.load_page(page_num).get_text() for page_num in range(len(document))]
    return metadata, text, document

@st.cache_data(ttl="2h")
def pdf_page_to_image(doc, page_num):
    page = doc.load_page(page_num)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img
#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

data_source = st.radio('Select the main source', ["File Upload", "Load from a URL"],horizontal=True, label_visibility='collapsed', key='options_dt')

if data_source == "File Upload":

    uploaded_file = st.file_uploader("**:blue[Choose a PDF file]**",type="pdf",accept_multiple_files=True)
    st.divider()

#---------------------------------------------------------------------------------------------------------------------------------
### Content
#---------------------------------------------------------------------------------------------------------------------------------

    tab1, tab2, tab3  = st.tabs(["**Preview**","**Extract**","**Convert**"])

#---------------------------------------------------------------------------------------------------------------------------------
### Preview
#---------------------------------------------------------------------------------------------------------------------------------

    with tab1:

        if uploaded_file is not None:
            metadata, text, document = extract_pdf_info(uploaded_file)

            col1, col2 = st.columns((0.7,0.3))
            with col1:

                st.subheader("View",divider='blue')
                page_numbers = list(range(len(document)))
                page_num = st.selectbox("Select Page Number", page_numbers)
                with st.container(height=750,border=True):

                    img = pdf_page_to_image(document, page_num)
                    st.image(img, caption=f"Page {page_num + 1}", use_column_width=True)
                    
                    with col2:

                        st.subheader("View",divider='blue')
                        with st.container(height=750,border=True):
                
                            metadata_df = pd.DataFrame(list(metadata.items()), columns=["Key", "Value"])
                            st.table(metadata_df)
