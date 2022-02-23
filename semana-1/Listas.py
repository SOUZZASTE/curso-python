# Criando uma Lista
alunos= ["José", "João", "Luiz"]
notas= [8.5, 9.2, 6.7]
listaVazia= []
print(alunos)
print(notas)
print(listaVazia)

# Listas podem conter informações variadas
listaMisturada= [12, 12.56, "Sorvteris", ["Baunilha", "Chocolate"]]
print(listaMisturada)

# Acessando itens de uma lista utilizando o índice (posição)
print(alunos[0])
print(notas[2])

# Acessando itens de uma lista utilizando o índice (posição), com números negativos
print(alunos[-1])
print(notas[-3])

# Alterando o valor de um índice
print(notas)
notas[2]= 7.7
print(notas)

# Função apped() - Adiciona um item a lista
print(alunos)
alunos.append("Alfredo")
print(alunos)

#Função insert() - Adiciona mais um intem na posição desejada
print(alunos)
alunos.insert(1, "Daniela")
print(alunos)

# Função extend() - Adiciona uma lista no final da lista
print(alunos)
novosAlunos= ["Carlos", "Maria", "Ana"]
alunos.extend(novosAlunos)
print(alunos)

# Concatenar, ou seja, juntar duas listas
alunos1= ["José", "Daniela", "João"]
alunos2= ["Carlos", "Denis", "Augusto"]
print(alunos1+alunos2)

# Multiplicando uma lista
print(notas)
print(notas*2)

# Removendo Itens de uma Lista

#Função remover()
print(alunos)
alunos.remove("João")
print(alunos)

# Função pop()
print(alunos)
alunosRemovidos= alunos.pop()
print(alunosRemovidos)
alunosRemovidos= alunos.pop(2)
print(alunosRemovidos)

# Função slicing []
print(alunos)
print(alunos[0:2])
print(alunos[2:4])
print(alunos[2:5])

print(alunos[:3])
print(alunos[3:])

# Funções úteis para trabalhar com listas

# Função len()
print(len(alunos))

# Funções max() e min()
print(max(notas))
print(min(notas))

# Função copy()

# Se a função copy()
alunos= ["José", "João", "Luiz", "Carlos", "Alfredo"]
alunosBackup= alunos
print(alunosBackup)
alunos.clear()
print(alunosBackup)

# Com a função copy()
alunos= ["José", "Daniela", "Carla", "Carlos", "Augusto", "Denis"]
alunos_backup= alunos.copy()
print(alunos_backup)
alunos.clear()
print(alunos_backup)

# Função count()
alunos = ['José', 'Daniela', 'Carla', 'Carlos', 'Augusto', 'Denis']
alunos.extend(['Daniela', 'Felipe', 'Carla', 'Daniela'])
print(alunos.count('Daniela'))

# Função sort()
print(alunos)
alunos.sort()
print(alunos)
 
# Função reverse()
alunos.reverse()
print(alunos)

# Função in
print("José" in alunos)
print("Feline" in alunos)

# Funções split() e join()
alunosString= "; " .join(alunos)
print(alunosString)
alunosLista= alunosString.split("; ")
print(alunosLista)