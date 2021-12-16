from django.core import mail
from .pdf_generator import pdf_bill


# Send email
def send_email(emailto, guest_name, bill_amount):
    """Function to send the bill by email to the guest.
    Args:
        emailto (str): [description]
        guest_name (str): guest's first name and last name
        bill_amount (str): total amount of the bill, formated with 2 decimal digits.
    """
    body_message = f"Salut Léa et William,\n\nVoici la facture du passager.ère {guest_name} \
        pour un  montant total de {bill_amount} USD.\n\n\n"
    connection = mail.get_connection()
    connection.open()
    email = mail.EmailMessage(
        subject="test",
        body=body_message,
        from_email="jfsubrini@zoho.com",
        to=[emailto],
        # to=[emailto[0]],
        # cc=[emailto[1]],
        connection=connection,
    )
    # Generate the PDF file.
    # pdf_file = pdf_bill(emailto, guest_name, bill_amount)
    # Save the PDF file in the Datastore.
    # print("KKKKKK : ", pdf_file, type(pdf_file))  # TODO
    # Attach the PDF to the email and send the email.
    # email.attach_file(f'billing/{pdf_file}')
    email.attach_file(f'billing/test_bill.pdf')
    email.send()
