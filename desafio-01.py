#Desafio #01
# Escreva uma função em Python para encontrar os fatores primos que compõem um número.

def fatores_primos(n):
    fatores = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return fatores

fatores = fatores_primos(60)
print(fatores)