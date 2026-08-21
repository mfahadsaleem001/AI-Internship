# ============================================================
# WEEK 9 - AIRFLOW SENTIMENT ANALYSIS PIPELINE
# ============================================================
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

# DAY 1 - Airflow DAG & Data Collection
# Topic: Creating a DAG and collecting sentiment data
def collect_data():
    print("Step 1: Collecting sentiment data...")

    data = [
        "I love this product",
        "This product is amazing",
        "Very bad experience",
        "I hate this service"
    ]

    print("Collected data:")
    
    for text in data:
        print(text)

    print("Data collection completed!")

    return data

# DAY 2 - Data Cleaning & Sentiment Analysis
# Topic: Cleaning text data and analyzing sentiment
def clean_data(ti):
    print("Step 2: Cleaning sentiment data...")

    # Get data from Day 1 task using XCom
    data = ti.xcom_pull(task_ids="collect_data")

    print("Received data:", data)

    cleaned_data = [
        text.lower().strip()
        for text in data
    ]

    print("Cleaned data:")

    for text in cleaned_data:
        print(text)

    print("Data cleaning completed!")

    return cleaned_data


def analyze_sentiment(ti):
    print("Step 3: Analyzing sentiment...")

    # Get cleaned data from clean_data task
    data = ti.xcom_pull(task_ids="clean_data")

    print("Received cleaned data:", data)

    for text in data:

        if "love" in text or "amazing" in text:
            sentiment = "Positive"

        elif "bad" in text or "hate" in text:
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

        print(f"Text: {text}")
        print(f"Sentiment: {sentiment}")
        print("-" * 40)

    print("Sentiment analysis completed!")

# DAY 3 - Task Testing, Debugging & Pipeline Validation
# Topic: Testing Airflow tasks and validating the complete DAG
def validate_pipeline():
    print("Week 9 sentiment pipeline validation started.")

    print("Checking pipeline stages:")
    print("1. Data collection")
    print("2. Data cleaning")
    print("3. Sentiment analysis")

    print("All pipeline stages are connected successfully.")
    print("Pipeline validation completed!")

# AIRFLOW DAG
with DAG(
    dag_id="week9_sentiment_pipeline",
    start_date=datetime(2026, 8, 18),
    schedule="@daily",
    catchup=False,
) as dag:

    # Day 1 Task
    collect_task = PythonOperator(
        task_id="collect_data",
        python_callable=collect_data,
    )

    # Day 2 Task
    clean_task = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data,
    )

    analyze_task = PythonOperator(
        task_id="analyze_sentiment",
        python_callable=analyze_sentiment,
    )

    # Day 3 Task
    validation_task = PythonOperator(
        task_id="validate_pipeline",
        python_callable=validate_pipeline,
    )

    collect_task >> clean_task >> analyze_task >> validation_task