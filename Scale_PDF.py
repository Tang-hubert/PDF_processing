import PyPDF2

def resize_pdf(input_path, output_path, new_width, new_height):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            
            # Create a new page with the desired width and height
            new_page = PyPDF2.pdf.PageObject.createBlankPage(width=new_width, height=new_height)
            
            # Merge the content of the original page onto the new page
            new_page.mergeTranslatedPage(page, 0, 0)
            
            # Add the new page to the writer
            pdf_writer.addPage(new_page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


if __name__ == "__main__":
    input_pdf = r"C:\Users\luke1\Desktop\SUTD\VISA\20231120_terms_-_conditions_stp.pdf"
    output_pdf = r"C:\Users\luke1\Desktop\SUTD\VISA\20231120_terms_-_conditions_stp_.pdf"
    new_width = 600  # Set your desired width
    new_height = 800  # Set your desired height

    resize_pdf(input_pdf, output_pdf, new_width, new_height)
