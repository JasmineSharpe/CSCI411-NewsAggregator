import requests
from bs4 import BeautifulSoup

def scrape_babylonbee():
    url = "https://babylonbee.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    articles = []
    seen_urls = set()

    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=True)

        for link in links:
            title = link.get_text(" ", strip=True)
            href = link.get("href")

            if not title or len(title.split()) <= 3:
                continue

            if not href:
                continue

            if href.startswith("/"):
                href = "https://babylonbee.com" + href

            if "babylonbee.com" not in href:
                continue

            if href in seen_urls:
                continue

            seen_urls.add(href)

            article = {
                "title": title,
                "date": None,
                "source": "Babylon Bee",
                "category": "Satire",
                "url": href,
                "content": None,
                "word_count": len(title.split())
            }
            articles.append(article)

    except requests.exceptions.RequestException as e:
        print(f"Error scraping Babylon Bee: {e}")

    return articles