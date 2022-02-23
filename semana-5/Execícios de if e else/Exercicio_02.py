# Solicite ao usuario o sexo e a idade

# Caso a idade for maior ou igual a 18 e o sexo seja masculino

# Vamos solicitar a carteira de reservista

idade = int(input("Inform sua idade: "))
sexo = input("Informe o sexo (M/F): ")

if idade >= 18 and sexo.upper()== 'M':
    print("Serviço Militar Obrigatório")
    carteiraRservista = input("Informe sua Carteira de Reservista: ")
    print("Todos os dados coletados")

print("Fim da aplicação")