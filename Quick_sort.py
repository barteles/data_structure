"""
QUICK SORT:
    Rápido e eficiente, criado em 1960 para traduzir um dicionário de inglês para russo.
    Funcionamento:
        - O vetor é dividido em subvetores que são chamados recursivamente para ordernar os elementos
        - Estratégia de divisão  e conquista

"""
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

Vetor = np.array([38,27,43,3,9,82,10])
print(Vetor)
print(quick_sort(Vetor, 0, len(Vetor) -1))