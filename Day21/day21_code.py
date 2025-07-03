# Challenge - Scrape headlines from a news site
import requests
from bs4 import BeautifulSoup

# URL of the news site
url = "https://www.thehindu.com/"

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all headline tags
headlines = soup.find_all("h3")

print("📰 Top TheHindu Headlines:\n")
# Print top 20 headlines
for i, headline in enumerate(headlines[:20], 1):
    text = headline.get_text(strip=True)
    print(f"{i}. {text}")
