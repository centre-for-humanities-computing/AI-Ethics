import sys

sys.path.append("../src/ethics")
from preprocess import clean_text


def test_clean_func():

    sent = "Here you can find the   definiton for the dot   product https://en.wikipedia.org/wiki/Dot_product 1111"
    cleaned_sent = clean_text(sent)

    assert isinstance(cleaned_sent, str)
    assert cleaned_sent == "here you can find the definiton for the dot product"