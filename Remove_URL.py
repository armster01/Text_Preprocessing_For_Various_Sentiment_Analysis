import re
def remove_url (text):
  pattern = re.compile(r'https?://\s+|www\.\s+')
return pattern.sub(r '',text)
