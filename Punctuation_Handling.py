import string, time
string.punctuation

exclude = string.punctuation
exclude

def remove_punc(text):
  for char in exclude:
    text = text.replace(char,'')
return text
