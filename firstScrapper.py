import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.lipsum.com"
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the paragraphs containing the Lorem Ipsum text
paragraphs = soup.find_all('p')

# Extract and print the text content of the paragraphs
for paragraph in paragraphs:
    print(paragraph.get_text())
