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

    print(f"[+]Encriptando {file} \n[+]Done!")

if __name__ == "__main__":
    file = "please_dont_share.pdf"
    password = "$3cureP4$$w0rD"
    encryp_pdf(file,password)
