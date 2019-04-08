#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if len(array) <= index:   #check valid index
        return None
    elif array[index] == item:  # item found
        return index
    else:
        # call the function recursively for following index
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        # if the item is in middle index, it is found and done
        if array[mid] == item:
            return mid #found

        # if the middle value is less than (left side of) our target 
        elif array[mid] < item:
            # make the starting point one more than the middle, and we will only look at the right side
            left = mid+1

        # if the middle value is greater than (right side of) our target 
        elif array[mid] > item:
            # starting point will not change, ending point will be one less than the current middle value. and we will only look at the left side
            right = mid - 1

    # after while loop, if never found, return none
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

  
    # this only runs first iteration
    if left == None and right == None:
        left = 0
        right = len(array) - 1
    
    # recursively call function only if the leftMost index and rightMost index doesnt cross over
    if right <= left:
        # get the middle index
        mid = (left + right) // 2

        # if the item is in middle index, it is found and done
        if array[mid] == item:
            return mid #found

        # if the middle value is less than (left side of) our target 
        if array[mid] < item:
            # make the starting point one more than the middle, and we will only look at the right side
            left = mid+1

        # if the middle value is greater than (right side of) our target 
        elif array[mid] > item:
            # starting point will not change, ending point will be one less than the current middle value. and we will only look at the left side
            right = mid - 1

        return binary_search_recursive(array, item, left, right)

    # after right crossed over left, if never found, return none
    return None