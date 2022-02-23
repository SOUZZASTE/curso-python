# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:
# 11% para o Imposto de Renda
# 8% para o INSS
# 5% para o sindicato, faça um programa que nos dê:

nome = input("Digite seu nome: ")
horas = int(input("Horas trabalhadas por dia: "))
valorHora = float(input("Valor da hora de trabalho: R$ "))
descIR = (horas*valorHora / 100) * 11
descINSS = (horas*valorHora / 100) * 8
descSind = (horas*valorHora / 100) * 5
totDesc = descIR + descINSS + descSind

print("\n Olá " + nome + " aqui está informações sobre sua folha de pagamento: \n")

print("- Salário Bruto : R${0:5.2f}".format(horas*valorHora))
print("- R (11%) : R${0:5.2f}".format(descIR))
print("- INSS (8%) : R${0:5.2f}".format(descINSS))
print("- Sindicato ( 5%) : R${0:5.2f}".format(descSind))
print("= Salário Liquido : R${0:5.2f}".format((horas*valorHora) - totDesc))