"""
FILAS- Seguem uma estrutura semelhante às pilhas, porem a fila é do tipo FIFO - first in, first out

OPERAÇÕES:
 - enfileirar: Colocar um item no final da fila
 - desenfileirar: remover um item do inicio da fila
 - ver inicio da fila: mostra o elemento que está no inicio da fila

Uma fila pode ser circular, ou seja, num array de 5 posições (indice de 0 a 4), o ultimo elemento está no indice 4, porém após
diversos desenfileiramentos, o indice 4 se torna o inicio da fila e o indice 3 é o
ultimo elemento (tendo sido inseridos posteriormente às exclusões)

"""
import numpy as np

class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0   #outra maneira de se criar um if[...] return True

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self,valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        """
        Caso ele chegue no final da fila, irá retornar ao inicio (indice 0), ou seja, se ele atingiu o máximo da direita,
        o cursor voltará à extrema esquerda
        """
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]

fila = FilaCircular(5)

print(fila.primeiro())

fila.enfileirar(1)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
fila.enfileirar(6)
print(fila.primeiro())

fila.enfileirar(2)

print(fila.valores)
print('---------')
#desenfileirando
fila.desenfileirar()
fila.desenfileirar()
print(fila.primeiro())

fila.enfileirar(7)
fila.enfileirar(8)

print(fila.valores)
