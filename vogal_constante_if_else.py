letra = str.upper(input('Digite uma letra: '))

if (letra == 'A' or letra == 'E') or (letra == 'I' or letra == 'O') or letra == 'U':
    print(f'{letra} é vogal!')
else:
    print(f'{letra} é constante!')
