# CSCI411-NewsAggregator
A small-scale news aggregator for collecting and analyzing satirical and real news to explore patterns and differences in article metadata.

The system scrapes articles from predefined websites and stores structured metadata including:

- Headline
- Publication date
- Source
- URL
- Word count

The collected data is stored in a local database and can be queried, sorted, and analyzed to explore patterns across satire and real news articles.

## Features

- Web scraping using BeautifulSoup
- Structured storage using SQLite
- Querying by keyword, source, or date
- Data analysis using pandas
- Visualizations using matplotlib/seaborn
- Optional command-line or Flask interface

## Purpose

This project focuses on building a complete data pipeline including:

- Data collection
- Database design
- Querying
- Data analysis
- Visualization

The goal is to explore trends and differences between satirical and real news articles.

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the project:
   python main.py

## Example Analyses
- Compare the number of satire vs. real articles
- Compare headline word counts
- Search for keywords in titles