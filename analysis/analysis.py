import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "articles.db"

def run_analysis():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM articles", conn)
    conn.close()

    if df.empty:
        print("No data found in database.")
        return

    print("\nArticle count by source:")
    print(df["source"].value_counts())

    print("\nArticle count by category:")
    print(df["category"].value_counts())

    print("\nAverage word count by category:")
    print(df.groupby("category")["word_count"].mean())

    df["category"].value_counts().plot(kind="bar")
    plt.title("Article Count: Satire vs Real")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()