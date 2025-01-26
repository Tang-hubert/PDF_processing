# --- START OF FILE pdf_to_text_converter.py ---
from PyPDF2 import PdfReader
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFtoTextConverter:
    """
    A class to convert PDF documents to text files using PyPDF2 library.
    """
    def __init__(self, input_pdf_path, output_dir):
        """
        Initializes the PDF to Text Converter.

        Args:
            input_pdf_path (str): Path to the input PDF file.
            output_dir (str): Directory to save the output text file.
        """
        self.input_pdf_path = input_pdf_path
        self.output_dir = output_dir
        self.output_text_name = "pdf_to_text_output.txt" # Name for output text file

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def convert_to_text(self):
        """
        Extracts text from each page of the PDF document and saves it to a text file.
        """
        logging.info(f"Starting PDF to Text conversion for: {self.input_pdf_path}")
        try:
            # Open PDF document
            reader = PdfReader(self.input_pdf_path)
            logging.info(f"Document loaded successfully: {self.input_pdf_path}")

            # Define output text path
            output_text_path = os.path.join(self.output_dir, self.output_text_name)

            # Open output text file for writing
            with open(output_text_path, 'w', encoding='utf-8') as text_file:
                # Iterate through each page
                for page_number in range(len(reader.pages)):
                    page = reader.pages[page_number]
                    text = page.extract_text()
                    logging.info(f"Extracted text from page {page_number + 1}")
                    text_file.write(f"Page {page_number + 1}:\n")
                    text_file.write(text)
                    text_file.write("\n\n") # Add page separator

            logging.info(f"PDF converted to Text and saved to: {output_text_path}")

        except FileNotFoundError:
            logging.error(f"Input PDF file not found: {self.input_pdf_path}")
        except Exception as e:
            logging.error(f"An error occurred during PDF to Text conversion: {e}")

def main():
    """
    Main function to execute PDF to Text conversion.
    """
    input_pdf_file = 'input.pdf' # Anonymized input path
    output_directory = 'output_text' # Anonymized output directory

    converter = PDFtoTextConverter(input_pdf_file, output_directory)
    converter.convert_to_text()

if __name__ == "__main__":
    main()
# --- END OF FILE pdf_to_text_converter.py ---