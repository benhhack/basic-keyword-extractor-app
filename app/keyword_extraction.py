import pandas as pd
from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer

# from stopwords import Stopwords
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize

# https://towardsdatascience.com/enhancing-keybert-keyword-extraction-results-with-keyphrasevectorizers-3796fa93f4db


def get_keywords(text, top):

    # initalise default vectoriser
    vectorizer = KeyphraseCountVectorizer()

    # fit to text
    vectorizer.fit_transform([text])

    kw_model = KeyBERT()
    kw = kw_model.extract_keywords(docs=text, vectorizer=KeyphraseCountVectorizer())

    df = pd.DataFrame(kw)

    df.rename({0: "Keyword", 1: "Value"}, axis=1, inplace=True)

    freq = calculate_word_frequencies(text)
    # print(freq)
    df['Count'] = df['Keyword'].apply(lambda x: freq[x])
    print(df)

    return df


# Function to calculate word frequencies and return a Counter object
def calculate_word_frequencies(text):
    # Tokenize the text into words and multi-word phrases
    words = word_tokenize(text)

    # Use n-grams to consider multi-word phrases up to length 3
    n_grams = list(nltk.ngrams(words, 1)) + list(nltk.ngrams(words, 2)) + list(nltk.ngrams(words, 3))

    word_frequencies = Counter(n_grams)

    return {" ".join(i): word_frequencies[i] for i in word_frequencies}
