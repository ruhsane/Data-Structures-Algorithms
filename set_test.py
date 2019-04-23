#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0

    def test_contains(self):
        s = Set()
        s.add('I', 1)
        s.add('V', 5)
        s.add('X', 10)
        assert s.contains('I') is True
        assert s.contains('V') is True
        assert s.contains('X') is True
        assert s.contains('A') is False

if __name__ == '__main__':
    unittest.main()