import aspose.words as aw

# load Word document
doc = aw.Document(r"C:\Users\Hubert Tang\Desktop\testing.docx")

# get page count
pageCount = doc.page_count

# loop through pages
for page in range(0, pageCount, 3):
  
    # save each page as a separate document
    extractedPage = doc.extract_pages(page, 3)
    extractedPage.save(f"split_by_page_{page + 3}.docx")