from bs4 import BeautifulSoup
import requests

URL = 'https://www.youtube.com/watch?v=1WSDn3B_Z_s'

PAGE = requests.get(URL).text
soup = BeautifulSoup(PAGE,'lxml')

print(soup.title.text)
