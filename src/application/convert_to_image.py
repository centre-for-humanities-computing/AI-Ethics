"""Pipeline for looping over subdirectories in a given directory, 
finding pdfs, checking whether those pdfs are valid, transforming them into images per page, 
extracting text from images, saving text per image (page) per pdf into json"""

from pdf2image import convert_from_path
import pandas as pd
import pytesseract
import os
import json
import glob

ROOT_DIR = "/data_archive/eu-ethics-temp/data/"
subdirectories = glob.glob(f"{ROOT_DIR}*/", recursive = True)

path_to_tesseract = r"/usr/bin/tesseract"
pytesseract.tesseract_cmd = path_to_tesseract
not_pdfs = []

for dir in subdirectories:
    for file in os.listdir(dir):
        if file.endswith(".pdf"):
            file_path = os.path.join(ROOT_DIR, file)

            # test whether a file is a valid PDF
            # if yes, transform each pdf into a sequence of images per page 
            # if no, skip this file and save its path into a list (futher tehe list will be saved into a dataframe)
            try:
                images = convert_from_path(file_path)
                
                dic = {}
                dataset = []
                
                # extract text from each image (page) and save into json
                for i in range(len(images)):
                    text = pytesseract.image_to_string(images[i])
                    dic[f"page_{i}"] = text
                dataset.append(dic)
            
                data = json.dumps(dataset, ensure_ascii=False, indent=2)

                name = file.split(".pdf")[0]
                folder_label = dir.split("/")[-2]
                file_name = f"{name}.json"
                folder_path = os.path.join(ROOT_DIR, f"parsed_pdf_per_page/{folder_label}/")
                save_file_to = os.path.join(folder_path, file_name)

                if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
            
                with open(save_file_to, "w") as outfile:
                    outfile.write(data)

            except:
                not_pdfs.append(file_path)
                continue

df = pd.DataFrame(not_pdfs, columns=["files"])
df.to_csv(os.path.join(ROOT_DIR, f"not_pdfs/{folder_label}.csv"))
