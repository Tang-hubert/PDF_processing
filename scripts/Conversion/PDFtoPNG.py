# --- START OF FILE pdf_to_png_converter.py ---
import aspose.pdf as ap
import io
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFtoPNGConverter:
    """
    A class to convert PDF documents to PNG images using Aspose.PDF library.
    """
    def __init__(self, input_pdf_path, output_dir):
        """
        Initializes the PDF to PNG Converter.

        Args:
            input_pdf_path (str): Path to the input PDF file.
            output_dir (str): Directory to save the output PNG images.
        """
        self.input_pdf_path = input_pdf_path
        self.output_dir = output_dir
        self.output_pdf_name = "pdf_to_png_output" # Base name for output PNG files
        self.resolution_dpi = 300 # Default resolution

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def set_resolution(self, dpi):
        """
        Sets the resolution for PNG conversion.

        Args:
            dpi (int): Resolution in dots per inch.
        """
        if not isinstance(dpi, int) or dpi <= 0:
            raise ValueError("Resolution must be a positive integer.")
        self.resolution_dpi = dpi
        logging.info(f"Resolution set to {dpi} DPI.")

    def convert_to_png(self):
        """
        Converts each page of the PDF document to a PNG image and saves it in the output directory.
        """
        logging.info(f"Starting PDF to PNG conversion for: {self.input_pdf_path}")
        try:
            # Open PDF document
            document = ap.Document(self.input_pdf_path)
            logging.info(f"Document loaded successfully: {self.input_pdf_path}")

            # Create resolution object
            resolution = ap.devices.Resolution(self.resolution_dpi)
            png_device = ap.devices.PngDevice(resolution)

            for page_number in range(1, len(document.pages) + 1):
                output_file_path = os.path.join(
                    self.output_dir,
                    f"{self.output_pdf_name}_page_{page_number}_out.png"
                )

                logging.info(f"Processing page {page_number} and saving to: {output_file_path}")
                try:
                    # Create file stream to save image
                    with io.FileIO(output_file_path, 'wb') as image_stream: # Changed mode to 'wb' for binary write
                        # Convert specific page and save image to stream
                        png_device.process(document.pages[page_number], image_stream)
                    logging.info(f"Page {page_number} converted and saved successfully.")
                except Exception as e:
                    logging.error(f"Error processing page {page_number}: {e}")

            logging.info(f"PDF to PNG conversion completed for: {self.input_pdf_path}")

        except FileNotFoundError:
            logging.error(f"Input PDF file not found: {self.input_pdf_path}")
        except Exception as e:
            logging.error(f"An error occurred during PDF to PNG conversion: {e}")

def main():
    """
    Main function to execute PDF to PNG conversion.
    """
    input_pdf_file = 'input.pdf' # Anonymized input path
    output_directory = 'output_png' # Anonymized output directory

    converter = PDFtoPNGConverter(input_pdf_file, output_directory)
    converter.set_resolution(300) # You can adjust resolution here
    converter.convert_to_png()

if __name__ == "__main__":
    main()
# --- END OF FILE pdf_to_png_converter.py ---