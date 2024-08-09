import streamlit as st
import pikepdf
from pikepdf import Encryption

# Streamlit app setup
st.title("PDF Password Protection with Encryption Options")

# File uploader
uploaded_file = st.file_uploader("Choose PDF file", type="pdf")

# Available encryption options
encryption_options = {
    "RC4-40": Encryption.RC4_40,
    "RC4-128": Encryption.RC4_128,
    "AES-128": Encryption.AES_128,
    "AES-256": Encryption.AES_256,
}

if uploaded_file is not None:
    # Text input for password
    password = st.text_input("Enter a password to protect your PDF", type="password")
    
    # Dropdown for encryption algorithm selection
    algorithm = st.selectbox("Select encryption algorithm", options=list(encryption_options.keys()))
    
    st.divider()

    st.write(f"You have selected **{uploaded_file.name}** for protection.")
    
    if st.button("**Protect PDF**"):

        if password:
            with st.spinner("Protecting PDF..."):
                # Load the PDF
                pdf = pikepdf.Pdf.open(uploaded_file)

                # Encrypt the PDF
                output_pdf = f"protected_{uploaded_file.name}"
                pdf.save(output_pdf, encryption=encryption_options[algorithm](user=password))

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
