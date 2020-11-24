class Node:
    """Representação de um nó em python. Com ele é possível criar uma lista encadeada"""
    def __init__(self, data):
        self.data = data # Valor do nó
        self.next = None # Próximo nó

class LinkedList:
    """Representação de uma lista encadeada em python, onde cada elemento, é uma instância da classe nó"""
    def __init__(self):
        self.first = None # Primeiro elemento da lista encadeada
        self._size = 0 # Define o nº de elementos na lista

    def getItemByIndex(self, index):
        """Método auxiliar que encontra o nó a partir do índice"""
        pointer = self.first
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Índice fora do intervalo")
        return pointer

    def append(self, elem):
        """Adiciona um novo nó ao final da lista"""
        if self.first: # Se não for None
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
    
    def pop(self, index):
        """Deleta um item da lista, baseado em seu índice e retorna o seu valor"""
        if self._size == 0:
            raise Exception("Lista vazia")
        if index >= self._size:
            raise IndexError("Índice fora do intervalo")
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

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):
        """Retorna o valor de um nó da lista a partir de um índice"""
        pointer = self.getItemByIndex(index)
        return pointer.data

    def __setitem__(self, index, elem):
        """Atribui um novo valor a um nó a partir de um índice"""
        pointer = self.getItemByIndex(index)
        pointer.data = elem

    def __delitem__(self, index):
        """Remove um nó da lista a partir de um índice"""
        if index == 0:
            pointer = self.getItemByIndex(index)
            self.first = pointer.next
        else:
            pointer = self.getItemByIndex(index-1)
            pointer.next = pointer.next.next
        self._size -= 1

    def __repr__(self):
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
