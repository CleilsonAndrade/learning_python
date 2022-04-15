altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / altura**2

print(f"Seu IMC é: {imc:,.2f}")

if imc < 18:
    print("Você está abaixo do peso!")
if imc >= 18.5 and imc <= 24.9:
    print("Seu peso é normal!")
if imc >= 25 and imc <= 29.9:
    print("Você está acima do peso!")
if imc >= 30 and imc <= 34.9:
    print("Você está com Obsidade Grau I")
if imc >= 35 and imc <= 39.9:
    print("Você esta com Obsidade Grau II")
if imc >= 40:
    print("Você está com Obsidade Grau III ou Mórbida!")
