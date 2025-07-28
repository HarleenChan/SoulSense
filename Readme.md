# SoulSense: Sentiment Analysis Dashboard 🌊

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Last Commit](https://img.shields.io/github/last-commit/HarleenChan/SoulSense)
![License: MIT](https://img.shields.io/github/license/HarleenChan/SoulSense)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/meenal-p-chan)



SoulSense is a lightweight sentiment analysis pipeline and dashboard built with Python, Streamlit, and MySQL.  
It analyzes text data (like customer feedback or logs), calculates sentiment using VADER, and provides a clean dashboard interface to view, filter, and manage insights.

---

## 💡 Features

- 🧠 Real-time Sentiment Analysis (Positive, Neutral, Negative)
- 🗃️ Daily Summarization via ETL pipeline
- 🔁 Backfill support for old entries
- 📊 Streamlit Dashboard with Filters & Delete Option
- 💽 Data stored and retrieved from MySQL

---

## 🚀 Getting Started

### 1. Clone the repository:
```bash
git clone https://github.com/Harleenchan/soulsense.git
cd soulsense

2. Install dependencies:

pip install -r requirements.txt

3. Run the ETL pipeline:

python etl/aggregate_logs.py

4. Launch the dashboard:

streamlit run dashboard.py


📁 Folder Structure

soulsense/
│
├── etl/
│   ├── aggregate_logs.py
│   └── backfill_sentiment.py
│
├── outputs/
│   └── daily_summary.csv
│
├── app.py
├── dashboard.py
├── db_handler.py
├── requirements.txt
├── README.md
└── .gitignore


🧠 Tech Stack
Python

Streamlit

MySQL

NLTK (VADER)

pandas

🌸 Author
Made with love by Meenal 

📬 Contact
GitHub: https://github.com/HarleenChan

LinkedIn: Meenal Padgil

