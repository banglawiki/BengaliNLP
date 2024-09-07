__version__ = "2.0.0"

import os
from bengalinlp.tokenizer.basic import BasicTokenizer
from bengalinlp.tokenizer.nltk import NLTKTokenizer
from bengalinlp.tokenizer.sentencepiece import (
    SentencepieceTokenizer,
    SentencepieceTrainer,
)

from bengalinlp.embedding.word2vec import (
    BengaliWord2Vec,
    Word2VecTraining,
)
from bengalinlp.embedding.glove import BengaliGlove

from bengalinlp.embedding.doc2vec import (
    BengaliDoc2vec,
    BengaliDoc2vecTrainer,
)

from bengalinlp.token_classification.pos import BengaliPOS
from bengalinlp.token_classification.ner import BengaliNER
from bengalinlp.token_classification.token_classification_trainer import (
    CRFTaggerTrainer,
)

from bengalinlp.cleantext.clean import CleanText

from bengalinlp.corpus.corpus import BengaliCorpus
