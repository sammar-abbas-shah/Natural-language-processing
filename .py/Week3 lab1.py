import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = 'The hospital is preparing to launch new health programs. The goal is to improve patient care and provide advanced facilities for people in remote areas.'

stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
filtered = [w for w in words if w.lower() not in stop_words]

print("Original:", text)
print("After stopwords removal:", filtered)
