import streamlit as st
import io
from srt_to_vtt import srt_to_vtt

st.title("Untertitel Konverter")
st.write("Dieses Tool konvertiert `srt` Untertitel Dateien in das `vtt` Format.")
uploaded_file = st.file_uploader("Datei hochladen", accept_multiple_files=False, type='srt')
if uploaded_file:
    try:
        buffer = io.StringIO()
        srt_to_vtt(uploaded_file, buffer)
        content = buffer.getvalue()
        st.success("Datei(en) erfolgreich konvertiert.")
        st.download_button(
            label="Download Untertitel",
            data=content,
            file_name="Untertitel.vtt",
            mime="text/vtt",
        )

    except Exception as e:
        st.error(f"Error: {e}")
