"""Pipeline for extracting text from pdfs with pdfminer. This approach is faster than tesserocr but less accurate in terms of coherence for 2 column formated texts."""
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
from tqdm import tqdm
import glob
import time

st = time.time()


def pdfparser(data):

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


ROOT_DIR = "../../../data/"
subdirectories = glob.glob(f"{ROOT_DIR}*/", recursive=True)

for dir in subdirectories:
    if "pdfs" not in dir:
        print(dir)

        folder_label = dir.split("/")[-2]
        folder_path = os.path.join(ROOT_DIR, f"parsed_pdfs/{folder_label}")

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        for file in os.listdir(dir):
            print(file)
            txt_name = file.split(".pdf")[0] + ".txt"
            txt_path = os.path.join(folder_path, txt_name)
            file_path = os.path.join(dir, file)

            try:
                text = pdfparser(file_path)
                txt = open(txt_path, "a")
                txt.write(text)

            except:
                continue

elapsed_time = time.time() - st
print("Execution time:", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
