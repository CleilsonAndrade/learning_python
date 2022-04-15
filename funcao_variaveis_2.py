a = 5
def muda_e_imprime():
    global a
    a = 7
    print(f"Variavel a dentro da função: {a}")
print(f"variavel a antes de mudar: {a}")
muda_e_imprime()
print(f"variavel a depois de mudar: {a}")
