temperatura = float(input("digite a temperatura atual: "))

if temperatura <= 30:
    print("clima estavel")

    if temperatura > 30:
        print("Alerta de calor!")

umidade = float(input("digite a umidade: "))

if umidade < 40:
    print("Ação: ligar irrigação")
else:
    print("Ação: ligar somente os ventiladores")