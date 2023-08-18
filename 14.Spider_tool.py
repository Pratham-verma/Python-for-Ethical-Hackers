import requests

from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"request failed {url}")
    
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        a_tags = soup.find_all('a')
        urls = []
        
        for tag in a_tags:
            href = tag.get("href")
            if href is not None and href != "":
             urls.append(href)
        print(urls)
    
    
url = input("enter the URL you want to scrap\n")
keyword = input("enter the keyword search for in the URL provided. ")

spider_urls(url, keyword)
