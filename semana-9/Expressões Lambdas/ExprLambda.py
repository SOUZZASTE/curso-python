# Aplicação uilizando função e expressão labda
# Para comprção de sintaxe

def subtrair(num1, num2):
    return num1-num2

# Função Lambda
sub = lambda a, b: a-b

vl1 = int(input("Informe o Primeiro valor: "))
vl2 = int(input("Informe o Segundo Valor: "))

# Utilizando a expressão LAMBDA
print("Expressão LAMBDA")
print(sub(vl1, vl2))


# Função DEF
print("Função DEF")
print(subtrair(vl1, vl2))