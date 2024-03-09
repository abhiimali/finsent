import requests
from bs4 import BeautifulSoup

def get_urls_from_google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        print(links)
        for link in links:
            href = link.get('href')
            if href and 'url?q=' in href:
                url = href.split('url?q=')[1].split('&sa=')[0]
                print(url)
    else:
        print("Failed to fetch search results.")

query = "iex stock news"
get_urls_from_google_search(query)
