ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"Existem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila, ")
    print("A para realizar o atendimento ou S para Sair")
    operacao = input("Operação (F, A ou S): ")
    operacao = operacao.upper()
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia!")
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S":
        print("Você preferiu SAIR!")
        break;
    else:
        print("Operação invalida ! Digite F, A ou S")
