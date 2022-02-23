# Faça um algoritmo que solcite ao usuário números
# E os armazene em um velor de 10 posições
# Criar uma função que receba o vetor preenchido
# E substitua todas as ocorrências de valores positivos
# Por 1 e todos os valores negativos por 0.

# Criando a função DEF
def troca(vet):
    for i in range(10):
        if vet[i] >= 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet

# Construindo o vetor
vet = [0]*10
for i in range(10):
    vet[i] = int(input("Digite um valor: "))

# Chamar a função
troca(vet)
print(vet)


