# Combine o primeiro nome e o sobrenome da pessoa

completa = lambda nome,sobrenome: nome.strip().title() + " " +sobrenome.strip().title()

primeiro = str(input("Informe o nome: "))
segundo = str(input("Informe o sobrenome: "))

print(completa(primeiro,segundo))