PDF Splitter Script
A Python script to split a PDF into multiple parts, automatically saving the output in the same directory as the input file.

Features
Splits a PDF into a user-defined number of parts.
Automatically saves output files in a folder named {input_filename}_OUTPUT, located in the same directory as the original PDF.
Handles cases where the number of parts exceeds the number of pages.
Simple command-line interface.
Requirements
This script requires Python 3 and the following library:

PyMuPDF (fitz)
Installation
Install PyMuPDF using pip:

pip install pymupdf
Usage
Run the script from the command line:

python PDFsplitter.py <input_pdf> <num_parts>
Example
python PDFsplitter.py "C:\Users\brych\Documents\file.pdf" 5
This will:

Split file.pdf into 5 parts.
Save the split files in:
makefile
Copy
Edit
C:\Users\brych\Documents\file_OUTPUT\
file_part_1.pdf
file_part_2.pdf
file_part_3.pdf
file_part_4.pdf
file_part_5.pdf
Help Command
To see usage instructions, run:

python PDFsplitter.py -h
Notes
If the requested number of parts exceeds the number of pages, the script adjusts accordingly.
Output files are named based on the original file, e.g., file_part_1.pdf, file_part_2.pdf, etc.
The script ensures proper error handling for invalid inputs.