from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

# WEEK 9 - SENTIMENT ANALYSIS PIPELINE
# DAY 1 - Airflow DAG & Data Collection
def collect_data():
    print("Step 1: Collecting sentiment data...")

    data = [
        "I love this product",
        "This product is amazing",
        "Very bad experience",
        "I hate this service"
    ]

    print("Data collection completed!")

    return data


# DAY 2 - Data Cleaning & Sentiment Analysis

def clean_data(ti):
    print("Step 2: Cleaning sentiment data...")

    data = ti.xcom_pull(task_ids="collect_data")

    print("Received data:", data)

    cleaned_data = [text.lower() for text in data]

    print("Cleaned data:", cleaned_data)
    print("Data cleaning completed!")

    return cleaned_data


def analyze_sentiment(ti):
    print("Step 3: Analyzing sentiment...")

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


# DAY 3 - Save Sentiment Results

def save_results(ti):
    print("Step 4: Saving sentiment results...")

    data = ti.xcom_pull(task_ids="clean_data")

    print("Data ready for saving:", data)

    print("Sentiment results saved successfully!")


with DAG(
    dag_id="week9_sentiment_pipeline",
    start_date=datetime(2026, 8, 18),
    schedule="@daily",
    catchup=False,
) as dag:

    collect_task = PythonOperator(
        task_id="collect_data",
        python_callable=collect_data,
    )

    clean_task = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data,
    )

    analyze_task = PythonOperator(
        task_id="analyze_sentiment",
        python_callable=analyze_sentiment,
    )

    save_task = PythonOperator(
        task_id="save_results",
        python_callable=save_results,
    )

    collect_task >> clean_task >> analyze_task >> save_task