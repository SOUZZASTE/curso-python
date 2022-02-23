#Lançamento de Notas:
#Crie uma estrutura que permita o lançamento de notas para vários alunos
#Cada aluno terá 3 notas
#Nenhuma nota poderá receber nota inferior a 0(zero)
#Nenhuma nota poderá receber nota superior a 10(Dez)
#Somatório das três notas e divida por 3


aprovados = 0
exame = 0
reprovados = 0
totCad = 0
totMas = 0
totFem = 0
medSexo = [0,0,0,0,0,0,]

# Inicio do Cadastro
cadastro = input("Deseja iniciar o cadastro de notas ? (S/N): ").upper()
while (cadastro != "S" and cadastro!= "N"):
    print("Opção inválida, por favor digitar S - para SIM e N - para NÃO")
    cadastro = input("Deseja inicar o cadastro de notas ? (S/N): ").upper()

# Nome do aluno
while cadastro.upper() == "S":
    totCad += 1
    nomeDoAluno = input("Nome do Aluno: ")

    # Sexo
    sexo = input("Informe o Sexo (F/M): ").upper()
    while (sexo != "F" and sexo != "M"):
        print("Opção Inválida, informe F - Feminino ou M - Masculino:")
        sexo = input("Informe o Sexo (F/M): ").upper()

    if (sexo == "F"):
        totFem += 1
    else:
        totMas += 1

    # Lançamento das Notas
    for cont in range(1,4):
        if cont == 1:
            nota1 = float(input("Informe a Primeira Nota: "))
            while nota1 < 0 or nota1 > 10:
                print("Primeira nota inválida, o valor deve ser entre 0 e 10")
                nota1 = float(input("Informe a Primeira Nota: "))
        elif cont == 2:
            nota2 = float(input("Informe a Segunda Nota: "))
            while nota2 < 0 or nota2 > 10:
                print("Segunda nota inválida, o valor deve ser entre 0 e 10")
                nota2 = float(input("Informe a Segunda Nota: "))
        else:
            nota3 = float(input("Informe a Terceira Nota: "))
            while nota3 < 0 or nota3 > 10:
                print("Terceira nota inválida, o valor deve ser entre 0 e 10")
                nota3 = float(input("Informe a Terceira Nota: "))
    
    # Média
    media = (nota1+nota2+nota3)/3

    print("A média do(a) " + nomeDoAluno + " foi de: " + format(media, ".1f"))
    if media >= 7:
        if sexo.upper() == 'F':
            medSexo[0] += 1
        else:
            medSexo[1] += 1
        aprovados += 1
        print('Aluno aprovado')
    elif media>=4 and media<7:
        if sexo.upper() == 'F':
            medSexo[2] += 1
        else:
            medSexo[3] += 1
        exame += 1
        print('Aluno de exame')
    else:
        if sexo.upper() == 'F' and media<3:
            medSexo[4] += 1
        else:
            medSexo[5] += 1
        reprovados += 1
        print('Aluno reprovado')
    
    # Estrutura de Repetição
    print("\n")
    cadastro = input("Deseja iniciar o cadastro de notas ? (S/N): ").upper()
    while (cadastro != "S" and cadastro!= "N"):
        print ("Opção inválida, por favor digitar S - para SIM e N - para NÃO")
        cadastro = input("Deseja inicar o cadastro de notas ? (S/N): ").upper()
else:
    print("LANÇAMENTO DAS NOTAS FINALIZADOS".center(50,"*"))
    print("\n")


print("Resultado".center(50, "*"))
# Retirar
print("Quantidade de alunos CADASTRADOS: ", totCad)       
print("Quantidade de alunos APROVADOS: ", aprovados)
print("Quantidade de alunos EXAME: ", exame)
print("Quantidade de alunos REPROVADOS: ", reprovados)
print("\n")

print("PORCENTAGEM".center(50,"*"))
print("Quantidade percentual de alunos APROVADOS: {0:.0f}".format((aprovados*100)/totCad), "%")
print("Quantidade percentual de alunos EXAME: {0:.0f}".format((exame*100)/totCad), "%")
print("Quantidade percentual de alunos REPROVADOS: {0:.0f}".format((reprovados*100)/totCad), "%")
print("\n")
# Retirar
print("Quantidade de pessoas do sexo feminino CADASTRADAS: ", totFem)
print("Quantidade de pessoas do sexo masculino CADASTRADAS: ", totMas)
print("\n")

print("VALORES ABSOLUTOS".center(50,"*"))

print("Quantidade de pessoas do sexo FEMININO APROVADAS: ", (medSexo[0]))
print("Quantidade de pessoas do sexo MASCULINO APROVADOS: ", (medSexo[1]))
print("Quantidade de pessoas do sexo FEMININO DE EXAME: ", (medSexo[2]))
print("Quantidade de pessoas do sexo MASCULINO DE EXAME: ", (medSexo[3]))
print("Quantidade de pessoas do sexo FEMININO REPROVADAS: ", (medSexo[4]))
print("Quantidade de pessoas do sexo MASCULINO REPROVADOS: ", (medSexo[5]))