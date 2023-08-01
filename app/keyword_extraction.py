import pandas as pd
from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer

from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
stopword = nltk.corpus.stopwords.words('english')

# https://towardsdatascience.com/enhancing-keybert-keyword-extraction-results-with-keyphrasevectorizers-3796fa93f4db


def get_keywords(text, top):


    kw_model = KeyBERT()
    kws = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), use_maxsum=True, stop_words=stopword, top_n=top)

    df = pd.DataFrame(kws)

    df.rename({0: "Keyword", 1: "Value"}, axis=1, inplace=True)

    df.sort_values(by=["Value"], ascending=False, inplace=True)

    # freq = calculate_word_frequencies(text)
    # # print(freq)
    # df['Count'] = df['Keyword'].apply(lambda x: freq[x])
    # print(df)

    return df


# Function to calculate word frequencies and return a Counter object
def calculate_word_frequencies(text):
    # Tokenize the text into words and multi-word phrases
    words = word_tokenize(text)

    # Use n-grams to consider multi-word phrases up to length 3
    n_grams = list(nltk.ngrams(words, 1)) + list(nltk.ngrams(words, 2)) + list(nltk.ngrams(words, 3))

    word_frequencies = Counter(n_grams)

    return {" ".join(i): word_frequencies[i] for i in word_frequencies}
