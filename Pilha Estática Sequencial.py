class Stack:
    """Representação de uma Pilha estática sequencial em Python3"""
    def __init__(self, maximum):
        self.max = maximum # Define tamanho reservado para pilha
        self.stack = [None] * maximum # Pilha iniciada com tamanho definido
        self._size = 0 # Tamanho atual da pilha

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

    def push(self, elem):
        """Insere um elemento no topo da pilha"""
        if self._size == self.max:
            raise Exception("Pilha cheia")
        self.stack[self._size] = elem
        self._size += 1

    def pop(self):
        """Deleta um item do topo da pilha e retorna o seu valor"""
        if self._size == 0:
            raise Exception("Pilha vazia")
        elem, self.stack[self._size-1] = self.stack[self._size-1], None
        self._size -= 1
        return elem

    def top(self):
        """retorna o elemento no topo da pilha"""
        if self._size == 0:
            raise Exception("Pilha vazia")
        return self.stack[self._size-1]

    def empty(self):
        """Verifica se a pilha está vazia"""
        if self._size == 0:
            return True
        return False
    
    def full(self):
        """Verifica se a pilha está cheia"""
        if self._size == self.max:
            return True
        return False
    
    def length(self):
        """Retorna o tamanho da pilha"""
        return self._size

    def __repr__(self):
        """Representa a pilha excluindo os obj NoneType"""
        rep = "\033[1;34m" + "topo -> " + "\033[0;0m"
        if self._size == 0:
            rep += "None"
            return rep
        for i in range(self._size-1, -1, -1):
            if self.stack[i] == None:
                pass
            elif i == self._size-1:
                rep += f"{str(self.stack[i]).rjust(2)}"
            elif i == 0:
                rep += f"\n{str(self.stack[i]).rjust(10)}"
            else:
                rep += f"\n{str(self.stack[i]).rjust(10)}"
        return rep
        