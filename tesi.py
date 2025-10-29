# Assumiamo di avere sempre parametri legali

# (1) funzione nulla
def zero(x):
    return 0

# (2) successore
def succ(n):
    return n+1

# (3) proiezioni
def proj(i, x):
    return x[i]

# (4) composizione
def comp(g, f, x):
    return g(f(x))

# (5) ricorsione primitiva
def ric(g, f, x, y):
    if y == 0:
        return f(x)
    else:
        return g(x, y-1, ric(g, f, x, y-1))
    
# (6) minimalizzazione
def minimalize(f, x):
    y = 0
    while f(x, y) > 0:
        y = y+1