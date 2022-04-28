n1 = int(input('Digite a 1º nota: '))
n2 = int(input('Digite a 2º nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print('Aprovado')
    if media == 10:
        print('Aprovado com Disitinção')
else:
    print('Reprovado')
