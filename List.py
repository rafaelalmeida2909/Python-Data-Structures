class List:
    """Class to represent a sequential static list in Python3"""

    def __init__(self, maximum):
        self.max = maximum  # The maximum stack size
        self._list = [None] * self._max  # Empty list
        self._size = 0  # The size of stack

    @property
    def max(self):
        """Getters to maximum table size"""
        return self._max

    @max.setter
    def max(self, maximum):
        """Setters to maximum table size"""
        if isinstance(maximum, int):
            self._max = maximum
        else:
            raise Exception("It is not a integer")

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
        if self._max == self._size:
            raise Exception("Full list")
        self._list[self._size] = elem
        self._size += 1

    def remove(self, elem):
        """Removes the first occurrence of the element from the list"""
        if self._size == 0:
            raise Exception("Empty list")
        index = self.index(elem)
        elem = None
        elem, self._list[index] = self._list[index], None
        for i in range(index, self._size-1, +1):
            self._list[i], self._list[i+1] = self._list[i+1], self._list[i]
        self._size -= 1

    def empty(self):
        """Returns true if the stack is empty, otherwise, it returns false"""
        if self._size == 0:
            return True
        return False

    def insert(self, index, elem):
        """Inserts a new element by index"""
        if self._max == self._size:
            raise Exception("Full list")
        if index < 0 and abs(index) >= self._size:
            index = 0
        elif index < 0:
            index = self._size + index
        if index < self._size:
            for i in range(self._size, index, -1):
                self._list[i], self._list[i-1] = self._list[i-1], self._list[i]
            self._list[index] = elem
            self._size += 1
        else:
            self.append(elem)

    def pop(self, index=None):
        """Removes and returns the last element from the list"""
        if self._size == 0:
            raise IndexError("Empty list")
        index = self.processIndex(index)
        elem, self._list[index] = self._list[index], None
        for i in range(index, self._size-1, +1):
            self._list[i], self._list[i+1] = self._list[i+1], self._list[i]
        self._size -= 1
        return elem

    def clear(self):
        """Restores the list to its starting point (Empty)"""
        for i in range(self._size):
            self._list[i] = None
        self._size = 0

    def count(self, elem):
        """Returns the number of elements with the specified value"""
        cont = 0
        for i in range(self._size):
            if self._list[i] == elem:
                cont += 1
        return cont

    def index(self, elem):
        """Returns the index of specified element"""
        for i in range(self._size):
            if self._list[i] == elem:
                return i
        raise ValueError(f"{elem} not in list")

    def reverse(self):
        """Reverses the original list"""
        if self._size == 0:
            raise IndexError("Empty list")
        final = self._size - 1
        for i in range((self._size//2)):
            self._list[i], self._list[final] = self._list[final], self._list[i]
            final -= 1

    def createReverse(self):
        """Creates and returns a reversed new list"""
        if self._size == 0:
            raise IndexError("Empty list")
        new = List(self._max)
        for i in range(self._size-1, -1, -1):
            new.append(self._list[i])
        return new

    def __len__(self):
        """Returns the size of list; Ex: len(obj)"""
        return self._size

    def __getitem__(self, index):
        """Returns an element that corresponding to the index; Ex: obj[index]"""
        index = self.processIndex(index)
        return self._list[index]

    def __setitem__(self, index, elem):
        """Sets the value by the index; Ex: obj[index] = value"""
        index = self.processIndex(index)
        self._list[index] = elem

    def __delitem__(self, index):
        """Removes an element that corresponding to the index; Ex: obj[index]"""
        if self._size == 0:
            raise IndexError("Empty list")
        if index >= self._size:
            raise IndexError("Index out of range")
        self._list[index] = None
        for i in range(index, self._size-1, +1):
            self._list[i], self._list[i+1] = self._list[i+1], self._list[i]
        self._size -= 1

    def __del__(self):
        """Destructor method"""

    def __str__(self):
        """Method to represent a list (user)"""
        tam = "\033[1;34m" + f"{self._max}" + "\033[0;0m"
        rep = f"List[{tam}] = "
        rep += f"{[self._list[x] for x in range(0, self._size)]}"
        return rep

    def __repr__(self):
        """Method to represent a list (developer)"""
        return str(self)
