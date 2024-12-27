# First, install the required PyPDF2 library
# pip install PyPDF2

from PyPDF2 import PdfReader, PdfWriter
import getpass


def protect_pdf(input_pdf, output_pdf):
    # Read the input PDF file
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Prompt the user to enter a password
    password = getpass.getpass("Enter the password to protect the PDF: ")

    # Encrypt the PDF with the password
    writer.encrypt(password)

    # Save the protected PDF to the output file
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    print(f"The PDF has been protected with a password and saved as {output_pdf}")


# Call the function to protect the PDF
protect_pdf("clcoding_dummy.pdf", "protected_clcoding_dummy.pdf")
