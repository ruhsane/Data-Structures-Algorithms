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
    if array[index] == item:
        return index
    elif index < len(array) -1 :
        index += 1
        return linear_search_recursive(array, item, index)
    return None


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

    while left != right:
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

    if array[left] == item:
        return left
    else:
        return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

  
    # this only runs first iteration
    if left == None and right == None:
        left = 0
        right = len(array) - 1
    
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

    # check if we are now only looking at one last thing in the array
    if left == right :
        # check if the last thing is the item we are looking for
        if item == array[left]:
            return left
        # if the last item is not the item we are looking for, means the item is not in the list
        return None

    return binary_search_recursive(array, item, left, right)
