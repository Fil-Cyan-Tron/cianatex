# Assumiamo che f in input abbia la forma di una stringa (il blocco indentato che definisce la funzione)

def smn(f, n, x):
    for i in range(n):
        F = f.split("a["+str(i)+"]");
        t = str(x[i])
        f = t.join(F)
    return f