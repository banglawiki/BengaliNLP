"""
Bengali stemming utility (rudimentary rule-based version).
For advanced stemming, consider integrating Indic NLP Library.
"""
import re

_SUFFIXES = [
    "গুলো", "রা", "টি", "টা", "তে", "রা", "রা", "কে", "দের", "য়ের", "তে", "য়",
    "রা", "তে", "টা", "টি", "কে", "রা", "য়", "তে", "রা", "টা", "টি",
]

def stem_bengali_word(word):
    for suffix in sorted(_SUFFIXES, key=len, reverse=True):
        if word.endswith(suffix) and len(word) > len(suffix)+1:
            return word[:-len(suffix)]
    return word

def stem_bengali_text(text):
    tokens = text.split()
    return ' '.join(stem_bengali_word(token) for token in tokens)

class BengaliStemmer:
    def __call__(self, text):
        return stem_bengali_text(text)
