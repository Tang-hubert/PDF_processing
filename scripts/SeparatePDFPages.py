from PyPDF2 import PdfWriter, PdfReader

inputpdf = PdfReader(open(r"C:\Users\luke1\Desktop\1121獎學金\身份文件.pdf", "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)