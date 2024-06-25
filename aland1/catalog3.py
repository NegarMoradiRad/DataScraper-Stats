import requests
from bs4 import BeautifulSoup

url = "https://catalog.data.gov/dataset"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    datasets = soup.find_all('div', class_='dataset-heading')

    with open('datasets.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>')
        f.write('<html lang="en">')
        f.write('<head>')
        f.write('<meta charset="UTF-8">')
        f.write('<title>Data.gov Datasets</title>')
        f.write('</head>')
        f.write('<body>')
        f.write('<h1>Data.gov Datasets</h1>')
        f.write('<table>')
        f.write('<tr>')
        f.write('<th>Title</th>')
        f.write('<th>View Count</th>')
        f.write('</tr>')

        for dataset in datasets:
            title = dataset.find('h3').text
            views = dataset.find('span', class_='dataset-views').text
            f.write('<tr>')
            f.write(f'<td>{title}</td>')
            f.write(f'<td>{views}</td>')
            f.write('</tr>')

        f.write('</table>')
        f.write('</body>')
        f.write('</html>')
else:
    print("Error fetching data:", response.status_code)