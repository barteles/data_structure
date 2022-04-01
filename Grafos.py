"""
GRAFOS:


BUSCA EM PROFUNDIDADE:
    REGRAS:
     1 -Visite um nó adjacente não visitado, marque-o e coloque-o na pilha
     2 - se não puder seguir a regra 1, retire um nó da pilha (desempilhe)
     3 - se não puder seguir a regra 1 ou 2, terminou

BUSCA EM LARGURA;
    Regras:
     1 - Visite um nó adjacente não visitado, marque-o e coloque na fila
     2 - se não puder seguir a regra 1, remova um nó da fila e torne-o o nó atual
     3 - Se não puder executar a regra 2 porque a fila está vazia, terminou!

BUSCA GULOSA:
    utiliza eurística para resolver seu algorítimo, neste caso aqui será a distância em linha reta até a capital Bucharest

BUSCA AESTRELA (A*)
    Será mais preciso e melhor do que a busca gulosa, pois além de utilizar a eurística, utilizará também os custos (km)
    entre as cidades, trazendo o menor caminho a ser percorrido.

ALGORÍTIMO DE DIJKSTRA:
    Encontra o caminho mais curto a partir de um nó especificado até todos os outros.
    Descobrir a maneira mais barata de viajar de A até todas as outras cidades.
        - Os nós representam algum objeto do mundo real
        - Uma aresta faz a ligação entre os nós
        - A representação pode ser por:
            1 - matriz de adjacencia
            2 - lista de adjjacencias
"""

"""
Criando um grafo que mostra a menor distância (melhor rota) entre a cidade de Arad até Bucharest 
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


class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        #mudança no tipo de array
        self.valores = np.empty(self.capacidade, dtype=object)

    def __fila_vazia(self):
        return self.numero_elementos == 0   #outra maneira de se criar um if[...] return True

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self,valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        """
        Caso ele chegue no final da fila, irá retornar ao inicio (indice 0), ou seja, se ele atingiu o máximo da direita,
        o cursor voltará à extrema esquerda
        """
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]


class BuscaLargura:

    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.fila = FilaCircular(20)
        self.fila.enfileirar(inicio)

    def buscar(self):
        primeiro = self.fila.primeiro()
        print('-------')
        print(f'Primeiro da fila: {primeiro.rotulo}')
        temp = self.fila.desenfileirar()
        print(f'Desenfileirou {temp.rotulo}')
        for adjacente in primeiro.adjacentes:
            print(f'O primeiro elemento era {temp.rotulo}. {adjacente.vertice.rotulo} já foi visitado? {adjacente.vertice.visitado}')
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.fila.enfileirar(adjacente.vertice)
                print(f'Enfileirou {adjacente.vertice.rotulo}')
        if self.fila.numero_elementos > 0:
            self.buscar()


class VetorOrdenado():

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        #mudança no tipo de dado
        self.valores = np.empty(self.capacidade, dtype=object)


    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)

    #Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, vertice):
        if self.ultima_posicao == self.capacidade + 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1

        self.valores[posicao] = vertice
        self.ultima_posicao += 1

class BuscaGulosa:

    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('----------')
        print(f'Atual: {atual.rotulo}')
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))   #cria o vetor com o número de adjacentes do ponto atual
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente.vertice)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != 0:
                self.buscar(vetor_ordenado.valores[0])


class VetorOrdenadoAdjacentes():

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        #mudança no tipo de dado
        self.valores = np.empty(self.capacidade, dtype=object)


    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ' - ', self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)

    #Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade + 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1

        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

class Aestrela:

    def __init__(self,objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('----------')
        print(f'Atual: {atual.rotulo}')
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenadoAdjacentes(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)

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
#grafo.arad.mostra_adjacente()

#Verificação se deu certo o empilhamento
"""
pilha = Pilha(5)
pilha.empilhar(grafo.arad)
pilha.empilhar(grafo.sibiu)
pilha.empilhar(grafo.timisoara)

print(pilha.ver_topo().rotulo)
pilha.desempilhar()
print(pilha.ver_topo().rotulo)
pilha.desempilhar()
print(pilha.ver_topo().rotulo)
"""

# Busca em Profundidade
"""
busca_profundidade = BuscaProfundidade(grafo.arad)
busca_profundidade.buscar()
"""


#testando a fila
"""
fila = FilaCircular(20)
fila.enfileirar(grafo.arad)
fila.enfileirar(grafo.bucharest)
fila.enfileirar(grafo.fagaras)

print(fila.primeiro().rotulo)
"""


#testando Busca Largura
"""
busca_largura = BuscaLargura(grafo.arad)
busca_largura.buscar()
"""

#testando o vetor ordenado
"""
vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.dobreta)
vetor.insere(grafo.bucharest)
vetor.imprime()
vetor.insere(grafo.lugoj)
vetor.imprime()
"""

#testando a Busca Gulosa
"""
busca_gulosa = BuscaGulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad)
"""

#testando o vetor ordenado da busca Aestrela
"""
print(grafo.arad.adjacentes)
print(grafo.arad.adjacentes[0].vertice.rotulo, grafo.arad.adjacentes[0].vertice.distancia_objetivo)
print(grafo.arad.adjacentes[0].distancia_aestrela, grafo.arad.adjacentes[0].custo)

vetor = VetorOrdenadoAdjacentes(3)
vetor.insere(grafo.arad.adjacentes[0])
vetor.insere(grafo.arad.adjacentes[1])
vetor.insere(grafo.arad.adjacentes[2])
vetor.imprime()
"""

#testando busca Aestrela
"""
busca_aestrela = Aestrela(grafo.bucharest)
busca_aestrela.buscar(grafo.arad)
"""

#testando algorítimo de Dijksta

dijkstra = Dijkstra(cidades, arestas, vertices['arad'])
dijkstra.dijkstra()