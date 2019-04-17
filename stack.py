#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) because we only have to change the linkedList tail's next property """
        # Push given item
        return self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if self.is_empty():
            return None
        return self.list.tail.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) because linkedList.delete method loops over all the nodes to find the item to delete """
        # Remove and return top item, if any
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            top = self.peek()
            self.list.delete(top)
            return top


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) to append to list"""
        # Insert given item
        return self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if self.is_empty():
            return None
        last_index = self.length() - 1
        return self.list[last_index]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) since python pop method runtime complexity is O(1)"""
        # Remove and return top item, if any

        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack