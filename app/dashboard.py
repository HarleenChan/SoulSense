# dashboard.py

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Load data
OUTPUT_PATH = 'outputs/daily_summary.csv'

st.set_page_config(page_title="SoulSense Dashboard", layout="centered")

st.title("💠 SoulSense: Emotional Reflection Dashboard")

# Load CSV
if os.path.exists(OUTPUT_PATH):
    df = pd.read_csv(OUTPUT_PATH)

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Sidebar Date Filter
    selected_date = st.sidebar.date_input("Select a date to reflect on", value=df['Date'].max().date())

    # Filter data
    filtered = df[df['Date'].dt.date == selected_date]

    if not filtered.empty:
        st.subheader(f"🗓️ Emotions on {selected_date.strftime('%B %d, %Y')}")

        st.metric("😊 Average Mood", f"{filtered['Avg_Mood'].iloc[0]:.1f}")
        st.metric("💬 Average Sentiment", f"{filtered['Avg_Sentiment'].iloc[0]:.2f}")
        st.text(f"🧠 Tags Captured: {filtered['Collected_Tags'].iloc[0]}")
    else:
        st.warning("No data found for the selected date.")

    # Line Chart for Mood over Time
    st.subheader("📈 Mood & Sentiment Trends")

    mood_chart = df[['Date', 'Avg_Mood', 'Avg_Sentiment']].set_index('Date')
    st.line_chart(mood_chart)
else:
    st.error("No summary data found. Please run the ETL pipeline first.")

st.subheader("📂 Full Data Snapshot")
st.dataframe(df)

