import pandas as pd
import nltk
import re
import math

from collections import Counter
from unicodedata import normalize
from nltk import ngrams

class CosineSimilarity:
    """
    Compare sentences using the Cosine Similarity 
    technique.
    """
    def __init__(self):
        self.regex_word = re.compile(r"\w+")
        self.ngram_token = 3

    def compare(self, sentence_a, sentence_b):
        """
        Calculate similarity between two disciplines taking
        their syllabus as parameter.
        """
        similarity = self._calc_sentence_similarity(sentence_a, sentence_b)
        return similarity

    def _normalize_text(self, text):
        """
        Normalize the text removing spaces and accents, so it can
        be better compared.
        """
        without_accents = normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII")
        without_extra_spaces = re.sub("\s+", " ", without_accents)
        return without_extra_spaces.lower().strip()

    def _calc_cosine_similarity(self, vector_a, vector_b):
        """
        Calculate the similarity based on both vectors' cosine
        """
        intersection = set(vector_a.keys()) & set(vector_b.keys())
        numerator = sum([vector_a[x] * vector_b[x] for x in intersection])

        sum_a = sum([vector_a[x] ** 2 for x in vector_a.keys()])
        sum_b = sum([vector_b[x] ** 2 for x in vector_b.keys()])

        denominator = math.sqrt(sum_a) * math.sqrt(sum_b)

        if not denominator:
            return 0.0
        else:
            coeficient = float(numerator) / denominator
            return coeficient if coeficient <= 1 else 1

    def _sentence_to_vector(self, sentence):
        """
        Create a vector based on the given sentence.
        """
        words = self.regex_word.findall(sentence)
        accumulator = []

        for n in range(1, self.ngram_token):
            gramas = ngrams(words, n)
            for grama in gramas:
                accumulator.append(str(grama))

        return Counter(accumulator)

    def _calc_sentence_similarity(self, sentence_a, sentence_b):
        """
        Calculate similarity between two sentences.
        """
        sentence_a = self._normalize_text(sentence_a)
        sentence_b = self._normalize_text(sentence_b)
        vector_a = self._sentence_to_vector(sentence_a)
        vector_b = self._sentence_to_vector(sentence_b)
        return self._calc_cosine_similarity(vector_a, vector_b)