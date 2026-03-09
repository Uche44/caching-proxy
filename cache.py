from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=300)


def get_cache(key):
    return cache.get(key)

def set_cache(key, value):
    cache[key] = value

def clear_cache():
    cache.clear()    