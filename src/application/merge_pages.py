"""Pipluine for merging strings per page into a single text and saving all texts per doc per subdir into json"""

import glob
import json 
import os 

dir_names = ["humanism"]

#or

#ROOT_DIR = "/media/kate/Seagate Expansion Drive/kasper-eu/eur-lex/"
#subdirectories = glob.glob(f"{ROOT_DIR}*/", recursive = True)
#dir_names = [name.split("/")[-2] for name in subdirectories]


dataset = []

for name in dir_names:
    dir = f"{name}_parsed/"
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

    file_name = f"{name}_all_docs.json"
            
    with open(f"{dir}{file_name}", "w") as outfile:
        outfile.write(json_data)
