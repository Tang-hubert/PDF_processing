import fitz
from PIL import Image

def compress_pdf(input_path, output_path, quality=95):
    # Open the PDF file
    pdf_document = fitz.open(input_path)

    # Create a PDF writer
    pdf_writer = fitz.open()

    # Iterate through each page in the input PDF
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Convert the page to an image
        image_list = page.get_pixmap()

        # Convert the image to a PIL Image
        pil_image = Image.frombytes("RGB", [image_list.width, image_list.height], image_list.samples)

        # Save the image with reduced quality
        pil_image.save("temp.jpg", "JPEG", quality=quality)

        # Open the compressed image and add it to the PDF writer
        compressed_page = pdf_writer.new_page(width=page.rect.width-5, height=page.rect.height-5)
        compressed_page.insert_image(page.rect, filename="temp.jpg")
        print(page.rect.width, page.rect.height)

    # Save the compressed PDF
    pdf_writer.save(output_path)

    # Close the PDF documents
    pdf_document.close()
    pdf_writer.close()


if __name__ == "__main__":
    input_pdf = r"C:\Users\luke1\Desktop\SUTD\VISA\20231120_terms_-_conditions_stp.pdf"
    output_pdf = r"C:\Users\luke1\Desktop\SUTD\VISA\20231120_terms_-_conditions_stp_.pdf"

    compress_pdf(input_pdf, output_pdf)
