# Document Conversion and Processing Scripts

This repository contains Python scripts for various document conversion and processing tasks. It is organized into three main sections:

*   **Conversion Scripts**:  Scripts for converting between different document formats (PDF to PNG, JPG to PDF, PDF to Text, PDF to Word).
*   **Word Document Splitting Scripts**: Scripts for splitting Word DOCX documents in different ways (by page range, by section, by page count).
*   **PDF Processing Scripts**: Scripts for manipulating PDF documents (scaling pages, separating pages, compressing PDFs).

## Sections and Scripts Overview

### 1. Conversion Scripts

This section contains scripts for converting between different document formats:

*   **`pdf_to_png_converter.py`**: Converts PDF documents to PNG images, with each page becoming a separate PNG file.
*   **`jpg_to_pdf_converter.py`**: Converts JPG images to PDF documents.
*   **`pdf_to_text_converter.py`**: Extracts text from PDF documents and saves it to a TXT file.
*   **`pdf_to_word_converter.py`**: Converts PDF documents to Word DOCX files.

### 2. Word Document Splitting Scripts

This section includes scripts for splitting Word DOCX documents using Aspose.Words:

*   **`split_word_document_by_page_range.py`**: Splits a Word document by extracting a specified range of pages into a new document.
*   **`split_word_document_by_section.py`**: Splits a Word document into multiple documents, with each section becoming a separate DOCX file.
*   **`split_word_document_by_page.py`**: Splits a Word document into multiple documents, where each output document contains a defined number of pages.

### 3. PDF Processing Scripts

This section provides scripts for various PDF manipulation tasks:

*   **`scale_pdf_converter.py`**: Resizes PDF documents to a new specified width and height, scaling page content.
*   **`separate_pdf_pages_converter.py`**: Separates each page of a PDF document into individual PDF files.
*   **`compress_pdf_converter.py`**: Compresses PDF documents by reducing the quality of images within, aiming for smaller file sizes.

## Requirements

The scripts in this repository rely on several Python libraries. Before running any script, ensure you have installed the necessary libraries. You can install all required libraries using pip and the provided `requirements.txt` file.

**Required Python Libraries:**

*   **aspose-pdf**: For PDF to PNG conversion. (Aspose might require a license for commercial use.)
*   **aspose-words**: For Word document splitting. (Aspose might require a license for commercial use.)
*   **Pillow (PIL)**: For JPG to PDF conversion and image manipulation in PDF compression.
*   **PyPDF2**: For PDF to Text conversion, PDF scaling, and PDF page separation.
*   **pdf2docx**: For PDF to Word conversion.
*   **PyMuPDF (fitz)**: For PDF compression.

## Installation

1.  **Install Python**: Ensure you have Python installed on your system (Python 3.6 or later recommended).
2.  **Install Required Libraries**: Navigate to the root directory of this repository in your terminal and run:

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all the necessary Python packages listed in the `requirements.txt` file.

## Usage

Each script is designed to be run from the command line. To use a script:

1.  **Navigate to the script's directory**: Open your terminal and navigate to the directory containing the specific script you want to run (e.g., `conversion`, `word_page_split`, or `PDF process`).

2.  **Modify Script Parameters (if needed)**: Open the script (e.g., `pdf_to_png_converter.py`) in a text editor. Look for the `main()` function.  You will need to adjust the input file paths, output directories, and any script-specific parameters (like page ranges, resolution, JPEG quality) within the `main()` function to match your needs.

    **Example: Modifying `pdf_to_png_converter.py`:**

    ```python
    def main():
        input_pdf_file = 'path/to/your/input.pdf'  # 📝 Replace with your input PDF file path
        output_directory = 'path/to/your/output_png_directory' # 📝 Replace with your desired output directory

        converter = PDFtoPNGConverter(input_pdf_file, output_directory)
        converter.set_resolution(300) # ⚙️ Optional: Adjust resolution if needed
        converter.convert_to_png()
    ```

    **Example: Modifying `split_word_document_by_page_range.py`:**

    ```python
    def main():
        input_docx_file = 'path/to/your/input.docx' # 📝 Replace with your input DOCX file path
        output_directory = 'path/to/your/output_split_range_directory' # 📝 Replace with your output directory

        splitter = WordDocumentSplitterByRange(input_docx_file, output_directory)
        splitter.split_document(3, 6) # ⚙️ Example: Extract pages 3 to 6. Adjust page numbers as needed.
    ```

    **Example: Modifying `compress_pdf_converter.py`:**

    ```python
    def main():
        input_pdf_file = 'path/to/your/input.pdf' # 📝 Replace with your input PDF file path
        output_directory = 'path/to/your/output_compressed_pdf_directory' # 📝 Replace with your output directory
        jpeg_quality = 80 # ⚙️ Example JPEG quality: 80 (adjust for desired compression/quality)

        compressor = PDFCompressor(input_pdf_file, output_directory)
        compressor.set_jpeg_quality(jpeg_quality) # Set JPEG quality
        compressor.compress_pdf()
    ```

3.  **Run the script**: In your terminal, from within the script's directory, execute the script using Python:

    ```bash
    python pdf_to_png_converter.py  # Example for PDF to PNG conversion
    python split_word_document_by_page_range.py # Example for Word splitting
    python compress_pdf_converter.py # Example for PDF compression
    ```

    Replace the script name with the one you intend to use.

## Logging

All scripts are configured with basic logging. Informational messages and errors will be logged to the console during script execution, providing feedback on the process and helping to diagnose any issues.

## Notes

*   **Aspose Licensing**: Scripts using `aspose-pdf` and `aspose-words` libraries (specifically `pdf_to_png_converter.py` and the Word splitting scripts) may require licenses for commercial use. Please review Aspose's licensing terms if you plan to use these scripts commercially.
*   **PyMuPDF Dependency**: The `compress_pdf_converter.py` script relies on `PyMuPDF`, which has native library dependencies. Ensure PyMuPDF is installed correctly for your operating system.
*   **JPEG Compression Quality**: When using `compress_pdf_converter.py`, adjust the `jpeg_quality` parameter to balance between output file size and image quality degradation. Lower quality values will result in smaller files but potentially lower image fidelity.
*   **Error Handling**: Basic error handling is included in all scripts to catch common issues like file not found errors and exceptions during processing. Check the console output for error messages if a script fails to run as expected.
*   **Path Anonymization**:  Within the `main()` functions of the scripts, you'll find anonymized path variables (e.g., `input.pdf`, `output_png`, `input.docx`, `output_split_range`, etc.). Remember to replace these with the actual paths to your input files and desired output locations before running the scripts.

For detailed information about specific libraries or functionalities, please refer to the official documentation of Aspose, Pillow, PyPDF2, pdf2docx, and PyMuPDF.