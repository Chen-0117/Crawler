import trafilatura
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
import json

MAX_DEPTH = 3  # Set the maximum search depth

def get_random_user_agent():
    user_agent = UserAgent()
    return user_agent.random

def crawl_and_extract_links(url):
    headers = {
        "User-Agent": get_random_user_agent(),
        # Add more headers as needed
    }
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers, timeout=(3.05,3))
        if response:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                links = [urljoin(url, link.get('href')) for link in soup.find_all('a')]
                return links
            else:
                print(f"Failed to retrieve links from {url}. Status code: {response.status_code}")
                return []
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    

def extract_text_from_url(url):
    downloaded = trafilatura.fetch_url(url)
    extracted = trafilatura.extract(downloaded)
    return extracted

def crawl_and_extract_all_content(base_url, max_depth):
    links_to_visit = [(base_url, 1)]  # Use a tuple to store URL and depth
    visited_links = set()
    extracted_content = []
    
    max_links = 3000
    while links_to_visit and len(visited_links) < max_links:
        current_url, depth = links_to_visit.pop(0)
        
        if depth > max_depth:
            continue
        
        if current_url in visited_links:
            continue
        print(len(visited_links))
        print(f"Crawling {current_url}")
        visited_links.add(current_url)
        
        try:
            extracted_text = extract_text_from_url(current_url)
            if extracted_text:
                extracted_content.append({"url": current_url, "content": extracted_text})
            new_links = crawl_and_extract_links(current_url)
            links_to_visit.extend((link, depth + 1) for link in new_links if link not in visited_links and link[:4] == 'http')
        except:
            continue
            

    return extracted_content

if __name__ == "__main__":
    base_url = "https://dlgc.dlzb.com/"  # Replace with the base URL of the website you want to crawl
    search_depth = 3  # Set the desired search depth
    
    extracted_content = crawl_and_extract_all_content(base_url, search_depth)
    
    json_filename = "extracted_content电力工程网.json"
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(extracted_content, json_file, ensure_ascii=False, indent=4)
    
    print(f"Extracted content saved to {json_filename}")
