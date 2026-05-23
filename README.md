# 🗣️ Natural Language Processing — Fifth Semester Academic Repository

> **By [Sammar Abbas](https://www.linkedin.com/in/sammar-abbas-372359289)**  
> 📧 [sammarabbas0619@gmail.com](mailto:sammarabbas0619@gmail.com)  
> 🔗 [LinkedIn](https://www.linkedin.com/in/sammar-abbas-372359289) | 💻 [GitHub](https://github.com/sammar-abbas-shah/Natural-language-processing)

---

## 📌 About This Repository

This repository contains all the work completed by **Sammar Abbas** during the **Natural Language Processing (NLP)** course in her **Fifth Semester**. It covers core NLP concepts from basic text preprocessing to deep learning-based language models — implemented through Python scripts and Jupyter Notebooks.

The repository is organized into three sections: the **Emotion Detector Project** (the main semester deliverable), a **Jupyter Notebook** folder with lab exercises, and a **.py** folder with weekly lab scripts.

---

## 📁 Repository Structure

```
Natural-language-processing/
│
├── Emotion Detector Project/     ← 🌟 Main semester project
│   ├── Final.py                  ← Complete Tkinter desktop application
│   ├── out 1.png                 ← Screenshot of app output
│   ├── out2.png                  ← Screenshot of app output
│   └── out3.png                  ← Screenshot of app output
│
├── jupyter notebook/             ← Lab exercises (Jupyter)
│   ├── DFA.ipynb
│   ├── POS.ipynb
│   ├── count_vectorizer.ipynb
│   ├── sentiment analysis.ipynb
│   ├── sentiment_analysis.ipynb
│   ├── sentiment_classification_LSTM.ipynb
│   ├── series prediction.ipynb
│   ├── stopword removal.ipynb
│   ├── word prediction.ipynb
│   └── word_prediction_LSTM.ipynb
│
└── .py/                          ← Weekly lab scripts (Python)
    ├── Week3 lab1.py
    ├── week3 Lab2.py
    ├── wee4_lab2.py
    ├── week5.py
    ├── Week 12.py / Week12.py
    ├── Week 13.py / Week 13 lab 2.py / Week13.py
    ├── Week_14_Lab1.py
    ├── Week_14_Lab2.py
    ├── rough.py
    └── second.py
```

---

## 🌟 Main Project: Emotion Detector

> The `Emotion Detector Project/` folder is the **core deliverable** of this repository — a fully functional desktop application that detects emotions from user-typed text in real time.

### 🎯 Objective

Build a rule-based NLP application that analyzes any input text and identifies which of **20 distinct human emotions** it expresses, complete with confidence scores and visual breakdowns.

---

### 🧠 How It Works

The application is built entirely using **rule-based NLP** — no pre-trained ML model, no API. It uses three core linguistic components:

**1. Emotion Lexicon** — A hand-crafted dictionary mapping hundreds of words to one of 20 emotions, each with a weighted score indicating intensity. For example:
- `'ecstatic': 2.5` → strongly happy
- `'slightly sad': 0.5` → mildly sad
- `'furious': 2.5` → strongly angry

**2. Negation Handling** — Detects negation words (`not`, `never`, `don't`, `can't`, etc.) within a 3-word context window before any emotion keyword. When negation is found, it flips or reduces the emotion score. For example, `"not happy"` shifts score toward `sad`.

**3. Intensifiers & Diminishers** — Words like `very`, `extremely`, `absolutely` multiply emotion scores (up to ×2), while words like `slightly`, `barely`, `somewhat` reduce them (down to ×0.4).

---

### 💡 Emotions Detected (20 Total)

| Emotion | Emoji | Emotion | Emoji |
|---|---|---|---|
| Happy | 😊 | Sad | 😢 |
| Angry | 😠 | Fearful | 😨 |
| Surprised | 😲 | Love | ❤️ |
| Excitement | 🤩 | Boredom | 😴 |
| Confusion | 😵 | Curiosity | 🤔 |
| Relief | 😌 | Guilt | 😓 |
| Shame | 😳 | Jealousy | 😒 |
| Pride | 🦁 | Trust | 🤝 |
| Anticipation | 👀 | Calmness | 🧘 |
| Disgust | 🤢 | Neutral | 😐 |

---

### 🖥️ Application Features

The app is built with **Python's Tkinter** GUI library and includes:

- **Text input area** — Type any text to analyze
- **Main emotion display** — Shows the dominant emotion with its emoji and confidence percentage
- **20 emotion progress bars** — Color-coded horizontal bars showing the % score for every emotion simultaneously
- **Mixed emotion detection** — Detects when text carries contradictory feelings (e.g., "happy but sad")
- **Sentence-level analysis** — Breaks multi-sentence text into individual sentences and reports varying emotions across them
- **Details panel** — Explains which keywords triggered the detected emotion
- **Quick example buttons** — 20 pre-loaded example sentences, one per emotion, to test the app instantly
- **Clear button** — Resets all inputs and outputs

---

### 📸 Application Screenshots

The `out 1.png`, `out2.png`, and `out3.png` files in the project folder show the live application analyzing different text inputs with emotion bars and confidence scores displayed.

---

### 🛠️ Running the Project

```bash
# Install dependency (tkinter is built into Python standard library)
pip install nltk

# Run the app
python "Emotion Detector Project/Final.py"
```

---

## 📚 Lab Exercises

### Jupyter Notebooks (`jupyter notebook/`)

| Notebook | Topic |
|---|---|
| `DFA.ipynb` | Deterministic Finite Automaton (DFSA) implementation — accepts/rejects strings based on state transitions |
| `POS.ipynb` | Part-of-Speech tagging using NLTK — tokenization, lemmatization, stopword removal |
| `stopword removal.ipynb` | Text preprocessing — removing stopwords from sentences using NLTK |
| `count_vectorizer.ipynb` | Bag of Words representation using Scikit-learn's CountVectorizer and n-gram models |
| `sentiment analysis.ipynb` | Word2Vec embeddings with Gensim — finding word similarity and semantic vectors |
| `sentiment_analysis.ipynb` | Sentiment classification using LSTM — binary positive/negative classification |
| `sentiment_classification_LSTM.ipynb` | Extended LSTM sentiment classifier with Embedding + LSTM + Dense layers |
| `word prediction.ipynb` | Next-word prediction using LSTM trained on a short Islamabad-themed paragraph |
| `word_prediction_LSTM.ipynb` | LSTM-based word prediction on NLP-themed training text |
| `series prediction.ipynb` | Sequential number series prediction using LSTM with sliding window |

---

### Weekly Lab Scripts (`.py/`)

| File | Topic |
|---|---|
| `Week3 lab1.py` | Stopword removal using NLTK on a healthcare-themed sentence |
| `week3 Lab2.py` / `second.py` | POS tagging, lemmatization, regex pattern matching, DFSA |
| `wee4_lab2.py` | Additional text processing lab |
| `week5.py` | CountVectorizer — Bag of Words and n-gram (bigram, 4-gram, 10-gram) encoding |
| `rough.py` | Word2Vec on multiple datasets (sports, geography, food) + DFSA + regex experiments |
| `Week 12.py` / `Week12.py` | LSTM-based sentiment analysis with Embedding layer |
| `Week 13.py` / `Week 13 lab 2.py` / `Week13.py` | Advanced LSTM experiments |
| `Week_14_Lab1.py` | Word prediction using RNN + Word2Vec (Gensim) embeddings |
| `Week_14_Lab2.py` | Urdu-to-English sequence-to-sequence translation using LSTM encoder-decoder |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **NLP Libraries:** NLTK, Gensim (Word2Vec)
- **Deep Learning:** TensorFlow, Keras (LSTM, Embedding, Dense layers)
- **ML Utilities:** Scikit-learn (CountVectorizer)
- **GUI:** Tkinter
- **Notebooks:** Jupyter Notebook
- **Other:** `re` (regex), `collections`

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/sammar-abbas-shah/Natural-language-processing.git
cd Natural-language-processing

# Install dependencies
pip install nltk gensim tensorflow scikit-learn

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger'); nltk.download('wordnet')"

# Run the main project
python "Emotion Detector Project/Final.py"

# Or open any notebook
jupyter notebook "jupyter notebook/sentiment_classification_LSTM.ipynb"
```

---

## 👩‍💻 Author

**Sammar Abbas**  
Fifth Semester — Natural Language Processing

📧 Email: [sammarabbas0619@gmail.com](mailto:sammarabbas0619@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/sammar-abbas-372359289](https://www.linkedin.com/in/sammar-abbas-372359289)  
💻 GitHub: [github.com/sammar-abbas-shah](https://github.com/sammar-abbas-shah)

---

*This repository represents semester-long academic work exploring Natural Language Processing from foundational text preprocessing techniques to deep learning-based language models.*
