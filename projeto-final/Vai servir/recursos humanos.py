# Desenvolver uma aplicação que faça o cadastro de pessoas para um sistema de Recursos Humanos
# O cadastro deverá responder se sabe utilizar o computador e seu nível de idioma em inglês
# Ao final deverá apresentar a quantidade de pessoas que saber utilizar o computador
# A qualtidade de pessoas que saber o nivel Basico de inglês
# A qualtidade de pessoas que saber o nivel Intermediario de inglês
# A qualtidade de pessoas que sabe o novel Avançado de inglês
# A quantidade de pessoas que sabem o nivel Avançado de inglês e que sabem utilizar o computador


# Delharando Varias 

usoComputador = 0 
nivelBasio = 0
nivelIntermediario = 0
nivelAvancado = 0
computadorIdioma = 0

# Variavel para o usuario preencher
cadastro = input("Deseja Efetuar o Cadastro? (S/N): ")
while cadastro.upper() != "S" and cadastro.upper() != "N":
    print("Opção Inválida !")
    cadastro = input("Informe uma Opção Válida (S/N): ")

# Se o usuria aceitar a fazer o cadastro
while cadastro.upper() == "S":
    print("************************")
    print("Iniciando Cadastro !")
    print("************************")
    
     # Perguntar se Saber usar o computador
    computador = input(" Sabe Utilizar o Computador? (S/N): ")
    while computador.upper() != "S" and computador.upper() != "N":
        print("Opção Inválida !")
        computador = input(" Sabe Utilizar o Computador? (S/N): ")
    
    # Perguntar o Nivel de Inglês
    ingles = input("Nível do Idioma B- Básico, I-Intermediário, A- Avançado: ")
    while ingles.upper() != "B" and ingles.upper() != "I" and ingles.upper() != "A":
        print("Opção Inválida !")
        ingles = input("Nível do Idioma (B- Básico, I-Intermediário, A- Avançado: ")
    
    # Estrutura Condicional computador
    if computador.upper() == "S":
        usoComputador +=1

    if ingles.upper() == "B":
        nivelBasio += 1
    
    elif ingles.upper() == "I":
        nivelIntermediario += 1 
    
    else:
        nivelAvancado += 1 
    
    if computador.upper == "S" and ingles.upper() == "A":
        computadorIdioma += 1 
    
    cadastro = input(" Deseja Efetuar um Novo Cadastro? (S/N): ")
    while cadastro.upper() != "S" and cadastro.upper() != "N":
        print ("Opção Inválida !")
        cadastro = input(" Deseja Efetuar um Novo Cadastro? (S/N): ")

else: 
    print("****** FIM DOS CADASTROS *****")

print(" Total de pessoas que sabem utilizar o computador: " + str(usoComputador))
print("Total de pessoas que tem o nível de inglês básico: " + str(nivelBasio))
print("Total de pessoas que tem o nível de inglês intemédiario: " + str(nivelIntermediario))
print("Total de pessoas que tem o nível de inglês avançado: " + str(nivelAvancado))
print("Total de pessoas que tem que saber utilizar o computador e tem o nível avançado de inglês: " + str(usoComputador + nivelAvancado))