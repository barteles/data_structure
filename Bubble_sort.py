"""
ALGORÍTIMO DE ORDENAÇÃO BUBBLE SORT
 - Notavelmente mais lento e é o mais simples dos algorítimos de ordenação
 - Funcionamento:
    - Comparação de dois números
    - Se o da esquerda for maior, os elementos devem ser trocados
    - desloca-se uma posição à direita
 - A medida que o algorítmo avança, os itens maiores "surgem como uma bolha", na extremidade superior do vetor
 - Um algorítimo com 10 elementos faz 9 comparações na primeira passagem, 8 na segunda, 7 na terceira, etc
 (n-1, n-2, n-3, ...).
     - Para 10 itens: 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45 passos
 - BIG- O: é quadratico O(n²)
 - O algoritimo faz cerca de N²/2 comparações
 - Há menos trocas do que há comparações, pois os elementos são trocados somente se precisarem
 - Se os dados forem aleatórios, uma troca será necessária mais ou menos N²/4 (no pior caso, com os dados no modo inverso,
 uma troca será necessária a cada comparação)

"""
import numpy as np

def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0,n - i -1):
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp
    return vetor

print(bubble_sort(np.array([15,34,8,3])))

# teste para o pior caso, ordem inversa
print(bubble_sort(np.array([10,9,8,7,6,5,4,3,2,1])))