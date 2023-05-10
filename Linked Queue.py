class Node:
    """Class to represent a node in Python3"""

    def __init__(self, data):
        self.data = data  # Node value
        self.next = None  # Next node


class LinkedQueue:
    """Class to represent a Linked Queue(without priority) in Python3"""

    def __init__(self):
        self._front = None  # The first element of queue
        self._back = None  # The last element of queue
        self._size = 0  # The size of queue

    def enqueue(self, elem):
        """Inserts an element at the end of the queue"""
        if self._size == 0:
            aux = Node(elem)
            self._front = aux
            self._back = aux
        else:
            pointer = self._back
            aux = Node(elem)
            pointer.next = aux
            self._back = aux
        self._size += 1

    def dequeue(self):
        """Removes and returns the first element from the queue"""
        if self._size == 0:
            raise Exception("Empty queue")
        elem = self._front.data
        self._front = self._front.next
        self._size -= 1
        return elem

    def length(self):
        """Returns the size of queue"""
        return self._size

    def first(self):
        """Returns the first element from queue"""
        if self._size == 0:
            raise Exception("Empty queue")
        return self._front.data

    def last(self):
        """Returns the last element from queue"""
        if self._size == 0:
            raise Exception("Empty queue")
        return self._back.data

    def empty(self):
        """Returns true if the queue is empty, otherwise, it returns false"""
        if self._size == 0:
            return True
        return False

    def __del__(self):
        """Destructor method"""

    def __str__(self):
        """Method for representing the linked queue (user)"""
        rep = "\033[1;31m" + "first" + "\033[0;0m" + " -> "
        pointer = self._front
        while pointer != None:
            rep += f"{pointer.data} -> "
            if pointer.next is None:
                break
            pointer = pointer.next
        rep += "\033[1;34mNone\033[0;0m"
        return rep

    def __repr__(self):
        """Method for representing the linked queue (developer)"""
        return str(self)
