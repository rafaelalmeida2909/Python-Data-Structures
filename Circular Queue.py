class Queue:
    """Class to represent a circular sequencial static in Python3 (without priority)"""

    def __init__(self, maximum):
        self.max = maximum  # The maximum queue size
        self._queue = [None] * maximum  # Empty queue
        self._front = 0  # The first element of queue
        self._size = 0  # The size of queue
        self._back = 0  # The last element of queue

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
            raise Exception("Atributo deve ser um número inteiro")

    def enqueue(self, elem):
        """Appends a new element in the end of queue"""
        if self._size == self.max:  # Verifys if the queue is full
            raise Exception("Full queue!")
        self._queue[self._back] = elem
        self._back = (self._back + 1) % self.max  # Ensures a circular queue
        self._size += 1

    def dequeue(self):
        """Removes the first element from the queue"""
        if self._size == 0:  # Verifys if the queue is empty
            raise Exception("Empty queue")
        elem = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % self.max  # Ensures a circular queue
        self._size -= 1
        return elem

    def length(self):
        """Returns the size of queue"""
        return self._size

    def first(self):
        """Returns the first element from queue"""
        if self._size == 0:
            raise Exception("Empty queue")
        return self._queue[self._front]

    def last(self):
        """Returns the last element from queue"""
        if self._size == 0:
            raise Exception("Empty queue")
        return self._queue[self._back-1]

    def empty(self):
        """Verifys if the queue is empty"""
        if self._size == 0:
            return True
        return False

    def __del__(self):
        """Destructor method"""

    def __str__(self):
        """Method for representing the queue, excluding NoneType objects (user)"""
        tam = f"\033[1;32m{self.max}\033[0;0m"
        rep = f"[{tam}]\033[1;31mfirst\033[0;0m -> "
        cont = self._front
        for _ in range(self._size):
            if cont == self.max:
                cont = 0
            rep += f"{self._queue[cont]} -> "
            cont += 1
        rep += "\033[1;34mNone\033[0;0m"
        return rep

    def __repr__(self):
        """Method for representing the queue, excluding NoneType objects (developer)"""
        return str(self)
