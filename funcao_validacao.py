def faixa_int(valor,minimo,maximo):
    while True:
        v = int(input("Digite um valor: "))
        if v < minimo or v > maximo:
            print(f"Valor Invalido. Digite um valor entre {minimo} e {maximo}")
        else:
            return v
