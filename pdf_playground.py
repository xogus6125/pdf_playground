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
from pdf2docx import Converter
from pypdf import PaperSize, PdfReader, PdfWriter, Transformation
from pypdf.errors import FileNotDecryptedError
from st_social_media_links import SocialMediaIcons
from streamlit import session_state
from streamlit_pdf_viewer import pdf_viewer
#----------------------------------------
import utils
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
