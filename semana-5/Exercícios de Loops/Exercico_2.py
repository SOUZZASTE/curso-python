# Faça uma aplicação que receba o nome e o sexo de uma pessoa

# Sendo no sexo o valor M para masculino e F para Feminino

# No final apresentar o sexo e o nome da pessoa

nome = input("Informe o seu nome: ")
sexo = input("Informe o seu sexo (M/F): ")

while sexo.upper() != "F" and sexo.upper() != "M":
    sexo = input("Sexo Incorreto. Informe M ou F: ")

print("A pessoa de nome " + nome.upper() + " é do sexo " + sexo.upper())