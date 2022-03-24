"""
LISTAS DUPLAMENTE ENCADEADAS:
    Permitem percorrer a lista tanto da direita para a esquerda, quanto da esquerda para a direita.
    Cada um dos nós tem duas referências para outros nós, ao invés de uma só
    A primeira referência é para o próximo nó e a segunda é para o nó inferior


"""
class No:

    def __init__(self,valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)

class ListaDuplamenteEncadeada:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self,valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self,valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def exclui_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def exclui_final(self):
        temp = self.ultimo
        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior

    def exclui_posicao(self,valor):
        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
            if atual == None:
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_frente(self):
        atual =  self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        atual =  self.ultimo
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior


# teste inicial
"""
lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar_frente()
print(lista.primeiro,lista.ultimo)

print('------')
lista.mostrar_tras()
"""
# teste insere final
"""
lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_final(3)
lista.insere_final(4)

lista.mostrar_frente()
print(lista.primeiro,lista.ultimo)

print('------')
lista.mostrar_tras()
"""

# teste exclui inicio e final
"""
lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar_frente()

print('--------')
lista.exclui_inicio()
lista.mostrar_frente()

print('--------')
lista.exclui_final()
lista.mostrar_frente()
lista.mostrar_tras()
"""

# teste exclui posicao

lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar_frente()

print('------')
exclui = lista.exclui_posicao(3)
print(exclui)
lista.mostrar_frente()
print('-------')
lista.mostrar_tras()

print('------')
exclui = lista.exclui_posicao(1)
exclui = lista.exclui_posicao(5)

lista.mostrar_frente()
print('-------')
lista.mostrar_tras()