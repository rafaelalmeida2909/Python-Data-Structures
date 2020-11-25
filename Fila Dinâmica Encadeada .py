class Node:
    """Representação de um nó em Python3. Com ele é possível criar uma fila encadeada"""
    def __init__(self, data):
        self.data = data # Valor do nó
        self.next = None # Próximo nó

class LinkedQueue:
    """Representação de um estrutura de fila dinâmica encadeada em Python3 (sem prioridade)"""
    def __init__(self):
        self.front = None # Define o elemento que deverá sair primeiro da fila
        self.back = None # Define o último elemento da fila
        self._size = 0 # Atributo privado que diz o nº de elementos na fila

    def enqueue(self, elem):
        """Adiciona um elemento ao fim da fila"""
        if self._size == 0:
            aux = Node(elem)
            self.front = aux
            self.back = aux
        else:
            pointer = self.back
            aux = Node(elem)
            pointer.next = aux
            self.back = aux
        self._size += 1

    def dequeue(self):
        """Retira o primeiro elemento da fila"""
        if self._size == 0:
            raise Exception("Fila vazia")
        elem = self.front.data
        self.front = self.front.next
        self._size -= 1
        return elem
    
    def length(self):
        """Retorna a quantidade de elementos na fila"""
        return self._size

    def peek(self):
        """Retorna o valor do primeiro elemento da fila"""
        if self._size == 0:
            raise Exception("Fila vazia")
        return self.front.data

    def empty(self):
        """Verifica se a fila está ou não vazia"""
        if self._size == 0:
            return True
        return False

    def __repr__(self):
        """Método para representação da fila encadeada"""
        rep = "\033[1;31m" + "frente" + "\033[0;0m" + " -> "
        pointer = self.front
        while(pointer != None):
            rep += f"{pointer.data} -> "
            if pointer.next is None:
                break
            pointer = pointer.next
        rep += "\033[1;34m" + "None" + "\033[0;0m"
        return rep
