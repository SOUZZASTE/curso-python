# Criar uma função que calcule a área de um círculo

import math

def calculo (r):
    area = math.pi * r**2
    return area

raio = int(input("Informe o valor do raio do circulo em metros: "))

print(calculo(raio))

