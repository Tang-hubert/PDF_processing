# --- START OF FILE separate_pdf_pages_converter.py ---
from PyPDF2 import PdfWriter, PdfReader
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFPageSeparator:
    """
    A class to separate each page of a PDF document into individual PDF files using PyPDF2 library.
    """
    def __init__(self, input_pdf_path, output_dir):
        """
        Initializes the PDF Page Separator.

        Args:
            input_pdf_path (str): Path to the input PDF file.
            output_dir (str): Directory to save the output individual PDF pages.
        """
        self.input_pdf_path = input_pdf_path
        self.output_dir = output_dir
        self.output_pdf_base_name = "document-page" # Base name for output PDF page files
        os.makedirs(self.output_dir, exist_ok=True) # Ensure output directory exists

    def separate_pages(self):
        """
        Separates each page of the input PDF into a new PDF file and saves them in the output directory.
        """
        logging.info(f"Starting PDF page separation for: {self.input_pdf_path}")
        try:
            # Open the input PDF file in binary read mode
            inputpdf = PdfReader(open(self.input_pdf_path, "rb"))
            logging.info(f"Document loaded successfully: {self.input_pdf_path}")

            # Iterate through each page of the input PDF
            for i in range(len(inputpdf.pages)):
                output = PdfWriter()
                output.add_page(inputpdf.pages[i])

                # Define output file path for each page
                output_file_path = os.path.join(self.output_dir, f"{self.output_pdf_base_name}{i+1}.pdf")

                # Open the output file in binary write mode and write the page to it
                with open(output_file_path, "wb") as output_stream:
                    output.write(output_stream)
                logging.info(f"Page {i+1} saved to: {output_file_path}")

            logging.info(f"PDF page separation completed for: {self.input_pdf_path}")

        except FileNotFoundError:
            logging.error(f"Input PDF file not found: {self.input_pdf_path}")
        except Exception as e:
            logging.error(f"An error occurred during PDF page separation: {e}")

def main():
    """
    Main function to execute PDF page separation.
    """
    input_pdf_file = 'input.pdf' # Anonymized input path
    output_directory = 'output_pdf_pages' # Anonymized output directory

    separator = PDFPageSeparator(input_pdf_file, output_directory)
    separator.separate_pages()

if __name__ == "__main__":
    main()
# --- END OF FILE separate_pdf_pages_converter.py ---