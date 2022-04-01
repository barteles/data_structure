"""
ALGORÍTIMO DE DIJKSTRA:
    Encontra o caminho mais curto a partir de um nó especificado até todos os outros.
    Descobrir a maneira mais barata de viajar de A até todas as outras cidades.
        - Os nós representam algum objeto do mundo real
        - Uma aresta faz a ligação entre os nós
        - A representação pode ser por:
            1 - matriz de adjacencia
            2 - lista de adjjacencias

"""
import numpy as np
import sys

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

#------------
# Criando vértice para executar o algorítimo de dijkstra
vertices = {'arad': 0, 'zerind': 1, 'oradea': 2,'sibiu':3,'timisoara': 4,'lugoj': 5, 'mehadia':6, 'dobreta': 7,
            'craiova': 8, 'rimnicu': 9, 'fagaras': 10, 'pitesti': 11, 'bucharest': 12, 'giurgiu': 13}
cidades = {0:'arad', 1: 'zerind', 2: 'ordea', 3: 'sibiu', 4 :'timisoara', 5 :'lugoj', 6 :'mehadia',
           7:'dobreta', 8 :'craiova', 9 :'rimnicu', 10: 'fagaras', 11: 'pitesti', 12: 'bucharest', 13: 'giurgiu'}

arestas = np.zeros([len(cidades),len(cidades)],dtype=int)

#matriz de adjacencia
arestas[vertices['arad'], [vertices['zerind']]] = 75
arestas[vertices['arad'], [vertices['sibiu']]] = 140
arestas[vertices['arad'], [vertices['timisoara']]] = 118

arestas[vertices['zerind'], [vertices['arad']]] = 75
arestas[vertices['zerind'], [vertices['oradea']]] = 71

arestas[vertices['oradea'], [vertices['zerind']]] = 71
arestas[vertices['oradea'], [vertices['sibiu']]] = 151

arestas[vertices['sibiu'], [vertices['arad']]] = 140
arestas[vertices['sibiu'], [vertices['oradea']]] = 151
arestas[vertices['sibiu'], [vertices['fagaras']]] = 90
arestas[vertices['sibiu'], [vertices['rimnicu']]] = 80

arestas[vertices['rimnicu'], [vertices['sibiu']]] = 80
arestas[vertices['rimnicu'], [vertices['pitesti']]] = 97
arestas[vertices['rimnicu'], [vertices['craiova']]] = 146

arestas[vertices['craiova'], [vertices['rimnicu']]] = 146
arestas[vertices['craiova'], [vertices['pitesti']]] = 138
arestas[vertices['craiova'], [vertices['dobreta']]] = 120

arestas[vertices['dobreta'], [vertices['craiova']]] = 120
arestas[vertices['dobreta'], [vertices['mehadia']]] = 75

arestas[vertices['mehadia'], [vertices['dobreta']]] = 75
arestas[vertices['mehadia'], [vertices['lugoj']]] = 70

arestas[vertices['lugoj'], [vertices['mehadia']]] = 70
arestas[vertices['lugoj'], [vertices['timisoara']]] = 111

arestas[vertices['timisoara'], [vertices['lugoj']]] = 111
arestas[vertices['timisoara'], [vertices['arad']]] = 118

arestas[vertices['pitesti'], [vertices['craiova']]] = 138
arestas[vertices['pitesti'], [vertices['rimnicu']]] = 97
arestas[vertices['pitesti'], [vertices['bucharest']]] = 101

arestas[vertices['bucharest'], [vertices['pitesti']]] = 101
arestas[vertices['bucharest'], [vertices['giurgiu']]] = 90
arestas[vertices['bucharest'], [vertices['fagaras']]] = 211

arestas[vertices['giurgiu'], [vertices['bucharest']]] = 90

arestas[vertices['fagaras'], [vertices['bucharest']]] = 211
arestas[vertices['fagaras'], [vertices['sibiu']]] = 99

class Dijkstra:

    def __init__(self,vertices, arestas, inicio):
        self.tamanho = len(vertices)
        self.vertices = vertices
        self.grafo =arestas
        self.inicio = inicio

    def mostra_solucao(self, distancias):
        print(f'Menores distânias de {self.vertices[self.inicio]} até todos os outros')
        for vertice in range(self.tamanho):
            print(self.vertices[vertice], distancias[vertice])

    def distancia_minima(self, distancia, visitados):
        minimo = sys.maxsize
        for vertice in range(self.tamanho):
            if distancia[vertice] < minimo and visitados[vertice] == False:
                minimo = distancia[vertice]
                indice_minimo = vertice
        return indice_minimo

    def dijkstra(self):
        distancia = [sys.maxsize] * self.tamanho
        distancia[self.inicio] = 0
        visitados = [False] * self.tamanho

        for _ in range(self.tamanho):
            indice_minimo = self.distancia_minima(distancia, visitados)
            visitados[indice_minimo] = True
            for vertice in range(self.tamanho):
                if self.grafo[indice_minimo][vertice] > 0 and visitados[vertice] == False \
                      and distancia[vertice] > distancia[indice_minimo] + self.grafo[indice_minimo][vertice]:
                    distancia[vertice] = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]

        self.mostra_solucao(distancia)



grafo = Grafo()
grafo.arad.mostra_adjacente()

#testando algorítimo de Dijksta
dijkstra = Dijkstra(cidades, arestas, vertices['arad'])
dijkstra.dijkstra()