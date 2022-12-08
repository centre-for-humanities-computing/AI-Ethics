"""Pipeline for transforming pdfs into images and extracting text from those images using tesserocr."""

from pdf2image import convert_from_path
import tesserocr
import pytesseract
import os
import glob
import time 

st = time.time()

ROOT_DIR = "../../../data/"
subdirectories = glob.glob(f"{ROOT_DIR}*/", recursive=True)

path_to_tesseract = r"/usr/bin/tesseract"
pytesseract.tesseract_cmd = path_to_tesseract

for dir in subdirectories:
    if "pdfs" not in dir:
        folder_label = dir.split("/")[-2]
        folder_path = os.path.join(ROOT_DIR, f"parsed_pdfs/{folder_label}")

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        for file in os.listdir(dir):
            txt_path = os.path.join(folder_path, f"{file}.txt")
            file_path = os.path.join(dir, file)

            try:
                images = convert_from_path(file_path)
                txt = open(txt_path, "a")
                for i in range(len(images)):
                    text = tesserocr.image_to_text(images[i])
                    txt.write(text)

            except:
                continue


elapsed_time = time.time() - st
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
