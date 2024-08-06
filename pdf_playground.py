import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

# Function to convert audio to text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_file)

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    return text

# Streamlit App
st.set_page_config(page_title="Audio to Text Converter", layout="wide")
st.title("Audio to Text Converter")

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_audio_file", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(uploaded_file, format='audio/wav')

    # Convert audio to text
    with st.spinner("Converting audio to text..."):
        try:
            extracted_text = audio_to_text("temp_audio_file")
            st.success("Conversion successful!")
            st.text_area("Extracted Text", extracted_text, height=300)
        except Exception as e:
            st.error(f"Error: {e}")
