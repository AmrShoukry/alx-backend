#!/usr/bin/python3
""" Basic caching """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching class """

    def put(self, key, item):
        """ PUT an item """
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """ GET an item """
        if (key is None):
            return None
        return self.cache_data.get(key, None)
