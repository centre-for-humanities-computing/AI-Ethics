"""Pipeline for preprocessing texts per key/folder (f.ex., ethics, science, etc.)."""
import sys

sys.path.append("../ethics")
import pandas as pd
import glob
import os
import spacy
from preprocess import clean_text, collect_lemmas, rm_stops

nlp = spacy.load("en_core_web_lg")
stops = open("../../stopwords.txt", "r")
stops = stops.read().split()

ROOT_DIR = "../../../data/w2v_test/"
subdirectories = glob.glob(f"{ROOT_DIR}*/", recursive=True)

for dir in subdirectories:
    if "pdfs" not in dir:

        docs_per_folder = []
        files = []

        for file in os.listdir(dir):
            if file.endswith(".txt"):
                file_path = os.path.join(dir, file)
                files.append(file)
                with open(file_path) as f:
                    text = f.read()
                    cleaned_text = clean_text(text)
                    lemmas = collect_lemmas(cleaned_text, nlp)
                    no_stops = rm_stops(lemmas, stops)
                    docs_per_folder.append(no_stops)

            key = dir.split("/")[-2]
            df = pd.DataFrame(columns=["doc", "lemmas"])
            df["doc"] = files
            df["lemmas"] = docs_per_folder
            df.to_csv(f"{dir}{key}_lemmas.csv", index=False)
