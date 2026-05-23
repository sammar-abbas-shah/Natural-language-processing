from gensim.models import Word2Vec

# Dataset 1
text = [
    ['cricket', 'is', 'a', 'popular', 'sport'],
    ['player', 'hit', 'the', 'ball', 'to', 'score', 'runs']
]
model = Word2Vec(text, vector_size=10, window=2, min_count=1)
a = model.wv['cricket']
print("Most similar to 'cricket':", model.wv.most_similar('cricket'))
print("Vector size =", a.shape)

# Dataset 2
SENTENCE = [
    ['king', 'queen', 'man', 'woman'],
    ['paris', 'france', 'tokyo', 'japan']
]
model2 = Word2Vec(SENTENCE, vector_size=10, window=2, min_count=1)
vector = model2.wv['king']
print("\nVector for 'king':\n", vector)

# Dataset 3
SEN2 = [
    ['i', 'love', 'eating', 'pizza'],
    ['pasta', 'and', 'burger', 'also', 'tasty']
]
model3 = Word2Vec(SEN2, vector_size=10, window=3, min_count=1)
# Note: 'pizza' may not have enough context for similarity, so this may warn or return few results
print("\nMost similar to 'pizza':", model3.wv.most_similar('pizza'))
print("Vector for 'pizza':\n", model3.wv['pizza'])

# Dataset 4
SEN3 = [
    ['teacher', 'explained', 'the', 'lesson', 'carefully'],
    ['students', 'listen', 'carefully', 'in', 'class']
]
model4 = Word2Vec(SEN3, vector_size=10, window=2, min_count=1)
vector5 = model4.wv['teacher']
print("\nVector for 'teacher':\n", vector5)
print("Vector shape for 'teacher':", vector5.shape)

# Dataset 5
cars = [
    ['cars', 'run', 'on', 'road'],
    ['and', 'airplanes', 'fly', 'in', 'the', 'sky']
]
model5 = Word2Vec(cars, vector_size=10, window=2, min_count=1)
print("\nMost similar to 'cars':", model5.wv.most_similar('cars'))
