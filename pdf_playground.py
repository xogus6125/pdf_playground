import streamlit as st

# Set up the sidebar
st.sidebar.header("Navigation")

# Add different sidebar elements
st.sidebar.subheader("Actions")
view_button = st.sidebar.button("View Documents")
extract_button = st.sidebar.button("Extract Text")
merge_button = st.sidebar.button("Merge PDFs")

st.sidebar.subheader("Settings")
scale_factor = st.sidebar.slider("Scale Factor", 0.1, 2.0, 1.0)
compression_level = st.sidebar.selectbox("Compression Level", ["Low", "Medium", "High"])

st.sidebar.subheader("Upload")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx"])

# Main app content
st.title("Main Page Content")
st.write("This is the main content of the app.")

# Display different content based on the sidebar actions
if view_button:
    st.write("View Documents action selected.")
elif extract_button:
    st.write("Extract Text action selected.")
elif merge_button:
    st.write("Merge PDFs action selected.")

# Display uploaded file information
if uploaded_file:
    st.write(f"Uploaded file: {uploaded_file.name}")
    # Further processing of the uploaded file can be added here

# Display selected settings
st.write(f"Selected Scale Factor: {scale_factor}")
st.write(f"Selected Compression Level: {compression_level}")
