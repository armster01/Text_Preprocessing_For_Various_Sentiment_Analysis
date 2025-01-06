import re
def remove_emoji(text):
  emoji_pattern = re.compile("["
                             "\U0001F600-\U0001F64F"
                             #These are nothing but the emojis id available in google for several types of emojis
                             #Removing these helps in making the text clear and accurate form emojis to be ready for processed
                             "]+",flags=re.UNICODE)

  return emoji_pattern.sub(r " ",text)

# This code is given to make sure that python understand emojis
!pip install emoji

import emoji
print(emoji.demojize('python is 🔥'))
# This would give:- Python is : Fire
