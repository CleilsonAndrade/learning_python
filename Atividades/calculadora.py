n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor:  '))

opcao = 0


def soma(a, b):
    return a+b


def subtracao(a, b):
    return a-b


def multiplicacao(a, b):
    return a*b


def divisao(a, b):
    return a/b


def potencia(a, b):
    return a**b


def imprime(a, b, funcao):
    if funcao.__name__ == 'soma':
        print(f'''        
                            {a} + {b} = {soma(a,b)}''')
    elif funcao.__name__ == 'subtracao':
        print(f'''        
                            {a} - {b} = {subtracao(a,b)}''')
    elif funcao.__name__ == 'multiplicacao':
        print(f'''        
                            {a} * {b} = {multiplicacao(a,b)}''')
    elif funcao.__name__ == 'divisao':
        print(f'''        
                            {a} / {b} = {divisao(a,b)}''')
    elif funcao.__name__ == 'potencia':
        print(f'''        
                            {a}^{b} = {potencia(a,b)}''')


while opcao != 6:
    print('''
    =======================Calculadora=======================
      [1] Somar
      [2] Subtração
      [3] Multiplicação
      [4] Divisão
      [5] Potência
      [6] Sair
    =========================================================
  ''')
    opcao = int(input('      Qual a opção que deseja escolher? '))
    if opcao == 1:
        imprime(n1, n2, soma)
    elif opcao == 2:
        imprime(n1, n2, subtracao)
    elif opcao == 3:
        imprime(n1, n2, multiplicacao)
    elif opcao == 4:
        imprime(n1, n2, divisao)
    elif opcao == 5:
        imprime(n1, n2, potencia)


print('Fim do programa! Volte sempre!')
