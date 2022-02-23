import random

lista = []
x=0

for x in range(10):
    lista.append(random.randrange(100))

print(lista)
print(type(lista))