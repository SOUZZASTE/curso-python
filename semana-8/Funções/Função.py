def print_ola_tres_vezes():
    print("Olá, Python")
    print("Olá, Python")
    print("Olá, Python")

print_ola_tres_vezes()

def numero_ao_cubo(numero):
    valor_a_retornar =  numero * numero * numero
    return(valor_a_retornar)

numero = numero_ao_cubo(4)
print(numero)

def print_ola(nome= "estranho"):
    print("Olá, " + nome)

print_ola("Stefanie")
print_ola()

def print_infos(nome, idade):
    print_ola("Olá, meu nome é %s e tenho %d anos" % (nome, idade))

print_infos(idade= 26, nome= "Stefanie")