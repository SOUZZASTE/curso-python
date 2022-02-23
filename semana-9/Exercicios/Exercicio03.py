# Uma lista retorna uma outra lista de numeros pares
# Maiores que 10


a = [1,3,4,6,8,12,14,26,39,5,50]

result=list(filter(lambda x : x % 2 == 0 and x >10, a))

print(result)
