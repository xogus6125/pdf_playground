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

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
#import custom_style()
st.set_page_config(page_title="PDF Playground",
                   layout="wide",
                   #page_icon=               
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
