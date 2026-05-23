from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Extended sample data for better training
text = [
    'I love this', 'This is amazing', 'I hate this', 'This is bad',
    'Great movie', 'Terrible experience', 'Fantastic work', 'Awful',
    'I really like it', 'Not good at all', 'Perfect', 'Disappointing'
]
labels = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # More examples
Y = np.array(labels)

# Tokenization
tokenizer = Tokenizer(num_words=1000, oov_token='<OOV>')  # Handle unknown words
tokenizer.fit_on_texts(text)
sequences = tokenizer.texts_to_sequences(text)
X = pad_sequences(sequences, maxlen=5)

print("Word Index:", tokenizer.word_index)
print("Training sequences:", sequences)

# Build model
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64, input_length=5),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

# Compile and train
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, Y, epochs=50, verbose=1)  # More epochs for small dataset

# Prediction on new text
test_text = ['I really hate this']  # Remove punctuation for better tokenization
test_seq = tokenizer.texts_to_sequences(test_text)
test_pad = pad_sequences(test_seq, maxlen=5)
prediction = model.predict(test_pad)

print('\nTest sequence:', test_seq)
print('Padded sequence:', test_pad)
print('Sentiment Score:', prediction[0][0])

# Interpretation
sentiment = "Positive" if prediction[0][0] > 0.5 else "Negative"
confidence = prediction[0][0] if prediction[0][0] > 0.5 else 1 - prediction[0][0]
print(f'Predicted Sentiment: {sentiment} (Confidence: {confidence:.2f})')