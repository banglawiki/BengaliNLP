# -*- coding: utf-8 -*-import unittest
from bengalinlp.preprocessing.stopwords import remove_stopwords, BengaliStopwordRemover
from bengalinlp.preprocessing.stemming import stem_bengali_text, BengaliStemmer


class TestPreprocessing(unittest.TestCase):
    def test_stopword_removal(self):
        text = "আমি আজ স্কুলে যাবো এবং আমার বন্ধুদের সাথে দেখা করবো।"
        result = remove_stopwords(text)
        self.assertNotIn("আমি", result)
        remover = BengaliStopwordRemover()
        result2 = remover(text)
        self.assertNotIn("আমি", result2)

    def test_stemming(self):
        text = "ছেলেরা স্কুলে যায়"
        result = stem_bengali_text(text)
        self.assertIn("ছেলে", result)
        stemmer = BengaliStemmer()
        result2 = stemmer(text)
        self.assertIn("ছেলে", result2)


if __name__ == "__main__":
    unittest.main()
