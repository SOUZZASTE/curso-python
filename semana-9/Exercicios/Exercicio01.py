# Programa para filtrar apenas os itens pares de uma lista

lista = [1,4,7,3,9,12,44,30]

lista_par = list(filter(lambda x:(x%2==0), lista))
print(lista_par)