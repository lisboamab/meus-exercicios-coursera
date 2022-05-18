#scrip que calcula o valor de delta para saber se uma equação de segundo grau possui 1, 2 ou nenhuma raiz.
import math
import time
a= int(input("Digite o valor de a: "))
time.sleep(1)
b= int(input("Digite o valor de b: "))
time.sleep(1)
c= int(input("Digite o valor de c: "))
time.sleep(1)

delta = (b**2) - 4 * a * c

if delta > 0:
    raiz1 = (-b+(math.sqrt(delta)))/2*a
    raiz2 = (-b-(math.sqrt(delta)))/2*a
    print(f"Essa equação possui 2 raizes que são: {raiz1} e {raiz2}")
elif delta < 0:
    print("A equação não possui raizes reais")
else:
    raiz3 = (-b+(math.sqrt(delta)))/2*a
    print(f"Essa equação possui 1 raiz real que é: {raiz3}")