from cli_app.cache import CacheManager
import requests
import re
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
        return cache.get(key=CREDENTIALS_KEY).split('|')


def parse_website_content(source):
    """
    Make a request to the ipv4/domain website and extract the title and top 10 keywords using BeautifulSoup.
    """
    website_url = 'http://%s' % source
    response = requests.get(website_url)
    if response.ok:
        page_content = response.content
        soup = BeautifulSoup(page_content)
        page_text = soup.findAll(text=True)
        visible_texts = filter(visible, page_text)

        print soup.title, visible_texts
        print '\n\n'
        return {'title': soup.title, 'keywords': []}
    return response.status_code, response.content


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', unicode(element)):
        return False
    return True
