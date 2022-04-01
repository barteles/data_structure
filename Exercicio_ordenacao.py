"""
Crie um vetor com 5000 números float aleatórios de 0 a 1 (random). Meça o desempenho e compare o tempo de execução de cada
algorítimo
"""
import random
import timeit
import numpy as np


def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1
    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i],vetor[j] = vetor[j],vetor[i]
    vetor[i+1], vetor[final] = vetor[final], vetor[i + 1]
    return i + 1

def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)
        #esquerda
        quick_sort(vetor, inicio, posicao -1)
        #direita
        quick_sort(vetor, posicao + 1, final)
    return vetor

def merge_sort(vetor):
    if len(vetor) > 1:
        divisao = len(vetor) // 2
        esquerda = vetor[:divisao].copy()
        direita = vetor[divisao:].copy()

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        #ordena esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        #ordenação final
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1

    return vetor

def shell_sort(vetor):
    intervalo = len(vetor)//2

    while intervalo >0:
        for i in range(intervalo,len(vetor)):
            temp  = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j-intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2
    return vetor

def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0,n - i -1):
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp
    return vetor

def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        id_minimo= i
        for j in range(i + 1, n):
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
        temp  = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp

    return vetor

def insertion_sort(vetor):
    n = len(vetor)

    for i in range(n):
        marcado = vetor[i]

        j = i -1
        while j >=0 and marcado < vetor[j]:
            vetor[j+1] = vetor[j]
            j -= 1
        vetor[j+1] = marcado
    return vetor

## criando o vetor
vetor = []
for i in range(1000):
    vetor.append(round(random.random(),4))

vetor= np.array(vetor)

print(f'Bubble sort: {timeit.timeit(lambda: bubble_sort(vetor.copy()))}')
print('--------')
print(f'Selection sort: {timeit.timeit(lambda: selection_sort(vetor.copy()))}')
print('--------')
print(f'Insertion sort: {timeit.timeit(lambda: insertion_sort(vetor.copy()))}')
print('--------')
print(f'Shell sort: {timeit.timeit(lambda: shell_sort(vetor.copy()))}')
print('--------')
print(f'Merge sort: {timeit.timeit(lambda: merge_sort(vetor.copy()))}')
print('--------')
print(f'Quick sort: {timeit.timeit(lambda: quick_sort(vetor.copy(),0, len(vetor) -1))}')