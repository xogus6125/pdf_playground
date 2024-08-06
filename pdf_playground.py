import streamlit as st
from docx import Document
from io import BytesIO
import docx2txt

# Function to merge multiple Word documents
def merge_word_docs(doc_files):
    merged_doc = Document()

    for doc_file in doc_files:
        temp_doc = Document(doc_file)
        
        # Copy each paragraph from the document to the merged document
        for paragraph in temp_doc.paragraphs:
            merged_doc.add_paragraph(paragraph.text)
        
        # Add a page break between documents
        merged_doc.add_page_break()

    merged_doc_stream = BytesIO()
    merged_doc.save(merged_doc_stream)
    merged_doc_stream.seek(0)

    return merged_doc_stream

# Function to extract text from a Word document
def extract_text_from_doc(doc_file):
    text = docx2txt.process(doc_file)
    return text

# Streamlit app setup
st.set_page_config(page_title="Word Document Merger", layout="wide")
st.title("Merge Multiple Word Documents")

# File uploader
uploaded_files = st.file_uploader("Choose Word files to merge", type="docx", accept_multiple_files=True)

if uploaded_files:
    st.write(f"You have selected {len(uploaded_files)} Word file(s) for merging.")
    
    if st.button("Merge Word Documents"):
        with st.spinner("Merging Word documents..."):
            merged_doc = merge_word_docs(uploaded_files)
        
        st.success("Word documents merged successfully!")

        # Create a download button for the merged Word document
        st.download_button(
            label="Download Merged Word Document",
            data=merged_doc,
            file_name="merged_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

        # Add a section to view the merged document
        st.write("---")
        st.subheader("View Merged Document")
        
        merged_text = extract_text_from_doc(merged_doc)
        st.text_area("Merged Document Content", merged_text, height=400)
else:
    st.info("Please upload multiple Word files to merge them into a single document.")
