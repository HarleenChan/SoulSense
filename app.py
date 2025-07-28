import streamlit as st
import mysql.connector
import pandas as pd
from Core.db_handler import insert_entry, connect_db

# Page setup
st.set_page_config(page_title="SoulSense", page_icon="🌱")
st.title("🌱 SoulSense - Daily Emotional Check-In")

# Form for entry
with st.form("check_in_form"):
    mood = st.slider("How are you feeling today? (1 = Low, 10 = High)", 1, 10, 5)
    tags = st.multiselect("Tags (optional)", ["Stress", "Joy", "Fatigue", "Clarity", "Anxiety", "Love", "Focus"])
    journal = st.text_area("Write a few lines about how you feel...", height=150)

    submitted = st.form_submit_button("Submit")

    if submitted and journal.strip():
        insert_entry(mood, ",".join(tags), journal)
        st.success("Your entry has been saved. Thank you for sharing 💖")

# --- Database Connection ---
conn = connect_db()
cursor = conn.cursor(dictionary=True)

# --- Load all logs ---
cursor.execute("SELECT * FROM emotional_logs ORDER BY id DESC")
rows = cursor.fetchall()
df = pd.DataFrame(rows)

# --- Display Entries ---
st.write("### Your Journal Entries")
st.dataframe(df)

# --- Delete Option ---
st.write("### 🗑️ Delete an Entry")
delete_id = st.number_input("Enter the ID of the entry you want to delete:", min_value=1, step=1)

if st.button("Delete Entry"):
    try:
        cursor.execute("DELETE FROM emotional_logs WHERE id = %s", (delete_id,))
        conn.commit()
        st.success(f"Entry with ID {delete_id} has been deleted.")
    except Exception as e:
        st.error(f"Error deleting entry: {e}")

# --- Filter by Sentiment ---
st.write("### 🔍 Filter by Sentiment Score")
if not df.empty and "sentiment_score" in df.columns:
    min_score = float(df["sentiment_score"].min())
    max_score = float(df["sentiment_score"].max())
    sentiment_range = st.slider("Select sentiment range", min_value=-1.0, max_value=1.0, value=(min_score, max_score), step=0.01)
    filtered_df = df[(df["sentiment_score"] >= sentiment_range[0]) & (df["sentiment_score"] <= sentiment_range[1])]
    st.dataframe(filtered_df)

# Close connection
cursor.close()
conn.close()
