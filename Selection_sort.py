"""
SELECTION SORT:
    - Melhora a ordenação pelo método da bolha reduzindo o número de trocas necessárias de N² para N
    - O número de comparações continua N²/2
    - Funcionamento:
        - Percorre todos os elementos e seleciona o menor
        - O menor elemento é trocado com o elemento da extremidade esquerda do vetor (posições iniciais)
        - Os elementos ordenados acumulam-se pela esquerda
    - Um algorítimo com 10 elementos faz 9 comparações na primeira passagem, 8 na segunda, 7 na terceira, etc
 (n-1, n-2, n-3, ...).
     - Para 10 itens: 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45 passos
    - BIG- O: é quadratico O(n²)
    - O algoritimo faz cerca de N²/2 comparações (mesmo numero de comparação que o bubble)
    - Com 10 elementos, são requeridas menos de 10 trocas (geralmente é feita uma troca por cada passagem)
    - com 100 elementos, são necessárias 4950 comparações e menos de 100 trocas
"""

import numpy as np

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

print(selection_sort(np.array([15,34,8,3])))

# teste para o pior caso, ordem inversa
print(selection_sort(np.array([10,9,8,7,6,5,4,3,2,1])))