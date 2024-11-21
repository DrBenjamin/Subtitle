import streamlit as st
from srt_to_vtt import srt_to_vtt

path_to_my_srt_file = "example.srt"
path_to_converted_vtt_file = "output.vtt"

# Title
st.title("Untertitel Konverter")
uploaded_files = st.file_uploader("Datei(en) hochladen", accept_multiple_files=True, type='srt')
if uploaded_files:
    try:
        # Converting example.srt into output.vtt
        srt_to_vtt(path_to_my_srt_file, path_to_converted_vtt_file)
        with open('output.vtt', 'r') as file:
            content = file.read()
        st.success("Datei(en) erfolgreich konvertiert.")
        st.download_button(
            label="Download Untertitel",
            data=content,
            file_name="Untertitel.vtt",
            mime="text/vtt",
        )

    except S3Error as e:
        st.error(f"Error: {e}")
