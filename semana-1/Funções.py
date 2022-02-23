
#Função print()
print("Olá, mundo !")

# Função comentario
#Isto é um comentário e não será executado pelo Python
print("Tudo o que está dentro da # não aparecerá na tela")

# Funções úteis para Strings

# Função capitalize () - Deixa a primeira da String maiúscula
string1= "olá ! Meu nome é Stefanie"

print(string1.capitalize())

# Função lower() - Deixa todas as letras minúsculas
string2= "OLÁ ! MEU NOME É STEFANIE"

print(string2.lower())

#Função upper() - Deixa todas as letras maiúscula
string3= "olá ! meu nome é stefanie"

print(string3.upper())

#Função center ()
string4= "Olá, meu nome é STEFANIE"

print(string4.center(50, "*"))

#Função ljust
string5= "Olá, mundo !"

print(string5.ljust(50,"*"))

#Função rjust
string6= "Olá, mundo !!!"

print(string5.rjust(50,"*"))

#Função find()
string7= "Olá!! meu nome é Stefanie"
substring1= "meu"
print(string7.find(substring1))
    
substring2 = "José"
print(string7.find(substring2))

# Função isalnum(), isalpha() e isumerico()
# Exemplo com Letras:
string8= "Stefanie"
print(string8.isalnum())
print(string8.isalpha())
print(string8.isnumeric())

# Exemplo com Números:
string9= "123"
print(string9.isalnum())
print(string9.isalpha())
print(string9.isnumeric())

# Exemplo com Letras e Números
string10= "Stefanie123"
print(string10.isalnum())
print(string10.isalpha())
print(string10.isnumeric())

# Função len()

string11=("Meu nome é Stefanie")
print(len(string11))

# Função replace()
string12= "Olá, meu nome é Stefanie"
print(string12.replace("Stefanie", "José"))

# Função strip(). rstrip(), lstripe()

string13= "Meu nome é Stefanie !"
print(string13)
print(string13.strip())
print(string13.rsplit())
print(string13.lstrip())
