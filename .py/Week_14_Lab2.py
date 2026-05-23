from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# -------- DATA --------
ur = ["میں سیب کھاتا ہوں", "میں پانی پیتا ہوں"]
en = ["start I eat apples end", "start I drink water end"]

# -------- TOKENIZE --------
u_tok = Tokenizer(); u_tok.fit_on_texts(ur)
e_tok = Tokenizer(); e_tok.fit_on_texts(en)
u_seq = pad_sequences(u_tok.texts_to_sequences(ur))
e_seq = pad_sequences(e_tok.texts_to_sequences(en))

# -------- MODEL --------
enc_in = Input(shape=(None,))
dec_in = Input(shape=(None,))
enc_emb = Embedding(len(u_tok.word_index)+1, 64)(enc_in)
dec_emb = Embedding(len(e_tok.word_index)+1, 64)(dec_in)
enc_out, h, c = LSTM(64, return_state=True)(enc_emb)
dec_out = LSTM(64, return_sequences=True)(dec_emb, initial_state=[h, c])
out = Dense(len(e_tok.word_index)+1, activation='softmax')(dec_out)
model = Model([enc_in, dec_in], out)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# -------- PREPARE DECODER TARGETS --------
y = pad_sequences([seq[1:] for seq in e_seq], maxlen=e_seq.shape[1])
y = np.expand_dims(y, -1)  # 3D for sparse_categorical_crossentropy

# -------- TRAIN --------
model.fit([u_seq, e_seq], y, epochs=500, verbose=0)

# -------- SIMPLE TRANSLATE FUNCTION --------
def translate(sentence):
    seq = pad_sequences(u_tok.texts_to_sequences([sentence]), maxlen=u_seq.shape[1])
    dec_seq = np.array([[e_tok.word_index['start']]])
    for _ in range(e_seq.shape[1]):
        pred = model.predict([seq, dec_seq], verbose=0)
        next_word = np.argmax(pred[0, -1])
        if next_word == e_tok.word_index['end']: break
        dec_seq = np.hstack([dec_seq, [[next_word]]])
    return ' '.join([e_tok.index_word[i] for i in dec_seq[0] if i not in [0, e_tok.word_index['start']]])

# -------- TEST --------
print(translate("میں پانی پیتا ہوں"))