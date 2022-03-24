"""
INSERTION SORT:
    - Cerca de 2x mais rápido que a ordenação pelo método da bolha e um pouco mais rápido que a ordenação
    por seleção em situações normais.
    - Funcionamento:
        - Há um marcador em algum lugar no meio do vetor.
        - Os elementos da esquerda do marcador são parcialmente ordenados (estão ordenados entre eles, porém não estão
        em suas posições finais)
        - Os elementos à direita do marcador não estão ordenados
    - Na primeira passagem é comparado no máximo um item. Na segunda são comparados no máximo dois, na terceira três, etc.
        - 1 + 2 + 3 + ... + N-1 = N*(N-1)/2
    - Como em cada passagem uma média de apenas metade do número máximo de itens é de fato comparada antes do ponto de
    inserção ser encontrado, então:
        - N*(N-1)/4
    - O número de cópias é aproximadamente o mesmo que o número de comparações
    - Para dados aleatórios esse algorítimo executad duas vezes mais rápido que o método da bolha e mais rápido que o método
    da seleção.
    - Para dados que já estejam quase ordenados o algorítimo é ainda mais eficiente

"""
import numpy as np

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

print(insertion_sort(np.array([15,34,8,3])))

# teste para o pior caso, ordem inversa
print(insertion_sort(np.array([10,9,8,7,6,5,4,3,2,1])))