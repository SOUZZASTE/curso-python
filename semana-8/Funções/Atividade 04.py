# Criar uma função que ira retornar os resultados de operações entre dois números
# Retornar se o primeiro número é par
# retornar a multiplicação do primeiro pelo segundo número


def calcular(x, y):
    return x %2 == 0, x*y

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

print(calcular(num1, num2))