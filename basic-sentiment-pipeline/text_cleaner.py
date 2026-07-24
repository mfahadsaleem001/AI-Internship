import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

punctuations = string.punctuation

def clean_text(text):
    text = text.lower()
    text_words = word_tokenize(text)
    important_words = []
    clean_words = []
    
    stop_words = stopwords.words("english") 
    
    for word in text_words:
        if word not in stop_words:
            important_words.append(word)
            
    for word in important_words:
        if word not in punctuations:
            clean_words.append(word)
    return clean_words