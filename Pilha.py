"""
Ideia de encadeiamento em pilha seguindo o LIFO- 'Last in, first out'
 - permite acesso ao ultimo item de dados: o ultimo item a ser inserido
 - se o ultimo item for removido, o item anterior ao ultimo inserido poderá ser acessado, se tornando o novo ultimo

Operações:
 - Empilhar: colocar um item de dados no topo da pilha/
 - Desempilhar: retirar um item de dados do topo da pilha;
 - Ver topo: mostra o ultimo elemento da pilha (que está no topo)
"""
import numpy as np

class Pilha:

    def __init__(self, capacidade):
        self.__capacidade  = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade,dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self,valor):
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1


pilha = Pilha(5)
ver = pilha.ver_topo()
print(ver)
pilha.empilhar(3)
pilha.empilhar(2)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.empilhar(6)

ver = pilha.ver_topo()
print(ver)

print("------------")
pilha.desempilhar()
print(pilha.ver_topo())

print("------------")
pilha.desempilhar()
print(pilha.ver_topo())