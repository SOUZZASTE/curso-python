# Solicitar  ao usuario 3 notas

# Calcular a media

# Caso menor que 6, mensagem: Aumentar a dedicação

# Caso maior que 6, mensagem: Continue assim

nomeAluno = str(input("Informe o do aluno: "))

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))

media = (n1+n2+n3) / 3


if media < 6:
    print("Você precisa se dedicar mais !")
else:
    print("Continue assim . . .")

print("Olá," + nomeAluno + " sua média foi: " + format(media, ".1f"))
print("Fim da aplicação")