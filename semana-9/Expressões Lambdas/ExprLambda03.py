# Iremos percorrer os valores de uma lista e elevalos ao qudrado
# Assim é retornado o dobro deles com a operação: x*2
# E como a operação irá nos rteornar um mao object utilizamos
# O metodo liste para voltar a ter array

lista = [2,5,3,7,9]

# MAP: Mapeamento 
elev = list(map(lambda x: x**2, lista))
print(elev)