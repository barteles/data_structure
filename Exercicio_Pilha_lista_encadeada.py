"""
Criar uma pilha com lista encadeada simples, com os métodos:
  - empilhar, desempilhar, pilha_vazia, ver_topo
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

    def lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self,valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            print('A lista está vazia')
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

class PilhaListaEncadeada:

    def __init__(self):
        self.lista = ListaEncadeada()

    def __pilha_vazia(self):
        return self.lista.lista_vazia()

    def empilhar(self,valor):
        self.lista.insere_inicio(valor)

    def desempilhar(self):
        return self.lista.excluir_inicio()

    def ver_topo(self):
        if self.lista.primeiro == None:
            return -1
        return self.lista.primeiro.valor

pilha = PilhaListaEncadeada()
pilha.empilhar(20)
pilha.empilhar(40)
print(pilha.ver_topo())

pilha.empilhar(60)
pilha.empilhar(80)
print(pilha.ver_topo())

pilha.desempilhar()
print(pilha.ver_topo())
pilha.desempilhar()
print(pilha.ver_topo())
pilha.desempilhar()
print(pilha.ver_topo())
pilha.desempilhar()
print(pilha.ver_topo())