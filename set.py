#!python

from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.items = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def __iter__(self):
        for el in self.all_items():
            yield el

    def all_items(self):
        return self.items.keys()

    def contains(self, key):
        '''return a boolean indicating whether element is in this set'''
        return self.items.contains(key)

    def length(self):
        return self.size

    def add(self, element):
        '''add element to this set, if not present already'''
        self.size += 1
        return self.items.set(element, element)

    def remove(self, element):
        ''' remove element from this set, if present, or else raise KeyError '''
        self.size -= 1
        return self.items.delete(element)

    def union(self, other_set):
        ''' return a new set that is the union of this set and other_set '''
        # initialize union with other_set
        union = other_set
        for item in self:
            # add every item in our set to union
            union.add(item)
        return union

    def intersection(self, other_set):
        ''' return a new set that is the intersection of this set and other_set '''

        # compare their size to reduce running time
        if other_set.size > self.size:
            smaller_set = self
            larger_set = other_set
        else:
            smaller_set = other_set
            larger_set = self

        intersection = Set()
        
        # iterate through the smaller set
        for el in smaller_set:
            # if the element also in larger set, add to intersection
            if larger_set.contains(el):
                intersection.add(el)
        return intersection

    def difference(self, other_set):
        ''' return a new set that is the difference of this set and other_set '''
        # difference = this set minus intersection

        #initialize result with this set
        result = self
        intersection = self.intersection(other_set)

        # for every common element we have
        for el in intersection:
            # delete it out of this set
            result.remove(el)

        return result


    def is_subset(self, other_set):
        ''' return a boolean indicating whether other_set is a subset of this set '''