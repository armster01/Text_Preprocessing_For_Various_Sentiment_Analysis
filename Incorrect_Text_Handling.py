from textblob import TextBlob

incorrect_text = "ceertain conditionas duriing seceal ggeneratioons aree moodifieed in the saame maner"

textBlb = TextBlob(incorrect_text)
textBlb.correct().string
