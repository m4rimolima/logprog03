
nome = input('Digite seu nome: ')
disciplina = input('Digite a disciplína: ')
nota = float(input('Digite a sua nota: '))
if nota <0.0 or nota >10.0 :
    print("Nota invalida. Tente novamente ")
else:
    if 5.5  < nota <6.0 :
        nota = 6.0
    if nota >= 6.0:
        print (f'{nome} está aprovado em {disciplina} com a nota {nota}')
    else:
     print (f'{nome} está reprovado em {disciplina} com a nota {nota}')