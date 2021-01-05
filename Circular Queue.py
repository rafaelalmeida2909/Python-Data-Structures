class Queue:
    """Representação de um estrutura de fila estática sequencial circular em Python3 (sem prioridade)"""

    def __init__(self, maximum):
        self.max = maximum  # Tamanho máximo da fila
        self.queue = [None] * maximum  # Fila iniciada com tamanho definido
        self._front = 0  # Define o elemento que deverá sair primeiro da fila
        self._size = 0  # Atributo privado que diz o nº de elementos na fila
        self._back = 0  # Define o último elemento da fila

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

    def enqueue(self, elem):
        """Adiciona um elemento ao fim da fila"""
        if self._size == self.max:  # Verifica se a fila está cheia
            raise Exception("Fila Cheia!")
        self.queue[self._back] = elem
        self._back = (self._back + 1) % self.max  # Garante uma fila circular
        self._size += 1

    def dequeue(self):
        """Retira o primeiro elemento da fila"""
        if self._size == 0:  # Verifica se a fila está vazia
            raise Exception("Fila Vazia!")
        elem = self.queue[self._front]
        self.queue[self._front] = None
        self._front = (self._front + 1) % self.max  # Garante uma fila circular
        self._size -= 1
        return elem

    def length(self):
        """Retorna a quantidade de elementos na fila"""
        return self._size

    def first(self):
        """Retorna o valor do primeiro elemento da fila"""
        if self._size == 0:
            raise Exception("Fila vazia")
        return self.queue[self._front]

    def last(self):
        """Retorna o valor do último elemento da fila"""
        if self._size == 0:
            raise Exception("Fila vazia")
        return self.queue[self._back-1]

    def empty(self):
        """Verifica se a lista está vazia"""
        if self._size == 0:
            return True
        return False

    def __del__(self):
        """Método destrutor"""

    def __str__(self):
        """Representa a fila excluindo os obj NoneType"""
        tam = f"\033[1;32m{self.max}\033[0;0m"
        rep = f"[{tam}]\033[1;31mfirst\033[0;0m -> "
        cont = self._front
        for _ in range(self._size):
            if cont == self.max:
                cont = 0
            rep += f"{self.queue[cont]} -> "
            cont += 1
        rep += "\033[1;34mNone\033[0;0m"
        return rep

    def __repr__(self):
        return str(self)
