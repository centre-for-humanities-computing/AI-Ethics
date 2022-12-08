"""Pipeline for training w2v across all keys (human, science, etc.)."""
import pandas as pd
from gensim.models import Word2Vec
import os
import glob
import ast


ROOT_DIR = "../../../data/"
subdirectories = glob.glob(f"{ROOT_DIR}*/", recursive=True)

corpus = []

for dir in subdirectories:
    if "pdfs" not in dir:
        for file in os.listdir(dir):
            if file.endswith(".csv"):

                csv_path = os.path.join(dir, file)
                df = pd.read_csv(csv_path)
                df["lemmas"] = df["lemmas"].apply(lambda x: ast.literal_eval(x))
                docs = df["lemmas"].tolist()
                corpus.append(docs)

train_corpus = [item for sublist in corpus for item in sublist]
w2v_model = Word2Vec(sentences=train_corpus, sg=1)
w2v_model.save(f"{ROOT_DIR}/models/w2v_all_docs")
