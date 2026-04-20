import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "articles.db"

def create_database():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date TEXT,
        source TEXT NOT NULL,
        category TEXT,
        url TEXT UNIQUE,
        content TEXT,
        word_count INTEGER
    )
    """)

    conn.commit()
    conn.close()

    print(f"Database created at: {DB_PATH}")
    print("Table 'articles' is ready.")

if __name__ == "__main__":
    create_database()