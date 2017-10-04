"""This module suppose to manage cache operations"""
from diskcache import Cache
from dev_config import CACHE_PATH

TTL = 600


class CacheManager(object):

    def __init__(self, cache_path=CACHE_PATH):
        self.cache = Cache(cache_path)

    def items(self):
        return self.cache.iterkeys()

    def has_key(self, key):
        return key in self.cache

    def set(self, key, value, ttl=TTL):
        return self.cache.set(key=key, value=value, expire=ttl)

    def get(self, key):
        return self.cache.get(key=key)

    def clear_cache(self):
        for key in self.cache:
            if key != 'censys_credentials':
                del self.cache[key]
        return True

    def close(self):
        self.cache.close()
