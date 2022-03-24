"""
DEQUE (DOUBLE END QUEUE)
    Suportam operações do tipo pilha ou fila.

Operações:
 - Adicionar no inicio
 - Remover no inicio
 - Adicionar no final
 - Remover no final

A implementação pode ser do tipo ESTÁTICA ou do tipo CIRCULAR.
 - Na estática, ela irá se comportar como um vetor ordenado, portanto, tanto na remoção, quanto adicionando novos itens
 de dados o algorítimo terá de fazer um realocamento dos itens restantes no vetor, levando assim O(n) para adicionar e
 O(n) para remover.

"""
import numpy as np

class Deque:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade -1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return
        #se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final =0
        elif self.inicio == 0:
            self.inicio = self.capacidade -1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor

    def insere_final(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return

        #se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        elif self.final == self.capacidade -1:
            self.final = 0
        else:
            self.final += 1
        self.valores[self.final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('O deque está vazio')
            return
    #possui somente um elemento
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        else:
            #volta para a posiçao inicial
            if self.inicio == self.capacidade -1:
                self.inicio = 0
            else:
                #incrementar o inicio para remover o inicial(atual)
                self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print('O deque está vazio')
            return

        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        elif self.inicio == 0:
            self.final = self.capacidade -1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio():
            print('O deque está vazio')
            return

        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0:
            print('O deque está vazio')
            return

        return self.valores[self.final]

deque = Deque(5)

deque.insere_final(5)
print(deque.get_inicio(),deque.get_final())

deque.insere_final(10)
print(deque.get_inicio(),deque.get_final())

deque.insere_inicio(3)
print(deque.get_inicio(),deque.get_final())

# 2 3 5 10 11
deque.insere_inicio(2)
deque.insere_final(11)
print(deque.get_inicio(),deque.get_final())

print('-----------')
#retirando valores de inicio e fim
deque.excluir_final()
deque.excluir_inicio()

print(deque.get_inicio(),deque.get_final())
print(deque.valores)

print('--------')
print(deque.inicio)
print(deque.final)