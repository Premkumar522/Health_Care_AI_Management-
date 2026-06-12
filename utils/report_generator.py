import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_patient_csv(df, filename):
    df.to_csv(filename, index=False)


def generate_patient_excel(df, filename):
    df.to_excel(filename, index=False)


def generate_patient_pdf(df, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Patient Report",
        styles["Title"]
    )

    elements.append(title)
    elements.append(Spacer(1, 12))

    data = [list(df.columns)]

    for row in df.values.tolist():
        data.append(row)

    table = Table(data)

    table.setStyle(
        TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('GRID',(0,0),(-1,-1),1,colors.black),
            ('BACKGROUND',(0,1),(-1,-1),colors.beige)
        ])
    )

    elements.append(table)

    doc.build(elements)