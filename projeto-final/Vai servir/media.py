quantidade = int(input('Informe o total de cadastros: '))
totM=0
totF=0

for qt in range(quantidade):
    sexo = input('Informe o Sexo (M/F): ')
    while sexo.upper() != 'M' and sexo.upper() != 'F':
        print('Sexo invalido.')
        sexo = input('Informe o Sexo (M/F): ')

    resfriado = input('Algum sintoma de resfriado nos últimos 7 dias: (S/N): ')
    while resfriado.upper() != 'S' and resfriado.upper() != 'N':
        print('Responda S(Sim) ou N(Não)')
        resfriado = input('Algum sintoma de resfriado nos últimos 7 dias: (S/N): ')
    if sexo.upper() == 'M' and resfriado.upper() == 'N':
        totM += 1
    elif sexo.upper() == 'F' and resfriado.upper() == 'N':
        totF += 1
    print('***** Próximo Registro *****')
else:
    print('***** RESULTADO FINAL *****')

print('Total de Mulheres aptas a doação = '+str(totF))
print('Total de Homens aptos a doação = '+str(totM))
print('Total Geral de doadores aptos = ' +str(totF+totM))