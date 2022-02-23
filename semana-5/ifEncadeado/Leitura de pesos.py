# Ler o nome de três pessoas e o seus pesos

# Mostrar os dados (nome e peso) em ordem decresente de peso

nome1 = input("Informe o primeiro nome: ")
peso1 = input("Informe o peso: ")

nome2 = input("Informe o segundo nome: ")
peso2 = input("Informe o peso: ")

nome3 = input("Informe o terceiro nome: ")
peso3 = input("Informe o peso: ")

if peso1 > peso2 and peso1 > peso3:
    print("O nome da pessoa com o maior peso é " + nome1+ " e seu peso é " + peso1)
    if peso2 > peso3:
        print("O nome da pessoa com o peso médio é " + nome2 + " e seu peso é " + peso2)
        print("o nome da pessoa com o menor peso é " + nome3 + " e seu peso é " + peso3)
    else:
        print("O nome da pessoa com peso médio é " + nome3 + " e seu peso é " + peso3)
        print("O nome da pessoa com o peso médio é " + nome2 + " e seu peso é " + peso2)

elif peso2 > peso1 and peso2 > peso3:
        print("O nome da pessoa com o maior peso é " + nome2+ " e seu peso é " + peso2)
        if peso1 > peso3:
            print("O nome da pessoa com o peso médio é " + nome1 + " e seu peso é " + peso1)
            print("o nome da pessoa com o menor peso é " + nome3 + " e seu peso é " + peso3)
        else:
            print("O nome da pessoa com peso médio é " + nome3 + " e seu peso é " + peso3)
            print("o nome da pessoa com o menor peso é " + nome1 + " e seu peso é " + peso1)
else:
    print("O nome da pessoa com o maior peso é " + nome3+ " e seu peso é " + peso3)
    if peso1 > peso2:
        print("O nome da pessoa com peso médio é " + nome1 + " e seu peso é " + peso1)
        print("o nome da pessoa com o menor peso é " + nome2 + " e seu peso é " + peso2)
    else:
        print("O nome da pessoa com peso médio é " + nome2 + " e seu peso é " + peso2)
        print("o nome da pessoa com o menor peso é " + nome1 + " e seu peso é " + peso1)

    print("Fim da Aplicação . . . ")



