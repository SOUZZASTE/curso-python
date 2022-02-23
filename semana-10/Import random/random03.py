# Criar uma lista de 20 posições com números Randomicos
# Variando entre 1000 e 2000

import random

list = []
x=0

for x in range(20):
    list.append(random.randrange(1000, 2000))

print(list)