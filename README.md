# PDF Page Extractor

A simple yet powerful Python script to extract a specific range of pages from a PDF file and save them as a new, cleanly-named PDF document.

This tool is designed to be run from the command line and is ideal for quickly splitting chapters from books, separating articles, or isolating specific sections of a large PDF without the need for heavy software.

## Features

- **Interactive Prompts**: Asks for the start and end pages directly in your terminal.
- **Safe**: Never overwrites the original file. It aborts if the destination file already exists.
- **Smart Naming**: The output file is automatically named based on the original filename and the page range selected (e.g., `MyBook_from_10-25_pages.pdf`).
- **Cross-Platform**: Works on macOS, Windows, and Linux.
- **Handles Spaces**: Correctly processes file paths that contain spaces.

## Installation

Follow these steps to set up the script and its dependencies in a clean virtual environment.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone git@github.com:fpinero/splitPDF.git
    cd splitPDF
    ```

2.  **Create a Python virtual environment:**
    ```bash
    # For Python 3
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    - On macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, execute it with `python` and provide the full path to the PDF file you want to split as a command-line argument.

**Important**: Remember to enclose the file path in double quotes (`"`) if it contains any spaces.

### Example

```bash
python split_pdf.py "/Users/fpinero/Documents/My Important Book.pdf"
```

After running the command, the script will prompt you to enter the desired page range:

```
The PDF original has 250 pages.
Página inicial (1-250): 30
Página final (30-250): 45
```

Upon success, it will create a new file in the same directory as the original:

```
¡Éxito! Se ha creado el fichero:
/Users/fpinero/Documents/My Important Book_from_30-45_pages.pdf
```