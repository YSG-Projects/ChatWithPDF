import PyPDF2

def read_pdf(file) -> str:
    """
    Reads a PDF file and returns the extracted text.
    """
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text
