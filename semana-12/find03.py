frase = "Indicar o ponto de inicio da busca"
palavra = "Indicar"
result = frase.find(palavra, 5)
print(result)


frase = "Passando o parametro de inicio e fim"
busca = input("Qual a palavra deseja buscar ? ")
inicio = int(input("Informe a posição inicial: "))
fim = int(input("Infotme a posição final: "))
resultado = frase.find(busca, inicio, fim)
print(resultado)