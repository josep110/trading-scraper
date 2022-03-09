import logging, time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup 

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)

class Crawler:   # Generic web crawling object primarily using BeautifulSoup for site traversal.

    def __init__(self, urls=[]):
        self.visited = []
        self.unvisited = urls
       
    def download_url(self, url):
        return requests.get(url).text
        
    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser') # uses standard Python html parser.
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path
        
    def add_url_to_visit(self, url):
        if url not in self.visited and url not in self.unvisited:
            self.unvisited.append(url)
        
    def crawl(self,url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)
        
    def run(self):
        while self.unvisited:
            url = self.unvisited.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited.append(url)

                

    def navigate(self, url):
        run()
            
        

def go(url):
    Crawler(urls=[url]).run()


 
