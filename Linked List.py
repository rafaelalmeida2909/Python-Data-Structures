class Node:
    """Representação de um nó em Python3. Com ele é possível criar uma lista encadeada"""

    def __init__(self, data):
        self.data = data  # Valor do nó
        self.next = None  # Próximo nó


class LinkedList:
    """Representação de uma lista dinâmica encadeada em Python3, onde cada elemento, é uma instância da classe nó"""

    def __init__(self):
        self.first = None  # Primeiro elemento da lista encadeada
        self._size = 0  # Define o nº de elementos na lista

    def getItemByIndex(self, index):
        """Método auxiliar que encontra o nó a partir do índice"""
        pointer = self.first
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Índice fora do intervalo")
        return pointer

    def processIndex(self, index):
        """Método auxiliar que garante o funcionamento dos métodos com índice negativo"""
        if index is None:
            index = self._size - 1
        elif index == self._size or abs(index) > self._size:
            raise IndexError("Índice inválido")
        if index < 0:
            index = self._size + index
        return index

    def append(self, elem):
        """Adiciona um novo nó ao final da lista"""
        if self.first:  # Se não for None
            pointer = self.first
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.first = Node(elem)
        self._size += 1

    def remove(self, elem):
        """Deleta a primeira aparição de um elemento na lista"""
        if self._size == 0:
            raise Exception("Lista Vazia")
        index = self.index(elem)
        if index == 0:
            self.first = self.first.next
            self._size -= 1
        else:
            pointer = self.getItemByIndex(index-1)
            pointer.next = pointer.next.next
            self._size -= 1

    def empty(self):
        """Verifica se a lista está vazia"""
        if self._size == 0:
            return True
        return False

    def insert(self, index, elem):
        """Insere um novo nó a partir de um índice"""
        if index < 0 and abs(index) > self._size:
            index = 0
        elif index < 0:
            index = self._size + index
        if index == 0:
            pointer = self.getItemByIndex(index)
            aux = Node(elem)
            aux.next, self.first = pointer, aux
            self._size += 1
        elif index < self._size:
            pointer = self.getItemByIndex(index-1)
            aux = Node(elem)
            aux.next, pointer.next = pointer.next, aux
            self._size += 1
        else:
            self.append(elem)

    def pop(self, index=None):
        """Deleta um item da lista, baseado em seu índice e retorna o seu valor"""
        if self._size == 0:
            raise Exception("Lista vazia")
        index = self.processIndex(index)
        if index == 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem
        pointer = self.getItemByIndex(index-1)
        elem = pointer.next.data
        pointer.next = pointer.next.next
        self._size -= 1
        return elem

    def clear(self):
        """Restaura a lista para seu ponto inicial(Vazia)"""
        self.first = None
        self._size = 0

    def count(self, elem):
        """Conta o número de aparições de um determinado elemento na lista"""
        pointer = self.first
        cont = 0
        while(pointer != None):
            if pointer.data == elem:
                cont += 1
            pointer = pointer.next
        return cont

    def index(self, elem):
        """Retorna o índice da primeira aparição de um elemento"""
        pointer = self.first
        cont = 0
        while(pointer):
            if pointer.data == elem:
                return cont
            else:
                pointer = pointer.next
                cont += 1
        raise ValueError(f"{elem} não está na lista")

    def reverse(self):
        """Inverte lista original"""
        if self._size == 0:
            raise IndexError("Lista vazia")
        for i in range(self._size-1, -1, -1):
            self.append(self.pop(i))

    def createReverse(self):
        """Cria lista invertida em novo objeto"""
        if self._size == 0:
            raise IndexError("Lista vazia")
        new = LinkedList()
        for i in range(self._size-1, -1, -1):
            new.append(self[i])
        return new

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):
        """Retorna o valor de um nó da lista a partir de um índice"""
        index = self.processIndex(index)
        pointer = self.getItemByIndex(index)
        return pointer.data

    def __setitem__(self, index, elem):
        """Atribui um novo valor a um nó a partir de um índice"""
        index = self.processIndex(index)
        pointer = self.getItemByIndex(index)
        pointer.data = elem

    def __delitem__(self, index):
        """Remove um nó da lista a partir de um índice"""
        index = self.processIndex(index)
        if index == 0:
            pointer = self.getItemByIndex(index)
            self.first = pointer.next
        else:
            pointer = self.getItemByIndex(index-1)
            pointer.next = pointer.next.next
        self._size -= 1

    def __del__(self):
        """Método destrutor invocado sempre que o código é finalizado"""

    def __str__(self):
        """Método para representação da lista encadeada"""
        rep = "\033[1;31m" + "head" + "\033[0;0m" + " -> "
        pointer = self.first
        while(pointer != None):
            rep += f"{pointer.data} -> "
            if pointer.next is None:
                break
            pointer = pointer.next
        rep += "\033[1;34m" + "None" + "\033[0;0m"
        return rep

    def __repr__(self):
        return str(self)
