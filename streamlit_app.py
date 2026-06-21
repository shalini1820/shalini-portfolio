from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
RESUME_PATH = BASE_DIR / "assets" / "Shalini_Resume.pdf"

st.set_page_config(
    page_title="Shalini | SAP Commerce Cloud Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def pdf_download_link(path: Path) -> str:
    """Return a browser download link for the resume PDF."""
    if not path.exists():
        return "#"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:application/pdf;base64,{encoded}"


resume_href = pdf_download_link(RESUME_PATH)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg: #06111f;
    --bg-2: #081826;
    --surface: rgba(255,255,255,0.055);
    --surface-2: rgba(255,255,255,0.085);
    --border: rgba(148, 163, 184, 0.20);
    --border-strong: rgba(125, 211, 252, 0.34);
    --text: #eef8ff;
    --muted: #9fb3c8;
    --soft: #c7d7e8;
    --blue: #38bdf8;
    --cyan: #22d3ee;
    --green: #34d399;
    --violet: #a78bfa;
    --amber: #fbbf24;
    --shadow: 0 24px 70px rgba(2, 6, 23, .38);
    --radius-lg: 26px;
    --radius-md: 18px;
    --max: 1180px;
}

html { scroll-behavior: smooth; }

.stApp {
    background:
        radial-gradient(circle at 12% 9%, rgba(56,189,248,.22), transparent 30%),
        radial-gradient(circle at 82% 6%, rgba(167,139,250,.18), transparent 28%),
        radial-gradient(circle at 70% 76%, rgba(52,211,153,.12), transparent 30%),
        linear-gradient(135deg, #06111f 0%, #071827 45%, #040916 100%);
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

section.main-container {
    width: min(var(--max), calc(100vw - 40px));
    margin: 0 auto;
}

.top-nav {
    position: sticky;
    top: 0;
    z-index: 999;
    backdrop-filter: blur(22px);
    background: rgba(6,17,31,.76);
    border-bottom: 1px solid rgba(148,163,184,.15);
}

.nav-inner {
    width: min(var(--max), calc(100vw - 40px));
    height: 72px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none !important;
    color: var(--text) !important;
    font-weight: 850;
    letter-spacing: -.02em;
}

.brand-mark {
    width: 38px;
    height: 38px;
    border-radius: 14px;
    display: grid;
    place-items: center;
    color: #02111f;
    background: linear-gradient(135deg, var(--blue), var(--green));
    box-shadow: 0 12px 28px rgba(56,189,248,.20);
    font-weight: 900;
}

.nav-links {
    display: flex;
    gap: 8px;
    align-items: center;
}

.nav-links a {
    color: var(--muted) !important;
    text-decoration: none !important;
    font-size: .88rem;
    padding: 10px 13px;
    border-radius: 999px;
    border: 1px solid transparent;
    transition: all .18s ease;
}

.nav-links a:hover {
    color: var(--text) !important;
    border-color: rgba(125,211,252,.26);
    background: rgba(255,255,255,.045);
}

.hero {
    width: min(var(--max), calc(100vw - 40px));
    margin: 0 auto;
    min-height: calc(100vh - 72px);
    display: grid;
    grid-template-columns: 1.13fr .87fr;
    align-items: center;
    gap: 44px;
    padding: 74px 0 56px;
}

.kicker {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: 999px;
    background: rgba(255,255,255,.052);
    color: var(--soft);
    font-size: .86rem;
    margin-bottom: 22px;
}

.pulse {
    width: 8px;
    height: 8px;
    border-radius: 999px;
    background: var(--green);
    box-shadow: 0 0 0 7px rgba(52,211,153,.10);
}

.hero h1 {
    margin: 0;
    font-size: clamp(2.4rem, 5.8vw, 5.4rem);
    line-height: .88;
    letter-spacing: -.08em;
    font-weight: 900;
}

.gradient-text {
    background: linear-gradient(120deg, #fff 12%, #9be7ff 45%, #b6ffe3 85%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.hero-role {
    margin-top: 22px;
    color: var(--blue);
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(1rem, 2vw, 1.35rem);
    font-weight: 600;
}

.hero-copy {
    margin: 20px 0 0;
    max-width: 720px;
    color: var(--soft);
    font-size: clamp(1rem, 1.6vw, 1.19rem);
    line-height: 1.78;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-top: 30px;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 13px 18px;
    border-radius: 999px;
    text-decoration: none !important;
    font-weight: 750;
    font-size: .95rem;
    border: 1px solid var(--border);
    transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}

.btn:hover { transform: translateY(-2px); }

.btn-primary {
    background: linear-gradient(135deg, var(--blue), var(--green));
    color: #02111f !important;
    box-shadow: 0 18px 40px rgba(56,189,248,.22);
    border-color: rgba(255,255,255,.12);
}

.btn-ghost {
    background: rgba(255,255,255,.055);
    color: var(--text) !important;
}

.profile-card {
    position: relative;
    border: 1px solid var(--border);
    background:
        linear-gradient(180deg, rgba(255,255,255,.09), rgba(255,255,255,.04)),
        radial-gradient(circle at 18% 0%, rgba(56,189,248,.20), transparent 32%);
    border-radius: 32px;
    padding: 28px;
    box-shadow: var(--shadow);
    overflow: hidden;
}

.profile-card::before {
    content: '';
    position: absolute;
    inset: -1px;
    pointer-events: none;
    background: linear-gradient(135deg, rgba(56,189,248,.28), transparent 35%, rgba(52,211,153,.18));
    mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    padding: 1px;
    -webkit-mask-composite: xor;
    mask-composite: exclude;
}

.avatar {
    width: 118px;
    height: 118px;
    border-radius: 34px;
    display: grid;
    place-items: center;
    background: linear-gradient(135deg, rgba(56,189,248,.98), rgba(52,211,153,.92));
    color: #03111f;
    font-size: 2.45rem;
    font-weight: 900;
    margin-bottom: 18px;
    box-shadow: 0 22px 44px rgba(56,189,248,.20);
}

.card-name {
    font-size: 1.85rem;
    font-weight: 850;
    letter-spacing: -.045em;
    margin: 0;
}

.card-title {
    color: var(--blue);
    font-family: 'JetBrains Mono', monospace;
    margin-top: 4px;
}

.card-line {
    display: flex;
    align-items: center;
    gap: 9px;
    color: var(--muted);
    margin-top: 13px;
    font-size: .95rem;
}

.profile-list {
    display: grid;
    gap: 10px;
    margin-top: 22px;
}

.profile-item {
    display: flex;
    justify-content: space-between;
    gap: 18px;
    padding: 13px 0;
    border-bottom: 1px solid rgba(148,163,184,.13);
}

.profile-item span:first-child {
    color: var(--muted);
}

.profile-item span:last-child {
    color: var(--text);
    font-weight: 700;
    text-align: right;
}

.metric-strip {
    width: min(var(--max), calc(100vw - 40px));
    margin: -6px auto 0;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
}

.metric-card {
    border: 1px solid var(--border);
    background: rgba(255,255,255,.052);
    border-radius: 22px;
    padding: 22px;
    min-height: 128px;
}

.metric-value {
    font-size: clamp(1.7rem, 3vw, 2.45rem);
    font-weight: 900;
    letter-spacing: -.06em;
    color: var(--text);
}

.metric-label {
    color: var(--muted);
    margin-top: 6px;
    line-height: 1.45;
    font-size: .93rem;
}

.section {
    width: min(var(--max), calc(100vw - 40px));
    margin: 0 auto;
    padding: 96px 0 0;
}

.section-heading {
    max-width: 760px;
    margin-bottom: 34px;
}

.section-eyebrow {
    color: var(--green);
    font-family: 'JetBrains Mono', monospace;
    font-size: .82rem;
    letter-spacing: .12em;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 10px;
}

.section h2 {
    font-size: clamp(2.1rem, 4.1vw, 4rem);
    line-height: 1.02;
    letter-spacing: -.07em;
    margin: 0;
}

.section-subtitle {
    color: var(--muted);
    margin-top: 14px;
    font-size: 1.03rem;
    line-height: 1.72;
}

.proof-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
}

.proof-card, .case-card, .skill-card, .timeline-card, .edu-card, .contact-card {
    border: 1px solid var(--border);
    background: linear-gradient(180deg, rgba(255,255,255,.065), rgba(255,255,255,.035));
    border-radius: var(--radius-lg);
    box-shadow: 0 20px 48px rgba(2,6,23,.16);
}

.proof-card {
    padding: 22px;
}

.proof-card strong {
    display: block;
    font-size: 1.05rem;
    margin-bottom: 8px;
}

.proof-card p {
    color: var(--muted);
    margin: 0;
    line-height: 1.62;
    font-size: .95rem;
}

.case-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.case-card {
    padding: 26px;
    position: relative;
    overflow: hidden;
}

.case-card::after {
    content: '';
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: radial-gradient(circle at 90% 0%, rgba(56,189,248,.12), transparent 28%);
}

.case-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 18px;
    margin-bottom: 14px;
}

.case-number {
    color: var(--blue);
    font-family: 'JetBrains Mono', monospace;
    font-size: .86rem;
    font-weight: 700;
}

.tags {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: flex-end;
}

.tag {
    display: inline-flex;
    padding: 6px 9px;
    border: 1px solid rgba(125,211,252,.21);
    background: rgba(56,189,248,.07);
    color: #bceeff;
    border-radius: 999px;
    font-size: .75rem;
    font-weight: 700;
}

.case-card h3 {
    font-size: 1.35rem;
    letter-spacing: -.035em;
    margin: 0 0 12px;
}

.case-card p {
    color: var(--muted);
    line-height: 1.7;
    margin: 0;
}

.impact-list {
    list-style: none;
    padding: 0;
    margin: 18px 0 0;
    display: grid;
    gap: 10px;
}

.impact-list li {
    color: var(--soft);
    line-height: 1.5;
    padding-left: 24px;
    position: relative;
}

.impact-list li::before {
    content: '✓';
    position: absolute;
    left: 0;
    top: 0;
    color: var(--green);
    font-weight: 900;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.skill-card {
    padding: 24px;
}

.skill-title {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
}

.skill-icon {
    width: 42px;
    height: 42px;
    display: grid;
    place-items: center;
    border-radius: 15px;
    background: rgba(56,189,248,.12);
    border: 1px solid rgba(125,211,252,.18);
}

.skill-title h3 {
    margin: 0;
    font-size: 1.15rem;
    letter-spacing: -.03em;
}

.chips {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
}

.chip {
    padding: 8px 10px;
    border-radius: 999px;
    background: rgba(255,255,255,.055);
    color: var(--soft);
    border: 1px solid rgba(148,163,184,.16);
    font-size: .84rem;
}

.timeline-card {
    padding: 30px;
}

.timeline-top {
    display: flex;
    justify-content: space-between;
    gap: 24px;
    border-bottom: 1px solid rgba(148,163,184,.14);
    padding-bottom: 20px;
    margin-bottom: 20px;
}

.timeline-card h3 {
    margin: 0 0 7px;
    font-size: 1.45rem;
    letter-spacing: -.04em;
}

.company {
    color: var(--blue);
    font-weight: 700;
}

.period {
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    white-space: nowrap;
    text-align: right;
}

.active-pill {
    display: inline-flex;
    margin-top: 8px;
    padding: 5px 9px;
    border-radius: 999px;
    background: rgba(52,211,153,.10);
    color: #a7f3d0;
    border: 1px solid rgba(52,211,153,.20);
    font-family: 'Inter', sans-serif;
    font-size: .75rem;
    font-weight: 800;
}

.edu-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.edu-card {
    padding: 24px;
}

.edu-card h3 {
    margin: 0 0 8px;
    font-size: 1.15rem;
    letter-spacing: -.03em;
}

.edu-degree {
    color: var(--blue);
    font-weight: 750;
    margin-bottom: 9px;
}

.edu-meta {
    color: var(--muted);
    margin-bottom: 14px;
}

.cgpa {
    display: inline-flex;
    padding: 8px 10px;
    border-radius: 999px;
    background: rgba(251,191,36,.10);
    color: #fde68a;
    border: 1px solid rgba(251,191,36,.22);
    font-weight: 800;
    font-size: .85rem;
}

.contact-wrap {
    padding: 96px 0 34px;
}

.contact-card {
    width: min(var(--max), calc(100vw - 40px));
    margin: 0 auto;
    padding: 34px;
    display: grid;
    grid-template-columns: 1.08fr .92fr;
    gap: 24px;
    align-items: center;
    background:
        radial-gradient(circle at 0% 0%, rgba(56,189,248,.15), transparent 26%),
        linear-gradient(180deg, rgba(255,255,255,.075), rgba(255,255,255,.035));
}

.contact-card h2 {
    margin: 0;
    font-size: clamp(2rem, 4vw, 3.4rem);
    line-height: 1.02;
    letter-spacing: -.07em;
}

.contact-card p {
    color: var(--muted);
    margin-top: 12px;
    line-height: 1.7;
}

.contact-links {
    display: grid;
    gap: 12px;
}

.contact-link {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px;
    border-radius: 17px;
    background: rgba(255,255,255,.055);
    border: 1px solid rgba(148,163,184,.16);
    color: var(--text) !important;
    text-decoration: none !important;
    font-weight: 700;
}

.footer-line {
    width: min(var(--max), calc(100vw - 40px));
    margin: 0 auto;
    padding: 28px 0 46px;
    border-top: 1px solid rgba(148,163,184,.14);
    color: var(--muted);
    display: flex;
    justify-content: space-between;
    gap: 18px;
    font-size: .9rem;
}

@media (max-width: 980px) {
    .hero, .contact-card { grid-template-columns: 1fr; }
    .metric-strip, .proof-grid { grid-template-columns: repeat(2, 1fr); }
    .case-grid, .skills-grid, .edu-grid { grid-template-columns: 1fr; }
    .profile-card { max-width: 650px; }
}

@media (max-width: 720px) {
    .nav-inner { height: auto; padding: 14px 0; align-items: flex-start; gap: 12px; flex-direction: column; }
    .nav-links { width: 100%; overflow-x: auto; padding-bottom: 4px; }
    .hero { padding-top: 50px; min-height: auto; }
    .metric-strip, .proof-grid { grid-template-columns: 1fr; }
    .section { padding-top: 72px; }
    .timeline-top { flex-direction: column; }
    .period { text-align: left; white-space: normal; }
    .footer-line { flex-direction: column; }
}
</style>
"""

HTML = f"""
<div class="top-nav">
  <div class="nav-inner">
    <a class="brand" href="#top"><span class="brand-mark">S</span><span>Shalini</span></a>
    <nav class="nav-links">
      <a href="#proof">Proof</a>
      <a href="#case-studies">Case Studies</a>
      <a href="#skills">Skills</a>
      <a href="#experience">Experience</a>
      <a href="#contact">Contact</a>
    </nav>
  </div>
</div>

<div id="top"></div>
<section class="hero">
  <div>
    <div class="kicker"><span class="pulse"></span> Available for SAP Commerce, backend and enterprise platform roles</div>
    <h1><span class="gradient-text">Shalini</span><br>Pathak</h1>
    <div class="hero-role">SAP Commerce Cloud Developer · Backend Engineering</div>
    <p class="hero-copy">
      Backend developer with 3+ years of hands-on experience delivering B2B enterprise solutions on SAP Hybris / SAP Commerce Cloud. I build secure commerce backends, OCC APIs, cron-job automation, Backoffice workflows and performance improvements that reduce manual work and improve enterprise portal reliability.
    </p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#case-studies">View case studies ↓</a>
      <a class="btn btn-ghost" href="{resume_href}" download="Shalini_Pathak_Resume.pdf">Download resume ↗</a>
      <a class="btn btn-ghost" href="mailto:shalinipathak3@gmail.com">Email me</a>
    </div>
  </div>

  <aside class="profile-card">
    <div class="avatar">SP</div>
    <h2 class="card-name">SAP Commerce Backend Developer</h2>
    <div class="card-title">Hybris · OCC · CCv2 · Java · Spring MVC</div>
    <div class="card-line">📍 Bangalore, Karnataka, India</div>
    <div class="profile-list">
      <div class="profile-item"><span>Current role</span><span>Associate Software Developer</span></div>
      <div class="profile-item"><span>Company</span><span>Collins Aerospace</span></div>
      <div class="profile-item"><span>Experience</span><span>3+ years</span></div>
      <div class="profile-item"><span>Core strength</span><span>B2B enterprise platforms</span></div>
    </div>
  </aside>
</section>

<section class="metric-strip">
  <div class="metric-card"><div class="metric-value">60%</div><div class="metric-label">manual operations reduced through SAP Commerce automation</div></div>
  <div class="metric-card"><div class="metric-value">78%</div><div class="metric-label">batch processing improvement from 18 minutes to 4 minutes</div></div>
  <div class="metric-card"><div class="metric-value">450+</div><div class="metric-label">users supported through B2B customer portal initiatives</div></div>
  <div class="metric-card"><div class="metric-value">99.95%</div><div class="metric-label">service availability maintained across production support</div></div>
</section>

<div id="proof"></div>
<section class="section">
  <div class="section-heading">
    <div class="section-eyebrow">Proof over keywords</div>
    <h2>Backend work shown through real platform outcomes.</h2>
    <p class="section-subtitle">This portfolio is structured like a case-study portfolio: what business problem existed, what was built, and what changed after the solution.</p>
  </div>
  <div class="proof-grid">
    <div class="proof-card"><strong>Commerce automation</strong><p>Built Hybris customizations, cron jobs, Impex scripts and Backoffice workflows to reduce repetitive manual operations.</p></div>
    <div class="proof-card"><strong>API delivery</strong><p>Developed OCC/headless web services and REST APIs using Spring MVC for B2B portal and external-system integration.</p></div>
    <div class="proof-card"><strong>Data security</strong><p>Implemented RBAC, PII masking and row-level security controls aligned with enterprise platform standards.</p></div>
    <div class="proof-card"><strong>Reliability</strong><p>Handled P1/P2 production incidents, optimized p95 API latency, and supported regular quarterly releases.</p></div>
  </div>
</section>

<div id="case-studies"></div>
<section class="section">
  <div class="section-heading">
    <div class="section-eyebrow">Selected impact</div>
    <h2>Case studies from SAP Commerce and B2B platform work.</h2>
    <p class="section-subtitle">Each case focuses on a concrete engineering contribution instead of repeating a standard job description.</p>
  </div>
  <div class="case-grid">
    <div class="case-card">
      <div class="case-top"><span class="case-number">Case Study 01</span><div class="tags"><span class="tag">SAP Hybris</span><span class="tag">Cron Jobs</span><span class="tag">Impex</span></div></div>
      <h3>B2B SAP Commerce Automation Suite</h3>
      <p>Designed SAP Hybris B2B customizations, Backoffice customizations, Impex-based migration scripts and cron jobs to automate enterprise workflows.</p>
      <ul class="impact-list"><li>Reduced manual operations by 60%</li><li>Improved batch processing from 18 minutes to 4 minutes</li><li>Supported Related SBU, SBU Offboarding, Project Hornet and Warranty Claims</li></ul>
    </div>

    <div class="case-card">
      <div class="case-top"><span class="case-number">Case Study 02</span><div class="tags"><span class="tag">OCC</span><span class="tag">Spring MVC</span><span class="tag">CCv2</span></div></div>
      <h3>Headless B2B Portal APIs</h3>
      <p>Built and customized OCC web services and RESTful APIs in SAP Commerce Cloud to connect B2B portal functionality with external systems.</p>
      <ul class="impact-list"><li>Enabled smoother B2B portal functionality</li><li>Supported self-service access for 450+ users</li><li>Contributed to a 12-point increase in Customer Portal satisfaction</li></ul>
    </div>

    <div class="case-card">
      <div class="case-top"><span class="case-number">Case Study 03</span><div class="tags"><span class="tag">RBAC</span><span class="tag">PII Masking</span><span class="tag">Security</span></div></div>
      <h3>Enterprise Data Protection Controls</h3>
      <p>Architected data-protection controls for enterprise workflows, including role-based access, sensitive-data masking and row-level restrictions.</p>
      <ul class="impact-list"><li>Reduced audit findings by 70%</li><li>Aligned platform controls with SAP Commerce security practices</li><li>Improved handling of sensitive enterprise data</li></ul>
    </div>

    <div class="case-card">
      <div class="case-top"><span class="case-number">Case Study 04</span><div class="tags"><span class="tag">Performance</span><span class="tag">Production</span><span class="tag">Reliability</span></div></div>
      <h3>Customer Portal Performance & Reliability</h3>
      <p>Diagnosed critical P1/P2 incidents, improved backend performance and collaborated with Product, QA and DevOps to keep releases on track.</p>
      <ul class="impact-list"><li>Maintained 99.95% service availability</li><li>Improved p95 API latency by 28%</li><li>Achieved 1.8-hour MTTR for critical incidents</li></ul>
    </div>
  </div>
</section>

<div id="skills"></div>
<section class="section">
  <div class="section-heading">
    <div class="section-eyebrow">Technical stack</div>
    <h2>Skills mapped to enterprise commerce delivery.</h2>
    <p class="section-subtitle">The stack is grouped by how it is used in real work: commerce platform, backend engineering, data/security, and delivery tooling.</p>
  </div>
  <div class="skills-grid">
    <div class="skill-card"><div class="skill-title"><span class="skill-icon">☁️</span><h3>SAP Commerce Cloud</h3></div><div class="chips"><span class="chip">Hybris Core Architecture</span><span class="chip">CCv2</span><span class="chip">OCC / Headless</span><span class="chip">Backoffice Customization</span><span class="chip">WCMS</span><span class="chip">Impex</span><span class="chip">Cron Jobs</span><span class="chip">Solr</span><span class="chip">Hot Folder</span><span class="chip">Populators & Converters</span><span class="chip">Events</span><span class="chip">Interceptors</span><span class="chip">Restrictions</span><span class="chip">Cart & Checkout</span></div></div>
    <div class="skill-card"><div class="skill-title"><span class="skill-icon">⚙️</span><h3>Backend Engineering</h3></div><div class="chips"><span class="chip">Java</span><span class="chip">Spring MVC</span><span class="chip">Spring Hibernate</span><span class="chip">RESTful APIs</span><span class="chip">Microservices Architecture</span><span class="chip">System Design</span><span class="chip">Performance Optimization</span><span class="chip">Code Review</span></div></div>
    <div class="skill-card"><div class="skill-title"><span class="skill-icon">🔐</span><h3>Data & Security</h3></div><div class="chips"><span class="chip">SQL</span><span class="chip">MySQL</span><span class="chip">Oracle</span><span class="chip">DBMS / RDBMS</span><span class="chip">Data Modeling</span><span class="chip">RBAC</span><span class="chip">PII Masking</span><span class="chip">Row-level Security</span><span class="chip">JSON</span><span class="chip">XML</span></div></div>
    <div class="skill-card"><div class="skill-title"><span class="skill-icon">🛠️</span><h3>DevOps & Tools</h3></div><div class="chips"><span class="chip">Git</span><span class="chip">Jenkins</span><span class="chip">Azure DevOps</span><span class="chip">CI/CD Pipelines</span><span class="chip">Eclipse</span><span class="chip">IntelliJ IDEA</span><span class="chip">Agile Delivery</span><span class="chip">QA Collaboration</span></div></div>
  </div>
</section>

<div id="experience"></div>
<section class="section">
  <div class="section-heading">
    <div class="section-eyebrow">Work history</div>
    <h2>Where the work has been applied.</h2>
  </div>
  <div class="timeline-card">
    <div class="timeline-top">
      <div><h3>Associate Software Developer</h3><div class="company">Collins Aerospace · Bangalore, India</div></div>
      <div class="period">Feb 2023 — Present<br><span class="active-pill">Current role</span></div>
    </div>
    <ul class="impact-list">
      <li>Designed and implemented SAP Hybris B2B customizations, Backoffice workflows, Impex scripts, cron jobs, WCMS components and customer portal dashboards.</li>
      <li>Delivered 3+ high-impact automation initiatives that reduced user task time by 40% and enabled self-service data access for 450+ users.</li>
      <li>Collaborated with Product, QA and DevOps teams to deliver 4 releases per quarter with 95% on-time delivery.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-heading">
    <div class="section-eyebrow">Education</div>
    <h2>Academic background.</h2>
  </div>
  <div class="edu-grid">
    <div class="edu-card"><h3>PES University, Bangalore</h3><div class="edu-degree">Master of Computer Applications</div><div class="edu-meta">Dec 2021 — Jul 2023 · Relevant coursework: Machine Learning, Design & Analysis of Algorithms, Data Visualization, Java</div><span class="cgpa">CGPA 8.28 / 10</span></div>
    <div class="edu-card"><h3>Lalit Narayan Mishra Institute, Patna</h3><div class="edu-degree">Bachelor of Computer Applications</div><div class="edu-meta">Aug 2017 — Jul 2020 · Relevant coursework: Data Structures, DBMS, Web Development, Statistics</div><span class="cgpa">CGPA 7.9 / 10</span></div>
  </div>
</section>

<div id="contact"></div>
<div class="contact-wrap">
  <div class="contact-card">
    <div>
      <div class="section-eyebrow">Let's connect</div>
      <h2>Open to SAP Commerce, backend and B2B platform roles.</h2>
      <p>Based in Bangalore. Best fit: SAP Commerce Cloud, Hybris backend, OCC API development, enterprise portal engineering and platform automation roles.</p>
    </div>
    <div class="contact-links">
      <a class="contact-link" href="mailto:shalinipathak3@gmail.com">✉️ shalinipathak3@gmail.com</a>
      <a class="contact-link" href="tel:+916204275383">📱 +91 6204 275 383</a>
      <a class="contact-link" href="{resume_href}" download="Shalini_Pathak_Resume.pdf">📄 Download resume</a>
    </div>
  </div>
</div>

<div class="footer-line">
  <span>© 2026 Shalini Pathak · SAP Commerce Cloud Developer</span>
  <span>Built with Streamlit</span>
</div>
"""

def render_html(markup: str) -> None:
    # Streamlit's Markdown engine treats 4-space indented HTML as a code block.
    # Left-stripping each line prevents raw tags from appearing on the live site.
    cleaned = "\n".join(line.lstrip() for line in markup.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)

render_html(CSS)

if not RESUME_PATH.exists():
    st.warning("Resume PDF not found. Add it at assets/Shalini_Resume.pdf to enable the download buttons.")

render_html(HTML)
