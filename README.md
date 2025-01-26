# Document Conversion and Processing Scripts

This repository contains Python scripts for various document conversion and processing tasks. It is organized into three main sections, each within its own directory:

*   **`conversion_scripts`**:  Scripts for converting between different document formats (PDF to PNG, JPG to PDF, PDF to Text, PDF to Word).
*   **`word_splitting_scripts`**: Scripts for splitting Word DOCX documents in different ways (by page range, by section, by page count).
*   **`pdf_processing_scripts`**: Scripts for manipulating PDF documents (scaling pages, separating pages, compressing PDFs).

## Sections and Scripts Overview

### 1. `conversion_scripts` Directory

This directory (`conversion_scripts/`) contains scripts for converting between different document formats:

*   **`pdf_to_png_converter.py`**: Converts PDF documents to PNG images, with each page becoming a separate PNG file.
*   **`jpg_to_pdf_converter.py`**: Converts JPG images to PDF documents.
*   **`pdf_to_text_converter.py`**: Extracts text from PDF documents and saves it to a TXT file.
*   **`pdf_to_word_converter.py`**: Converts PDF documents to Word DOCX files.

### 2. `word_splitting_scripts` Directory

This directory (`word_splitting_scripts/`) includes scripts for splitting Word DOCX documents using Aspose.Words:

*   **`split_word_document_by_page_range.py`**: Splits a Word document by extracting a specified range of pages into a new document.
*   **`split_word_document_by_section.py`**: Splits a Word document into multiple documents, with each section becoming a separate DOCX file.
*   **`split_word_document_by_page.py`**: Splits a Word document into multiple documents, where each output document contains a defined number of pages.

### 3. `pdf_processing_scripts` Directory

This directory (`pdf_processing_scripts/`) provides scripts for various PDF manipulation tasks:

*   **`scale_pdf_converter.py`**: Resizes PDF documents to a new specified width and height, scaling page content.
*   **`separate_pdf_pages_converter.py`**: Separates each page of a PDF document into individual PDF files.
*   **`compress_pdf_converter.py`**: Compresses PDF documents by reducing the quality of images within, aiming for smaller file sizes.

## Requirements

The scripts in this repository rely on several Python libraries. Before running any script, ensure you have installed the necessary libraries. You can install all required libraries using pip and the provided `requirements.txt` file located in the root directory of this repository.

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

The scripts are organized into directories based on their functionality. To use a script:

1.  **Navigate to the correct script directory**: Open your terminal and first navigate to the root directory of this repository (where `README.md` and `requirements.txt` are located). Then, change your current directory to the folder containing the script you wish to use:

    *   **For Conversion Scripts**:
        ```bash
        cd conversion_scripts
        ```
        You are now in the `conversion_scripts` directory, which contains scripts like `pdf_to_png_converter.py`, `jpg_to_pdf_converter.py`, etc.

    *   **For Word Splitting Scripts**:
        ```bash
        cd word_splitting_scripts
        ```
        You are now in the `word_splitting_scripts` directory, which contains scripts like `split_word_document_by_page_range.py`, `split_word_document_by_section.py`, etc.

    *   **For PDF Processing Scripts**:
        ```bash
        cd pdf_processing_scripts
        ```
        You are now in the `pdf_processing_scripts` directory, which contains scripts like `scale_pdf_converter.py`, `separate_pdf_pages_converter.py`, etc.

2.  **Modify Script Parameters (if needed)**: Once you are in the correct script directory, open the script you intend to run (e.g., `pdf_to_png_converter.py`) in a text editor. Look for the `main()` function and adjust the input file paths, output directories, and any script-specific parameters within the `main()` function to match your needs.

    **(Example modifications remain the same as in the previous README and are omitted here for brevity, but should be included in the full README.md)**
    *(Refer to the previous full README.md for example modifications for `pdf_to_png_converter.py`, `split_word_document_by_page_range.py`, and `compress_pdf_converter.py`)*

    **Example: Modifying `pdf_to_png_converter.py` (in `conversion_scripts` directory):**

    ```python
    def main():
        input_pdf_file = 'path/to/your/input.pdf'  # 📝 Replace with your input PDF file path
        output_directory = 'path/to/your/output_png_directory' # 📝 Replace with your desired output directory

        converter = PDFtoPNGConverter(input_pdf_file, output_directory)
        converter.set_resolution(300) # ⚙️ Optional: Adjust resolution if needed
        converter.convert_to_png()
    ```

    **Example: Modifying `split_word_document_by_page_range.py` (in `word_splitting_scripts` directory):**

    ```python
    def main():
        input_docx_file = 'path/to/your/input.docx' # 📝 Replace with your input DOCX file path
        output_directory = 'path/to/your/output_split_range_directory' # 📝 Replace with your output directory

        splitter = WordDocumentSplitterByRange(input_docx_file, output_directory)
        splitter.split_document(3, 6) # ⚙️ Example: Extract pages 3 to 6. Adjust page numbers as needed.
    ```

    **Example: Modifying `compress_pdf_converter.py` (in `pdf_processing_scripts` directory):**

    ```python
    def main():
        input_pdf_file = 'path/to/your/input.pdf' # 📝 Replace with your input PDF file path
        output_directory = 'path/to/your/output_compressed_pdf_directory' # 📝 Replace with your output directory
        jpeg_quality = 80 # ⚙️ Example JPEG quality: 80 (adjust for desired compression/quality)

        compressor = PDFCompressor(input_pdf_file, output_directory)
        compressor.set_jpeg_quality(jpeg_quality) # Set JPEG quality
        compressor.compress_pdf()
    ```

3.  **Run the script**: From within the script's directory (which you navigated to in step 1), execute the script using Python:

    ```bash
    python pdf_to_png_converter.py  # Example for PDF to PNG conversion (run from conversion_scripts directory)
    python split_word_document_by_page_range.py # Example for Word splitting (run from word_splitting_scripts directory)
    python compress_pdf_converter.py # Example for PDF compression (run from pdf_processing_scripts directory)
    ```

    Make sure you are running the `python` command from *inside* the specific script's directory (e.g., `conversion_scripts`, `word_splitting_scripts`, or `pdf_processing_scripts`). Replace the script name with the one you intend to use.

**(The rest of the "Logging" and "Notes" sections of the README remain the same as in the previous version and are omitted here for brevity, but should be included in the full README.md)**
*(Refer to the previous full README.md for the "Logging" and "Notes" sections)*

**To summarize the folder structure for usage:**
```bash
document_processing_scripts/ [Root directory]
├── README.md [Integrated README file]
├── requirements.txt [Integrated requirements file]
├── conversion_scripts/ [Directory for conversion scripts]
│ ├── pdf_to_png_converter.py
│ ├── jpg_to_pdf_converter.py
│ ├── pdf_to_text_converter.py
│ └── pdf_to_word_converter.py
├── word_splitting_scripts/ [Directory for word splitting scripts]
│ ├── split_word_document_by_page_range.py
│ ├── split_word_document_by_section.py
│ └── split_word_document_by_page.py
└── pdf_processing_scripts/ [Directory for PDF processing scripts]
├── scale_pdf_converter.py
├── separate_pdf_pages_converter.py
└── compress_pdf_converter.py
```


## Logging

All scripts are configured with basic logging. Informational messages and errors will be logged to the console during script execution, providing feedback on the process and helping to diagnose any issues.

## Notes

*   **Aspose Licensing**: Scripts using `aspose-pdf` and `aspose-words` libraries (specifically `pdf_to_png_converter.py` and the Word splitting scripts) may require licenses for commercial use. Please review Aspose's licensing terms if you plan to use these scripts commercially.
*   **PyMuPDF Dependency**: The `compress_pdf_converter.py` script relies on `PyMuPDF`, which has native library dependencies. Ensure PyMuPDF is installed correctly for your operating system.
*   **JPEG Compression Quality**: When using `compress_pdf_converter.py`, adjust the `jpeg_quality` parameter to balance between output file size and image quality degradation. Lower quality values will result in smaller files but potentially lower image fidelity.
*   **Error Handling**: Basic error handling is included in all scripts to catch common issues like file not found errors and exceptions during processing. Check the console output for error messages if a script fails to run as expected.
*   **Path Anonymization**:  Within the `main()` functions of the scripts, you'll find anonymized path variables (e.g., `input.pdf`, `output_png`, `input.docx`, `output_split_range`, etc.). Remember to replace these with the actual paths to your input files and desired output locations before running the scripts.

For detailed information about specific libraries or functionalities, please refer to the official documentation of Aspose, Pillow, PyPDF2, pdf2docx, and PyMuPDF.