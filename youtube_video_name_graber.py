from bs4 import BeautifulSoup
import requests

URL = input('Enter the URL:')

PAGE = requests.get(URL).text
soup = BeautifulSoup(PAGE,'lxml')

print(soup.title.text)
