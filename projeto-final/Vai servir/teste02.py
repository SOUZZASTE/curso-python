aprovados = 0
exame = 0
reprovados = 0
totCad = 0
totMas=0
totFem=0

# Inicio do Cadastro
cadastro = input("Deseja inicar o cadastro de notas ? (S/N): ").upper()
while (cadastro != 'S' and cadastro!='N'):
    print ("Opção inválida, por favor digitar S - para SIM e N - para NÃO")
    cadastro = input("Deseja inicar o cadastro de notas ? (S/N): ").upper()

# Nome do aluno
while cadastro.upper() == "S":
    totCad += 1
    nomeDoAluno = input("Nome do Aluno: ")

    #Sexo do Aluno
    sexo = input("Sexo do Aluno (F/M): ").upper()
    while (sexo != 'M' and sexo != 'F'):
        print("Opção inválida, por favor digitar F - para FEMININO e M - para MASCULINO")
        sexo = input("Sexo do Aluno (F/M): ").upper()

    if (sexo == 'M'):
        totMas += 1
    else:
        totFem += 1
    
    if (aprovados >= 10):
        nota1 = float(input("Informe a Primeita Nota: "))
        while (nota1 < 0 or nota1 > 10):
            print("Primeita nota inválida, o valor deve ser entre 0 e 10")
            nota1 = float(input("Informe a Primeita Nota: "))
            aprovados += 1 
