"""

BUSCA EM PROFUNDIDADE:
    REGRAS:
     1 -Visite um nó adjacente não visitado, marque-o e coloque-o na pilha
     2 - se não puder seguir a regra 1, retire um nó da pilha (desempilhe)
     3 - se não puder seguir a regra 1 ou 2, terminou


"""
import numpy as np

class Vertice:

    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacente(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

class Adjacente:

    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo


class Grafo:


    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara',329)
    lugoj  = Vertice('Lugoj',244)
    mehadia = Vertice('Mehadia',241)
    dobreta = Vertice('Dobreta',242)
    craiova = Vertice('Craiova',160)
    rimnicu = Vertice('Rimnicu',193)
    fagaras = Vertice('Fagaras',178)
    pitesti = Vertice('Pitesti',98)
    bucharest = Vertice('Bucharest',0)
    giurgiu = Vertice('Giurgiu',77)

    #adicionando as adjacencias das cidades:
    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))
    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))

    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(dobreta, 120))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(dobreta, 120))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))
    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras,211))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))

    giurgiu.adiciona_adjacente(Adjacente(bucharest,90))


class Pilha:

    def __init__(self, capacidade):
        self.__capacidade  = capacidade
        self.__topo = -1
        #mudança do tipo de array
        self.__valores = np.empty(self.__capacidade,dtype=object)

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
            return None
        else:
            temp = self.__valores[self.__topo]
            self.__topo -= 1
            return temp

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1


class BuscaProfundidade:

    def __init__(self,inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(inicio)

    def buscar(self):
        topo = self.pilha.ver_topo()
        print(f'Topo: {topo.rotulo}')
        for adjacente in topo.adjacentes:
            print(f'Topo é {topo.rotulo}. {adjacente.vertice.rotulo} ja foi visitado? {adjacente.vertice.visitado}')
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.pilha.empilhar(adjacente.vertice)
                print(f'Empilhou {adjacente.vertice.rotulo}')
                self.buscar()
        print(f'Desempilhou {self.pilha.desempilhar().rotulo}')
        print('\n')

grafo = Grafo()
grafo.arad.mostra_adjacente()

#Verificação se deu certo o empilhamento

pilha = Pilha(5)
pilha.empilhar(grafo.arad)
pilha.empilhar(grafo.sibiu)
pilha.empilhar(grafo.timisoara)

print(pilha.ver_topo().rotulo)
pilha.desempilhar()
print(pilha.ver_topo().rotulo)
pilha.desempilhar()
print(pilha.ver_topo().rotulo)


# Busca em Profundidade

busca_profundidade = BuscaProfundidade(grafo.arad)
busca_profundidade.buscar()

