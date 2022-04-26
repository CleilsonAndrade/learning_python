n1 = int(input('Digite a 1 nota: '))
n2 = int(input('Digite a 2 nota: '))

media = (n1+n2) / 2

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
