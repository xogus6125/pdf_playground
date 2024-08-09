import streamlit as st
from PyPDF2 import PdfReader, PdfWriter

# Streamlit app setup
st.title("PDF Password Protection")

# File uploader
uploaded_file = st.file_uploader("Choose PDF file", type="pdf")

if uploaded_file is not None:
    # Text input for password
    password = st.text_input("Enter a password to protect your PDF", type="password")
    
    st.divider()

    st.write(f"You have selected **{uploaded_file.name}** for protection.")
    if st.button("**Protect PDF**"):

        if password:
            pdf_reader = PdfReader(uploaded_file)
            pdf_writer = PdfWriter()

            # Adding pages to the writer
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            with st.spinner("Protecting PDF..."):
                # Encrypt the PDF with the given password
                pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

                output_pdf = f"protected_{uploaded_file.name}"
                with open(output_pdf, "wb") as f:
                    pdf_writer.write(f)

            with open(output_pdf, "rb") as f:
                st.success("Your PDF has been protected and is ready for download.")
                st.download_button(
                    label="**Download Password Protected PDF**", 
                    data=f, 
                    file_name=output_pdf, 
                    mime="application/pdf"
                )
        else:
            st.warning("Please enter a password to protect your PDF.")
else:
    st.info("Please upload a PDF file to protect.")
