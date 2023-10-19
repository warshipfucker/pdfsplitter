# pdfsplitter
This Python script allows you to split a large PDF file into smaller PDF files. You can specify the input PDF file, the prefix for the output files, and the number of pages per small file.

## Requirements

- Python 3.x
- PyPDF2 library (you can install it using `pip install PyPDF2`)

## Usage
1. Download and install Python from the [official website](https://www.python.org/downloads/).
2. Open a terminal or command prompt.
3. Clone or download this repository to your computer.
4. Navigate to the directory where the script is located.
5.  To install the required PyPDF2 library, open a terminal or command prompt, navigate to the directory with the script, and run the following command:
`pip install -r requirements.txt` or `pip install PyPDF2`
7.  Run the script using the following command: `python3 pdfsplitter.py` or `python pdfsplitter.py`
8. Follow the on-screen instructions to split your PDF file:
- Enter the name of the large PDF file (with or without .pdf ending).
- Enter the prefix for the output files.
- Enter the number of pages per small file.
7. The script will create a folder with the same name as the input PDF file (without the .pdf extension) and save the smaller PDF files there.
8. The process is completed, and you will find the split PDF files in the specified folder.

## Example
Suppose you have a large PDF file named `example.pdf`, and you want to split it into smaller files with a prefix of `output` and 10 pages per small file. You would run the script as follows:

Enter the following when prompted:

- Enter the name of the large PDF file: `example.pdf`
- Enter the prefix for the output files: `output`
- Enter the number of pages per small file: `10`

The script will create a folder named `example` and save the split PDF files inside.

## License

This script is released under the [MIT License](LICENSE).


