n = int(input("Digite um número natual para obter o fatorial do mesmo: "))
i = 1
fatorialAcumulado = 1
while i <= n:
    fatorialAcumulado*= i
    i+= 1
print(fatorialAcumulado)
    