"""
Exercício 1 - Máximo
Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

"""
def maximo(num1: int, num2: int):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return num1
    else:
        return num2