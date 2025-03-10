import requests
import certifi
from bs4 import BeautifulSoup

def scrape_webpage(url):
    response = requests.get(url, verify=certifi.where())
    bs = BeautifulSoup(response.content, 'html.parser')
    result = bs.get_text(separator='\n')
    return result
