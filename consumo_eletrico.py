qtdKWh = int(input('Qual a quantidade de KWh consumida: '))
tipInst = input('Qual o tipo de instalação "C" para Comercial ou "R" para residencial: ')

if tipInst == 'R':
    if qtdKWh <= 500:
        print(f"Valor a pagar é de ${qtdKWh * 0.8}")
    else:
        print(f"Valor a pagar é de ${qtdKWh * 0.95}")


if tipInst == 'C':
    if qtdKWh <= 1000:
        print(f"Valor a pagar é de ${qtdKWh * 1.10}")
    else:
        print(f"Valor a pagar é de ${qtdKWh * 1.30}")
