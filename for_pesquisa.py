L = [1,3,5,7,11,13,17]
p = int(input("Digite o número que deve ser pesquisado: "))

for x in L:
    if x == p:
        print(f"Número {p} encontrado na lista!")
        break
else:
    print(f"Número {p} não encontrado")
