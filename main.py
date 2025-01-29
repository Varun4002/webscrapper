import requests
from bs4 import BeautifulSoup


url = 'https://nouraessence.com/'  # Replace with actual URL
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')
print(response.status_code)

headlines = soup.find_all('h2')

for headline in headlines:
    print(headline.text)

print(soup.prettify())

