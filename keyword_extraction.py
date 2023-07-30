import pandas as pd
import yake
from stopwords import Stopwords
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize

def get_keywords(text, top):
    lang = 'en'
    stopwords = Stopwords().stopwords

    custom_kw_extr = yake.KeywordExtractor(lan=lang, top=top, stopwords=stopwords)

    kws = custom_kw_extr.extract_keywords(text)
    df = pd.DataFrame(kws)

    df.rename({0:"keyword", 1:"value"}, axis=1, inplace=True)

    print(df)

    df['count'] = df['keyword'].apply(calculate_word_frequencies)

    return df



# Function to calculate word frequencies and return a Counter object
def calculate_word_frequencies(text):
    # Tokenize the text into words and multi-word phrases
    words = word_tokenize(text)

    # Use n-grams to consider multi-word phrases up to length 3
    n_grams = list(nltk.ngrams(words, 1)) + list(nltk.ngrams(words, 2)) + list(nltk.ngrams(words, 3))

    word_frequencies = Counter(n_grams)
    return word_frequencies


