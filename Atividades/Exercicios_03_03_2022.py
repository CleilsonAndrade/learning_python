# 1 - Criar um programa que recebe um número e imprime a tabuada desse número, até dez. No modelo: 2 x 1 = 2, 2 x 2 = 4, etc...

""" numero = int(input('Digite um número: '))

multiplicador = 0

while(multiplicador <= 10):
    print('A tabuada de', numero, 'x', multiplicador, ':', numero*multiplicador)
    multiplicador = multiplicador + 1 """


# 2 - Criar um programa que pergunta quantos números você quer utilizar, em seguida, recebe cada um dos números e imprime a média entre eles

""" qtdNumeros = int(input('Digite quantos números: '))
contador = 0
totNum = 0

while(contador < qtdNumeros):
    totNum = int(input('Digite o valor: '))
    totNum = totNum + totNum
    contador = contador + 1

print('A média de ', totNum, 'é igual a', totNum/qtdNumeros) """


# 3 - Criar um programa que recebe um depósito inicial e a taxa de juros mensal de uma aplicação e imprime os valores, mês a mês, para os 24 primeiros meses. Além disso, escreve o total ganho com os juros do período.

""" deposito = float(input("Digite o valor do depósito inicial: "))
taxa = float(input("Taxa de juros da aplicação (Exemplo: 10 para 10%): "))
mês = 1
saldo = deposito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1
print(f"O total de ganhos com os juros foi de R${saldo-deposito:8.2f}.") """
