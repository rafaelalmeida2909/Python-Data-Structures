class Node:
    """Class to represent a node in Python3"""

    def __init__(self, data):
        self.data = data  # Node value
        self.next = None  # Next node


class LinkedList:
    """Class to represent a linked list in Python3"""

    def __init__(self):
        self._first = None  # First element of list
        self._size = 0  # The size of list

    def getItemByIndex(self, index):
        """Auxiliary method that returns the node by the index"""
        pointer = self._first
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Index out of range")
        return pointer

    def processIndex(self, index):
        """Auxiliary method that helps with negative indexs"""
        if index is None:
            index = self._size - 1
        elif index == self._size or abs(index) > self._size:
            raise IndexError("Index out of range")
        if index < 0:
            index = self._size + index
        return index

    def append(self, elem):
        """Appends a new element in the end of list"""
        if self._first:  # if is not None
            pointer = self._first
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self._first = Node(elem)
        self._size += 1

    def remove(self, elem):
        """Removes the first occurrence of the element from the list"""
        if self._size == 0:
            raise Exception("Empty list")
        index = self.index(elem)
        if index == 0:
            self._first = self._first.next
            self._size -= 1
        else:
            pointer = self.getItemByIndex(index-1)
            pointer.next = pointer.next.next
            self._size -= 1

    def empty(self):
        """Returns true if the stack is empty, otherwise, it returns false"""
        if self._size == 0:
            return True
        return False

    def insert(self, index, elem):
        """Inserts a new element by index"""
        if index < 0 and abs(index) > self._size:
            index = 0
        elif index < 0:
            index = self._size + index
        if index == 0:
            pointer = self.getItemByIndex(index)
            aux = Node(elem)
            aux.next, self._first = pointer, aux
            self._size += 1
        elif index < self._size:
            pointer = self.getItemByIndex(index-1)
            aux = Node(elem)
            aux.next, pointer.next = pointer.next, aux
            self._size += 1
        else:
            self.append(elem)

    def pop(self, index=None):
        """Removes and returns the last element from the list"""
        if self._size == 0:
            raise Exception("Empty list")
        index = self.processIndex(index)
        if index == 0:
            elem = self._first.data
            self._first = self._first.next
            self._size -= 1
            return elem
        pointer = self.getItemByIndex(index-1)
        elem = pointer.next.data
        pointer.next = pointer.next.next
        self._size -= 1
        return elem

    def clear(self):
        """Restores the list to its starting point (Empty)"""
        self._first = None
        self._size = 0

    def count(self, elem):
        """Returns the number of elements with the specified value"""
        pointer = self._first
        cont = 0
        while(pointer != None):
            if pointer.data == elem:
                cont += 1
            pointer = pointer.next
        return cont

    def index(self, elem):
        """Returns the index of specified element"""
        pointer = self._first
        cont = 0
        while(pointer):
            if pointer.data == elem:
                return cont
            else:
                pointer = pointer.next
                cont += 1
        raise ValueError(f"{elem} not in list")

    def reverse(self):
        """Reverses the original list"""
        if self._size == 0:
            raise IndexError("Empty list")
        for i in range(self._size-1, -1, -1):
            self.append(self.pop(i))

    def createReverse(self):
        """Creates and returns a reversed new list"""
        if self._size == 0:
            raise IndexError("Empty list")
        new = LinkedList()
        for i in range(self._size-1, -1, -1):
            new.append(self[i])
        return new

    def __len__(self):
        """Returns the size of list; Ex: len(obj)"""
        return self._size

    def __getitem__(self, index):
        """Returns an element that corresponding to the index; Ex: obj[index]"""
        index = self.processIndex(index)
        pointer = self.getItemByIndex(index)
        return pointer.data

    def __setitem__(self, index, elem):
        """Sets the value by the index; Ex: obj[index] = value"""
        index = self.processIndex(index)
        pointer = self.getItemByIndex(index)
        pointer.data = elem

    def __delitem__(self, index):
        """Removes an element that corresponding to the index; Ex: obj[index]"""
        index = self.processIndex(index)
        if index == 0:
            pointer = self.getItemByIndex(index)
            self._first = pointer.next
        else:
            pointer = self.getItemByIndex(index-1)
            pointer.next = pointer.next.next
        self._size -= 1

    def __del__(self):
        """Destructor method"""

    def __str__(self):
        """Method to represent a linked list (user)"""
        rep = "\033[1;31m" + "head" + "\033[0;0m" + " -> "
        pointer = self._first
        while(pointer != None):
            rep += f"{pointer.data} -> "
            if pointer.next is None:
                break
            pointer = pointer.next
        rep += "\033[1;34m" + "None" + "\033[0;0m"
        return rep

    def __repr__(self):
        """Method to represent a linked list (developer)"""
        return str(self)
