from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_receipt(customer_name, receipt_number, items, total_amount):
    # Set up the PDF file and canvas
    file_name = f"Receipt_{receipt_number}.pdf"
    pdf = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Title of the receipt
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, height - 50, "Transaction Receipt")
    
    # Add customer and receipt details
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 100, f"Customer Name: {customer_name}")
    pdf.drawString(50, height - 120, f"Receipt Number: {receipt_number}")
    
    # Add items table
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, height - 160, "Item")
    pdf.drawString(300, height - 160, "Quantity")
    pdf.drawString(400, height - 160, "Price")
    
    # List the items
    pdf.setFont("Helvetica", 12)
    y_position = height - 180
    for item, (quantity, price) in items.items():
        pdf.drawString(50, y_position, item)
        pdf.drawString(300, y_position, str(quantity))
        pdf.drawString(400, y_position, f"${price:.2f}")
        y_position -= 20

    # Add the total amount
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y_position - 20, f"Total Amount: ${total_amount:.2f}")

    # Footer
    pdf.setFont("Helvetica", 10)
    pdf.setFillColor(colors.gray)
    pdf.drawString(50, 50, "Thank you for shopping with us!")

    
    pdf.save()

    print(f"Receipt saved as {file_name}")

customer_name = "John Doe"
receipt_number = 12345
items = {
    "Laptop": (1, 1200.00),
    "Mouse": (2, 25.00),
    "Keyboard": (1, 45.00)
}
total_amount = 1295.00

create_receipt(customer_name, receipt_number, items, total_amount)
