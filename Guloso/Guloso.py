
# alteração aqui
def mochilafracionaria(p, v, n, c):
    x = [] 
    for i in range(1, n + 1):
        if p[i] <= c:
            x[i] = 1
            c = c - p[i]
        else:
            x[i] = c / p[i]
            break
    return x
