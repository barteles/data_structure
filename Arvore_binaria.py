"""
ÁRVORE BINÁRIA DE BUSCA:
    Uma árvore combina as vantagens de um vetor ordenado e a de uma lista encadeada
        - Busca Rápida (igual a um vetor ordenado)
        - Inserção/Eliminação Rápida (igual uma lista encadeada)
    Uma árvore consiste em nós(circulos) conectados por arestas(linhas).
        - Máximo de dois filhos.
        - Filho à esquerda e filho à direita
        - Pode ter 1 ou nenhum filho.

 - CAMINHO: caminho que liga um nó ao outro.
 - RAIZ: é o nó na parte superior. Há apenas uma raiz em uma árvore e deve haver somente um caminho da raiz até
 qualquer nó
 - PAI: qualquer nó (exceto a raiz) tem exatamente uma aressta que sobe para outro nó. O nó acima dele é chamado
 de PAI DO NÓ.
 - FILHO: qualquer nó pode ter uma ou mais linhas descendo para outros nós. Esses nós abaixo de um dado nó são
 chamados de seus filhos
 - FOLHA: Um nó que não tem filhos
 - SUBÁRVORE: qualquer nó pode ser considerado como sendo raiz de uma subárvore,que consiste em seus filhos.
 - VISITANDO: um nó é visitado quando o controle do programa chega ao nó, em geral para a finalidade de executar
 uma operação de nó.
 - PERCORRENDO: visitar todos os nós em agluma ordem especificada.
 - CHAVES: valor usado para buscar um item


TRAVESSIA EM PRÉ-ORDEM:
    Primeiro visita a raiz e depois recursivamente faz uma travessia na subárvore esquerda, seguindo de uma travessia
    na subárvore direita.
     - Raiz, esquerda, direita

TRAVESSIA EM ORDEM:
    Recursivamente faz a travessia na subárvore esquerda, visita a raiz e faz uma travessia recursiva na subárvore direita
     - esquerda, raiz, direita

TRAVESSIA PÓS-ORDEM:
    Recursivamente faz a travessia na subárvore esquerda, faz uma visita recursiva na subárvore direita e por fim visita
    a raiz
     - esquerda, direia, raiz
"""

class No:

    def __init__(self,valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)

class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def inserir(self,valor):
        novo = No(valor)
        # se a árvore está vazia
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                # esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                # direita
                else:
                    atual = atual.direita
                    if atual  == None:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return

    def pesquisar(self,valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                print('Elemento não localizado na árvore')
                return
        return atual

    #raiz, esquerda, direita
    def pre_ordem(self,no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    #esquerda, raiz, direita
    def em_ordem(self,no):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    #esquerda, direita, raiz
    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def excluir(self, valor):
        if self.raiz == None:
            print('A árvore está vazia')
            return

        #encontrar o nó
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True
        while atual.valor != valor:
            pai = atual
            #esquerda
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            #direita
            else:
                e_esquerda = False
                atual = atual.direita
            if atual == None:
                return False

        #o nó a ser apagado é uma folha:
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda == True:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
                pai.esquerda = None
            else:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
                pai.direita = None

        #o nó a ser apagado não possui filho na direita
        elif atual.direita == None:
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.esquerda.valor))


            if atual == self.raiz:
                self.raiz = atual.esquerda
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(atual.esquerda.valor))

            elif e_esquerda == True:
                pai.esquerda = atual.esquerda
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.esquerda.valor))

            else:
                pai.direita = atual.esquerda
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.esquerda.valor))

        #o nó a ser apagado não possui filho na esquerda
        elif atual.esquerda == None:
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.direita.valor))

            if atual ==  self.raiz:
                self.raiz = atual.direita
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(atual.direita.valor))

            elif e_esquerda == True:
                pai.esquerda = atual.direita
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.direita.valor))

            else:
                pai.direita = atual.direita
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.direita.valor))

        #o nó possui dois filhos:
        sucessor = self.get_sucessor(atual)

        if atual ==self.raiz:
            self.raiz = sucessor


        elif e_esquerda == True:
            pai.esquerda = sucessor
        else:

            pai.direita = sucessor

        sucessor.esquerda =atual.esquerda
        return True

    def get_sucessor(self,no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita
        while atual != None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        return sucessor


arvore  = ArvoreBinariaBusca()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

print(arvore.raiz.esquerda.valor)
print(arvore.raiz.direita.valor)

#pesquisando valores
print(arvore.pesquisar(39))
print(arvore.pesquisar(84))
print(arvore.pesquisar(100))

#travessia em pre_ordem
# Raiz, esquerda, direita
print(arvore.pre_ordem(arvore.raiz))

#travessia em ordem
# Esquerda, raiz, direita
print('------')
print(arvore.em_ordem(arvore.raiz))

#Travessia pós-ordem
# esquerda, direita, raiz
print('-----')
print(arvore.pos_ordem(arvore.raiz))


#----------------
# excluir folha
"""arvore.excluir(9)
print('------')
print(arvore.ligacoes)

#----------------
# excluir nó pai 84
arvore.excluir(84)
print('------')
print(arvore.ligacoes)

arvore.excluir(14)          #esse também é aceito, pois o 9 foi apagado, deixando o 14 sómente com 1 filho à direita
print('------')
print(arvore.ligacoes)"""

# o nó a ser apagado deve ser substituido por seu sucessor
print('--------')
print(arvore.get_sucessor(arvore.raiz).valor)

arvore.excluir(72)
print('------')
print(arvore.em_ordem(arvore.raiz))
