import numpy as np
import time


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide a lista ao meio
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Chama o merge_sort recursivamente nas duas metades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Mescla as duas metades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    # Compara elementos de left e right e os insere no resultado em ordem
    while left_idx < len(left) and right_idx < len(right):
        # Ordernar por V/P
        if left[left_idx][0] // left[left_idx][1] > right[right_idx][0] // right[right_idx][1]:
        #ordernr normal pelo peso
        # if left[left_idx][1] < right[right_idx][1]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Adiciona os elementos restantes, se houver
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


def mochilafracionaria(vetor, qtd_objetos, capacidade):
    valores, pesos = zip(*vetor)
    valores = list(valores)
    pesos = list(pesos)

    mochila = []
    valor_total = 0

    for i in range(qtd_objetos):
        if pesos[i] <= capacidade:
            # objeto adicionado completamente
            mochila.append((valores[i],pesos[i], 1))
            valor_total += valores[i]
            capacidade -= pesos[i]
        else:
            fracao_obj = capacidade / pesos[i]
            # Objeto Adicionado fracionado
            mochila.append((valores[i],pesos[i],fracao_obj))
            valor_total += fracao_obj * valores[i]
            break
            
    return mochila, valor_total


def construir_mochila(arr, capacidade):
    sorted_arr = merge_sort(arr)
    mochila, valor_total = mochilafracionaria(sorted_arr,len(sorted_arr),capacidade)

    return mochila, valor_total