import requests
from bs4 import BeautifulSoup

url = "https://catalog.data.gov/dataset"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    datasets = soup.find_all('div', class_='dataset-heading')
    for dataset in datasets:
        title = dataset.find('h3').text
        views = dataset.find('span', class_='dataset-views').text
        print(f"{title} - {views}")
else:
    print("Error fetching data:", response.status_code)