"""
Stopword removal utility for Bengali NLP.
"""

from bengalinlp.corpus._stopwords import bengali_stopwords


def remove_stopwords(text, custom_stopwords=None):
    """
    Remove Bengali stopwords from a string.
    Args:
        text (str): Input text.
        custom_stopwords (set or list, optional): Additional stopwords.
    Returns:
        str: Text with stopwords removed.
    """
    stopwords = set(bengali_stopwords)
    if custom_stopwords:
        stopwords.update(custom_stopwords)
    tokens = text.split()
    filtered = [word for word in tokens if word not in stopwords]
    return " ".join(filtered)


class BengaliStopwordRemover:
    def __init__(self, custom_stopwords=None):
        self.stopwords = set(bengali_stopwords)
        if custom_stopwords:
            self.stopwords.update(custom_stopwords)

    def __call__(self, text):
        tokens = text.split()
        filtered = [word for word in tokens if word not in self.stopwords]
        return " ".join(filtered)
