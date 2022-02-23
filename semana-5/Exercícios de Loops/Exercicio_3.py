# Faça uma aplicação que tenha uma estrutura de repetição
# Solicitando uma palavra ao usuário
# Até que o usuário informe que o programa deve encerrar
# Após a finalização da aplicação, apresente ao usuário o número de palavras que ele inseriu no sistema


qtPalavras = 0
continuar = input("Deseja informar uma palavra ? (S/N): ")


while continuar.upper() != "S" and continuar.upper() != "N":
    continuar = input("Opção inválida. Informe S ou N: ")

while continuar.upper() == "S":
    qtPalavras+=1
    palavra = input("Informe uma palavra: ")
    continuar = input("Deseja continuar ? (S/N): ")
    while continuar.upper() != "S" and continuar.upper() != "N":
        continuar = input("Opção inválida. Informe S ou N: ")

print("Você informou " + str(qtPalavras) + " palavra(s) ao sistema")
