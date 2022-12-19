"""Functions for cleaning, lemmatising and removing stop words from text."""
import regex as re
from typing import List


def clean_text(text: str) -> str:
    """
    Cleans text from punctuation, URLs, multiple spaces and lowercases.
    Args:
        text (str): The text document to clean.
    Returns:
        str: The cleaned document.
    """
    no_urls = re.sub(r"http\S+", "", text)
    no_special_ch = re.sub(
        r"(#[A-Za-z]+)|(@[A-Za-z]+)|([^A-Za-z \t])|(\w+:\/\/\S+)", " ", no_urls
    )

    no_special_ch = no_special_ch.replace("\n", " ")
    lowercased_str = no_special_ch.lower()
    cleaned_text = " ".join(lowercased_str.split())

    return cleaned_text


def collect_lemmas(text: str, nlp) -> List[str]:
    """
    Lemmatizes text using spaCy pipeline.
    Args:
        text (str): A string to be lemmatized.
        nlp: A spaCy pipeline.
    Returns:
        List[str]: A list with lemmas.
    """
    lemmas = []
    doc = nlp(text, disable = ['ner', 'parser'])
    for token in doc:
        lemmas.append(token.lemma_)

    return lemmas


def rm_stops(doc: List[str], stopwords: List[str]) -> List[str]:
    """
    Removes stopwords from tokenized/lemmatized text.
    Args:
        text (List[str]): A list with tokens/lemmas.
        stopwords (List[str]): A list of stopwords.
    Returns:
       List[str]: A list with tokens/lemmas without stopwords.
    """
    no_stopwords = []

    for word in doc:
        if word not in stopwords:
            no_stopwords.append(word)

    return no_stopwords
