#!python

from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.set = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(self, element):
        '''return a boolean indicating whether element is in this set'''
        return self.set.contains(element.key)

    def add(self, element):
        '''add element to this set, if not present already'''
        for key, value in element:
            return self.set.set(key, value)