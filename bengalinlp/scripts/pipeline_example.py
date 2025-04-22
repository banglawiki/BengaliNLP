"""
Example Bengali NLP pipeline script.
"""

from bengalinlp.cleantext.clean import CleanText
from bengalinlp.tokenizer.basic import word_tokenize
from bengalinlp.preprocessing.stopwords import remove_stopwords
from bengalinlp.preprocessing.stemming import stem_bengali_text

# Add POS/NER imports as needed


def run_pipeline(text):
    # 1. Clean and normalize
    cleaner = CleanText()
    cleaned = cleaner(text)
    # 2. Tokenize
    tokens = word_tokenize(cleaned)
    # 3. Stopword removal
    filtered = remove_stopwords(" ".join(tokens))
    # 4. Stemming
    stemmed = stem_bengali_text(filtered)
    # 5. Further processing (POS/NER/LLM inference)
    # ...
    return stemmed


if __name__ == "__main__":
    sample = "আমি আজ স্কুলে যাবো এবং আমার বন্ধুদের সাথে দেখা করবো।"
    result = run_pipeline(sample)
    print("Pipeline output:", result)
