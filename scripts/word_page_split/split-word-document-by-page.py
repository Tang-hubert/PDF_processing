# --- START OF FILE split_word_document_by_page.py ---
import aspose.words as aw
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WordDocumentSplitterByPage:
    """
    A class to split a Word document into separate documents,
    where each output document contains a specified number of pages.
    """
    def __init__(self, input_docx_path, output_dir):
        """
        Initializes the Word Document Splitter by Page.

        Args:
            input_docx_path (str): Path to the input Word document file.
            output_dir (str): Directory to save the output split documents.
        """
        self.input_docx_path = input_docx_path
        self.output_dir = output_dir
        self.output_docx_base_name = "split_by_page" # Base name for output Word documents
        os.makedirs(self.output_dir, exist_ok=True) # Ensure output directory exists

    def split_document(self, pages_per_split):
        """
        Splits the Word document into multiple documents, each containing a specified number of pages.

        Args:
            pages_per_split (int): The number of pages to include in each split document.
        """
        logging.info(f"Starting document splitting by page for: {self.input_docx_path}")
        try:
            # Load Word document
            doc = aw.Document(self.input_docx_path)
            logging.info(f"Document loaded successfully: {self.input_docx_path}")

            # Get total page count of the document
            page_count = doc.page_count
            logging.info(f"Total page count: {page_count}")

            # Loop through pages with a step of 'pages_per_split'
            for page_start in range(0, page_count, pages_per_split):
                # Calculate the end page for extraction
                page_end = min(page_start + pages_per_split, page_count)

                # Extract a range of pages
                extracted_page = doc.extract_pages(page_start, page_end)
                logging.info(f"Extracting pages from {page_start + 1} to {page_end}")

                # Define output file path for each split
                output_file_path = os.path.join(self.output_dir, f"{self.output_docx_base_name}_{page_end}.docx")

                # Save each extracted page range as a separate document
                extracted_page.save(output_file_path)
                logging.info(f"Pages {page_start + 1} to {page_end} saved to: {output_file_path}")

            logging.info(f"Document splitting by page completed for: {self.input_docx_path}")

        except FileNotFoundError:
            logging.error(f"Input Word document file not found: {self.input_docx_path}")
        except Exception as e:
            logging.error(f"An error occurred during document splitting by page: {e}")

def main():
    """
    Main function to execute Word document splitting by page.
    """
    input_docx_file = 'input.docx' # Anonymized input path
    output_directory = 'output_split_page' # Anonymized output directory
    pages_per_split = 3 # Split document every 3 pages

    splitter = WordDocumentSplitterByPage(input_docx_file, output_directory)
    splitter.split_document(pages_per_split)

if __name__ == "__main__":
    main()
# --- END OF FILE split_word_document_by_page.py ---