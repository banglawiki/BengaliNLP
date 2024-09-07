# Bengali Natural Language Processing(BengaliNLP)

[![PyPI version](https://img.shields.io/pypi/v/bengalinlp)](https://pypi.org/project/bengalinlp/)
<a href="https://pypi.org/project/readyapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/readyapi.svg?color=%2334D058" alt="Supported Python versions">
</a>

BengaliNLP is a natural language processing toolkit for Bengali Language. This tool will help you to **tokenize Bengali text**, **Embedding Bengali words**, **Embedding Bengali Document**, **Bengali POS Tagging**, **Bengali Name Entity Recognition**, **Bangla Text Cleaning** for Bengali NLP purposes.


## Features
- Tokenization
   - [Basic Tokenizer](./docs/README.md#basic-tokenizer)
   - [NLTK Tokenizer](./docs/README.md#nltk-tokenization)
   - [Sentencepiece Tokenizer](./docs/README.md#bengali-sentencepiece-tokenization)
- Embeddings
   - [Word2vec embedding](./docs/README.md#bengali-word2vec)
   - [Fasttext embedding](./docs/README.md#bengali-fasttext)
   - [Glove Embedding](./docs/README.md#bengali-glove-word-vectors)
   - [Doc2vec Document embedding](./docs/README.md#document-embedding)
- Part of speech tagging
   - [CRF-based POS tagging](./docs/README.md#bengali-crf-pos-tagging)
- Named Entity Recognition
   - [CRF-based NER](./docs/README.md#bengali-crf-ner)
- [Text Cleaning](./docs/README.md#text-cleaning)
- [Corpus](./docs/README.md#bengali-corpus-class)
   - Letters, vowels, punctuations, stopwords

## Installation

### PIP installer

  ```
  pip install bengalinlp
  ```
  **or Upgrade**

  ```
  pip install -U bengalinlp
  ```
  - Python: 3.8, 3.9, 3.10, 3.11
  - OS: Linux, Windows, Mac

### Build from source
```
git clone https://github.com/banglawiki/bengalinlp.git
cd bengalinlp
python setup.py install
```

## Sample Usage

```py
from bengalinlp import BasicTokenizer

tokenizer = BasicTokenizer()

raw_text = "আমি বাংলায় গান গাই।"
tokens = tokenizer(raw_text)
print(tokens)
# output: ["আমি", "বাংলায়", "গান", "গাই", "।"]
```
