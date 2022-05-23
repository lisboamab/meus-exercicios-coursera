"""
def maior_primo(n):

    primos = []
    for i in range(n):
        c = 0
        for j in range(n):
            if i%(j+1) == 0: 
                c += 1
        if c == 2:
            primos.append(i)

    return(max(primos))
"""
def maior_primo(entrada):
    primos = 0
    for i in reversed(range(entrada + 1)):
        cont = 0
        for j in reversed(range(entrada + 1)):
            if i % (j + 1) == 0:
                cont += 1
        if cont == 2:
            primos = i
            break
    return primos

print(maior_primo(999))