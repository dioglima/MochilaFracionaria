from mochila_frac_n import construir_mochila

arquivo = open(f"instancia_{n}.txt", "r")
conteudo = arquivo.read()
arquivo.close()
# Converter a string em uma lista de tuplas usando a função eval
arr = eval(conteudo)

m, v = construir_mochila(arr, 10)

print(m)
print(v)
