import requests
import certifi
from bs4 import BeautifulSoup
from readability import Document  




def scrape_webpage(url):
    response = requests.get(url,verify=certifi.where())
    # Use readability to extract the article/content
    doc = Document(response.text)
    cleaned_html = doc.summary()

    # Now parse that cleaned HTML with BeautifulSoup
    soup = BeautifulSoup(cleaned_html, "html.parser")

    # Remove any remaining scripts/styles
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Get clean text
    return soup.get_text(separator=" ", strip=True)


