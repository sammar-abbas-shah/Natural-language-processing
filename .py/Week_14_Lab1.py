import tensorflow as tf
from gensim.models import Word2Vec
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
import numpy as np

Sentences = ('I love food', 'I love coding', 'you love pizza', 'They play cricket')
tokenizer = Tokenizer(lower=True)  # avoid case issues
tokenizer.fit_on_texts(Sentences)
word_index = tokenizer.word_index

x = []
y = []
for sentence in Sentences:
    words = sentence.lower().split()
    for i in range(len(words) - 1):
        x.append(word_index[words[i]])
        y.append(word_index[words[i+1]])

x = np.array(x)
x = x.reshape(-1, 1)  # ← ADD THIS: (samples,) → (samples, 1)
y = to_categorical(y, num_classes=len(word_index) + 1)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(word_index) + 1, output_dim=10),
    tf.keras.layers.SimpleRNN(20),
    tf.keras.layers.Dense(len(word_index) + 1, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(x, y, epochs=200)