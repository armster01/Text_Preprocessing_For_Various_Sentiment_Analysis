from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
def stem_words(text):
  retrun " ".json([ps.stem(word) for word in text.split()])

sample = "Walk Walks Walking Walked"
stem_words(sample)
