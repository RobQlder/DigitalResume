#!/usr/bin/env python3
"""Generate a clean, recruiter-friendly PDF resume (no phone number).

Run: python3 build_resume_pdf.py  ->  writes RobM_Resume.pdf
Kept in the repo so the downloadable PDF can be regenerated when content changes.
"""
from fpdf import FPDF

NAVY = (16, 42, 67)
GREY = (90, 90, 90)
RULE = (180, 180, 180)


class Resume(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

    def section(self, title):
        self.ln(2)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*NAVY)
        self.cell(0, 7, title.upper(), new_x="LMARGIN", new_y="NEXT")
        y = self.get_y()
        self.set_draw_color(*RULE)
        self.set_line_width(0.4)
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(2)

    def role(self, title, meta):
        self.ln(1)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "I", 9.5)
        self.set_text_color(*GREY)
        self.cell(0, 5, meta, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        x = self.get_x()
        self.cell(5, 5, chr(149))
        self.set_x(x + 5)
        self.multi_cell(self.w - self.r_margin - (x + 5), 5, text)
        self.ln(0.5)


pdf = Resume(format="A4")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(18, 15, 18)
pdf.add_page()

# Header
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(*NAVY)
pdf.cell(0, 11, "Rob McGuire", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 13)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 7, "IT Director & Technology Leader", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(*GREY)
pdf.cell(0, 6,
         "Brisbane, Queensland, Australia   |   "
         "linkedin.com/in/rob-mcguire-7759573a",
         new_x="LMARGIN", new_y="NEXT")
pdf.set_text_color(0, 0, 0)
pdf.ln(2)

# Profile
pdf.section("Profile")
pdf.set_font("Helvetica", "", 10)
pdf.multi_cell(0, 5,
    "Passionate IT professional with nearly 30 years' enterprise experience in strategic "
    "and operational roles. Genuinely interested in technology across domains including "
    "cloud infrastructure, cyber security, AI adoption, and application development. "
    "Focused on ensuring technology delivers business goals.")

# Core competencies (three columns, column-major to match the website)
pdf.section("Core Competencies")
columns = [
    ["IT Service Management & Delivery", "Vendor Management", "IT Procurement",
     "Agile & Prince2 Project Management", "Information Security & Cyber Security"],
    ["AI Adoption", "Solution Architecture", "Enterprise Architecture",
     "DevOps Principles", "Strategic Planning"],
    ["Risk Management", "Leadership", "Stakeholder Engagement", "Team Building & Development"],
]
pdf.set_font("Helvetica", "", 10)
usable = pdf.w - pdf.l_margin - pdf.r_margin
gap = 6
col_w = (usable - 2 * gap) / 3
bullet_w = 4
line_h = 5
item_gap = 1.5
start_y = pdf.get_y()
max_bottom = start_y
for c, items in enumerate(columns):
    x = pdf.l_margin + c * (col_w + gap)
    pdf.set_y(start_y)
    for item in items:
        y = pdf.get_y()
        pdf.set_xy(x, y)
        pdf.cell(bullet_w, line_h, chr(149))
        pdf.set_xy(x + bullet_w, y)
        # hanging indent: wrapped lines align under the text, not the bullet
        pdf.multi_cell(col_w - bullet_w, line_h, item, new_x="LMARGIN", new_y="NEXT")
        pdf.set_y(pdf.get_y() + item_gap)
    max_bottom = max(max_bottom, pdf.get_y())
pdf.set_y(max_bottom)
pdf.ln(1)

# Professional experience
pdf.section("Professional Experience")
roles = [
    ("Director ICT",
     "National Injury Insurance Scheme Queensland, Brisbane  |  Jun 2020 - Present",
     ["Corporate ICT, budgeting, vendor management, application development, and cyber security."]),
    ("Acting Director, Cyber Security",
     "QLD Dept of the Premier and Cabinet, Ministerial Services, Brisbane  |  Feb 2020 - Jun 2020",
     ["Developed a suite of information security policies in response to a recent audit finding.",
      "Identified opportunities to mature cyber security capabilities for Ministerial Services.",
      "Member of the QLD Government committee formed to establish the QLD Government Cyber Security Arrangements."]),
    ("Acting Director, Technology Solutions / Manager, Technology Services",
     "Queensland Treasury, Brisbane  |  May 2015 - Feb 2020",
     ["Managed 35 staff across Solution Architecture, IT Project Management, Information Management, "
      "Service Desk, Desktop Support, Desktop SoE, Application Packaging, Database Administration, "
      "Networking, Platform Support, Messaging, Cloud environments, and Cyber Security.",
      "Provided strategic IT advice to the CIO, executives, and business stakeholders.",
      "Transitioned infrastructure from internally operated Data Centres to a 3rd party Private Cloud.",
      "Established Public Cloud tenants for AWS and Microsoft Azure.",
      "Implemented an ISO 27001 aligned Information Security Management System (ISMS) and improved "
      "agency cyber security controls."]),
    ("Acting Executive Manager, Data Centre / Manager, Platform Support",
     "Public Safety Business Agency / Queensland Police Service, Brisbane  |  Jul 2012 - May 2015",
     ["Managed the Platform Support, Database Management, and Software Asset Management teams - 30 staff "
      "providing operational support to 3,000 virtual servers across three Data Centres.",
      "Provided operational and strategic advice to PSBA and partner agency executives on IT systems, "
      "services, and policy.",
      "Vendor management across Storage, Backup, Server, Virtualisation, and Operating System vendors.",
      "System owner for vCenter, Active Directory, Exchange, and corporate backup/restore.",
      "Administered the HP Server Support and Maintenance contract."]),
    ("Desktops QLD Team Leader",
     "Department of Education, Employment and Workplace Relations, Brisbane  |  May 2003 - Jun 2012",
     ["Managed a small team supporting approximately 500 staff across 10 Queensland sites.",
      "Project managed and implemented IT infrastructure for new sites, including cabling specification "
      "review and inspection, data room configuration, and IT equipment deployment."]),
    ("IT Security Technical Officer",
     "Department of Employment, Workplace Relations and Small Business, Canberra  |  2001 - May 2003",
     ["Website SSL certificate renewals and internal Certificate Authority.",
      "Designed and deployed a smart card logon solution to 2,400 staff across Australia."]),
]
for title, meta, bullets in roles:
    pdf.role(title, meta)
    for b in bullets:
        pdf.bullet(b)

# Certifications
pdf.section("Certifications")
certs = [
    "Microsoft Azure Fundamentals (2020)",
    "Certified Information Security Manager - ISACA CISM (2019)",
    "VMware VCA - Cloud, Data Centre, and Workforce Mobility certified (2013)",
    "Foundation Certificate in IT Service Management - ITIL v3 (2002)",
]
for c in certs:
    pdf.bullet(c)

# Professional development
pdf.section("Professional Development")
dev = [
    "Databricks Lakehouse Fundamentals (2023)",
    "Responsive Web Design (2022)",
    "Microsoft Power Apps & Power Automate (2021)",
    "ISACA CSX Penetration Testing Overview (2020)",
    "Plain English Writing for Government (2020)",
    "AWS Solution Architect (2019)",
    "Implementing an ISMS - ISO 27001 (2018)",
    "Fundamental Linux Administration (2017)",
    "Corporate Cybersecurity Management (2017)",
    "Chief Information Security Officer (2017)",
    "QLD Treasury Great Leaders Program, QUT (2016)",
    "Configuring & Managing MS Exchange Server 2010 (2014)",
    "Cisco Networking Technologies (2005)",
]
for d in dev:
    pdf.bullet(d)

pdf.output("RobM_Resume.pdf")
print("wrote RobM_Resume.pdf")
