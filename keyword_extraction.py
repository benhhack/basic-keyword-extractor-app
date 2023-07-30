import pandas as pd
import yake
from stopwords import Stopwords

def get_keywords(text, top):
    lang = 'en'
    stopwords = Stopwords().stopwords

    custom_kw_extr = yake.KeywordExtractor(lan=lang, top=top, stopwords=stopwords)

    kws = custom_kw_extr.extract_keywords(text)
    df = pd.DataFrame(kws)

    df.rename({0:"keyword", 1:"value"})
    return df





