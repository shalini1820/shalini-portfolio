# Shalini Pathak Portfolio

A polished Streamlit portfolio for Shalini Pathak, focused on SAP Commerce Cloud, Hybris backend engineering, B2B portal development, API delivery, automation, security and performance outcomes.

## What changed

- Rebuilt the app as a native Streamlit landing page instead of rendering the whole portfolio inside an iframe.
- Added a cleaner hero section, sticky navigation, impact metrics, proof section, case studies, skills, experience, education and contact sections.
- Added `requirements.txt` for Streamlit Cloud deployment.
- Added `.streamlit/config.toml` for consistent dark theme styling.
- Kept the resume PDF in `assets/Shalini_Resume.pdf` and wired it into the download buttons.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Cloud

1. Push this repository to GitHub.
2. Go to Streamlit Cloud.
3. Choose the repo.
4. Main file path: `streamlit_app.py`
5. Deploy.

## Files

```text
streamlit_app.py          # Main portfolio app
requirements.txt          # Streamlit dependency for deployment
.streamlit/config.toml    # App theme
assets/Shalini_Resume.pdf # Resume used by the download buttons
```

## Optional next improvement

Add a professional headshot to `assets/` and replace the initials avatar in the hero card with the image.
