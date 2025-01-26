# --- START OF FILE split_word_document_by_section.py ---
import aspose.words as aw
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WordDocumentSplitterBySection:
    """
    A class to split a Word document by sections.
    Each section will be saved as a separate Word document.
    """
    def __init__(self, input_docx_path, output_dir):
        """
        Initializes the Word Document Splitter by Section.

        Args:
            input_docx_path (str): Path to the input Word document file.
            output_dir (str): Directory to save the output split documents.
        """
        self.input_docx_path = input_docx_path
        self.output_dir = output_dir
        self.output_docx_base_name = "split_by_sections" # Base name for output Word documents
        os.makedirs(self.output_dir, exist_ok=True) # Ensure output directory exists

    def split_document(self):
        """
        Splits the Word document into separate documents based on sections.
        Each section is saved as a new Word document.
        """
        logging.info(f"Starting document splitting by sections for: {self.input_docx_path}")
        try:
            # Load Word document
            doc = aw.Document(self.input_docx_path)
            logging.info(f"Document loaded successfully: {self.input_docx_path}")

            # Loop through each section in the document
            for i in range(0, doc.sections.count):
                # Clone the section to split
                section = doc.sections[i].clone()

                # Create an instance of Document class for new document
                new_doc = aw.Document()

                # Clear the default sections in the new document
                new_doc.sections.clear()

                # Import the cloned section into the new document
                imported_section = new_doc.import_node(section, True).as_section()
                new_doc.sections.add(imported_section)

                # Define output file path for each section
                output_file_path = os.path.join(self.output_dir, f"{self.output_docx_base_name}_{i}.docx")

                # Save section as a separate document
                new_doc.save(output_file_path)
                logging.info(f"Section {i+1} saved to: {output_file_path}")

            logging.info(f"Document splitting by sections completed for: {self.input_docx_path}")

        except FileNotFoundError:
            logging.error(f"Input Word document file not found: {self.input_docx_path}")
        except Exception as e:
            logging.error(f"An error occurred during document splitting by sections: {e}")

def main():
    """
    Main function to execute Word document splitting by sections.
    """
    input_docx_file = 'input.docx' # Anonymized input path
    output_directory = 'output_split_sections' # Anonymized output directory

    splitter = WordDocumentSplitterBySection(input_docx_file, output_directory)
    splitter.split_document()

if __name__ == "__main__":
    main()
# --- END OF FILE split_word_document_by_section.py ---