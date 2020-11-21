class Lista:
    def __init__(self, maximo):
        self.max = maximo # Tamanho máximo da lista
        self.lista = [None] * maximo # Lista iniciada com tamanho definido
        self._quantidade = 0 # Indica lista inicialmente vazia

    @property
    def max(self):
        """Retorna o valor do atributo max"""
        return self._max

    @max.setter
    def max(self, maximo):
        """Garante que max tenha um valor inteiro"""
        if isinstance(maximo, int):
            self._max = maximo
        else:
            raise Exception("Atributo deve ser um número inteiro")

    def append(self, elem):
        """Adiciona um elemento ao final da lista"""
        if self.max == self._quantidade:
            raise "Lista Cheia"
        self.lista[self._quantidade] = elem
        self._quantidade += 1

    def remove(self, elem):
        """Deleta a primeira aparição de um elemento na lista"""
        if self._quantidade == 0:
            raise "Lista vazia"
        index = self.index(elem)
        elem = None
        elem, self.lista[index] = self.lista[index], None
        for i in range(index, self._quantidade-1, +1):
            self.lista[i], self.lista[i+1] = self.lista[i+1], self.lista[i]
        self._quantidade -= 1

    def insert(self, index, elem):
        """Inserte um elemento em uma posição qualquer da lista"""
        if self.max == self._quantidade:
            raise "Lista Cheia"
        if index >= self._quantidade:
            self.append(elem)
            return
        for i in range(self._quantidade, index, -1):
            self.lista[i], self.lista[i-1] = self.lista[i-1], self.lista[i]
        self.lista[index] = elem
        self._quantidade += 1

    def pop(self, index):
        """Deleta um item da lista, baseado em seu índice e retorna o seu valor"""
        if index >= self._quantidade:
            raise IndexError("Index fora do intervalo da lista")
        if self._quantidade == 0:
            raise IndexError("Lista vazia")
        elem, self.lista[index] = self.lista[index], None
        for i in range(index, self._quantidade-1, +1):
            self.lista[i], self.lista[i+1] = self.lista[i+1], self.lista[i]
        self._quantidade -= 1
        return elem 

    def clear(self):
        """Restaura a lista para seu ponto inicial(Vazia)"""
        for i in range(self._quantidade):
            self.lista[i] = None
        self._quantidade = 0

    def count(self, elem):
        """Conta o número de aparições de um determinado elemento na lista"""
        cont = 0
        for i in range(self._quantidade):
            if self.lista[i] == elem:
                cont += 1
        return cont
    
    def index(self, elem):
        """Retorna o primeiro index de um determinado elemento da lista"""
        for i in range(self._quantidade):
            if self.lista[i] == elem:
                return i
        raise ValueError(f"{elem} não está na lista.")

    def __len__(self):
        """Retorna a quantidade de elementos da lista"""
        return self._quantidade

    def __getitem__(self, index):
        """Retorna o valor de uma posição da lista"""
        if index >= self._quantidade or abs(index) > self._quantidade:
            raise IndexError("Índice fora do intervalo da lista")
        if index < 0:
            return self.lista[self._quantidade+index]
        return self.lista[index]

    def __setitem__(self, index, elem):
        """Atribuição de valor a uma posição qualquer da lista"""
        if index >= self._quantidade or abs(index) > self._quantidade:
            raise IndexError("Atribuição fora do intervalo da lista")
        if index < 0:
            self.lista[self._quantidade+index] = elem
        else:
            self.lista[index] = elem

    def __delitem__(self, index):
        """Deleta um item da lista, baseado em seu índice"""
        if self._quantidade == 0:
            raise IndexError("Lista vazia")
        if index >= self._quantidade:
            raise IndexError("Index fora do intervalo da lista")
        self.lista[index] = None
        for i in range(index, self._quantidade-1, +1):
            self.lista[i], self.lista[i+1] = self.lista[i+1], self.lista[i]
        self._quantidade -= 1

    def __repr__(self):
        """Representa a lista excluindo os obj NoneType"""
        tam = "\033[1;34m" + f"{self.max}" + "\033[0;0m"
        rep = f"Lista[{tam}] = "
        rep += f"{[self.lista[x] for x in range(0, self._quantidade)]}"
        return rep
