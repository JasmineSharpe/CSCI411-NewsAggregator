# scraper for Onion - satirical news source
## same code as Reuters, just tailored to Onion

import requests
from bs4 import BeautifulSoup

def scrape_onion():
    url = "https://theonion.com/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    articles = []

    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=True)

        for link in links:
            title = link.get_text(strip=True)
            href = link["href"]

            if title and len(title.split()) > 3:
                article = {
                    "title": title,
                    "date": None,
                    "source": "The Onion",
                    "category": "Satire",
                    "url": href,
                    "content": None,
                    "word_count": len(title.split())
                }
                articles.append(article)

    except requests.exceptions.Timeout:
        print("The Onion request timed out. Skipping Onion for now.")
    except requests.exceptions.RequestException as e:
        print(f"Error scraping The Onion: {e}")

    return articles