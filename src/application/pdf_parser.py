"""Pipeline for extracting text from pdfs with pdfminer. This approach is faster than tesserocr but less accurate in terms of coherence for 2 column formated texts."""
import sys

sys.path.append("../ethics")
import os
import glob
import time
from parser import pdfparser

st = time.time()

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
