import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.example.com"
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the paragraphs containing the Lorem Ipsum text
paragraphs = soup.find_all('p')

print('Printing all paragraphs')

# Extract and print the text content of the paragraphs
for paragraph in paragraphs:
    print(paragraph.get_text())

# Find the div tags on the page
div_tags = soup.find_all('div')

print('\n\n')

print('Printing all div tags')

# Print the div tags
for div in div_tags:
    print(div)
    print('-' * 50)  # Add a separator for readability
