from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Space Bun", layout="wide")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 0.75rem;
        padding-bottom: 0.5rem;
        padding-left: 0.75rem;
        padding-right: 0.75rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Space Bun")
st.caption("Click inside the game area to focus controls. Move with WASD, aim with mouse, click to shoot.")

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

components.html(html, height=900, scrolling=False)
