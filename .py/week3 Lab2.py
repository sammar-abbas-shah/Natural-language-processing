import nltk
import string
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Download required resources
for res in ('punkt', 'stopwords', 'omw-1.4', 'averaged_perceptron_tagger'):
    nltk.download(res, quiet=True)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def treebank_to_wordnet_pos(treebank_tag):
    if treebank_tag.startswith("J"):
        return wordnet.ADJ
    elif treebank_tag.startswith("V"):
        return wordnet.VERB
    elif treebank_tag.startswith("N"):
        return wordnet.NOUN
    elif treebank_tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN
def preprocess(text, remove_stopwords=True, remove_punkt=True, do_lemmatization=True):
    tokens = word_tokenize(text)  # tokenize first

    # remove punctuation
    if remove_punkt:
        tokens = [t for t in tokens if t not in string.punctuation]

    # remove stopwords
    if remove_stopwords:
        tokens = [t for t in tokens if t.lower() not in stop_words]

    # lemmatization
    if do_lemmatization:
        from nltk import pos_tag
        pos_tags = pos_tag(tokens)  # get POS tags
        tokens = [lemmatizer.lemmatize(t.lower(), treebank_to_wordnet_pos(pos))
                  for t, pos in pos_tags]

    return tokens


