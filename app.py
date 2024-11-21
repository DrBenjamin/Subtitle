import streamlit as st
import io

def srt_to_vtt(srt_file):
    buffer_vtt = io.StringIO()
    buffer_vtt.write("WEBVTT\n\n")
    for line in srt_file:
        if line.strip().isdigit():
            continue
        if "-->" in line:
            line = line.replace(",", ".")
        buffer_vtt.write(line)
    return buffer_vtt
            
st.title("Untertitel Konverter")
st.write("Dieses Tool konvertiert `srt` Untertitel Dateien in das `vtt` Format.")
uploaded_file = st.file_uploader("Datei hochladen", accept_multiple_files=False, type='srt')
if uploaded_file:
    try:
        buffer = srt_to_vtt(io.StringIO(uploaded_file.read().decode("utf-8")))
        st.success("Datei(en) erfolgreich konvertiert.")
        st.download_button(
            label="Download Untertitel",
            data=buffer.getvalue(),
            file_name="Untertitel.vtt",
            mime="text/vtt",
        )

    except Exception as e:
        st.error(f"Error: {e}")
