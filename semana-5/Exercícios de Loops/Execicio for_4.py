# Escreva um programa que pergunte ao usuário quantos alunos ele tem em sala de aula.
# Em seguida, através de um laço FOR, peça para que entre com as notas de todos os alunos da sala, um por vez
# Por fim, o programa deve mostrar a média atrtmética da turma.

qt = int(input("Quantos alunos você possui? "))
somaNota = 0
media = 0

for qtAluno in range(qt):
    nota = int(input("Informe a nota: "))
    somaNota += nota
else:
    media = somaNota/qt

print("A média da turma foi: " + str(media))