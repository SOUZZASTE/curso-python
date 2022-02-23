#Criando variáveis
a= 3
b= 7
print(a+b)

#Alterando o valor da variável
a= "Agora a variável vira uma String"
print(a)

# Designando uma variável com o valor de outra variavél
b= a
print(a)

#Definição de Mútiplas variáveis com valores iguais
x=y=z= 10
print(x)
print(y)
print(z)

#Deifinição de Múltiplas variáveis com valores diferentes
x,y,z= 10,20,30
print(x)
print(y)
print(z)

#Função inpult(): Tem a função de captar informações preenchidas pelos usuários
nome=input("Olá, quel é o seu nome ?")
print("Olá, %s" % nome)