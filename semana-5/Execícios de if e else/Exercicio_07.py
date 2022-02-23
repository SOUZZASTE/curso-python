# Solicitar dois valores

# Verificar se é par ou impat

valor1 = int(input("Informar o primeiro valor: "))
valor2 = int(input("Informar o segundo valor: "))

valor3 = valor1**valor2

resto = valor3 % 2

if resto == 0:
    print("O resultado da potência do primeiro valor pelo segundo valor, gerou um número PAR . . .")

else:
    print("O resultado da potência do primeiro valor pelo segundo valor, gerou um número IMPAR . . .")

print("Fim da Aplicação !")