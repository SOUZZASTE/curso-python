# Verificando se o conteúdo de uma váriavel é Alpha (somente Strings)

# Se a String possui apenas letras
endereco = "Av. Paulista"
print(endereco.isalpha())

endereco = "Av. Paulista, 247"
print(endereco.isalpha())

sobreNome = "Machado"
print(sobreNome.isalpha())

sobrenome = "IV"
print(sobrenome.isalpha())

especiais = "#$)*"
print(especiais.isalpha())
