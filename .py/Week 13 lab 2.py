from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

text = "In the heart of Islamabad there are small cafe's that everyone love. The aroma of freshly coffee fill the air and the sound of soft jazz music create a relaxing atmosphere"
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
seq = tokenizer.texts_to_sequences([text])[0]
x = []  # for input
y = []  # for predicting output
for i in range(1, len(seq)):
    x.append(seq[:i])
    y.append(seq[i])
x = pad_sequences(x)
x, y = np.array(x), np.array(y)
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=32))
model.add(LSTM(128))
model.add(Dense(len(tokenizer.word_index)+1, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])  # Fixed duplicate 'loss' argument
model.fit(x, y, epochs=200, verbose=0)
seed = "In the heart of"
test = tokenizer.texts_to_sequences([seed])
test = pad_sequences(test, maxlen=x.shape[1])
pred = model.predict(test, verbose=0).argmax()
print("Next word: ", tokenizer.index_word[pred])  # Fixed: convert index back to word
