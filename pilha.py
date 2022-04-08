prato = 10
pilha = list(range(1, ultimo + 1))

while True:
    print(f"Existem {len(pilha)} clientes na fila")
    print(f"Pilha atual: {fila}")
    print("Digite E para empilhar um prato, ")
    print("D para desempilhar ou S para Sair")
    operacao = input("Operação (E, D ou S): ")
    operacao = operacao.upper()
    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia! Nada para lavar!")
    elif operacao == "E":
        prato += 1
        pilha.append(prato)
    elif operacao == "S":
        print("Você preferiu SAIR!")
        break;
    else:
        print("Operação invalida ! Digite F, A ou S")
