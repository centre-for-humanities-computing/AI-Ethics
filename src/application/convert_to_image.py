"""Pipeline for looping over subdirectories in a given directory, 
finding pdfs, check whether those pdfs are valid, transforming them into images per page, 
extracting text from images, saving text per image (page) into json"""

from pdf2image import convert_from_path
import pandas as pd
import pytesseract
import os
import json
import glob

ROOT_DIR = "/media/kate/Seagate Expansion Drive/kasper-eu/eur-lex/"
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
                file_name = f"{name}_parsed.json"
            
                with open(f"{dir}_parsed/{file_name}", "w") as outfile:
                    outfile.write(data)

            except:
                not_pdfs.append(file_path)
                continue

df = pd.DataFrame(not_pdfs, columns=["files"])
df.to_csv(f"not_pdfs/{dir}.csv")
