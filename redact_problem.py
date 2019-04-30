''' 
Problem: A web application needs to redact some words. Write a function that takes 2 arrays of words (strings),
and return a new array of words in the first array (the text) taht are not in the second array (the redacted words) 
'''
from hashtable import HashTable

def redact(array1, array2) :
    result = []
    hash_table = HashTable()
    for word in array2:
        hash_table.set(word, word)

    for word in array1:
        if hash_table.contains(word) is False:
            result.append(word)
    return result

def test():
    answer = redact(['a', 'b', 'c'], ['b', 'd', 'e'])
    assert answer == ['a', 'c']
    
    answer = redact(['word', 'idk', 'another'], ['haha', 'cs', 'class'])
    assert answer == ['word', 'idk', 'another']

    answer = redact(['ooooof', 'no', 'none'], ['no','none'])
    assert answer == ['ooooof']

    answer = redact(['a', 'a', 'b'], ['b','b'])
    assert answer == ['a', 'a']

if __name__ == '__main__':
    test()
