# PDF Generator from CSV Data

This script generates a multi-page PDF file from a CSV file (`data.csv`). Each row in the CSV file represents a topic that may span multiple pages, with a title at the top and a footer at the bottom of each page. Horizontal lines are added to each page to serve as note lines.

## Requirements

- Python 3.x
- Required libraries: `fpdf2`, `pandas`

Install the required libraries with:

```bash
pip install fpdf2 pandas
```

## How to Use

1. **Prepare the `data.csv` file**:
   - Ensure `data.csv` is in the same directory as the script.
   - The CSV should have the following columns:
     - **Order**: A number representing the order (not used in the script but helpful for reference).
     - **Topic**: Title of the topic, which will appear as the header on each page.
     - **Pages**: The number of pages for each topic.

   Example content for `data.csv`:
   ```csv
   Order,Topic,Pages
   1,Python Basics,2
   2,Advanced Python,1
   3,Data Analysis,3
   ```

2. **Run the Script**:
   - Execute the script to generate `output.pdf`.
   ```bash
   python script_name.py
   ```

3. **Output**:
   - The generated `output.pdf` will contain a header, horizontal note lines, and a footer with the topic name on each page.
   - Each topic will be divided across the specified number of pages.

## Functions Overview

- **draw_lines(pdf: FPDF) -> None**: Draws horizontal lines across each page for note-taking.
- **set_footer(pdf: FPDF, text: str) -> None**: Adds a footer with the topic name at the bottom right of each page.

## Example Usage

With a `data.csv` file containing multiple topics, each with a specific page count, running the script will create a formatted PDF file, ready for printing or digital use.

