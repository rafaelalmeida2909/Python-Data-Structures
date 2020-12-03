class Node:
    """Representação de um nó em Python3. Com ele é possível criar uma pilha encadeada"""

    def __init__(self, data):
        self.data = data  # Valor do nó
        self.next = None  # Próximo nó


class LinkedStack:
    """Representação de uma pilha dinâmica encadeada em Python3"""

    def __init__(self):
        self._top = None  # Define o topo da pilha
        self._size = 0  # Tamanho atual da pilha

    def push(self, elem):
        """Insere um elemento no topo da pilha"""
        if self._size == 0:
            self._top = Node(elem)
        else:
            aux = self._top
            self._top = Node(elem)
            self._top.next = aux
        self._size += 1

    def pop(self):
        """Deleta um item do topo da pilha e retorna o seu valor"""
        if self._size == 0:
            raise Exception("Pilha vazia")
        elem, self._top = self._top.data, self._top.next
        self._size -= 1
        return elem

    def top(self):
        """retorna o elemento no topo da pilha"""
        if self._size == 0:
            raise Exception("Pilha vazia")
        return self._top.data

    def empty(self):
        """Verifica se a pilha está vazia"""
        if self._size == 0:
            return True
        return False

    def length(self):
        """Retorna o tamanho da pilha"""
        return self._size

    def __del__(self):
        """Método destrutor"""

    def __str__(self):
        """Representa a pilha excluindo os obj NoneType"""
        rep = "\033[1;34m" + "topo -> " + "\033[0;0m"
        if self._size == 0:
            rep += "None"
            return rep
        pointer = self._top
        for i in range(self._size):
            if i == 0:
                rep += f"{str(pointer.data).rjust(2)}"
            else:
                rep += f"\n{str(pointer.data).rjust(10)}"
            pointer = pointer.next
        return rep

    def __repr__(self):
        return str(self)
