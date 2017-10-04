import os
import sys


CENSYS_API_KEY = os.environ.get('CENSYS_API_KEY', None)
CENSYS_API_SECRET = os.environ.get('CENSYS_API_SECRET', None)

CACHE_PATH = os.environ.get('REP_CACHE_PATH', '~/cache')

