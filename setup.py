from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="bengalinlp",
    version="1.0.0",
    author="KhulnaSoft DevOps",
    author_email="info@khulnasoft.com",
    description="BengaliNLP is a natural language processing toolkit for Bengali Language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/banglawiki/bengalinlp",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "sentencepiece",
        "gensim",
        "nltk",
        "numpy>=1.18.5,<2.0",
        "scipy>=1.7.0,<1.14.0",
        "sklearn-crfsuite",
        "tqdm",
        "ftfy",
        "emoji",
        "requests",
    ],
    extras_require={
        "fasttext": ["fasttext"],
    },
)
