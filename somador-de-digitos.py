"""
Exercício 3
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:
Digite um número inteiro: 123
6

Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, 
aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da 
divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.
"""
numero = int(input("Digite um número inteiro: "))
s = 0
while numero > 0:
    s += numero % 10 # Soma `s` ao ultimo numero de `numero`
    numero //= 10 # Remove o ultimo numero de `n`
print(s)

