"""
VETORES ORDENADOS PARA AULA DE ESTRUTURA DE DADOS

a principal diferença estará no insere comparado ao vetor não ordenado
"""

#Vetor ordenado com pesquisa normal
"""
import numpy as np


class VetorOrdenado():

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n) notação BiG-O será linear
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade + 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i ==  self.ultima_posicao:
                return -1

    def excluir(self,valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            print(-1)
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -=1

vetor = VetorOrdenado(10)
vetor.imprime()
print('----------')
vetor.insere(6)
vetor.imprime()

print('----------')
vetor.insere(4)
vetor.imprime()

print('----------')
vetor.insere(10)
vetor.imprime()

print('----------')
vetor.insere(3)
vetor.imprime()


print('----------')
vetor.insere(1)
vetor.insere(11)
vetor.insere(5)
vetor.imprime()

print('Valor está no indice: ',vetor.pesquisar(12))

#excluindo valores
print('-----------')
vetor.excluir(1)
vetor.imprime()

print('-----------')
vetor.excluir(5)
vetor.imprime()

print('-----------')
vetor.excluir(11)
vetor.imprime()

print('-----------')
vetor.excluir(12)

"""

#Vetor ordenado com pesquisa binária
import numpy as np


class VetorOrdenado():

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n) notação BiG-O será linear
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade + 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisa_binaria(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i ==  self.ultima_posicao:
                return -1

    # O(log n)
    def pesquisa_binaria(self,valor):
        limite_inferior  = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = (limite_inferior + limite_superior)//2
            #se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            #se não achou na primeira tentativa
            elif limite_inferior > limite_superior:
                return -1
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual -1

    def excluir(self,valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            print(-1)
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -=1

vetor = VetorOrdenado(10)
vetor.insere(8)
vetor.insere(9)
vetor.insere(5)
vetor.insere(4)
vetor.insere(1)
vetor.insere(7)
vetor.insere(11)
vetor.insere(13)
vetor.insere(2)

vetor.imprime()

print('Valor na posicao: ',vetor.pesquisa_binaria(7))
print('Valor na posicao: ',vetor.pesquisa_binaria(13))
print('Valor na posicao: ',vetor.pesquisa_binaria(1))
print('Valor na posicao: ',vetor.pesquisa_binaria(15))


