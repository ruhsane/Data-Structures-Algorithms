#!python

from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.set = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                for key, value in element:
                    self.add(key, value)

    def contains(self, key):
        '''return a boolean indicating whether element is in this set'''
        return self.set.contains(key)

    def add(self, key, value):
        '''add element to this set, if not present already'''
        return self.set.set(key, value)