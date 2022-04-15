# 1 - Escreva um programa que pergunta a velocidade de um veículo. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$10 por km acima de 80km/h.

""" velocidade = float(input('Digite a velocidade km/h: '))
multa = (velocidade - 80) * 10

if(velocidade > 80):
  print(f'Você ultrapassou o limite de velocidade de 80km/h, valor da sua multa é de R${multa:,.2f}') """


# 2 -  Escreva um programa que leia três números e que imprima o maior e o menor.

""" n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
  maior = n2

if n3 > n1 and n3 > n2:
  maior = n3


if n2 < n1 and n2 < n3:
  menor = n2

if n3 < n1 and n3 < n2:
  menor = n3

print('O maior número é', maior)
print('O menor número é', menor) """


# 3 - Escreva um programa que receba dois números e pergunte qual operação você deseja realizar (soma, subtração, multiplicação e divisão). Exiba o resultado da operação.

""" n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
operacao = input('Digite qual a operação (+, -, * ou /) desejada: ')

if operacao == '+':
  print('A soma de', n1, '+', n2, 'é igual a', n1 + n2)
elif operacao == '-':
  print('A subtração de',n1, '-', n2, 'é igual a', n1 - n2)
elif operacao == '*':
  print('A multiplicação de',n1, '*', n2, 'é igual a', n1 * n2)
elif operacao == '/':
  print('A divisão de',n1, '/', n2, 'é igual a', n1 // n2) """
