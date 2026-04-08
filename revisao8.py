peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/altura**2

if imc > 25:
    print("Você está sobrepeso")
else: 
    print("Você está com o peso normal")