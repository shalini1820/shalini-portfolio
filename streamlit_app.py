"""
streamlit_app.py  ←  Main entry point for Streamlit Cloud.

What it does:
  1. Generates the resume PDF in memory (no disk writes needed).
  2. Injects the PDF as a base64 data-URI into index.html so the
     "Download Resume" button inside the portfolio works perfectly.
  3. Renders the full animated portfolio via components.html().
"""

import base64

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ── Page config ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Shalini | SAP Commerce Cloud Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide all Streamlit chrome so the portfolio fills the full screen ─────────

st.markdown(
    """
    <style>
        #MainMenu                        { display: none !important; }
        header                           { display: none !important; }
        footer                           { display: none !important; }
        .block-container                 { padding: 0 !important; max-width: 100% !important; }
        [data-testid="stSidebar"]        { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        iframe                           { border: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Generate PDF once and cache it for the session ───────────────────────────

@st.cache_data(show_spinner="Building your portfolio…")
def get_portfolio_html() -> str:
    from generate_resume import build_pdf_bytes

    # Build PDF in memory and encode as base64
    pdf_b64 = base64.b64encode(build_pdf_bytes()).decode()

    # Read the portfolio HTML
    html = Path("index.html").read_text(encoding="utf-8")

    # Patch the "Download Resume" button to use the base64 data URI
    # so it works inside Streamlit's iframe without any external file
    html = html.replace(
        'href="static/assets/Shalini_Resume_With_Portfolio.pdf"',
        f'href="data:application/pdf;base64,{pdf_b64}" download="Shalini_Resume.pdf"',
    )
    return html


# ── Render ───────────────────────────────────────────────────────────────────

components.html(get_portfolio_html(), height=5200, scrolling=True)
