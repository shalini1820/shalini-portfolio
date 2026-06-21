"""
streamlit_app.py
Reads your resume PDF from assets/ and wires it into the
portfolio's "Download Resume" button via a base64 data-URI.
"""

import base64
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ── Page config ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Shalini | SAP Commerce Cloud Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide all Streamlit chrome ─────────────────────────────────────────────────

st.markdown("""
<style>
    #MainMenu                        { display: none !important; }
    header                           { display: none !important; }
    footer                           { display: none !important; }
    .block-container                 { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stSidebar"]        { display: none !important; }
    [data-testid="collapsedControl"] { display: none !important; }
    iframe                           { border: none !important; }
</style>
""", unsafe_allow_html=True)

# ── Load resume PDF from assets/ folder ──────────────────────────────────────

RESUME_PATH = Path("assets/Shalini_Resume.pdf")

@st.cache_data(show_spinner=False)
def get_portfolio_html() -> str:
    # Read and encode the resume PDF
    pdf_b64 = base64.b64encode(RESUME_PATH.read_bytes()).decode()

    # Read the portfolio HTML
    html = Path("index.html").read_text(encoding="utf-8")

    # Patch the Download Resume button with the actual PDF data
    html = html.replace(
        'href="static/assets/Shalini_Resume_With_Portfolio.pdf"',
        f'href="data:application/pdf;base64,{pdf_b64}" download="Shalini_Resume.pdf"',
    )
    return html

# ── Render portfolio ──────────────────────────────────────────────────────────

if not RESUME_PATH.exists():
    st.error("Resume PDF not found. Please add your PDF to the `assets/` folder as `Shalini_Resume.pdf`")
else:
    components.html(get_portfolio_html(), height=5200, scrolling=True)
