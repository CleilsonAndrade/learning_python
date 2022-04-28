n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

if n1 < n2:
    if n2 > n3:
        print(f'{n2} é o maior número!')
    else:
        print(f'{n3} é o maior número!') 
else:
    print(f'{n1} é o maior número!')
    
