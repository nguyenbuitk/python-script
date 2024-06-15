import glob
import pandas as pd
from fpdf import FPDF

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:    
    invoice_number, date = filepath.split("/")[1].strip(".xlsx").split("-")

    df = pd.read_excel(filepath)
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(40, 15, f"Invoice number {invoice_number}", border=0, ln=1)
    
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(40, 15, f"Date {date}", border=0, ln=1)
    
    # Add a header
    # Retrieve the column name
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    print(columns)
    
    pdf.set_font(family="Times", size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    
    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times")
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)
    
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)
    
    pdf.ln()
    pdf.output(f"PDFs/{invoice_number}.pdf")