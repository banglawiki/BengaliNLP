"""
Script for preparing Bengali data for LLM fine-tuning.
"""
import pandas as pd
import re
from bengalinlp.cleantext.clean import CleanText

def prepare_data(input_path, output_path):
    df = pd.read_csv(input_path)
    cleaner = CleanText()
    df['text'] = df['text'].apply(cleaner)
    # Additional preprocessing (e.g., dropna, deduplication)
    df = df.dropna(subset=['text'])
    df = df.drop_duplicates(subset=['text'])
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    prepare_data("./data/raw.csv", "./data/train.csv")
