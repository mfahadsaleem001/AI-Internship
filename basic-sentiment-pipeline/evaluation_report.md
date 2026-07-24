# Basic Sentiment Pipeline - Evaluation Report

## 1. Project Overview

Basic Sentiment Pipeline is an NLP-based project that analyzes text posts and predicts their sentiment. The system performs text cleaning, keyword extraction, and sentiment classification using Machine Learning techniques.

The purpose of this project is to build an automated pipeline that processes raw text data and generates meaningful insights from user posts.


## 2. Pipeline Workflow

The project follows an automated NLP processing pipeline:

1. Input Data Collection
   - Raw text posts are stored in a CSV file (`input_posts.csv`).

2. Text Cleaning
   - The raw text is cleaned using NLP preprocessing techniques.
   - Unnecessary words and punctuation are removed to prepare text for analysis.

3. Keyword Extraction
   - Important keywords are extracted from text using word frequency analysis.
   - The system identifies the most relevant words from each post.

4. Sentiment Classification
   - A Machine Learning model is trained using text examples.
   - CountVectorizer converts text into numerical features.
   - Decision Tree Classifier predicts sentiment as Positive or Negative.

5. Output Generation
   - The processed results are stored in `output_dataset.csv`.
   - The output contains cleaned text, extracted keywords, and predicted sentiment.


## 3. Technologies and Libraries Used

### Programming Language
- Python

### NLP Libraries
- NLTK
  - Tokenization
  - Stopwords removal
  - Text preprocessing

### Machine Learning Libraries
- Scikit-learn
  - CountVectorizer
  - DecisionTreeClassifier

### Data Processing
- Pandas
  - CSV reading
  - Data processing
  - Output generation

### Model Saving
- Joblib
  - Saving trained model
  - Saving vectorizer


## 4. Dataset Description

The project uses a CSV-based dataset containing text posts.

Input Dataset:

File Name:
`input_posts.csv`

Columns:
- id
- post

Example:

| id | post |
|----|------|
| 1 | I love this AI project |
| 2 | This code has many bugs |


Output Dataset:

File Name:
`output_dataset.csv`

Columns:
- id
- post
- cleaned_text
- keywords
- sentiment


## 5. Machine Learning Model

The sentiment classification model uses:

Model:
Decision Tree Classifier

Feature Extraction:
CountVectorizer

Process:

Raw Text  
↓  
Text Vectorization  
↓  
Machine Learning Model  
↓  
Sentiment Prediction


The model was trained using positive and negative example sentences.


## 6. Results

The pipeline successfully processed input text data and generated sentiment predictions.

Example Results:

| Post | Predicted Sentiment |
|------|---------------------|
| I love this AI project | Positive |
| This code has many bugs | Negative |
| Python is amazing for machine learning | Positive |
| The project is excellent | Positive |


The system successfully performed:
- Text cleaning
- Keyword extraction
- Sentiment prediction
- CSV output generation


## 7. Limitations

- The sentiment model was trained on a small dataset.
- A larger dataset can improve prediction accuracy.
- The current model supports only Positive and Negative sentiments.
- More advanced NLP models can provide better results.


## 8. Future Improvements

Possible improvements:

- Use a larger real-world dataset.
- Add Neutral sentiment classification.
- Use advanced NLP models like BERT.
- Create a web interface using Flask or FastAPI.
- Add real-time social media data collection.
- Improve model evaluation using accuracy, precision, recall, and F1-score.


## 9. Conclusion

Basic Sentiment Pipeline successfully demonstrates an end-to-end NLP workflow.

The project combines text preprocessing, keyword extraction, and machine learning-based sentiment analysis into an automated pipeline that converts raw text data into meaningful insights.