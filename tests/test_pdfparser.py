import sys

sys.path.append("../src/ethics")
from pdf_parsing import pdf_parser


def test_parser():

    file_path = (
        "../../data/humanism/1993-04-13_Provisional data_OJJOC_1993_101_R_0001_01.pdf"
    )
    text = pdf_parser(file_path)

    assert isinstance(text, str)
