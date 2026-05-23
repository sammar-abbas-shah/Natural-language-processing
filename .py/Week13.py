from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

TEXT = ['I LOVE NATURAL LANGUAGE PROCESSING . I LOVE NEURAL NETWORKS.']
tokenizer = Tokenizer()
tokenizer.fit_on_texts(TEXT)

SEQ = tokenizer.texts_to_sequences(TEXT)[0]

x = []
y = []

for i in range(1, len(SEQ)):
    x.append(SEQ[:i])
    y.append(SEQ[i])

x = pad_sequences(x)
x, y = np.array(x), np.array(y)

MODEL = Sequential([Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=32)])
MODEL.add(LSTM(69))
MODEL.add(Dense(len(tokenizer.word_index)+1, activation='softmax'))
MODEL.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

MODEL.fit(x, y, epochs=200)

seed = "I LOVE"
seed_seq = tokenizer.texts_to_sequences([seed])[0]
seed_seq = pad_sequences([seed_seq], maxlen=x.shape[1])

pred = MODEL.predict(seed_seq, verbose=0).argmax()
print("Next Word is", tokenizer.index_word[pred])
