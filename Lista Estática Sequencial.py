class List:
    """Representação de uma Lista estática sequencial em Python3"""
    def __init__(self, maximum):
        self.max = maximum # Tamanho máximo da lista
        self.list = [None] * maximum # Lista iniciada com tamanho definido
        self._size = 0 # Indica lista inicialmente vazia

    @property
    def max(self):
        """Retorna o valor do atributo max"""
        return self._max

    @max.setter
    def max(self, maximum):
        """Garante que max tenha um valor inteiro"""
        if isinstance(maximum, int):
            self._max = maximum
        else:
            raise Exception("Atributo deve ser um número inteiro")

    def append(self, elem):
        """Adiciona um elemento ao final da lista"""
        if self.max == self._size:
            raise "Lista Cheia"
        self.list[self._size] = elem
        self._size += 1

    def remove(self, elem):
        """Deleta a primeira aparição de um elemento na lista"""
        if self._size == 0:
            raise "Lista vazia"
        index = self.index(elem)
        elem = None
        elem, self.list[index] = self.list[index], None
        for i in range(index, self._size-1, +1):
            self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
        self._size -= 1
    
    def empty(self):
        """Verifica se a lista está vazia"""
        if self._size == 0:
            return True
        return False

    def insert(self, index, elem):
        """Inserte um elemento em uma posição qualquer da lista"""
        if self.max == self._size:
            raise "Lista Cheia"
        if index >= self._size:
            self.append(elem)
            return
        for i in range(self._size, index, -1):
            self.list[i], self.list[i-1] = self.list[i-1], self.list[i]
        self.list[index] = elem
        self._size += 1

    def pop(self, index):
        """Deleta um item da lista, baseado em seu índice e retorna o seu valor"""
        if index >= self._size:
            raise IndexError("Index fora do intervalo da lista")
        if self._size == 0:
            raise IndexError("Lista vazia")
        elem, self.list[index] = self.list[index], None
        for i in range(index, self._size-1, +1):
            self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
        self._size -= 1
        return elem 

    def clear(self):
        """Restaura a lista para seu ponto inicial(Vazia)"""
        for i in range(self._size):
            self.list[i] = None
        self._size = 0

    def count(self, elem):
        """Conta o número de aparições de um determinado elemento na lista"""
        cont = 0
        for i in range(self._size):
            if self.list[i] == elem:
                cont += 1
        return cont
    
    def index(self, elem):
        """Retorna o primeiro index de um determinado elemento da lista"""
        for i in range(self._size):
            if self.list[i] == elem:
                return i
        raise ValueError(f"{elem} não está na lista.")

    def __len__(self):
        """Retorna a quantidade de elementos da lista"""
        return self._size

    def __getitem__(self, index):
        """Retorna o valor de uma posição da lista"""
        if index >= self._size or abs(index) > self._size:
            raise IndexError("Índice fora do intervalo da lista")
        if index < 0:
            return self.list[self._size+index]
        return self.list[index]

    def __setitem__(self, index, elem):
        """Atribuição de valor a uma posição qualquer da lista"""
        if index >= self._size or abs(index) > self._size:
            raise IndexError("Atribuição fora do intervalo da lista")
        if index < 0:
            self.list[self._size+index] = elem
        else:
            self.list[index] = elem

    def __delitem__(self, index):
        """Deleta um item da lista, baseado em seu índice"""
        if self._size == 0:
            raise IndexError("Lista vazia")
        if index >= self._size:
            raise IndexError("Index fora do intervalo da lista")
        self.list[index] = None
        for i in range(index, self._size-1, +1):
            self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
        self._size -= 1

    def __str__(self):
        """Representa a lista excluindo os obj NoneType"""
        tam = "\033[1;34m" + f"{self.max}" + "\033[0;0m"
        rep = f"Lista[{tam}] = "
        rep += f"{[self.list[x] for x in range(0, self._size)]}"
        return rep

    def __repr__(self):
    	return str(self)
    	