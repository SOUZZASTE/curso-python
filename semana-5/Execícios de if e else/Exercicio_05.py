# Solicitar nome e peso de duas pessoas

# Apresentar o nome da pessoa com o maior peso

pessoa1 = str(input("Informe o nome da primeira pessoa: "))
peso1 = float(input("Informe o peso da primeira pessoa: "))

pessoa2 = str(input("Informe o nome da segunda pessoa: "))
peso2 = float(input("Informe o peso da segunda pessoa: "))

if peso1 > peso2:
    print("A pessoa com o maior peso é: "+pessoa1)

else:
    print("A pessoa com o maoir peso é: " +pessoa2)

print("Fim da Aplicação . . .")