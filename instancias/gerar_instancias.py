import random
def main(lista):
    lista_instancias = []
    qtd_instancias = len(lista)
    for i in range(qtd_instancias):
        tuplas = []
        for j in range(lista[i]):
            tupla_int = (random.randint(1, 100), random.randint(1, 10))
            tuplas.append(tupla_int)
        lista_instancias.append(tuplas)


    for instancia in range(qtd_instancias):
        arquivo = open(f"instancia_{instancia}.txt", "w")
        arquivo.write(str(lista_instancias[instancia]))
        arquivo.close()

lista = [20,40,60,80,100]
main(lista)