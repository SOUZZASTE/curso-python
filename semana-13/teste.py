#Possuir no mínimo dez centímetros em cada mecha;
#Ter atenção para que os fios cortados não toquem o chão;
#Não ter nenhuma doença capilar;
#Guardar os fios secos e limpos em um saco plástico;

continuar = input('Deseja iniciar o sistema(S/N) ? ').upper()
while (continuar != 'S' and continuar!='N'):
    print ('Opção Inválida')
    continuar = input('Informe S-Sim ou N-Não: ').upper()

totalDoadores = 0
totalMasculino = 0
totalFeminino = 0
doacoesPerdidas = 0


while (continuar == 'S'):
    totalDoadores +=1
    nome = input('Informe seu nome: ')

    sexo = input('Qual o Sexo (M/F): ').upper()
    while (sexo != 'M' and sexo != 'F'):
        print('Opção Inválida')
        sexo = input('Informe M-Masculino ou F-Feminino: ').upper()

    #Doadores por Sexo
    if (sexo == 'M'):
        totalMasculino +=1
    else:
        totalFeminino +=1
    tamanhoMecha = int(input('Qual o tamanho da mecha em centímetros? '))    

    #Teste Tamanho da Mecha
    if (tamanhoMecha<10):
        print('Para doação a mecha deve possuir no mínimo 10cm.')
        print('Deixe seu cabelo crescer mais um pouco.')
        doacoesPerdidas += 1

    else:
        tocouChao = input('Durante o processo os cabelos tocaram no chão (S/N)? ').upper()
        while (tocouChao != 'S' and tocouChao != 'N'):
            print('Opção Inválida')
            tocouChao = input('Informe S-Sim ou N-Não: ').upper()

        #Teste se a mecha tocou o chão
        if (tocouChao == 'S') :
            print('Para doação a mecha não pode ter tocado o chão.')
            doacoesPerdidas += 1

        else:
            doencaCapilar = input('Doador possui alguma doença capilar (S/N)?').upper()
            while (doencaCapilar != 'S' and doencaCapilar != 'N'):
                print('Opção Inválida')
                doencaCapilar = input('Informe S-Sim ou N-Não: ').upper()

            #Teste de doença capilar
            if (doencaCapilar == 'S'):
                print('Para doação os cabelos devem estar saudáveis.')
                doacoesPerdidas +=1

            else:
                armazenamento = input('Os fios foram guardados adequadamente (S/N)? ').upper()
                while (armazenamento != 'S' and armazenamento != 'N'):
                    print('Opção Inválida')
                    armazenamento = input('Informe S-Sim ou N-Não: ').upper()
                if (armazenamento == 'N'):
                    print('Para doação os cabelos devem ser armazenados limpos e secos em um saco plástico')
                    doacoesPerdidas +=1
    continuar = input('Deseja continuar o sistema(S/N) ? ').upper()
    while (continuar != 'S' and continuar != 'N'):
        print('Opção Inválida')
        continuar = input('Informe S-Sim ou N-Não: ').upper()
else:
    print ('\n\nApresentar os resultados finais\n\n')

print('Total de Doações:',totalDoadores)
print('Total de Doações Perdidas:', doacoesPerdidas)
print('Total de Doações Válidas:', totalDoadores-doacoesPerdidas)
print('Porcentagem de participantes do sexo Feminino: ', (totalFeminino*100)/totalDoadores, '%')
print('Porcentagem de participantes do sexo Masculino: ', (totalMasculino*100)/totalDoadores, '%')