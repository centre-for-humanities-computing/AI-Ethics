"""Function for extarecting text from a pdf."""
rom pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

def pdfparser(data) -> str:
    """
    Extracts text from a pdf.
    Args:
        data: pdf file
    Returns:
        str: text from pdf.
    """

    fp = open(data, "rb")
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()
    return data