
import os
import sys
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path):
    """
    Extracts a range of pages from a PDF file and saves it as a new file.
    """
    # 1. Validate that the input file exists.
    if not os.path.isfile(input_path):
        print(f"Error: The file does not exist at the specified path: {input_path}")
        sys.exit(1)

    try:
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        print(f"The original PDF has {total_pages} pages.")

        # 2. Prompt the user for the page range.
        while True:
            try:
                start_page = int(input(f"Start page (1-{total_pages}): "))
                end_page = int(input(f"End page ({start_page}-{total_pages}): "))
                
                if 1 <= start_page <= end_page <= total_pages:
                    break
                else:
                    print("Error: Invalid page range. Please ensure that 1 <= start <= end <= total_pages.")
            except ValueError:
                print("Error: Please enter a valid integer.")

        # 3. Build the output filename.
        directory = os.path.dirname(input_path)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_filename = f"{base_name}_from_{start_page}-{end_page}_pages.pdf"
        output_path = os.path.join(directory, output_filename)

        # 4. Validate that the output file does not already exist.
        if os.path.exists(output_path):
            print(f"Error: The destination file already exists and will not be overwritten: {output_path}")
            sys.exit(1)

        # 5. Create the new PDF with the selected pages.
        writer = PdfWriter()
        # Page indices in pypdf are 0-based, so we subtract 1.
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        # 6. Save the resulting file.
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"\nSuccess! The file has been created:")
        print(output_path)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # The script expects the full path to the file as the first argument.
    if len(sys.argv) < 2:
        print("Usage: python split_pdf.py \"/path/to/your/file.pdf\"")
        print("Remember to use quotes if the path contains spaces.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    split_pdf(file_path)
