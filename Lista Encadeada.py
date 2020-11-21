class No:
    """Representação de um nó em python. Com ele é possível criar uma lista encadeada"""
    def __init__(self, data):
        self.data = data # Valor do nó
        self.prox = None # Próximo nó

class ListaEncadeada:
    """Representação de uma lista encadeada em python, onde cada elemento, é uma instância da classe nó"""
    def __init__(self):
        self.primeiro = None # Primeiro elemento da lista encadeada
        self._quantidade = 0 # Define o nº de elementos na lista

    def getItemByIndex(self, index):
        """Método auxiliar que encontra o nó a partir do índice"""
        ponteiro = self.primeiro
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.prox
            else:
                raise IndexError("Índice fora do intervalo")
        return ponteiro

    def append(self, elem):
        """Adiciona um novo nó ao final da lista"""
        if self.primeiro: # Se não for None
            ponteiro = self.primeiro
            while(ponteiro.prox):
                ponteiro = ponteiro.prox
            ponteiro.prox = No(elem)
        else:
            self.primeiro = No(elem)
        self._quantidade += 1

    def remove(self, elem):
        """Deleta a primeira aparição de um elemento na lista"""
        if self.empty():
            raise Exception("Lista Vazia")
        index = self.index(elem)
        if index == 0:
            self.primeiro = self.primeiro.prox
            self._quantidade -= 1
        else:
            ponteiro = self.getItemByIndex(index-1)
            ponteiro.prox = ponteiro.prox.prox
            self._quantidade -= 1

    def empty(self):
        """Verifica se a lista está vazia"""
        if self._quantidade == 0:
            return True
        return False

    def insert(self, index, elem):
        """Insere um novo nó a partir de um índice"""
        if index == 0:
            ponteiro = self.getItemByIndex(index)
            aux = No(elem)
            aux.prox, self.primeiro = ponteiro, aux
            self._quantidade += 1
        elif index < self._quantidade:
            ponteiro = self.getItemByIndex(index-1)
            aux = No(elem)
            aux.prox, ponteiro.prox = ponteiro.prox, aux
            self._quantidade += 1
        else:
            self.append(elem)
    
    def pop(self, index):
        """Deleta um item da lista, baseado em seu índice e retorna o seu valor"""
        if self.empty():
            raise Exception("Lista vazia")
        if index >= self._quantidade:
            raise IndexError("Índice fora do intervalo")
        if index == 0:
            elem = self.primeiro.data
            self.primeiro = self.primeiro.prox
            self._quantidade -= 1
            return elem
        ponteiro = self.getItemByIndex(index-1)
        elem = ponteiro.prox.data
        ponteiro.prox = ponteiro.prox.prox
        self._quantidade -= 1
        return elem

    def clear(self):
        """Restaura a lista para seu ponto inicial(Vazia)"""
        self.primeiro = None
        self._quantidade = 0

    def count(self, elem):
        """Conta o número de aparições de um determinado elemento na lista"""
        ponteiro = self.primeiro
        cont = 0
        while(ponteiro != None):
            if ponteiro.data == elem:
                cont += 1
            ponteiro = ponteiro.prox
        return cont

    def index(self, elem):
        """Retorna o índice da primeira aparição de um elemento"""
        ponteiro = self.primeiro
        cont = 0
        while(ponteiro):
            if ponteiro.data == elem:
                return cont
            else:
                ponteiro = ponteiro.prox
                cont += 1
        raise ValueError(f"{elem} não está na lista")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._quantidade

    def __getitem__(self, index):
        """Retorna o valor de um nó da lista a partir de um índice"""
        ponteiro = self.getItemByIndex(index)
        return ponteiro.data

    def __setitem__(self, index, elem):
        """Atribui um novo valor a um nó a partir de um índice"""
        ponteiro = self.getItemByIndex(index)
        ponteiro.data = elem

    def __delitem__(self, index):
        """Remove um nó da lista a partir de um índice"""
        if index == 0:
            ponteiro = self.getItemByIndex(index)
            self.primeiro = ponteiro.prox
        else:
            ponteiro = self.getItemByIndex(index-1)
            ponteiro.prox = ponteiro.prox.prox
        self._quantidade -= 1

    def __repr__(self):
        """Método para representação da lista encadeada"""
        rep = "\033[1;31m" + "head" + "\033[0;0m" + " -> "
        ponteiro = self.primeiro
        while(ponteiro != None):
            rep += f"{ponteiro.data} -> "
            if ponteiro.prox is None:
                break
            ponteiro = ponteiro.prox
        rep += "\033[1;34m" + "None" + "\033[0;0m"
        return rep
