from PyPDF2 import PdfReader

reader = PdfReader(r"C:\Users\luke1\Desktop\CGU\Senior\DataMining\資料探勘考古\107.pdf")
number_of_pages = len(reader.pages)
page1 = reader.pages[0]
text1 = page1.extract_text()
page2 = reader.pages[1]
text2 = page2.extract_text()
print(text1)
print()
print(text2)