# WEEK 6 - MODERN AI MODELS
# Imports
from transformers import pipeline
from transformers import AutoTokenizer, AutoModel
import torch.nn.functional as F

# DAY 1 & DAY 2
# SENTIMENT ANALYSIS
classifier = pipeline("sentiment-analysis")
result = classifier("The movie was fantastic!")
print(result)

# TRANSLATION
translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-fr"
)

# Translate English → French
translation = translator("Python is the best programming language.")
print(translation[0]["translation_text"])

# SUMMARIZATION
# Load Summarization Model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

# Large article to summarize
article = """
Artificial Intelligence (AI) is one of the fastest-growing technologies in the world. It enables computers to perform tasks that normally require human intelligence, such as understanding language, recognizing images, making decisions, and solving problems. AI is widely used in healthcare to assist doctors in diagnosing diseases, in finance to detect fraud, in education to provide personalized learning experiences, and in transportation through self-driving vehicles. Machine Learning, a branch of AI, allows systems to learn from data and improve their performance over time without being explicitly programmed. Deep Learning uses artificial neural networks to process large amounts of information and achieve remarkable accuracy in tasks like speech recognition and image classification. As AI continues to evolve, it is transforming industries, creating new job opportunities, and improving the quality of life for millions of people. However, it also raises important ethical concerns regarding privacy, security, bias, and the responsible use of technology.
"""

# Generate summary
summary = summarizer(
    article,
    max_length=60,      # Maximum words/tokens in summary
    min_length=30,      # Minimum words/tokens in summary
    do_sample=False     # Deterministic output
)

print("\nOriginal Article:\n")
print(article)

print("\nSummary:\n")
print(summary[0]["summary_text"])

# DAY 3
# TRANSFORMERS & EMBEDDINGS
tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2"
)

model = AutoModel.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# INPUT SENTENCES
sentence1 = "I love Artificial Intelligence."
sentence2 = "Artificial Intelligence is amazing."

# TOKENIZATION
inputs1 = tokenizer(
    sentence1,
    return_tensors="pt"
)
inputs2 = tokenizer(
    sentence2,
    return_tensors="pt"
)
print(inputs1)
print(inputs2)

# GENERATE EMBEDDING FOR SENTENCE 1
outputs1 = model(**inputs1)
print(outputs1)

sentence_embedding1 = outputs1.pooler_output
print(sentence_embedding1)

# GENERATE EMBEDDING FOR SENTENCE 2
outputs2 = model(**inputs2)
print(outputs2)

sentence_embedding2 = outputs2.pooler_output
print(sentence_embedding2)

# COSINE SIMILARITY
similarity = F.cosine_similarity(
    sentence_embedding1,
    sentence_embedding2
)

print(similarity)

# Day 4
# Question Answering using Transformers

qa_pipeline = pipeline("question-answering")
qa_result = qa_pipeline(
    question="Who created Python?",
    context="Python is a programming language created by Guido van Rossum in 1991."
)

print(qa_result["answer"])

#Semantic Search using Transformers
sentences = [
    "I Learn Python",
    "Artificial Intelligence is changing the world",
    "I play cricket",
    "I like Food",
    "I travel to Sahiwal"
            ]

query = "Machine Learning"
query_inputs = tokenizer(query, return_tensors="pt")
query_outputs = model(**query_inputs)
query_embedding = query_outputs.pooler_output
print(query_embedding)

best_score = -1
best_sentence = ""

for sentence in sentences:
    sentence_inputs = tokenizer(sentence, return_tensors="pt")
    sentence_outputs = model(**sentence_inputs)
    sentence_embedding = sentence_outputs.pooler_output
    
    similarity = F.cosine_similarity(
    query_embedding,
    sentence_embedding
    )
    
    print(f"{sentence} -> {similarity.item():.4f}")
    
    score = similarity.item()

    if score > best_score:
        best_score = score
        best_sentence = sentence
        
print("\nBest Match:")
print(best_sentence)

print("\nSimilarity Score:")
print(best_score)

# Day 5
# Text Generation
generator = pipeline("text-generation", model="gpt2")

generated_result = generator(
    "Artificial Intelligence is transforming the future because",
    max_new_tokens=100
)

print(generated_result[0]["generated_text"])