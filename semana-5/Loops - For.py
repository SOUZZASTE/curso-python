lista = ["Alfredo", "Marcio", "José", "Carolina", "Joana", "Luiza"]
for nome in lista:
    print(nome)

aluno = {"nome": "Marcia", "idade": 20, "nota": 9.2}

print("Exemplo 1a - iterando sobre chaves")
for chave in aluno:
    print(chave)

print("Exemplo 1b - iterando sobre chaves")
for chave in aluno.keys():
    print(chave)

print("Exemplo 2 - iterando sobre valores")
for valor in aluno.values():
    print(valor)

print("Exemplo 3 - iterando sobre ambos")
for chave, valor in aluno.items():
    print(chave + ": " + str(valor))