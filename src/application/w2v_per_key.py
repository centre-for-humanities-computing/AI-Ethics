"""Pipeline for training w2v per key (f.ex., corpus for human, science, etc.)."""
import pandas as pd
from gensim.models import Word2Vec
from gensim.models.phrases import Phrases
import os
import glob
import ast


ROOT_DIR = "../../../data/parsed_pdfs/"
subdirectories = glob.glob(f"{ROOT_DIR}*/", recursive=True)


for dir in subdirectories:
    print(dir)
    if "models" not in dir:
        for file in os.listdir(dir):
            if file.endswith(".csv"):
                print(file)
                
                csv_path = os.path.join(dir, file)
                df = pd.read_csv(csv_path)
                df["lemmas"] = df["lemmas"].apply(lambda x: ast.literal_eval(x))
                docs = df["lemmas"].tolist()

                bigram = Phrases(docs)
                trigram = Phrases(bigram[docs])

                trigrams = []

                for i in range(len(docs)):
                    trigrams.append(bigram[docs[i]])

                w2v_model = Word2Vec(sentences=trigrams, sg=1)
                label = dir.split("/")[-2]
                path_w2v = f"{ROOT_DIR}/models/w2v_trigrams_{label}"
                w2v_model.save(path_w2v)
