import mysql.connector
from datetime import datetime
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chifuyu*28",
        database="soulsense"
    )

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)['compound']
    return score    



def insert_entry(mood_rating, tags, journal_entry):
    conn = connect_db()
    cursor = conn.cursor()

    entry_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sentiment_score = analyze_sentiment(journal_entry)

    query = """
        INSERT INTO emotional_logs (entry_date, mood_rating, tags, journal_entry, sentiment_score)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (entry_date, mood_rating, tags, journal_entry, sentiment_score)

    cursor.execute(query, values)
    conn.commit()
    conn.close()

