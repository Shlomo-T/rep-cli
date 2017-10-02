from diskcache import Cache

CACHE_PATH = '/cache'
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
        return self.get(key=key)

    def clear_cache(self):
        for key in self.cache:
            if key != 'credentials':
                del self.cache[key]

    def close(self):
        self.cache.close()