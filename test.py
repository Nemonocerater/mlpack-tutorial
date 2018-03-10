
from nltk import word_tokenize, pos_tag

sentence = "And now for something completely different."
text = word_tokenize(sentence)
nltk.pos_tag(text)
