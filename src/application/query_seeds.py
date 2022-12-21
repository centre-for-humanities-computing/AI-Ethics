"""Pipeline for finding the top-N most similar words."""
from gensim.models import Word2Vec
import os
import json

ROOT_DIR = "../../../data/parsed_pdfs/models/"

seed_list = [
    "ai",
    "ai_ethics",
    "responsible_ai",
    "human_centred_ai",
    "european_ai",
    "trustworthy_ai",
    "ai_and_society",
    "humanism",
    "humanist",
    "sovereignty",
    "technological_sovereignty",
    "ethics",
    "european_values",
    "european_identity",
    "european_unity",
    "ai_and_humanism",
    "ai_and_sovereignty",
    "ai_and_european_values",
    "ai_and_trust",
    "ai_and_ethics",
]


for file in os.listdir(ROOT_DIR):
    if "npy" not in file:
        file_path = os.path.join(ROOT_DIR, file)
        model = Word2Vec.load(file_path)

        dataset = []
        for seed in seed_list:
            file_dict = {}
            try:
                similar = model.wv.most_similar(seed, topn=10)
                file_dict[seed] = similar
            except KeyError:
                continue
            dataset.append(file_dict)

        data = json.dumps(dataset, ensure_ascii=False, indent=2)
        file_name = "query/" + file + ".json"

        with open(file_name, "w") as outfile:
            outfile.write(data)
