"""
SHELL SORT:
    Melhora a ordenação por inserção, podendo ser considerada uma "versão" do insertion sort
    Funcionamento:
        - O vetor original é quebrado em subvetores
        - cada subvetor é comparado e trocado os valores
        - ao final de uma rodada, o subvetor é quebrado em mais subvetores
    Vetor com 20 elementos:
        - 1° rodada: 10 elementos
        - 2° rodada: 5 elementos
        - 3° rodada: 2/3 elementos
    A complexidade do algorítimo depende dos intervalos escolhidos (há diversos intervalos que podem ser feitos)
    Pior Caso: O(n²)
    Melhor Caso: O(n* log n) (melhor do que o selection O(n²) e Bubble sort O(n²)


"""
import numpy as np

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


shell_sort(np.array([15,34,8,3,2,1,22,9,17,12,40,72]))
print(shell_sort(np.array([15,34,8,3,2,1,22,9,17,12,40,72])))
