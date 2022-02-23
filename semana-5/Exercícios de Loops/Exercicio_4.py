# Escrva um programa que solicita 10 números ao usuário
# Através de um laço while, e ao final mostre
# Qual dos números é o maior
# Qualdos números é o menor
# E qual é a média dos números

quantidade = 1 
somatorio = 0

while quantidade < 11 :
    numero = int(input(" Informe um número: "))
    if quantidade == 1:
        maior = numero
        menor = numero
    elif (numero > maior):
        maior = numero
    elif (numero < menor):
        menor = numero

    somatorio += numero
    quantidade += 1

else:
    media = somatorio/10

print(" O maior valor é: " + str(maior))
print("O menor valor é: " + str(menor))
print("A média é: " + str(media))
