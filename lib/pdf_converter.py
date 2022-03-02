# Copied from
# https://stackoverflow.com/questions/28246161/pdfminer-export-pages-as-list-of-strings

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def pdf_to_txt_list(file_path):
    # Returns a list of strings, one for each page in the PDF file.
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    # A list for all each page's text
    pages_text = []

    with open(file_path, 'rb') as fp:
        for page in PDFPage.get_pages(fp):
            # Get (and store) the "cursor" position of stream before reading from PDF
            # On the first page, this will be zero
            read_position = retstr.tell()

            # Read PDF page, write text into stream
            interpreter.process_page(page)

            # Move the "cursor" to the position stored
            retstr.seek(read_position, 0)

            # Read the text (from the "cursor" to the end)
            page_text = retstr.read()

            # Add this page's text to a convenient list
            pages_text.append(page_text)
        
    return pages_text
