chat_words ={
  "ASAP":"As Soon As Possible",
  "LOL":"Laugh Out Loud",
  "BTW":"By The Way"
}
  # You can add more if you want to 
  # Higher the number of chat words, higher the accuracy

def chat_conversion(text):
  new_text =[]
  for w in text.split():
    if w.upper() in chat_words:
      new_text.append(chat_words[w.upper()])
    else:
      new_text.append(w)
  return " ".join(new_text)
