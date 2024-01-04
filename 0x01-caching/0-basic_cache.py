#!/usr/bin/python3
""" Basic caching """

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ Basic caching class """
    def __init__(self):
        """ Init """
        self.cache_data = {}
        super()

