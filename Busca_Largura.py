"""
BUSCA EM LARGURA;
    Regras:
     1 - Visite um nó adjacente não visitado, marque-o e coloque na fila
     2 - se não puder seguir a regra 1, remova um nó da fila e torne-o o nó atual
     3 - Se não puder executar a regra 2 porque a fila está vazia, terminou!


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

grafo = Grafo()
grafo.arad.mostra_adjacente()


#testando a fila

fila = FilaCircular(20)
fila.enfileirar(grafo.arad)
fila.enfileirar(grafo.bucharest)
fila.enfileirar(grafo.fagaras)

print(fila.primeiro().rotulo)



#testando Busca Largura

busca_largura = BuscaLargura(grafo.arad)
busca_largura.buscar()