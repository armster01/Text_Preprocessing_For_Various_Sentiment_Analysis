from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

stopwords.words('english')

def remove_stopwords(text):
  new_text=[]
  for words in text.split():
    if word in stopwords.words('english'):
      new_text.append('')
    else:
      new_text.append(word)
x=new_text[:]
new_text.cleaar()
return " ".json(x)

df['review'].apply(remove_stopwords)
