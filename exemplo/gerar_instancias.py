import random
def main():
    tuplas = []
    for i in range(50):
        tupla_int = (random.randint(1, 100), random.randint(1, 10))
        tuplas.append(tupla_int)
    

    arquivo = open("instancia.txt", "w")
    arquivo.write(str(tuplas))
    arquivo.close()


main()