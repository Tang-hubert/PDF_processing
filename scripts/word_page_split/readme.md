# Word Document Splitting Scripts

This directory contains Python scripts for splitting Word DOCX documents using Aspose.Words library:

*   **`split_word_document_by_page_range.py`**: Splits a Word document by extracting a specified range of pages into a new document.
*   **`split_word_document_by_section.py`**: Splits a Word document into multiple documents, with each section becoming a separate DOCX file.
*   **`split_word_document_by_page.py`**: Splits a Word document into multiple documents, where each output document contains a defined number of pages.

These scripts utilize the **Aspose.Words** library for Python. (Note: Aspose.Words might require a license for commercial use beyond evaluation.)

## Requirements

Before running these scripts, you need to install the Aspose.Words library for Python. You can do this using pip and the provided `requirements.txt` file (see below) or by installing it individually.

## Installation

1.  **Install Python**: Ensure you have Python installed on your system. Python 3.6 or later is recommended.
2.  **Install Aspose.Words for Python**: Navigate to this directory in your terminal and run:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Each script is designed to be run from the command line. You'll need to modify the `main()` function in each script to set the input file path, output directory, and any specific splitting parameters.

**Example Usage:**

1.  **Modify script parameters:** Open the script you want to use (e.g., `split_word_document_by_page_range.py`) in a text editor. Look for the `main()` function and adjust the `input_docx_file`, `output_directory`, and any relevant parameters for splitting.

    For example, in `split_word_document_by_page_range.py`:

    ```python
    def main():
        input_docx_file = 'path/to/your/input.docx' # Replace with your input DOCX path
        output_directory = 'path/to/your/output_split_range_directory' # Replace with your desired output directory

        splitter = WordDocumentSplitterByRange(input_docx_file, output_directory)
        splitter.split_document(3, 6) # Example: Extract pages from 3 to 6. Adjust page numbers as needed.
    ```

2.  **Run the script:** Open your terminal, navigate to the directory containing the script, and run the script using Python:

    ```bash
    python split_word_document_by_page_range.py
    ```

    Repeat this process for other scripts, adjusting the input and output paths and the splitting parameters in the `main()` function of each script according to your needs.

## Logging

All scripts are equipped with basic logging. Log messages will be printed to the console, providing information about the document splitting process and any errors encountered.

## Notes

*   **Aspose.Words Licensing**: Be aware of the licensing requirements for Aspose.Words, especially for commercial use. You may need to obtain a license from Aspose if you intend to use these scripts in a commercial setting.
*   **Error Handling**: The scripts include basic error handling and logging to help identify and resolve issues during document splitting.
*   **Path Anonymization**: The scripts use anonymized path variables in the `main()` functions (`input.docx`, `output_split_range`, etc.). Replace these with your actual file paths.

For any questions or issues, please refer to the documentation of Aspose.Words for Python.