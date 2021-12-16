from io import BytesIO
from datetime import date
from reportlab.lib.colors import blue
from reportlab.pdfgen.canvas import Canvas
from django.http import FileResponse


# Create the Bill PDF file.
def pdf_bill(emailto, guest_name, bill_amount):
    """Create the Bill PDF file to be sent to the guest email.
    """
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()
    # Create the PDF object, using the buffer as its "file."
    canvas = Canvas(buffer)
    # Set font to Times New Roman with 12-point size.
    canvas.setFont("Times-Roman", 12)
    # Draw blue text from 72 points from the left and 72 points from the bottom.
    canvas.setFillColor(blue)
    # text_pdf = f"Facture de {guest_name} pour un  montant total de {bill_amount} USD."
    text_pdf = "Facture de %s pour un montant total de %s USD." % (
        guest_name, bill_amount)
    print("UUUUUUUUUU ", text_pdf)
    canvas.drawString(72, 72, text_pdf)
    # Save the PDF file.
    canvas.showPage()
    canvas.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    file_name = "{}-{}.pdf".format(emailto, date.today())
    print("OOOOOOOOOOOOO OOOOOOO : ", file_name)
    return FileResponse(buffer, as_attachment=True, filename=file_name)
