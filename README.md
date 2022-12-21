# AI-Ethics

## Data

All data is on `grundtvig` under `/data_archive/eu-ethics-temp/data` and organized as follows:

```
├── data/                        
│   ├── artificial_intelligence/
│   │    └── ...       ---------> raw pdfs
│   ├── ethics/  
│   │    └── ...       ---------> raw pdfs
│   ├── human/
│   │    └── ...       ---------> raw pdfs
│   ├── humanism/
│   │    └── ...       ---------> raw pdfs
│   ├── human_rights/
│   │    └── ...       ---------> raw pdfs
│   ├── innovation/
│   │    └── ...       ---------> raw pdfs
│   ├── parsed_pdfs/
│   │      ├── human_rights/ ---------> parsed pdfs (not complete) saved into txt and csv with lemmas
│   │      │    └── ...
│   │      ├── humanism/     ---------> parsed pdfs saved into txt and csv with lemmas
│   │      │     └── ...
│   │      ├── innovation/   ---------> parsed pdfs saved into txt and csv with lemmas
│   │      │     └── ...
│   │      ├── models/       ---------> w2v models
│   │      │     └── ...     
│   │      └── science/      ---------> parsed pdfs saved into txt and csv with lemmas
│   │            └── ...  
│   │      
│   ├── science/       ---------> raw pdfs
│   │    └── ...       ---------> raw pdfs
│   ├── sovereignty/
│   │    └── ...       ---------> raw pdfs
│   └── technology/
│        └── ...       ---------> raw pdfs
└──

```

## Repo structure 

```
├── models/            ---------> w2v models
│    └── ...
├── src/                        
│   ├── application/
│   │    ├── query/                     ---------> json files with most similar uni-, bi-, trigrams for seed words
│   │    ├── extract_lemmas.py          ---------> pipeline for preprocessing (cleaning, lemmatization) .txt docs
│   │    ├── extract_text_from_pdfs.py  ---------> pdf parser based on pdf -> images -> text pipeline  
│   │    ├── pdf_parser.py              ---------> pdf parsering based on PDFResourceManager (all existing txt files are prepared with this pipeline)
│   │    ├── query_seeds.py             ---------> script for findings the most similar uni-, bi-, trigrams for seed words
│   │    ├── w2v_all_keys.py            ---------> pipeline for training w2v based on all folders
│   │    └── w2v_per_key.py             ---------> pipeline for training w2v per foder
│   │
│   └── ethics/ 
│        ├── parser.py        ---------> function for PDFResourceManager based parsering
│        └── preprocess.py    ---------> functions for cleaning, lemmatising and removing stop words from a doc
│
├── requirements.txt   ---------> packages required to run the scripts
│
└── stopwords.txt      ---------> list of English stopwords

```

## Usage 
The repo can be found under `/data_archive/eu-ethics-temp/`.

If does not exist then:  

```
cd /data_archive/eu-ethics-temp/

git clone https://github.com/centre-for-humanities-computing/AI-Ethics.git

cd AI-Ethics

pip install pip --upgrade

pip install requirements.txt
```

## Run unit tests

```
cd tests/

python -m  pytest
```