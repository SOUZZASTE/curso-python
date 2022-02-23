# Faça uma aplicação que receba um número e mostre os proximos três números

numero = int(input("Informe um número: "))
contatdor = 1
print("O número informado foi " + str(numero))

while(contatdor <= 3):
    numero+=1
    print("Próximo: " + str(numero))
    contatdor+=1

print("Fim da Aplicação . . . ")