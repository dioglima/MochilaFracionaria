
def mochilafracionaria(p, v, n, c):
    x = {}
    for i in range(n):
        if p[i] <= c:
            x[i] = 1
            c = c - p[i]
        else:
            x[i] = c / p[i]
            break
    return x
