#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
from streamlit import session_state
from streamlit.runtime.uploaded_file_manager import UploadedFile
from streamlit_pdf_viewer import pdf_viewer
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
#----------------------------------------
#import utils
import re
import base64
import requests
import contextlib
from io import BytesIO
from pathlib import Path
from random import random
from datetime import datetime
from typing import Callable, Dict, Literal, Optional, Tuple, Union
from io import BytesIO
#----------------------------------------
import fitz
from PIL import Image
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.errors import PdfReadError, PdfStreamError

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="PDF Playground",
                    layout="wide",
                    page_icon="📄",            
                    initial_sidebar_state="collapsed")
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

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

tab1, tab2, tab3, tab4, tab5  = st.tabs(["**Preview**","**Extract**","**Convert**","**Merge**","**Reduce**"])

#---------------------------------------------------------------------------------------------------------------------------------
### Content
#---------------------------------------------------------------------------------------------------------------------------------

with tab1:
    
    if uploaded_file is not None:
        metadata, text, document = extract_pdf_info(uploaded_file)
    
        st.write("## PDF Metadata")
        metadata_df = pd.DataFrame(list(metadata.items()), columns=["Key", "Value"])
        st.table(metadata_df)
