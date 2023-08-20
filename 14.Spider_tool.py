import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_urls = set()
urls_to_visit = []

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed for {url}")
        return

    if response.status_code == 200:
        if url in visited_urls:
            return  
        visited_urls.add(url) 

        soup = BeautifulSoup(response.content, 'html.parser')
        urls = []

        for tag in soup.find_all('a'):
            href = tag.get("href")
            if href and href.startswith(('http', 'https')):
                full_url = href
            else:
                full_url = urljoin(url, href) 
            urls.append(full_url)

        print("URLs found:", urls)
        urls_to_visit.extend(url for url in urls if url not in visited_urls)

url = input("Enter the URL you want to scrape: ")
keyword = input("Enter the keyword to search for in the URLs: ")

urls_to_visit.append(url)

while urls_to_visit:
    current_url = urls_to_visit.pop(0)
    spider_urls(current_url, keyword)
