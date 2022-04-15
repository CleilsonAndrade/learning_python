def soma(a,b):
    return a + b
def subtracao(a,b):
    return a - b

def imprime(a,b,funcao):
    print(funcao(a,b))

imprime(5,4,soma)
imprime(10,1,subtracao)
