# streamlit_app.py
import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Text→Image demo", layout="centered")

st.title("Text → Image (SDXL)")

prompt = st.text_input("Enter prompt")

col1, col2 = st.columns([3,1])
with col2:
    generate = st.button("Generate")

if generate:
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            try:
                # Change URL if your FastAPI is hosted elsewhere
                url = "http://localhost:8000/predict"
                resp = requests.post(url, json={"prompt": prompt}, timeout=120)
                resp.raise_for_status()

                img = Image.open(io.BytesIO(resp.content))
                st.image(img, caption=prompt, use_column_width=True)

                # Download button (serves bytes directly)
                st.download_button(
                    label="Download PNG",
                    data=resp.content,
                    file_name="generated.png",
                    mime="image/png",
                )
            except requests.exceptions.RequestException as re:
                st.error(f"Request error: {re}")
            except Exception as e:
                st.error(f"Error: {e}")