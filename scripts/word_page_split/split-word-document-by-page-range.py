import aspose.words as aw

# load Word document
doc = aw.Document(r"C:\Users\Hubert Tang\Desktop\testing.docx")

# extract range of pages
extractedPages = doc.extract_pages(3, 6)

# save pages as a separate document
extractedPages.save("split_by_page_range.docx")