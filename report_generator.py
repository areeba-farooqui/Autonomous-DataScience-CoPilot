from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import darkblue
from reportlab.lib.styles import ParagraphStyle
from datetime import datetime


def generate_report(summary, health_score, insights):

    filename = "AI_Dataset_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        textColor=darkblue,
        spaceAfter=20
    )

    story = []

    story.append(Paragraph("Autonomous Data Science Co-Pilot", title_style))
    story.append(Paragraph("<b>AI Dataset Analysis Report</b>", styles["Heading2"]))
    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Dataset Overview</b>", styles["Heading2"]))
    story.append(Paragraph(f"Rows: {summary['rows']}", styles["Normal"]))
    story.append(Paragraph(f"Columns: {summary['columns']}", styles["Normal"]))
    story.append(Paragraph(f"Health Score: {health_score}/100", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Insights</b>", styles["Heading2"]))

    for item in insights:
        story.append(Paragraph(f"• {item}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Values</b>", styles["Heading2"]))

    story.append(
        Paragraph(
            summary["missing"].to_string().replace("\n", "<br/>"),
            styles["Code"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Statistical Summary</b>", styles["Heading2"]))

    story.append(
        Paragraph(
            summary["statistics"].to_string().replace("\n", "<br/>"),
            styles["Code"]
        )
    )

    doc.build(story)

    return filename