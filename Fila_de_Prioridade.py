"""
FILA DE PRIORIDADE:
    É o mesmo conceito das filas, porém os itens são ordenados por valor-chave, de modo que o item com a chave mais baixa/alta
    esteja sempre no inicio da fila.
    Elementos de alta prioridade são colocados no inicio da fila, média prioridade no meio da fila e elementos de baixa prioridade
    no final da fila.
"""
import numpy as np

class FilaPrioridade:

    def __init__(self, capacidade):
        self.capacidade  = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0  # outra maneira de se criar um if[...] return True

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos - 1]

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return

        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos -1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x+1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x+1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return

        valor = self.valores[self.numero_elementos -1]
        self.numero_elementos -= 1
        return valor

fila = FilaPrioridade(5)
print(fila.primeiro())

fila.enfileirar(30)
fila.enfileirar(50)
fila.enfileirar(10)
fila.enfileirar(40)
fila.enfileirar(20)
print(fila.valores)

#testes para desenfileirar
print('-----------')
fila.desenfileirar()
print(fila.primeiro())  #inicio passa a ser 20

print('-----------')
fila.desenfileirar()
print(fila.primeiro())

print('-----------')
fila.enfileirar(5)
print(fila.primeiro())
