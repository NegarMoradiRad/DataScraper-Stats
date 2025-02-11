# DataScraper-Stats

This project is a Python script that processes dataset information from [Catalog Data Gov](https://catalog.data.gov/dataset), extracts the number of views for each dataset on the first page, and presents the results in an HTML file.

## Features:
- Fetch and save the complete webpage data in a text file.  
- Extract the view count of each dataset using **BeautifulSoup**.  
- Store the extracted information in an **HTML file**.  
- Display the data in a **structured HTML table**.

## How to Run:
1. Install the required dependencies:

pip install requests beautifulsoup4
2. Run the script:

python scraper.py
3. Outputs:
- **dataset.html** containing the processed data.
- The extracted dataset view counts displayed in the **terminal**.

## Dependencies:
- Python 3.x
- requests
- BeautifulSoup4
