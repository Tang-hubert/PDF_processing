# --- START OF FILE jpg_to_pdf_converter.py ---
from PIL import Image
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class JPGtoPDFConverter:
    """
    A class to convert JPG images to PDF documents using PIL (Pillow) library.
    """
    def __init__(self, input_jpg_path, output_dir):
        """
        Initializes the JPG to PDF Converter.

        Args:
            input_jpg_path (str): Path to the input JPG file.
            output_dir (str): Directory to save the output PDF file.
        """
        self.input_jpg_path = input_jpg_path
        self.output_dir = output_dir
        self.output_pdf_name = "jpg_to_pdf_output.pdf" # Name for output PDF file

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def convert_to_pdf(self):
        """
        Converts the JPG image to a PDF document and saves it in the output directory.
        """
        logging.info(f"Starting JPG to PDF conversion for: {self.input_jpg_path}")
        try:
            # Open the JPG image
            image = Image.open(self.input_jpg_path)
            logging.info(f"Image loaded successfully: {self.input_jpg_path}")

            # Convert image to RGB (if necessary)
            image_rgb = image.convert('RGB')

            # Define output PDF path
            output_pdf_path = os.path.join(self.output_dir, self.output_pdf_name)

            # Save as PDF
            image_rgb.save(output_pdf_path)
            logging.info(f"JPG converted to PDF and saved to: {output_pdf_path}")

        except FileNotFoundError:
            logging.error(f"Input JPG file not found: {self.input_jpg_path}")
        except Exception as e:
            logging.error(f"An error occurred during JPG to PDF conversion: {e}")

def main():
    """
    Main function to execute JPG to PDF conversion.
    """
    input_jpg_file = 'input.jpg' # Anonymized input path
    output_directory = 'output_pdf' # Anonymized output directory

    converter = JPGtoPDFConverter(input_jpg_file, output_directory)
    converter.convert_to_pdf()

if __name__ == "__main__":
    main()
# --- END OF FILE jpg_to_pdf_converter.py ---