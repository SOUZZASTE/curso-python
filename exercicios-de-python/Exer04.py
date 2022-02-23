nome = input("Informe o nome completo do aluno: ")
nota1 = int(input("Informe a nota do primeiro semestre: "))
if nota1 > 10:
    print("Nota inválida, por favor formecer uma nota de 0 a 10: ")
    nota1 = int(input("Informe a nota do primeiro semestre: "))


nota2 = int(input("Informe a nota do segundo semestre: "))
if nota2 > 10:
    print("Nota inválida, por favor formecer uma nota de 0 a 10: ")
    nota2 = int(input("Informe a nota do primeiro semestre: "))


nota3 = int(input("Informe a nota do terceiro semestre: "))
if nota3 > 10:
    print("Nota inválida, por favor formecer uma nota de 0 a 10: ")
    nota3 = int(input("Informe a nota do primeiro semestre: "))


nota4 = int(input("Informe a nota do quarto semestre: "))
if nota4 > 10:
    print("Nota inválida, por favor formecer uma nota de 0 a 10: ")
    nota4 = int(input("Informe a nota do primeiro semestre: "))



media = (nota1 + nota2 + nota3 + nota4) / 4

print("Nota final do Aluno(a) %s " % nome + "é: " + str(media))
