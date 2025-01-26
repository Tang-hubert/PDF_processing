# Conversion Scripts: PDF, JPG, Text, and Word Converters

This directory contains Python scripts for converting between different document formats:

*   **`pdf_to_png_converter.py`**: Converts PDF documents to PNG images, with each page becoming a separate PNG file.
*   **`jpg_to_pdf_converter.py`**: Converts JPG images to PDF documents.
*   **`pdf_to_text_converter.py`**: Extracts text from PDF documents and saves it to a TXT file.
*   **`pdf_to_word_converter.py`**: Converts PDF documents to Word DOCX files.

These scripts utilize the following Python libraries:

*   **Aspose.PDF**: For PDF to PNG conversion. (Note: Aspose.PDF might require a license for commercial use beyond evaluation.)
*   **Pillow (PIL)**: For JPG to PDF conversion.
*   **PyPDF2**: For PDF to Text conversion and as a dependency for other scripts.
*   **pdf2docx**: For PDF to Word conversion.

## Requirements

Before running these scripts, you need to install the necessary Python libraries. You can do this using pip and the provided `requirements.txt` file (see below) or by installing them individually.

## Installation

1.  **Install Python**: Ensure you have Python installed on your system. Python 3.6 or later is recommended.
2.  **Install required libraries**: Navigate to this directory in your terminal and run:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Each script is designed to be run from the command line.  You'll need to modify the `main()` function in each script to set the input file path and output directory as needed.

**Example Usage:**

1.  **Modify script parameters:** Open the script you want to use (e.g., `pdf_to_png_converter.py`) in a text editor. Look for the `main()` function and adjust the `input_pdf_file` and `output_directory` variables to point to your input file and desired output location.

    ```python
    def main():
        input_pdf_file = 'path/to/your/input.pdf'  # Replace with your input PDF path
        output_directory = 'path/to/your/output_png_directory' # Replace with your desired output directory

        converter = PDFtoPNGConverter(input_pdf_file, output_directory)
        converter.set_resolution(300) # Optional: Adjust resolution if needed
        converter.convert_to_png()
    ```

2.  **Run the script:** Open your terminal, navigate to the directory containing the script, and run the script using Python:

    ```bash
    python pdf_to_png_converter.py
    ```

    Repeat this process for other scripts, adjusting the input and output paths and any specific parameters (like resolution for PDF to PNG, or JPEG quality if applicable to future scripts) in the `main()` function of each script.

## Logging

All scripts are equipped with basic logging. Log messages will be printed to the console, providing information about the conversion process and any errors encountered.

## Notes

*   **Aspose.PDF Licensing**: Be aware of the licensing requirements for Aspose.PDF, especially for commercial use. You may need to obtain a license from Aspose if you intend to use `pdf_to_png_converter.py` in a commercial setting.
*   **Error Handling**: The scripts include basic error handling and logging to help identify and resolve issues during conversion.
*   **Path Anonymization**: The scripts use anonymized path variables in the `main()` functions (`input.pdf`, `output_png`, etc.).  Replace these with your actual file paths.

For any questions or issues, please refer to the documentation of the respective Python libraries used in these scripts.