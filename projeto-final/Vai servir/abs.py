nomeAluno = input("Digite o nome do Aluno: ")

sexo = input('Qual o Sexo (M/F): ').upper()
while (sexo != 'M' and sexo != 'F'):
    print('Opção Inválida')
    sexo = input('Informe M-Masculino ou F-Feminino: ').upper()
