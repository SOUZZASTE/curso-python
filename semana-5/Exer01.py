# Usuário irá informar um número 
# Vamos verificar se o valor é maior que 100
# Se for maior, vamos calcular 10%

valor = int(input("Informe um valor: "))

#Se o valor for maior que 100:
if valor > 100:
    valor = valor * 0.1

print("Valor é: " + str(valor))
