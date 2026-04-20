import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "articles.db"

def insert_articles(articles):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for article in articles:
        cursor.execute("""
        INSERT OR IGNORE INTO articles
        (title, date, source, category, url, content, word_count)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            article.get("title"),
            article.get("date"),
            article.get("source"),
            article.get("category"),
            article.get("url"),
            article.get("content"),
            article.get("word_count")
        ))

    conn.commit()
    conn.close()
    print(f"{len(articles)} articles inserted into {DB_PATH}")