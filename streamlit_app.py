from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
RESUME_PATH = BASE_DIR / "assets" / "Shalini_Resume.pdf"

st.set_page_config(
    page_title="Shalini Pathak | SAP Commerce Cloud Developer",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def pdf_download_link(path: Path) -> str:
    if not path.exists():
        return "#"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:application/pdf;base64,{encoded}"


resume_href = pdf_download_link(RESUME_PATH)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --ink: #050b18;
    --ink-2: #0b1220;
    --navy: #101827;
    --blue: #38bdf8;
    --cyan: #67e8f9;
    --indigo: #818cf8;
    --ice: #dbeafe;
    --text: #f8fafc;
    --soft: #cbd5e1;
    --muted: #94a3b8;
    --border: rgba(255,255,255,.11);
    --panel: rgba(255,255,255,.052);
    --panel-strong: rgba(255,255,255,.075);
    --max: 1180px;
}

html { scroll-behavior: smooth; }

.stApp {
    background:
        radial-gradient(circle at 4% 4%, rgba(56,189,248,.16), transparent 28rem),
        radial-gradient(circle at 92% 14%, rgba(129,140,248,.13), transparent 30rem),
        radial-gradient(circle at 48% 100%, rgba(103,232,249,.08), transparent 34rem),
        linear-gradient(135deg, #050b18 0%, #0b1220 52%, #050b18 100%);
    color: var(--text);
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

#MainMenu, header, footer, [data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none !important;
}

.block-container {
    max-width: 100% !important;
    padding: 0 !important;
}

[data-testid="stVerticalBlock"] { gap: 0 !important; }

.site-nav {
    position: sticky;
    top: 0;
    z-index: 999;
    border-bottom: 1px solid var(--border);
    background: rgba(5,11,24,.80);
    backdrop-filter: blur(20px);
}

.nav-inner {
    width: min(var(--max), calc(100vw - 40px));
    height: 76px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 22px;
}

.brand {
    color: white !important;
    text-decoration: none !important;
    font-size: .72rem;
    font-weight: 900;
    letter-spacing: .20em;
    text-transform: uppercase;
    white-space: nowrap;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 22px;
}

.nav-links a {
    color: var(--soft) !important;
    text-decoration: none !important;
    font-size: .86rem;
    font-weight: 650;
    transition: color .18s ease;
}

.nav-links a:hover {
    color: var(--cyan) !important;
}

.resume-pill {
    color: var(--soft) !important;
    text-decoration: none !important;
    padding: 10px 16px;
    border-radius: 999px;
    border: 1px solid var(--border);
    background: rgba(255,255,255,.04);
    font-size: .84rem;
    font-weight: 800;
}

.resume-pill:hover {
    color: var(--cyan) !important;
    border-color: rgba(103,232,249,.40);
}

.ticker {
    border-bottom: 1px solid rgba(255,255,255,.08);
    background: rgba(255,255,255,.018);
    overflow: hidden;
}

.ticker-inner {
    width: min(var(--max), calc(100vw - 40px));
    margin: 0 auto;
    overflow: hidden;
}

.ticker-track {
    width: max-content;
    min-width: 100%;
    display: flex;
    gap: 34px;
    padding: 11px 0;
    animation: tickerScroll 48s linear infinite;
}

.ticker-track span {
    color: var(--muted);
    font-size: .80rem;
    font-weight: 750;
    white-space: nowrap;
}

.ticker-track span::before {
    content: '';
    display: inline-block;
    width: 6px;
    height: 6px;
    margin-right: 10px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--blue), var(--cyan));
    box-shadow: 0 0 18px rgba(56,189,248,.42);
}

@keyframes tickerScroll {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}

.hero {
    width: min(var(--max), calc(100vw - 40px));
    margin: 0 auto;
    min-height: auto;
    display: grid;
    grid-template-columns: 1.02fr .98fr;
    align-items: center;
    gap: 52px;
    padding: 74px 0 54px;
}

.kicker {
    color: var(--cyan);
    font-size: .68rem;
    font-weight: 900;
    letter-spacing: .22em;
    text-transform: uppercase;
}

.hero h1 {
    margin: 24px 0 0;
    max-width: 760px;
    color: white;
    font-size: clamp(1.9rem, 3.45vw, 3.75rem);
    line-height: 1.12;
    letter-spacing: -.035em;
    font-weight: 900;
}

.text-gradient {
    background: linear-gradient(135deg, #ffffff 0%, var(--cyan) 46%, var(--indigo) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.hero-copy {
    margin: 24px 0 0;
    max-width: 720px;
    color: var(--soft);
    font-size: clamp(1rem, 1.2vw, 1.12rem);
    line-height: 1.76;
}

.hero-meta {
    margin-top: 20px;
    color: var(--muted);
    font-size: .92rem;
    line-height: 1.75;
}

.hero-meta p {
    margin: 0;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 13px;
    margin-top: 28px;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 13px 18px;
    border-radius: 999px;
    text-decoration: none !important;
    font-size: .90rem;
    font-weight: 850;
    transition: .18s ease;
}

.btn:hover {
    transform: translateY(-2px);
}

.btn-primary {
    background: linear-gradient(135deg, var(--blue), var(--cyan));
    color: #03111f !important;
    box-shadow: 0 16px 38px rgba(56,189,248,.20);
}

.btn-secondary {
    color: var(--text) !important;
    border: 1px solid var(--border);
    background: rgba(255,255,255,.045);
}

.btn-secondary:hover {
    color: var(--cyan) !important;
    border-color: rgba(103,232,249,.40);
}

.profile-panel {
    border: 1px solid var(--border);
    border-radius: 34px;
    background:
        linear-gradient(135deg, rgba(56,189,248,.08), rgba(129,140,248,.045)),
        radial-gradient(circle at 18% 18%, rgba(56,189,248,.13), transparent 30%),
        radial-gradient(circle at 84% 0%, rgba(103,232,249,.10), transparent 30%),
        rgba(8,17,34,.88);
    backdrop-filter: blur(18px);
    box-shadow:
        0 0 0 1px rgba(255,255,255,.05),
        0 28px 80px rgba(0,0,0,.42),
        0 0 70px rgba(56,189,248,.08);
    overflow: hidden;
    padding: 26px;
}

.profile-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 24px;
}

.profile-role {
    color: var(--cyan);
    font-size: .72rem;
    font-weight: 900;
    letter-spacing: .20em;
    text-transform: uppercase;
}

.profile-title {
    margin-top: 12px;
    color: white;
    font-size: clamp(1.35rem, 2.1vw, 2rem);
    line-height: 1.16;
    letter-spacing: -.04em;
    font-weight: 900;
}

.status-pill {
    flex: none;
    color: #e0faff;
    border: 1px solid rgba(103,232,249,.22);
    background: rgba(103,232,249,.08);
    padding: 8px 11px;
    border-radius: 999px;
    font-size: .74rem;
    font-weight: 850;
}

.snapshot-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.snapshot-card {
    min-height: 132px;
    padding: 16px;
    border-radius: 22px;
    border: 1px solid var(--border);
    background: rgba(255,255,255,.045);
    transition: .22s ease;
}

.snapshot-card:hover {
    transform: translateY(-3px);
    border-color: rgba(103,232,249,.34);
    background: rgba(255,255,255,.065);
}

.snapshot-card strong {
    display: block;
    color: white;
    margin-bottom: 9px;
    font-size: .96rem;
}

.snapshot-card span {
    color: var(--muted);
    font-size: .88rem;
    line-height: 1.55;
}

.feature-card {
    margin-top: 14px;
    padding: 20px;
    border-radius: 24px;
    border: 1px solid rgba(103,232,249,.24);
    background: linear-gradient(135deg, rgba(56,189,248,.12), rgba(129,140,248,.07));
}

.feature-card strong {
    display: block;
    color: white;
    font-size: 2.15rem;
    line-height: .95;
    letter-spacing: -.055em;
    font-weight: 900;
}

.feature-card span {
    display: block;
    color: var(--soft);
    margin-top: 9px;
    line-height: 1.55;
}

.metric-wrap,
.section,
.contact-card,
.footer-line {
    width: min(var(--max), calc(100vw - 40px));
    margin: 0 auto;
}

.metric-wrap {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    padding: 22px 0 36px;
}

.metric-card,
.proof-card,
.case-card,
.skill-card,
.timeline-card,
.edu-card,
.contact-card {
    border: 1px solid var(--border);
    background: var(--panel);
    backdrop-filter: blur(18px);
    box-shadow: 0 20px 70px rgba(0,0,0,.25);
}

.metric-card {
    min-height: 132px;
    padding: 21px;
    border-radius: 24px;
}

.metric-value {
    color: white;
    font-size: clamp(1.8rem, 3vw, 2.6rem);
    line-height: 1;
    letter-spacing: -.055em;
    font-weight: 900;
}

.metric-label {
    margin-top: 11px;
    color: white;
    font-size: .92rem;
    font-weight: 850;
}

.metric-note {
    margin-top: 7px;
    color: var(--muted);
    line-height: 1.45;
    font-size: .86rem;
}

.section {
    padding: 86px 0 0;
}

.section-head {
    max-width: 820px;
    margin-bottom: 32px;
}

.section-eyebrow {
    color: var(--cyan);
    font-size: .76rem;
    font-weight: 900;
    letter-spacing: .24em;
    text-transform: uppercase;
}

.section h2 {
    margin: 13px 0 0;
    color: white;
    font-size: clamp(2rem, 4vw, 3.7rem);
    line-height: 1.05;
    letter-spacing: -.055em;
    font-weight: 900;
}

.section-subtitle {
    margin-top: 16px;
    color: var(--muted);
    font-size: 1rem;
    line-height: 1.7;
}

.proof-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
}

.proof-card {
    padding: 23px;
    border-radius: 24px;
    transition: .22s ease;
}

.proof-card:hover,
.case-card:hover,
.skill-card:hover {
    transform: translateY(-3px);
    border-color: rgba(103,232,249,.34);
    background: rgba(255,255,255,.065);
}

.proof-card strong {
    display: block;
    color: var(--cyan);
    font-size: .76rem;
    font-weight: 900;
    letter-spacing: .16em;
    text-transform: uppercase;
}

.proof-card p {
    margin: 16px 0 0;
    color: var(--soft);
    line-height: 1.66;
    font-size: .94rem;
}

.case-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.case-card {
    border-radius: 28px;
    padding: 26px;
    transition: .22s ease;
    position: relative;
    overflow: hidden;
    min-height: 360px;
}

.case-card::after {
    content: '';
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: radial-gradient(circle at 96% 0%, rgba(56,189,248,.10), transparent 32%);
}

.case-card > * {
    position: relative;
    z-index: 1;
}

.case-top {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    align-items: flex-start;
    margin-bottom: 18px;
}

.case-number {
    color: var(--cyan);
    font-size: .74rem;
    font-weight: 950;
    letter-spacing: .18em;
    text-transform: uppercase;
}

.tags {
    display: flex;
    gap: 7px;
    flex-wrap: wrap;
    justify-content: flex-end;
}

.tag {
    color: #e0faff;
    background: rgba(56,189,248,.10);
    border: 1px solid rgba(103,232,249,.20);
    border-radius: 999px;
    padding: 7px 9px;
    font-size: .72rem;
    font-weight: 850;
}

.case-card h3 {
    margin: 0;
    color: white;
    font-size: clamp(1.22rem, 1.8vw, 1.65rem);
    line-height: 1.18;
    letter-spacing: -.035em;
    font-weight: 900;
}

.case-body {
    display: block;
    margin-top: 16px;
}

.case-label {
    color: var(--muted);
    font-size: .70rem;
    font-weight: 900;
    letter-spacing: .16em;
    text-transform: uppercase;
    margin-top: 16px;
}

.case-card p {
    color: var(--soft);
    line-height: 1.68;
    margin: 7px 0 0;
    font-size: .94rem;
}

.impact-list {
    list-style: none;
    padding: 0;
    margin: 12px 0 0;
    display: grid;
    gap: 9px;
}

.impact-list li {
    color: var(--soft);
    line-height: 1.52;
    padding-left: 18px;
    border: none;
    background: transparent;
    position: relative;
    font-size: .94rem;
}

.impact-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: .65em;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--blue), var(--cyan));
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.skill-card {
    padding: 25px;
    border-radius: 28px;
    transition: .22s ease;
}

.skill-card h3 {
    margin: 0 0 17px;
    color: white;
    font-size: 1.18rem;
    letter-spacing: -.025em;
    font-weight: 900;
}

.chips {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
}

.chip {
    color: var(--soft);
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 999px;
    padding: 9px 11px;
    font-size: .84rem;
    font-weight: 700;
}

.timeline-card,
.edu-card {
    border-radius: 28px;
    padding: 28px;
}

.timeline-top {
    display: flex;
    justify-content: space-between;
    gap: 26px;
    padding-bottom: 20px;
    margin-bottom: 18px;
    border-bottom: 1px solid rgba(255,255,255,.10);
}

.timeline-card h3,
.edu-card h3 {
    margin: 0;
    color: white;
    font-size: 1.35rem;
    letter-spacing: -.03em;
    font-weight: 900;
}

.company,
.edu-degree {
    margin-top: 7px;
    color: var(--cyan);
    font-weight: 850;
}

.period,
.edu-meta {
    color: var(--muted);
    line-height: 1.65;
}

.period {
    text-align: right;
    white-space: nowrap;
    font-weight: 700;
}

.active-pill,
.cgpa {
    display: inline-flex;
    margin-top: 9px;
    color: #e0faff;
    background: rgba(103,232,249,.08);
    border: 1px solid rgba(103,232,249,.18);
    border-radius: 999px;
    padding: 7px 10px;
    font-size: .76rem;
    font-weight: 850;
}

.edu-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.edu-meta {
    margin: 12px 0 0;
}

.contact-wrap {
    padding: 90px 0 34px;
}

.contact-card {
    border-radius: 32px;
    padding: 34px;
    display: grid;
    grid-template-columns: 1.05fr .95fr;
    gap: 28px;
    align-items: center;
    background:
        radial-gradient(circle at 0% 0%, rgba(56,189,248,.12), transparent 30%),
        linear-gradient(135deg, rgba(129,140,248,.08), rgba(255,255,255,.04));
}

.contact-card h2 {
    margin: 12px 0 0;
    color: white;
    font-size: clamp(1.9rem, 3.8vw, 3.5rem);
    line-height: 1.04;
    letter-spacing: -.055em;
    font-weight: 900;
}

.contact-card p {
    color: var(--muted);
    line-height: 1.7;
}

.contact-links {
    display: grid;
    gap: 12px;
}

.contact-link {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    color: white !important;
    text-decoration: none !important;
    padding: 15px;
    border-radius: 17px;
    border: 1px solid rgba(255,255,255,.10);
    background: rgba(255,255,255,.045);
    font-weight: 850;
}

.contact-link:hover {
    color: var(--cyan) !important;
    border-color: rgba(103,232,249,.34);
}

.contact-link span {
    color: var(--muted);
    font-size: .74rem;
    text-transform: uppercase;
    letter-spacing: .14em;
}

.footer-line {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    padding: 26px 0 46px;
    border-top: 1px solid rgba(255,255,255,.10);
    color: var(--muted);
    font-size: .88rem;
}

@media (max-width: 1050px) {
    .hero,
    .contact-card {
        grid-template-columns: 1fr;
    }

    .metric-wrap,
    .proof-grid,
    .case-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .profile-panel {
        max-width: 720px;
    }
}

@media (max-width: 760px) {
    .nav-inner {
        height: auto;
        padding: 16px 0;
        flex-direction: column;
        align-items: flex-start;
    }

    .nav-links {
        width: 100%;
        overflow-x: auto;
        gap: 18px;
        padding-bottom: 5px;
    }

    .resume-pill {
        display: none;
    }

    .hero {
        padding: 54px 0 30px;
    }

    .hero h1 {
        font-size: clamp(2.25rem, 10vw, 3.8rem);
    }

    .snapshot-grid,
    .metric-wrap,
    .proof-grid,
    .case-grid,
    .skills-grid,
    .edu-grid {
        grid-template-columns: 1fr;
    }

    .section {
        padding-top: 70px;
    }

    .timeline-top {
        flex-direction: column;
    }

    .period {
        text-align: left;
        white-space: normal;
    }

    .footer-line {
        flex-direction: column;
    }
}
</style>
"""

HTML = f"""
<div class="site-nav">
  <div class="nav-inner">
    <a class="brand" href="#top">Shalini Pathak</a>
    <nav class="nav-links">
      <a href="#case-studies">Case Studies</a>
      <a href="#skills">Skills</a>
      <a href="#experience">Experience</a>
      <a href="#education">Education</a>
      <a href="#contact">Contact</a>
    </nav>
    <a class="resume-pill" href="{resume_href}" download="Shalini_Pathak_Resume.pdf">Resume</a>
  </div>
</div>

<div class="ticker">
  <div class="ticker-inner">
    <div class="ticker-track">
      <span>60% fewer manual operations</span>
      <span>78% faster batch processing</span>
      <span>450+ portal users supported</span>
      <span>99.95% service availability maintained</span>
      <span>28% lower p95 API latency</span>
      <span>70% fewer audit findings</span>
      <span>60% fewer manual operations</span>
      <span>78% faster batch processing</span>
      <span>450+ portal users supported</span>
      <span>99.95% service availability maintained</span>
      <span>28% lower p95 API latency</span>
      <span>70% fewer audit findings</span>
    </div>
  </div>
</div>

<div id="top"></div>

<section class="hero">
  <div>
    <div class="kicker">Shalini Pathak · SAP Commerce Cloud Developer</div>

    <h1>
      I build <span class="text-gradient">SAP Commerce backends and B2B portal workflows</span>
      for reliable enterprise commerce.
    </h1>

    <p class="hero-copy">
      Associate Software Developer at Collins Aerospace with 3+ years of experience building SAP Commerce Cloud
      and SAP Hybris backend solutions across OCC APIs, Backoffice workflows, cron-job automation,
      security controls and production reliability.
    </p>

    <div class="hero-meta">
      <p>Bangalore, India · Backend engineering · Enterprise B2B commerce platforms</p>
      <p>Best fit: SAP Commerce Cloud, Hybris backend, OCC APIs and platform automation roles</p>
    </div>

    <div class="hero-actions">
      <a class="btn btn-primary" href="#case-studies">View Case Studies</a>
      <a class="btn btn-secondary" href="{resume_href}" download="Shalini_Pathak_Resume.pdf">Download Resume</a>
      <a class="btn btn-secondary" href="mailto:shalinipathak3@gmail.com">Email</a>
    </div>
  </div>

  <aside class="profile-panel">
    <div class="profile-head">
      <div>
        <div class="profile-role">Engineering focus areas</div>
        <div class="profile-title">
           Platform strengths across APIs, automation, security and production reliability.
        </div>
      </div>
      <div class="status-pill">Open to backend roles</div>
    </div>

    <div class="snapshot-grid">
      <div class="snapshot-card">
        <strong>Commerce platform</strong>
        <span>SAP Hybris, SAP Commerce Cloud, CCv2, Backoffice, WCMS, Solr and Impex-led migration flows.</span>
      </div>

      <div class="snapshot-card">
        <strong>API engineering</strong>
        <span>Java, Spring MVC, RESTful services and OCC APIs connecting portal features with external systems.</span>
      </div>

      <div class="snapshot-card">
        <strong>Automation</strong>
        <span>Cron jobs, workflow customization and reusable backend components that remove repetitive platform operations.</span>
      </div>

      <div class="snapshot-card">
        <strong>Security controls</strong>
        <span>Role-based access, sensitive-data masking and row-level restrictions for enterprise data workflows.</span>
      </div>
    </div>

    <div class="feature-card">
      <strong>99.95%</strong>
      <span>service availability maintained while supporting production incidents, release delivery and customer portal performance.</span>
    </div>
  </aside>
</section>

<section class="metric-wrap">
  <div class="metric-card">
    <div class="metric-value">60%</div>
    <div class="metric-label">Manual operations reduced</div>
    <div class="metric-note">SAP Commerce automation across recurring workflows</div>
  </div>

  <div class="metric-card">
    <div class="metric-value">78%</div>
    <div class="metric-label">Batch processing improved</div>
    <div class="metric-note">18-minute process reduced to around 4 minutes</div>
  </div>

  <div class="metric-card">
    <div class="metric-value">450+</div>
    <div class="metric-label">Portal users supported</div>
    <div class="metric-note">B2B self-service and customer portal workflows</div>
  </div>

  <div class="metric-card">
    <div class="metric-value">99.95%</div>
    <div class="metric-label">Service availability</div>
    <div class="metric-note">Production support across release and incident cycles</div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div class="section-eyebrow">Proof over keywords</div>
    <h2>Skills shown through shipped platform outcomes.</h2>
    <p class="section-subtitle">
      The structure is not a resume copy, but a proof-led view of problems,
      technical work and measurable results.
    </p>
  </div>

  <div class="proof-grid">
    <div class="proof-card">
      <strong>Commerce Automation</strong>
      <p>Hybris customizations, cron jobs, Impex scripts and Backoffice workflows that reduce repeated platform operations.</p>
    </div>

    <div class="proof-card">
      <strong>API Delivery</strong>
      <p>OCC and REST API development using Java and Spring MVC for B2B portal and external-system integration.</p>
    </div>

    <div class="proof-card">
      <strong>Security Controls</strong>
      <p>Role-based access, sensitive-data masking and row-level restrictions for enterprise data workflows.</p>
    </div>

    <div class="proof-card">
      <strong>Reliability</strong>
      <p>P1/P2 incident handling, p95 latency improvement and production support for customer portal environments.</p>
    </div>
  </div>
</section>

<div id="case-studies"></div>

<section class="section">
  <div class="section-head">
    <div class="section-eyebrow">Industry case studies</div>
    <h2>Real SAP Commerce problems solved across automation, APIs, security and reliability.</h2>
    <p class="section-subtitle">
      Each case uses a serious portfolio structure: problem, solution and measurable impact.
    </p>
  </div>

  <div class="case-grid">
    <div class="case-card">
      <div class="case-top">
        <span class="case-number">Case Study 01</span>
        <div class="tags">
          <span class="tag">SAP Hybris</span>
          <span class="tag">Cron Jobs</span>
          <span class="tag">Impex</span>
        </div>
      </div>
      <h3>B2B SAP Commerce Automation Suite</h3>
      <div class="case-body">
        <div>
          <div class="case-label">Problem</div>
          <p>Manual B2B operations required repeatable backend automation across Backoffice, migration scripts and customer portal workflows.</p>
        </div>
        <div>
          <div class="case-label">Solution and impact</div>
          <p>Designed SAP Hybris B2B customizations, Impex-based migration scripts and cron jobs to automate enterprise commerce workflows.</p>
          <ul class="impact-list">
            <li>Reduced manual operations by 60%</li>
            <li>Improved batch processing from 18 minutes to 4 minutes</li>
            <li>Supported SBU, offboarding, warranty-claim and portal workflows</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="case-card">
      <div class="case-top">
        <span class="case-number">Case Study 02</span>
        <div class="tags">
          <span class="tag">OCC</span>
          <span class="tag">Spring MVC</span>
          <span class="tag">CCv2</span>
        </div>
      </div>
      <h3>Headless B2B Portal APIs</h3>
      <div class="case-body">
        <div>
          <div class="case-label">Problem</div>
          <p>B2B portal features needed stable API connections between SAP Commerce Cloud and external enterprise systems.</p>
        </div>
        <div>
          <div class="case-label">Solution and impact</div>
          <p>Built and customized OCC web services and RESTful APIs in SAP Commerce Cloud to support headless portal functionality.</p>
          <ul class="impact-list">
            <li>Enabled smoother B2B portal functionality</li>
            <li>Supported self-service access for 450+ users</li>
            <li>Contributed to a 12-point increase in customer portal satisfaction</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="case-card">
      <div class="case-top">
        <span class="case-number">Case Study 03</span>
        <div class="tags">
          <span class="tag">RBAC</span>
          <span class="tag">PII Masking</span>
          <span class="tag">Security</span>
        </div>
      </div>
      <h3>Enterprise Data Protection Controls</h3>
      <div class="case-body">
        <div>
          <div class="case-label">Problem</div>
          <p>Enterprise workflows required stricter access control and cleaner handling of sensitive platform data.</p>
        </div>
        <div>
          <div class="case-label">Solution and impact</div>
          <p>Architected controls including role-based access, sensitive-data masking and row-level restrictions within SAP Commerce workflows.</p>
          <ul class="impact-list">
            <li>Reduced audit findings by 70%</li>
            <li>Aligned controls with SAP Commerce security practices</li>
            <li>Improved sensitive-data handling for enterprise workflows</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="case-card">
      <div class="case-top">
        <span class="case-number">Case Study 04</span>
        <div class="tags">
          <span class="tag">Performance</span>
          <span class="tag">Production</span>
          <span class="tag">Reliability</span>
        </div>
      </div>
      <h3>Customer Portal Performance and Reliability</h3>
      <div class="case-body">
        <div>
          <div class="case-label">Problem</div>
          <p>Critical portal incidents and backend latency affected customer-facing reliability and release confidence.</p>
        </div>
        <div>
          <div class="case-label">Solution and impact</div>
          <p>Diagnosed P1/P2 incidents, improved backend performance and collaborated with Product, QA and DevOps during release cycles.</p>
          <ul class="impact-list">
            <li>Maintained 99.95% service availability</li>
            <li>Improved p95 API latency by 28%</li>
            <li>Achieved 1.8-hour MTTR for critical incidents</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<div id="skills"></div>

<section class="section">
  <div class="section-head">
    <div class="section-eyebrow">Technical stack</div>
    <h2>Grouped by how the work is delivered.</h2>
    <p class="section-subtitle">
      A cleaner skills section for recruiters and hiring managers, without turning the page into a keyword dump.
    </p>
  </div>

  <div class="skills-grid">
    <div class="skill-card">
      <h3>SAP Commerce Cloud</h3>
      <div class="chips">
        <span class="chip">SAP Hybris</span>
        <span class="chip">CCv2</span>
        <span class="chip">OCC / Headless</span>
        <span class="chip">Backoffice</span>
        <span class="chip">WCMS</span>
        <span class="chip">Impex</span>
        <span class="chip">Cron Jobs</span>
        <span class="chip">Solr</span>
        <span class="chip">Hot Folder</span>
        <span class="chip">Populators</span>
        <span class="chip">Converters</span>
        <span class="chip">Interceptors</span>
        <span class="chip">Restrictions</span>
      </div>
    </div>

    <div class="skill-card">
      <h3>Backend Engineering</h3>
      <div class="chips">
        <span class="chip">Java</span>
        <span class="chip">Spring MVC</span>
        <span class="chip">Spring Hibernate</span>
        <span class="chip">RESTful APIs</span>
        <span class="chip">Microservices</span>
        <span class="chip">System Design</span>
        <span class="chip">Performance Optimization</span>
        <span class="chip">Code Review</span>
      </div>
    </div>

    <div class="skill-card">
      <h3>Data and Security</h3>
      <div class="chips">
        <span class="chip">SQL</span>
        <span class="chip">MySQL</span>
        <span class="chip">Oracle</span>
        <span class="chip">DBMS</span>
        <span class="chip">Data Modeling</span>
        <span class="chip">RBAC</span>
        <span class="chip">PII Masking</span>
        <span class="chip">Row-level Security</span>
        <span class="chip">JSON</span>
        <span class="chip">XML</span>
      </div>
    </div>

    <div class="skill-card">
      <h3>Delivery Tools</h3>
      <div class="chips">
        <span class="chip">Git</span>
        <span class="chip">Jenkins</span>
        <span class="chip">Azure DevOps</span>
        <span class="chip">CI/CD</span>
        <span class="chip">Eclipse</span>
        <span class="chip">IntelliJ IDEA</span>
        <span class="chip">Agile</span>
        <span class="chip">QA Collaboration</span>
      </div>
    </div>
  </div>
</section>

<div id="experience"></div>

<section class="section">
  <div class="section-head">
    <div class="section-eyebrow">Experience</div>
    <h2>Where the platform work has been applied.</h2>
  </div>

  <div class="timeline-card">
    <div class="timeline-top">
      <div>
        <h3>Associate Software Developer</h3>
        <div class="company">Collins Aerospace · Bangalore, India</div>
      </div>
      <div class="period">
        Feb 2023 - Present<br>
        <span class="active-pill">Current role</span>
      </div>
    </div>

    <ul class="impact-list">
      <li>Designed and implemented SAP Hybris B2B customizations, Backoffice workflows, Impex scripts, cron jobs, WCMS components and customer portal dashboards.</li>
      <li>Delivered 3+ high-impact automation initiatives that reduced user task time by 40% and enabled self-service data access for 450+ users.</li>
      <li>Collaborated with Product, QA and DevOps teams to deliver 4 releases per quarter with 95% on-time delivery.</li>
    </ul>
  </div>
</section>

<div id="education"></div>

<section class="section">
  <div class="section-head">
    <div class="section-eyebrow">Education</div>
    <h2>Academic background.</h2>
  </div>

  <div class="edu-grid">
    <div class="edu-card">
      <h3>PES University, Bangalore</h3>
      <div class="edu-degree">Master of Computer Applications</div>
      <div class="edu-meta">Dec 2021 - Jul 2023 · Machine Learning, Design and Analysis of Algorithms, Data Visualization, Java</div>
      <span class="cgpa">CGPA 8.28 / 10</span>
    </div>

    <div class="edu-card">
      <h3>Lalit Narayan Mishra Institute, Patna</h3>
      <div class="edu-degree">Bachelor of Computer Applications</div>
      <div class="edu-meta">Aug 2017 - Jul 2020 · Data Structures, DBMS, Web Development, Statistics</div>
      <span class="cgpa">CGPA 7.9 / 10</span>
    </div>
  </div>
</section>

<div id="contact"></div>

<div class="contact-wrap">
  <div class="contact-card">
    <div>
      <div class="section-eyebrow">Contact</div>
      <h2>Open to SAP Commerce, backend and B2B platform roles.</h2>
      <p>Best fit: SAP Commerce Cloud, Hybris backend, OCC API development, enterprise portal engineering and platform automation roles.</p>
    </div>

    <div class="contact-links">
      <a class="contact-link" href="mailto:shalinipathak3@gmail.com">
        <span>Email</span>
        <strong>shalinipathak3@gmail.com</strong>
      </a>

      <a class="contact-link" href="https://www.linkedin.com/in/shalini-pathak-6bb331216/" target="_blank">
        <span>LinkedIn</span>
        <strong>View Profile</strong>
      </a>

      <a class="contact-link" href="{resume_href}" download="Shalini_Pathak_Resume.pdf">
        <span>Resume</span>
        <strong>Download PDF</strong>
      </a>
    </div>
  </div>
</div>

<div class="footer-line">
  <span>SAP Commerce Cloud portfolio</span>
  <span>Built with Streamlit</span>
</div>
"""


def render_html(markup: str) -> None:
    cleaned = "\n".join(line.lstrip() for line in markup.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


render_html(CSS)

if not RESUME_PATH.exists():
    st.warning("Resume PDF not found. Add it at assets/Shalini_Resume.pdf to enable the download buttons.")

render_html(HTML)
