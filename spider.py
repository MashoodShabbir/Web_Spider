import requests
import re
from urllib.parse import urljoin
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "-url", dest="url", help="Please specify the URL to crawl")
    options = parser.parse_args()
    if options.url:
        return options
    else:
        parser.error("[-] Please specify the url to crawl. Use --help for more details")
        
def request(url):
    try:
        response = requests.get("http://" + url if not url.startswith("http") else url)
        if response.status_code == 200:
            return response
    except requests.exceptions.ConnectionError:
        print(f"[!] Failed to connect to {url}")
        return None

def extract_links_from(url):
    response = request(url)
    if response:
        href_links = re.findall(r'(?:href=["\'])(.*?)(?:["\'])', response.content.decode("utf-8", errors="ignore"))
        return href_links
 
    return []

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        absolute_link = urljoin(url, link)
        if "#" in absolute_link:
            absolute_link = absolute_link.split("#")[0]
        if url in absolute_link and absolute_link not in target_links: 
            target_links.append(absolute_link)
            print(absolute_link)
            crawl(absolute_link)
            

target_links = []
options = get_args()
            
crawl(options.url)