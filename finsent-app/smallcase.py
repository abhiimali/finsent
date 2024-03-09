import requests
from bs4 import BeautifulSoup

from stock_dict import stocks_dict

base_url = "https://www.smallcase.com/stocks/"

def get_small_case_data(stock_name):
    
    special_url = base_url + stocks_dict.get(stock_name)
    print(special_url)
    response = requests.get(special_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the container with class "flyntComponent" and attribute "is" equal to "stock-news"
        stock_news_container = soup.find('div', class_='flyntComponent', attrs={'is': 'stock-news'})

        if stock_news_container:
            # Find all the divs with class "latest-child"
            latest_child_divs = stock_news_container.find_all('div', class_='latest-child')
            urls = []
            titles = []
            for div in latest_child_divs:
                # Find the title and URL
                title = div.find('p', class_='latest-title').text.strip()
                url = div.find('a')['href']

                # Find the value of class name of span inside p class="change-news"
                change_news_span = div.find('p', class_='change-news').find('span')
                change_class = change_news_span['class'][0] if change_news_span else None
                urls.append(url)
                titles.append(title)
                print("Title:", title)
                print("URL:", url)
                print("Change Class:", change_class)
                print()
            return urls, titles
        else:
            print("Stock news container not found.")
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
