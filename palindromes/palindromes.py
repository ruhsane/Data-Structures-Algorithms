#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)

    # lower case the input, and ingore anything other than lower letters
    filteredText = ''.join(c for c in text.lower() if c in string.ascii_lowercase)

    # return is_palindrome_iterative(filteredText)
    return is_palindrome_recursive(filteredText)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests

    left = 0
    right = len(text) - 1

    # run loop until leftMost index and rightMost index cross over
    while left <= right:
        # if the leftMost value and rightMost value in current iteration are not the same, return false
        if text[left] != text[right]:
            return False
        # move left and right towards middle for next iteration
        left += 1
        right -= 1

    # after the loop is done when indexes cross and didn't return false -- return true
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    # this only runs first iteration
    if left == None and right == None:
        # begin with left being the first index, and left being the last index
        left = 0
        right = len(text) - 1
    
    # recursively call function only if the left index and right index doesnt cross over
    if left <= right:
        # if the left value and right value are not the same, return false
        if text[left] != text[right]:
            return False
         # move left and right towards middle for next iteration of call
        left += 1
        right -= 1
        # call the function again to check palindrome with updated left and right index
        return is_palindrome_recursive(text, left, right)

    # returns true until left index and right index crossed over and didnt return false during the process
    return True

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
