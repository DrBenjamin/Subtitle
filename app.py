import streamlit as st
from srt_to_vtt import srt_to_vtt

path_to_my_srt_file = "example.srt"
path_to_converted_vtt_file = "output.vtt"

# Title
st.title("Untertitel Konverter")
uploaded_files = st.file_uploader("Datei(en) hochladen", accept_multiple_files=True, type='srt')
if uploaded_files:
    try:
        st.success("Datei(en) erfolgreich hochgeladen.")
    except S3Error as e:
        st.error(f"Error: {e}")
        
# Converting example.srt into output.vtt
vtt_file = srt_to_vtt(path_to_my_srt_file, path_to_converted_vtt_file)

st.download_button(vtt_file, "Download VTT-Datei", "Click here to download your file", "vtt")
