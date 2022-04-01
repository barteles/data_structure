"""
MERGE SORT:
    Segue a ideia de 'dividi e conquistar'.
    Um dos algoritimos de ordenação mais popular
    Funcionamento:
        - Divisão do problema em subproblemas
        - Divide o vetor continuamente pela metade, ordena e combina (merge)
    Pior caso: O(n* log n)
    Melhor caso: O(n* log n)

    Melhor do que Bubble sort O(n²), selection sort O(n²), e shell sort O(n²) no pior caso e O(n* log n) em média.
"""
import numpy as np

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

print(merge_sort(np.array([15,34,8,3])))

print(merge_sort(np.array([10,9,8,7,6,5,4,3,2,1])))

print(merge_sort(np.array([38,27,43,3,9,82,10])))