#!/usr/bin/python3
""" MRU Caching """

BasicCache = __import__('0-basic_cache').BasicCache


class MRUCache(BasicCache):
    """ MRU Cache class """

    def __init__(self):
        """ Init method """
        super().__init__()
        self.counter = 0
        self.priorities = {}

    def put(self, key, item):
        """ Put an item """
        cache = self.cache_data
        if (key in cache.keys()):
            cache[key] = item
            self.priorities[key] = self.counter
            self.counter += 1
        elif not (key is None or item is None):
            if len(self.cache_data) >= BasicCache.MAX_ITEMS:
                first_key = sorted(self.priorities.items(),
                                   key=lambda item: item[1],
                                   reverse=True)[0][0]
                cache.pop(first_key)
                self.priorities.pop(first_key)
                print(f"DISCARD: {first_key}")
            cache[key] = item
            self.priorities[key] = self.counter
            self.counter += 1

    def get(self, key):
        """ GET an item """
        if (key is None):
            return None
        return self.cache_data.get(key, None)
