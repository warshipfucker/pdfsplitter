import os
import PyPDF2

# Prompt for user input
input_pdf_file = input("Enter the name of the large PDF file: ")
# Check if the input PDF file has the .pdf extension, and add it if it's missing
if not input_pdf_file.lower().endswith('.pdf'):
    input_pdf_file += '.pdf'
output_prefix = input("Enter the prefix for the output files: ")
pages_per_file = int(input("Enter the number of pages per small file: "))
# Get the folder containing the input PDF file
input_folder = os.path.dirname(input_pdf_file)
# Extract the folder name from the input PDF file
output_folder = os.path.join(input_folder, os.path.splitext(os.path.basename(input_pdf_file))[0])
# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
# Open the large PDF file
with open(input_pdf_file, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)   
    # Get the total number of pages in the large PDF
    total_pages = len(pdf_reader.pages)   
    # Calculate how many small PDF files to create
    num_small_pdfs = (total_pages // pages_per_file) + 1   
    for i in range(num_small_pdfs):
        start_page = i * pages_per_file
        end_page = min((i + 1) * pages_per_file, total_pages)
        # Create a new PDF file
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(start_page, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])
            output_file_name = os.path.join(output_folder, f'{output_prefix}_{i + 1}.pdf')
        with open(output_file_name, 'wb') as small_pdf_file:
            pdf_writer.write(small_pdf_file)
print("Process completed. Small PDF files have been created in the folder:", output_folder)
