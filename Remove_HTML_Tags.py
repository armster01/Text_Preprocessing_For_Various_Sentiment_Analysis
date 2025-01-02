import re #Regular Expression
def remove_html_tags(text):
  pattern = re.compile('<.*?>')
  return pattern.sub(r '' , text)

df['review']=df['review'].apply(remove_html_tags)
