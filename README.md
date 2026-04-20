# CSCI411-NewsAggregator
A small-scale news aggregator for collecting and analyzing satirical and real news to explore patterns and differences in article metadata.

The system scrapes articles from predefined websites and stores structured metadata, including:

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

  ## Technologies Used
  - Python
  - BeautifulSoup (for web scraping)
  - SQLite (database)
  - pandas (data analysis)
  - matplotlib (visualization)

## Purpose

This project focuses on building a complete data pipeline including:

- Data collection
- Database design
- Querying
- Data analysis
- Visualization

<<<<<<< HEAD
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
=======
## Project Structure
- database/ # database setup and insertion scripts
- scraper/ # web scraping scripts
- query/ # database query functions
- analysis/ # data analysis and visualization
- data/ # SQLite database file
- main.py # main program entry point
- requirements.txt

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/JasmineSharpe/CSCI411-NewsAggregator
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## How to run the project
  ###1. Run the main script with python main.py


## What the program does 
- creates the database if it does not already exist
- scrapes articles from the source
- inserts the articles into the database
- prints sample results and queries
- generates a visualization

## Example Usage
### example output:

### AP News articles collected: 140
### Total rows in database: 140

### All articles:
### (1, 'Example headline...', 'AP News', 'Real', ...)

### Search for keyword 'Trump':
### (5, 'Trump meets...', ...)
### The goal is to explore trends and differences between satirical and real news articles.

### a bar chart will appear showing the average headline work count

## Limitations
- Data is limited to sources that allow consistent access
- Some news sources could not be reliably scraped due to connection/structural issues

## Future Improvements
- add more reliable news sources
-  improve scraping robustness using APIs
-  expand analysis (keyword accuracy, sentiment analysis)
-  build a simple web interface for interaction

>>>>>>> 2e92d6d370eb1d7b5fe3357117035f9ef0944771
