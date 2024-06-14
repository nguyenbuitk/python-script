from fpdf import FPDF
import os
import pandas as pd
from typing import Union

# longestCommonPrefix(self, v: List[str]) -> str:
def draw_lines(pdf: FPDF) -> None:
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

def set_footer(pdf, text):
    pdf.ln(277)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=text, align="R")

# Orientation: Portrait nghĩa là "định hướng: dọc". Khi nói về định dạng giấy trong các tài liệu PDF hoặc in ấn.
'''
  _______________
 |               |
 |               |
 |               |
 |               |
 |               |
 |               |
 |_______________|
'''
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# dataframe
df = pd.read_csv("data.csv")

for index, row in df.iterrows():
    ''' row <class 'pandas.core.series.Series'> =
    Order             6
    Topic    Match-case
    Pages             2
    Name: 5, dtype: object
    '''
    
    pdf.add_page()
    # Add a page for each topic
    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Draw horizontal lines
    draw_lines(pdf)

    # Set the footer
    set_footer(pdf, row["Topic"])

    # Add the additional pages if the topic span multiple pages
    for _ in range(row["Pages"] - 1):
        pdf.add_page()
        draw_lines(pdf)
        set_footer(pdf, row["Topic"])

pdf.output("output.pdf")