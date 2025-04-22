# BengaliNLP

A modular, extensible toolkit for Bengali Natural Language Processing (NLP) with classic and LLM-based pipelines.

## Features
- Text normalization & cleaning
- Tokenization (basic, NLTK, SentencePiece)
- Stopword removal
- Stemming/lemmatization
- POS tagging & NER (pretrained models)
- Embeddings & LLM integration (HuggingFace Transformers)
- Utilities & evaluation metrics
- Example scripts and notebooks
- Unit tests

## Example Pipeline Usage
```python
from bengalinlp.cleantext.clean import CleanText
from bengalinlp.tokenizer.basic import word_tokenize
from bengalinlp.preprocessing.stopwords import remove_stopwords
from bengalinlp.preprocessing.stemming import stem_bengali_text

text = "আমি আজ স্কুলে যাবো এবং আমার বন্ধুদের সাথে দেখা করবো।"
cleaned = CleanText()(text)
tokens = word_tokenize(cleaned)
filtered = remove_stopwords(' '.join(tokens))
stemmed = stem_bengali_text(filtered)
print(stemmed)
```

## LLM Fine-tuning & Inference
See scripts in `bengalinlp/scripts/` for training and inference with HuggingFace Transformers.

### mT5 for Bengali NLP
You can use the mT5 model for Bengali-to-English translation, summarization, and other sequence-to-sequence tasks. Example:

```python
from bengalinlp.scripts.mt5_inference import mt5_generate

bengali_text = "আমি স্কুলে যাচ্ছি।"
translation = mt5_generate(bengali_text, task_prefix="translate Bengali to English: ")
print("Translation:", translation)
```

Or run the script directly:
```bash
python bengalinlp/scripts/mt5_inference.py
```

## Testing
Run unit tests with:
```bash
python -m unittest discover bengalinlp/tests
```

## License
MIT
