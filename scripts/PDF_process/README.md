# PDF Processing Scripts: Scale, Separate Pages, and Compress

This directory contains Python scripts for various PDF processing tasks:

*   **`scale_pdf_converter.py`**: Resizes PDF documents to a new specified width and height, effectively scaling the content of each page.
*   **`separate_pdf_pages_converter.py`**: Separates each page of a PDF document into individual PDF files.
*   **`compress_pdf_converter.py`**: Compresses PDF documents by reducing the quality of images within the PDF, aiming to reduce file size.

These scripts utilize the following Python libraries:

*   **PyPDF2**: For PDF scaling and page separation.
*   **PyMuPDF (fitz)**: For PDF compression.
*   **Pillow (PIL)**: For image manipulation during PDF compression (used by PyMuPDF).

## Requirements

Before running these scripts, you need to install the necessary Python libraries. You can do this using pip and the provided `requirements.txt` file (see below) or by installing them individually.

## Installation

1.  **Install Python**: Ensure you have Python installed on your system. Python 3.6 or later is recommended.
2.  **Install required libraries**: Navigate to this directory in your terminal and run:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Each script is designed to be run from the command line. You will need to modify the `main()` function in each script to set the input file path, output directory, and any specific processing parameters.

**Example Usage:**

1.  **Modify script parameters:** Open the script you want to use (e.g., `scale_pdf_converter.py`) in a text editor. Look for the `main()` function and adjust the `input_pdf_file`, `output_directory`, and any relevant parameters for processing.

    For example, in `scale_pdf_converter.py`:

    ```python
    def main():
        input_pdf_file = 'path/to/your/input.pdf' # Replace with your input PDF path
        output_directory = 'path/to/your/output_scaled_pdf_directory' # Replace with your desired output directory
        new_width = 600  # Desired width for resized pages
        new_height = 800 # Desired height for resized pages

        scaler = PDFScaler(input_pdf_file, output_directory)
        scaler.set_dimensions(new_width, new_height) # Set new dimensions
        scaler.resize_pdf()
    ```

    For `compress_pdf_converter.py`, you can adjust the `jpeg_quality` parameter in the `main()` function to control the compression level (lower quality = higher compression, smaller file size).

2.  **Run the script:** Open your terminal, navigate to the directory containing the script, and run the script using Python:

    ```bash
    python scale_pdf_converter.py
    ```

    Repeat this process for other scripts, adjusting the input and output paths and processing parameters in the `main()` function of each script to suit your needs.

## Logging

All scripts are equipped with basic logging. Log messages will be printed to the console, providing information about the PDF processing and any errors encountered.

## Notes

*   **PyMuPDF (fitz) Dependency**: The PDF compression script relies on `PyMuPDF`, which in turn uses native libraries. Ensure that `PyMuPDF` is installed correctly and compatible with your system.
*   **Compression Quality**: The `compress_pdf_converter.py` script reduces PDF size by compressing images to JPEG format with a specified quality. Adjust the `jpeg_quality` parameter to balance between file size and image quality. Very low quality values might result in noticeable image degradation.
*   **Error Handling**: The scripts include basic error handling and logging to help identify and resolve issues during PDF processing.
*   **Path Anonymization**: The scripts use anonymized path variables in the `main()` functions (`input.pdf`, `output_scaled_pdf`, etc.). Replace these with your actual file paths.

For any questions or issues, please refer to the documentation of the respective Python libraries used in these scripts.