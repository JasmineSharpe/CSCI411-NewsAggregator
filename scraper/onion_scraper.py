# scraper for Onion - satirical news source
## same code as Reuters, just tailored to Onion

import requests #library that allows Python to connect to websites and download web content
from bs4 import BeautifulSoup #reads website HTML and finds specific elements

url = "https://www.theonion.com/"

response = requests.get(url) #sends a request to Reuters, and the website sends back the HTML in 'response'

soup = BeautifulSoup(response.text, "html.parser") #converts the HTML to an organized structure Python can search

articles = soup.find_all("a") #collects all articles and puts them in a list

for article in articles[:10]: #traverses first 10 articles and prints them in a clean list

    headline = article.text.strip()

    if headline:
        print("Onion:", headline)