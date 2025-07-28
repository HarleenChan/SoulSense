import mysql.connector
import pandas as pd

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chifuyu*28",
        database="soulsense"
    )

def run_etl():
    conn = connect_db()
    query = "SELECT entry_date, mood_rating, tags, sentiment_score FROM emotional_logs"
    df = pd.read_sql(query, conn)

    # Convert entry_date to just the date
    df['entry_date'] = pd.to_datetime(df['entry_date']).dt.date

    # Aggregate mood and sentiment by day
    summary = df.groupby('entry_date').agg({
        'mood_rating': 'mean',
        'sentiment_score': 'mean',
        'tags': lambda x: ', '.join([tag for tag in x if tag])  # flatten tag text
    }).reset_index()

    summary.rename(columns={
        'entry_date': 'Date',
        'mood_rating': 'Avg_Mood',
        'sentiment_score': 'Avg_Sentiment',
        'tags': 'Collected_Tags'
    }, inplace=True)

    summary.to_csv("outputs/daily_summary.csv", index=False)
    print("Aggregation complete. Saved to outputs/daily_summary.csv")

if __name__ == "__main__":
    run_etl()
