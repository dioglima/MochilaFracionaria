import csv
import os

def salvarInformacoes(dados, saida='output', nomeArquivo='dados.csv'):
    if not os.path.exists(saida):
        os.makedirs(saida)

    caminhoArquivo = os.path.join(saida, nomeArquivo)

    with open(caminhoArquivo, 'w', newline='') as arquivo:
        # Defina as colunas manualmente com base no formato dos dados
        colunas = ['Iteracao', 'Tempo de Execucao', 'Memoria Atual', 'Memoria Pico', 'Mochila', 'Valor Total']

        escritor_csv = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor_csv.writeheader()

        for i, linha in dados.items():
            # Extrai os valores diretamente com base nas chaves
            escritor_csv.writerow({
                'Iteracao': i,
                'Tempo de Execucao': linha['Tempo de Execucao'],
                'Memoria Atual': linha['Memoria Atual'],
                'Memoria Pico': linha['Memoria Pico'],
                'Mochila': linha['Mochila'],
                'Valor Total': linha['Valor Total'],
            })

    print(f'Dados salvos em {caminhoArquivo}')