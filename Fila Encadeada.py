class No:
    """Representação de um nó em python. Com ele é possível criar uma fila encadeada"""
    def __init__(self, data):
        self.data = data # Valor do nó
        self.prox = None # Próximo nó

class FilaEncadeada:
    """Representaçãõ de um estrutura de fila encadeada em python (sem prioridade)"""
    def __init__(self):
        self.inicio = None # Define o elemento que deverá sair primeiro da fila
        self.final = None # Define o último elemento da fila
        self._quantidade = 0 # Atributo privado que diz o nº de elementos na fila

    def enfileirar(self, elem):
        """Adiciona um elemento ao fim da fila"""
        if self._quantidade == 0:
            aux = No(elem)
            self.inicio = aux
            self.final = aux
        else:
            ponteiro = self.final
            aux = No(elem)
            ponteiro.prox = aux
            self.final = aux
        self._quantidade += 1

    def desenfileirar(self):
        """Retira o primeiro elemento da fila"""
        if self._quantidade == 0:
            raise Exception("Lista vazia")
        self.inicio = self.inicio.prox
        self._quantidade -= 1
    
    def tamanho(self):
        """Retorna a quantidade de elementos na fila"""
        return self._quantidade

    def consulta(self):
        """Retorna o valor do primeiro elemento da fila"""
        if self.vazia():
            raise Exception("Lista vazia")
        return self.inicio.data

    def vazia(self):
        """Verifica se a lista está ou não vazia"""
        if self._quantidade == 0:
            return True
        return False

    def __repr__(self):
        """Método para representação da fila encadeada"""
        rep = "\033[1;31m" + "frente" + "\033[0;0m" + " -> "
        ponteiro = self.inicio
        while(ponteiro != None):
            rep += f"{ponteiro.data} -> "
            if ponteiro.prox is None:
                break
            ponteiro = ponteiro.prox
        rep += "\033[1;34m" + "None" + "\033[0;0m"
        return rep