with open('impares.txt', 'w') as impares:
    with open('par.txt', 'w') as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")
