# Word Tokenization
sent_1 = "I am going to Delhi"
sent_1.split()

# Using RE
import re #Regular Expression
sent_2 = "I am going to Delhi"
tokens = re.findall("[\w] + ",sent_2)
tokens

# Using NLTK
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt')

sent_3 = "I am going to Delhi"
word_tokenize(sent_3)
