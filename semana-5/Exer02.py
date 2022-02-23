# Solicitar o sexo do usuário e a idade
# Caso a idade seja maior ou igual a 18 anos e seja do sexo masculino
# Vamos solicitar a carteira de reservista

# Solicitar a idade da pessoa
idade = int(input("Informe sua idade: "))

# Solicitar o sexo da pessoa
sexo = input("Informe o sexo (M/F): ")

# Condicional
# Se a idade do usuário for maior que 18 e for do sexo M:
if idade >= 18 and sexo.upper() == "M":
    print("Serviço Militar Obrigatorio")
    carteiraRservista = input("Informe o número da carteira reservista: ")
    print("Todos os dados coletados")

print("Fim da Aplicação")