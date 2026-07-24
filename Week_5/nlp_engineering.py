# ============================================
# Week 5 - NLP Engineering
# AI Internship
# ============================================

import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.util import bigrams, trigrams
from sklearn.feature_extraction.text import CountVectorizer

punctuations = string.punctuation

# ============================================
# Topic 1: Tokenization
# ============================================

word_sentence = "Python, AI and NLP are amazing."
paragraph = "I love AI. I play Cricket. I watch Cricket"

word_tokens = word_tokenize(word_sentence)
sentence_tokens = sent_tokenize(paragraph)

print("Word Tokens:", word_tokens)
print("Sentence Tokens:", sentence_tokens)

# ============================================
# Topic 2: Stopwords Removal
# ============================================

text = "the cat is sleeping on bed."

important_words = []
clean_words = []

stop_words = stopwords.words("english")
text_words = word_tokenize(text)

for word in text_words:
    if word not in stop_words:
        important_words.append(word)

for word in important_words:
    if word not in punctuations:
        clean_words.append(word)

print("\nText Words:", text_words)
print("Important Words:", important_words)
print("Clean Words:", clean_words)
print("Total Stopwords:", len(stop_words))

# ============================================
# Topic 3: Keyword Extraction
# ============================================

important_words = []
clean_words = []
frequency = {}

top_keyword = ""
highest_count = 0

text = "AI is amazing. AI is powerful. I love AI. Python helps in AI."
text = text.lower()

text_words = word_tokenize(text)

for word in text_words:
    if word not in stop_words:
        important_words.append(word)

for word in important_words:
    if word not in punctuations:
        clean_words.append(word)

for word in clean_words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

for word, count in frequency.items():
    if count > highest_count:
        highest_count = count
        top_keyword = word

print("\nFrequency Dictionary:", frequency)
print("Top Keyword:", top_keyword)
print("Highest Count:", highest_count)

# ============================================
# Topic 4: Stemming
# ============================================

stemmer = PorterStemmer()

word = "playing"
stemmed_word = stemmer.stem(word)

print("\nStemmed Word:", stemmed_word)

# ============================================
# Topic 5: Lemmatization
# ============================================

lemmatizer = WordNetLemmatizer()

word = "better"
lemmatized_word = lemmatizer.lemmatize(word, pos="a")

print("Lemmatized Word:", lemmatized_word)

# ============================================
# Topic 6: N-Grams
# ============================================

sentence = "I love learning NLP"

text_words = word_tokenize(sentence)

print("\nText Words:", text_words)

# Unigrams
print("Unigrams:", text_words)

# Bigrams
bigram_list = list(bigrams(text_words))
print("Bigrams:", bigram_list)

# Trigrams
trigram_list = list(trigrams(text_words))
print("Trigrams:", trigram_list)

# ============================================
# Topic 7: Bag of Words (CountVectorizer)
# ============================================

sentences = [
    "I am Software Engineer",
    "I love Python",
    "I learn AI"
]

vectorizer = CountVectorizer()

vectorizer.fit(sentences)

bow_matrix = vectorizer.transform(sentences)

print("\nBag of Words Matrix (Sparse):")
print(bow_matrix)

print("\nBag of Words Matrix:")
print(bow_matrix.toarray())

print("\nVocabulary:")
print(vectorizer.get_feature_names_out())