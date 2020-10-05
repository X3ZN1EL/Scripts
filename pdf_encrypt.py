#!/usr/bin/env python3
# @xeniel

from PyPDF2 import PdfFileWriter, PdfFileReader

def encryp_pdf(file,password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)

    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))

    parser.encrypt(password)

    with open(f"encrypted_{file}","wb") as f:
        parser.write(f)
        f.close()

    print(f"encrypted_{file} Created ...")

if __name__ == "__main__":
    file = "pdf_file_name.pdf"
    password = "password"
    encryp_pdf(file,password)