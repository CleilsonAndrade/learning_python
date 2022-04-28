letra = str.upper(input('Digite F ou M: '))

if letra == 'F' or letra == 'M':
    if letra == 'F':
        print(f'Letra digitada {letra} sexo feminino')
    if letra == 'M':
        print(f'Letra digitada {letra} sexo masculino')
else:
    print(f'Letra digitada {letra} sexo invalido')
