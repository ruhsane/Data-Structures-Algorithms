#!python

from set import Set
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0
        test_set = Set(['Apple','Banana','Cactus','Durian'])
        assert test_set.length() == 4
        
    def test_contains(self):
        test_set = Set(['Apple','Banana','Cactus','Durian'])
        assert test_set.length() == 4
        assert test_set.contains('Apple') == True
        assert test_set.contains('Banana') == True
        assert test_set.contains('Cactus') == True
        assert test_set.contains('Durian') == True
        assert test_set.contains('Eggs') == False
        assert test_set.contains('Z') == False

    def test_add(self):
        test_set = Set()
        assert test_set.length() == 0
        test_set.add('Apple')
        assert test_set.contains('Apple') == True
        test_set.add('Banana')
        assert test_set.contains('Banana') == True
        test_set.add('Cactus')
        assert test_set.contains('Cactus') == True

    def test_remove(self):
        test_set = Set(['Apple','Banana','Cactus','Durian'])
        assert test_set.length() == 4
        test_set.remove('Durian')
        assert test_set.length() == 3
        assert test_set.contains('Durian') == False
        test_set.remove('Cactus')
        assert test_set.length() == 2
        assert test_set.contains('Cactus') == False
        test_set.remove('Banana')
        assert test_set.length() == 1
        assert test_set.contains('Banana') == False
        test_set.remove('Apple')
        assert test_set.length() == 0
        assert test_set.contains('Apple') == False
    
    def test_union(self):
        test_set_one = Set(['Apple','Banana','Cactus','Durian'])
        test_set_two = Set(['Eggs','F','G','H'])
        union = test_set_one.union(test_set_two)
        assert union.size == 8
        assert union.contains('Apple') == True
        assert union.contains('Banana') == True
        assert union.contains('Cactus') == True
        assert union.contains('Durian') == True
        assert union.contains('Eggs') == True
        assert union.contains('F') == True
        assert union.contains('G') == True
        assert union.contains('H') == True
    
    def test_intersection(self):
        test_set_one = Set(['Apple','Banana','Cactus','Durian'])
        test_set_two = Set(['Apple','Eggs','Cactus','F'])
        intersection_set = test_set_one.intersection(test_set_two)
        assert intersection_set.size == 2
        assert intersection_set.contains('Apple') == True
        assert intersection_set.contains('Cactus') == True
        assert intersection_set.contains('F') == False

    
    def test_difference(self):
        test_set_one = Set(['Apple','Banana','Cactus','Durian'])
        test_set_two = Set(['Apple','F','Cactus','H'])
        difference = test_set_one.difference(test_set_two)
        assert difference.size == 2
        assert difference.contains('Banana') == True
        assert difference.contains('Durian') == True
    
    def test_is_subset(self):
        test_set = Set(['Apple','Banana','Cactus','Durian'])
        subset = Set(['Apple', 'Banana'])
        is_subset = test_set.is_subset(subset)
        assert type(is_subset) == bool
        assert subset.is_subset(test_set) == True

        subset.add('Z')
        assert subset.is_subset(test_set) == False

if __name__ == '__main__':
    unittest.main()