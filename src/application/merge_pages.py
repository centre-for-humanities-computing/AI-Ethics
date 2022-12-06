"""Pipeline for merging strings per page into a single text i.e., all docs per keyword are saved into a single json"""

import glob
import json 
import os 

ROOT_DIR = "/data_archive/eu-ethics-temp/data/"
subdirectories = glob.glob(f"{ROOT_DIR}*/", recursive = True)
dir_names = [name.split("/")[-2] for name in subdirectories]

for name in dir_names:

    dataset = []
    dir = os.path.join(ROOT_DIR, f"parsed_pdf_per_page/{name}/")

    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)

        with open(file_path, "r") as f:
            data = json.load(f)

            text = []
            dic = {}

            for page in data:
                for value in page.values():
                    text.append(value)

            doc = " ".join(text)
            dic["document"] = file
            dic["text"] = doc
            dataset.append(dic)

     
    json_data = json.dumps(dataset, ensure_ascii=False, indent=2)
    
    save_to_path = os.path.join(ROOT_DIR, f"merged_texts/{name}.json")

    with open(save_to_path, "w") as outfile:
        outfile.write(json_data)
