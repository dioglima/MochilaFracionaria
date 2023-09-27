import numpy as np
import time
import random


def pivot(vetor):
    return random.randint(0, len(vetor))


def swap(vetor, i, j):
    temp = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = temp
    return vetor


def partition(vetor, left, right):
    swap(vetor, pivot(vetor), right)

    storeIndex = left

    for i in range(vetor):
        if vetor[i] < pivot(vetor):
            swap(vetor, i, storeIndex)
            storeIndex = storeIndex + 1

    swap(vetor, storeIndex, right)

    return storeIndex


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
    sorted_arr = partition(arr)
    mochila, valor_total = mochilafracionaria(sorted_arr, len(sorted_arr), capacidade)

    return mochila, valor_total
