#connect everything to run seamlessly

from database.db_setup import create_database
from database.insert_articles import insert_articles
from scraper.run_scrapers import collect_all_articles
from query.query_articles import get_all_articles, get_articles_by_source, search_articles_by_keyword
from analysis.analysis import run_analysis

def main():
    create_database()

    articles = collect_all_articles()

    if not articles:
        print("No articles collected")
        return
    
    insert_articles(articles)

    all_articles = get_all_articles()
    print(f"\nTotal rows in database: {len(all_articles)}")

    print("\nAll articles:")
    for article in all_articles[:5]:
        print(article)

    print("\nReal news articles:")
    real_articles = get_articles_by_source("AP News")
    print(f"Real rows: {len(real_articles)}")
    for article in real_articles[:5]:
        print(article)

    print("\nSatire articles:")
    satire_articles = get_articles_by_source("Babylon Bee")
    print(f"Satire rows: {len(satire_articles)}")
    for article in satire_articles[:5]:
        print(article)

    print("\nSearch for keyword 'Trump':")
    keyword_results = search_articles_by_keyword("Trump")
    for article in keyword_results[:5]:
        print(article)

    run_analysis()

if __name__ == "__main__":
    main()