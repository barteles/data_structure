"""
LISTAS ENCADEADAS:
 - Cada item de dados é incorporado em um nó
 - Cada nó possui uma referência para o próximo nó da lista
 - Um campo da própria lista contém referência para o primeiro nó
 Nas listas, a única maneira de encontrar um elemento é seguir a sequÊncia de elementos, diferentes dos vetores que possuem
 indices
 Cada elemento da lista é armazenado em um objeto.
 Cada elemento da lista referencia o próximo e só é alocado dinamicamente quando é necessário.

OPERAÇÕES:
 - Insere inicio
 - Exclui inicio
 - Mostrar lista
 - Pesquisar
 - Excluir da posição

"""
import numpy as np


class No:

    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)



class ListaEncadeada:

    def __init__(self):
        self.primeiro = None

    def insere_inicio(self,valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def pesquisar(self,valor):
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
        return atual

    def excluir_inicio(self):
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_posicao(self, valor):
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual =  atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual



#testando insere_inicio
"""lista = ListaEncadeada()
lista.insere_inicio(1)
lista.mostrar()
print(lista.primeiro)

lista.insere_inicio(2)
lista.mostrar()
print(lista.primeiro.proximo)"""

#testando excluir
"""lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()

print('-----------')
lista.excluir_inicio()
lista.mostrar()
print('-----------')
lista.excluir_inicio()
lista.mostrar()
print('-----------')
lista.excluir_inicio()
lista.mostrar()
print('-----------')
lista.excluir_inicio()
lista.mostrar()
print('-----------')
lista.excluir_inicio()
lista.mostrar()"""

#testando o pesquisar
""""
lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()

pesquisa = lista.pesquisar(5)
print(pesquisa)

if pesquisa != None:
    print('Encontrado', pesquisa.valor)
else:
    print('Não encontrado')"""

#testando excluir_posicao

lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()

print('-----------')    #testando no meio
lista.excluir_posicao(3)
lista.mostrar()

print('-----------')    #testando no final
lista.excluir_posicao(1)
lista.mostrar()

print('-----------')    #testando no inicio da fila
lista.excluir_posicao(5)
lista.mostrar()