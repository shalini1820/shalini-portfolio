"""
generate_resume.py
Generates Shalini's resume as PDF bytes using ReportLab.
Called by streamlit_app.py at startup — no file is written to disk.
"""

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ── Styles ──────────────────────────────────────────────────────────────────

_styles = getSampleStyleSheet()

_styles.add(ParagraphStyle(
    name="Name",
    parent=_styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=24, leading=28,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#172033"),
    spaceAfter=4,
))
_styles.add(ParagraphStyle(
    name="Contact",
    parent=_styles["BodyText"],
    fontName="Helvetica",
    fontSize=8.8, leading=11,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#3f495c"),
    spaceAfter=8,
))
_styles.add(ParagraphStyle(
    name="Section",
    parent=_styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=10.5, leading=13,
    textColor=colors.HexColor("#0f766e"),
    spaceBefore=8, spaceAfter=4,
))
_styles.add(ParagraphStyle(
    name="Body",
    parent=_styles["BodyText"],
    fontName="Helvetica",
    fontSize=8.7, leading=11,
    textColor=colors.HexColor("#172033"),
    alignment=TA_LEFT,
    spaceAfter=3,
))
_styles.add(ParagraphStyle(
    name="Small",
    parent=_styles["BodyText"],
    fontName="Helvetica",
    fontSize=8.1, leading=10,
    textColor=colors.HexColor("#465168"),
))
_styles.add(ParagraphStyle(
    name="Role",
    parent=_styles["BodyText"],
    fontName="Helvetica-Bold",
    fontSize=9.3, leading=11.5,
    textColor=colors.HexColor("#172033"),
    spaceAfter=0,
))


# ── Helpers ──────────────────────────────────────────────────────────────────

def _p(text, style="Body"):
    return Paragraph(text, _styles[style])


def _bullets(items):
    return ListFlowable(
        [ListItem(_p(item), leftIndent=7, bulletFontSize=5) for item in items],
        bulletType="bullet",
        leftIndent=10,
        bulletFontName="Helvetica",
        bulletFontSize=5,
        bulletOffsetY=1,
        spaceAfter=1,
    )


def _section(title):
    return [
        Spacer(1, 3),
        _p(title, "Section"),
        Table(
            [[""]],
            colWidths=[180 * mm],
            style=TableStyle([
                ("LINEABOVE", (0, 0), (-1, -1), 0.6, colors.HexColor("#d9e1ee"))
            ]),
        ),
        Spacer(1, 2),
    ]


# ── Story ────────────────────────────────────────────────────────────────────

def _build_story():
    s = []

    # Header
    s.append(_p("SHALINI", "Name"))
    s.append(_p(
        "Bangalore, Karnataka, India &nbsp;|&nbsp; shalinipathak3@gmail.com "
        "&nbsp;|&nbsp; +91-6204275383",
        "Contact",
    ))

    # Profile
    s.extend(_section("PROFILE"))
    s.append(_p(
        "SAP Hybris / SAP Commerce Cloud Backend Developer with 3+ years of hands-on experience "
        "delivering B2B enterprise solutions. Proven expertise in Hybris core architecture, OCC web "
        "services, cron jobs, Impex scripting, RESTful API integration, and SAP Commerce Cloud (CCv2). "
        "Experienced in performance optimization, RBAC, PII masking, data security, Spring MVC, Java, "
        "Git, Jenkins, and Agile delivery."
    ))

    # Experience
    s.extend(_section("WORK EXPERIENCE"))
    s.append(_p("Associate Software Developer — Collins Aerospace, Bangalore, India", "Role"))
    s.append(_p("Feb 2023 – Present", "Small"))
    s.append(_bullets([
        "Designed and implemented SAP Hybris B2B customizations including Backoffice customizations, "
        "Impex-based data migration scripts, and cron jobs, reducing manual operations by 60% and "
        "improving batch processing from 18 minutes to 4 minutes.",
        "Built and customized OCC/headless web services and RESTful APIs using Spring MVC within SAP "
        "Commerce Cloud (CCv2), integrating with external systems for B2B portal functionality.",
        "Architected enterprise data-protection controls including RBAC, PII masking, and row-level "
        "security, reducing audit findings by 70%.",
        "Delivered automation initiatives (Related SBU, SBU Offboarding, Project Hornet, Warranty Claims), "
        "reducing user task time by 40% and enabling self-service data access for 450+ users.",
        "Developed WCMS page components, navigations, and Customer Portal dashboards.",
        "Resolved critical P1/P2 production incidents with 1.8-hour MTTR; improved p95 API latency "
        "by 28% while maintaining 99.95% service availability.",
        "Collaborated with Product, QA, and DevOps to deliver 4 releases per quarter with 95% on-time delivery.",
    ]))

    # Projects
    s.extend(_section("PROJECTS"))
    s.append(_p("B2B SAP Commerce Automation Suite | SAP Commerce Cloud, Cron Jobs, Impex", "Role"))
    s.append(_bullets([
        "Automated enterprise commerce workflows through Hybris customizations, Backoffice updates, "
        "data migration scripts, and scheduled jobs.",
        "Improved operational efficiency by reducing manual work and cutting batch runtime by 78%.",
    ]))
    s.append(Spacer(1, 4))
    s.append(_p("OCC / Headless B2B Portal APIs | OCC, Spring MVC, REST APIs, CCv2", "Role"))
    s.append(_bullets([
        "Built API services for B2B portal features and external system integration, improving "
        "portal usability for 450+ users.",
        "Delivered reusable backend services for customer portal workflows and self-service data access.",
    ]))
    s.append(Spacer(1, 4))
    s.append(_p("Enterprise Data Security Controls | RBAC, PII Masking, Row-level Security", "Role"))
    s.append(_bullets([
        "Implemented data-protection controls aligned with SAP Commerce security practices.",
        "Reduced audit findings by 70% and improved security posture for enterprise customer data.",
    ]))

    s.append(PageBreak())

    # Skills
    s.extend(_section("TECHNICAL SKILLS"))
    skill_rows = [
        ("SAP Commerce Cloud",
         "Hybris Core Architecture, CCv2, OCC/Headless, Backoffice Customization, WCMS, Impex, "
         "Cron Jobs, Solr, Hot Folder, Populators & Converters, Events, Interceptors, Cart & Checkout"),
        ("Languages & Frameworks",
         "Java, Spring MVC, Spring Hibernate, JavaScript, Python, SQL, HTML, CSS, XML, JSON"),
        ("DevOps & Tools",
         "Git, Jenkins, Azure DevOps, Eclipse, IntelliJ IDEA, CI/CD Pipelines, Agile Delivery"),
        ("Databases",        "MySQL, Oracle, DBMS / RDBMS"),
        ("Core Competencies",
         "System Design, Microservices Architecture, Performance Optimization, RBAC, PII Masking, "
         "Data Modeling, End-to-End Hybris Implementation"),
    ]
    tbl = Table(
        [[_p(f"<b>{lbl}</b>"), _p(val)] for lbl, val in skill_rows],
        colWidths=[43 * mm, 137 * mm],
        hAlign="LEFT",
    )
    tbl.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
    ]))
    s.append(tbl)

    # Education
    s.extend(_section("EDUCATION"))
    s.append(_p("PES University, Bangalore", "Role"))
    s.append(_p("Master of Computer Applications | CGPA: 8.28/10 | Dec 2021 – Jul 2023", "Small"))
    s.append(_p("Relevant coursework: Machine Learning, Design and Analysis of Algorithms, Data Visualization, Java"))
    s.append(Spacer(1, 4))
    s.append(_p("Lalit Narayan Mishra Institute of Economic Development and Social Change, Patna", "Role"))
    s.append(_p("Bachelor of Computer Applications | CGPA: 7.9/10 | Aug 2017 – Jul 2020", "Small"))
    s.append(_p("Relevant coursework: Data Structures, Database Management Systems, Web Development, Statistics"))

    # Leadership
    s.extend(_section("LEADERSHIP & ACTIVITIES"))
    s.append(_p("Volunteer — Care Needy Foundation, Delhi | Feb 2021 – Mar 2021", "Role"))
    s.append(_bullets([
        "Led a 3-week computer literacy program training 30 children, achieving 25% average "
        "proficiency increase across Microsoft Office tools and Windows operations."
    ]))

    return s


# ── Public API ────────────────────────────────────────────────────────────────

def build_pdf_bytes() -> bytes:
    """Return the resume as PDF bytes (no file is written to disk)."""
    buf = BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=13 * mm,
        bottomMargin=13 * mm,
        title="Shalini — Resume",
        author="Shalini",
    )
    doc.build(_build_story())
    return buf.getvalue()
