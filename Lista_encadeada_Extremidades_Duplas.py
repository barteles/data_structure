"""
LISTAS ENCADEADAS COM EXTREMIDADES DUPLAS
    Permite inserir valores no ultimo nó;
    Para inserir um nó no final de uma lista com extremidade simples, é necessário percorrer todos os elementos.
    A referencia paraa o ultimo nó permite inserir um novo nó diretamente no final da lista, assim como no inicio.

OPERAÇÕES
 - Inserir no inicio
 - Inserir no Final(adicional)
 - Excluir no inicio


"""
class No:

    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeadaExtremidadeDupla:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self,valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self,valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('lista vazia')
            return

        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp


    def mostrar(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

# teste insere inicio
"""
lista  = ListaEncadeadaExtremidadeDupla()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
print(lista.primeiro,lista.ultimo)"""

#teste insere final
"""
lista  = ListaEncadeadaExtremidadeDupla()
lista.insere_final(1)
lista.insere_final(2)
lista.insere_final(3)
lista.insere_inicio(0)
lista.insere_final(4)
lista.mostrar()
print(lista.primeiro,lista.ultimo)"""

#testando exclui inicio

lista  = ListaEncadeadaExtremidadeDupla()
lista.insere_final(1)
lista.insere_final(2)

lista.mostrar()
print(lista.primeiro,lista.ultimo)

print('-------')
lista.excluir_inicio()
lista.mostrar()
print('-------')
lista.excluir_inicio()
lista.mostrar()