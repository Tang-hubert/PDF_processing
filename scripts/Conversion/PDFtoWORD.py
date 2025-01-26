# --- START OF FILE pdf_to_word_converter.py ---
from pdf2docx import Converter
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFtoWORDConverter:
    """
    A class to convert PDF documents to WORD documents using pdf2docx library.
    """
    def __init__(self, input_pdf_path, output_dir):
        """
        Initializes the PDF to WORD Converter.

        Args:
            input_pdf_path (str): Path to the input PDF file.
            output_dir (str): Directory to save the output WORD file.
        """
        self.input_pdf_path = input_pdf_path
        self.output_dir = output_dir
        self.output_docx_name = "pdf_to_word_output.docx" # Name for output WORD file

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def convert_to_word(self):
        """
        Converts the PDF document to a WORD document and saves it in the output directory.
        """
        logging.info(f"Starting PDF to WORD conversion for: {self.input_pdf_path}")
        try:
            # Define output WORD path
            output_docx_path = os.path.join(self.output_dir, self.output_docx_name)

            # Using the built-in function, convert the PDF file to a document file by saving it in a variable.
            cv = Converter(self.input_pdf_path)
            logging.info(f"Converter initialized for: {self.input_pdf_path}")

            # Store the Document in the variable's initialized path
            cv.convert(output_docx_path)
            logging.info(f"PDF converted to WORD and saved to: {output_docx_path}")

            # Conversion closure through the function close()
            cv.close()
            logging.info("Converter closed.")

        except FileNotFoundError:
            logging.error(f"Input PDF file not found: {self.input_pdf_path}")
        except Exception as e:
            logging.error(f"An error occurred during PDF to WORD conversion: {e}")

def main():
    """
    Main function to execute PDF to WORD conversion.
    """
    input_pdf_file = 'input.pdf' # Anonymized input path
    output_directory = 'output_word' # Anonymized output directory

    converter = PDFtoWORDConverter(input_pdf_file, output_directory)
    converter.convert_to_word()

if __name__ == "__main__":
    main()
# --- END OF FILE pdf_to_word_converter.py ---