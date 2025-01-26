# --- START OF FILE compress_pdf_converter.py ---
import fitz  # PyMuPDF
from PIL import Image
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFCompressor:
    """
    A class to compress PDF documents by reducing image quality using PyMuPDF (fitz) and PIL libraries.
    """
    def __init__(self, input_pdf_path, output_dir):
        """
        Initializes the PDF Compressor.

        Args:
            input_pdf_path (str): Path to the input PDF file.
            output_dir (str): Directory to save the output compressed PDF file.
        """
        self.input_pdf_path = input_pdf_path
        self.output_dir = output_dir
        self.output_pdf_name = "compressed_pdf_output.pdf" # Name for output compressed PDF
        self.jpeg_quality = 95 # Default JPEG quality (higher is better, lower compression)
        os.makedirs(self.output_dir, exist_ok=True) # Ensure output directory exists

    def set_jpeg_quality(self, quality):
        """
        Sets the JPEG quality for image compression.

        Args:
            quality (int): JPEG quality level (0-100, higher is better quality, lower compression).
        """
        if not isinstance(quality, int) or not 0 <= quality <= 100:
            raise ValueError("JPEG quality must be an integer between 0 and 100.")
        self.jpeg_quality = quality
        logging.info(f"JPEG quality set to {quality}")

    def compress_pdf(self):
        """
        Compresses the input PDF by converting pages to images, compressing them, and then recreating the PDF.
        Saves the compressed PDF to the output directory.
        """
        input_path = self.input_pdf_path # for easy reference
        output_path = os.path.join(self.output_dir, self.output_pdf_name) # for easy reference
        quality = self.jpeg_quality # for easy reference

        logging.info(f"Starting PDF compression for: {input_path} with quality={quality}")
        try:
            # Open the PDF file using PyMuPDF
            pdf_document = fitz.open(input_path)
            logging.info(f"Document loaded successfully: {input_path}")

            # Create a new PDF writer
            pdf_writer = fitz.open()

            # Iterate through each page in the input PDF
            for page_number in range(pdf_document.page_count):
                # Get the page
                page = pdf_document[page_number]

                # Convert the page to a Pixmap image
                pixmap = page.get_pixmap()

                # Convert the Pixmap to a PIL Image
                pil_image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

                # Save the image as JPEG with specified quality (in memory)
                temp_image_path = "temp.jpg" # Temporary file to save compressed image
                pil_image.save(temp_image_path, "JPEG", quality=quality)
                logging.debug(f"Page {page_number + 1} converted to JPEG and saved temporarily.")

                # Create a new page in the output PDF with slightly reduced dimensions
                compressed_page = pdf_writer.new_page(width=page.rect.width, height=page.rect.height) # Keep original dimensions
                compressed_page.insert_image(page.rect, filename=temp_image_path) # Insert compressed image
                logging.debug(f"Compressed image inserted into new page {page_number + 1}.")

            # Save the compressed PDF to the specified output path
            pdf_writer.save(output_path)
            logging.info(f"Compressed PDF saved to: {output_path}")

            # Close the PDF documents and remove temporary image file
            pdf_document.close()
            pdf_writer.close()
            os.remove(temp_image_path) # Clean up temporary JPEG file
            logging.debug("Temporary image file removed.")

        except FileNotFoundError:
            logging.error(f"Input PDF file not found: {input_path}")
        except Exception as e:
            logging.error(f"An error occurred during PDF compression: {e}")

def main():
    """
    Main function to execute PDF compression.
    """
    input_pdf_file = 'input.pdf' # Anonymized input path
    output_directory = 'output_compressed_pdf' # Anonymized output directory
    jpeg_quality = 80 # Example JPEG quality setting (adjust as needed)

    compressor = PDFCompressor(input_pdf_file, output_directory)
    compressor.set_jpeg_quality(jpeg_quality)
    compressor.compress_pdf()

if __name__ "__main__":
    main()
# --- END OF FILE compress_pdf_converter.py ---