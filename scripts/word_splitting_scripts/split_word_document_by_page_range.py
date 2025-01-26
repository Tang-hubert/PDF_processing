# --- START OF FILE split_word_document_by_page_range.py ---
import aspose.words as aw
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WordDocumentSplitterByRange:
    """
    A class to split a Word document by a specified page range.
    """
    def __init__(self, input_docx_path, output_dir):
        """
        Initializes the Word Document Splitter by Page Range.

        Args:
            input_docx_path (str): Path to the input Word document file.
            output_dir (str): Directory to save the output split documents.
        """
        self.input_docx_path = input_docx_path
        self.output_dir = output_dir
        self.output_docx_name = "split_by_page_range.docx" # Name for output Word document
        os.makedirs(self.output_dir, exist_ok=True) # Ensure output directory exists

    def split_document(self, start_page, end_page):
        """
        Extracts a range of pages from the Word document and saves them as a new document.

        Args:
            start_page (int): The starting page number (1-based index).
            end_page (int): The ending page number (1-based index).
        """
        logging.info(f"Starting document splitting by page range for: {self.input_docx_path}")
        try:
            # Load Word document
            doc = aw.Document(self.input_docx_path)
            logging.info(f"Document loaded successfully: {self.input_docx_path}")

            # Extract range of pages
            extracted_pages = doc.extract_pages(start_page, end_page)
            logging.info(f"Pages {start_page} to {end_page} extracted.")

            # Define output file path
            output_file_path = os.path.join(self.output_dir, self.output_docx_name)

            # Save pages as a separate document
            extracted_pages.save(output_file_path)
            logging.info(f"Extracted pages saved to: {output_file_path}")

        except FileNotFoundError:
            logging.error(f"Input Word document file not found: {self.input_docx_path}")
        except Exception as e:
            logging.error(f"An error occurred during document splitting: {e}")

def main():
    """
    Main function to execute Word document splitting by page range.
    """
    input_docx_file = 'input.docx' # Anonymized input path
    output_directory = 'output_split_range' # Anonymized output directory

    splitter = WordDocumentSplitterByRange(input_docx_file, output_directory)
    splitter.split_document(3, 6) # Example: Extract pages from 3 to 6

if __name__ == "__main__":
    main()
# --- END OF FILE split_word_document_by_page_range.py ---