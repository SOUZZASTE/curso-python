# Solicitar 3 valores e veremos se formam um triangulo equilatero

lado1 = int(input("Informe lado 1: "))
lado2 = int(input("Informe lado 2: "))
lado3 = int(input("Informe lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("Forma um triângulo equilátero")

else:
    print("Não foma um triângulo equilátero")

print("Fim da Aplicação . . .")