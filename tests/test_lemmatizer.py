import sys

sys.path.append("../src/ethics")
import spacy
from preprocess import collect_lemmas


def test_lemmatizer():

    nlp = spacy.load("en_core_web_lg")
    test_sent = "She has two dogs and a cat"
    tokens = collect_lemmas(test_sent, nlp=nlp)

    assert tokens == [
        "she",
        "have",
        "two",
        "dog",
        "and",
        "a",
        "cat",
    ]

    for token in tokens:
        assert isinstance(token, str)
