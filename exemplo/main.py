import numpy as np
import time
import tracemalloc
from salvar import salvarInformacoes


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



def medicoes(arr, capacidade):
    # inicia o tracemaloc para verificar a memoria
    tracemalloc.start()
    #inicia o tempo
    inicio = time.time()

    sorted_arr = merge_sort(arr)
    mochila, valor_total = mochilafracionaria(sorted_arr,len(sorted_arr),capacidade)
    
    #fim da execução
    fim = time.time()
    tempo_execucao = fim - inicio
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    current = current # Atual
    peak = peak # Pico

    return tempo_execucao, current, peak, mochila, valor_total



def main():
    # forma de divisão de valores e peso retirado do site https://128mots.com/2021/03/29/problema-da-mochila-algoritmo-em-python-problema-da-mochila/

    # Exemplo A do site https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/mochila-frac.html
    # (valor, peso)
    # arr = [(100,10), (300,20), (600,30), (400,20),(840,40)]

    # arr = gerar_instancias()
    arquivo = open("instancia.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    # Converter a string em uma lista de tuplas usando a função eval
    arr = eval(conteudo)    

    continua = True
    
    resultados = {}
    inicio_geral = time.time()
    contador = 0

    while(continua):	
        tempo_execucao, uso_memoria_atual, uso_memoria_pico, mochila, valor_total = medicoes(arr, 100)
        fim_geral = time.time()
        resultados[contador] = {}

        resultados[contador]['Tempo de Execucao'] = tempo_execucao
        resultados[contador]['Memoria Atual'] = uso_memoria_atual
        resultados[contador]['Memoria Pico'] = uso_memoria_pico
        resultados[contador]['Mochila'] = mochila
        resultados[contador]['Valor Total'] = valor_total

        contador += 1


        tempo_geral = fim_geral - inicio_geral

        if(tempo_geral > 0.5):
            continua = False

    salvarInformacoes(resultados)


    



main()