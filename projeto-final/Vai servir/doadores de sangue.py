# Desenvolver uma aplicação para cadastro de doadores de sangue
# Neste projeto a etapa que iremos solicitar o número total de pessoa que serão cadastradas
# Condiderar se a pessoa está apta a doação de sangue
# Não ter tido resfriado nos últimos 7 dias
# Ao final devemos apresentar a quantidade total de pessoas aptas a doação de sangue
# Apresentar a quantidade de pessoas do sexo Masculino aptas para doação
# E do Sexo Famenino aptas para doação

# Variavel para receber informações do usuario sobre a quantidade de pessoas cadastradas
qualtidade = int(input(" Informe o total de cadastros: "))

# Zerar a quantidade de pessoas do sexo Masculino (M) e Feminico(F)
totM = 0
totF = 0

#Estrutura para Saber o Sexo
for qt in range(qualtidade):
    sexo = input("Informe o Sexo (M/F): ")
    while sexo.upper() != "M" and sexo.upper() != "F":
        print("Sexo Informado é Inválido !")
        sexo = input("Infome o Sexo (M/F): ")


# Estrutura Para Saber Se Teve Resfriado
    resfriado = input("Teve Algum Sintoma de Resfriado dos Últimos 7 Dias? (S/N): ")
    while resfriado.upper() != "S" and resfriado.upper() != "N":
        print("Informação Inválida !")
        resfriado = input(" Informe Corretamente (S/N): ")


# Estrura Condicional

# Se o Sexo for do sexo Masculino e resfriado for igual a negativo, a pessoa pode ser doadora
    if sexo.upper () == "M" and resfriado.upper() == "N":
        totM += 1
# Ou se, for do sexo feminino
    elif sexo.upper() == "F" and resfriado.upper() == "N":
        totF += 1

    # Mensagem ao Usuario para o Próximo Registro    
    print("******Próximo Registro******")

else:
    print("***** RESULTADO FINAL ! *****")

print("Total de Pessoad do Sexo Feminino Aptas a Doação = " +str(totF))
print("Total de Pessoad do Sexo Masculino Aptas a Doação = " +str(totM))
print("Total de Pessoas Aptas Para Doação = " +str(totF + totM))