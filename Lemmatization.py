import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
wordnet_lemmatizer = WordNetLemmatizer()

sentence = "He was running and eating at same time."
punctuations = "?:!.,;"
sentence_words = nltk.word_tokenize(sentence)

for word in sentence_words:
  if word in punctuations:
    sentence_words.remove(word)

sentence_words
print("{0:20}{1:20}",format("word","Lemma"))
for word in sentence_words:
  print("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word,pos='v')))
    
