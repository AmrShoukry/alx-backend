#!/usr/bin/python3
""" FIFO Caching """

BasicCache = __import__('0-basic_cache').BasicCache


class FIFOCache(BasicCache):
    """ FIFO Cache class """

    def __init__(self):
        """ Init method """
        super().__init__()
        self.counter = 0
        self.orders = {}

    def put(self, key, item):
        """ Put an item """
        cache = self.cache_data
        if not (key is None or item is None or key in cache.keys()):
            if len(self.cache_data) >= BasicCache.MAX_ITEMS:
                first_key = list(dict(sorted(self.orders.items())).keys())[0]
                cache.pop(first_key)
                self.orders.pop(first_key)
                print(f"DISCARD: {first_key}")
            cache[key] = item
            self.orders[key] = self.counter
            self.counter += 1

    def get(self, key):
        """ GET an item """
        if (key is None):
            return None
        return self.cache_data.get(key, None)
