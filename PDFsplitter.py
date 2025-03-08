import fitz  # PyMuPDF
import os
import argparse
import sys

def split_pdf(input_pdf, num_parts):
    """Splits a PDF into the specified number of parts and saves it in the same directory as the input."""
    
    # Ensure the input file exists
    if not os.path.exists(input_pdf):
        print(f"Error: The file '{input_pdf}' does not exist.")
        sys.exit(1)

    try:
        doc = fitz.open(input_pdf)
    except Exception as e:
        print(f"Error: Could not open the PDF file. {e}")
        sys.exit(1)

    total_pages = len(doc)

    if num_parts > total_pages:
        print(f"Warning: The PDF has only {total_pages} pages. Adjusting number of parts to {total_pages}.")
        num_parts = total_pages

    # Get input file details
    input_dir = os.path.dirname(input_pdf)
    input_filename = os.path.splitext(os.path.basename(input_pdf))[0]

    # Create default output folder in the same directory
    output_folder = os.path.join(input_dir, f"{input_filename}_OUTPUT")
    os.makedirs(output_folder, exist_ok=True)

    pages_per_part = total_pages // num_parts
    remainder = total_pages % num_parts

    start_page = 0
    for i in range(num_parts):
        end_page = start_page + pages_per_part + (1 if i < remainder else 0)
        new_pdf = fitz.open()
        for j in range(start_page, end_page):
            new_pdf.insert_pdf(doc, from_page=j, to_page=j)

        output_filename = os.path.join(output_folder, f"{input_filename}_part_{i+1}.pdf")
        new_pdf.save(output_filename)
        new_pdf.close()
        print(f"Saved: {output_filename}")

        start_page = end_page

    doc.close()
    print(f"PDF splitting complete! Files saved in: {output_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split a PDF into multiple parts and save them in the same directory as the input file.",
        epilog="Example: python PDFsplitter.py input.pdf 5"
    )

    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("num_parts", type=int, help="Number of parts to split into")

    args = parser.parse_args()

    # Validate num_parts
    if args.num_parts < 1:
        print("Error: The number of parts must be at least 1.")
        sys.exit(1)

    split_pdf(args.input_pdf, args.num_parts)
