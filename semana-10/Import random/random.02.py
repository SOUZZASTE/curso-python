# Criar uma lista de 10 posições com números Randomicos
# Limitados a 100

import random

lista = []
x=0
for x in range(10):
    lista.append(random.randrange(100))

print(lista)