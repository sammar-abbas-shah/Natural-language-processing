from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

text5 = [
    "I absolutely loved the movie, The storyline was amazing, The acting was brilliant and the visuals were stunning",
    "This product is amazing. I have been using it for weeks and it still works perfectly with no issues at all.",
    "I really hated the experience. The staff was rude and the overall environment felt uncomfortable",
    "This was the worst purchase I hve ever made. It stopped working after one day and customer support was not helpful."
]

labels = [1, 1, 0, 0]

tokenizer = Tokenizer(oov_token="<OOV>") 
tokenizer.fit_on_texts(text5)

X1 = tokenizer.texts_to_sequences(text5)
X1 = pad_sequences(X1, maxlen=20)
Y1 = np.array(labels)

model9 = Sequential()
model9.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=32, input_length=20))
model9.add(LSTM(64))
model9.add(Dense(1, activation='sigmoid'))


model9.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model9.fit(X1, Y1, epochs=169)


text_text1 = ["I really enjoyed the movie because the story was emotional, the characters felt real, and the ending was beautifully done."]
seq = tokenizer.texts_to_sequences(text_text1)
text_seq1 = pad_sequences(seq, maxlen=20)

prediction = model9.predict(text_seq1)
print("Sentiment (1 = positive, 0 = negative):", prediction[0][0])