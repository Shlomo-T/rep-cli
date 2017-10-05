"""This module holds frequent util methods"""
from cli_app.cache import CacheManager
import requests
import collections
from bs4 import BeautifulSoup

CREDENTIALS_KEY = 'censys_credentials'


def set_censys_credentials(credentials):
    """
    Store user's credentials in local cache.
    """
    cache = CacheManager()
    return cache.set(key='censys_credentials', value=credentials, ttl=None)


def get_censys_credentials():
    """
    Pull user's credentials if exists.
    """
    cache = CacheManager()
    if cache.has_key(CREDENTIALS_KEY):
        return cache.get(key=CREDENTIALS_KEY)


def parse_website_content(source):
    """
    Make a request to the ipv4/domain website and extract the title and top 10 keywords using BeautifulSoup.
    """
    website_url = 'http://%s' % source
    session = requests.session()
    response = session.get(website_url)
    if response.ok:
        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()
        words = soup.get_text().split()
        words_counter = collections.Counter(words)
        # Extract top 10 keywords from counter
        top_10_keywords = map(lambda keyword_count: keyword_count[0], words_counter.most_common(10))
        return {'title': soup.title.get_text(), 'keywords': top_10_keywords}
    return response.status_code, response.content

