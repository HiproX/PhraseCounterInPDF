import PyPDF2

''' 
Function to find page numbers in PDF documents where the phrase occurs

Accepts 2 arguments:
    pdf_filenames: an array of strings with pdf file names.
    word: the string to search for in the pdf files.

Returns:
    A map structure, where the key is the name of the PDF file,
     and the value is a set containing the page numbers of the pdf file,
     where the word word occurs.
'''
def find_string_in_pdfs(pdf_filenames, line):
    result = {}
    for pdf_filename in pdf_filenames:
        try:
            with open(pdf_filename, "rb") as f:
                pdf_file = PyPDF2.PdfReader(f)
                pages = set()
                for page_num in range(len(pdf_file.pages)):
                    page = pdf_file.pages[page_num]
                    if line in page.extract_text():
                        pages.add(page_num)
                if (len(pages)):
                    result[pdf_filename] = pages
        # Exception - If file not found
        except FileNotFoundError:
            pass
    return result


''''Example of Use'''
pdf_filenames = ["your_document1.pdf", "your_document2.pdf", "your_document3.pdf"] # or if 1 document, just ["your_document1.pdf"]
line = 'your search phrase'
# Search for a line in PDF documents
result = find_string_in_pdfs(pdf_filenames, line)
# Print the result, but first check for blank
if (len(result)):
    print('The word [', line, '] appeared in:')
    for pdf_filename, pages in result.items():
        print("--[", pdf_filename, "] on the pages:", pages)         
else:
    print('Nothing found')