import mysql.connector
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chifuyu*28",
        database="soulsense"
    )

def update_null_sentiments():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, journal_entry FROM emotional_logs WHERE sentiment_score IS NULL")
    rows = cursor.fetchall()

    for row in rows:
        entry_id = row[0]
        text = row[1]
        score = analyzer.polarity_scores(text)['compound']

        update_query = "UPDATE emotional_logs SET sentiment_score = %s WHERE id = %s"
        cursor.execute(update_query, (score, entry_id))

    conn.commit()
    conn.close()
    print(f"Updated {len(rows)} entries with sentiment scores.")

if __name__ == "__main__":
    update_null_sentiments()
