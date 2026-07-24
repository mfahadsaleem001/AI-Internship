# Basic Sentiment Pipeline

An NLP-based sentiment analysis pipeline that processes raw text data, extracts important keywords, and predicts sentiment using Machine Learning.


## Project Overview

Basic Sentiment Pipeline is an automated Natural Language Processing (NLP) project that analyzes text posts and classifies them into Positive or Negative sentiments.

The system performs:
- Text cleaning
- Keyword extraction
- Sentiment classification
- CSV output generation


## Features

✅ Text preprocessing using NLP techniques  
✅ Stopwords and punctuation removal  
✅ Keyword extraction using frequency analysis  
✅ Sentiment prediction using Machine Learning  
✅ Automated CSV processing pipeline  
✅ Output dataset generation  


## Technologies Used

### Programming Language
- Python

### Libraries

- Pandas
- NLTK
- Scikit-learn
- Joblib



## How To Run

### 1. Install Required Libraries

```bash
pip install pandas nltk scikit-learn joblib
````

### 2. Run Pipeline

```bash
python pipeline.py
```

### 3. Output

After successful execution, the system generates:

```
output_dataset.csv
```

containing:

* Cleaned text
* Extracted keywords
* Predicted sentiment

## Example Output

| Post                    | Sentiment |
| ----------------------- | --------- |
| I love this AI project  | Positive  |
| This code has many bugs | Negative  |

## Future Improvements

* Train model on larger datasets
* Add Neutral sentiment class
* Use advanced NLP models like BERT
* Add web interface using Flask/FastAPI
* Connect real-time social media data

## Author
Muhammad Fahad Saleem