class Node:
    """Representação de um nó em Python3. Com ele é possível criar uma lista duplamente encadeada"""

    def __init__(self, data):
        self.data = data  # Valor do nó
        self.next = None  # Próximo nó
        self.prev = None  # Nó anterior


class DoublyLinkedList:
    """Representação de uma lista dinâmica duplamente encadeada em Python3, onde cada elemento, é uma instância da classe nó"""

    def __init__(self):
        self.first = None  # Primeiro elemento da lista
        self.last = None  # Ultimo elemento da lista
        self._size = 0  # Define o nº de elementos na lista

    def getItemByIndex(self, index):
        """Método auxiliar que encontra o nó a partir do índice"""
        if index < 0:
            index = self._size + index
        pointer = self.first
        for i in range(index):
            if pointer.next:
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
        node = Node(elem)
        if self.first:  # Se não for None
            self.last.next = node
            node.prev = self.last
            node.next = None
            self.last = node
        else:
            self.first = self.last = node
        self._size += 1

    def remove(self, elem):
        """Deleta a primeira aparição de um elemento na lista"""
        if self._size == 0:
            raise Exception("Lista Vazia")
        index = self.index(elem)
        del self[index]

    def empty(self):
        """Verifica se a lista está vazia"""
        if self._size == 0:
            return True
        return False

    def insert(self, index, elem):
        """Insere um novo nó a partir de um índice"""
        node = Node(elem)
        if index < 0 and abs(index) > self._size:
            index = 0
        elif index < 0:
            index = self._size + index
        if self._size == 0 or index >= self._size:
            self.append(elem)
        elif index == 0:
            node.next = self.first
            self.first.prev = node
            self.first = node
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
            raise IndexError("Indíce inválido")

    def pop(self, index=None):
        """Deleta o último item da lista e retorna o seu valor"""
        if self._size == 0:
            raise Exception("Lista vazia")
        index = self.processIndex(index)
        if self._size == 1:
            elem = self.last.data
            self.clear()
        else:
            elem = self.getItemByIndex(index).data
            del self[index]
        return elem

    def clear(self):
        """Restaura a lista para seu ponto inicial(Vazia)"""
        self.first = None
        self.last = None
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
        """Retorna o índice da primeira aparição de um elemento na lista"""
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
        pointer = self.first
        while(pointer):
            pointer.next, pointer.prev = pointer.prev, pointer.next
            pointer = pointer.prev
        self.first, self.last = self.last, self.first

    def createReverse(self):
        """Cria lista invertida em novo objeto"""
        if self._size == 0:
            raise IndexError("Lista vazia")
        new = DoublyLinkedList()
        pointer = self.last
        while(pointer):
            new.append(pointer.data)
            pointer = pointer.prev
        return new

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):
        """Retorna o valor de um nó da lista a partir de um índice"""
        if self._size == 0:
            raise IndexError("Lista vazia")
        index = self.processIndex(index)
        pointer = self.getItemByIndex(index)
        return pointer.data

    def __setitem__(self, index, elem):
        """Atribui um novo valor a um nó a partir de um índice"""
        if self._size == 0:
            raise IndexError("Lista vazia")
        index = self.processIndex(index)
        pointer = self.getItemByIndex(index)
        pointer.data = elem

    def __delitem__(self, index): # testar indice negativo
        """Remove um nó da lista a partir de um índice"""
        if self._size == 0:
            raise IndexError("Lista vazia")
        index = self.processIndex(index)
        if index == 0:
            self.first = self.first.next
            self.first.prev = None
        elif index == self._size-1:
            self.last = self.last.prev
            self.last.next = None
        else:
            node_next = self.getItemByIndex(index+1)
            node_prev = self.getItemByIndex(index-1)
            node_next.prev = node_prev
            node_prev.next = node_next
        self._size -= 1

    def __del__(self):
        """Método destrutor"""

    def __str__(self):
        """Método para representação da lista encadeada"""
        rep = "\033[1;34mNone\033[0;0m" + " <- {} " + "\033[1;34mNone\033[0;0m"
        pointer = self.first
        aux = ""
        while(pointer != None):
            if pointer == self.first and pointer.next is None:
                aux += "\033[1;31m" + str(pointer.data) + "\033[0;0m" + " -> "
                break
            elif pointer.next is None:
                aux += f"{pointer.data} -> "
                break
            else:
                if self.first == pointer:
                    aux += "\033[1;31m" + \
                        str(pointer.data) + "\033[0;0m" + " <-> "
                else:
                    aux += f"{pointer.data} <-> "
                pointer = pointer.next
        rep = rep.format(aux)
        return rep

    def __repr__(self):
        return str(self)
