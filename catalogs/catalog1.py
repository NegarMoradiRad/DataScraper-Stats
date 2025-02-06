import requests
from bs4 import BeautifulSoup

url = "https://catalog.data.gov/dataset"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    with open('dataset.txt', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
else:
    print("Error fetching data:", response.status_code)
