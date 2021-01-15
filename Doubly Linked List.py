class Node:
    """Class to represent a node in Python3"""

    def __init__(self, data):
        self.data = data  # Node value
        self.next = None  # Next node
        self.prev = None  # Previus node


class DoublyLinkedList:
    """Class to represent a doubly linked list in Python3"""

    def __init__(self):
        self._first = None  # First element of list
        self._last = None  # Last element of list
        self._size = 0  # The size of list

    def getItemByIndex(self, index):
        """Auxiliary method that returns the node by the index"""
        if index < 0:
            index = self._size + index
        pointer = self._first
        for _ in range(index):
            if pointer.next:
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
        node = Node(elem)
        if self._first:  # if is not None
            self._last.next = node
            node.prev = self._last
            node.next = None
            self._last = node
        else:
            self._first = self._last = node
        self._size += 1

    def remove(self, elem):
        """Removes the first occurrence of the element from the list"""
        if self._size == 0:
            raise Exception("Empty list")
        index = self.index(elem)
        del self[index]

    def empty(self):
        """Returns true if the stack is empty, otherwise, it returns false"""
        if self._size == 0:
            return True
        return False

    def insert(self, index, elem):
        """Inserts a new element by index"""
        node = Node(elem)
        if index < 0 and abs(index) > self._size:
            index = 0
        elif index < 0:
            index = self._size + index
        if self._size == 0 or index >= self._size:
            self.append(elem)
        elif index == 0:
            node.next = self._first
            self._first.prev = node
            self._first = node
            self._size += 1
        elif index > 0:
            node_next = self.getItemByIndex(index)
            node_prev = self.getItemByIndex(index-1)
            node.next = node_next
            node.prev = node_prev
            node_next.prev = node
            node_prev.next = node
            self._size += 1
        else:
            raise IndexError("Index out of range")

    def pop(self, index=None):
        """Removes and returns the last element from the list"""
        if self._size == 0:
            raise Exception("Empty list")
        index = self.processIndex(index)
        if self._size == 1:
            elem = self._last.data
            self.clear()
        else:
            elem = self.getItemByIndex(index).data
            del self[index]
        return elem

    def clear(self):
        """Restores the list to its starting point (Empty)"""
        self._first = None
        self._last = None
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
        pointer = self._first
        while(pointer):
            pointer.next, pointer.prev = pointer.prev, pointer.next
            pointer = pointer.prev
        self._first, self._last = self._last, self._first

    def createReversed(self):
        """Creates and returns a reversed new list"""
        if self._size == 0:
            raise IndexError("Empty list")
        new = DoublyLinkedList()
        pointer = self._last
        while(pointer):
            new.append(pointer.data)
            pointer = pointer.prev
        return new

    def __len__(self):
        """Returns the size of list; Ex: len(obj)"""
        return self._size

    def __getitem__(self, index):
        """Returns an element that corresponding to the index; Ex: obj[index]"""
        if self._size == 0:
            raise IndexError("Empty list")
        index = self.processIndex(index)
        pointer = self.getItemByIndex(index)
        return pointer.data

    def __setitem__(self, index, elem):
        """Sets the value by the index; Ex: obj[index] = value"""
        if self._size == 0:
            raise IndexError("Empty list")
        index = self.processIndex(index)
        pointer = self.getItemByIndex(index)
        pointer.data = elem

    def __delitem__(self, index):
        """Removes an element that corresponding to the index; Ex: obj[index]"""
        if self._size == 0:
            raise IndexError("Empty list")
        index = self.processIndex(index)
        if index == 0:
            self._first = self._first.next
            self._first.prev = None
        elif index == self._size-1:
            self._last = self._last.prev
            self._last.next = None
        else:
            node_next = self.getItemByIndex(index+1)
            node_prev = self.getItemByIndex(index-1)
            node_next.prev = node_prev
            node_prev.next = node_next
        self._size -= 1

    def __del__(self):
        """Destructor method"""

    def __str__(self):
        """Method to represent a doubly linked list (user)"""
        if self._size == 0:
            return "\033[1;34mNone\033[0;0m" + " <-> " + "\033[1;34mNone\033[0;0m"
        rep = "\033[1;34mNone\033[0;0m" + " <- {} " + "\033[1;34mNone\033[0;0m"
        pointer = self._first
        aux = ""
        while(pointer != None):
            if pointer == self._first and pointer.next is None:
                aux += "\033[1;31m" + str(pointer.data) + "\033[0;0m" + " -> "
                break
            elif pointer.next is None:
                aux += f"{pointer.data} -> "
                break
            else:
                if self._first == pointer:
                    aux += "\033[1;31m" + \
                        str(pointer.data) + "\033[0;0m" + " <-> "
                else:
                    aux += f"{pointer.data} <-> "
                pointer = pointer.next
        rep = rep.format(aux)
        return rep

    def __repr__(self):
        """Method to represent a doubly linked list (developer)"""
        return str(self)
