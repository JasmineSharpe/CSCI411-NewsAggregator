# query the file

import sqlite3
import os

DB_PATH = os.path.join("data", "articles.db")

def get_all_articles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM articles")
    results = cursor.fetchall()

    conn.close()
    return results

def get_articles_by_source(source):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM articles WHERE source = ?", (source,))
    results = cursor.fetchall()

    conn.close()
    return results

def search_articles_by_keyword(keyword):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM articles WHERE title LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()

    conn.close()
    return results