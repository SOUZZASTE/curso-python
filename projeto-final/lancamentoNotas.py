aprovados = 0
exame = 0
reprovados = 0
sexos = [0, 0, 0, 0, 0, 0]

cadastrar = input('Deseja iniciar lançamentos (S/N)? ')
while cadastrar.upper() != 'S' and cadastrar.upper() != 'N':
    cadastrar = input('Opção Inválida, informe (S/N): ')

while cadastrar.upper() == 'S':
    sexo = input('Informe sexo do aluno: ')
    while sexo.upper() != 'M' and sexo.upper() != 'F':
        print('Sexo invalido.')
        sexo = input('Informe o Sexo (M/F): ')
    nome = input('Informe nome do aluno: ')
    for cont in range(1, 4):
        if cont == 1:
            nota1 = int(input('Informe Nota1:'))
            while nota1 < 0 or nota1 > 10:
                nota1 = int(input('Nota1 inválido, valor deve ser entre 0 e 10: '))
        elif cont == 2:
            nota2 = int(input('Informe Nota2:'))
            while nota2 < 0 or nota2 > 10:
                nota2 = int(input('Nota2 inválido, valor deve ser entre 0 e 10: '))
        else:
            nota3 = int(input('Informe Nota3:'))
            while nota3 < 0 or nota3 > 10:
                nota3 = int(input('Nota3 inválido, valor deve ser entre 0 e 10: '))

    #calculo da média
    media = (nota1+nota2+nota3)/3
    print('Média aluno ' + nome.title() + ': ' + str(media))
    if media >= 7:
        if sexo.upper() == 'M':
            sexos[0] += 1
        else:
            sexos[1] += 1
        aprovados += 1
        print('Aluno aprovado')
    elif media>=4 and media<7:
        if sexo.upper() == 'M':
            sexos[2] += 1
        else:
            sexos[3] += 1
        exame += 1
        print('Aluno de exame')
    else:
        if sexo.upper() == 'M' and media<3:
            sexos[4] += 1
        else:
            sexos[5] += 1
        reprovados += 1
        print('Aluno reprovado')

    cadastrar = input('Deseja efetuar outro lançamento (S/N)? ')
    while cadastrar.upper() != 'S' and cadastrar.upper() != 'N':
        cadastrar = input('Opção Inválida, informe (S/N): ')

else:
    print('Lancamentos Finalizados')

#Total
totaldealunos = (aprovados+exame+reprovados)
print('Total de alunos cadastrados: ' +str(totaldealunos))
print('*******')

#percentual
print('Percentual de alunos Aprovados', (aprovados/totaldealunos)*100, '%')
print('Percentual de alunos Exame', (exame/totaldealunos)*100, '%')
print('Percentual de alunos Reprovados', (reprovados/totaldealunos)*100, '%')
print('*******')

#valores absolutos
print('Total de alunos APROVADOS: ' + str(aprovados))
print('Total de alunos de EXAME: ' + str(exame))
print('Total de alunos REPROVADOS: ' + str(reprovados))

print('*******')

print('Total de alunos sexo masculino Aprovados: ' + str(sexos[0]))
print('Total de alunos sexo feminino Aprovados: ' + str(sexos[1]))
print('Total de alunos sexo masculino Exame: ' + str(sexos[2]))
print('Total de alunos sexo feminino Exame: ' + str(sexos[3]))
print('Total de alunos sexo masculino Reprovados: ' + str(sexos[4]))
print('Total de alunos sexo feminino Reprovados: ' + str(sexos[5]))