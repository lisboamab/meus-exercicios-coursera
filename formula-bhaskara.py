#scrip que calcula o valor de delta para saber se uma equação de segundo grau possui 1, 2 ou nenhuma raiz.
import math

def main():
    a= int(input("Digite o valor de a: "))
    b= int(input("Digite o valor de b: "))
    c= int(input("Digite o valor de c: "))
    imprime_valores(a, b, c)

def delta(a, b, c):
     return (b**2) - 4 * a * c

def imprime_valores(a, b, c):
    delta_local = delta(a, b, c)
    if delta_local > 0:
        raiz1 = (-b+(math.sqrt(delta_local)))/2*a
        raiz2 = (-b-(math.sqrt(delta_local)))/2*a
        if raiz1 < raiz2:
            print(f"as raízes da equação são {raiz1} e {raiz2}")
        else:
            print(f"as raízes da equação são {raiz2} e {raiz1}")
    elif delta_local < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz3 = (-b+(math.sqrt(delta_local)))/2*a
        print(f"a raiz desta equação é {raiz3}")