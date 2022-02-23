# Desenvolver uma Aplicação que repita a inserção de dados de alunos (Nome, Nota 1, Nota 2 e Nota 3)
# Até que o usuário peça para parar a aplicação
# As notas para serem consideradas validas devem estar entre 0 e 10
# Apresentar as notas no final
# Quantidade de alunos aprovados (médias >= 7)
# Quantidade de reprovados (média <= 4)
# Quantidade de anos de exame final (média >= 4 e < 7)


# Declarar variavel
aprovados = 0
exame = 0
reprovados = 0 

# Se o usuário deseja começar a cadastrar
cadastrar = input("Deseja iniciar o lançamento das notas? (S/N): ")
while cadastrar.upper() != "S" and cadastrar.upper() != "N":
    print("Opção inválida, por favor digitar S ou N")
    cadastrar = input("Deseja iniciar o lançamento das notas? (S/N): ")

# Estrutura de repetição Caso o Usuário Digite S
while cadastrar.upper() == "S":
    nome = input("Nome do aluno: ")
    for cont in range(1,4):
        if cont == 1:
            nota1 = int(input("Informe a Primeita Nota: "))
            while nota1 < 0 or nota1 > 10:
                nota1 = int(input("Primeita nota inválida, o valor deve ser entre 0 e 10"))
        elif cont == 2:
            nota2 = int(input("Informe a Segunda Nota: "))
            while nota2 < 0 or nota2 > 10:
                nota2 = int(input(" Segunda nota inválida, o valor deve ser entre 0 e 10"))
        else:
            nota3 = (int(input("Informe a Terceira Nota: ")))
            while nota3 < 0 or nota3 > 10:
                nota3 = int(input(" Terceira nota inválida, o valor deve ser entre 0 e 10"))
    
    # Calcular média e verificar status
    media = (nota1+nota2+nota3)/3
    print(str(media))
    if media >= 7 :
        aprovados += 1
    elif media >= 4:
        exame += 1
    else:
        reprovados += 1
    
    cadastrar = input("Deseja Efetuar outro Lançamento ? (S/N): ")
    while cadastrar.upper() != "S" and cadastrar.upper() != "N":
        print("Opção inválida, por favor digitar S ou N")
        cadastrar = input("Deseja Efetuar outro Lançamento ? (S/N): ")
else:
    print("***** LANÇAMENTOS FINALIZADOS ******")

print("Total de alunos APROVADOS: " + str(aprovados))
print("Total de alunos de EXAME FINAL: " + str(exame))
print("Total de alubos REPROVADOS: " + str(reprovados))