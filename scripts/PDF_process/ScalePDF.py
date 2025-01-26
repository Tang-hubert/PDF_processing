# --- START OF FILE scale_pdf_converter.py ---
import PyPDF2
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFScaler:
    """
    A class to resize PDF documents to a new specified width and height using PyPDF2 library.
    """
    def __init__(self, input_pdf_path, output_dir):
        """
        Initializes the PDF Scaler.

        Args:
            input_pdf_path (str): Path to the input PDF file.
            output_dir (str): Directory to save the output resized PDF file.
        """
        self.input_pdf_path = input_pdf_path
        self.output_dir = output_dir
        self.output_pdf_name = "scaled_pdf_output.pdf" # Name for output PDF file
        self.new_width = 600 # Default new width
        self.new_height = 800 # Default new height
        os.makedirs(self.output_dir, exist_ok=True) # Ensure output directory exists

    def set_dimensions(self, width, height):
        """
        Sets the new dimensions for resizing PDF pages.

        Args:
            width (int): The desired width for PDF pages.
            height (int): The desired height for PDF pages.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        self.new_width = width
        self.new_height = height
        logging.info(f"New dimensions set: width={width}, height={height}")

    def resize_pdf(self):
        """
        Resizes each page of the input PDF to the new specified dimensions and saves it as a new PDF.
        """
        logging.info(f"Starting PDF resizing for: {self.input_pdf_path}")
        try:
            # Open the input PDF file in binary read mode
            with open(self.input_pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                pdf_writer = PyPDF2.PdfWriter()

                # Iterate through each page of the input PDF
                for page_num in range(len(pdf_reader.pages)): # Corrected page count access
                    page = pdf_reader.pages[page_num] # Corrected page access

                    # Create a new blank page with the desired width and height
                    new_page = PyPDF2.pdf.PageObject.create_blank_page(width=self.new_width, height=self.new_height)

                    # Merge the content of the original page onto the new page
                    new_page.merge_page(page) # Using merge_page for content merging
                    logging.info(f"Page {page_num + 1} content merged and resized.")

                    # Add the new page to the PDF writer
                    pdf_writer.add_page(new_page)

                # Define output file path
                output_file_path = os.path.join(self.output_dir, self.output_pdf_name)

                # Open the output PDF file in binary write mode and write the resized PDF
                with open(output_file_path, 'wb') as output_file:
                    pdf_writer.write(output_file)
                logging.info(f"Resized PDF saved to: {output_file_path}")

        except FileNotFoundError:
            logging.error(f"Input PDF file not found: {self.input_pdf_path}")
        except Exception as e:
            logging.error(f"An error occurred during PDF resizing: {e}")

def main():
    """
    Main function to execute PDF resizing.
    """
    input_pdf_file = 'input.pdf' # Anonymized input path
    output_directory = 'output_scaled_pdf' # Anonymized output directory
    new_width = 600 # Desired width
    new_height = 800 # Desired height

    scaler = PDFScaler(input_pdf_file, output_directory)
    scaler.set_dimensions(new_width, new_height)
    scaler.resize_pdf()

if __name__ == "__main__":
    main()
# --- END OF FILE scale_pdf_converter.py ---