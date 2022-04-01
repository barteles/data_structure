"""
BUSCA AESTRELA (A*)
    Será mais preciso e melhor do que a busca gulosa, pois além de utilizar a eurística, utilizará também os custos (km)
    entre as cidades, trazendo o menor caminho a ser percorrido.


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


grafo = Grafo()
grafo.arad.mostra_adjacente()

#testando o vetor ordenado da busca Aestrela
print(grafo.arad.adjacentes)
print(grafo.arad.adjacentes[0].vertice.rotulo, grafo.arad.adjacentes[0].vertice.distancia_objetivo)
print(grafo.arad.adjacentes[0].distancia_aestrela, grafo.arad.adjacentes[0].custo)

vetor = VetorOrdenadoAdjacentes(3)
vetor.insere(grafo.arad.adjacentes[0])
vetor.insere(grafo.arad.adjacentes[1])
vetor.insere(grafo.arad.adjacentes[2])
vetor.imprime()


#testando busca Aestrela
print('-------------------------------------------')
busca_aestrela = Aestrela(grafo.bucharest)
busca_aestrela.buscar(grafo.arad)

