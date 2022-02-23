#Lançamento de Notas
#Crie uma estrutura que permita o lançamento de notas para vários alunos
#Cada aluno terá 3 notas
#Nenhuma nota poderá receber nota inferior a 0(zero)
#Nenhuma nota poderá receber nota superior a 10(Dez)
#Somatório das três notas e divida por 3



aprovados = 0
exame = 0
reprovados = 0
totM=0
totF=0

# Inicio do Cadastro
cadastrar = input("Deseja inicar o cadastro de notas ? (S/N): ")
while cadastrar.upper() != "S" and cadastrar.upper() != "N":
    print("Opção inválida, por favor digitar S - para SIM e N - para NÃO")
    cadastrar = input("Deseja iniciar o lançamento das notas? (S/N): ")

# Nome do Aluno
while cadastrar.upper() == "S":
    nomeDoAluno = input("Nome do Aluno: ")

    # Sexo do Aluno
    sexo = input("Sexo do Aluno (F/M): ")
    while sexo.upper() != "F" and sexo.upper() != "M":
        print("Opção inválida, por favor digitar F - para FEMININO e M - para MASCULINO")
        sexo = input("Sexo do Aluno (F/M): ")

    # Lançamento das Notas    
    for cont in range(1,4):
        if cont == 1:
            nota1 = int(input("Informe a Primeita Nota: "))
            while nota1 < 0 or nota1 > 10:
                print("Primeita nota inválida, o valor deve ser entre 0 e 10")
                nota1 = int(input("Informe a Primeita Nota: "))

        elif cont == 2:
            nota2 = int(input("Informe a Segunda Nota: "))
            while nota2 < 0 or nota2 > 10:
                print(" Segunda nota inválida, o valor deve ser entre 0 e 10")
                nota2 = int(input("Informe a Segunda nota"))
        else:
            nota3 = (int(input("Informe a Terceira Nota: ")))
            while nota3 < 0 or nota3 > 10:
                print(" Terceira nota inválida, o valor deve ser entre 0 e 10")
                nota3 = int(input("Informe a Terceira Nota"))
    

    #Verificar o print mostrando a média
    media = (nota1+nota2+nota3)/3
    print("A média do(a) " + nomeDoAluno + " foi de: " + format(media, ".1f"))
    if media >= 7:
        aprovados += 1
    elif media >= 4:
        exame += 1
    else:
        reprovados += 1
    
    # Estrutura de Repetição
    cadastrar = input("Deseja Efetuar outro Lançamento ? (S/N): ")
    while cadastrar.upper() != "S" and cadastrar.upper() != "N":
        print("Opção inválida, por favor digitar S ou N")
        cadastrar = input("Deseja Efetuar outro Lançamento ? (S/N): ")
else:
    print("***** LANÇAMENTOS FINALIZADOS ******")

print("***** RESULTADO FINAL ******")

print("Quantidade de pessoas do sexo feminino aprovadas " + str(aprovados + totF))
print("Quantidade de pessoas do sexo masculino aprovados: " + str(aprovados + totM))