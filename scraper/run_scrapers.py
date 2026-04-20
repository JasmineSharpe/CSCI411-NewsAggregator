# run both onion and AP scrapers together

from scraper.ap_scraper import scrape_ap_news
from scraper.babylonbee_scraper import scrape_babylonbee

def collect_all_articles():
    all_articles = []

    try:
        ap_articles = scrape_ap_news()
        print(f"AP News articles collected: {len(ap_articles)}")
        all_articles.extend(ap_articles)
    except Exception as e:
        print(f"Error scraping AP News: {e}")

    try:
        bee_articles = scrape_babylonbee()
        print(f"Babylon Bee articles collected: {len(bee_articles)}")
        all_articles.extend(bee_articles)
    except Exception as e:
        print(f"Error scraping Babylon Bee: {e}")

    print(f"Total articles collected: {len(all_articles)}")
    return all_articles