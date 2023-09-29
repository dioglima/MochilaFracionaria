import numpy as np
import time
import random


def pivot(vetor,size_arr):
    #[1] considera o peso 
    termo_1 = 1 / size_arr
    soma_v_p = 0
    for valor, peso in vetor:
        soma_v_p += (valor / peso)

    #pivot
    p = int(round(termo_1 * soma_v_p))

    return p


def swap(vetor, i, j):
    temp = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = temp
    return vetor


def partition(vetor, left, right, size_arr):
    p = pivot(vetor, size_arr)
    swap(vetor, p, right)

    storeIndex = left

    for i in range(size_arr):
        # [1] chave na tupla das instancias referente ao peso
        if vetor[i][1] < p:
            swap(vetor, i, storeIndex)
            storeIndex = storeIndex + 1

    swap(vetor, storeIndex-1, right)

    return vetor


def mochilafracionaria(vetor, qtd_objetos, capacidade):
    valores, pesos = zip(*vetor)
    valores = list(valores)
    pesos = list(pesos)

    mochila = []
    valor_total = 0

    for i in range(qtd_objetos):
        if pesos[i] <= capacidade:
            # objeto adicionado completamente
            mochila.append((valores[i], pesos[i], 1))
            valor_total += valores[i]
            capacidade -= pesos[i]
        else:
            fracao_obj = capacidade / pesos[i]
            # Objeto Adicionado fracionado
            mochila.append((valores[i], pesos[i], fracao_obj))
            valor_total += fracao_obj * valores[i]
            break

    return mochila, valor_total


def construir_mochila(arr, capacidade):
    size_arr = len(arr)
    # ordena o vetor
    sorted_arr = partition(vetor=arr,left=0, right=size_arr-1, size_arr=size_arr)
    #cria a mochila
    mochila, valor_total = mochilafracionaria(sorted_arr, size_arr, capacidade)

    return mochila, valor_total
