from wordcloud import STOPWORDS
from wordcloud import WordCloud
import nltk
stopword = nltk.corpus.stopwords.words('english')


def make_cloud(text):
    # Create a word cloud
    # instantiate wordcloud
    wordcloud = WordCloud(
        stopwords=STOPWORDS,
        width=900,
        height=400,
        background_color="#F9F9FA",
        colormap="viridis",
        collocations=True,
        regexp=r"[a-zA-z#&]+",
        max_words=30,
        min_word_length=2,
        font_path="assets/Arial Unicode.ttf"
    )
    return wordcloud.generate(text).to_image()






