# Strings

string1 = "Oi, Python !"
string2 = 'Tchau, Python !'

# Para executar a string
print(string1)
print(string2)


string_grande = '''Olá. Esta é uma string grande no Python.
Aqui você pode usar " ou ' 
Caracteres são escapados como se espera.
É a terceira forma de definir uma STRING, apesar de não ser tão usual....
\t  testanto o TAB para finalizar'''
print (string_grande)

# Escapando strings

string3 = "A cantora Sinned O'Connor."
string4 = 'Alfredo disse "Corram aqui pra ver isso !"'

print(string3)
print(string4)


#Utilizando R para representar uma String
string8 = r"Ulilizamos \n para inserir uma nova linha na String."

print(string8)

#Inserindo Variáveis em uma String
nome = 'Stefanie'
idade = 25 # Número inteiro (Intenger)

print("Meu nome é %s " % nome)
print("Tenho %d anos " % idade)

altura = 1.65

print("E tenho %.2f de altura" % altura) #Númenos Dicimais (Float)

#Difinindo a quantidade de algorismos depois do ponto
a=30.42657

print("Formatando Decimais: %.2f" % a)
print("Formatandi Decimais: %.3f" % a)

#Inserindo mais de um valor na String

nome="Stefanie"
idade= 25

print("Meu nome é %s e tenho %d anos " % (nome, idade))

# Concatenação (Juntando Strings e Variáveis como sinal de "+")
nome ="Stefanie"

print("Olá, meu nome é " + nome)

# Não pode ser realizado da seguinte forma:
nome="Stefanie"
idade=25

# print("Olá, meu nome é" + nome + "e tenho" + idade + "anos.") ---- Forma errada

print("Olá, meu nome é " + nome + " e tenho " + str(idade) + " anos.") # Forma certa

# Usando a função + com números decimais
valor= 503.78987

print("O valor é " + str(valor))

# Formatado os números decimais

valor2= 503.78987

print("O valor é " + format (valor2,'.2f'))




