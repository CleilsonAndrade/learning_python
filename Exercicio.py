qtdNomes = 1

while qtdNomes == 1:
    nome = input('Digite um nome: ')
    with open ('lista-nomes.txt', 'a') as listaNomes:
        listaNomes.write(f'{nome}\n')
        qtdNomes = int(input("Deseja colocar mais algum nome? 1 [SIM], 0 [NAO] "))
else:
    print('Lista de nomes finalizada!')
