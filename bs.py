from bs4 import BeautifulSoup
import requests
import os
import dotenv

dotenv.load_dotenv()

URL = os.getenv('URL')
headers = os.getenv('HEADERS')

def check():
    s = []
    PAGE = requests.get(URL).text
    soup = BeautifulSoup(PAGE, 'html.parser')
    name = soup.find('h1', class_='rf-pdp-title').text
    price = soup.find('div', class_='rf-pdp-currentprice').text
    print(name ,price)

check()
