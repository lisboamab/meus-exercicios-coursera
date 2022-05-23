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